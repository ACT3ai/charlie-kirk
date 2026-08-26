#!/usr/bin/env python3
"""Pull the ADS-B aircraft-days that the CLAIMED OVERLAPS need.

`fetch_event_windows.py` walks the TPUSA speaking calendar. That is the right
spine for "was a jet at an event", but it is the WRONG spine for auditing the
claimed-overlap ledger: a claim can name a date that is not a speaking date at
all, and every such row then sits at NEVER ASKED forever. Nine of the eighty
dated rows in overlaps.csv were in exactly that state.

This script closes that gap and nothing else. It reads overlaps.csv, takes every
(claimed tail, claimed date +/- 1 day) pair, skips what is already on disk, and
pulls the rest from the two free historical archives -- reusing
fetch_event_windows.py's own fetch/save so the on-disk conventions, the miss
records and the meta files are byte-identical to every other pull.

    python3 fetch_overlap_days.py --plan
    python3 fetch_overlap_days.py --run
    python3 fetch_overlap_days.py --run --control   same dates, control airframes

THE CONTROL RUN IS NOT OPTIONAL. An archive that has nothing for SU-BTT on a
date and nothing for a Ryanair 737 on the same date is an ARCHIVE LIMIT, not a
missing aircraft. Run --control over the same dates before any absence here is
described in public as anything at all.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from fetch_event_windows import (          # noqa: E402
    CONTROLS, SOURCES, already_have, fetch, load_fleet, save,
)

FOLLOWING = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
OVERLAPS_CSV = os.path.join(FOLLOWING, "overlaps.csv")

TAIL_RE = re.compile(r"SU-[A-Z]{3}")


def claim_days(window=1):
    """{tail -> sorted[date]} for every dated, tailed row in overlaps.csv.

    A row that names two tails ("SU-BTT or SU-BND") needs BOTH asked: the claim
    is that one of them was there, and only asking both can answer it.
    """
    need = {}
    with open(OVERLAPS_CSV, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            day = (r["date"] or "").strip()
            if len(day) != 10 or day == "UNKNOWN":
                continue
            tails = TAIL_RE.findall((r["foreign_tail"] or "").upper())
            if not tails:
                continue
            base = dt.date.fromisoformat(day)
            for t in tails:
                for k in range(-window, window + 1):
                    need.setdefault(t, set()).add((base + dt.timedelta(days=k)).isoformat())
    return {t: sorted(d) for t, d in sorted(need.items())}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--window", type=int, default=1)
    ap.add_argument("--control", action="store_true")
    ap.add_argument("--sleep", type=float, default=0.4)
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    need = claim_days(args.window)
    hexes = {a["reg"]: a["hex"] for a in load_fleet()}

    jobs = []
    if args.control:
        every = sorted({d for days in need.values() for d in days})
        for ac in CONTROLS:
            for day in every:
                for source, tmpl in SOURCES:
                    if already_have(ac["reg"], day, source):
                        continue
                    y, m, dd = day.split("-")
                    jobs.append((ac["reg"], day, source,
                                 tmpl.format(y=y, m=m, d=dd, t2=ac["hex"][-2:], hex=ac["hex"])))
    else:
        for tail, days in need.items():
            hx = hexes.get(tail)
            if not hx:
                print(f"  !! {tail} is not in lib/fleet.js - cannot resolve its ICAO hex")
                continue
            for day in days:
                for source, tmpl in SOURCES:
                    if already_have(tail, day, source):
                        continue
                    y, m, dd = day.split("-")
                    jobs.append((tail, day, source,
                                 tmpl.format(y=y, m=m, d=dd, t2=hx[-2:], hex=hx)))

    days_in_scope = (len({d for ds in need.values() for d in ds}) * len(CONTROLS)
                     if args.control else sum(len(d) for d in need.values()))
    total = days_in_scope * len(SOURCES)
    print(f"{len(CONTROLS) if args.control else len(need)} tails, {days_in_scope} "
          f"aircraft-days x {len(SOURCES)} archives = {total} requests in scope")
    print(f"{len(jobs)} still needed ({total - len(jobs)} already on disk)")
    if args.limit:
        jobs = jobs[:args.limit]
    if args.plan or not args.run:
        for j in jobs[:20]:
            print(f"  {j[0]:8} {j[1]} {j[2]:16} {j[3]}")
        if len(jobs) > 20:
            print(f"  ... and {len(jobs) - 20} more")
        return

    hits = misses = errors = 0
    for i, (reg, day, source, url) in enumerate(jobs, 1):
        status, body = fetch(url)
        save(reg, day, source, url, status, body)
        if status == 200:
            hits += 1
        elif status in (403, 404):
            misses += 1
        else:
            errors += 1
        print(f"  {i}/{len(jobs)} {reg:8} {day} {source:16} HTTP {status} "
              f"{len(body or b''):>8} B", flush=True)
        time.sleep(args.sleep)

    print(f"\nDONE  {hits} traces recovered, {misses} days the archives do not hold, "
          f"{errors} transport errors")
    if misses and not args.control:
        print("\nBEFORE ANY OF THOSE MISSES IS DESCRIBED IN PUBLIC, RUN:\n"
              "  python3 fetch_overlap_days.py --run --control")


if __name__ == "__main__":
    main()
