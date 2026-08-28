#!/usr/bin/env python3
"""THE HARD TEST on the geographic-sweep recurrence list.

geo_recurrence.csv says 857 aircraft were on the ground near 2+ sourced
Kirk/TPUSA events in 2+ states. That number means NOTHING on its own. This
script asks the three questions that decide whether any of it is a signal:

  1. BASE RATE. How many aircraft of ANY kind -- including perfectly ordinary
     US-registered ones with no flag at all -- clear the same 2-events /
     2-states bar? If thousands do, the bar is meaningless.

  2. THE OFFSET TEST (an INTERNAL control that needs no matched control city).
     Every event circle was swept on offset -1, 0 and +1. An aircraft that is
     FOLLOWING a person should be preferentially present on the event day. An
     aircraft that simply lives at that metro is flat across the three days.

  3. METRO CONCENTRATION. An aircraft whose "recurrence" is 40 hits at Phoenix
     and 2 elsewhere is a Phoenix resident, not a shadow.

It also prints the exposure asymmetry that makes `control_contaminated=no`
close to worthless as a per-aircraft clean bill: the six control cities are
fixed mid-size metros, so an aircraft that never leaves the southwest is
"uncontaminated" by construction.

Reads only files already on disk. Makes no network request.
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


def rows():
    for f in sorted(glob.glob(os.path.join(SWEEP, "*", "hits.csv.gz"))):
        with gzip.open(f, "rt") as fh:
            for r in csv.DictReader(fh):
                yield r


def main():
    ac = collections.defaultdict(lambda: dict(
        reg="", typ="", op="", flags=set(),
        ev=set(), ev_city=collections.Counter(), ev_state=set(),
        off=collections.Counter(), ctl_city=set(), ctl_days=set()))
    city_days = collections.defaultdict(set)      # (kind, city) -> set of sweep dates
    circle_days = collections.defaultdict(set)    # kind -> set (date, circle_key)
    offset_circle_days = collections.Counter()    # offset -> circle-days (event only)
    n = 0
    for r in rows():
        n += 1
        kind, hx = r["circle_kind"], r["hex"]
        typ = (r.get("type") or "").upper()
        circle_days[kind].add((r["sweep_date"], r["circle_key"]))
        city_days[(kind, f'{r["city"]},{r["state"]}')].add(r["sweep_date"])
        if kind == "event":
            offset_circle_days[r["offset_days"]] = offset_circle_days[r["offset_days"]]
        if r["on_ground_in_circle"] != "True" or typ in AIRLINER:
            continue
        d = ac[hx]
        d["reg"] = d["reg"] or (r.get("reg") or "")
        d["typ"] = d["typ"] or typ
        d["op"] = d["op"] or (r.get("own_op") or "")
        d["flags"] |= {x for x in (r.get("flag_reasons") or "").split("|") if x}
        if kind == "event":
            d["ev"].add((r["event_date"], r["city"], r["state"]))
            d["ev_city"][f'{r["city"]},{r["state"]}'] += 1
            d["ev_state"].add(r["state"])
            d["off"][r["offset_days"]] += 1
        else:
            d["ctl_city"].add(r["city"])
            d["ctl_days"].add(r["sweep_date"])

    # exposure: distinct circle-days by offset
    off_exposure = collections.Counter()
    for f in sorted(glob.glob(os.path.join(SWEEP, "*", "_sweep.meta.json"))):
        m = json.load(open(f))
        for c in m.get("circles", []):
            if c.get("kind") == "event":
                off_exposure[str(c.get("offset_days"))] += 1

    print(f"hit rows scanned                : {n}")
    print(f"event circle-days               : {len(circle_days['event'])}")
    print(f"control circle-days             : {len(circle_days['control'])}")
    print(f"distinct event cities           : {len({c for (k,c) in city_days if k=='event'})}")
    print(f"distinct control cities         : {len({c for (k,c) in city_days if k=='control'})}")
    print(f"event circle-days by offset     : {dict(sorted(off_exposure.items()))}")
    print()

    # --- 1. BASE RATE -------------------------------------------------------
    bar = [h for h, d in ac.items() if len(d["ev"]) >= 2 and len(d["ev_state"]) >= 2]
    flagged_bar = [h for h in bar if ac[h]["flags"]]
    unflagged_bar = [h for h in bar if not ac[h]["flags"]]
    print("=== BASE RATE: who clears '2+ event-days in 2+ states' ===")
    print(f"  ALL non-airliner aircraft on the ground in an event circle : {len(ac)}")
    print(f"  clearing the bar, ANY aircraft                             : {len(bar)}")
    print(f"    of which FLAGGED (foreign/LADD/mil/gov/no-reg)           : {len(flagged_bar)}")
    print(f"    of which ORDINARY, no flag at all                        : {len(unflagged_bar)}")
    print()

    # --- 2. OFFSET TEST -----------------------------------------------------
    tot = collections.Counter()
    for h, d in ac.items():
        for o, c in d["off"].items():
            tot[o] += c
    print("=== OFFSET TEST (population of all non-airliner ground hits in event circles) ===")
    for o in ("-1", "0", "1"):
        exp = off_exposure.get(o, 0) or 1
        print(f"  offset {o:>2}: ground hits={tot[o]:7}  circle-days={off_exposure.get(o,0):5}  per-circle-day={tot[o]/exp:.2f}")
    print()

    # --- 3. RANKED CANDIDATES ----------------------------------------------
    cand = []
    for h in bar:
        d = ac[h]
        cities = d["ev_city"]
        top_city, top_n = cities.most_common(1)[0]
        n_ev = len(d["ev"])
        tot_hits = sum(cities.values())
        o = d["off"]
        cand.append(dict(
            hex=h, reg=d["reg"], type=d["typ"], operator=d["op"],
            flags="|".join(sorted(d["flags"])) or "NONE",
            event_days=n_ev, distinct_cities=len(cities), states=len(d["ev_state"]),
            states_list="|".join(sorted(d["ev_state"])),
            top_city=top_city, top_city_hits=top_n,
            top_city_share=round(top_n / tot_hits, 3),
            off_m1=o["-1"], off_0=o["0"], off_p1=o["1"],
            day0_share=round(o["0"] / max(1, o["-1"] + o["0"] + o["1"]), 3),
            control_cities="|".join(sorted(d["ctl_city"])),
            control_contaminated="yes" if d["ctl_city"] else "no"))
    cand.sort(key=lambda r: (-r["event_days"], -r["distinct_cities"]))
    with open(os.path.join(OUT, "recurrence_hardtest.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(cand[0].keys())); w.writeheader(); w.writerows(cand)
    print(f"wrote {OUT}/recurrence_hardtest.csv  ({len(cand)} rows)")

    print()
    print("=== TOP 25 by distinct event CITIES, control-clean, flagged ===")
    top = [c for c in cand if c["control_contaminated"] == "no" and c["flags"] != "NONE"]
    top.sort(key=lambda r: (-r["distinct_cities"], -r["states"], -r["event_days"]))
    for c in top[:25]:
        print(f"  {c['reg'] or c['hex']:10} {c['type']:5} cities={c['distinct_cities']:3} states={c['states']:2} "
              f"days={c['event_days']:3} topcity={c['top_city']:22} share={c['top_city_share']:.2f} "
              f"day0share={c['day0_share']:.2f} {c['flags'][:42]}")

    # offset test restricted to the top candidates
    a = sum(c["off_m1"] for c in top); b = sum(c["off_0"] for c in top); d_ = sum(c["off_p1"] for c in top)
    print()
    print(f"=== OFFSET TEST on the {len(top)} control-clean flagged candidates ===")
    print(f"  offset -1 : {a}    offset 0 : {b}    offset +1 : {d_}")


if __name__ == "__main__":
    main()
