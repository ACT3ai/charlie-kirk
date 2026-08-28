#!/usr/bin/env python3
"""RE-RUN THE SWEEP'S EXACT CIRCLE CHECK OVER THE PER-TAIL TRACES ALREADY ON DISK.

Why this exists. `geo_sweep.py` streams a whole UTC day and rejects most
aircraft with a BYTE PRE-FILTER before parsing. `prefilter_patterns()` builds
its longitude tokens with `math.floor`, but the LEADING TEXT of a negative
longitude is its TRUNCATION, not its floor: a point at -111.72 is written
"-111.72" and carries the token ",-111.", while floor(-111.72) is -112. For a
circle centred at -111.99 the function emits ",-113." and ",-112." and never
",-111." -- so the entire eastern half of that circle, INCLUDING ITS CENTRE, is
invisible to the pre-filter. An aircraft whose whole day never reaches a
longitude below -112 is dropped before `check_trace()` ever sees it.

This script does NOT touch the network. It replays the SAME `check_trace()`
against the traces this repo already holds per tail, so the tracked fleet can
be re-scored against every swept day's own circles.

SCOPE, AND IT MATTERS. This can only correct the count for the 17 tails we
already hold traces for. It CANNOT recover the unknown aircraft the sweep
dropped -- that needs the sweep re-run, which is a network job.

  OUT  data/analysis/sweep_recheck_local.csv
"""
import csv, glob, gzip, json, os, sys, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.normpath(os.path.join(HERE, ".."))                       # public_open_source
PLANES = os.path.normpath(os.path.join(HERE, "..", "..", "..", ".."))   # docs/Planes
SWEEP = os.path.join(BASE, "data", "geo_sweep")
AN = os.path.join(BASE, "data", "analysis")

spec = importlib.util.spec_from_file_location("gs", os.path.join(HERE, "geo_sweep.py"))
gs = importlib.util.module_from_spec(spec); spec.loader.exec_module(gs)


def load(path):
    op = gzip.open if path.endswith(".gz") else open
    with op(path, "rb") as fh:
        return json.loads(fh.read())


def main():
    out = []
    for meta_path in sorted(glob.glob(os.path.join(SWEEP, "*", "_sweep.meta.json"))):
        meta = json.load(open(meta_path))
        date = meta["sweep_date"]
        circles = meta["circles"]
        pl, po = gs.prefilter_patterns(circles)
        for tp in sorted(glob.glob(os.path.join(PLANES, "*", "data", "recovered",
                                                f"*_{date}_*_trace_full.json*"))):
            if ".meta.json" in tp or ".miss." in tp:
                continue
            tail = os.path.basename(tp).split("_")[0]
            src = os.path.basename(tp).split("_")[2]
            raw = open(tp, "rb").read()
            body = gzip.decompress(raw) if tp.endswith(".gz") else raw
            passes = bool(any(p in body for p in pl) and any(p in body for p in po))
            try:
                d = json.loads(body)
            except Exception:
                continue
            for h in gs.check_trace(d, circles):
                c = h["circle"]
                out.append(dict(
                    sweep_date=date, tail=tail, source=src,
                    circle_key=c["key"], circle_kind=c["kind"],
                    city=c["city"], state=c["state"],
                    event_date=c.get("event_date") or "", offset_days=c["offset_days"],
                    who=c.get("who") or "",
                    points_in_circle=h["n"], on_ground_in_circle=h["ground"],
                    min_dist_mi=round(h["min_dist"], 2),
                    ground_lat=h.get("ground_lat"), ground_lon=h.get("ground_lon"),
                    passed_geo_sweep_prefilter=passes,
                    trace_file=os.path.relpath(tp, PLANES)))
    out.sort(key=lambda r: (r["sweep_date"], r["tail"], r["circle_key"]))
    p = os.path.join(AN, "sweep_recheck_local.csv")
    with open(p, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
    print(f"wrote {p} rows={len(out)}", file=sys.stderr)
    missed = [r for r in out if not r["passed_geo_sweep_prefilter"]]
    print(f"rows the sweep's prefilter would have DROPPED: {len(missed)}", file=sys.stderr)
    mg = [r for r in missed if r["on_ground_in_circle"] and r["circle_kind"] == "event"]
    print(f"  ... of which ON THE GROUND in an EVENT circle: {len(mg)}", file=sys.stderr)
    for r in mg:
        print("   ", r["sweep_date"], r["tail"], r["city"], r["state"],
              r["min_dist_mi"], "mi", r["trace_file"], file=sys.stderr)


if __name__ == "__main__":
    main()
