#!/usr/bin/env python3
"""Turn the whole-aircraft sweep into the two things the claim actually needs:
every United States flight these aircraft made, and the denominator underneath it.

The per-claim pulls could only ever answer "was this tail at this field that day?".
This reads every window the sweep bought and answers the question nobody had asked:
HOW OFTEN were these aircraft in the United States at all, across the years the
"73 overlaps" tally is counted over?

    python3 analyse_fleet_us.py                 read the private store, print the summary
    python3 analyse_fleet_us.py --write         also write the CSVs beside the raw data

WHAT COUNTS AS A UNITED STATES FLIGHT. The ICAO prefix K is the contiguous US; P is
Alaska, Hawaii and the Pacific territories; TJ is Puerto Rico and TI the US Virgin
Islands. A flight counts if EITHER end is one of those. Legs with no airport code at
one end - FlightAware sometimes has only a position - are counted separately and named,
never silently dropped.

THE RAW RESPONSES STAY PRIVATE. This writes derived tables: our own columns, computed
from their answer. The published restatement of each response is a different file
(see p_restate_flight_data.md).
"""
import csv, glob, json, os, re, sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from private_store import private_vendor_dir  # noqa: E402

RAW = private_vendor_dir("flightaware")
TAILS = ["SU-BTT", "SU-BND", "SU-BTU", "SU-BTV", "SU-BGM"]
US_PREFIX = ("K", "P", "TJ", "TI")
WINDOW = re.compile(r"(\d{4}-\d{2}-\d{2})_to_(\d{4}-\d{2}-\d{2})_history_p(\d+)\.json$")


def is_us(code):
    if not code:
        return False
    return code.startswith(("TJ", "TI")) or (len(code) == 4 and code[0] in ("K", "P"))


def flights_for(tail):
    """Every flight in every window on disk for this tail, de-duplicated by fa_flight_id."""
    seen = {}
    for path in sorted(glob.glob(os.path.join(RAW, tail, "*_history_p*.json"))):
        m = WINDOW.search(os.path.basename(path))
        if not m:
            continue
        try:
            body = json.load(open(path))
        except Exception:
            continue
        for f in body.get("flights") or []:
            fid = f.get("fa_flight_id")
            if fid:
                seen[fid] = f
    return seen


def row(tail, f):
    o, d = f.get("origin") or {}, f.get("destination") or {}
    oc, dc = o.get("code_icao") or o.get("code"), d.get("code_icao") or d.get("code")
    return {
        "tail": tail,
        "fa_flight_id": f.get("fa_flight_id"),
        "callsign": f.get("ident"),
        "off_utc": f.get("actual_off") or "",
        "on_utc": f.get("actual_on") or "",
        "date_utc": (f.get("actual_off") or f.get("scheduled_out") or "")[:10],
        "origin_icao": oc or "",
        "origin_city": o.get("city") or "",
        "destination_icao": dc or "",
        "destination_city": d.get("city") or "",
        "us_leg": "yes" if (is_us(oc) or is_us(dc)) else "no",
        "us_end": "both" if is_us(oc) and is_us(dc) else ("arrival" if is_us(dc) else ("departure" if is_us(oc) else "")),
        "missing_airport": "yes" if not (oc and dc) else "no",
        "status": f.get("status") or "",
        "distance_miles": (f.get("route_distance") or ""),
        "aircraft_type": f.get("aircraft_type") or "",
    }


def main():
    write = "--write" in sys.argv
    all_rows, per_tail = [], {}
    for tail in TAILS:
        fl = flights_for(tail)
        rows = sorted((row(tail, f) for f in fl.values()), key=lambda r: (r["date_utc"], r["off_utc"]))
        per_tail[tail] = rows
        all_rows += rows

    us_rows = [r for r in all_rows if r["us_leg"] == "yes"]
    print(f"raw windows on disk: {len(glob.glob(os.path.join(RAW, 'SU-*', '*_history_p*.json')))}")
    print(f"flights held: {len(all_rows)}   United States legs: {len(us_rows)}")
    print()
    print(f"{'tail':8} {'flights':>7} {'US legs':>7} {'US days':>7} {'first':>10} {'last':>10}")
    for tail in TAILS:
        rows = per_tail[tail]
        us = [r for r in rows if r["us_leg"] == "yes"]
        days = {r["date_utc"] for r in us if r["date_utc"]}
        dates = [r["date_utc"] for r in rows if r["date_utc"]]
        print(f"{tail:8} {len(rows):7} {len(us):7} {len(days):7} {min(dates) if dates else '-':>10} {max(dates) if dates else '-':>10}")

    print("\nUnited States legs by year:")
    by_year = defaultdict(Counter)
    for r in us_rows:
        if r["date_utc"]:
            by_year[r["date_utc"][:4]][r["tail"]] += 1
    for y in sorted(by_year):
        line = "  ".join(f"{t} {n}" for t, n in sorted(by_year[y].items()))
        print(f"  {y}: {sum(by_year[y].values()):3}   {line}")

    print("\nUnited States airports used, most visited first:")
    ap = Counter()
    for r in us_rows:
        for code in (r["origin_icao"], r["destination_icao"]):
            if is_us(code):
                ap[code] += 1
    for code, n in ap.most_common(25):
        print(f"  {code:6} {n}")

    miss = [r for r in all_rows if r["missing_airport"] == "yes"]
    if miss:
        print(f"\nlegs with an end FlightAware gives no airport for: {len(miss)} (kept, flagged in the CSV)")

    if write:
        out_all = os.path.join(RAW, "_fleet_flights.csv")
        out_us = os.path.join(RAW, "_fleet_us_flights.csv")
        cols = list(all_rows[0].keys()) if all_rows else []
        for path, rows in ((out_all, all_rows), (out_us, us_rows)):
            with open(path, "w", newline="") as fh:
                w = csv.DictWriter(fh, fieldnames=cols)
                w.writeheader()
                w.writerows(rows)
            print(f"wrote {path} ({len(rows)} rows)")


if __name__ == "__main__":
    main()
