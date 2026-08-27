#!/usr/bin/env python3
"""What the geographic sweep actually says, with the control comparison attached.

`geo_sweep.py` produces one CSV per UTC day: every aircraft that entered a
50-mile circle around a Charlie Kirk / TPUSA event city, and every aircraft that
entered the same-sized circle around six control cities on the same day. This
turns that pile into the three questions worth asking of it.

    python3 analyse_geo_sweep.py                    all three
    python3 analyse_geo_sweep.py --recurrence       just the repeat visitors
    python3 analyse_geo_sweep.py --min-events 3
    python3 analyse_geo_sweep.py --json             machine-readable, to data/

1. RATE: how many notable aircraft sit on the ground inside an EVENT circle per
   circle-day, against the same figure for a CONTROL circle-day. This is the
   only number that can make "foreign jets were near the event" mean anything,
   and it is computed first so it cannot be left out.

2. RECURRENCE: which aircraft appear on the ground near MORE THAN ONE event, in
   more than one state, on separate dates. This is the question the whole
   following-planes claim is really making, and per-tail archive probing could
   never ask it, because you have to already suspect a tail to probe it.

3. WHAT THE CONTROL DOES TO THE RECURRENCE LIST. An aircraft that recurs near
   events and ALSO recurs near Des Moines and Spokane is a busy charter
   aircraft, not a shadow. Recurrence alone is not a finding; recurrence that
   the controls do not reproduce is the beginning of one.

THREE READINGS THAT ARE NOT AVAILABLE FROM THIS OUTPUT, EVER
------------------------------------------------------------
  * A trace proves presence. Not purpose, not tasking, not who was aboard.
  * Event cities are not random: they are big metros, university towns and
    conference venues, and busy fields draw busy aircraft. A control city is a
    weak control, not a matched one, and the comparison is a floor rather than
    a significance test.
  * An aircraft absent from this data was not necessarily absent from the sky.
    Volunteer receiver coverage is wherever volunteers live, and ground coverage
    is the weakest coverage there is.
"""
from __future__ import annotations

import argparse
import collections
import csv
import gzip
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOTS = [os.path.join(HERE, "..", "data", "geo_sweep"),
         os.path.join(HERE, "..", "data", "geo_sweep_samples")]
OUT = os.path.join(HERE, "..", "data", "geo_sweep", "analysis.json")

# The fleet already on this site. Recurrence for these is not news -- it is the
# claim being tested -- so they are reported in their own block rather than
# padding the discovery list.
KNOWN = "tracked_fleet:"


def rows():
    for root in ROOTS:
        root = os.path.normpath(root)
        if not os.path.isdir(root):
            continue
        for day in sorted(os.listdir(root)):
            d = os.path.join(root, day)
            if not os.path.isdir(d):
                continue
            mp = os.path.join(d, "_sweep.meta.json")
            if os.path.exists(mp):
                try:
                    if json.load(open(mp)).get("status") not in (
                            "SWEPT", "NO_RELEASE_FOR_THIS_DATE"):
                        continue      # TRUNCATED / PROBE_UNRESOLVED: an open question,
                except Exception:     # not a result. Never fold it into a total.
                    continue
            for name in ("hits.csv.gz", "hits.csv"):
                p = os.path.join(d, name)
                if not os.path.exists(p):
                    continue
                fh = gzip.open(p, "rt", newline="") if p.endswith(".gz") else open(p, newline="")
                with fh:
                    for r in csv.DictReader(fh):
                        r["_source"] = os.path.basename(root)
                        yield r
                break


# Scheduled airliners. A 50-mile circle around Grapevine TX is a circle around
# DFW, and a sweep of it returns Qatar, Emirates, Lufthansa and British Airways
# widebodies on the ground every single day. They are not a finding, they are an
# airline timetable. Tagged rather than deleted, and both figures are reported,
# because the tag is a heuristic on the type code and heuristics get things
# wrong -- a head-of-state aircraft is very often an airliner type.
AIRLINER_TYPES = (
    "A19", "A20", "A21", "A22", "A30", "A31", "A32", "A33", "A34", "A35", "A38",
    "B37", "B38", "B39", "B73", "B74", "B75", "B76", "B77", "B78", "BCS",
    "CRJ", "CR7", "CR9", "DH8", "AT4", "AT5", "AT7", "E17", "E19", "E29",
    "E75", "E90", "E95", "MD8", "MD9", "B461", "B462", "B463",
)
AIRLINE_WORDS = ("AIRLINE", "AIRWAYS", "AIR CANADA", "WESTJET", "LUFTHANSA", "EMIRATES",
                 "QATAR", "DELTA", "UNITED AIR", "AMERICAN AIR", "SOUTHWEST",
                 "ALASKA AIR", "JETBLUE", "SPIRIT", "FRONTIER", "AER LINGUS",
                 "KLM", "BRITISH AIR", "AIR FRANCE", "TURKISH", "SUNWING",
                 "PORTER AIR", "FLAIR", "AIR TRANSAT", "CARGO", "FEDERAL EXPRESS",
                 "UNITED PARCEL", "ATLAS AIR", "KALITTA", "AIRBUS", "BOEING COMPANY")


def is_airliner(r):
    t = (r.get("type") or "").upper()
    own = (r.get("own_op") or "").upper()
    return t.startswith(AIRLINER_TYPES) or any(w in own for w in AIRLINE_WORDS)


def is_ground(r):
    return r["on_ground_in_circle"] == "True"


def notable(r):
    """Foreign, unregistered, non-ICAO, military or PIA. Deliberately EXCLUDES a
    bare LADD flag: LADD is a request to the FAA to keep a tail off the
    commercial displays, and it is so common among US business jets that
    counting it here would drown everything else. LADD is counted separately
    below, where it is a finding about the tracking industry."""
    f = r["flag_reasons"]
    return any(k in f for k in ("non_us_registration", "no_registration",
                                "non_icao_address", "dbflag:military", "dbflag:PIA"))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--recurrence", action="store_true")
    ap.add_argument("--min-events", type=int, default=2)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    all_rows = list(rows())
    if not all_rows:
        print("no swept days on disk yet — run geo_sweep.py --run first")
        return

    ev = [r for r in all_rows if r["circle_kind"] == "event"]
    ct = [r for r in all_rows if r["circle_kind"] == "control"]
    ev_days = {(r["sweep_date"], r["circle_key"]) for r in ev}
    ct_days = {(r["sweep_date"], r["circle_key"]) for r in ct}

    def stats(rs, ndays):
        g = [r for r in rs if is_ground(r)]
        n_all = [r for r in g if notable(r)]
        n = [r for r in n_all if not is_airliner(r)]
        ladd = [r for r in g if "dbflag:LADD" in r["flag_reasons"]]
        return {
            "circle_days": ndays,
            "aircraft_entering": len({r["hex"] for r in rs}),
            "on_ground": len({r["hex"] for r in g}),
            "notable_on_ground_incl_airliners": len({r["hex"] for r in n_all}),
            "notable_on_ground": len({r["hex"] for r in n}),
            "ladd_on_ground": len({r["hex"] for r in ladd}),
            "notable_on_ground_per_circle_day": round(len(n) / ndays, 2) if ndays else 0,
            "ladd_on_ground_per_circle_day": round(len(ladd) / ndays, 2) if ndays else 0,
        }

    e, c = stats(ev, len(ev_days)), stats(ct, len(ct_days))

    if not args.recurrence:
        print("=" * 78)
        print("1. RATE — event circles against control circles, same days, same code")
        print("=" * 78)
        print(f"{'':44}{'EVENT':>16}{'CONTROL':>16}")
        for label, k in [("circle-days swept", "circle_days"),
                         ("distinct aircraft entering the circle", "aircraft_entering"),
                         ("distinct aircraft ON THE GROUND", "on_ground"),
                         ("  foreign/unreg/mil/PIA incl. airliners", "notable_on_ground_incl_airliners"),
                         ("  the same, SCHEDULED AIRLINERS REMOVED", "notable_on_ground"),
                         ("  of those, FAA LADD-listed", "ladd_on_ground"),
                         ("notable on the ground PER CIRCLE-DAY", "notable_on_ground_per_circle_day"),
                         ("LADD on the ground PER CIRCLE-DAY", "ladd_on_ground_per_circle_day")]:
            print(f"{label:44}{e[k]:>16}{c[k]:>16}")
        print()
        print("Read the last two rows and nothing else first. If the event and control")
        print("figures are close, a foreign-registered jet inside a 50-mile circle is an")
        print("ordinary feature of American airspace and no single instance of one means")
        print("anything on its own.")
        print()
        print(f"LADD note: {e['ladd_on_ground']} aircraft on the ground in event circles are")
        print("FAA LADD-listed — the commercial trackers are asked to suppress them, and do.")
        print("Every one of those is an aircraft that research starting at a paid tracker")
        print("would never have seen, and would never have known it did not see.")
        print()

    # ---- recurrence -------------------------------------------------------
    seen = collections.defaultdict(lambda: {"events": set(), "states": set(),
                                            "controls": set(), "reg": "", "type": "",
                                            "own": "", "reasons": set(), "fields": set()})
    for r in all_rows:
        if not (is_ground(r) and notable(r)) or is_airliner(r):
            continue
        s = seen[r["hex"]]
        s["reg"] = s["reg"] or r["reg"]
        s["type"] = s["type"] or r["type"]
        s["own"] = s["own"] or r["own_op"]
        s["reasons"].update(x for x in r["flag_reasons"].split("|") if x)
        if r["nearest_field"]:
            s["fields"].add(r["nearest_field"])
        if r["circle_kind"] == "event":
            s["events"].add((r["event_date"] or r["sweep_date"], r["city"], r["state"]))
            s["states"].add(r["state"])
        else:
            s["controls"].add(r["city"])

    recur = sorted(
        ((h, s) for h, s in seen.items()
         if len(s["events"]) >= args.min_events and len(s["states"]) >= 2),
        key=lambda kv: (-len(kv[1]["events"]), -len(kv[1]["states"])))

    print("=" * 78)
    print(f"2. RECURRENCE — on the ground near {args.min_events}+ events, in 2+ states")
    print("=" * 78)
    if not recur:
        print("Nothing yet. With the sweep still running this is a coverage statement and")
        print("nothing else; it becomes a result only when the target set is complete.")
    for h, s in recur[:60]:
        known = any(x.startswith(KNOWN) for x in s["reasons"])
        tag = "ALREADY TRACKED" if known else ("also near controls"
                                               if s["controls"] else "EVENTS ONLY")
        print(f"\n  {s['reg'] or h:12} {s['type']:6} {len(s['events'])} events, "
              f"{len(s['states'])} states   [{tag}]")
        if s["own"]:
            print(f"      operator: {s['own'][:66]}")
        print(f"      reasons: {', '.join(sorted(s['reasons']))[:80]}")
        for d, city, st in sorted(s["events"])[:12]:
            print(f"        {d}  {city}, {st}")
        if len(s["events"]) > 12:
            print(f"        ... and {len(s['events']) - 12} more")
        if s["controls"]:
            print(f"      ALSO on the ground near controls: {', '.join(sorted(s['controls']))}")
            print("      -> a busy aircraft, not a shadow. The control is doing its job here.")

    print()
    print("=" * 78)
    print("3. WHAT THIS LIST IS NOT")
    print("=" * 78)
    print("Recurrence is a starting point, not a finding. Event cities are big metros and")
    print("university towns, and the aircraft that recur near them are overwhelmingly the")
    print("aircraft that recur near everywhere — charter fleets, air ambulances, freight,")
    print("training aircraft and military transports on their ordinary business. An entry")
    print("marked EVENTS ONLY is worth a look. It is not yet worth a sentence on a page.")

    if args.json:
        json.dump({
            "event": e, "control": c,
            "recurrence": [{"hex": h, "reg": s["reg"], "type": s["type"], "operator": s["own"],
                            "events": sorted(s["events"]), "states": sorted(s["states"]),
                            "also_near_controls": sorted(s["controls"]),
                            "fields": sorted(s["fields"]),
                            "reasons": sorted(s["reasons"])} for h, s in recur],
        }, open(os.path.normpath(OUT), "w"), indent=2)
        print(f"\nwritten: {os.path.normpath(OUT)}")


if __name__ == "__main__":
    main()
