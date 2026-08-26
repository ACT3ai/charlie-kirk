#!/usr/bin/env python3
"""Re-audit every claimed overlap against the RECOVERED TRACE CORPUS on disk.

WHY THIS EXISTS AND WHY IT IS NOT verify_overlaps.js
----------------------------------------------------
`verify_overlaps.js` asks the two archives over the network, one row at a time,
at the moment it runs. That was the right tool on the day the ledger was first
audited. It is the wrong tool now, for one reason: THE ARCHIVE WE ASK TODAY IS
NOT THE ARCHIVE WE ASKED THEN. Records in this case have been removed after the
fact -- that is the thing being investigated -- so a verdict must be computed
against bytes we PULLED AND KEPT, not against whatever a live endpoint feels
like serving this morning.

So this script reads only `<TAIL>/data/recovered/`. Every verdict it produces is
reproducible from files in this repo, by anyone, forever, whatever the archives
later do.

HOW A ROW IS MEASURED
---------------------
Not from a summary. From the raw `trace_full` points. For each claimed field the
script takes the minimum great-circle distance to any point in the trace, and
does it TWICE: once over points the aircraft flagged ON GROUND, once over
airborne points. Ground evidence always outranks airborne evidence, because an
aircraft that overflies a field at 4,000 ft did not visit it, and a verdict that
cannot tell those apart is worthless.

THE VERDICTS, AND EXACTLY WHAT EACH ONE IS WORTH
------------------------------------------------
  AT_CLAIMED_AIRPORT      A recovered trace puts this airframe within 15 km of
                          the claimed field ON THE CLAIMED DATE. The note says
                          whether that was an ON-GROUND position (strong) or a
                          low airborne pass (weaker - an arrival or departure,
                          possibly an overflight). CORROBORATED by primary data.
  SAME_METRO_WRONG_FIELD  Within 80 km (~50 mi) but not within 15 km. Right
                          area, wrong airport: neither confirmed nor refuted at
                          the field it names. The published source tolerance is
                          50-100 miles, so this is exactly what that tolerance
                          buys and exactly where the public dispute lives.
  ELSEWHERE               Tracked that day and nowhere near it. This REFUTES the
                          row, and it is the only verdict here with teeth
                          against a claim.
  NOT_HEARD               An archive was serving that day -- other airframes came
                          back from it -- but holds no trace for this one. WEAK.
                          Parked with the transponder off, outside receiver
                          coverage, and a wrong claimed date all look identical.
  NO_ARCHIVE_COVERAGE     Neither archive holds the day for any airframe we
                          probed. Says NOTHING either way. Most 2022-2023 rows
                          land here, and that is a retention boundary, not a
                          cover-up.
  NOT_QUERIED             Nobody has asked yet. An OPEN QUESTION, not a coverage
                          fact, and it must never be counted as one.
  NO_DATE_CLAIMED /
  NO_TAIL_CLAIMED         The claim itself is not testable as published.

AN ABSENCE IS NOT A FINDING. A TRACE PROVES PRESENCE, NEVER PURPOSE, AND NEVER
OCCUPANCY -- recovering an aircraft's movements still places nobody aboard it.

    python3 verify_overlaps_local.py                  report only
    python3 verify_overlaps_local.py --write          write the columns back
    python3 verify_overlaps_local.py --id OWENS-041
"""
from __future__ import annotations

import argparse
import collections
import csv
import datetime as dt
import gzip
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "lib"))

import traces                                   # noqa: E402
from geo import airport_by_code, haversine_km, nearest_airport   # noqa: E402

FOLLOWING = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
OVERLAPS_CSV = os.path.join(FOLLOWING, "overlaps.csv")
OUT_JSON = os.path.normpath(os.path.join(HERE, "..", "data", "overlap_verification",
                                         "overlap_verification_local.json"))

NEAR_KM = 15.0      # "at the claimed field"
METRO_KM = 80.0     # the source spreadsheet's own ~50-mile tolerance
# ABOVE GROUND LEVEL, not above sea level. A jet 6,000 ft over Wichita (field
# elevation 1,333 ft) is transiting; 6,000 ft over Provo (4,497 ft) is on final.
# Measuring against the field's own elevation is the only way those two do not
# get scored the same.
LOW_PASS_AGL_FT = 4000
TAIL_RE = re.compile(r"SU-[A-Z]{3}")


def claimed_airports(code):
    """A row may name several fields ('KSTL/KCPS/KSUS'). Resolve all of them."""
    out, seen = [], set()
    for c in re.split(r"[/;, ]+", (code or "").strip()):
        ap = airport_by_code(c)
        if ap and ap["ident"] not in seen:
            seen.add(ap["ident"])
            out.append(ap)
    return out


def load_points(path):
    """[(lat, lon, on_ground, alt_ft)] straight out of a recovered trace_full."""
    opener = gzip.open if path.endswith(".gz") else open
    try:
        with opener(path, "rt", encoding="utf-8") as fh:
            doc = json.load(fh)
    except (OSError, ValueError, EOFError):
        return []
    out = []
    for p in doc.get("trace") or []:
        if len(p) < 4 or p[1] is None or p[2] is None:
            continue
        alt = p[3]
        out.append((p[1], p[2], alt == "ground",
                    alt if isinstance(alt, (int, float)) else 0))
    return out


def measure(paths, aps):
    """Closest approach to any claimed field, ground and air measured separately.

    Also records WHERE the aircraft actually sat on the ground that day, when it
    sat anywhere. For a row corroborated only in the air that is the difference
    between "the archive lost it on the ramp" and "it landed somewhere else" -
    and a reader is entitled to which.
    """
    best = {"ground_km": None, "air_km": None, "air_agl": None,
            "field": None, "ground_field": None, "parked_at": None,
            "points": 0, "ground_points": 0}
    parked = None
    for path in paths:
        for lat, lon, on_ground, alt in load_points(path):
            best["points"] += 1
            if on_ground:
                best["ground_points"] += 1
                if parked is None:
                    parked = nearest_airport(lat, lon, radius_mi=12)
            for ap in aps:
                km = haversine_km(lat, lon, ap["lat"], ap["lon"])
                if on_ground:
                    if best["ground_km"] is None or km < best["ground_km"]:
                        best["ground_km"], best["ground_field"] = km, ap["ident"]
                else:
                    try:
                        elev = float(ap.get("elevation_ft") or 0)
                    except (TypeError, ValueError):
                        elev = 0.0
                    if best["air_km"] is None or km < best["air_km"]:
                        best["air_km"] = km
                        best["air_agl"] = alt - elev
                        best["field"] = ap["ident"]
    if parked:
        best["parked_at"] = f"{parked['ident']} ({parked['name']})"
    return best


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true", help="write the columns back into overlaps.csv")
    ap.add_argument("--id", default=None)
    args = ap.parse_args()

    # tail -> date -> [paths];  and (source, date) the archives demonstrably served.
    have = collections.defaultdict(lambda: collections.defaultdict(list))
    served = collections.defaultdict(set)
    for tail, date, source, path in traces.trace_files():
        have[tail][date].append(path)
        served[source].add(date)
    miss = traces.build_miss_index()
    print(f"corpus: {sum(len(d) for d in have.values())} aircraft-days with a payload, "
          f"{sum(len(d) for d in miss.values())} asked-and-empty, "
          f"{len({d for s in served.values() for d in s})} distinct days an archive served",
          flush=True)

    rows = list(csv.DictReader(open(OVERLAPS_CSV, newline="", encoding="utf-8")))
    fields = list(rows[0].keys())
    # An ON-GROUND position is a different class of evidence from a low pass and
    # the file has to say which, or a downstream chart will silently score them
    # the same.
    if "adsb_ground_position" not in fields:
        fields.append("adsb_ground_position")
    results, counts, ground_hits = [], collections.Counter(), 0

    for r in rows:
        rid = r["overlap_id"]
        if args.id and rid != args.id:
            continue
        day = (r["date"] or "").strip()
        tails = TAIL_RE.findall((r["foreign_tail"] or "").upper())
        aps = claimed_airports(r["airport_code"])
        km, srcs = None, []

        if len(day) != 10 or day == "UNKNOWN":
            v, note = "NO_DATE_CLAIMED", (
                "The claim carries no date, so no archive can be asked about it. "
                "Untestable as published.")
        elif not tails:
            v, note = "NO_TAIL_CLAIMED", (
                "The claim names no tail number, so there is no airframe to look up. "
                "Untestable as published.")
        else:
            paths = [p for t in tails for p in have.get(t, {}).get(day, [])]
            srcs = sorted({os.path.basename(p).split("_")[2] for p in paths})
            if paths and not aps:
                v, note = "NOT_HEARD", (
                    "A recovered trace exists for this aircraft-day, but the claim names "
                    "no resolvable airport to measure it against.")
            elif paths:
                m = measure(paths, aps)
                g, a = m["ground_km"], m["air_km"]
                if g is not None and g <= NEAR_KM:
                    v, km = "AT_CLAIMED_AIRPORT", g
                    note = ("CORROBORATED, AND ON THE GROUND. A trace we pulled and kept "
                            f"puts this airframe on the ground {g:.1f} km from "
                            f"{m['ground_field']} on the claimed date. It places NOBODY "
                            "aboard.")
                elif a is not None and a <= NEAR_KM and m["air_agl"] <= LOW_PASS_AGL_FT:
                    v, km = "AT_CLAIMED_AIRPORT", a
                    where = (f" The only on-ground positions in this trace are at "
                             f"{m['parked_at']}." if m["parked_at"] and
                             (m["ground_km"] is None or m["ground_km"] > NEAR_KM)
                             else " This trace holds no on-ground positions at all, which is "
                                  "ordinary: receiver coverage of a parked aircraft is thin.")
                    note = ("CORROBORATED IN THE AIR, NOT ON THE GROUND. Closest recovered "
                            f"position is {a:.1f} km from {m['field']} at "
                            f"{int(m['air_agl']):,} ft above the field - an arrival, a "
                            f"departure or a low pass.{where} It places NOBODY aboard.")
                else:
                    km = min(x for x in (g, a) if x is not None)
                    field = m["ground_field"] if km == g else m["field"]
                    if km <= METRO_KM:
                        v = "SAME_METRO_WRONG_FIELD"
                        note = (f"RIGHT AREA, WRONG FIELD. Closest recovered position is "
                                f"{km:.0f} km from {field} - inside the source sheet's own "
                                "50-100 mile tolerance, outside a same-airport test. "
                                "Neither confirmed nor refuted.")
                    else:
                        v = "ELSEWHERE"
                        note = (f"REFUTED. The airframe was tracked that day and its closest "
                                f"recovered position is {km:,.0f} km from {field}.")
                if v == "AT_CLAIMED_AIRPORT" and g is not None and g <= NEAR_KM:
                    ground_hits += 1
            else:
                asked = {s for t in tails for s in miss.get(t, {}).get(day, [])}
                serving = {s for s in served if day in served[s]}
                srcs = sorted(asked)
                if not asked:
                    v, note = "NOT_QUERIED", (
                        "OPEN QUESTION. No archive has been asked about this aircraft-day "
                        "yet. This is not a coverage fact and must not be counted as one.")
                elif serving:
                    v, note = "NOT_HEARD", (
                        f"SAYS ALMOST NOTHING. {'/'.join(sorted(serving))} served other "
                        "airframes that day but holds no trace for this one. Parked with "
                        "the transponder off, outside receiver coverage, and a wrong "
                        "claimed date all look identical from here. AN ABSENCE IS NOT A "
                        "FINDING.")
                else:
                    v, note = "NO_ARCHIVE_COVERAGE", (
                        "SAYS NOTHING EITHER WAY. Neither free archive holds this date for "
                        "any airframe we probed, so this is an archive limit and not "
                        "suppression.")

        counts[v] += 1
        results.append({"overlap_id": rid, "date": day, "tails": tails,
                        "on_ground": note.startswith("CORROBORATED, AND ON THE GROUND"),
                        "claimed_airport": r["airport_code"], "subject": r["subject"],
                        "kanekoa_audit_verdict": r["audit_verdict"], "verdict": v,
                        "closest_approach_km": round(km, 2) if km is not None else None,
                        "sources": srcs, "note": note})
        r["adsb_verified_verdict"] = v
        r["adsb_closest_approach_km"] = f"{km:.2f}" if km is not None else ""
        r["adsb_verified_note"] = note
        r["adsb_ground_position"] = ("yes" if note.startswith("CORROBORATED, AND ON THE GROUND")
                                     else "no" if v == "AT_CLAIMED_AIRPORT" else "")

    print()
    for k, n in counts.most_common():
        print(f"  {n:4d}  {k}")
    print(f"  ----  {sum(counts.values())} rows "
          f"({ground_hits} of the corroborations are ON-GROUND positions)")

    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as fh:
        json.dump({"verified_utc": dt.datetime.now(dt.timezone.utc)
                   .isoformat(timespec="seconds").replace("+00:00", "Z"),
                   "method": "Every verdict computed from recovered trace files held in this "
                             "repo under <TAIL>/data/recovered/, measured point-by-point off "
                             "the raw trace_full, not from a live archive query. "
                             "AT_CLAIMED_AIRPORT = within 15 km of the claimed field on the "
                             "claimed date, with on-ground positions ranked above airborne "
                             "ones. Only ELSEWHERE refutes a row; NOT_HEARD, "
                             "NO_ARCHIVE_COVERAGE and NOT_QUERIED do not. A trace proves "
                             "presence, never purpose, never occupancy.",
                   "counts": dict(counts), "on_ground_corroborations": ground_hits,
                   "rows": results}, fh, indent=2)
        fh.write("\n")
    print(f"\nwrote {os.path.relpath(OUT_JSON, FOLLOWING)}")

    if args.write and not args.id:
        with open(OVERLAPS_CSV, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=fields)
            w.writeheader()
            w.writerows(rows)
        print(f"wrote {os.path.relpath(OVERLAPS_CSV, FOLLOWING)}")


if __name__ == "__main__":
    main()
