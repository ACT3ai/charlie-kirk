#!/usr/bin/env python3
"""CLASSIFY EVERY "airplanes.live has it, adsb.lol does not" AIRCRAFT-DAY.

Reads ONLY files already on disk. Makes no network request.

Input : <PLANES>/<TAIL>/data/recovered/*.meta.json   (the archive's own answer,
        including the HTTP status it gave us) and the stored trace payloads.
Output: <analysis>/al_only_classified.csv  + al_only_summary.json

THE THREE STATES, and the evidence that separates them:

  RETENTION / SERVING BOUNDARY
      adsb.lol answered HTTP 403. Inside 2025-10-12..2025-11-05 EVERY request
      this investigation made to adsb.lol got 403 -- 14 tails including BOTH
      control airliners, zero 200s, zero 404s. That is the archive, not the
      airframe, and it can never be published as suppression.

  ARCHIVE COVERAGE GAP (whole day)
      adsb.lol answered 404 on a date where it also served NOTHING for any of
      the other aircraft asked that day. The day is thin or absent in that
      archive for everyone. Again the archive, not the airframe.

  ADSB_LOL_ARCHIVE_ABSENT_THAT_DAY
      A SECOND, INDEPENDENT route says adsb.lol has no archive for that UTC day
      at all: its own GitHub daily release (adsblol/globe_history_*) either does
      not exist or streamed 0 aircraft. Recorded in
      data/geo_sweep/<date>/_sweep.meta.json by geo_sweep.py.

  ONE-ARCHIVE-ONLY (the residue)
      adsb.lol answered 404 on a date it demonstrably served other aircraft.
      This is still NOT a removal. Two volunteer networks have different
      feeders; the median AL-only trace is about a THIRD the size of the
      median both-archives trace in every group INCLUDING the controls, which
      is the signature of marginal reception, not of deletion. Nothing on disk
      can distinguish "adsb.lol's feeders never heard it" from "it was taken
      out", because every pull in this repo comes from one 3-day window
      (2026-08-24..26) and no URL was pulled twice on two different dates.

Run:  python3 classify_al_only.py
"""
import collections, csv, glob, gzip, json, os, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PLANES = os.path.normpath(os.path.join(HERE, "..", "..", "..", ".."))
OUT = os.path.normpath(os.path.join(HERE, "..", "data", "analysis"))
BAND = ("2025-10-12", "2025-11-05")          # observed, not assumed -- see below
EGYPT = {"SU-BGM", "SU-BND", "SU-BTT", "SU-BTU", "SU-BTV"}
DARK_MIN_ASKED = 4                            # a "dark day" needs a real sample


def group(t):
    if t.startswith("CONTROL-"): return "CONTROL_AIRLINER"
    if t in EGYPT: return "EGYPT_SU"
    if t == "T7-ELL": return "T7_ELL"
    return "US_PRIVATE"


def region(lat, lon):
    if lat is None: return "UNKNOWN"
    if 24 <= lat <= 50 and -125 <= lon <= -66: return "USA"
    if 35 <= lat <= 72 and -12 <= lon <= 40: return "EUROPE"
    if 12 <= lat <= 40 and 24 <= lon <= 60: return "MIDEAST_EGYPT"
    if 0 <= lat <= 35 and -20 <= lon <= 52: return "AFRICA"
    return "OTHER"


def load_trace(p):
    try:
        return json.load(gzip.open(p)) if p.endswith(".gz") else json.load(open(p))
    except Exception:
        return None


def main():
    cells = collections.defaultdict(dict)
    for f in glob.glob(os.path.join(PLANES, "*", "data", "recovered", "*trace_full*.meta.json")):
        try: m = json.load(open(f))
        except Exception: continue          # one truncated double-write; reported separately
        tail = (m.get("tail") or "").upper()
        date = m.get("utc_date") or m.get("date_utc")
        src = m.get("source") or m.get("source_key")
        if not (tail and date and src): continue
        payload = f[: -len(".meta.json")]
        held = os.path.exists(payload)
        prev = cells[(tail, date)].get(src)
        if prev and prev["held"] and not held: continue   # .json/.gz duplicate pair
        cells[(tail, date)][src] = dict(held=held, status=m.get("http_status"),
                                        file=payload, url=m.get("url"),
                                        retrieved=m.get("retrieved_utc"))

    # per-date archive health: how many tails adsb.lol actually served that day
    health = collections.defaultdict(lambda: [0, 0])   # date -> [asked, lol_held]
    for (tail, date), v in cells.items():
        if "adsb-lol" in v:
            health[date][0] += 1
            if v["adsb-lol"]["held"]: health[date][1] += 1

    # SECOND ROUTE: adsb.lol's own GitHub daily release, already streamed to disk
    sweep = {}
    for f in glob.glob(os.path.join(OUT, "..", "geo_sweep", "*", "_sweep.meta.json")):
        try: m = json.load(open(f))
        except Exception: continue
        sweep[m.get("sweep_date")] = (m.get("status"), m.get("aircraft_in_archive") or 0)

    rows = []
    for (tail, date), v in sorted(cells.items()):
        a, l = v.get("adsb-lol"), v.get("airplanes-live")
        if not a or not l or not l["held"] or a["held"]: continue
        asked, lolheld = health[date]
        sw = sweep.get(date, ("NOT_SWEPT", ""))
        if a["status"] == 403 or BAND[0] <= date <= BAND[1]:
            cls = "RETENTION_SERVING_BOUNDARY"
        elif sw[0] == "NO_RELEASE_FOR_THIS_DATE" or (sw[0] == "SWEPT" and sw[1] == 0):
            cls = "ADSB_LOL_ARCHIVE_ABSENT_THAT_DAY"
        elif lolheld == 0 and asked >= DARK_MIN_ASKED:
            cls = "ARCHIVE_COVERAGE_GAP_WHOLE_DAY"
        else:
            cls = "ONE_ARCHIVE_ONLY"
        j = load_trace(l["file"])
        tr = (j or {}).get("trace") or []
        lats = [p[1] for p in tr if len(p) > 2 and p[1] is not None]
        lons = [p[2] for p in tr if len(p) > 2 and p[2] is not None]
        la = statistics.median(lats) if lats else None
        lo = statistics.median(lons) if lons else None
        rows.append(dict(tail=tail, date=date, group=group(tail),
                         classification=cls, adsb_lol_http=a["status"],
                         tails_asked_of_adsb_lol_that_day=asked,
                         tails_adsb_lol_served_that_day=lolheld,
                         al_trace_points=len(tr), region=region(la, lo),
                         median_lat=round(la, 3) if la is not None else "",
                         median_lon=round(lo, 3) if lo is not None else "",
                         adsb_lol_github_release=sw[0], aircraft_in_that_release=sw[1],
                         al_file=os.path.relpath(l["file"], PLANES),
                         adsb_lol_url=a["url"], retrieved_utc=a["retrieved"]))

    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, "al_only_classified.csv")
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

    # ---- the comparisons that decide whether any of this is about the aircraft
    both = collections.Counter(); only = collections.Counter()
    pts = collections.defaultdict(list)
    for (tail, date), v in cells.items():
        a, l = v.get("adsb-lol"), v.get("airplanes-live")
        if not a or not l or not l["held"]: continue
        if BAND[0] <= date <= BAND[1] or a["status"] == 403: continue
        j = load_trace(l["file"]); tr = (j or {}).get("trace") or []
        lats = [p[1] for p in tr if len(p) > 2 and p[1] is not None]
        lons = [p[2] for p in tr if len(p) > 2 and p[2] is not None]
        reg = region(statistics.median(lats) if lats else None,
                     statistics.median(lons) if lons else None)
        g = group(tail); k = "ALONLY" if not a["held"] else "BOTH"
        (only if k == "ALONLY" else both)[(g, reg)] += 1
        pts[(g, k)].append(len(tr))

    summary = dict(
        al_only_rows=len(rows),
        by_classification=dict(collections.Counter(r["classification"] for r in rows)),
        by_class_and_group=dict(collections.Counter(
            (r["classification"] + "|" + r["group"]) for r in rows)),
        rate_by_group_and_region={f"{g}|{reg}": dict(
            al_only=only[(g, reg)], both=both[(g, reg)],
            rate=round(only[(g, reg)] / (only[(g, reg)] + both[(g, reg)]), 4))
            for (g, reg) in sorted(set(list(only) + list(both)))},
        median_al_trace_points={f"{g}|{k}": dict(n=len(v), median=statistics.median(v))
                                for (g, k), v in sorted(pts.items())},
    )
    json.dump(summary, open(os.path.join(OUT, "al_only_summary.json"), "w"), indent=1)
    print(json.dumps(summary, indent=1))
    print("wrote " + path, file=sys.stderr)


if __name__ == "__main__":
    main()
