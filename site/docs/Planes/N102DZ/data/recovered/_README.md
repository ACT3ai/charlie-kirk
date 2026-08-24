# `N102DZ` — recovered flight data

NOTE: the leading underscore in this filename is deliberate. Docusaurus compiles every `.md` under
`site/docs/` into a published page, and this is a data-directory index, not a page. Files and
directories beginning with `_` are excluded from the build.

Written 2026-08-24 by `write_recovered_readmes.py`. **The source is in every filename**, and every
payload has a `.meta.json` beside it recording the exact URL, the HTTP status, the byte count, the
UTC date of the data and the UTC time of the request. Nothing here is hand-edited.

**85 files across 7 sources.**

## What is in here, by source

| Source | Where it came from | Files | Days | Covers |
|---|---|---|---|---|
| `adsb-lol` | adsb.lol/globe_history | 12 | 12 | 2025-09-01 → 2025-10-09 |
| `adsbexchange-samples` | samples.adsbexchange.com | 18 | 18 | 2022-05-01 → 2026-06-01 |
| `adsblol-github-backup` | github.com/adsblol/globe_history_YYYY releases | 1 | 1 | 2025-10-13 → 2025-10-13 |
| `airplanes-live` | globe.airplanes.live/globe_history | 50 | 50 | 2025-09-01 → 2026-06-05 |
| `flightaware-activity-log` | flightaware.com/live/flight/IDENT | 1 | 0 | — |
| `wayback/flightaware` | web.archive.org copy of flightaware.com/live/flight/TAIL | 1 | 1 | 2026-01-14 → 2026-01-14 |
| `wayback/flightradar24` | web.archive.org copy of flightradar24.com/data/aircraft/TAIL | 2 | 2 | 2022-05-26 → 2025-09-11 |

## What each source is, and what its silence means

**`adsb-lol`** — The archive this investigation originally relied on. Free, no account, 2023 to today. Returns 403 for a band of late-2025 dates and 404 for 2026 -- for EVERY aircraft, including unrelated controls. That is retention and serving policy, not suppression.

**`adsbexchange-samples`** — ADS-B Exchange's FREE sample archive: one complete day per month, the 1st only, back to July 2016. The ONLY free route into 2022. One day in thirty -- it can never test a claim about the 13th of anything.

**`adsblol-github-backup`** — adsb.lol's own OFF-SITE backup: one ~2 GB release per day under the Open Database Licence, often SPLIT into .tar.aa/.tar.ab. Same organisation as the live API, so a hit is not independent corroboration -- but a miss closes the last free door.

**`airplanes-live`** — Independent volunteer ADS-B network, free, no account. Reaches 2023 to today. Typically 5-10x the byte count of adsb.lol for the same aircraft-day.

**`flightaware-activity-log`** — FlightAware's server-rendered activity log, free and script-readable: named airports and actual off/on times. Reaches only about a WEEK back -- a current-activity source, not a recovery route.

**`wayback/flightaware`** — Same idea. Most modern FlightAware captures are JavaScript shells with no server-rendered rows in them, so they hold identity but no flight table.

**`wayback/flightradar24`** — What the tracking SITE said, as opposed to what the sensors heard. The only route that could document a page removal. Sparse: it depends on a crawler having visited.

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
