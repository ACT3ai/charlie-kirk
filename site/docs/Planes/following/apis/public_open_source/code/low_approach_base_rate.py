#!/usr/bin/env python3
"""How often does an aircraft fly down to the runway and NOT land?

    python3 low_approach_base_rate.py N1098L N2100L N102DZ

WHY THIS EXISTS
---------------
On 2025-09-10 N1098L descended twice to ~200-250 ft above Provo's runway 13,
40 m from the centreline, and climbed away both times without landing. That is a
striking-looking event and it is exactly the kind of observation this
investigation has previously got wrong by not asking the boring question first:
IS THIS UNUSUAL FOR THIS AIRFRAME? A crew flying published instrument approaches
to minimums and going around is doing routine training, and it looks identical
from an ADS-B trace.

So this script sweeps EVERY recovered trace on disk for the named tails and
counts two things per aircraft-day:

  LANDING       a descent below 600 ft above the nearest field's elevation,
                within 5 km of that field, FOLLOWED by an on-ground position
                report at the same field inside 15 minutes.
  LOW APPROACH  the same descent with NO on-ground report following it - the
                aircraft came down to the runway and climbed away.

The ratio is the base rate. It does not say why any single one happened. A trace
proves presence, never purpose. Field elevation comes from OurAirports and the
altitude is uncorrected barometric, so the AGL figure carries a few tens of feet
of error - which is why the threshold is 600 ft and not 50.
"""
from __future__ import annotations

import glob
import gzip
import json
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
from geo import haversine_km, nearest_airport  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
PLANES = os.path.normpath(os.path.join(HERE, "..", "..", "..", ".."))
NAME_RE = re.compile(r"^(?P<tail>[A-Z0-9-]+)_(?P<date>\d{4}-\d{2}-\d{2})_"
                     r"(?P<source>[a-z0-9-]+)_trace_full\.json(\.gz)?$")

AGL_MAX = 600.0     # ft above field elevation
NEAR_KM = 5.0       # of the airport reference point
FOLLOW_SEC = 900    # look this far ahead for an on-ground report


def load(path):
    opener = gzip.open if path.endswith(".gz") else open
    with opener(path, "rt", encoding="utf-8") as fh:
        return json.load(fh)


def events(path):
    doc = load(path)
    pts = [p for p in (doc.get("trace") or []) if len(p) >= 4 and p[1] is not None]
    out = []
    i = 0
    while i < len(pts):
        p = pts[i]
        if not isinstance(p[3], (int, float)):
            i += 1
            continue
        ap = nearest_airport(p[1], p[2], radius_mi=NEAR_KM * 0.621371)
        if not ap or ap.get("elevation_ft") in (None, ""):
            i += 1
            continue
        agl = p[3] - float(ap["elevation_ft"])
        if agl > AGL_MAX or agl < -400:
            i += 1
            continue
        # collect the whole low run at this field
        run = []
        j = i
        while j < len(pts):
            q = pts[j]
            if q[3] == "ground":
                run.append(q)
                j += 1
                continue
            if not isinstance(q[3], (int, float)):
                break
            if haversine_km(q[1], q[2], ap["lat"], ap["lon"]) > NEAR_KM * 2:
                break
            if q[3] - float(ap["elevation_ft"]) > AGL_MAX + 400:
                break
            run.append(q)
            j += 1
        landed = any(q[3] == "ground" for q in run)
        if not landed:
            t_end = run[-1][0] if run else p[0]
            for q in pts[j:]:
                if q[0] - t_end > FOLLOW_SEC:
                    break
                if q[3] == "ground" and haversine_km(q[1], q[2], ap["lat"], ap["lon"]) < NEAR_KM * 2:
                    landed = True
                    break
        lo = min((q for q in run if isinstance(q[3], (int, float))),
                 key=lambda q: q[3], default=p)
        out.append({
            "airport": ap["ident"],
            "elev_ft": float(ap["elevation_ft"]),
            "min_alt_ft": lo[3],
            "min_agl_ft": round(lo[3] - float(ap["elevation_ft"])),
            "t_start": run[0][0] if run else p[0],
            "t_min": lo[0],
            "landed": landed,
        })
        i = max(j, i + 1)
    return out


def main():
    tails = [a.upper() for a in sys.argv[1:]] or ["N1098L"]
    for tail in tails:
        paths = sorted(glob.glob(os.path.join(PLANES, tail, "data", "recovered",
                                              f"{tail}_*_trace_full.json"))
                       + glob.glob(os.path.join(PLANES, tail, "data", "recovered",
                                                f"{tail}_*_trace_full.json.gz")))
        # one source per date: prefer airplanes-live (denser), else adsb-lol
        by_date = {}
        for p in paths:
            m = NAME_RE.match(os.path.basename(p))
            if not m:
                continue
            by_date.setdefault(m.group("date"), {})[m.group("source")] = p
        land = lowap = 0
        lowlist = []
        for date in sorted(by_date):
            src = by_date[date].get("airplanes-live") or list(by_date[date].values())[0]
            try:
                evs = events(src)
            except Exception as exc:      # noqa: BLE001
                print(f"  ! {date} {exc}")
                continue
            for e in evs:
                if e["landed"]:
                    land += 1
                else:
                    lowap += 1
                    lowlist.append((date, e))
        tot = land + lowap
        print(f"{tail}: {len(by_date)} aircraft-days on disk; {tot} arrivals at "
              f"<= {AGL_MAX:.0f} ft AGL within {NEAR_KM:.0f} km of a field")
        print(f"   LANDED {land}   LOW APPROACH (no touchdown) {lowap}"
              f"   -> low-approach rate {100*lowap/max(tot,1):.1f}%")
        for date, e in lowlist:
            print(f"     LOW APPROACH {date} {e['airport']:6} min {e['min_alt_ft']} ft "
                  f"({e['min_agl_ft']} AGL)  t+{e['t_min']:.0f}s")


if __name__ == "__main__":
    main()
