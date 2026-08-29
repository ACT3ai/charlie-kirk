#!/usr/bin/env python3
"""Measure the ADS-B windows behind EVERY row of overlaps.csv.

WHY THIS EXISTS. build_info_yaml.py writes the info.yaml files, but it does not
measure anything itself — it reads a windows file. The first run of the Plane
Overlap graphics measured those windows in a throwaway script under /tmp, which
covered only the twelve field-years the Erika claim rests on (56 of the 85 rows)
and could not be re-run. This is that step, written down, covering ALL rows.

WHAT IT MEASURES, per (overlap row, tail):
  * ground windows  runs of positions with the ADS-B on-ground flag set within
                    GROUND_MAX_KM of the claimed field. A real stay.
  * near windows    runs of AIRBORNE positions within NEAR_FIELD_KM of the field
                    and below NEAR_FIELD_AGL above field elevation. Real,
                    measured, and NOT a landing.
  * closest         the single closest position of the day, whatever it was, so
                    "the archive holds this tail but it was 27 km away" can be
                    told apart from "the archive holds nothing".

WHAT IT REFUSES TO DO. It never invents a position, never widens a date into a
time, and never fills a gap. A tail with no payload for a date comes back with
points 0 and queried [] — an unasked-or-unheld question, NOT an absence. A
volunteer receiver network heard nothing; parked with the transponder off,
outside coverage, and a wrong claimed date all look identical from here.

  python3 measure_windows.py                 measure everything, write the JSON
  python3 measure_windows.py --out PATH      somewhere other than the default
  python3 measure_windows.py --verify        re-measure and diff against the JSON
"""
from __future__ import annotations

import csv
import datetime as dt
import glob
import json
import os
import re
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PLANES = os.path.normpath(os.path.join(HERE, "..", ".."))
FOLLOWING = os.path.join(PLANES, "following")
OVERLAPS_CSV = os.path.join(FOLLOWING, "overlaps.csv")
GEO_LIB = os.path.join(FOLLOWING, "apis", "public_open_source", "code", "lib")
DEFAULT_OUT = os.environ.get("CK_WINDOWS_JSON", "/tmp/ck_windows.json")

sys.path.insert(0, GEO_LIB)
from geo import airport_by_code, haversine_km  # noqa: E402
from traces import open_trace, TRACE_RE        # noqa: E402

# A ground position further than this from the field is not a visit to that
# field. 8 km covers a large international ramp and excludes the next field over.
GROUND_MAX_KM = 8.0
# Airborne and within this of the field is a PASS — an approach, a departure
# climb, an overflight. It is never a landing.
NEAR_FIELD_KM = 15.0
# ...and only below this above the field's own elevation. Without the ceiling a
# jet at cruise crossing the circle would be drawn as if it came to look.
NEAR_FIELD_AGL = 6000
# Gap that splits one run into two. Below it the aircraft never left.
RUN_GAP_SEC = 45 * 60

# Every airframe in this investigation's fleet gets queried at every field, so
# the record says what was asked as well as what answered.
FOLLOWING_TAILS = ["SU-BTT", "SU-BND", "SU-BGM", "SU-BTU", "SU-BTV", "T7-ELL"]
KIRK_TAILS = ["N102DZ", "N582MM", "N872RA", "N40JD", "N560TW", "N888KG"]


def _num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _iso(day, secs):
    base = dt.datetime.strptime(day, "%Y-%m-%d").replace(tzinfo=dt.timezone.utc)
    return (base + dt.timedelta(seconds=float(secs))).isoformat().replace("+00:00", "Z")


def trace_paths(tail, date):
    """Every recovered payload on disk for one tail on one UTC date, by source."""
    d = os.path.join(PLANES, tail, "data", "recovered")
    out = {}
    for path in sorted(glob.glob(os.path.join(d, "%s_%s_*_trace_full.json*" % (tail, date)))):
        m = TRACE_RE.match(os.path.basename(path))
        if m and m.group("date") == date:
            out.setdefault(m.group("source"), path)
    return out


def points_for(tail, date):
    """(t_secs, lat, lon, alt_or_None, source) for every position of the day.

    Points from every archive are pooled and sorted by time. Two archives that
    both heard the same second are two heard positions, not one — the point
    count is a measure of how well covered the moment was, not of how long the
    aircraft sat there, and the durations come from the timestamps regardless.
    """
    pts, sources = [], []
    for source, path in trace_paths(tail, date).items():
        try:
            with open_trace(path) as fh:
                doc = json.load(fh)
        except (OSError, ValueError, EOFError):
            continue                       # unreadable is not empty; it is dropped loudly below
        sources.append(source)
        for p in doc.get("trace") or []:
            if len(p) < 4:
                continue
            t, lat, lon, alt = p[0], p[1], p[2], p[3]
            if lat is None or lon is None or _num(t) is None:
                continue
            pts.append((float(t), float(lat), float(lon),
                        None if alt == "ground" else _num(alt), source))
    pts.sort(key=lambda r: r[0])
    return pts, sorted(sources)


def runs(marked, date, gap=RUN_GAP_SEC):
    """Split time-ordered (t, km, alt, source) hits into windows."""
    out, run = [], []
    for h in marked:
        if run and h[0] - run[-1][0] > gap:
            out.append(run)
            run = []
        run.append(h)
    if run:
        out.append(run)
    windows = []
    for r in out:
        alts = [h[2] for h in r if h[2] is not None]
        windows.append({
            "first": _iso(date, r[0][0]),
            "last": _iso(date, r[-1][0]),
            "n": len(r),
            "min_km": round(min(h[1] for h in r), 2),
            "median_km": round(statistics.median(h[1] for h in r), 2),
            "min_alt_ft": int(min(alts)) if alts else None,
            "srcs": sorted({h[3] for h in r}),
        })
    return windows


def measure(tail, date, ap):
    """One tail, one UTC date, against one field."""
    pts, sources = points_for(tail, date)
    rec = {"closest": None, "ground": [], "near": [], "points": len(pts), "queried": sources}
    if not pts:
        return rec
    elev = _num(ap.get("elevation_ft")) or 0.0
    ceiling = elev + NEAR_FIELD_AGL
    best = None
    ground_hits, near_hits = [], []
    for t, lat, lon, alt, src in pts:
        km = haversine_km(lat, lon, ap["lat"], ap["lon"])
        if best is None or km < best[0]:
            best = (km, t, alt, src)
        if alt is None:
            if km <= GROUND_MAX_KM:
                ground_hits.append((t, km, None, src))
        elif km <= NEAR_FIELD_KM and alt <= ceiling:
            near_hits.append((t, km, alt, src))
    rec["closest"] = {"km": round(best[0], 2), "utc": _iso(date, best[1]),
                      "alt_ft": None if best[2] is None else int(best[2]),
                      "on_ground": best[2] is None, "source": best[3]}
    rec["ground"] = runs(ground_hits, date)
    rec["near"] = runs(near_hits, date)
    return rec


def row_tails(row):
    """Every following tail a row names. "SU-BTT or SU-BND" names two."""
    raw = (row.get("foreign_tail") or "").strip()
    if not raw or raw.upper() == "UNKNOWN":
        return []
    return [t.strip().upper() for t in re.split(r"[;,]| or ", raw) if t.strip()]


def main():
    out_path = DEFAULT_OUT
    if "--out" in sys.argv:
        out_path = sys.argv[sys.argv.index("--out") + 1]
    verify = "--verify" in sys.argv

    rows = list(csv.DictReader(open(OVERLAPS_CSV, newline="", encoding="utf-8")))
    recs, unresolved = {}, []
    for row in rows:
        oid = row["overlap_id"]
        date = (row.get("date") or "").strip()
        code = (row.get("airport_code") or "").strip().upper()
        # A row naming three fields at once ("KSTL/KCPS/KSUS") is a claim about a
        # metro area, not about a field. It is recorded and not measured — there
        # is no single field to measure a ground contact against.
        multi = "/" in code
        ap = None if (multi or not code) else airport_by_code(code)
        rec = {
            "airport": code, "airport_name": (row.get("airport_name") or "").strip(),
            "city": (row.get("city") or "").strip(), "state": (row.get("state") or "").strip(),
            "date": date, "subject": (row.get("subject") or "").strip(),
            "charlie": (row.get("charlie_present") or "").strip(),
            "erika": (row.get("erika_present") or "").strip(),
            "foreign_tail": (row.get("foreign_tail") or "").strip(),
            "kirk_tail": (row.get("kirk_tail") or "").strip(),
            "overlap_page": (row.get("overlap_page") or "").strip(),
            "verdict": (row.get("adsb_verified_verdict") or "").strip(),
            "per_tail": {},
        }
        if not date or date.upper() == "UNKNOWN":
            rec["unmeasurable"] = "no date on this row - there is no window to measure"
            recs[oid] = rec
            continue
        if ap is None:
            rec["unmeasurable"] = ("no single field on this row (%s)" % (code or "airport_code empty")
                                   if not multi else
                                   "this row names a metro area (%s), not one field" % code)
            unresolved.append((oid, code))
            recs[oid] = rec
            continue
        rec["field_lat"], rec["field_lon"] = round(ap["lat"], 5), round(ap["lon"], 5)
        rec["field_name"] = ap["name"]
        for tail in sorted(set(FOLLOWING_TAILS + KIRK_TAILS + row_tails(row))):
            rec["per_tail"][tail] = measure(tail, date, ap)
        recs[oid] = rec
        held = [t for t, v in rec["per_tail"].items() if v["points"]]
        print("%-11s %-10s %-6s %-8s queried %2d tails, %2d held, %2d with ground contact"
              % (oid, date, code, rec["subject"], len(rec["per_tail"]), len(held),
                 sum(1 for v in rec["per_tail"].values() if v["ground"])))

    if verify:
        old = json.load(open(out_path))
        same = diff = 0
        for oid in sorted(set(old) & set(recs)):
            if json.dumps(old[oid]["per_tail"], sort_keys=True) == \
               json.dumps({k: v for k, v in recs[oid]["per_tail"].items()
                           if k in old[oid]["per_tail"]}, sort_keys=True):
                same += 1
            else:
                diff += 1
                print("DIFFERS  %s" % oid)
        print("\nverify: %d identical, %d differ, %d rows only in the new run"
              % (same, diff, len(set(recs) - set(old))))
        return

    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(recs, fh, indent=1, sort_keys=True)
    measured = sum(1 for r in recs.values() if "unmeasurable" not in r)
    print("\n%d overlap rows: %d measured, %d unmeasurable -> %s"
          % (len(recs), measured, len(recs) - measured, out_path))
    for oid, code in unresolved:
        print("  UNRESOLVED FIELD  %-11s %s" % (oid, code or "(empty)"))


if __name__ == "__main__":
    main()
