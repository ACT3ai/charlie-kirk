#!/usr/bin/env python3
"""
RE-EXTRACT THE FLIGHT ROWS FROM THE ARCHIVED TRACKING PAGES.

Why this file exists. recover_erased.js pulled 39 Internet Archive copies of
Flightradar24 and FlightAware aircraft pages and wrote `flight_rows_recovered: 0`
(FR24) or `null` (FlightAware) into every sidecar. BOTH NUMBERS WERE WRONG. The
FR24 parser in recover_erased.js worked on a stripped text rendering and matched
a row shape those pages do not use; the FlightAware pages were never parsed at
all. The rows were on disk the whole time.

That distinction matters more than the bug does. A "0" in a provenance sidecar
reads as AN ABSENCE OF EVIDENCE. Here it was an absence of parsing. Anything on
this site that rested on those zeros has to be re-read.

WHAT THIS EXTRACTS
  FR24        <tr class=" data-row" data-timestamp="EPOCH"> ... the server-rendered
              FLIGHTS HISTORY table. Epochs are UTC and exact.
  FlightAware pre-2017 captures only. The modern pages are a JavaScript shell
              (trackpollBootstrap) with no server-rendered rows -- 458 KB of
              chrome and no data. Those are reported as SHELL, not as zero.

WHAT A ROW DOES AND DOES NOT MEAN. A recovered row is what the site PUBLISHED on
the snapshot date. It is a tracking site's own reading of ADS-B, not a facility
record, and FR24 rows can carry scheduled rather than actual times. Where the
row and an ADS-B trace disagree, the trace is the better evidence and the
disagreement gets written down.

  python3 extract_wayback_flights.py            # every capture, write JSON
  python3 extract_wayback_flights.py --dry-run  # report only
"""
import re, os, json, glob, sys, datetime
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
from atomic import write_json   # atomic: never leave a spliced evidence file

PLANES = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../"))
DRY = "--dry-run" in sys.argv
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z")

def iso(ep):
    if not ep: return None
    return datetime.datetime.fromtimestamp(int(ep), datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

# ------------------------------------------------------------------ FR24
ROW = re.compile(r'<tr class="\s*data-row"\s+data-timestamp="(\d+)"(.*?)(?=<tr class="\s*data-row"|</tbody>)', re.S)
def fr24_rows(html):
    out = []
    for m in ROW.finditer(html):
        std_ep, body = m.group(1), m.group(2)
        def port(label):
            p = re.search(r'<label>%s</label>\s*<span class="details">\s*(.*?)</span>' % label, body, re.S)
            if not p: return None, None
            t = p.group(1)
            code = re.search(r'\(([A-Z0-9]{3})\)', t)
            name = re.sub(r'<[^>]+>', ' ', t)
            name = re.sub(r'\([A-Z0-9]{3}\)', '', name)
            return re.sub(r'\s+', ' ', name).strip(), (code.group(1) if code else None)
        fr_n, fr_c = port("FROM"); to_n, to_c = port("TO")
        land = re.search(r'data-timestamp="(\d+)"[^>]*data-prefix="([^"]*)"[^>]*>\s*([A-Za-z ]*?)\s*(\d{1,2}:\d{2})', body)
        ft = re.search(r'fa-clock-o"></i>\s*([\d:]+)', body)
        dt = re.search(r'data-time-format="DD MMM YYYY"[^>]*>\s*<i[^>]*></i>\s*([0-9]{1,2} [A-Za-z]{3} [0-9]{4})', body)
        std = re.search(r'<label>STD</label>\s*<span class="details" data-timestamp="(\d+)"', body)
        atd = re.search(r'<label>ATD</label>\s*<span class="details" data-timestamp="(\d+)"', body)
        sta = re.search(r'<label>STA</label>\s*<span class="details" data-timestamp="(\d+)"', body)
        out.append({
            "date": dt.group(1) if dt else None,
            "std_epoch": int(std_ep), "std_utc": iso(std_ep),
            "atd_utc": iso(atd.group(1)) if atd else None,
            "sta_utc": iso(sta.group(1)) if sta else None,
            "arr_utc": iso(land.group(1)) if land else None,
            "status": (land.group(3).strip() or land.group(2).strip()) if land else None,
            "flight_time": ft.group(1) if ft else None,
            "from_name": fr_n, "from_code": fr_c, "to_name": to_n, "to_code": to_c,
        })
    return out

def fr24_ident(html):
    t = re.sub(r'<[^>]+>', ' ', html)
    t = re.sub(r'&nbsp;', ' ', t); t = re.sub(r'\s+', ' ', t)
    g = lambda r: (re.search(r, t).group(1).strip() if re.search(r, t) else None)
    return {"aircraft": g(r'AIRCRAFT\s+(.+?)\s+AIRLINE'),
            "operator": g(r'OPERATOR\s+(.+?)\s+(?:JET|TYPE|MODE)'),
            "type_code": g(r'TYPE CODE\s+([A-Z0-9]+)'),
            "mode_s": g(r'MODE S\s+([A-F0-9]{6})'),
            "serial": g(r'SERIAL NUMBER \(MSN\)\s+(\S+)')}

# ------------------------------------------------------- FlightAware (legacy)
def fa_rows(html):
    if "trackpollBootstrap" in html and html.count("<tr") < 5:
        return None                                   # JavaScript shell, not data
    rows, seen = [], set()
    for tr in re.findall(r'<tr[^>]*>(.*?)</tr>', html, re.S):
        cells = [re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', c)).strip()
                 for c in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', tr, re.S)]
        line = " | ".join(cells)
        if not re.search(r'\d{1,2}-[A-Z][a-z]{2}-\d{4}', line): continue
        codes = re.findall(r'\b([KPC][A-Z]{3}|[A-Z]{4})\b', line)
        d = re.search(r'(\d{1,2}-[A-Z][a-z]{2}-\d{4})', line)
        key = (d.group(1), tuple(codes[:2]))
        if key in seen: continue
        seen.add(key)
        rows.append({"date": d.group(1), "airports": codes[:4], "cells": cells[:8]})
    return rows

# ------------------------------------------------------------------- main
report, totals = [], {"fr24_rows": 0, "fa_rows": 0, "fr24_files": 0, "fa_files": 0,
                      "fa_shell": 0, "fr24_empty": 0}
for path in sorted(glob.glob(os.path.join(PLANES, "*/data/recovered/*_wayback_*.html"))):
    base = os.path.basename(path)
    m = re.match(r'(.+?)_(\d{14})_wayback_(\w+)\.html$', base)
    if not m: continue
    tail, ts, site = m.groups()
    html = open(path, encoding="utf-8", errors="replace").read()
    meta_path = path + ".meta.json"
    meta = json.load(open(meta_path)) if os.path.exists(meta_path) else {}
    rec = {"tail": tail, "snapshot_utc": ts, "site": site, "file": base,
           "bytes": len(html), "live_http_today": meta.get("live_http_today"),
           "previously_recorded": meta.get("flight_rows_recovered")}
    if site == "flightradar24":
        rows = fr24_rows(html); totals["fr24_files"] += 1; totals["fr24_rows"] += len(rows)
        if not rows: totals["fr24_empty"] += 1
        rec.update(rows_recovered=len(rows), identity=fr24_ident(html), flights=rows,
                   table_state="POPULATED" if rows else "PRESENT_BUT_EMPTY")
    else:
        rows = fa_rows(html); totals["fa_files"] += 1
        if rows is None:
            totals["fa_shell"] += 1
            rec.update(rows_recovered=0, flights=[], table_state="JAVASCRIPT_SHELL_NO_SERVER_RENDERED_ROWS")
        else:
            totals["fa_rows"] += len(rows)
            rec.update(rows_recovered=len(rows), flights=rows,
                       table_state="POPULATED" if rows else "PRESENT_BUT_EMPTY")
    report.append(rec)
    if not DRY:
        out = path.replace(".html", "_flights.json")
        json.dump({"extracted_utc": NOW, "extractor": "extract_wayback_flights.py",
                   "supersedes": "flight_rows_recovered in the .meta.json sidecar, which was wrong",
                   **rec}, open(out, "w"), indent=2)
        meta["flight_rows_recovered"] = rec["rows_recovered"]
        meta["flight_rows_extractor"] = "extract_wayback_flights.py"
        meta["flight_rows_corrected_utc"] = NOW
        meta["table_state"] = rec["table_state"]
        write_json(meta_path, meta, indent=2)
    print(f"{tail:8s} {ts} {site:14s} {rec['rows_recovered']:3d} rows  "
          f"(was {rec['previously_recorded']})  {rec['table_state']}  live_today={rec['live_http_today']}")

idx = os.path.join(os.path.dirname(__file__), "../data/recovery/wayback_flight_rows.json")
if not DRY:
    json.dump({"generated_utc": NOW, "totals": totals, "captures": report},
              open(os.path.abspath(idx), "w"), indent=2)
print("\nTOTALS:", json.dumps(totals))
