#!/usr/bin/env python3
"""THE DENOMINATOR FOR THE FOLLOWING CLAIM.

For every sourced Charlie / Erika / TPUSA event city-day, this answers the only
question that makes an absence interpretable:

  Was any tracked aircraft's day ACTUALLY IN AN ARCHIVE for that window?

Three outcomes, and the whole point is that they are never merged:

  matched=yes                 a tracked aircraft was on the ground within 50 mi.
  matched=no, tails_held=0    NOBODY'S TRACE EXISTS for that window. A COVERAGE
                              GAP. It says nothing at all about where anything was.
  matched=no, tails_held>0    a real negative: we hold the aircraft's day and it
                              was somewhere else. Still not proof of absence --
                              a trace can start late, stop early, or never be
                              heard on the ground at a field with no receiver.

Reads only local files. No network.

  OUT  data/analysis/definitive_event_coverage_denominator.csv
"""
import csv, collections, datetime as dt, os, sys, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
AN = os.path.normpath(os.path.join(HERE, "..", "data", "analysis"))

spec = importlib.util.spec_from_file_location("bmp", os.path.join(HERE, "build_master_proximity.py"))
B = importlib.util.module_from_spec(spec); spec.loader.exec_module(B)

KIRK = {"N582MM", "N560TW", "N872RA", "N102DZ", "N888KG", "N40JD"}
FOLL = {"SU-BTT", "SU-BND", "SU-BTU", "SU-BTV", "SU-BGM", "T7-ELL"}


def main():
    ev = B.load_events(B.load_gazetteer())
    events = sorted({(e["date"], e["city"], e["state"], e["charlie"], e["erika"], e["who"]) for e in ev})

    held, asked = collections.defaultdict(set), collections.defaultdict(set)
    for r in csv.DictReader(open(os.path.join(AN, "recovery_ledger.csv"))):
        if r["is_control"] == "yes":
            continue
        asked[r["date"]].add(r["tail"])
        if r["verdict"] != "NEITHER_HAS_IT":
            held[r["date"]].add(r["tail"])

    matched = {(r["event_date"], r["event_city"], r["event_state"])
               for r in csv.DictReader(open(os.path.join(AN, "definitive_proximity.csv")))}

    rows = []
    for d, c, s, ch, er, who in events:
        d0 = dt.date.fromisoformat(d)
        win = [(d0 + dt.timedelta(days=i)).isoformat() for i in (-1, 0, 1)]
        h = set().union(*[held[x] for x in win]) if any(x in held for x in win) else set()
        a = set().union(*[asked[x] for x in win]) if any(x in asked for x in win) else set()
        rows.append(dict(date=d, city=c, state=s, charlie=ch, erika=er, who=who,
                         matched="yes" if (d, c, s) in matched else "no",
                         tails_asked=len(a), tails_held=len(h),
                         kirk_held=len(h & KIRK), following_held=len(h & FOLL)))
    p = os.path.join(AN, "definitive_event_coverage_denominator.csv")
    with open(p, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

    nm = [r for r in rows if r["matched"] == "no"]
    print(f"sourced event city-days: {len(rows)}", file=sys.stderr)
    print(f"  matched by >=1 tracked aircraft within 50 mi: {sum(r['matched']=='yes' for r in rows)}", file=sys.stderr)
    print(f"  unmatched: {len(nm)}", file=sys.stderr)
    print(f"    of which PURE COVERAGE GAP (0 tails held): {sum(r['tails_held']==0 for r in nm)}", file=sys.stderr)
    print(f"    of which REAL NEGATIVE  (>=1 tail held): {sum(r['tails_held']>0 for r in nm)}", file=sys.stderr)
    print(f"    with a FOREIGN tail's day held and not near: {sum(r['following_held']>0 for r in nm)}", file=sys.stderr)
    print(f"wrote {p}", file=sys.stderr)


if __name__ == "__main__":
    main()
