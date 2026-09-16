#!/usr/bin/env python3
"""Build the PUBLIC tables for the Egyptian fleet's United States flying, 2022-2025.

The raw AeroAPI responses and the flown paths stay in the private store - FlightAware's
terms do not allow republishing them. What this writes is OURS: counts, dates, airports
and per-flight summaries computed from their answer, in our own columns.

    python3 build_fleet_us_tables.py            print the tables
    python3 build_fleet_us_tables.py --write    also write them under ../data/flightaware_derived/

THE POINT OF THE DENOMINATOR. Every earlier pull asked "was this tail at this field on
this claimed date?" - a question that can only ever confirm or refute somebody else's
list. These tables answer the one nobody had asked: how often were these aircraft in the
United States AT ALL across the years the tally is counted over. A visit count is not a
finding about a person, and none of these rows places anyone aboard anything.
"""
import csv, glob, json, os, sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from private_store import private_vendor_dir  # noqa: E402

RAW = private_vendor_dir("flightaware")
OUT = os.path.normpath(os.path.join(HERE, "..", "data", "flightaware_derived"))
GAZ = os.path.normpath(os.path.join(HERE, "..", "..", "public_open_source", "data", "ourairports", "airports.csv"))
TAILS = ["SU-BTT", "SU-BND", "SU-BTU", "SU-BTV", "SU-BGM"]
YEARS = ["2022", "2023", "2024", "2025"]


def is_us(code):
    return bool(code) and (code.startswith(("TJ", "TI")) or (len(code) == 4 and code[0] in ("K", "P")))


def gazetteer():
    out = {}
    if not os.path.exists(GAZ):
        return out
    for r in csv.DictReader(open(GAZ, encoding="utf-8")):
        if r.get("ident"):
            out[r["ident"]] = (r.get("name", ""), r.get("municipality", ""), (r.get("iso_region") or "").split("-")[-1])
    return out


def flights():
    """Every flight held for the five tails, de-duplicated by the vendor's flight id."""
    seen = {}
    for tail in TAILS:
        for path in sorted(glob.glob(os.path.join(RAW, tail, "*_history_p*.json"))):
            try:
                body = json.load(open(path))
            except Exception:
                continue
            for f in body.get("flights") or []:
                if f.get("fa_flight_id"):
                    seen[f["fa_flight_id"]] = (tail, f)
    return seen


def track_summary(tail, fid):
    """Our summary of a flown path. The positions themselves are not published."""
    p = os.path.join(RAW, tail, "tracks", f"{fid}_track.json")
    if not os.path.exists(p):
        return {}
    try:
        pos = json.load(open(p)).get("positions") or []
    except Exception:
        return {}
    alts = [x["altitude"] for x in pos if isinstance(x.get("altitude"), (int, float))]
    return {
        "path_positions": len(pos),
        "path_max_altitude_ft": max(alts) * 100 if alts else "",
        "path_first_utc": pos[0].get("timestamp", "") if pos else "",
        "path_last_utc": pos[-1].get("timestamp", "") if pos else "",
    }


def main():
    write = "--write" in sys.argv
    gaz = gazetteer()
    rows, us_rows = [], []
    for fid, (tail, f) in flights().items():
        o, d = f.get("origin") or {}, f.get("destination") or {}
        oc = o.get("code_icao") or o.get("code") or ""
        dc = d.get("code_icao") or d.get("code") or ""
        r = {
            "tail": tail,
            "date_utc": (f.get("actual_off") or f.get("scheduled_out") or "")[:10],
            "callsign": f.get("ident") or "",
            "from_icao": oc, "from_place": gaz.get(oc, ("", o.get("city") or "", ""))[1] or (o.get("city") or ""),
            "from_state": gaz.get(oc, ("", "", ""))[2],
            "to_icao": dc, "to_place": gaz.get(dc, ("", d.get("city") or "", ""))[1] or (d.get("city") or ""),
            "to_state": gaz.get(dc, ("", "", ""))[2],
            "off_utc": f.get("actual_off") or "", "on_utc": f.get("actual_on") or "",
            "status": f.get("status") or "",
            "us_leg": "yes" if (is_us(oc) or is_us(dc)) else "no",
            "us_end": "both" if is_us(oc) and is_us(dc) else ("arrival" if is_us(dc) else ("departure" if is_us(oc) else "")),
        }
        if r["us_leg"] == "yes":
            r.update(track_summary(tail, fid))
        rows.append(r)
    rows.sort(key=lambda r: (r["date_utc"], r["tail"], r["off_utc"]))
    us_rows = [r for r in rows if r["us_leg"] == "yes"]

    # 1. per tail
    print(f"{'tail':8} {'flights':>7} {'US legs':>7} {'US days':>7}   first US leg   last US leg")
    for t in TAILS:
        fl = [r for r in rows if r["tail"] == t]
        us = [r for r in fl if r["us_leg"] == "yes"]
        days = sorted({r["date_utc"] for r in us if r["date_utc"]})
        print(f"{t:8} {len(fl):7} {len(us):7} {len(days):7}   {days[0] if days else '-':12}   {days[-1] if days else '-'}")

    # 2. per airport per year
    ap = defaultdict(Counter)
    for r in us_rows:
        for c in (r["from_icao"], r["to_icao"]):
            if is_us(c):
                ap[c][r["date_utc"][:4]] += 1
    print(f"\n{'airport':8} {'2022':>5} {'2023':>5} {'2024':>5} {'2025':>5} {'total':>6}  place")
    for c, yrs in sorted(ap.items(), key=lambda kv: -sum(kv[1].values())):
        name, place, state = gaz.get(c, ("", "", ""))
        print(f"{c:8} {yrs['2022']:5} {yrs['2023']:5} {yrs['2024']:5} {yrs['2025']:5} {sum(yrs.values()):6}  {place}{', ' + state if state else ''}")

    # 3. how they enter and leave
    print("\nhow they reach the country and how they leave:")
    routes = Counter()
    for r in us_rows:
        if is_us(r["to_icao"]) and not is_us(r["from_icao"]):
            routes[f"IN   {r['from_icao'] or '?'} -> {r['to_icao']}"] += 1
        if is_us(r["from_icao"]) and not is_us(r["to_icao"]):
            routes[f"OUT  {r['from_icao']} -> {r['to_icao'] or '?'}"] += 1
    for k, n in routes.most_common(15):
        print(f"  {k:26} {n}")

    # 4. more than one of them in the country on the same day
    byday = defaultdict(set)
    for r in us_rows:
        byday[r["date_utc"]].add(r["tail"])
    multi = {d: t for d, t in byday.items() if len(t) > 1}
    print(f"\ndays with two or more of these aircraft in the United States: {len(multi)}")
    for d in sorted(multi):
        print(f"  {d}  {', '.join(sorted(multi[d]))}")

    held = [r for r in us_rows if "path_positions" in r]
    empty = [r for r in held if not r["path_positions"]]
    print(f"\nUnited States legs with a flown path held: {len(held)} of {len(us_rows)}; "
          f"{sum(r['path_positions'] for r in held):,} recorded positions"
          + (f"; {len(empty)} path(s) came back with no positions at all" if empty else ""))

    if write:
        os.makedirs(OUT, exist_ok=True)
        cols = ["tail", "date_utc", "callsign", "from_icao", "from_place", "from_state", "to_icao", "to_place",
                "to_state", "off_utc", "on_utc", "status", "us_leg", "us_end",
                "path_positions", "path_max_altitude_ft", "path_first_utc", "path_last_utc"]
        with open(os.path.join(OUT, "us_flights.csv"), "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
            w.writeheader()
            w.writerows(us_rows)
        with open(os.path.join(OUT, "flights_by_tail_year.csv"), "w", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["tail", "year", "flights_total", "us_legs", "us_days"])
            for t in TAILS:
                for y in YEARS:
                    fl = [r for r in rows if r["tail"] == t and r["date_utc"][:4] == y]
                    us = [r for r in fl if r["us_leg"] == "yes"]
                    w.writerow([t, y, len(fl), len(us), len({r["date_utc"] for r in us})])
        with open(os.path.join(OUT, "us_airports_by_year.csv"), "w", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["airport_icao", "place", "state"] + YEARS + ["total"])
            for c, yrs in sorted(ap.items(), key=lambda kv: -sum(kv[1].values())):
                name, place, state = gaz.get(c, ("", "", ""))
                w.writerow([c, place, state] + [yrs[y] for y in YEARS] + [sum(yrs.values())])
        print(f"\nwrote us_flights.csv, flights_by_tail_year.csv, us_airports_by_year.csv to {OUT}")


if __name__ == "__main__":
    main()
