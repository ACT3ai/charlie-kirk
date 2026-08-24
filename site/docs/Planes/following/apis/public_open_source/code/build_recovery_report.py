#!/usr/bin/env python3
"""Turn everything the recovery runs left on disk into one auditable matrix.

Reads, in this order of authority:

  1. site/docs/Planes/<TAIL>/data/recovered/*.meta.json   -- GROUND TRUTH. A file
     is on disk or it is not. Every sidecar records which SOURCE served it, the
     HTTP status, the UTC date, and the byte count.
  2. data/recovery/recovery_index.json                    -- the three case
     windows, plus the Wayback-vs-live page probe per tracking site.
  3. data/recovery/overlap_recovery_index.json            -- every alleged
     overlap date from overlaps.csv.
  4. data/recovery/adsbx_samples_index.json               -- the monthly free
     sample archive, the only free reach back into 2022.

Writes data/recovery/fleet_recovery_matrix.json and prints the markdown tables.

WHAT THE VERDICTS MEAN, because the distinction is the whole point:

  REMOVED_FROM_PUBLIC_PAGE  The Internet Archive holds a populated copy of a
                            tracking-site page that today returns non-200 to the
                            public. This is a documented removal. It is NOT
                            evidence of intent -- owners can lawfully request
                            blocking and sites reorganise URLs.
  NEVER_ARCHIVED            No Wayback snapshot exists. Nothing can be said.
  STILL_PUBLIC              Archived then, still 200 now.
  ARCHIVE_GAP_NOT_REMOVAL   A date range absent from an ADS-B archive that is
                            absent for unrelated control aircraft too.
"""
import json, glob, os, collections, datetime, sys

CODE    = os.path.dirname(os.path.abspath(__file__))
PLANES  = os.path.abspath(os.path.join(CODE, "../../../../"))
RECDIR  = os.path.abspath(os.path.join(CODE, "../data/recovery"))

def load(name):
    p = os.path.join(RECDIR, name)
    try:
        with open(p) as f: return json.load(f)
    except Exception: return None

recovery = load("recovery_index.json") or {}
overlaps = load("overlap_recovery_index.json") or {}
samples  = load("adsbx_samples_index.json") or {}

# ---------------------------------------------------------------- ground truth
per_tail = collections.defaultdict(lambda: {
    "sources": collections.Counter(),          # source -> files on disk
    "dates": collections.defaultdict(set),     # source -> {utc_date}
    "bytes": collections.Counter(),
    "wayback": [],                             # archived page captures
})
for meta in glob.glob(os.path.join(PLANES, "*", "data", "recovered", "*.meta.json")):
    tail = meta.split(os.sep)[-4]
    try:
        with open(meta) as f: j = json.load(f)
    except Exception: continue
    src = j.get("source") or "unknown"
    t = per_tail[tail]
    t["sources"][src] += 1
    t["bytes"][src] += int(j.get("bytes") or 0)
    if j.get("utc_date"): t["dates"][src].add(j["utc_date"])
    if src.startswith("wayback/"):
        t["wayback"].append({
            "site": src.split("/", 1)[1],
            "snapshot_utc": j.get("snapshot_utc"),
            "original_url": j.get("original_url"),
            "live_http_today": j.get("live_http_today"),
            "rows": j.get("flight_rows_recovered"),
            "table_state": j.get("table_state"),
            "bytes": j.get("bytes"),
        })

# ------------------------------------------------- page probe (site-level view)
# recovery_index.json carries the per-site snapshot count AND the live probe.
# But the live probe is a SCRIPT, and three of the five sites return 403 to any
# script regardless of which aircraft is asked for. page_control_probe.json
# establishes that per site using aircraft with no connection to this case, and
# the browser capture establishes what a REAL BROWSER gets. Both are consulted
# before any 403 is allowed to be called a removal.
page_probe = collections.defaultdict(dict)
for tail, v in (recovery.get("tails") or {}).items():
    for rec in (v.get("pages") or []):
        page_probe[tail][rec["site"]] = {
            "snapshots": rec.get("snapshots", 0),
            "live_http_today": rec.get("live_http_today"),
            "first": rec.get("first"), "last": rec.get("last"),
            "captured": len(rec.get("captured") or []),
        }

control = load("page_control_probe.json") or {}
# site -> True when the site refused EVERY control aircraft, i.e. it blocks robots
blocks_scripts = {}
for site, v in (control.get("verdicts") or {}).items():
    served, total = (v.get("controls_served") or "0/0").split("/")
    blocks_scripts[site] = (int(served) == 0 and int(total) > 0)

# Browser-session evidence: tail -> {site: http}. Today only FlightRadar24 has
# been probed this way; the file format allows the others to be added.
BROWSER = os.path.abspath(os.path.join(CODE, "../../browser_capture/captures/fr24_page_availability_2026-08-24.tsv"))
browser = collections.defaultdict(dict)
try:
    for line in open(BROWSER):
        if line.startswith("#") or not line.strip(): continue
        f = line.rstrip("\n").split("\t")
        if len(f) >= 4: browser[f[0]]["flightradar24"] = {"http": int(f[1]), "rows": int(f[3])}
except FileNotFoundError:
    pass

def page_verdict(p, tail, site):
    b = browser.get(tail, {}).get(site)
    if b and b["http"] == 200:
        return "STILL_PUBLIC_BROWSER_VERIFIED"
    if not p: return "NOT_PROBED"
    if p["live_http_today"] == 200:
        return "STILL_PUBLIC"
    if blocks_scripts.get(site):
        # A non-200 from a site that refuses every control aircraft is a robot
        # block. It says nothing whatever about this aircraft.
        return "SCRIPT_BLOCKED_TELLS_US_NOTHING"
    if p["snapshots"] == 0: return "NEVER_ARCHIVED"
    return "REMOVED_FROM_PUBLIC_PAGE"

# --------------------------------------------------------------- overlap recall
ov_by_tail = collections.defaultdict(lambda: {"alleged": 0, "recovered": 0, "window_only": 0, "none": 0, "rows": []})
for r in (overlaps.get("results") or []):
    b = ov_by_tail[r["tail"]]
    b["alleged"] += 1
    if r["alleged_date_verdict"] != "NEITHER_HAS_IT": b["recovered"] += 1
    elif r.get("any_track_in_window"): b["window_only"] += 1
    else: b["none"] += 1
    b["rows"].append(r)

# ------------------------------------------------------------------- assemble
out = {
    "generated_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "what_this_is": "Per-aircraft record of which flight-data source still serves the data, "
                    "which no longer does, and what was recovered from a backup.",
    "tails": {},
}
ADSB = ["adsb-lol", "airplanes-live", "adsbexchange-samples", "adsblol-github-backup"]
SITES = ["flightradar24", "flightaware", "radarbox", "adsbexchange", "planespotters"]

for tail in sorted(set(list(per_tail) + list(page_probe) + list(ov_by_tail))):
    t = per_tail.get(tail, {"sources": collections.Counter(), "dates": {}, "bytes": collections.Counter(), "wayback": []})
    dates = t["dates"]
    rec = {
        "adsb_archives": {s: {"files": t["sources"].get(s, 0),
                              "days": len(dates.get(s, [])),
                              "earliest": min(dates[s]) if dates.get(s) else None,
                              "latest": max(dates[s]) if dates.get(s) else None} for s in ADSB},
        "tracking_site_pages": {},
        "wayback_captures": sorted(t["wayback"], key=lambda x: (x["site"], x["snapshot_utc"] or "")),
        "alleged_overlaps": {k: v for k, v in ov_by_tail.get(tail, {}).items() if k != "rows"},
    }
    for site in SITES:
        p = page_probe.get(tail, {}).get(site)
        rec["tracking_site_pages"][site] = {**(p or {}), "verdict": page_verdict(p, tail, site),
                                            "browser_http": (browser.get(tail, {}).get(site) or {}).get("http")}
    rows = sum(w["rows"] or 0 for w in t["wayback"])
    rec["flight_rows_recovered_from_archived_pages"] = rows
    removed = [s for s in SITES if rec["tracking_site_pages"][s]["verdict"] == "REMOVED_FROM_PUBLIC_PAGE"]
    rec["removed_from"] = removed
    rec["headline"] = (
        f"page removed from {', '.join(removed)}" if removed else
        "no documented page removal")
    out["tails"][tail] = rec

with open(os.path.join(RECDIR, "fleet_recovery_matrix.json"), "w") as f:
    json.dump(out, f, indent=2); f.write("\n")

# --------------------------------------------------------------- markdown out
def n(x): return "—" if not x else str(x)
print("\n## Per-aircraft recovery matrix\n")
print("| Tail | adsb.lol | airplanes.live | ADSBX samples | Archived pages held | Rows recovered | Page removals |")
print("|---|---|---|---|---|---|---|")
for tail, r in out["tails"].items():
    a = r["adsb_archives"]
    print(f"| **{tail}** | {n(a['adsb-lol']['days'])} d | {n(a['airplanes-live']['days'])} d | "
          f"{n(a['adsbexchange-samples']['days'])} d | {len(r['wayback_captures'])} | "
          f"{n(r['flight_rows_recovered_from_archived_pages'])} | "
          f"{', '.join(r['removed_from']) or '—'} |")

print("\n## Tracking-site page status, per aircraft\n")
print("| Tail | " + " | ".join(s for s in SITES) + " |")
print("|---" * (len(SITES) + 1) + "|")
SHORT = {"REMOVED_FROM_PUBLIC_PAGE": "**REMOVED**", "NEVER_ARCHIVED": "never archived",
         "STILL_PUBLIC": "public", "NOT_PROBED": "not probed",
         "STILL_PUBLIC_BROWSER_VERIFIED": "public (browser)",
         "SCRIPT_BLOCKED_TELLS_US_NOTHING": "robot-blocked"}
for tail, r in out["tails"].items():
    print(f"| **{tail}** | " + " | ".join(
        SHORT[r["tracking_site_pages"][s]["verdict"]] for s in SITES) + " |")

if ov_by_tail:
    print("\n## Alleged overlaps, by aircraft\n")
    print("| Tail | Alleged dates | Track recovered for the alleged day | Track only on a neighbouring day | No track in the window |")
    print("|---|---|---|---|---|")
    for tail, b in sorted(ov_by_tail.items()):
        print(f"| **{tail}** | {b['alleged']} | {b['recovered']} | {b['window_only']} | {b['none']} |")

print(f"\nwrote {RECDIR}/fleet_recovery_matrix.json")
