"""Turn the recovered ADS-B traces into airport VISITS.

WHAT A VISIT IS, AND WHAT IT IS NOT
-----------------------------------
A "visit" here means: this airframe transmitted positions with the ON-GROUND
flag set, and the nearest airport to those positions was X, at a median of Y km.

That is a strong statement and a narrow one. It is NOT a landing record, NOT a
flight plan, and NOT evidence that anybody was aboard. A trace proves presence,
never purpose and never occupancy.

The failure modes, all of which this module reports rather than hides:

  * NO TRACE FOR A DATE IS NOT AN ABSENCE. A volunteer receiver network heard
    nothing. Parked with the transponder off, outside coverage, or the claimed
    date is wrong — all three look identical from here.
  * A NEAREST-FIELD LABEL IS NOT A DESTINATION. Every visit carries the median
    distance from the field. The Provo-versus-Dugway mislabel this
    investigation had to correct came from dropping that number.
  * COVERAGE IS SPARSE AND UNEVEN. The adsbexchange-samples source holds ONE
    DAY PER MONTH (the 1st). A hit from it fixes a position on that date and
    says nothing whatever about frequency.

Trace point layout, per the readsb `trace_full` format:
    [ seconds_after_UTC_midnight, lat, lon, altitude, ground_speed, track,
      flags, vert_rate, aircraft_obj, source, geom_alt, ... ]
`altitude` is the string "ground" when the aircraft reports itself on the
ground, otherwise barometric feet.
"""
from __future__ import annotations

import datetime as dt
import glob
import gzip
import json
import os
import re
import statistics

from geo import airports_within, haversine_km, nearest_airport

PLANES_DIR = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "..", "..", ".."))

# A ground position further than this from any runway is not a visit to that
# field, it is an unresolved position. 8 km comfortably covers a large
# international airport's ramps while excluding the next field over.
GROUND_MAX_KM = 8.0
# Gap that splits one ground run into two visits (aircraft left and came back).
VISIT_GAP_SEC = 45 * 60
# Below this AGL-ish figure a passing aircraft is manoeuvring near the field
# rather than transiting over it. Reported separately from ground presence.
NEAR_FIELD_FT = 6000
NEAR_FIELD_KM = 15.0

# `.json` and `.json.gz` are the SAME EVIDENCE in two containers. Older pulls are
# uncompressed; pulls from 24 Aug 2026 on are gzipped because a full fleet sweep
# in raw JSON would add most of a gigabyte to a repo an automated job pushes.
TRACE_RE = re.compile(
    r"^(?P<tail>[A-Z0-9-]+)_(?P<date>\d{4}-\d{2}-\d{2})_(?P<source>[a-z0-9-]+)_trace_full\.json(?P<gz>\.gz)?$")


def trace_files(tails=None):
    """Yield (tail, date, source, path) for every recovered trace on disk."""
    paths = (glob.glob(os.path.join(PLANES_DIR, "*", "data", "recovered", "*_trace_full.json"))
             + glob.glob(os.path.join(PLANES_DIR, "*", "data", "recovered", "*_trace_full.json.gz")))
    for path in sorted(paths):
        m = TRACE_RE.match(os.path.basename(path))
        if not m:
            continue
        tail = m.group("tail").upper()
        if tails and tail not in tails:
            continue
        yield tail, m.group("date"), m.group("source"), path


def _iso(day, secs):
    base = dt.datetime.strptime(day, "%Y-%m-%d").replace(tzinfo=dt.timezone.utc)
    return (base + dt.timedelta(seconds=float(secs))).isoformat().replace("+00:00", "Z")


def visits_from_trace(path, day):
    """Ground visits and near-field passes for one aircraft-day."""
    try:
        opener = gzip.open if path.endswith(".gz") else open
        with opener(path, "rt", encoding="utf-8") as fh:
            doc = json.load(fh)
    except (OSError, ValueError, EOFError):
        return {"error": "unreadable", "ground_visits": [], "near_field": []}

    pts = doc.get("trace") or []
    ground, air = [], []
    for p in pts:
        if len(p) < 4:
            continue
        t, lat, lon, alt = p[0], p[1], p[2], p[3]
        if lat is None or lon is None:
            continue
        if alt == "ground":
            ground.append((t, lat, lon))
        elif isinstance(alt, (int, float)):
            air.append((t, lat, lon, alt))

    # --- ground runs -> visits ---------------------------------------------
    visits = []
    run = []
    for pt in ground:
        if run and pt[0] - run[-1][0] > VISIT_GAP_SEC:
            visits.append(run)
            run = []
        run.append(pt)
    if run:
        visits.append(run)

    out = []
    for run in visits:
        mlat = statistics.median(p[1] for p in run)
        mlon = statistics.median(p[2] for p in run)
        ap = nearest_airport(mlat, mlon, radius_mi=GROUND_MAX_KM * 0.621371 + 1)
        dist_km = round(haversine_km(mlat, mlon, ap["lat"], ap["lon"]), 2) if ap else None
        out.append({
            "airport_code": ap["ident"] if ap else None,
            "airport_name": ap["name"] if ap else None,
            "airport_city": (ap.get("municipality") if ap else None),
            "median_distance_km": dist_km,
            "resolved": bool(ap),
            "first_seen_utc": _iso(day, run[0][0]),
            "last_seen_utc": _iso(day, run[-1][0]),
            "ground_points": len(run),
            "lat": round(mlat, 5),
            "lon": round(mlon, 5),
        })

    # --- low passes near a field, when there is no ground contact ----------
    near = []
    seen = set()
    for t, lat, lon, alt in air:
        if alt > NEAR_FIELD_FT:
            continue
        for ap in airports_within(lat, lon, NEAR_FIELD_KM * 0.621371):
            if ap["ident"] in seen:
                continue
            seen.add(ap["ident"])
            near.append({
                "airport_code": ap["ident"],
                "airport_name": ap["name"],
                "distance_mi": ap["distance_mi"],
                "altitude_ft": alt,
                "time_utc": _iso(day, t),
                "note": "LOW PASS ONLY - no on-ground position at this field in this trace.",
            })
    return {"ground_visits": out, "near_field": near,
            "trace_points": len(pts), "registration": doc.get("r"), "type": doc.get("t")}


def build_index(tails=None, cache_path=None, rebuild=False):
    """tail -> date -> list of per-source visit records. Cached as JSON."""
    if cache_path and os.path.exists(cache_path) and not rebuild:
        with open(cache_path, encoding="utf-8") as fh:
            return json.load(fh)
    idx = {}
    for tail, day, source, path in trace_files(tails):
        rec = visits_from_trace(path, day)
        rec["source"] = source
        rec["file"] = os.path.relpath(path, PLANES_DIR)
        idx.setdefault(tail, {}).setdefault(day, []).append(rec)
    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        with open(cache_path, "w", encoding="utf-8") as fh:
            json.dump(idx, fh, indent=1)
    return idx


if __name__ == "__main__":
    import sys
    tails = set(a.upper() for a in sys.argv[1:]) or None
    idx = build_index(tails)
    for tail in sorted(idx):
        days = idx[tail]
        gv = sum(len(r["ground_visits"]) for d in days.values() for r in d)
        print(f"{tail:8} {len(days):3} days  {gv:4} ground visits")
        for day in sorted(days)[:3]:
            for rec in days[day]:
                for v in rec["ground_visits"]:
                    print(f"    {day} {rec['source']:22} {v['airport_code']} "
                          f"{v['median_distance_km']}km {v['first_seen_utc']} -> {v['last_seen_utc']}")


MISS_RE = re.compile(
    r"^(?P<tail>[A-Z0-9-]+)_(?P<date>\d{4}-\d{2}-\d{2})_(?P<source>[a-z0-9-]+)_trace_full\.miss\.json\.meta\.json$")


def build_miss_index():
    """tail -> date -> [source, ...] for days an archive was ASKED and had nothing.

    This is the difference between "we never queried that day" and "we queried it
    and the archive holds no trace". Those two are NOT the same and merging them
    is how an unasked question gets published as a negative finding. It is still
    NOT evidence the aircraft was elsewhere - a volunteer receiver network simply
    heard nothing, and parked-with-the-transponder-off, outside-coverage, and a
    wrong claimed date all look identical from here.
    """
    idx = {}
    for path in glob.glob(os.path.join(PLANES_DIR, "*", "data", "recovered",
                                       "*_trace_full.miss.json.meta.json")):
        m = MISS_RE.match(os.path.basename(path))
        if not m:
            continue
        idx.setdefault(m.group("tail").upper(), {}) \
           .setdefault(m.group("date"), []).append(m.group("source"))
    return idx
