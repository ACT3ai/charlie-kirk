#!/usr/bin/env python3
"""Find every time an Egyptian jet and a Kirk-side aircraft were at the same place at the
same time, 2022-2025.

This is the question the following-planes claim actually makes. Not "were two Egyptian
jets together" - nobody claims that - but "did an Egyptian jet sit on the same ramp as a
plane carrying Charlie Kirk, Erika Kirk or their organisation".

    python3 find_egypt_kirk_overlaps.py            print the overlaps and the coverage
    python3 find_egypt_kirk_overlaps.py --write    also write the CSVs to the private store

THE TWO HALVES COME FROM DIFFERENT PLACES, ON PURPOSE.
  * The Egyptian side is FlightAware's record from the whole-aircraft sweep: an actual
    arrival and an actual departure at every United States airport, 2022-2025. Complete
    for those years - none of the five tails is blocked.
  * The Kirk side cannot come from FlightAware: N102DZ, N582MM and N888KG are on its block
    list and return nothing. It comes from the free volunteer ADS-B archives instead, via
    master_proximity.csv - one row per aircraft per ground contact, with the first and last
    time a receiver heard it on the ground at a named field.

THE KIRK SIDE IS INCOMPLETE, AND THIS SCRIPT SAYS SO ON EVERY ROW. A volunteer archive
holds only the days somebody's receiver heard the aircraft. So for every Egyptian stay the
coverage of each Kirk-side tail is reported three ways - a trace HELD for those days, the
archives ASKED and empty, or NEVER ASKED. Only the first two mean anything. "No overlap
found" on a never-asked day is an unanswered question, not a negative.

TIERS, strongest first:
  A  BOTH ON THE GROUND AT THE SAME AIRPORT AT THE SAME TIME
  B  SAME AIRPORT, within 24 hours of the Egyptian stay
  C  SAME AIRPORT, within 3 days of the Egyptian stay
  D  NEARBY AIRPORT (within 50 km), within 24 hours

A shared ramp shows two aircraft were near each other. It shows nothing about who was
aboard either one, or why.
"""
import csv, glob, json, math, os, re, sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from private_store import private_vendor_dir  # noqa: E402

RAW = private_vendor_dir("flightaware")
FOLLOWING = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
PLANES = os.path.normpath(os.path.join(FOLLOWING, ".."))
PROX = os.path.join(FOLLOWING, "apis", "public_open_source", "data", "analysis", "master_proximity.csv")
GAZ = os.path.join(FOLLOWING, "apis", "public_open_source", "data", "ourairports", "airports.csv")

EGYPT = ["SU-BTT", "SU-BND", "SU-BTU", "SU-BTV", "SU-BGM"]
# The Kirk / TPUSA side as lib/fleet.js declares it. The label travels with every row so a
# donor's jet is never reported as though it were the Kirks' own.
KIRK = {
    "N102DZ": "Kirk family (reported)",
    "N582MM": "TPUSA-linked",
    "N560TW": "donor-linked",
    "N888KG": "Provo departure 10 Sep (separate claim)",
    "N872RA": "Provo arrival 10 Sep",
    "N40JD": "Provo arrival 10 Sep",
}
NEAR_KM = 50
DAY = timedelta(days=1)


def ts(s):
    if not s:
        return None
    s = s.replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(s)
    except ValueError:
        return None


def is_us(code):
    return bool(code) and (code.startswith(("TJ", "TI")) or (len(code) == 4 and code[0] in ("K", "P")))


def gazetteer():
    out = {}
    for r in csv.DictReader(open(GAZ, encoding="utf-8")):
        try:
            out[r["ident"]] = (float(r["latitude_deg"]), float(r["longitude_deg"]), r.get("municipality", ""), (r.get("iso_region") or "").split("-")[-1])
        except (ValueError, KeyError):
            pass
    return out


def km(a, b, gaz):
    if a not in gaz or b not in gaz:
        return None
    la1, lo1 = gaz[a][:2]
    la2, lo2 = gaz[b][:2]
    p = math.radians
    h = math.sin(p(la2 - la1) / 2) ** 2 + math.cos(p(la1)) * math.cos(p(la2)) * math.sin(p(lo2 - lo1) / 2) ** 2
    return 6371 * 2 * math.asin(math.sqrt(h))


def egyptian_stays():
    """Every stay on the ground at a US airport: from the flight that arrived to the flight
    that next left the same field. A stay whose departure is not in the record is kept,
    open-ended, and flagged."""
    stays = []
    for tail in EGYPT:
        seen = {}
        for p in glob.glob(os.path.join(RAW, tail, "*_history_p*.json")):
            try:
                for f in json.load(open(p)).get("flights") or []:
                    if f.get("fa_flight_id"):
                        seen[f["fa_flight_id"]] = f
            except Exception:
                continue
        fl = sorted(seen.values(), key=lambda f: f.get("actual_off") or f.get("scheduled_out") or "")
        for i, f in enumerate(fl):
            dest = (f.get("destination") or {}).get("code_icao") or (f.get("destination") or {}).get("code") or ""
            if not is_us(dest):
                continue
            arrive = ts(f.get("actual_on")) or ts(f.get("estimated_on"))
            if not arrive:
                continue
            leave, closed = None, False
            for g in fl[i + 1:]:
                org = (g.get("origin") or {}).get("code_icao") or (g.get("origin") or {}).get("code") or ""
                if org == dest:
                    leave, closed = ts(g.get("actual_off")) or ts(g.get("scheduled_out")), True
                break
            stays.append({"tail": tail, "airport": dest, "arrive": arrive,
                          "leave": leave or arrive + timedelta(hours=2), "leave_known": closed,
                          "from": (f.get("origin") or {}).get("code_icao") or ""})
    return sorted(stays, key=lambda s: s["arrive"])


def kirk_contacts():
    out = []
    for r in csv.DictReader(open(PROX, encoding="utf-8")):
        if r["tail"] not in KIRK:
            continue
        a, b = ts(r["first_seen_utc"]), ts(r["last_seen_utc"])
        if a and b and r.get("airport_code"):
            out.append({"tail": r["tail"], "airport": r["airport_code"], "first": a, "last": b,
                        "sources": r.get("sources", "")})
    return out


def trace_contacts(tails, airports, gaz, near_km=3.0):
    """Ground contacts read straight from the recovered traces, for the airports the
    Egyptian jets used. master_proximity.csv is built by a longer chain that is not rerun
    here, so traces fetched after it was built would otherwise be invisible. A contact is a
    run of positions flagged on the ground within near_km of the field's reference point."""
    import gzip as _gz
    fields = {a: gaz[a][:2] for a in airports if a in gaz}
    out = []
    for tail in tails:
        d = os.path.join(PLANES, tail, "data", "recovered")
        try:
            names = os.listdir(d)
        except FileNotFoundError:
            continue
        for n in names:
            if not re.search(r"_trace_full\.json(\.gz)?$", n) or ".miss." in n:
                continue
            p = os.path.join(d, n)
            try:
                raw = open(p, "rb").read()
                try:
                    raw = _gz.decompress(raw)
                except Exception:
                    pass
                j = json.loads(raw)
            except Exception:
                continue
            base = j.get("timestamp")
            if base is None:
                continue
            run = None
            for pt in j.get("trace", []):
                if len(pt) < 4 or pt[3] != "ground":
                    if run:
                        out.append(run)
                        run = None
                    continue
                t = datetime.fromtimestamp(base + pt[0], tz=timezone.utc)
                hit = None
                for code, (la, lo) in fields.items():
                    if abs(la - pt[1]) > 0.05 or abs(lo - pt[2]) > 0.07:
                        continue
                    h = math.sin(math.radians(pt[1] - la) / 2) ** 2 + math.cos(math.radians(la)) * math.cos(math.radians(pt[1])) * math.sin(math.radians(pt[2] - lo) / 2) ** 2
                    if 6371 * 2 * math.asin(math.sqrt(h)) <= near_km:
                        hit = code
                        break
                if hit is None:
                    if run:
                        out.append(run)
                        run = None
                    continue
                if run and run["airport"] == hit and (t - run["last"]).total_seconds() < 3 * 3600:
                    run["last"] = t
                else:
                    if run:
                        out.append(run)
                    run = {"tail": tail, "airport": hit, "first": t, "last": t, "sources": n.split("_")[2]}
            if run:
                out.append(run)
    return out


def coverage(tail, day_from, day_to):
    """held / asked_empty / never_asked for a Kirk-side tail across a span of UTC days."""
    d = os.path.join(PLANES, tail, "data", "recovered")
    try:
        names = os.listdir(d)
    except FileNotFoundError:
        return "never_asked"
    held, asked = set(), set()
    for n in names:
        m = re.search(r"_(\d{4}-\d{2}-\d{2})_", n)
        if not m:
            continue
        if ".miss." in n:
            asked.add(m.group(1))
        elif re.search(r"_trace_full\.json(\.gz)?$", n):
            held.add(m.group(1))
    days = set()
    x = day_from
    while x <= day_to:
        days.add(x.strftime("%Y-%m-%d"))
        x += DAY
    if days & held:
        return "held"
    if days <= asked:
        return "asked_empty"
    return "never_asked"


def main():
    write = "--write" in sys.argv
    gaz = gazetteer()
    stays = [s for s in egyptian_stays() if s["arrive"].year <= 2025]
    for s in stays:
        s["parked"] = (s["leave"] - s["arrive"]).days > 9
    contacts = kirk_contacts()
    from_traces = trace_contacts(list(KIRK), {s["airport"] for s in stays}, gaz)
    known = {(c["tail"], c["airport"], c["first"].date()) for c in contacts}
    added = [c for c in from_traces if (c["tail"], c["airport"], c["first"].date()) not in known]
    contacts += added
    print(f"ground contacts read straight from traces and not already in master_proximity.csv: {len(added)}")
    matches = []
    for s in stays:
        for c in contacts:
            same = c["airport"] == s["airport"]
            dist = 0.0 if same else km(c["airport"], s["airport"], gaz)
            if dist is None or dist > NEAR_KM:
                continue
            overlap = c["first"] <= s["leave"] and c["last"] >= s["arrive"]
            gap_h = 0 if overlap else min(abs((c["first"] - s["leave"]).total_seconds()),
                                          abs((s["arrive"] - c["last"]).total_seconds())) / 3600
            if same and overlap:
                tier = "A"
            elif same and gap_h <= 24:
                tier = "B"
            elif same and gap_h <= 72:
                tier = "C"
            elif not same and gap_h <= 24:
                tier = "D"
            else:
                continue
            matches.append({**s, "kirk_tail": c["tail"], "kirk_label": KIRK[c["tail"]], "kirk_airport": c["airport"],
                            "kirk_first": c["first"], "kirk_last": c["last"], "km": round(dist, 1),
                            "gap_hours": round(gap_h, 1), "tier": tier, "kirk_sources": c["sources"]})
    # one row per (stay, kirk tail), keeping the strongest tier
    best = {}
    for m in matches:
        k = (m["tail"], m["airport"], m["arrive"], m["kirk_tail"])
        if k not in best or m["tier"] < best[k]["tier"] or (m["tier"] == best[k]["tier"] and m["gap_hours"] < best[k]["gap_hours"]):
            best[k] = m
    rows = sorted(best.values(), key=lambda m: (m["tier"], m["arrive"]))

    print(f"Egyptian US ground stays 2022-2025: {len(stays)} ({sum(1 for s in stays if not s['leave_known'])} with no departure in the record)")
    print(f"Kirk-side ground contacts held: {len(contacts)} across {len({c['tail'] for c in contacts})} tails\n")
    names = {"A": "BOTH ON THE GROUND, SAME AIRPORT, SAME TIME", "B": "SAME AIRPORT, within 24 h",
             "C": "SAME AIRPORT, within 3 days", "D": f"NEARBY AIRPORT (<= {NEAR_KM} km), within 24 h"}
    parked_rows = [r for r in rows if r.get("parked")]
    rows_visits = [r for r in rows if not r.get("parked")]
    for t in "ABCD":
        tr = [r for r in rows_visits if r["tier"] == t]
        print(f"=== TIER {t} - {names[t]}: {len(tr)}")
        for r in tr:
            place = gaz.get(r["airport"], (0, 0, "", ""))
            open_end = "" if r["leave_known"] else "?"
            gap = "" if t == "A" else "  gap %s h" % r["gap_hours"]
            dist = "" if r["km"] == 0 else "  %s km" % r["km"]
            print(f"  {r['arrive']:%Y-%m-%d}  {r['tail']:7} at {r['airport']} {place[2]} {place[3]}  "
                  f"{r['arrive']:%H:%MZ}-{r['leave']:%m-%d %H:%MZ}{open_end}  |  "
                  f"{r['kirk_tail']:7} ({r['kirk_label']}) at {r['kirk_airport']} "
                  f"{r['kirk_first']:%m-%d %H:%MZ}-{r['kirk_last']:%H:%MZ}{gap}{dist}")
        print()

    print(f"=== PARKED - Egyptian jet on the ground for more than 9 days (a layup, not a visit): {len(parked_rows)} Kirk-side contacts during those stays")
    for s in [s for s in stays if s["parked"]]:
        hits = [r for r in parked_rows if r["tail"] == s["tail"] and r["arrive"] == s["arrive"]]
        by = {}
        for r in hits:
            by.setdefault(r["kirk_tail"], []).append(r)
        summary = ", ".join(f"{k} x{len(v)}" for k, v in sorted(by.items())) or "none observed"
        print(f"  {s['tail']:7} parked at {s['airport']} {s['arrive']:%Y-%m-%d} -> {s['leave']:%Y-%m-%d} "
              f"({(s['leave'] - s['arrive']).days} days) | Kirk-side contacts at that field meanwhile: {summary}")
    print()

    # coverage: for every Egyptian stay, could each Kirk tail have been seen at all?
    cov = defaultdict(lambda: defaultdict(int))
    cov_rows = []
    for s in stays:
        d0 = (s["arrive"] - DAY).replace(hour=0, minute=0, second=0, microsecond=0)
        d1 = (s["leave"] + DAY).replace(hour=0, minute=0, second=0, microsecond=0)
        rec = {"tail": s["tail"], "airport": s["airport"], "arrive_utc": s["arrive"].isoformat(), "leave_utc": s["leave"].isoformat()}
        for k in KIRK:
            state = coverage(k, d0, d1)
            cov[k][state] += 1
            rec[f"{k}_coverage"] = state
        cov_rows.append(rec)
    print("=== KIRK-SIDE COVERAGE across the Egyptian stays (+/- 1 day)")
    print(f"  {'tail':7} {'held':>6} {'asked, empty':>13} {'never asked':>12}")
    for k in KIRK:
        c = cov[k]
        print(f"  {k:7} {c['held']:6} {c['asked_empty']:13} {c['never_asked']:12}   {KIRK[k]}")

    if write:
        out = os.path.join(RAW, "_egypt_kirk_overlaps.csv")
        cols = ["tier", "tail", "airport", "arrive", "leave", "leave_known", "from", "kirk_tail", "kirk_label",
                "kirk_airport", "kirk_first", "kirk_last", "km", "gap_hours", "kirk_sources"]
        with open(out, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
            w.writeheader()
            for r in rows:
                w.writerow({**r, "arrive": r["arrive"].isoformat(), "leave": r["leave"].isoformat(),
                            "kirk_first": r["kirk_first"].isoformat(), "kirk_last": r["kirk_last"].isoformat()})
        out2 = os.path.join(RAW, "_egypt_stays_kirk_coverage.csv")
        with open(out2, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(cov_rows[0].keys()))
            w.writeheader()
            w.writerows(cov_rows)
        print(f"\nwrote {out}\nwrote {out2}")


if __name__ == "__main__":
    main()
