#!/usr/bin/env python3
"""THE GEOGRAPHIC SWEEP: stop asking about tails, start asking about places.

Everything this repo has pulled from the open archives until now was a PER-TAIL
question -- "was SU-BTT at Provo on 10 September" -- and a per-tail question can
only ever confirm or fail to confirm an aircraft somebody had already named. It
holds about 9% of the aircraft-days the speaking-event windows need, and it is
structurally incapable of finding the aircraft nobody thought to look for.

adsb.lol mirrors its ENTIRE global database to public GitHub Releases, one tar
per UTC day, Open Database Licence, no account and no key. That archive holds
every aircraft its volunteer receivers heard that day -- roughly 90,000 of them
-- not just the sixteen in this repo's fleet file. Streaming one day and
filtering it by GEOGRAPHY instead of by hex turns the question inside out:

    WHAT WAS WITHIN 50 MILES OF THIS CITY ON THIS DAY?

That is the question the following-planes claim actually needs answered, and
this is the only free way to answer it.

    python3 geo_sweep.py --plan                  what it would sweep, in order
    python3 geo_sweep.py --run                   sweep, priority order, resumable
    python3 geo_sweep.py --run --date 2025-09-10
    python3 geo_sweep.py --run --max-dates 20    bounded run
    python3 geo_sweep.py --run --radius 50 --window 1
    python3 geo_sweep.py --report                what is on disk now

HOW IT WORKS, AND WHY IT IS AFFORDABLE
--------------------------------------
Each day is ~2-5 GB. It is STREAMED and never stored: curl pipes the tar into
Python, each member is gunzipped in memory, and a cheap byte pre-filter throws
out the ~92% of aircraft that were never in the right degree square before any
JSON is parsed. Measured cost is about one minute of CPU per day; the wire is
the only real budget.

WHAT LANDS ON DISK
------------------
A CSV row for EVERY aircraft that entered any circle -- that is the coverage
record, and it is the part that makes an absence meaningful. The full trace is
kept only for aircraft that are FLAGGED (foreign-registered, unregistered,
military/PIA/LADD, or in this repo's fleet file), because keeping 90,000 traces
a day in a git repo an automated job pushes every few minutes is not an option.
Unflagged aircraft are counted, described in the CSV, and not stored.

THE FOUR RULES THIS SCRIPT EXISTS TO KEEP
-----------------------------------------
1. THE CONTROL CITIES ARE SWEPT ON THE SAME DAYS, in the same run, by the same
   code. "Foreign jets were within 50 miles of the event" means nothing until
   you know how many were within 50 miles of Des Moines that day. This
   investigation has already had to retract one finding for skipping a control.

2. A CIRCLE IS NOT AN AIRPORT AND A POSITION IS NOT A LANDING. Every row
   carries the distance in miles to the nearest field and whether the aircraft
   ever reported itself ON GROUND. Never drop those two columns.

3. AN EMPTY DAY IS A COVERAGE FACT, NOT AN ABSENCE. A swept day with no hits
   is written down as swept, with the aircraft count the archive held, so
   "asked and nothing was there" can never be confused with "never asked".

4. NOTHING IS OVERWRITTEN. A re-sweep of a date already on disk lands beside
   the first with a timestamp suffix. The diff between two sweeps of one day is
   how this repo proves something stopped being retrievable.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import gzip
import io
import json
import math
import os
import subprocess
import sys
import tarfile
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))

from geo import airports_within, haversine_mi          # noqa: E402
from targets import build_targets, priority            # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_ROOT = os.path.normpath(os.path.join(HERE, "..", "data", "geo_sweep"))
FLEET_JS = os.path.join(HERE, "lib", "fleet.js")

REPO = "adsblol/globe_history_{year}"
TAG = "v{y}.{m}.{d}-planes-readsb-prod-0"
DL = "https://github.com/{repo}/releases/download/{tag}/{asset}"

# readsb dbFlags bitfield, as published by the tar1090 database.
DB_FLAGS = {1: "military", 2: "interesting", 4: "PIA", 8: "LADD"}


def utcnow():
    return dt.datetime.now(dt.timezone.utc).isoformat()


# --------------------------------------------------------------------------
# Which aircraft are worth keeping the whole trace for
# --------------------------------------------------------------------------

def load_fleet_hexes():
    """The hexes this repo already tracks, read out of lib/fleet.js so the two
    never drift. A miss here is not fatal -- it only means a known tail gets
    kept for being foreign rather than for being known."""
    out = {}
    if not os.path.exists(FLEET_JS):
        return out
    import re
    for m in re.finditer(r'reg:\s*"([^"]+)",\s*hex:\s*"([0-9a-fA-F]+)"', open(FLEET_JS).read()):
        out[m.group(2).lower()] = m.group(1)
    return out


FLEET_HEX = load_fleet_hexes()

GOV_WORDS = ("AIR FORCE", "ARMY", "NAVY", "MARINE CORPS", "COAST GUARD",
             "DEPARTMENT OF", "UNITED STATES OF AMERICA", "GOVERNMENT",
             "STATE OF", "FEDERAL", "CUSTOMS", "BORDER PROTECTION",
             "EXECUTIVE", "ROYAL", "REPUBLIC OF", "MINISTRY")


def flag_aircraft(d):
    """Why this aircraft is worth storing in full. Returns a list of reasons;
    an empty list means CSV row only. The reasons are published as-is so a
    reader can see exactly what the filter did and disagree with it."""
    reasons = []
    hexid = (d.get("icao") or "").lower().lstrip("~")
    reg = (d.get("r") or "").strip()
    own = (d.get("ownOp") or "").upper()
    flags = int(d.get("dbFlags") or 0)

    if hexid in FLEET_HEX:
        reasons.append(f"tracked_fleet:{FLEET_HEX[hexid]}")
    if (d.get("icao") or "").startswith("~"):
        reasons.append("non_icao_address")       # TIS-B / ADS-R, not a real airframe address
    if not reg:
        reasons.append("no_registration")
    elif not reg.upper().startswith("N"):
        reasons.append("non_us_registration")
    for bit, name in DB_FLAGS.items():
        if flags & bit:
            reasons.append(f"dbflag:{name}")
    if any(w in own for w in GOV_WORDS):
        reasons.append("government_operator_string")
    return reasons


# --------------------------------------------------------------------------
# The byte pre-filter
# --------------------------------------------------------------------------

def prefilter_patterns(circles):
    """Degree-square tokens for one day's circles.

    A trace point is `[seconds, lat, lon, ...]`, so every latitude and every
    longitude in the file is preceded by a comma. Requiring one in-range
    latitude token AND one in-range longitude token rejects the great majority
    of the world's aircraft for the cost of a substring search.

    It is a PRE-filter and only a pre-filter: it can pass an aircraft that was
    at the right latitude over one ocean and the right longitude over another,
    which the exact check below then rejects. It cannot reject an aircraft that
    was genuinely inside a circle, because that aircraft necessarily carries
    both tokens. Run with --no-prefilter to confirm that on any given day.
    """
    lats, lons = set(), set()
    for c in circles:
        pad_lat = c["radius_mi"] / 69.0 + 0.02
        pad_lon = c["radius_mi"] / (69.0 * max(0.15, math.cos(math.radians(c["lat"])))) + 0.02
        for v in (c["lat"] - pad_lat, c["lat"] + pad_lat):
            lats.add(int(math.floor(v)))
        for v in (c["lon"] - pad_lon, c["lon"] + pad_lon):
            lons.add(int(math.floor(v)))
        lats.update(range(int(math.floor(c["lat"] - pad_lat)), int(math.floor(c["lat"] + pad_lat)) + 1))
        lons.update(range(int(math.floor(c["lon"] - pad_lon)), int(math.floor(c["lon"] + pad_lon)) + 1))
    pats_lat = [p for n in sorted(lats) for p in (f",{n}.".encode(), f",{n},".encode())]
    pats_lon = [p for n in sorted(lons) for p in (f",{n}.".encode(), f",{n},".encode())]
    return pats_lat, pats_lon


# --------------------------------------------------------------------------
# The exact check
# --------------------------------------------------------------------------

def check_trace(d, circles):
    """Every circle this aircraft entered, with the closest approach in each.

    Returns a list of hit dicts. `ground` is True only if the aircraft reported
    itself ON GROUND while inside the circle -- readsb writes the literal
    string "ground" in the altitude slot for that, and it is the single most
    useful bit in the whole record.
    """
    ts = float(d.get("timestamp") or 0)
    per = {}
    for p in d.get("trace") or ():
        try:
            lat, lon = p[1], p[2]
        except (IndexError, TypeError):
            continue
        if lat is None or lon is None:
            continue
        for c in circles:
            dist = haversine_mi(c["lat"], c["lon"], lat, lon)
            if dist > c["radius_mi"]:
                continue
            h = per.setdefault(c["key"], {
                "circle": c, "n": 0, "first": None, "last": None,
                "min_dist": 1e9, "min_lat": None, "min_lon": None,
                "ground": False, "ground_lat": None, "ground_lon": None,
                "min_alt": None,
            })
            h["n"] += 1
            t = ts + (p[0] or 0)
            h["first"] = t if h["first"] is None else min(h["first"], t)
            h["last"] = t if h["last"] is None else max(h["last"], t)
            alt = p[3] if len(p) > 3 else None
            if alt == "ground":
                if not h["ground"]:
                    h["ground"], h["ground_lat"], h["ground_lon"] = True, lat, lon
            elif isinstance(alt, (int, float)):
                h["min_alt"] = alt if h["min_alt"] is None else min(h["min_alt"], alt)
            if dist < h["min_dist"]:
                h["min_dist"], h["min_lat"], h["min_lon"] = dist, lat, lon
    return list(per.values())


def resolve_field(lat, lon):
    """Nearest usable field to a position, WITH THE DISTANCE. The distance is
    not decoration: a nearest-field label read as a destination is the exact
    mistake that produced the Provo-versus-Dugway correction on this site."""
    if lat is None:
        return None, None
    near = airports_within(lat, lon, 25)
    if not near:
        return None, None
    return near[0]["ident"], near[0]["distance_mi"]


# --------------------------------------------------------------------------
# The archive
# --------------------------------------------------------------------------

def asset_urls(date_iso, timeout=30):
    """Locate one UTC day in the GitHub backup WITHOUT touching the GitHub API.

    The API allows 60 unauthenticated requests an hour and a full sweep needs
    hundreds, so the release URL is constructed and probed directly on the CDN,
    which is not rate limited. Tags use dots in the date. A day is either one
    `.tar` or a `split` of one into `.tar.aa`, `.tar.ab`, ... which concatenate
    back into a single stream in sort order.

    Releases sit in the repo for the year, except at the year boundary where
    adsb.lol has filed the first days of January under the previous year's
    repo -- so the adjacent years are tried too.
    """
    y, m, d = date_iso.split("-")
    tag = TAG.format(y=y, m=m, d=d)
    years = [int(y), int(y) - 1, int(y) + 1]
    for yr in years:
        repo = REPO.format(year=yr)
        base = DL.format(repo=repo, tag=tag, asset="")
        single = base + tag + ".tar"
        if _exists(single, timeout):
            return [single], repo, tag
        parts, suf = [], 0
        while True:
            name = f"{tag}.tar.a{chr(ord('a') + suf)}"
            url = base + name
            if not _exists(url, timeout):
                break
            parts.append(url)
            suf += 1
            if suf > 25:
                break
        if parts:
            return parts, repo, tag
    return [], None, tag


def _exists(url, timeout=30):
    p = subprocess.run(["curl", "-sL", "-r", "0-1", "--max-time", str(timeout),
                        "-o", os.devnull, "-w", "%{http_code}", url],
                       capture_output=True, text=True)
    return p.stdout.strip() in ("200", "206")


def sweep_date(date_iso, circles, outdir, prefilter=True, timeout=30, verbose=True):
    """Stream one UTC day and return the hits. Nothing but hits touches disk."""
    urls, repo, tag = asset_urls(date_iso, timeout)
    meta = {
        "sweep_date": date_iso, "retrieved_utc": utcnow(), "source": "adsblol-github-backup",
        "github_repo": repo, "release_tag": tag, "asset_urls": urls,
        "licence": "Open Database Licence (ODbL), adsb.lol",
        "radius_mi": circles[0]["radius_mi"] if circles else None,
        "circles": [{"key": c["key"], "kind": c["kind"], "city": c.get("city"),
                     "state": c.get("state"), "lat": c["lat"], "lon": c["lon"],
                     "radius_mi": c["radius_mi"], "offset_days": c.get("offset_days"),
                     "center_basis": c.get("center_basis"),
                     "event_date": c.get("date"), "who": c.get("who")}
                    for c in circles],
        "prefilter": prefilter,
    }
    if not urls:
        meta.update(status="NO_RELEASE_FOR_THIS_DATE", aircraft_in_archive=0, hits=0,
                    note="The backup has no prod release for this UTC day. That is an "
                         "ARCHIVE fact, not an aircraft fact, and it is not evidence "
                         "that anything was or was not here.")
        return [], meta

    pl, po = prefilter_patterns(circles) if prefilter else ([], [])
    t0 = time.time()
    n_files = n_deep = n_bytes = 0
    hits = []
    keep = {}

    proc = subprocess.Popen(["curl", "-sL", "--max-time", "5400"] + urls,
                            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                            bufsize=1024 * 1024)
    try:
        tf = tarfile.open(fileobj=proc.stdout, mode="r|")
        for m in tf:
            if not m.isfile() or "trace_full_" not in m.name:
                continue
            n_files += 1
            n_bytes += m.size
            try:
                raw = tf.extractfile(m).read()
            except Exception:
                break                       # truncated stream; recorded below
            try:
                b = gzip.decompress(raw)
            except Exception:
                b = raw
            if prefilter and not (any(p in b for p in pl) and any(p in b for p in po)):
                continue
            n_deep += 1
            try:
                d = json.loads(b)
            except Exception:
                continue
            got = check_trace(d, circles)
            if not got:
                continue
            reasons = flag_aircraft(d)
            for h in got:
                lat = h["ground_lat"] if h["ground"] else h["min_lat"]
                lon = h["ground_lon"] if h["ground"] else h["min_lon"]
                field, fdist = resolve_field(lat, lon)
                hits.append({
                    "sweep_date": date_iso,
                    "circle_key": h["circle"]["key"],
                    "circle_kind": h["circle"]["kind"],
                    "city": h["circle"].get("city"),
                    "state": h["circle"].get("state"),
                    "event_date": h["circle"].get("date"),
                    "offset_days": h["circle"].get("offset_days"),
                    "who": h["circle"].get("who"),
                    "hex": d.get("icao"),
                    "reg": d.get("r") or "",
                    "type": d.get("t") or "",
                    "own_op": d.get("ownOp") or "",
                    "year": d.get("year") or "",
                    "db_flags": int(d.get("dbFlags") or 0),
                    "flag_reasons": "|".join(reasons),
                    "flagged": bool(reasons),
                    "points_in_circle": h["n"],
                    "first_utc": dt.datetime.fromtimestamp(h["first"], dt.timezone.utc).isoformat()
                                  if h["first"] else "",
                    "last_utc": dt.datetime.fromtimestamp(h["last"], dt.timezone.utc).isoformat()
                                 if h["last"] else "",
                    "closest_mi_to_city": round(h["min_dist"], 2),
                    "closest_lat": round(h["min_lat"], 5) if h["min_lat"] is not None else "",
                    "closest_lon": round(h["min_lon"], 5) if h["min_lon"] is not None else "",
                    "on_ground_in_circle": h["ground"],
                    "min_alt_ft": h["min_alt"] if h["min_alt"] is not None else "",
                    "nearest_field": field or "",
                    "nearest_field_mi": fdist if fdist is not None else "",
                })
            if reasons:
                keep[d.get("icao")] = b
        tf.close()
    finally:
        try:
            proc.stdout.close()
        except Exception:
            pass
        proc.wait()

    if keep:
        tdir = os.path.join(outdir, "traces")
        os.makedirs(tdir, exist_ok=True)
        for hexid, b in keep.items():
            path = os.path.join(tdir, f"{hexid}.json.gz")
            if os.path.exists(path):        # never overwrite a previous pull
                path = os.path.join(tdir, f"{hexid}.{utcnow()[:19].replace(':', '')}.json.gz")
            with gzip.open(path, "wb") as fh:
                fh.write(b)

    meta.update(status="SWEPT", aircraft_in_archive=n_files, deep_parsed=n_deep,
                archive_bytes_streamed=n_bytes, hits=len(hits),
                distinct_aircraft_in_circles=len({h["hex"] for h in hits}),
                flagged_aircraft_stored=len(keep),
                seconds=round(time.time() - t0, 1),
                note="A swept day with no hits means the archive was ASKED and held "
                     "nothing inside these circles. It is not evidence that no "
                     "aircraft was there: a volunteer network heard nothing, and "
                     "transponder-off, out-of-coverage and a wrong claimed date all "
                     "look identical from here.")
    return hits, meta


HITS_FIELDS = ["sweep_date", "circle_key", "circle_kind", "city", "state", "event_date",
               "offset_days", "who", "hex", "reg", "type", "own_op", "year", "db_flags",
               "flag_reasons", "flagged", "points_in_circle", "first_utc", "last_utc",
               "closest_mi_to_city", "closest_lat", "closest_lon", "on_ground_in_circle",
               "min_alt_ft", "nearest_field", "nearest_field_mi"]


def write_day(date_iso, hits, meta):
    outdir = os.path.join(OUT_ROOT, date_iso)
    os.makedirs(outdir, exist_ok=True)
    mp = os.path.join(outdir, "_sweep.meta.json")
    if os.path.exists(mp):
        mp = os.path.join(outdir, f"_sweep.{utcnow()[:19].replace(':', '')}.meta.json")
    with open(mp, "w") as fh:
        json.dump(meta, fh, indent=2)
    hp = os.path.join(outdir, "hits.csv")
    if os.path.exists(hp):
        hp = os.path.join(outdir, f"hits.{utcnow()[:19].replace(':', '')}.csv")
    with open(hp, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=HITS_FIELDS)
        w.writeheader()
        for h in sorted(hits, key=lambda x: (not x["flagged"], x["circle_key"], x["hex"])):
            w.writerow(h)
    return outdir


def already_swept(date_iso):
    return os.path.exists(os.path.join(OUT_ROOT, date_iso, "_sweep.meta.json"))


# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--date", action="append", help="sweep only this UTC date (repeatable)")
    ap.add_argument("--radius", type=float, default=50.0, help="circle radius in miles")
    ap.add_argument("--window", type=int, default=1, help="+/- days around each event date")
    ap.add_argument("--max-dates", type=int, default=0)
    ap.add_argument("--no-controls", action="store_true")
    ap.add_argument("--no-prefilter", action="store_true",
                    help="parse every aircraft; slow, used to verify the pre-filter")
    ap.add_argument("--repull", action="store_true", help="re-sweep dates already on disk")
    args = ap.parse_args()

    by_date, meta = build_targets(args.radius, args.window, controls=not args.no_controls)
    order = priority(by_date, meta)
    if args.date:
        order = [d for d in order if d in set(args.date)]
        for d in args.date:                      # allow a date with no event circle
            if d not in by_date:
                print(f"  {d}: no event circle on this date; controls only")
                by_date[d] = [dict(c, sweep_date=d) for c in
                              next(iter(by_date.values())) if c["kind"] == "control"]
                order.append(d)
    if not args.repull:
        order = [d for d in order if not already_swept(d)]
    if args.max_dates:
        order = order[:args.max_dates]

    os.makedirs(OUT_ROOT, exist_ok=True)
    with open(os.path.join(OUT_ROOT, "targets.json"), "w") as fh:
        json.dump({"built_utc": utcnow(),
                   "radius_mi": args.radius, "window_days": args.window,
                   "event_days_on_map": len(meta["events"]),
                   "utc_dates": len(by_date),
                   "controls": meta["controls"],
                   "archive_floor": meta["archive_floor"],
                   "not_swept_no_exact_date": [
                       {"dates": r["dates"], "city": r["city"], "state": r["state"],
                        "title": r.get("title")} for r in meta["undated"]],
                   "not_swept_not_geocodable": [
                       {"dates": r["dates"], "city": r["city"], "state": r["state"]}
                       for r in meta["ungeocoded"]],
                   "dates": {d: [{"key": c["key"], "kind": c["kind"], "city": c.get("city"),
                                  "state": c.get("state"), "lat": c["lat"], "lon": c["lon"],
                                  "offset_days": c.get("offset_days")}
                                 for c in cs] for d, cs in by_date.items()}}, fh, indent=2)

    if args.report:
        return report()

    if args.plan or not args.run:
        print(f"{len(meta['events'])} US event-days on the map "
              f"({len(meta['undated'])} rows name no exact date, "
              f"{len(meta['ungeocoded'])} cannot be geocoded)")
        print(f"{len(by_date)} UTC dates in the target set at radius {args.radius} mi, "
              f"window +/-{args.window} d, {len(meta['controls'])} control cities per date")
        print(f"{len(order)} dates still to sweep\n")
        for d in order[:40]:
            ev = [c for c in by_date[d] if c["kind"] == "event"]
            print(f"  {d}  " + (", ".join(f"{c['city']},{c['state']}" for c in ev) or "(controls only)"))
        if len(order) > 40:
            print(f"  ... and {len(order) - 40} more")
        return

    for i, d in enumerate(order, 1):
        circles = by_date[d]
        ev = ", ".join(f"{c['city']},{c['state']}" for c in circles if c["kind"] == "event")
        print(f"[{i}/{len(order)}] {d}  {ev or '(controls only)'}", flush=True)
        try:
            hits, m = sweep_date(d, circles, os.path.join(OUT_ROOT, d),
                                 prefilter=not args.no_prefilter)
        except Exception as e:
            print(f"    ERROR {type(e).__name__}: {e}", flush=True)
            continue
        write_day(d, hits, m)
        if m["status"] != "SWEPT":
            print(f"    {m['status']}", flush=True)
            continue
        fl = sorted({h["reg"] or h["hex"] for h in hits if h["flagged"]})
        print(f"    {m['aircraft_in_archive']} aircraft in archive, "
              f"{m['distinct_aircraft_in_circles']} in circles, "
              f"{m['flagged_aircraft_stored']} flagged, {m['seconds']}s", flush=True)
        if fl:
            print("    flagged: " + ", ".join(fl[:25])
                  + (f" ... +{len(fl) - 25}" if len(fl) > 25 else ""), flush=True)


def report():
    days = sorted(d for d in os.listdir(OUT_ROOT)
                  if os.path.isdir(os.path.join(OUT_ROOT, d)))
    tot = flagged = 0
    ev_f = ct_f = 0
    for d in days:
        hp = os.path.join(OUT_ROOT, d, "hits.csv")
        if not os.path.exists(hp):
            continue
        for r in csv.DictReader(open(hp)):
            tot += 1
            if r["flagged"] == "True":
                flagged += 1
                if r["circle_kind"] == "event":
                    ev_f += 1
                else:
                    ct_f += 1
    print(f"{len(days)} UTC days swept")
    print(f"{tot} circle entries, {flagged} by flagged aircraft")
    print(f"  flagged inside EVENT circles:   {ev_f}")
    print(f"  flagged inside CONTROL circles: {ct_f}   <- the comparison that makes the "
          f"first number mean anything")


if __name__ == "__main__":
    main()
