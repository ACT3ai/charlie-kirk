#!/usr/bin/env python3
"""THE DEFINITIVE PROXIMITY TABLE.

Every (tail, UTC date, airport) where a TRACKED aircraft transmitted ON-GROUND
positions inside 50 miles of a SOURCED Charlie Kirk / Erika Kirk / TPUSA event
city, same day or +/-1 day.

Reads only files already on disk. Makes no network request.

  IN   data/analysis/master_proximity.csv   (built by build_master_proximity.py)
       data/analysis/recovery_ledger.csv    (built by build_recovery_ledger.py)
       following/tpusa_events.csv
  OUT  data/analysis/definitive_proximity.csv
       data/analysis/definitive_proximity_by_tail.csv
       data/analysis/definitive_event_coverage.csv

WHAT A ROW IS. An airframe's transponder reported ground positions near a
runway on that UTC day, and a sourced event city sat within 50 straight-line
miles within +/-1 day.

WHAT A ROW IS NOT. It is not a landing, not a passenger, not a purpose, and
not occupancy. NOBODY named in this investigation is placed aboard any of
these aircraft by any file in this repo.

THE EXPECTED / NOT-EXPECTED SPLIT is the whole point of the `side` column.
N582MM, N560TW, N872RA, N102DZ, N888KG and N40JD are US-registered private
jets already associated with Kirk / TPUSA travel. THEIR proximity to a Kirk
event is the null hypothesis, not a finding. Only the `following` side
(Egyptian and San Marino registrations) and the `n1098l` survey side can carry
a claim, and each of those is reported with its own coverage denominator.
"""
import csv, collections, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
AN = os.path.normpath(os.path.join(HERE, "..", "data", "analysis"))
FOLLOWING = os.path.normpath(os.path.join(HERE, "..", "..", "..", ".."))

SIDE = {
    "N582MM": "kirk", "N560TW": "kirk", "N872RA": "kirk",
    "N102DZ": "kirk", "N888KG": "kirk", "N40JD": "kirk",
    "SU-BTT": "following", "SU-BND": "following", "SU-BTU": "following",
    "SU-BTV": "following", "SU-BGM": "following", "T7-ELL": "following",
    "N1098L": "n1098l", "N2100L": "n1098l", "N59906": "n1098l",
    "CONTROL-LUFTHANSA": "control", "CONTROL-RYANAIR": "control",
}
REGISTRY = {"SU-": "Egypt", "T7-": "San Marino"}


def registry_of(tail):
    for p, v in REGISTRY.items():
        if tail.startswith(p):
            return v
    if tail.startswith("CONTROL-"):
        return "control airliner (Europe)"
    return "United States"


def main():
    led = {}
    for r in csv.DictReader(open(os.path.join(AN, "recovery_ledger.csv"))):
        led[(r["tail"], r["date"])] = r

    rows = list(csv.DictReader(open(os.path.join(AN, "master_proximity.csv"))))
    hits = [r for r in rows if r["within_50mi"] == "yes"]

    # collapse the per-segment ground visits into one row per tail/date/airport
    agg = collections.OrderedDict()
    for r in hits:
        k = (r["tail"], r["date"], r["airport_code"])
        a = agg.get(k)
        if a is None:
            a = agg[k] = dict(r)
            a["_segments"] = 0
            a["_points"] = 0
            a["_srcs"] = set()
            a["_first"] = r["first_seen_utc"]
            a["_last"] = r["last_seen_utc"]
        a["_segments"] += 1
        a["_points"] += int(r["ground_points"] or 0)
        a["_srcs"] |= {s for s in r["sources"].split("|") if s}
        a["_first"] = min(a["_first"], r["first_seen_utc"])
        a["_last"] = max(a["_last"], r["last_seen_utc"])

    out = []
    for (tail, date, ap), a in agg.items():
        l = led.get((tail, date), {})
        srcs = sorted(a["_srcs"])
        v = l.get("verdict", "NOT_IN_LEDGER")
        # Which archive actually CONTAINS the on-ground points for this visit.
        # NOTE the ledger verdict is about the DAY; this is about the VISIT.
        # A day can be BOTH_HAVE_IT while only ONE archive's trace carries the
        # ground segment -- denser receiver coverage, not a deletion.
        visit_only_in_backup = "yes" if ("adsb-lol" not in srcs and srcs) else "no"
        out.append(dict(
            side=SIDE.get(tail, "unknown"), registry=registry_of(tail),
            tail=tail, date=date, airport=ap,
            airport_name=a["airport_name"], airport_city=a["airport_city"],
            median_km_from_field=a["median_km_from_field"],
            ground_points=a["_points"], ground_segments=a["_segments"],
            first_seen_utc=a["_first"], last_seen_utc=a["_last"],
            event_city=a["nearest_event_city"], event_state=a["nearest_event_state"],
            event_date=a["nearest_event_date"], event_offset_days=a["event_offset_days"],
            event_who=a["nearest_event_who"], event_title=a["nearest_event_title"],
            charlie_sourced_present=a["charlie_present"],
            erika_sourced_present=a["erika_present"],
            miles_to_event_city=a["miles_to_event_city"],
            archives_holding="|".join(srcs),
            archives_agreeing=len(srcs),
            ledger_verdict=v,
            adsb_lol_403_band=l.get("adsb_lol_403_band", ""),
            visit_only_in_non_adsblol_archive=visit_only_in_backup,
            adsb_lol_held_the_day="yes" if "adsb-lol" in (l.get("archives_held") or "") else "no",
            needed_wayback_or_github_backup="yes" if any(x in srcs for x in ("wayback","adsblol-github-backup")) else "no",
            event_page=a["event_page"]))
    out.sort(key=lambda r: (r["date"], r["tail"], r["airport"]))
    p = os.path.join(AN, "definitive_proximity.csv")
    with open(p, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
    print(f"wrote {p}  rows={len(out)}", file=sys.stderr)

    # ---- per-tail summary with the COVERAGE DENOMINATOR beside every count ----
    ask = collections.defaultdict(collections.Counter)
    for (t, d), r in led.items():
        ask[t][r["verdict"]] += 1
    vis = collections.defaultdict(lambda: dict(visits=0, days=set(), mind=None))
    for r in rows:
        v = vis[r["tail"]]; v["visits"] += 1; v["days"].add(r["date"])
        if r["miles_to_event_city"]:
            m = float(r["miles_to_event_city"])
            if v["mind"] is None or m < v["mind"]: v["mind"] = m
    hit = collections.defaultdict(lambda: dict(rows=0, days=set(), events=set(), aps=set()))
    for r in out:
        h = hit[r['tail']]; h["rows"] += 1; h["days"].add(r["date"])
        h["events"].add((r["event_city"], r["event_date"])); h["aps"].add(r["airport"])
    tp = []
    for t in sorted(vis, key=lambda x: (SIDE.get(x, "z"), -hit[x]["rows"])):
        c = ask[t]; tot = sum(c.values())
        tp.append(dict(side=SIDE.get(t, "unknown"), registry=registry_of(t), tail=t,
                       archive_days_asked=tot,
                       archive_days_held=tot - c["NEITHER_HAS_IT"],
                       archive_days_asked_and_empty=c["NEITHER_HAS_IT"],
                       ground_visits=vis[t]["visits"], ground_visit_days=len(vis[t]["days"]),
                       proximity_rows=hit[t]["rows"], proximity_days=len(hit[t]["days"]),
                       distinct_events=len(hit[t]["events"]),
                       distinct_airports="|".join(sorted(hit[t]["aps"])),
                       closest_ever_miles_to_an_event_city=round(vis[t]["mind"], 1) if vis[t]["mind"] is not None else ""))
    p2 = os.path.join(AN, "definitive_proximity_by_tail.csv")
    with open(p2, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(tp[0].keys())); w.writeheader(); w.writerows(tp)
    print(f"wrote {p2}  rows={len(tp)}", file=sys.stderr)

    # ---- per-event coverage: which sourced events got a tracked aircraft ----
    byev = collections.defaultdict(lambda: collections.defaultdict(set))
    for r in out:
        byev[(r["event_date"], r["event_city"], r["event_state"])][r["side"]].add(r["tail"])
    ev = []
    for k, sides in sorted(byev.items()):
        ev.append(dict(event_date=k[0], event_city=k[1], event_state=k[2],
                       kirk_side_tails="|".join(sorted(sides.get("kirk", []))),
                       following_side_tails="|".join(sorted(sides.get("following", []))),
                       n1098l_side_tails="|".join(sorted(sides.get("n1098l", []))),
                       n_tails=sum(len(v) for v in sides.values())))
    p3 = os.path.join(AN, "definitive_event_coverage.csv")
    with open(p3, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(ev[0].keys())); w.writeheader(); w.writerows(ev)
    print(f"wrote {p3}  distinct events matched={len(ev)}", file=sys.stderr)


if __name__ == "__main__":
    main()
