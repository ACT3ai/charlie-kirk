#!/usr/bin/env python3
"""RE-RUN THE SAMPLE SWEEP'S EXACT CIRCLE CHECK OVER THE PER-TAIL TRACES ON DISK.

The sibling `recheck_sweep_circles_local.py` replays `geo_sweep.py`'s
`check_trace()` against `data/geo_sweep/` -- the adsb.lol GitHub-backup sweeps,
2023 onward. It does NOT look at `data/geo_sweep_samples/`, which is the ONLY
sweep layer that reaches 2022. This script closes that gap.

WHY IT MATTERS. `geo_sweep.py`'s byte pre-filter builds its longitude tokens
with `math.floor`, but the leading text of a negative longitude is its
TRUNCATION. A circle centred at -97.076 with a 50-mile pad spans -97.96..-96.19,
whose floors are -98 and -97, so the pre-filter emits ",-98." and ",-97." and
never ",-96." -- and an aircraft that spent the whole day east of -97 is dropped
before the exact check ever runs. Dallas Love Field is at -96.85, INSIDE the
2022-06-01 Grapevine circle and OUTSIDE the pre-filter's token set.

This touches NO network. It replays the exact check against traces already held.

SCOPE. It can only re-score the ~17 tails this repo holds traces for. It CANNOT
recover the unknown aircraft the sweep dropped; that needs the sweep re-run.

  OUT  data/analysis/sample_sweep_recheck_local.csv
"""
import csv, glob, gzip, json, os, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.normpath(os.path.join(HERE, ".."))
PLANES = os.path.normpath(os.path.join(HERE, "..", "..", "..", ".."))
SWEEP = os.path.join(BASE, "data", "geo_sweep_samples")
AN = os.path.join(BASE, "data", "analysis")

spec = importlib.util.spec_from_file_location("gs", os.path.join(HERE, "geo_sweep.py"))
gs = importlib.util.module_from_spec(spec); spec.loader.exec_module(gs)


def main():
    os.makedirs(AN, exist_ok=True)
    out = []
    for meta_path in sorted(glob.glob(os.path.join(SWEEP, "*", "_sweep.meta.json"))):
        meta = json.load(open(meta_path))
        date, circles = meta["sweep_date"], meta["circles"]
        pl, po = gs.prefilter_patterns(circles)
        in_hits = set()
        hp = os.path.join(os.path.dirname(meta_path), "hits.csv.gz")
        if os.path.exists(hp):
            with gzip.open(hp, "rt") as fh:
                for r in csv.DictReader(fh):
                    in_hits.add((r["circle_key"], r["hex"].lower()))
        for tp in sorted(glob.glob(os.path.join(
                PLANES, "*", "data", "recovered", f"*_{date}_*_trace_full.json*"))):
            if ".meta.json" in tp or ".miss." in tp:
                continue
            base = os.path.basename(tp)
            tail, src = base.split("_")[0], base.split("_")[2]
            raw = open(tp, "rb").read()
            body = gzip.decompress(raw) if tp.endswith(".gz") else raw
            passes = bool(any(p in body for p in pl) and any(p in body for p in po))
            try:
                d = json.loads(body)
            except Exception:
                continue
            for h in gs.check_trace(d, circles):
                lat = h["ground_lat"] if h["ground"] else h["min_lat"]
                lon = h["ground_lon"] if h["ground"] else h["min_lon"]
                field, fdist = gs.resolve_field(lat, lon)
                key = (h["circle"]["key"], (d.get("icao") or "").lower())
                out.append(dict(
                    sweep_date=date, circle_key=h["circle"]["key"],
                    city=h["circle"].get("city"), state=h["circle"].get("state"),
                    event_date=h["circle"].get("event_date"),
                    offset_days=h["circle"].get("offset_days"),
                    tail=tail, hex=(d.get("icao") or "").lower(),
                    reg=d.get("r"), type=d.get("t"), source=src,
                    points_in_circle=h["n"],
                    closest_mi=round(h["min_dist"], 2),
                    on_ground_in_circle=h["ground"],
                    min_alt_ft=h["min_alt"],
                    nearest_field=field, nearest_field_mi=fdist,
                    prefilter_would_pass=passes,
                    present_in_sweep_hits_csv=key in in_hits,
                    trace_file=os.path.relpath(tp, PLANES)))
    cols = list(out[0].keys()) if out else ["sweep_date"]
    op = os.path.join(AN, "sample_sweep_recheck_local.csv")
    with open(op, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols); w.writeheader(); w.writerows(out)
    print(f"{len(out)} circle-entries by tracked tails across the sample sweeps -> {op}")
    for r in out:
        print(f"  {r['sweep_date']} {r['circle_key']:24} {r['tail']:8} {r['reg']:8} "
              f"{r['closest_mi']:>7} mi  ground={r['on_ground_in_circle']}  "
              f"field={r['nearest_field']}  prefilter_pass={r['prefilter_would_pass']}  "
              f"in_hits_csv={r['present_in_sweep_hits_csv']}")


if __name__ == "__main__":
    main()
