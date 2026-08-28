#!/usr/bin/env python3
"""Event vs control, NAIVE and NORMALISED, plus the all-aircraft recurrence rank.

WHY THIS EXISTS. data/analysis/geo_rates.csv reports 44.16 notable aircraft on
the ground per event circle-day against 4.49 per control circle-day. Taken at
face value that is a 9.8x excess. It is not a comparison. Event circles are
Phoenix, Dallas, Las Vegas and Washington DC; the six control cities are mid-
size. Event circles average 1,502 aircraft entering and 393 reporting on the
ground per circle-day; controls average 790 and 34. Comparing raw counts
compares metro size.

Three denominators are printed so the reader can see the claim shrink:
    per circle-day          naive, confounded by metro size
    per aircraft ENTERING   normalises busy airspace
    per aircraft ON GROUND  normalises busy ramps -- the tightest

And one more control on the control: FOUR OF THE SIX CONTROL CITIES HAVE
ALMOST NO GROUND COVERAGE in adsb.lol's archive (Chattanooga reports an
aircraft on the ground on 28% of its circle-days, Shreveport 25%, Syracuse
33%). Albuquerque, which does have ground coverage, is a Kirtland AFB city and
supplies 68% of all control on-ground aircraft and 84% of the control's
military ones. So the control ground denominator is mostly one military ramp.
Every normalised number is therefore printed a second time with Albuquerque
removed, and the honest headline is the SMALLER of the two.

Reads only data/geo_sweep/*/hits.csv.gz. No network. Node/pandas not needed.
    python3 analyse_geo_normalised.py            # tables to stdout
    python3 analyse_geo_normalised.py --csv      # also write analysis CSVs
"""
import collections, csv, glob, gzip, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(HERE, "..", "data"))
SWEEP = os.path.join(DATA, "geo_sweep")
OUT = os.path.join(DATA, "analysis")

# Scheduled-airliner types. An airliner inside a 50-mile circle is scheduled
# service, not presence in the sense the following claim means, and both sides
# of every comparison drop them.
AIRLINER = set("""A19N A20N A21N A319 A320 A321 A332 A333 A339 A343 A359 A35K A388 B38M
B39M B738 B739 B737 B752 B753 B762 B763 B764 B772 B77L B77W B788 B789 B78X B744 B748
E170 E175 E190 E195 CRJ2 CRJ7 CRJ9 E75L E75S A306 B733 B734 B735 MD11 BCS1 BCS3 AT72
AT76 DH8D SF34 E290 E295 B463 CRJX E145 E135 E45X B712""".split())

MILGOV = {"us_military_serial", "dbflag:military", "government_operator_string"}


def klass(rs):
    """One mutually exclusive class per aircraft-circle-day, most specific first."""
    if any(r.startswith("tracked_fleet:") for r in rs):   return "tracked_fleet"
    if rs & MILGOV:                                        return "milgov"
    if "non_us_registration" in rs:                        return "foreign_civil"
    if "no_registration" in rs and "non_icao_address" not in rs: return "unregistered"
    if "non_icao_address" in rs:                           return "tisb_artifact"
    if "dbflag:PIA" in rs:                                 return "pia_only"
    if "dbflag:LADD" in rs:                                return "ladd_only"
    return "other"


CLASSES = ["tracked_fleet", "milgov", "foreign_civil", "unregistered",
           "tisb_artifact", "pia_only", "ladd_only", "other"]


def scan():
    cd, ev, ctl, info = {}, collections.defaultdict(set), collections.defaultdict(set), {}
    for f in sorted(glob.glob(os.path.join(SWEEP, "*", "hits.csv.gz"))):
        with gzip.open(f, "rt") as fh:
            for r in csv.DictReader(fh):
                k = (r["sweep_date"], r["circle_key"])
                d = cd.get(k)
                if d is None:
                    d = cd[k] = dict(date=r["sweep_date"], key=r["circle_key"],
                                     kind=r["circle_kind"], city=r["city"], state=r["state"],
                                     entering=0, on_ground=0,
                                     **{c: 0 for c in CLASSES})
                d["entering"] += 1
                if r["on_ground_in_circle"] != "True":
                    continue
                d["on_ground"] += 1
                typ = (r.get("type") or "").upper()
                h = r["hex"]
                info.setdefault(h, (r.get("reg", ""), typ, r.get("own_op", ""),
                                    r.get("flag_reasons", "")))
                if typ not in AIRLINER:
                    if r["circle_kind"] == "event":
                        ev[h].add((r["sweep_date"], r["city"] + "," + r["state"]))
                    else:
                        ctl[h].add((r["sweep_date"], r["city"]))
                rs = {x for x in (r.get("flag_reasons") or "").split("|") if x}
                if not rs or typ in AIRLINER:
                    continue
                d[klass(rs)] += 1
    return list(cd.values()), ev, ctl, info


def block(rows, sel, label):
    a = collections.Counter()
    for r in rows:
        if not sel(r):
            continue
        a["cd"] += 1; a["entering"] += r["entering"]; a["on_ground"] += r["on_ground"]
        for c in CLASSES:
            a[c] += r[c]
    a["notable"] = sum(a[c] for c in CLASSES)
    return label, a


def show(blocks, num):
    print(f"\n--- {num} ---")
    print(f"{'population':44}{'circle-days':>12}{'on-ground':>11}{'n':>8}"
          f"{'/circle-day':>13}{'/10k entering':>15}{'/1k on-ground':>15}")
    for label, a in blocks:
        if not a["on_ground"]:
            print(f"{label:44}{a['cd']:12d}{a['on_ground']:11d}  NO GROUND COVERAGE")
            continue
        n = a[num] if num != "notable" else a["notable"]
        print(f"{label:44}{a['cd']:12d}{a['on_ground']:11d}{n:8d}"
              f"{n/a['cd']:13.2f}{10000*n/a['entering']:15.2f}{1000*n/a['on_ground']:15.2f}")


def main():
    rows, ev, ctl, info = scan()
    E = lambda r: r["kind"] == "event"
    C = lambda r: r["kind"] == "control"
    CX = lambda r: r["kind"] == "control" and r["city"] != "Albuquerque"
    G = lambda f: (lambda r: f(r) and r["on_ground"] >= 100)

    pops = [block(rows, E, "EVENT circles"),
            block(rows, C, "CONTROL circles"),
            block(rows, CX, "CONTROL circles, Albuquerque removed"),
            block(rows, G(E), "EVENT circles, ground-covered days only"),
            block(rows, G(C), "CONTROL circles, ground-covered days only"),
            block(rows, G(CX), "CONTROL, ground-covered, Albuquerque removed")]
    for num in ("notable", "foreign_civil", "unregistered", "milgov", "ladd_only", "pia_only"):
        show(pops, num)

    print("\n--- ground coverage of each control circle ---")
    per = collections.defaultdict(collections.Counter)
    for r in rows:
        if r["kind"] != "control":
            continue
        per[r["city"]]["cd"] += 1
        per[r["city"]]["og"] += r["on_ground"]
        if r["on_ground"]:
            per[r["city"]]["days_with_ground"] += 1
    for city in sorted(per):
        p = per[city]
        print(f"  {city:14} circle-days {p['cd']:5d}  days with any aircraft on the ground "
              f"{p['days_with_ground']:5d} ({100*p['days_with_ground']/p['cd']:3.0f}%)  "
              f"total on-ground {p['og']:6d}")

    print("\n--- recurrence over ALL aircraft, not just flagged ones ---")
    print(f"  distinct non-airliner aircraft ever on the ground in an event circle: {len(ev)}")
    rank = sorted(ev.items(), key=lambda kv: -len(kv[1]))
    print(f"  {'reg':11}{'type':6}{'ev-pairs':>9}{'cities':>7}{'states':>7}{'ctl-pairs':>10}  operator")
    for h, s in rank[:15]:
        reg, typ, op, fr = info[h]
        cities = {c for _, c in s}
        states = {c.split(",")[1] for c in cities}
        print(f"  {reg or h:11}{typ:6}{len(s):9d}{len(cities):7d}{len(states):7d}"
              f"{len(ctl.get(h, ())):10d}  {op[:44]}")

    if "--csv" in sys.argv:
        os.makedirs(OUT, exist_ok=True)
        with open(os.path.join(OUT, "geo_circle_days_classed.csv"), "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
        with open(os.path.join(OUT, "geo_recurrence_all_aircraft.csv"), "w", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["reg", "hex", "type", "operator", "flag_reasons",
                        "event_ground_date_city_pairs", "event_cities", "event_states",
                        "control_ground_pairs", "event_pairs_detail"])
            for h, s in rank:
                reg, typ, op, fr = info[h]
                cities = sorted({c for _, c in s})
                w.writerow([reg, h, typ, op, fr, len(s), len(cities),
                            len({c.split(",")[1] for c in cities}), len(ctl.get(h, ())),
                            "; ".join(f"{d} {c}" for d, c in sorted(s))])
        print("\nwrote geo_circle_days_classed.csv, geo_recurrence_all_aircraft.csv")


if __name__ == "__main__":
    main()
