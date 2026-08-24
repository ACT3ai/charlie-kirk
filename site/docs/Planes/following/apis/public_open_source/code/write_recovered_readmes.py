#!/usr/bin/env python3
"""One _README.md per aircraft's data/recovered/ directory.

The point of that directory is that THE SOURCE IS IN EVERY FILENAME, so a reader
can tell where a payload came from without opening anything. This writes the index
that says so: which sources are represented, how many files and days each one
carries, what date range it covers, and what a 404 from that source does and does
not mean.

    python3 write_recovered_readmes.py
"""
import os, json, glob, collections, datetime

CODE   = os.path.dirname(os.path.abspath(__file__))
PLANES = os.path.abspath(os.path.join(CODE, "../../../../"))
NOW    = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")

SOURCES = {
    "airplanes-live": ("globe.airplanes.live/globe_history",
        "Independent volunteer ADS-B network, free, no account. Reaches 2023 to today. "
        "Typically 5-10x the byte count of adsb.lol for the same aircraft-day."),
    "adsb-lol": ("adsb.lol/globe_history",
        "The archive this investigation originally relied on. Free, no account, 2023 to today. "
        "Returns 403 for a band of late-2025 dates and 404 for 2026 -- for EVERY aircraft, "
        "including unrelated controls. That is retention and serving policy, not suppression."),
    "adsbexchange-samples": ("samples.adsbexchange.com",
        "ADS-B Exchange's FREE sample archive: one complete day per month, the 1st only, back to "
        "July 2016. The ONLY free route into 2022. One day in thirty -- it can never test a claim "
        "about the 13th of anything."),
    "adsblol-github-backup": ("github.com/adsblol/globe_history_YYYY releases",
        "adsb.lol's own OFF-SITE backup: one ~2 GB release per day under the Open Database Licence, "
        "often SPLIT into .tar.aa/.tar.ab. Same organisation as the live API, so a hit is not "
        "independent corroboration -- but a miss closes the last free door."),
    "flightaware-activity-log": ("flightaware.com/live/flight/IDENT",
        "FlightAware's server-rendered activity log, free and script-readable: named airports and "
        "actual off/on times. Reaches only about a WEEK back -- a current-activity source, not a "
        "recovery route."),
    "wayback/flightradar24": ("web.archive.org copy of flightradar24.com/data/aircraft/TAIL",
        "What the tracking SITE said, as opposed to what the sensors heard. The only route that "
        "could document a page removal. Sparse: it depends on a crawler having visited."),
    "wayback/flightaware": ("web.archive.org copy of flightaware.com/live/flight/TAIL",
        "Same idea. Most modern FlightAware captures are JavaScript shells with no server-rendered "
        "rows in them, so they hold identity but no flight table."),
    "wayback/radarbox": ("web.archive.org copy of radarbox.com", "Page archive."),
    "wayback/adsbexchange": ("web.archive.org copy of globe.adsbexchange.com", "Page archive."),
    "wayback/planespotters": ("web.archive.org copy of planespotters.net", "Page archive."),
}

HEADER = """# `{tail}` — recovered flight data

NOTE: the leading underscore in this filename is deliberate. Docusaurus compiles every `.md` under
`site/docs/` into a published page, and this is a data-directory index, not a page. Files and
directories beginning with `_` are excluded from the build.

Written {now} by `write_recovered_readmes.py`. **The source is in every filename**, and every
payload has a `.meta.json` beside it recording the exact URL, the HTTP status, the byte count, the
UTC date of the data and the UTC time of the request. Nothing here is hand-edited.

**{files} files across {nsrc} sources.**

## What is in here, by source

| Source | Where it came from | Files | Days | Covers |
|---|---|---|---|---|
{rows}

## What each source is, and what its silence means

{blurbs}

## The rule that governs reading any of this

**An absent day is an absent day.** A 404 means the volunteer network heard nothing from that
aircraft on that date. It does **not** mean the aircraft did not fly, and it does **not** mean a
transponder was switched off. The ordinary explanations come first every time: parked and silent,
outside receiver coverage, or a claimed date that was simply wrong.

**Both free daily archives begin in 2023.** Every 2022 date is untestable by construction, and no
404 from 2022 should ever be read as a removal.

**No aircraft page in this investigation was found removed from any tracking site.** The HTTP 403s
recorded from FlightRadar24, RadarBox and Planespotters are robot blocks that hit unrelated control
aircraft identically — see `/Planes/Flight-Data-Recovery/What-A-403-Means`.

Method, tooling and the fleet-wide matrix: `/Planes/Flight-Data-Recovery/overview`.
"""

made = 0
for d in sorted(glob.glob(os.path.join(PLANES, "*", "data", "recovered"))):
    tail = d.split(os.sep)[-3]
    per = collections.defaultdict(lambda: {"files": 0, "dates": set()})
    for meta in glob.glob(os.path.join(d, "*.meta.json")):
        try:
            with open(meta) as f: j = json.load(f)
        except Exception: continue
        src = j.get("source") or "unknown"
        per[src]["files"] += 1
        dt = j.get("utc_date") or (j.get("snapshot_utc") or "")[:8]
        if dt:
            per[src]["dates"].add(dt if "-" in dt else f"{dt[:4]}-{dt[4:6]}-{dt[6:8]}")
    if not per: continue

    rows, blurbs = [], []
    for src in sorted(per):
        where, why = SOURCES.get(src, (src, "Source not described in write_recovered_readmes.py."))
        ds = sorted(per[src]["dates"])
        covers = f"{ds[0]} → {ds[-1]}" if ds else "—"
        rows.append(f"| `{src}` | {where} | {per[src]['files']} | {len(ds)} | {covers} |")
        blurbs.append(f"**`{src}`** — {why}")
    body = HEADER.format(tail=tail, now=NOW, files=sum(v["files"] for v in per.values()),
                         nsrc=len(per), rows="\n".join(rows), blurbs="\n\n".join(blurbs))
    with open(os.path.join(d, "_README.md"), "w") as f:
        f.write(body)
    made += 1
    print(f"  {tail:<8} {sum(v['files'] for v in per.values()):>4} files, {len(per)} sources")
print(f"\nwrote {made} READMEs")
