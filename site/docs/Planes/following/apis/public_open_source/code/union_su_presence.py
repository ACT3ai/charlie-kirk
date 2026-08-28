#!/usr/bin/env python3
"""EVERY EGYPTIAN / FOREIGN-FLEET GROUND PRESENCE NEAR A SOURCED EVENT --
the UNION of the two routes, because neither one alone is complete.

WHY A UNION IS NECESSARY AND NOT JUST TIDY.

There are two independent ways this repo can put an aircraft near an event, and
each is blind where the other sees:

  PER-TAIL   ask an archive "where was SU-BTT on this date". Complete for the
             16 tails in lib/fleet.js and structurally incapable of finding
             anything else. Holds ~9% of the event-window aircraft-days.

  GEOGRAPHIC SWEEP  stream a whole UTC day and filter by circle. Finds aircraft
             nobody named. Covers 72% of the event window -- but its byte
             pre-filter had a negative-longitude defect (fixed 2026-08-28, see
             test_prefilter.py) that blinded an average 28.7% of each event
             circle's area on the 2026-08 run. UNTIL THAT SWEEP IS RE-RUN,
             EVERY SWEEP-ONLY COUNT IS A FLOOR, NOT A TOTAL.

The union is therefore the honest answer for the TRACKED tails, and a floor for
everything else. This script says which of those two a row is, in a column, on
every row -- and prints the sentence that may be published about each.
"""
import csv, glob, gzip, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(HERE, "..", "data"))
AN = os.path.join(DATA, "analysis")
FOREIGN_PREFIX = ("SU-", "T7-")


def sweep_rows():
    out = []
    for r in csv.DictReader(open(os.path.join(AN, "geo_ground_foreign.csv"))):
        if (r.get("reg") or "").upper().startswith("SU-"):
            out.append(r)
    return out


def pertail_rows():
    out = []
    for r in csv.DictReader(open(os.path.join(AN, "master_proximity.csv"))):
        if r["within_50mi"] == "yes" and r["tail"].startswith(FOREIGN_PREFIX):
            out.append(r)
    return out


def main():
    sw, pt = sweep_rows(), pertail_rows()
    rows = {}
    for r in sw:
        rows[(r["reg"], r["sweep_date"], r["nearest_field"])] = dict(
            tail=r["reg"], date=r["sweep_date"], field=r["nearest_field"],
            field_mi=r["nearest_field_mi"], city=f"{r['city']}, {r['state']}",
            event_date=r["event_date"], offset=r["offset_days"], who=r["who"],
            type=r["type"], found_by="geographic_sweep", archives="adsblol-github-backup")
    for r in pt:
        k = (r["tail"], r["date"], r["airport_code"])
        if k in rows:
            rows[k]["found_by"] = "BOTH ROUTES"
            rows[k]["archives"] = r["sources"]
        else:
            rows[k] = dict(
                tail=r["tail"], date=r["date"], field=r["airport_code"],
                field_mi=round(float(r["median_km_from_field"]) * 0.621371, 2),
                city=f"{r['nearest_event_city']}, {r['nearest_event_state']}",
                event_date=r["nearest_event_date"], offset=r["event_offset_days"],
                who=r["nearest_event_who"], type=r["type"],
                found_by="per_tail_only", archives=r["sources"])
    out = sorted(rows.values(), key=lambda x: (x["date"], x["tail"]))
    path = os.path.join(AN, "su_presence_union.csv")
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)

    print("EGYPTIAN-REGISTERED / FOREIGN-FLEET AIRCRAFT ON THE GROUND WITHIN 50 MILES")
    print("OF A SOURCED CHARLIE / ERIKA / TPUSA EVENT CITY, event date +/- 1 day")
    print("=" * 96)
    print(f"{'date':12}{'tail':8}{'type':6}{'field':7}{'mi':>6}  {'event city':22}{'off':>4} {'who':9} found by")
    for r in out:
        print(f"{r['date']:12}{r['tail']:8}{r['type']:6}{r['field']:7}{str(r['field_mi']):>6}  "
              f"{r['city']:22}{str(r['offset']):>4} {r['who'][:8]:9} {r['found_by']}")
    print()
    print(f"TOTAL: {len(out)}   both routes: {sum(1 for r in out if r['found_by']=='BOTH ROUTES')}"
          f"   sweep only: {sum(1 for r in out if r['found_by']=='geographic_sweep')}"
          f"   per-tail only: {sum(1 for r in out if r['found_by']=='per_tail_only')}")
    print()
    print("WHAT MAY BE PUBLISHED FROM THIS TABLE")
    print("-" * 96)
    print("* For the 16 tails in lib/fleet.js this is a COMPLETE list against the")
    print("  archive holdings -- both routes were run and the per-tail route asked every")
    print("  event-window day of every one of them.")
    print("* It is NOT complete against reality. The per-tail route holds ~9% of the")
    print("  event-window aircraft-days; the rest is 'asked and the archive had nothing',")
    print("  which is a coverage fact and not an absence.")
    print("* For any Egyptian aircraft NOT in the fleet file, the sweep is the only route")
    print("  and its 2026-08 run was area-blind, so that half is a FLOOR.")
    print("* No row here places any person aboard any aircraft.")
    print()
    print("wrote " + path, file=sys.stderr)


if __name__ == "__main__":
    main()
