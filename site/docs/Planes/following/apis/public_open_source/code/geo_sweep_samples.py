#!/usr/bin/env python3
"""THE 2022 BRIDGE: the same geographic sweep, against the only free archive
that reaches back before 2023.

adsb.lol's daily GitHub backup -- the archive `geo_sweep.py` streams -- starts in
2023. The following-planes claim starts in 2022, and 38 of this investigation's
US event-days fall in that year. For those, exactly one free source exists:
ADS-B Exchange publishes a FREE SAMPLE of one complete day a month, always the
FIRST of the month, back to July 2016.

    https://samples.adsbexchange.com/traces/YYYY/MM/DD/index.json    the hex list
    https://samples.adsbexchange.com/traces/YYYY/MM/DD/<2>/trace_full_<hex>.json

THE LIMIT IS THE HEADLINE, NOT THE FOOTNOTE, AND IT TRAVELS WITH EVERY RESULT
----------------------------------------------------------------------------
One day in thirty. Of this investigation's 38 US event-days in 2022, exactly
TWO fall within a day of a sampled date:

    2022-03-31  Auburn, AL      -> sampled day 2022-04-01
    2022-06-02  Grapevine, TX   -> sampled day 2022-06-01

So this script does NOT "cover 2022". It covers two of thirty-eight event-days,
and the other thirty-six are not covered by anything free that exists. A sample
can show that an aircraft WAS somewhere. It can never support a rate, a
frequency, or a pattern, and nothing produced here may be quoted as if it could.

There is no whole-day tarball on the samples host, so each aircraft is a
separate HTTP request -- about 75,000 of them per sampled day. That is why this
is a separate script from `geo_sweep.py` and why it is run deliberately rather
than as part of the main sweep.

    python3 geo_sweep_samples.py --plan
    python3 geo_sweep_samples.py --run                  sampled days near an event
    python3 geo_sweep_samples.py --run --date 2022-06-01
    python3 geo_sweep_samples.py --run --city Provo --state UT --from 2022-01 --to 2022-12
        ^ every sampled day in a range against ONE city. This is the 2022
          Provo baseline: not an event test, a "what did this ramp look like
          before any of this started" test. Say which one you ran.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import gzip
import json
import os
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))

from geo import geocode_place                                          # noqa: E402
from targets import load_events                                        # noqa: E402
from geo_sweep import (check_trace, flag_aircraft, store_worthy,        # noqa: E402
                       prefilter_patterns, resolve_field, utcnow,
                       HITS_FIELDS, OUT_ROOT)
from atomic import write_json   # atomic: never leave a spliced evidence file  # noqa: E402

BASE = "https://samples.adsbexchange.com/traces/{y}/{m}/{d}"
SAMPLES_FLOOR = dt.date(2016, 7, 1)
SAMPLE_ROOT = os.path.join(os.path.dirname(OUT_ROOT), "geo_sweep_samples")


def sampled_days(start, end):
    """Every day ADS-B Exchange publishes free: the 1st of each month."""
    out, y, m = [], start.year, start.month
    while dt.date(y, m, 1) <= end:
        d = dt.date(y, m, 1)
        if d >= max(start, SAMPLES_FLOOR):
            out.append(d)
        m += 1
        if m == 13:
            y, m = y + 1, 1
    return out


def get(url, timeout=60, tries=3):
    for i in range(tries):
        try:
            with urllib.request.urlopen(
                    urllib.request.Request(url, headers={"User-Agent": "curl/8"}),
                    timeout=timeout) as r:
                return r.status, r.read()
        except Exception as e:
            if i == tries - 1:
                return getattr(e, "code", 0), b""
            time.sleep(1 + i)
    return 0, b""


def sweep_sample_day(day, circles, workers=20, prefilter=True):
    d = day.isoformat()
    y, mo, dd = d.split("-")
    base = BASE.format(y=y, m=mo, d=dd)
    meta = {
        "sweep_date": d, "retrieved_utc": utcnow(), "source": "adsbexchange-samples",
        "index_url": f"{base}/index.json",
        "sample_basis": "ADS-B Exchange free monthly sample: ONE DAY A MONTH, always the "
                        "1st. A hit fixes a position on this date and says NOTHING about "
                        "frequency. 36 of this investigation's 38 US event-days in 2022 "
                        "are not covered by this or by any other free source.",
        "circles": [{"key": c["key"], "kind": c["kind"], "city": c.get("city"),
                     "state": c.get("state"), "lat": c["lat"], "lon": c["lon"],
                     "radius_mi": c["radius_mi"], "offset_days": c.get("offset_days"),
                     "event_date": c.get("date")} for c in circles],
    }
    st, body = get(meta["index_url"])
    if st != 200 or not body:
        meta.update(status="NO_SAMPLE_FOR_THIS_DATE", http_status=st,
                    aircraft_in_archive=0, hits=0)
        return [], meta
    hexes = json.loads(body).get("traces", [])
    pl, po = prefilter_patterns(circles) if prefilter else ([], [])
    t0 = time.time()
    hits, keep = [], {}
    counters = {"files": 0, "bytes": 0, "deep": 0, "miss": 0}

    def one(h):
        url = f"{base}/{h[-2:]}/trace_full_{h}.json"
        s, b = get(url, timeout=45)
        if s != 200 or not b:
            counters["miss"] += 1
            return None
        counters["files"] += 1
        counters["bytes"] += len(b)
        if b[:2] == b"\x1f\x8b":
            b = gzip.decompress(b)
        if prefilter and not (any(p in b for p in pl) and any(p in b for p in po)):
            return None
        counters["deep"] += 1
        try:
            return json.loads(b), b
        except Exception:
            return None

    with ThreadPoolExecutor(max_workers=workers) as ex:
        for res in ex.map(one, hexes):
            if not res:
                continue
            rec, raw = res
            got = check_trace(rec, circles)
            if not got:
                continue
            reasons = flag_aircraft(rec)
            for hit in got:
                lat = hit["ground_lat"] if hit["ground"] else hit["min_lat"]
                lon = hit["ground_lon"] if hit["ground"] else hit["min_lon"]
                field, fdist = resolve_field(lat, lon)
                hits.append({
                    "sweep_date": d, "circle_key": hit["circle"]["key"],
                    "circle_kind": hit["circle"]["kind"], "city": hit["circle"].get("city"),
                    "state": hit["circle"].get("state"),
                    "event_date": hit["circle"].get("date"),
                    "offset_days": hit["circle"].get("offset_days"),
                    "who": hit["circle"].get("who"),
                    "hex": rec.get("icao"), "reg": rec.get("r") or "",
                    "type": rec.get("t") or "", "own_op": rec.get("ownOp") or "",
                    "year": rec.get("year") or "", "db_flags": int(rec.get("dbFlags") or 0),
                    "flag_reasons": "|".join(reasons), "flagged": bool(reasons),
                    "points_in_circle": hit["n"],
                    "first_utc": dt.datetime.fromtimestamp(hit["first"], dt.timezone.utc).isoformat()
                                  if hit["first"] else "",
                    "last_utc": dt.datetime.fromtimestamp(hit["last"], dt.timezone.utc).isoformat()
                                 if hit["last"] else "",
                    "closest_mi_to_city": round(hit["min_dist"], 2),
                    "closest_lat": round(hit["min_lat"], 5) if hit["min_lat"] is not None else "",
                    "closest_lon": round(hit["min_lon"], 5) if hit["min_lon"] is not None else "",
                    "on_ground_in_circle": hit["ground"],
                    "min_alt_ft": hit["min_alt"] if hit["min_alt"] is not None else "",
                    "nearest_field": field or "",
                    "nearest_field_mi": fdist if fdist is not None else "",
                })
            if store_worthy(reasons, got):
                keep[rec.get("icao")] = raw

    outdir = os.path.join(SAMPLE_ROOT, d)
    if keep:
        tdir = os.path.join(outdir, "traces")
        os.makedirs(tdir, exist_ok=True)
        for hexid, b in keep.items():
            path = os.path.join(tdir, f"{hexid}.json.gz")
            if os.path.exists(path):
                path = os.path.join(tdir, f"{hexid}.{utcnow()[:19].replace(':', '')}.json.gz")
            with gzip.open(path, "wb") as fh:
                fh.write(b)

    meta.update(status="SWEPT", aircraft_in_index=len(hexes),
                aircraft_in_archive=counters["files"], not_retrievable=counters["miss"],
                deep_parsed=counters["deep"], archive_bytes=counters["bytes"],
                hits=len(hits), distinct_aircraft_in_circles=len({h["hex"] for h in hits}),
                flagged_aircraft_stored=len(keep), seconds=round(time.time() - t0, 1))
    return hits, meta


def write_day(day, hits, meta):
    d = day.isoformat()
    outdir = os.path.join(SAMPLE_ROOT, d)
    os.makedirs(outdir, exist_ok=True)
    mp = os.path.join(outdir, "_sweep.meta.json")
    if os.path.exists(mp):
        mp = os.path.join(outdir, f"_sweep.{utcnow()[:19].replace(':', '')}.meta.json")
    write_json(mp, meta, indent=2)
    hp = os.path.join(outdir, "hits.csv.gz")
    if os.path.exists(hp):
        hp = os.path.join(outdir, f"hits.{utcnow()[:19].replace(':', '')}.csv.gz")
    with gzip.open(hp, "wt", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=HITS_FIELDS)
        w.writeheader()
        for h in sorted(hits, key=lambda x: (not x["flagged"], x["circle_key"], x["hex"])):
            w.writerow(h)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--date", action="append")
    ap.add_argument("--city"), ap.add_argument("--state")
    ap.add_argument("--from", dest="frm", help="YYYY-MM, with --city")
    ap.add_argument("--to", dest="to", help="YYYY-MM, with --city")
    ap.add_argument("--radius", type=float, default=50.0)
    ap.add_argument("--window", type=int, default=1)
    ap.add_argument("--workers", type=int, default=20)
    ap.add_argument("--repull", action="store_true")
    args = ap.parse_args()

    work = {}
    if args.city:
        g = geocode_place(args.city, args.state, "USA")
        if not g:
            print(f"cannot geocode {args.city}, {args.state}"); return
        a = dt.date(*[int(x) for x in (args.frm or "2022-01").split("-")], 1)
        b = dt.date(*[int(x) for x in (args.to or "2022-12").split("-")], 1)
        circle = {"key": f"baseline_{args.city.lower().replace(' ', '_')}", "kind": "baseline",
                  "city": args.city, "state": args.state, "lat": g["lat"], "lon": g["lon"],
                  "radius_mi": args.radius, "center_basis": g["method"], "offset_days": None,
                  "who": "BASELINE — not tied to any event date"}
        for d in sampled_days(a, b):
            work[d] = [dict(circle, sweep_date=d.isoformat())]
    else:
        events, _, _ = load_events(args.radius)
        for e in events:
            d0 = dt.date.fromisoformat(e["date"])
            for d in sampled_days(d0 - dt.timedelta(days=args.window),
                                  d0 + dt.timedelta(days=args.window)):
                if abs((d - d0).days) <= args.window:
                    work.setdefault(d, []).append(
                        dict(e, offset_days=(d - d0).days, sweep_date=d.isoformat()))

    if args.date:
        want = {dt.date.fromisoformat(x) for x in args.date}
        work = {k: v for k, v in work.items() if k in want}
    if not args.repull:
        work = {k: v for k, v in work.items()
                if not os.path.exists(os.path.join(SAMPLE_ROOT, k.isoformat(),
                                                   "_sweep.meta.json"))}

    if args.plan or not args.run:
        print(f"{len(work)} sampled day(s) reachable, radius {args.radius} mi, "
              f"window +/-{args.window} d")
        for d in sorted(work):
            print(f"  {d}  " + ", ".join(
                f"{c.get('city')},{c.get('state')}"
                + (f" (event {c['date']}, {c['offset_days']:+d}d)" if c.get("date") else "")
                for c in work[d]))
        if not args.city:
            print("\nThe other 2022 event-days have NO free archive of any kind. "
                  "That is a coverage fact and it must be published as one.")
        return

    for d in sorted(work):
        print(f"{d}  {', '.join(str(c.get('city')) for c in work[d])}", flush=True)
        hits, meta = sweep_sample_day(d, work[d], args.workers)
        write_day(d, hits, meta)
        if meta["status"] != "SWEPT":
            print(f"    {meta['status']}", flush=True); continue
        print(f"    {meta['aircraft_in_archive']}/{meta['aircraft_in_index']} traces "
              f"retrieved, {meta['distinct_aircraft_in_circles']} in circles, "
              f"{meta['flagged_aircraft_stored']} kept, {meta['seconds']}s", flush=True)
        gnd = sorted({h["reg"] or h["hex"] for h in hits
                      if h["flagged"] and h["on_ground_in_circle"]})
        if gnd:
            print("    notable, on the ground: " + ", ".join(gnd[:25]), flush=True)


if __name__ == "__main__":
    main()
