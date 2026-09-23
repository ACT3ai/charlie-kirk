#!/usr/bin/env python3
"""Ask the free daily ADS-B archives about EVERY day for a set of tails, not just event windows.

Every earlier pull asked about the days somebody already suspected mattered - an event window,
an Egyptian stay. That can find an aircraft where we looked; it can never show where else it
went. The questions this answers need the whole record:

  * which trips a Kirk-side jet made on days a Kirk had a public event, and which it made on
    days nobody did (the "flew without them" pattern);
  * what a blocked tail (N102DZ, N582MM, N888KG, T7-ELL) did in the period FlightAware and
    Flightradar24 hide it.

    python3 sweep_tail_days.py                                   plan only
    python3 sweep_tail_days.py --run [--tails N102DZ,N582MM] [--from 2023-02-06] [--to 2026-09-16]

ORDER OF ASKING. globe.airplanes.live first (it holds 5-10x more per day). adsb.lol is asked
only on a day airplanes.live does not hold, so the second network fills gaps instead of
doubling the load. A day is finished when either network holds a trace, or both have been
asked and hold nothing.

WHAT IT WRITES, the repo's own convention, under Planes/<TAIL>/data/recovered/:
  <TAIL>_<date>_<source>_trace_full.json.gz + .meta.json      held
  <TAIL>_<date>_<source>_trace_full.miss.json.meta.json       asked, the archive holds nothing
A refusal (403, adsb.lol's site-wide band) or a network error is NOT written - it is not an
answer. Nothing already on disk is asked again or overwritten.
"""
import gzip, json, os, sys, threading, time, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timedelta, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
PLANES = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
HEX = {"N102DZ": "a00c85", "N582MM": "a77e75", "N888KG": "ac3c75", "T7-ELL": "50018a",
       "N560TW": "a728a8", "N40JD": "a4ab14", "N872RA": "abff3c",
       # Second Learjet 60 recurring at Kirk event cities (geo_recurrence_all_aircraft.csv).
       "N79SC": "aab73f",
       # Adelson / Las Vegas Sands fleet, FAA registry 2026-09-15, for the claimed "meet-ups".
       "N804MS": "aaf1dd", "N108MS": "a02390", "N885LS": "ac3173", "N889LS": "ac404f",
       "N336LS": "a3ad24", "N337LS": "a3b0db", "N338LS": "a3b492", "N339LS": "a3b849"}
SOURCES = [("airplanes-live", "https://globe.airplanes.live/globe_history/{y}/{m}/{d}/traces/{h2}/trace_full_{h}.json"),
           ("adsb-lol", "https://adsb.lol/globe_history/{y}/{m}/{d}/traces/{h2}/trace_full_{h}.json")]
UA = "Mozilla/5.0 (charlie-kirk investigation; full-record sweep)"
WHY = "Full-record sweep: every day for this tail, so trips on days with no public event can be seen."


def stem(tail, day, source):
    return os.path.join(PLANES, tail, "data", "recovered", f"{tail}_{day}_{source}_trace_full")


def state(tail, day, source):
    s = stem(tail, day, source)
    if os.path.exists(s + ".json") or os.path.exists(s + ".json.gz"):
        return "held"
    if os.path.exists(s + ".miss.json.meta.json"):
        return "miss"
    return None


def ask(tail, day, source, pattern):
    h = HEX[tail]
    url = pattern.format(y=f"{day.year:04d}", m=f"{day.month:02d}", d=f"{day.day:02d}", h2=h[-2:], h=h)
    s = stem(tail, day.isoformat(), source)
    os.makedirs(os.path.dirname(s), exist_ok=True)
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    for attempt in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=40) as r:
                wire, status = r.read(), r.status
            break
        except urllib.error.HTTPError as e:
            if e.code == 404:
                json.dump({"url": url, "http_status": 404, "retrieved_utc": now, "source_key": source,
                           "why": WHY + " Asked; the archive holds no trace for this aircraft on this day."},
                          open(s + ".miss.json.meta.json", "w"), indent=2)
                return "miss"
            if e.code == 429:
                time.sleep(5 * (attempt + 1))
                continue
            return f"http{e.code}"
        except Exception as e:
            if attempt == 2:
                return "error:" + type(e).__name__
            time.sleep(3)
    else:
        return "http429"
    try:
        body = gzip.decompress(wire)
    except Exception:
        body = wire
    try:
        points = len(json.loads(body).get("trace", []))
    except Exception:
        return "unparseable"
    with open(s + ".json.gz", "wb") as fh:
        fh.write(gzip.compress(body))
    json.dump({"url": url, "http_status": status, "bytes_wire": len(wire), "bytes_uncompressed": len(body),
               "stored_gzipped": True, "bytes_stored": os.path.getsize(s + ".json.gz"), "retrieved_utc": now,
               "source_key": source, "trace_points": points, "why": WHY},
              open(s + ".json.gz.meta.json", "w"), indent=2)
    return "held"


def work(tail, day):
    """One aircraft-day: airplanes.live, then adsb.lol only if needed."""
    d = day.isoformat()
    out = []
    first = state(tail, d, SOURCES[0][0]) or ask(tail, day, *SOURCES[0])
    out.append(("airplanes-live", first))
    if first == "held" or state(tail, d, SOURCES[1][0]) == "held":
        return out
    second = state(tail, d, SOURCES[1][0]) or ask(tail, day, *SOURCES[1])
    out.append(("adsb-lol", second))
    return out


def main():
    a = sys.argv[1:]
    get = lambda k, dflt: a[a.index(k) + 1] if k in a else dflt
    tails = get("--tails", ",".join(HEX)).split(",")
    d0 = date.fromisoformat(get("--from", "2023-02-06"))
    d1 = date.fromisoformat(get("--to", "2026-09-16"))
    days = [d0 + timedelta(n) for n in range((d1 - d0).days + 1)]
    todo = []
    for t in tails:
        n = 0
        for d in days:
            s0, s1 = state(t, d.isoformat(), "airplanes-live"), state(t, d.isoformat(), "adsb-lol")
            if s0 == "held" or s1 == "held" or (s0 and s1):
                continue
            todo.append((t, d))
            n += 1
        print(f"{t}: {n} of {len(days)} days still to ask")
    if "--run" not in a:
        print("PLAN ONLY - add --run")
        return
    tally, lock, done = {}, threading.Lock(), [0]

    def job(td):
        res = work(*td)
        with lock:
            for src, r in res:
                tally[(td[0], src, r)] = tally.get((td[0], src, r), 0) + 1
            done[0] += 1
            if done[0] % 200 == 0:
                print(f"... {done[0]}/{len(todo)}", flush=True)

    with ThreadPoolExecutor(max_workers=int(get("--jobs", "6"))) as ex:
        list(ex.map(job, todo))
    for k in sorted(tally):
        print(" ".join(k), tally[k])


if __name__ == "__main__":
    main()
