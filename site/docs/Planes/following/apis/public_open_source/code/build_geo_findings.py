#!/usr/bin/env python3
"""What the GEOGRAPHIC SWEEP found, as CSVs a page can be written from.

geo_sweep.py streamed 278 UTC days of adsb.lol's GitHub Release backup and
filtered ~1.77 million aircraft-circle rows by GEOGRAPHY: a 50-mile circle on
every sourced US event city, +/-1 day, AND on six control cities with no known
Kirk/TPUSA event, swept on the same days in the same run.

That control half is the whole point. A foreign jet parked near an event city
means nothing until you know how often one parks near Des Moines on the same
day. Every rate here is printed beside its control.

Outputs, all under data/analysis/:
  geo_ground_foreign.csv    every non-US / unregistered / military / PIA
                            aircraft ON THE GROUND inside a circle
  geo_rates.csv             per-circle-kind base rates
  geo_recurrence.csv        aircraft on the ground near 2+ events in 2+ states,
                            with a column saying whether it ALSO turns up near
                            a control city (a busy charter, not a shadow)
"""
import collections, csv, glob, gzip, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(HERE, "..", "data"))
SWEEP = os.path.join(DATA, "geo_sweep")
OUT = os.path.join(DATA, "analysis")
os.makedirs(OUT, exist_ok=True)

# Scheduled airliners are excluded from "notable" because an EgyptAir 777 at JFK
# is scheduled service, not a shadow. BCS1/BCS3 (A220), B712, E135/E145 and the
# regional Embraers were missing from this set until 2026-08-28 and were leaking
# into the recurrence list as if they were business jets.
AIRLINER = {"A19N","A20N","A21N","A318","A319","A320","A321","A332","A333","A338","A339",
            "A343","A346","A359","A35K","A388","A306","A310","A30B",
            "B38M","B39M","B3XM","B733","B734","B735","B736","B737","B738","B739",
            "B744","B748","B752","B753","B762","B763","B764","B772","B77L","B77W",
            "B788","B789","B78X","B712","BCS1","BCS3",
            "CRJ1","CRJ2","CRJ7","CRJ9","E135","E145","E45X","E170","E175","E190","E195",
            "E75L","E75S","E290","E295","MD11","MD82","MD83","MD88","MD90","AT72","AT75","AT76",
            "DH8A","DH8B","DH8C","DH8D","SF34","B463","B462","RJ85","RJ1H"}

# The government_operator_string flag in the stored sweep rows was produced by a
# substring match that also fired on FEDERAL EXPRESS, EXECUTIVE JET MANAGEMENT
# and ROYAL AIR. Rather than re-sweep 546 MB over the network, the flag is
# RE-DERIVED here from the own_op column that is already in every hits row.
GOV_WORDS = ("AIR FORCE", "ARMY", "NAVY", "MARINE CORPS", "COAST GUARD",
             "DEPARTMENT OF", "UNITED STATES OF AMERICA", "GOVERNMENT",
             "STATE OF", "CUSTOMS AND BORDER", "BORDER PROTECTION",
             "REPUBLIC OF", "MINISTRY OF")


def rederive_reasons(r):
    """Stored flag_reasons, with government_operator_string recomputed."""
    reasons = [x for x in (r.get("flag_reasons") or "").split("|")
               if x and x != "government_operator_string"]
    own = (r.get("own_op") or "").upper()
    if any(w in own for w in GOV_WORDS):
        reasons.append("government_operator_string")
    return reasons


def rows():
    for f in sorted(glob.glob(os.path.join(SWEEP, "*", "hits.csv.gz"))):
        with gzip.open(f, "rt") as fh:
            for r in csv.DictReader(fh):
                yield r


def main():
    ground_foreign, rate = [], collections.Counter()
    seen_circle_days = collections.defaultdict(set)
    by_hex = collections.defaultdict(lambda: dict(events=[], controls=set(), fields=set(),
                                                  reg="", typ="", op="", reasons=set()))
    n = 0
    for r in rows():
        n += 1
        kind = r["circle_kind"]
        seen_circle_days[kind].add((r["sweep_date"], r["circle_key"]))
        rate[(kind, "entering")] += 1
        on_ground = r["on_ground_in_circle"] == "True"
        if on_ground: rate[(kind, "on_ground")] += 1
        reasons = rederive_reasons(r)
        notable = bool(reasons)
        typ = (r.get("type") or "").upper()
        if notable and on_ground:
            rate[(kind, "notable_on_ground_incl_airliners")] += 1
            if typ not in AIRLINER:
                rate[(kind, "notable_on_ground")] += 1
                d = by_hex[r["hex"]]
                d["reg"] = d["reg"] or r.get("reg", "")
                d["typ"] = d["typ"] or typ
                d["op"] = d["op"] or r.get("own_op", "")
                d["reasons"] |= set(reasons)
                if r.get("nearest_field"): d["fields"].add(r["nearest_field"])
                if kind == "event": d["events"].append((r["sweep_date"], r["city"], r["state"], r.get("who", "")))
                else: d["controls"].add(r["city"])
                if kind == "event":
                    ground_foreign.append(dict(
                        sweep_date=r["sweep_date"], event_date=r["event_date"],
                        offset_days=r["offset_days"], city=r["city"], state=r["state"],
                        who=r["who"], hex=r["hex"], reg=r.get("reg", ""), type=typ,
                        operator=r.get("own_op", ""), year=r.get("year", ""),
                        flag_reasons="|".join(reasons),
                        nearest_field=r.get("nearest_field", ""),
                        nearest_field_mi=r.get("nearest_field_mi", ""),
                        closest_mi_to_city=r.get("closest_mi_to_city", ""),
                        points_in_circle=r.get("points_in_circle", ""),
                        first_utc=r.get("first_utc", ""), last_utc=r.get("last_utc", "")))
    print(f"scanned {n} hit rows", file=sys.stderr)

    ground_foreign.sort(key=lambda r: (r["sweep_date"], r["city"], r["reg"] or r["hex"]))
    with open(os.path.join(OUT, "geo_ground_foreign.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(ground_foreign[0].keys())); w.writeheader(); w.writerows(ground_foreign)

    with open(os.path.join(OUT, "geo_rates.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["circle_kind", "circle_days", "aircraft_entering", "on_ground",
                    "notable_on_ground_incl_airliners", "notable_on_ground_excl_airliners",
                    "notable_on_ground_per_circle_day"])
        for kind in ("event", "control"):
            cd = len(seen_circle_days[kind]) or 1
            w.writerow([kind, cd, rate[(kind, "entering")], rate[(kind, "on_ground")],
                        rate[(kind, "notable_on_ground_incl_airliners")],
                        rate[(kind, "notable_on_ground")],
                        round(rate[(kind, "notable_on_ground")] / cd, 3)])

    rec = []
    for hx, d in by_hex.items():
        states = sorted({s for _, _, s, _ in d["events"]})
        if len(d["events"]) >= 2 and len(states) >= 2:
            rec.append(dict(hex=hx, reg=d["reg"], type=d["typ"], operator=d["op"],
                            event_days=len(d["events"]), states="|".join(states),
                            events="; ".join(f"{a} {b},{c}" for a, b, c, _ in sorted(d["events"])),
                            fields="|".join(sorted(d["fields"])),
                            flag_reasons="|".join(sorted(d["reasons"])),
                            also_near_control_cities="|".join(sorted(d["controls"])),
                            control_contaminated="yes" if d["controls"] else "no"))
    rec.sort(key=lambda r: (-r["event_days"], r["reg"]))
    with open(os.path.join(OUT, "geo_recurrence.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rec[0].keys())); w.writeheader(); w.writerows(rec)

    print(f"geo_ground_foreign rows: {len(ground_foreign)}  recurrence rows: {len(rec)}", file=sys.stderr)
    for kind in ("event", "control"):
        cd = len(seen_circle_days[kind]) or 1
        print(f"  {kind:8} circle-days={cd:5} notable-on-ground={rate[(kind,'notable_on_ground')]:6} "
              f"rate={rate[(kind,'notable_on_ground')]/cd:.2f}/circle-day", file=sys.stderr)


if __name__ == "__main__":
    main()
