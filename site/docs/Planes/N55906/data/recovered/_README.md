# `N55906` — recovered flight data

NOTE: the leading underscore in this filename is deliberate. Docusaurus compiles every `.md` under
`site/docs/` into a published page, and this is a data-directory index, not a page. Files and
directories beginning with `_` are excluded from the build.

Written 2026-08-24 by `write_recovered_readmes.py`. **The source is in every filename**, and every
payload has a `.meta.json` beside it recording the exact URL, the HTTP status, the byte count, the
UTC date of the data and the UTC time of the request. Nothing here is hand-edited.

**2 files across 2 sources.**

## What is in here, by source

| Source | Where it came from | Files | Days | Covers |
|---|---|---|---|---|
| `flightaware-activity-log` | flightaware.com/live/flight/IDENT | 1 | 0 | — |
| `wayback/flightaware` | web.archive.org copy of flightaware.com/live/flight/TAIL | 1 | 1 | 2010-03-04 → 2010-03-04 |

## What each source is, and what its silence means

**`flightaware-activity-log`** — FlightAware's server-rendered activity log, free and script-readable: named airports and actual off/on times. Reaches only about a WEEK back -- a current-activity source, not a recovery route.

**`wayback/flightaware`** — Same idea. Most modern FlightAware captures are JavaScript shells with no server-rendered rows in them, so they hold identity but no flight table.

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
