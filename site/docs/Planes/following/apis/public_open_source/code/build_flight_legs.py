#!/usr/bin/env python3
"""EVERY FLIGHT WE CAN SHOW, as legs -- for the foreign fleet and the tracked
US aircraft.

A LEG here is: an on-ground run at field A, then airborne, then an on-ground run
at field B, inside one UTC day's trace. That is the strongest thing a raw ADS-B
trace supports and it is still weaker than a flight record:

  * A day's trace is cut at UTC midnight. A leg crossing midnight appears as two
    partial legs, and this file says so with `truncated_at_utc_midnight`.
  * An aircraft heard only in cruise gives an ORIGIN_UNKNOWN / DEST_UNKNOWN leg.
    That is a coverage fact about receivers, not a mystery about the aircraft.
  * A leg proves an airframe moved between two fields. It proves nothing about
    who was aboard or why.

Output: data/analysis/flight_legs.csv, one row per leg, with the archive(s) that
hold it, whether it had to come from a backup, and the nearest sourced
Charlie/Erika/TPUSA event to either end.
"""
import collections, csv, datetime as dt, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "lib"))
DATA = os.path.normpath(os.path.join(HERE, "..", "data"))
AN = os.path.join(DATA, "analysis")
FOLLOWING = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
from geo import haversine_km, MI_PER_KM  # noqa


def events():
    """(date -> [ (city, state, lat, lon, who, charlie, erika, title) ])"""
    import build_master_proximity as bmp
    gaz = bmp.load_gazetteer()
    out = collections.defaultdict(list)
    for e in bmp.load_events(gaz):
        out[e["date"]].append(e)
    return out


def main():
    vi = json.load(open(os.path.join(DATA, "recovery", "trace_visit_index.json")))
    led = {}
    for r in csv.DictReader(open(os.path.join(AN, "recovery_ledger.csv"))):
        led[(r["tail"], r["date"])] = r
    ev = events()

    # A long-haul leg crosses UTC midnight, so its origin lands in one day file
    # and its destination in the next. Building legs day-by-day therefore MISSES
    # exactly the transatlantic flights this fleet mostly flies. Ground runs are
    # collected per tail across the WHOLE record and legs are cut between
    # consecutive ground runs, with the day gap recorded so a reader can see how
    # much unobserved time sits inside a leg.
    legs = []
    ALLRUNS = {}
    for tail, days in vi.items():
        for day, entries in sorted(days.items()):
            # merge every archive's view of the day, keyed by field + hour so the
            # two networks' copies of one ground run collapse into one visit
            merged = {}
            for e in entries:
                for g in e.get("ground_visits", []):
                    k = (g.get("airport_code"), (g.get("first_seen_utc") or "")[:13])
                    m = merged.setdefault(k, dict(g=g, srcs=set()))
                    m["srcs"].add(e.get("source", ""))
                    if (g.get("ground_points") or 0) > (m["g"].get("ground_points") or 0):
                        m["g"] = g
            for m in merged.values(): m["day"] = day
            ALLRUNS.setdefault(tail, []).extend(merged.values())
    for tail, allruns in ALLRUNS.items():
            runs = sorted(allruns, key=lambda m: m["g"].get("first_seen_utc") or "")
            for i in range(len(runs)):
                a = runs[i]["g"]
                b = runs[i + 1]["g"] if i + 1 < len(runs) else None
                if b is None:
                    break
                if a.get("airport_code") == b.get("airport_code"):
                    continue              # same field twice = one interrupted ground run
                day = runs[i]["day"]; day2 = runs[i + 1]["day"]
                gap_days = (dt.date.fromisoformat(day2) - dt.date.fromisoformat(day)).days
                L = led.get((tail, day), {})
                L2 = led.get((tail, day2), {})
                BACKUP = ("ONLY_ON_AIRPLANES_LIVE", "HELD_BY_AIRPLANES-LIVE",
                          "HELD_BY_ADSBEXCHANGE-SAMPLES", "ONLY_ON_ADSB_LOL")
                recovered_only = L.get("verdict") in BACKUP or L2.get("verdict") in BACKUP
                near = ""
                for pt, lab, dref in ((a, "origin", day), (b, "dest", day2)):
                    for off in (-1, 0, 1):
                        d2 = (dt.date.fromisoformat(dref) + dt.timedelta(days=off)).isoformat()
                        for e in ev.get(d2, []):
                            mi = haversine_km(pt["lat"], pt["lon"], e["lat"], e["lon"]) * MI_PER_KM
                            if mi <= 50 and (not near or mi < float(near.split("|")[-1])):
                                near = f"{lab}|{e['city']},{e['state']}|{e['date']}|{e['who']}|{mi:.1f}"
                legs.append(dict(
                    tail=tail, utc_date=day, arrive_utc_date=day2,
                    gap_days=gap_days,
                    origin=a.get("airport_code", ""), origin_name=a.get("airport_name", ""),
                    origin_km_from_field=a.get("median_distance_km"),
                    depart_after_utc=a.get("last_seen_utc", ""),
                    dest=b.get("airport_code", ""), dest_name=b.get("airport_name", ""),
                    dest_km_from_field=b.get("median_distance_km"),
                    arrive_by_utc=b.get("first_seen_utc", ""),
                    archives="|".join(sorted(s for s in (runs[i]["srcs"] | runs[i + 1]["srcs"]) if s)),
                    ledger_verdict=L.get("verdict", "NOT_IN_LEDGER"),
                    arrive_day_verdict=L2.get("verdict", "NOT_IN_LEDGER"),
                    unobserved_days_inside_leg=max(0, gap_days - 1),
                    recovered_from_backup_only="yes" if recovered_only else "no",
                    crosses_utc_midnight="yes" if gap_days >= 1 else "no",
                    confidence=("direct" if gap_days == 0 else
                                "overnight" if gap_days == 1 else
                                "GAP -- aircraft unobserved for %d day(s) between these two fields; "
                                "intermediate stops are possible and are NOT ruled out" % (gap_days - 1)),
                    near_sourced_event=near))
    legs.sort(key=lambda r: (r["utc_date"], r["tail"]))
    path = os.path.join(AN, "flight_legs.csv")
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(legs[0].keys())); w.writeheader(); w.writerows(legs)
    print(f"legs: {len(legs)}", file=sys.stderr)
    print("per tail:", collections.Counter(l["tail"] for l in legs).most_common(), file=sys.stderr)
    print("near a sourced event:", sum(1 for l in legs if l["near_sourced_event"]), file=sys.stderr)
    print("recovered-from-backup-only legs:", sum(1 for l in legs if l["recovered_from_backup_only"] == "yes"), file=sys.stderr)
    print("wrote " + path, file=sys.stderr)


if __name__ == "__main__":
    main()
