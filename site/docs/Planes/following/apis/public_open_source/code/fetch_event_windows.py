#!/usr/bin/env python3
"""Pull the ADS-B aircraft-days that the speaking-event windows actually need.

`airports_near.py` can only answer "was an Egyptian jet here" for aircraft-days
this repo HOLDS A TRACE FOR. Most of the 139 speaking windows have no trace on
disk for most tails, and an empty answer from an unqueried day is worth nothing.
This script closes that gap: it works out every (tail, date) the windows need,
skips what is already on disk, and pulls the rest from the two free historical
archives.

    python3 fetch_event_windows.py --plan             what it would pull
    python3 fetch_event_windows.py --run              pull it
    python3 fetch_event_windows.py --run --side following   Egyptian tails only
    python3 fetch_event_windows.py --run --from 2025-01-01
    python3 fetch_event_windows.py --run --limit 200
    python3 fetch_event_windows.py --run --control    control aircraft, same dates

TWO RULES THIS SCRIPT EXISTS TO KEEP
------------------------------------
1. NOTHING IS EVER OVERWRITTEN. A day already on disk is skipped. `--repull`
   writes the new copy ALONGSIDE the old with a timestamp suffix, because the
   diff between two pulls of one URL on two dates is the evidence that
   something vanished.

2. A MISS IS RECORDED, NOT DISCARDED. An HTTP 404 means a volunteer receiver
   network heard nothing on that day. That is a coverage fact, and it is
   written to disk as a `.miss.json` meta record so the next run does not
   re-ask and so `airports_near.py` can tell "asked and got nothing" apart from
   "never asked". THOSE TWO ARE NOT THE SAME AND MUST NEVER BE MERGED.

BEFORE PUBLISHING ANY 4xx AS SUPPRESSION, RUN `--control`. Query an airframe
with no connection to this case over the same dates and the same endpoint. If
the control fails identically it is the ARCHIVE, not the airframe. Skipping
that test is how an investigation destroys its own credibility.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import gzip
import io
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))

HERE = os.path.dirname(os.path.abspath(__file__))
FOLLOWING = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
PLANES = os.path.normpath(os.path.join(FOLLOWING, ".."))
EVENTS_CSV = os.path.join(FOLLOWING, "tpusa_events.csv")
FLEET_JS = os.path.join(HERE, "lib", "fleet.js")

SOURCES = [
    ("airplanes-live", "https://globe.airplanes.live/globe_history/{y}/{m}/{d}/traces/{t2}/trace_full_{hex}.json"),
    ("adsb-lol", "https://adsb.lol/globe_history/{y}/{m}/{d}/traces/{t2}/trace_full_{hex}.json"),
]

# Aircraft with nothing to do with this case, queried over the same dates so a
# failure can be attributed to the archive instead of to the airframe.
CONTROLS = [
    {"reg": "CONTROL-RYANAIR", "hex": "4ca7b5", "side": "control"},
    {"reg": "CONTROL-LUFTHANSA", "hex": "3c6444", "side": "control"},
]

UA = ("charlie-kirk-investigation/1.0 (public-interest flight-record research; "
      "one request per aircraft-day; contact via the site)")


def load_fleet():
    txt = open(FLEET_JS, encoding="utf-8").read()
    out = []
    for m in re.finditer(r'\{\s*reg:\s*"([^"]+)",\s*hex:\s*"([^"]+)",\s*side:\s*"([^"]+)"', txt):
        out.append({"reg": m.group(1).upper(), "hex": m.group(2).lower(), "side": m.group(3)})
    return out


def parse_dates(raw):
    days = re.findall(r"\d{4}-\d{2}-\d{2}", raw or "")
    if days:
        return days[0], days[-1]
    m = re.match(r"(\d{4})-(\d{2})", raw or "")
    if m:
        y, mo = int(m.group(1)), int(m.group(2))
        last = dt.date(y + (mo == 12), (mo % 12) + 1, 1) - dt.timedelta(days=1)
        return f"{y:04d}-{mo:02d}-01", last.isoformat()
    return None, None


def window_days(window):
    days = set()
    with open(EVENTS_CSV, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            if "/speaking/" not in (r.get("mdx_page") or ""):
                continue
            first, last = parse_dates(r["dates"])
            if not first:
                continue
            cur = dt.date.fromisoformat(first) - dt.timedelta(days=window)
            end = dt.date.fromisoformat(last) + dt.timedelta(days=window)
            while cur <= end:
                days.add(cur.isoformat())
                cur += dt.timedelta(days=1)
    return sorted(days)


def recovered_dir(reg):
    return os.path.join(PLANES, reg, "data", "recovered")


def target_path(reg, day, source):
    return os.path.join(recovered_dir(reg), f"{reg}_{day}_{source}_trace_full.json")


def already_have(reg, day, source):
    """A day counts as held if the trace is on disk in EITHER form, or if the
    archive was already asked and had nothing."""
    p = target_path(reg, day, source)
    return (os.path.exists(p) or os.path.exists(p + ".gz")
            or os.path.exists(p.replace(".json", ".miss.json.meta.json")))


def fetch(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": UA,
                                               "Accept-Encoding": "gzip"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as res:
            raw = res.read()
            if res.headers.get("Content-Encoding") == "gzip" or raw[:2] == b"\x1f\x8b":
                try:
                    raw = gzip.decompress(raw)
                except OSError:
                    pass
            return res.status, raw
    except urllib.error.HTTPError as e:
        return e.code, b""
    except Exception as e:                                   # noqa: BLE001
        return 0, str(e).encode()


def save(reg, day, source, url, status, body, note=None):
    os.makedirs(recovered_dir(reg), exist_ok=True)
    stamp = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    stored_gzipped = False
    if status == 200 and body:
        # STORED GZIPPED. An ADS-B trace is repetitive JSON and compresses to
        # about 15% of its size; this repo's .git is already past 700 MB and a
        # full fleet sweep in raw JSON would add most of a gigabyte to a tree
        # that an automated job pushes every few minutes. The BYTES ARE
        # UNCHANGED - gzip is lossless, `gunzip -c` gives back the exact
        # response, and lib/traces.py reads either form transparently. The
        # earlier uncompressed files are left exactly as they are: nothing that
        # is already evidence gets rewritten.
        path = target_path(reg, day, source) + ".gz"
        if os.path.exists(path):
            path = path + ".pulled-" + stamp.replace(":", "-")
        with open(path, "wb") as fh:
            fh.write(gzip.compress(body, 6))
        stored_gzipped = True
    else:
        path = target_path(reg, day, source).replace(".json", ".miss.json")
    meta = {
        "url": url,
        "http_status": status,
        "bytes": len(body or b""),
        "stored_gzipped": stored_gzipped,
        "stored_bytes": (os.path.getsize(path) if status == 200 and body else 0),
        "retrieved_utc": stamp,
        "tail": reg,
        "date_utc": day,
        "source_key": source,
        "tool": "apis/public_open_source/code/fetch_event_windows.py",
        "note": note or (None if status == 200 else
                         "NO TRACE FOR THIS AIRCRAFT ON THIS DATE. A volunteer receiver "
                         "network heard nothing. Parked with the transponder off, outside "
                         "coverage, or the claimed date is wrong - all three look identical "
                         "from here. AN ABSENCE IS NOT A FINDING."),
    }
    with open(path + ".meta.json", "w", encoding="utf-8") as fh:
        json.dump(meta, fh, indent=2)
        fh.write("\n")
    return path


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--window", type=int, default=2)
    ap.add_argument("--side", action="append", default=[],
                    help="following | kirk | n1098l  (default: following)")
    ap.add_argument("--tail", action="append", default=[])
    ap.add_argument("--from", dest="dfrom", default=None)
    ap.add_argument("--to", dest="dto", default=None)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--sleep", type=float, default=0.4, help="seconds between requests")
    ap.add_argument("--repull", action="store_true")
    ap.add_argument("--control", action="store_true")
    args = ap.parse_args()

    fleet = CONTROLS if args.control else load_fleet()
    sides = set(args.side) or {"following"}
    if not args.control:
        fleet = [a for a in fleet if a["side"] in sides]
    if args.tail:
        want = {t.upper() for t in args.tail}
        fleet = [a for a in fleet if a["reg"] in want]

    days = window_days(args.window)
    if args.dfrom:
        days = [d for d in days if d >= args.dfrom]
    if args.dto:
        days = [d for d in days if d <= args.dto]

    jobs = []
    for ac in fleet:
        for day in days:
            for source, tmpl in SOURCES:
                if not args.repull and already_have(ac["reg"], day, source):
                    continue
                y, m, dd = day.split("-")
                jobs.append((ac, day, source,
                             tmpl.format(y=y, m=m, d=dd, t2=ac["hex"][-2:], hex=ac["hex"])))

    print(f"{len(fleet)} aircraft x {len(days)} window days x {len(SOURCES)} archives")
    print(f"{len(jobs)} requests needed ({len(fleet) * len(days) * len(SOURCES) - len(jobs)} "
          f"already on disk)")
    if args.limit:
        jobs = jobs[:args.limit]
        print(f"--limit: {len(jobs)} this run")
    est = len(jobs) * (args.sleep + 0.6) / 60
    print(f"estimated {est:.0f} min at {args.sleep}s between requests")

    if args.plan or not args.run:
        for ac, day, source, url in jobs[:15]:
            print(f"  {ac['reg']:8} {day} {source:16} {url}")
        if len(jobs) > 15:
            print(f"  ... and {len(jobs) - 15} more")
        return

    hits = misses = errors = 0
    t0 = time.time()
    for i, (ac, day, source, url) in enumerate(jobs, 1):
        status, body = fetch(url)
        save(ac["reg"], day, source, url, status, body)
        if status == 200:
            hits += 1
        elif status in (404, 403):
            misses += 1
        else:
            errors += 1
        if i % 50 == 0 or i == len(jobs):
            el = time.time() - t0
            print(f"  {i}/{len(jobs)}  hit={hits} miss={misses} err={errors}  "
                  f"{el / 60:.1f} min elapsed, ~{(el / i) * (len(jobs) - i) / 60:.0f} min left",
                  flush=True)
        time.sleep(args.sleep)

    print(f"\nDONE  {hits} traces recovered, {misses} days the archives do not hold, "
          f"{errors} transport errors")
    print("Now re-run:  python3 airports_near.py --rebuild-traces --report")
    if misses and not args.control:
        print("\nBEFORE CALLING ANY OF THOSE MISSES A REMOVAL, RUN:\n"
              "  python3 fetch_event_windows.py --run --control --from <date> --to <date>\n"
              "If the control aircraft fail the same way it is the archive, not the airframe.")


if __name__ == "__main__":
    main()
