#!/usr/bin/env python3
"""Second-by-second reconstruction of the 8-12 September 2025 Provo window,
built from the RAW recovered ADS-B traces on disk and from nothing else.

    python3 provo_window_reconstruct.py            # full report to stdout
    python3 provo_window_reconstruct.py --json     # machine-readable

WHAT IT DOES
------------
For every tail with a recovered `*_trace_full.json[.gz]` payload dated
2025-09-08 .. 2025-09-12 it reports, PER SOURCE ARCHIVE:

  * first fix / last fix (UTC, to the millisecond the archive published)
  * every air<->ground transition, i.e. wheels-up and wheels-down, with the
    nearest field to the transition point and the distance to it
  * every ground visit: nearest airport, MEDIAN distance in km from that
    field, ground-point count, first/last UTC, duration
  * the routing as an ordered ground-visit chain
  * max altitude and max ground speed seen in the day

and then DIFFS the two archives (adsb-lol vs airplanes-live) for the same
aircraft-day at the level of the individual position report: how many
timestamps each holds, how many are shared, and whether any shared timestamp
carries a different latitude/longitude/altitude.

WHAT IT DOES NOT DO
-------------------
It does not make a network request. It does not infer occupancy or purpose. A
ground contact says an airframe transmitted an on-ground position near a field;
it does not say who was aboard, why, or that anyone boarded at all. A DAY WITH
NO TRACE IS NOT AN ABSENCE - it means a volunteer receiver network published
nothing for that airframe-day, and parked-with-the-transponder-off,
outside-coverage and a wrong claimed date all look identical from here.
"""
from __future__ import annotations

import argparse
import datetime as dt
import glob
import gzip
import json
import os
import re
import statistics
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
from geo import haversine_km, nearest_airport  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
PLANES = os.path.normpath(os.path.join(HERE, "..", "..", "..", ".."))

DAYS = ["2025-09-08", "2025-09-09", "2025-09-10", "2025-09-11", "2025-09-12"]
VISIT_GAP_SEC = 45 * 60
NAME_RE = re.compile(
    r"^(?P<tail>[A-Z0-9-]+)_(?P<date>\d{4}-\d{2}-\d{2})_(?P<source>[a-z0-9-]+)"
    r"_trace_full\.json(?P<gz>\.gz)?$")


def iso(day, secs):
    base = dt.datetime.strptime(day, "%Y-%m-%d").replace(tzinfo=dt.timezone.utc)
    return (base + dt.timedelta(seconds=float(secs))).isoformat().replace("+00:00", "Z")


def load(path):
    opener = gzip.open if path.endswith(".gz") else open
    with opener(path, "rt", encoding="utf-8") as fh:
        return json.load(fh)


def field(lat, lon):
    ap = nearest_airport(lat, lon, radius_mi=30)
    if not ap:
        return None, None
    return ap["ident"], round(haversine_km(lat, lon, ap["lat"], ap["lon"]), 2)


def analyse(path, day):
    doc = load(path)
    pts = [p for p in (doc.get("trace") or []) if len(p) >= 4 and p[1] is not None]
    out = {
        "file": os.path.relpath(path, PLANES),
        "registration": doc.get("r"), "type": doc.get("t"),
        "icao": doc.get("icao"), "points": len(pts),
    }
    if not pts:
        return out
    out["first_fix_utc"] = iso(day, pts[0][0])
    out["last_fix_utc"] = iso(day, pts[-1][0])
    out["first_pos"] = [pts[0][1], pts[0][2]]
    out["last_pos"] = [pts[-1][1], pts[-1][2]]
    out["first_alt"] = pts[0][3]
    out["last_alt"] = pts[-1][3]
    alts = [p[3] for p in pts if isinstance(p[3], (int, float))]
    gs = [p[4] for p in pts if len(p) > 4 and isinstance(p[4], (int, float))]
    out["max_alt_ft"] = max(alts) if alts else None
    out["max_gs_kt"] = max(gs) if gs else None

    # --- transitions -------------------------------------------------------
    trans = []
    prev = None
    for p in pts:
        state = "ground" if p[3] == "ground" else "air"
        if prev is not None and state != prev[0]:
            code, km = field(p[1], p[2])
            trans.append({
                "kind": "wheels_up" if state == "air" else "wheels_down",
                "utc": iso(day, p[0]),
                "prev_fix_utc": iso(day, prev[1]),
                "lat": p[1], "lon": p[2],
                "nearest_field": code, "km_from_field": km,
            })
        prev = (state, p[0])
    out["transitions"] = trans

    # --- ground visits -----------------------------------------------------
    ground = [(p[0], p[1], p[2]) for p in pts if p[3] == "ground"]
    runs, run = [], []
    for pt in ground:
        if run and pt[0] - run[-1][0] > VISIT_GAP_SEC:
            runs.append(run)
            run = []
        run.append(pt)
    if run:
        runs.append(run)
    visits = []
    for r in runs:
        mlat = statistics.median(p[1] for p in r)
        mlon = statistics.median(p[2] for p in r)
        ap = nearest_airport(mlat, mlon, radius_mi=30)
        dists = [haversine_km(p[1], p[2], ap["lat"], ap["lon"]) for p in r] if ap else []
        visits.append({
            "airport_code": ap["ident"] if ap else None,
            "airport_name": ap["name"] if ap else None,
            "airport_city": ap.get("municipality") if ap else None,
            "median_km_from_field": round(statistics.median(dists), 3) if dists else None,
            "min_km": round(min(dists), 3) if dists else None,
            "max_km": round(max(dists), 3) if dists else None,
            "first_seen_utc": iso(day, r[0][0]),
            "last_seen_utc": iso(day, r[-1][0]),
            "seconds_on_ground_observed": round(r[-1][0] - r[0][0], 2),
            "ground_points": len(r),
            "median_lat": round(mlat, 6), "median_lon": round(mlon, 6),
        })
    out["ground_visits"] = visits
    return out


def diff_sources(a, b, day):
    """Point-level diff of two archives for the same aircraft-day."""
    da, db = load(a), load(b)
    ta = {round(float(p[0]), 3): p for p in (da.get("trace") or []) if len(p) >= 4}
    tb = {round(float(p[0]), 3): p for p in (db.get("trace") or []) if len(p) >= 4}
    shared = sorted(set(ta) & set(tb))
    mism = []
    for t in shared:
        pa, pb = ta[t], tb[t]
        if pa[1] != pb[1] or pa[2] != pb[2] or pa[3] != pb[3]:
            mism.append({"utc": iso(day, t),
                         "a": [pa[1], pa[2], pa[3]], "b": [pb[1], pb[2], pb[3]]})
    only_a = sorted(set(ta) - set(tb))
    only_b = sorted(set(tb) - set(ta))
    return {
        "points_a": len(ta), "points_b": len(tb), "shared": len(shared),
        "only_a": len(only_a), "only_b": len(only_b),
        "value_mismatches": len(mism), "mismatch_examples": mism[:5],
        "only_a_first_utc": iso(day, only_a[0]) if only_a else None,
        "only_a_last_utc": iso(day, only_a[-1]) if only_a else None,
        "only_b_first_utc": iso(day, only_b[0]) if only_b else None,
        "only_b_last_utc": iso(day, only_b[-1]) if only_b else None,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    paths = (glob.glob(os.path.join(PLANES, "*", "data", "recovered", "*_trace_full.json"))
             + glob.glob(os.path.join(PLANES, "*", "data", "recovered", "*_trace_full.json.gz")))
    by = {}
    for p in sorted(paths):
        m = NAME_RE.match(os.path.basename(p))
        if not m or m.group("date") not in DAYS:
            continue
        key = (m.group("tail").upper(), m.group("date"))
        by.setdefault(key, {}).setdefault(m.group("source"), []).append(p)

    report = {}
    for (tail, day), srcs in sorted(by.items()):
        rec = report.setdefault(tail, {}).setdefault(day, {"sources": {}, "diff": None})
        for src, files in sorted(srcs.items()):
            rec["sources"][src] = [analyse(f, day) for f in sorted(files)]
        if "adsb-lol" in srcs and "airplanes-live" in srcs:
            rec["diff"] = diff_sources(sorted(srcs["adsb-lol"])[0],
                                       sorted(srcs["airplanes-live"])[0], day)

    # miss records inside the window
    miss = {}
    for p in glob.glob(os.path.join(PLANES, "*", "data", "recovered",
                                    "*_trace_full.miss.json.meta.json")):
        b = os.path.basename(p)
        mm = re.match(r"^(?P<tail>[A-Z0-9-]+)_(?P<date>\d{4}-\d{2}-\d{2})_"
                      r"(?P<source>[a-z0-9-]+)_trace_full\.miss\.json\.meta\.json$", b)
        if mm and mm.group("date") in DAYS:
            miss.setdefault(mm.group("tail").upper(), {}) \
                .setdefault(mm.group("date"), []).append(mm.group("source"))

    if args.json:
        print(json.dumps({"traces": report, "asked_and_empty": miss}, indent=1))
        return

    for tail in sorted(report):
        print("=" * 78)
        print(tail)
        for day in sorted(report[tail]):
            rec = report[tail][day]
            print(f"  --- {day} ---")
            for src, recs in sorted(rec["sources"].items()):
                for r in recs:
                    print(f"   [{src}] {r['points']} pts  {r.get('type')}  {r['file']}")
                    if not r["points"]:
                        continue
                    print(f"      first {r['first_fix_utc']} {r['first_pos']} alt={r['first_alt']}")
                    print(f"      last  {r['last_fix_utc']} {r['last_pos']} alt={r['last_alt']}"
                          f"  maxalt={r['max_alt_ft']} maxgs={r['max_gs_kt']}")
                    for t in r["transitions"]:
                        print(f"      {t['kind']:12} {t['utc']}  {t['nearest_field']} "
                              f"{t['km_from_field']}km")
                    for v in r["ground_visits"]:
                        print(f"      GROUND {v['airport_code']} ({v['airport_city']}) "
                              f"med {v['median_km_from_field']}km  "
                              f"{v['first_seen_utc']} -> {v['last_seen_utc']}  "
                              f"{v['ground_points']}pts {v['seconds_on_ground_observed']}s")
            if rec["diff"]:
                d = rec["diff"]
                print(f"      DIFF lol={d['points_a']} al={d['points_b']} shared={d['shared']} "
                      f"only_lol={d['only_a']} only_al={d['only_b']} "
                      f"value_mismatches={d['value_mismatches']}")
    print("=" * 78)
    print("ASKED AND EMPTY (archive queried, held nothing) inside the window:")
    for tail in sorted(miss):
        for day in sorted(miss[tail]):
            print(f"  {tail:20} {day}  {','.join(sorted(miss[tail][day]))}")


if __name__ == "__main__":
    main()
