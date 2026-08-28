#!/usr/bin/env python3
"""EVENT CIRCLES vs CONTROL CIRCLES, normalised -- because the naive comparison
is worthless and publishing it would be a mistake.

THE CONFOUND. The event circles are wherever Charlie Kirk spoke: Phoenix,
Dallas, Las Vegas, Los Angeles, West Palm Beach. The six control cities are
Des Moines, Chattanooga, Spokane, Albuquerque, Syracuse, Shreveport. Phoenix
Sky Harbor moves an order of magnitude more business aviation than Shreveport.
Any "foreign jets per circle-day" comparison between those two sets measures
AIRPORT SIZE, not surveillance, and would collapse the moment anyone checked.

THE FIX, three independent normalisations, all reported:

  N1  PER AIRCRAFT ON THE GROUND. Of every aircraft that was on the ground
      inside the circle, what fraction was foreign / unregistered / military /
      blocked? A busy airport has more of everything, so the RATIO should be
      flat if nothing unusual is happening.
  N2  SIZE-MATCHED CIRCLE-DAYS. Bucket every circle-day by how many aircraft
      were on the ground in it, then compare event to control INSIDE each
      bucket. This compares like with like directly.
  N3  THE EGYPTIAN-SPECIFIC RATE, which is the only rate the actual claim is
      about. Foreign-registered is a category with thousands of members;
      SU-registered is a category with a handful.

If N1 and N2 come out flat, the naive 8x is airport size and nothing else, and
this file says so.
"""
import collections, csv, glob, gzip, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(HERE, "..", "data"))
SWEEP = os.path.join(DATA, "geo_sweep")
OUT = os.path.join(DATA, "analysis")

AIRLINER = {"A19N","A20N","A21N","A319","A320","A321","A332","A333","A339","A343","A359","A35K",
            "A388","B38M","B39M","B738","B739","B737","B752","B753","B762","B763","B764","B772",
            "B77L","B77W","B788","B789","B78X","B744","B748","E170","E175","E190","E195","CRJ2",
            "CRJ7","CRJ9","E75L","E75S","A306","B733","B734","B735","MD11"}


def main():
    cd = collections.defaultdict(lambda: collections.Counter())   # (kind, circle_key, date) -> counts
    egypt = collections.Counter()
    for f in sorted(glob.glob(os.path.join(SWEEP, "*", "hits.csv.gz"))):
        with gzip.open(f, "rt") as fh:
            for r in csv.DictReader(fh):
                if r["on_ground_in_circle"] != "True":
                    continue
                key = (r["circle_kind"], r["circle_key"], r["sweep_date"])
                c = cd[key]
                c["on_ground"] += 1
                typ = (r.get("type") or "").upper()
                reasons = [x for x in (r.get("flag_reasons") or "").split("|") if x]
                if reasons and typ not in AIRLINER:
                    c["notable"] += 1
                    if "non_us_registration" in reasons: c["foreign"] += 1
                    if "dbflag:military" in reasons or "us_military_serial" in reasons: c["military"] += 1
                    if "no_registration" in reasons or "dbflag:PIA" in reasons: c["unreg"] += 1
                if (r.get("reg") or "").upper().startswith("SU-"):
                    c["egyptian"] += 1
                    egypt[(r["circle_kind"], r["sweep_date"], r["city"], r["reg"])] += 1

    tot = collections.defaultdict(collections.Counter)
    for (kind, _, _), c in cd.items():
        for k, v in c.items(): tot[kind][k] += v
        tot[kind]["circle_days"] += 1

    print("=" * 92)
    print("NAIVE  -- per circle-day. THIS IS THE NUMBER THAT MISLEADS.")
    print("=" * 92)
    print(f"{'kind':10}{'circle-days':>13}{'on ground':>12}{'notable':>10}{'notable/day':>14}")
    for k in ("event", "control"):
        t = tot[k]
        print(f"{k:10}{t['circle_days']:>13}{t['on_ground']:>12}{t['notable']:>10}"
              f"{t['notable']/max(t['circle_days'],1):>14.2f}")
    r_naive = (tot["event"]["notable"]/max(tot["event"]["circle_days"],1)) / \
              (tot["control"]["notable"]/max(tot["control"]["circle_days"],1))
    print(f"\nnaive event:control ratio = {r_naive:.2f}x")
    print("Event circles are big metros; control circles are mid-size cities. Most or")
    print("all of that ratio is airport size. Do not publish this number alone.\n")

    print("=" * 92)
    print("N1  PER AIRCRAFT ON THE GROUND -- airport size divides out")
    print("=" * 92)
    print(f"{'kind':10}{'on ground':>12}{'notable':>10}{'notable %':>12}{'foreign %':>12}"
          f"{'military %':>12}{'unreg %':>10}")
    for k in ("event", "control"):
        t = tot[k]; g = max(t["on_ground"], 1)
        print(f"{k:10}{t['on_ground']:>12}{t['notable']:>10}{100*t['notable']/g:>11.2f}%"
              f"{100*t['foreign']/g:>11.2f}%{100*t['military']/g:>11.2f}%{100*t['unreg']/g:>9.2f}%")
    r1 = (tot["event"]["notable"]/max(tot["event"]["on_ground"],1)) / \
         (tot["control"]["notable"]/max(tot["control"]["on_ground"],1))
    print(f"\nN1 event:control ratio = {r1:.2f}x  "
          f"({'flat -- the naive ratio was airport size' if 0.7 < r1 < 1.4 else 'NOT flat -- worth explaining'})\n")

    print("=" * 92)
    print("N2  SIZE-MATCHED -- circle-days bucketed by how busy the circle was")
    print("=" * 92)
    def bucket(n):
        for hi, lab in ((5,"1-5"),(20,"6-20"),(50,"21-50"),(150,"51-150"),(400,"151-400")):
            if n <= hi: return lab
        return "400+"
    b = collections.defaultdict(collections.Counter)
    for (kind, _, _), c in cd.items():
        bb = bucket(c["on_ground"])
        b[(kind, bb)]["days"] += 1
        b[(kind, bb)]["on_ground"] += c["on_ground"]
        b[(kind, bb)]["notable"] += c["notable"]
    print(f"{'bucket':10}{'event days':>12}{'ev notable%':>13}{'ctrl days':>11}{'ctrl notable%':>15}{'ratio':>9}")
    for bb in ("1-5","6-20","21-50","51-150","151-400","400+"):
        e, c = b[("event", bb)], b[("control", bb)]
        if not e["days"] and not c["days"]: continue
        ep = 100*e["notable"]/max(e["on_ground"],1)
        cp = 100*c["notable"]/max(c["on_ground"],1)
        rr = (ep/cp) if cp else float("nan")
        print(f"{bb:10}{e['days']:>12}{ep:>12.2f}%{c['days']:>11}{cp:>14.2f}%{rr:>9.2f}")
    print()

    print("=" * 92)
    print("N3  THE RATE THE CLAIM IS ACTUALLY ABOUT -- SU-registered aircraft")
    print("=" * 92)
    ev = [k for k in egypt if k[0] == "event"]
    ct = [k for k in egypt if k[0] == "control"]
    print(f"SU-registered aircraft ON THE GROUND in an EVENT circle:   {len(ev)}")
    for k in sorted(ev): print(f"    {k[1]}  {k[3]:8} {k[2]}")
    print(f"SU-registered aircraft ON THE GROUND in a CONTROL circle:  {len(ct)}")
    for k in sorted(ct): print(f"    {k[1]}  {k[3]:8} {k[2]}")
    print()
    print("'Foreign-registered' has thousands of members and is dominated by Canadian and")
    print("Mexican business jets. 'SU-registered' has a handful. The claim is about the")
    print("second category, and the second category is what N3 counts.")

    json.dump({k[0] + "|" + k[1] + "|" + k[2]: dict(v) for k, v in
               [((a, b, c), d) for (a, b, c), d in cd.items()]},
              open(os.path.join(OUT, "circle_day_counts.json"), "w"))


if __name__ == "__main__":
    main()
