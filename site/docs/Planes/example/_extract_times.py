#!/usr/bin/env python3
"""Pull the CLOCK TIMES for every overlap on the qualifying field-years.

There is no time column anywhere in overlaps.csv or flights.csv — only dates.
The times on these pages are therefore measured here, point by point, out of the
raw recovered ADS-B traces held in this repo under <TAIL>/data/recovered/, the
same files the AT_CLAIMED_AIRPORT verdicts were computed from.

For each (tail, claimed date, claimed field) it reports:
  * closest    the single recovered position nearest the field: UTC second,
               distance, altitude, and whether the aircraft reported on-ground
  * ground     every run of on-ground positions at that field, first and last
               UTC second

A DAY WITH NO TRACE PRODUCES NO TIME, and that is written out as such. A
volunteer network heard nothing; parked with the transponder off, outside
receiver coverage, and a wrong claimed date all look identical from here.

Writes _times.json beside this file.
"""
import csv, datetime as dt, json, os, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
PLANES = os.path.normpath(os.path.join(HERE, ".."))
FOLLOWING = os.path.join(PLANES, "following")
sys.path.insert(0, os.path.join(FOLLOWING, "apis", "public_open_source", "code", "lib"))

import traces as T                      # noqa: E402
from geo import airport_by_code, haversine_km, timezone_at   # noqa: E402

try:
    from zoneinfo import ZoneInfo
except ImportError:
    ZoneInfo = None

GROUND_GAP_SEC = 45 * 60    # same split threshold traces.py uses for a visit

overlaps = list(csv.DictReader(open(os.path.join(FOLLOWING, "overlaps.csv"))))

# The qualifying set: >=2 overlap rows at one field in one year AND Erika
# claimed present at that field at least twice that year.
groups = defaultdict(list)
for r in overlaps:
    if not r["airport_code"] or r["date"] == "UNKNOWN":
        continue
    groups[(r["airport_code"], r["date"][:4])].append(r)
qualifying = {k: v for k, v in groups.items()
              if len(v) >= 2 and len([r for r in v if r["erika_present"] == "claimed"]) >= 2}

# Index every recovered trace on disk by (tail, date).
by_key = defaultdict(list)
for tail, date, source, path in T.trace_files():
    by_key[(tail, date)].append((source, path))

def local(iso_utc, tz):
    if not tz or ZoneInfo is None:
        return None
    t = dt.datetime.fromisoformat(iso_utc.replace("Z", "+00:00")).astimezone(ZoneInfo(tz))
    return t.strftime("%H:%M:%S") + " " + t.tzname()

out = {}
for (code, year), items in sorted(qualifying.items()):
    ap = airport_by_code(code)
    # Pass the state so the resolver can fall back to its state table:
    # timezonefinder is not installed here, and all six fields sit in states
    # with a single unambiguous zone, so the fallback is exact for this set.
    state = items[0]["state"]
    tz, tz_method = timezone_at(ap["lat"], ap["lon"], state) if ap else (None, "no_airport")
    for r in items:
        tails = [t.strip() for t in r["foreign_tail"].split(";")
                 if t.strip() and t.strip() != "UNKNOWN"]
        rec = {"overlap_id": r["overlap_id"], "date": r["date"], "airport": code,
               "tz": tz, "tz_method": tz_method, "tails": tails, "per_tail": {}}
        for tail in tails:
            files = by_key.get((tail, r["date"]), [])
            info = {"sources": sorted({s for s, _ in files}), "closest": None,
                    "ground": [], "points": 0, "unreadable": []}
            best, ground_pts = None, []
            for source, path in files:
                try:
                    with T.open_trace(path) as fh:
                        doc = json.load(fh)
                except (OSError, ValueError, EOFError) as exc:
                    info["unreadable"].append("%s: %s" % (source, type(exc).__name__))
                    continue
                for p in (doc.get("trace") or []):
                    try:
                        secs, lat, lon, alt = p[0], p[1], p[2], p[3]
                    except (IndexError, TypeError):
                        continue
                    if lat is None or lon is None:
                        continue
                    info["points"] += 1
                    km = haversine_km(lat, lon, ap["lat"], ap["lon"])
                    on_ground = (alt == "ground")
                    iso = T._iso(r["date"], secs)
                    cand = {"km": round(km, 2), "utc": iso, "on_ground": on_ground,
                            "alt_ft": None if on_ground else alt, "source": source}
                    # CLOSEST WINS; on-ground only breaks a tie. Ranking any
                    # on-ground point above any airborne one — which an earlier
                    # draft of this script did — picked a parked position 2,827
                    # km away at Provo over a 1.56 km pass at the claimed field
                    # and silently contradicted overlaps.csv on three rows.
                    if best is None or (km, not on_ground) < (best["km"], not best["on_ground"]):
                        best = cand
                    if on_ground and km <= 8.0:
                        ground_pts.append((iso, km))
            info["closest"] = best
            ground_pts.sort()
            runs = []
            for iso, km in ground_pts:
                t = dt.datetime.fromisoformat(iso.replace("Z", "+00:00"))
                if runs and (t - runs[-1]["_last_t"]).total_seconds() <= GROUND_GAP_SEC:
                    runs[-1].update(last=iso, _last_t=t)
                    runs[-1]["n"] += 1
                    runs[-1]["kms"].append(km)
                else:
                    runs.append({"first": iso, "last": iso, "_last_t": t, "n": 1, "kms": [km]})
            for run in runs:
                run.pop("_last_t")
                run["median_km"] = round(sorted(run["kms"])[len(run["kms"]) // 2], 2)
                run.pop("kms")
                run["first_local"] = local(run["first"], tz)
                run["last_local"] = local(run["last"], tz)
            info["ground"] = runs
            if best:
                best["local"] = local(best["utc"], tz)
            rec["per_tail"][tail] = info
        out[r["overlap_id"]] = rec

json.dump(out, open(os.path.join(HERE, "_times.json"), "w"), indent=1, sort_keys=True)
n_time = sum(1 for v in out.values()
             if any(t["closest"] for t in v["per_tail"].values()))
n_ground = sum(1 for v in out.values()
               if any(t["ground"] for t in v["per_tail"].values()))
print("overlaps on qualifying field-years: %d | with a recovered position: %d | "
      "with on-ground positions at the claimed field: %d"
      % (len(out), n_time, n_ground))
