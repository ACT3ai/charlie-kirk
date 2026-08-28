#!/usr/bin/env python3
"""Blind geographic sweep: what was ON THE GROUND, event circles vs controls.

Streams every data/geo_sweep/<date>/hits.csv.gz row once and writes:

  data/analysis/geo_circle_days.csv   one row per (sweep_date, circle) with the
                                      traffic denominators needed to normalise
  data/analysis/geo_ground_control.csv  the control-circle twin of
                                      geo_ground_foreign.csv (which is events only)
  data/analysis/geo_norm_rates.csv    naive AND normalised event-vs-control rates
  data/analysis/geo_ground_by_category.csv  per flag category, both circle kinds

THE CONFOUND THIS EXISTS TO HANDLE: event circles are big metros (Phoenix,
Dallas, Las Vegas) and the six control cities are mid-size. A per-circle-day
count is therefore NOT a comparison. Three denominators are printed side by
side and the reader picks:
  per circle-day        (naive; confounded by metro size)
  per aircraft ENTERING (normalises for how busy the airspace is)
  per aircraft ON THE GROUND (normalises for how busy the RAMPS are - the
                        tightest of the three, and the one that most weakens
                        the following claim)
"""
import collections, csv, glob, gzip, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(HERE, "..", "data"))
SWEEP = os.path.join(DATA, "geo_sweep")
OUT = os.path.join(DATA, "analysis")
os.makedirs(OUT, exist_ok=True)

AIRLINER = {"A19N","A20N","A21N","A319","A320","A321","A332","A333","A339","A343","A359","A35K",
            "A388","B38M","B39M","B738","B739","B737","B752","B753","B762","B763","B764","B772",
            "B77L","B77W","B788","B789","B78X","B744","B748","E170","E175","E190","E195","CRJ2",
            "CRJ7","CRJ9","E75L","E75S","A306","B733","B734","B735","MD11"}

CATS = ["non_us_registration", "no_registration", "us_military_serial", "dbflag:military",
        "dbflag:PIA", "dbflag:LADD", "non_icao_address", "government_operator_string",
        "dbflag:interesting", "tracked_fleet"]


def cat_of(reasons):
    out = set()
    for r in reasons:
        out.add("tracked_fleet" if r.startswith("tracked_fleet:") else r)
    return out


def main():
    cd = {}                                   # (date, circle_key) -> counters
    cat = collections.Counter()               # (kind, category) -> notable-on-ground count
    control_rows = []
    n = 0
    for f in sorted(glob.glob(os.path.join(SWEEP, "*", "hits.csv.gz"))):
        with gzip.open(f, "rt") as fh:
            for r in csv.DictReader(fh):
                n += 1
                key = (r["sweep_date"], r["circle_key"])
                d = cd.get(key)
                if d is None:
                    d = cd[key] = dict(sweep_date=r["sweep_date"], circle_key=r["circle_key"],
                                       circle_kind=r["circle_kind"], city=r["city"], state=r["state"],
                                       event_date=r["event_date"], offset_days=r["offset_days"],
                                       who=r["who"], entering=0, on_ground=0,
                                       notable_ground_all=0, notable_ground_excl_airliner=0)
                d["entering"] += 1
                ground = r["on_ground_in_circle"] == "True"
                if not ground:
                    continue
                d["on_ground"] += 1
                reasons = [x for x in (r.get("flag_reasons") or "").split("|") if x]
                if not reasons:
                    continue
                d["notable_ground_all"] += 1
                typ = (r.get("type") or "").upper()
                if typ in AIRLINER:
                    continue
                d["notable_ground_excl_airliner"] += 1
                kind = r["circle_kind"]
                for c in cat_of(reasons):
                    cat[(kind, c)] += 1
                if kind == "control":
                    control_rows.append(dict(
                        sweep_date=r["sweep_date"], city=r["city"], state=r["state"],
                        hex=r["hex"], reg=r.get("reg", ""), type=typ,
                        operator=r.get("own_op", ""), year=r.get("year", ""),
                        flag_reasons="|".join(reasons),
                        nearest_field=r.get("nearest_field", ""),
                        nearest_field_mi=r.get("nearest_field_mi", ""),
                        closest_mi_to_city=r.get("closest_mi_to_city", ""),
                        points_in_circle=r.get("points_in_circle", ""),
                        first_utc=r.get("first_utc", ""), last_utc=r.get("last_utc", "")))
    print(f"scanned {n} rows, {len(cd)} circle-days", file=sys.stderr)

    rows = sorted(cd.values(), key=lambda x: (x["sweep_date"], x["circle_key"]))
    with open(os.path.join(OUT, "geo_circle_days.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

    control_rows.sort(key=lambda r: (r["sweep_date"], r["city"], r["reg"] or r["hex"]))
    with open(os.path.join(OUT, "geo_ground_control.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(control_rows[0].keys())); w.writeheader(); w.writerows(control_rows)

    agg = collections.defaultdict(collections.Counter)
    for r in rows:
        a = agg[r["circle_kind"]]
        a["circle_days"] += 1
        for k in ("entering", "on_ground", "notable_ground_all", "notable_ground_excl_airliner"):
            a[k] += r[k]
    with open(os.path.join(OUT, "geo_norm_rates.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["circle_kind", "circle_days", "aircraft_entering", "aircraft_on_ground",
                    "notable_on_ground_excl_airliners",
                    "per_circle_day", "pct_of_entering", "pct_of_on_ground",
                    "entering_per_circle_day", "on_ground_per_circle_day"])
        for k in ("event", "control"):
            a = agg[k]
            w.writerow([k, a["circle_days"], a["entering"], a["on_ground"],
                        a["notable_ground_excl_airliner"],
                        round(a["notable_ground_excl_airliner"] / a["circle_days"], 3),
                        round(100 * a["notable_ground_excl_airliner"] / a["entering"], 4),
                        round(100 * a["notable_ground_excl_airliner"] / a["on_ground"], 4),
                        round(a["entering"] / a["circle_days"], 1),
                        round(a["on_ground"] / a["circle_days"], 1)])

    with open(os.path.join(OUT, "geo_ground_by_category.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["category", "event_on_ground", "control_on_ground",
                    "event_pct_of_event_on_ground", "control_pct_of_control_on_ground", "ratio"])
        for c in CATS:
            e, ct = cat[("event", c)], cat[("control", c)]
            pe = 100 * e / agg["event"]["on_ground"]
            pc = 100 * ct / agg["control"]["on_ground"]
            w.writerow([c, e, ct, round(pe, 4), round(pc, 4),
                        round(pe / pc, 3) if pc else ""])
    print("wrote geo_circle_days.csv geo_ground_control.csv geo_norm_rates.csv "
          "geo_ground_by_category.csv", file=sys.stderr)


if __name__ == "__main__":
    main()
