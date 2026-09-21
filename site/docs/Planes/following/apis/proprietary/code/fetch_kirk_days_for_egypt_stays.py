#!/usr/bin/env python3
"""Pull the free ADS-B traces a Kirk-side aircraft needs to be checked against every
Egyptian stay in the United States.

The overlap question is "was a Kirk plane on the ground where an Egyptian jet was, when it
was there". The Egyptian half is complete - FlightAware's record of every stay, 2022-2025.
The Kirk half has holes: N102DZ and N582MM are blocked on FlightAware, so their record is
whatever the free volunteer archives heard, and nobody had ever asked those archives about
most of the days that matter. This asks.

    python3 fetch_kirk_days_for_egypt_stays.py                  plan only: which days, how many
    python3 fetch_kirk_days_for_egypt_stays.py --run
    python3 fetch_kirk_days_for_egypt_stays.py --run --tails N102DZ

WHAT IT ASKS. Every UTC day from one day before an Egyptian jet arrived at a US airport to
one day after it left, for every stay of nine days or fewer. The multi-month stays - an
aircraft parked at a maintenance field for a season - are a different question and are
left to be reported as parked, not swept day by day.

WHERE IT ASKS. The two free daily archives, side by side: globe.airplanes.live and
adsb.lol. Neither reaches 2022 (their floor is February 2023), so 2022 days are skipped and
counted as unreachable rather than silently dropped.

WHAT IT WRITES, in the repo's own convention under Planes/<TAIL>/data/recovered/:
  <TAIL>_<date>_<source>_trace_full.json.gz + .meta.json      a trace the archive holds
  <TAIL>_<date>_<source>_trace_full.miss.json.meta.json       asked; the archive holds nothing
A refusal (HTTP 403, adsb.lol's site-wide band) is NOT written as a miss - a refusal is not
an answer, and recording it as "asked and empty" would turn an archive outage into a
finding. Nothing already on disk is fetched or overwritten again.
"""
import gzip, json, os, sys, time, urllib.error, urllib.request
from datetime import datetime, timedelta, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import find_egypt_kirk_overlaps as fek  # noqa: E402

HEX = {"N102DZ": "a00c85", "N582MM": "a77e75", "N560TW": "a728a8", "N888KG": "ac3c75", "N872RA": "abff3c", "N40JD": "a4ab14"}
SOURCES = [("airplanes-live", "https://globe.airplanes.live/globe_history/{y}/{m}/{d}/traces/{h2}/trace_full_{h}.json"),
           ("adsb-lol", "https://adsb.lol/globe_history/{y}/{m}/{d}/traces/{h2}/trace_full_{h}.json")]
FLOOR = datetime(2023, 2, 6, tzinfo=timezone.utc).date()
MAX_STAY_DAYS = 9
UA = "Mozilla/5.0 (charlie-kirk investigation; overlap coverage)"


def recovered_dir(tail):
    return os.path.join(fek.PLANES, tail, "data", "recovered")


def already(tail, day, source):
    d = recovered_dir(tail)
    stem = f"{tail}_{day}_{source}_trace_full"
    for suffix in (".json", ".json.gz", ".miss.json.meta.json"):
        if os.path.exists(os.path.join(d, stem + suffix)):
            return True
    return False


def plan(tails):
    days = set()
    unreachable = set()
    for s in fek.egyptian_stays():
        if s["arrive"].year > 2025:
            continue
        if (s["leave"] - s["arrive"]).days > MAX_STAY_DAYS:
            continue
        x = (s["arrive"] - timedelta(days=1)).date()
        last = (s["leave"] + timedelta(days=1)).date()
        while x <= last:
            (days if x >= FLOOR else unreachable).add(x)
            x += timedelta(days=1)
    todo = [(t, d, src, url) for t in tails for d in sorted(days) for src, url in SOURCES if not already(t, d.isoformat(), src)]
    return todo, days, unreachable


def fetch(tail, day, source, pattern):
    h = HEX[tail]
    url = pattern.format(y=f"{day.year:04d}", m=f"{day.month:02d}", d=f"{day.day:02d}", h2=h[-2:], h=h)
    d = recovered_dir(tail)
    os.makedirs(d, exist_ok=True)
    stem = os.path.join(d, f"{tail}_{day.isoformat()}_{source}_trace_full")
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=40) as r:
            wire = r.read()
            status = r.status
    except urllib.error.HTTPError as e:
        if e.code == 404:
            json.dump({"url": url, "http_status": 404, "retrieved_utc": now, "source_key": source,
                       "why": "Egyptian-stay overlap coverage: asked, the archive holds no trace for this aircraft on this day."},
                      open(stem + ".miss.json.meta.json", "w"), indent=2)
            return "miss"
        return f"http{e.code}"
    except Exception as e:
        return "error:" + type(e).__name__
    try:
        body = gzip.decompress(wire)
    except Exception:
        body = wire
    try:
        points = len(json.loads(body).get("trace", []))
    except Exception:
        return "unparseable"
    with open(stem + ".json.gz", "wb") as fh:
        fh.write(gzip.compress(body))
    json.dump({"url": url, "http_status": status, "bytes_wire": len(wire), "bytes_uncompressed": len(body),
               "stored_gzipped": True, "bytes_stored": os.path.getsize(stem + ".json.gz"), "retrieved_utc": now,
               "source_key": source, "trace_points": points,
               "why": "Egyptian-stay overlap coverage: was this Kirk-side aircraft near an Egyptian jet's US stay?"},
              open(stem + ".json.gz.meta.json", "w"), indent=2)
    return "held"


def main():
    args = sys.argv[1:]
    run = "--run" in args
    tails = ["N102DZ", "N582MM"]
    if "--tails" in args:
        tails = [t.strip() for t in args[args.index("--tails") + 1].split(",")]
    todo, days, unreachable = plan(tails)
    print(f"days around short Egyptian stays: {len(days)} reachable (2023+), {len(unreachable)} before the free archives' floor")
    for t in tails:
        n = sum(1 for x in todo if x[0] == t)
        print(f"  {t}: {n} archive requests still to ask")
    if not run:
        print("PLAN ONLY - nothing fetched. Add --run.")
        return
    tally = {}
    for i, (t, d, src, pattern) in enumerate(todo, 1):
        res = fetch(t, d, src, pattern)
        tally[(t, res)] = tally.get((t, res), 0) + 1
        if i % 50 == 0:
            print(f"  ... {i}/{len(todo)}", {f"{k[0]} {k[1]}": v for k, v in sorted(tally.items())}, flush=True)
        time.sleep(0.25)
    print("done:", {f"{k[0]} {k[1]}": v for k, v in sorted(tally.items())})


if __name__ == "__main__":
    main()
