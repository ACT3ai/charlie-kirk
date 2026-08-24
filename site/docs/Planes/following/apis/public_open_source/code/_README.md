# `public_open_source/code` — runnable clients for the free sources

No dependencies. Node 18+ (global `fetch`). Run any of them straight from this
directory. Every script writes its raw response under `../data/<source>/` next to a
`.meta.json` recording the URL, the HTTP status, the byte count and the UTC time of
the request — because a claim about what an API returned is worth nothing without
the response and the timestamp.

**Nothing here overwrites a previous pull.** A second pull of the same endpoint is
written alongside the first with a `.pulled-<timestamp>` suffix. The diff between
two pulls is how we show that something that used to be retrievable no longer is.

| script | source | what it gets |
|---|---|---|
| `globe_history.js` | adsb.lol globe history | **HISTORICAL ADS-B traces.** The only free, no-account historical source we found. |
| `pull_all.js` | adsb.lol globe history | Bulk: every claimed (tail, date) from the spine CSVs, into each aircraft and overlap directory, plus `MISSING_DATA.md` for every gap. |
| `adsbdb.js` | adsbdb.com | Tail → ICAO hex, type, registered owner. No history. |
| `live_networks.js` | adsb.lol, adsb.fi, airplanes.live | Live positions, side by side. Records that airplanes.live is now gated. |
| `opensky.js` | OpenSky Network | Historical flight list. **Needs OAuth2 credentials since March 2026.** |
| `wayback.js` | Internet Archive CDX | Snapshot history of the tracking pages — the scrubbing detector. |
| `ourairports.js` | OurAirports (CC0) | Public-domain airport and runway reference data. |

## The recovery harness

Added when this investigation took the claim "the flight records were erased"
seriously and went looking. Run in this order.

| script | what it does |
|---|---|
| `recover_erased.js` | The main sweep. For every tail and the three case date-windows, pulls **globe.airplanes.live** and **adsb.lol** side by side and diffs them, then walks the Internet Archive CDX for five tracking-site pages and probes what each URL returns to the public today. Writes `../data/recovery/recovery_index.json`. |
| `recover_overlaps.js` | The other list: every alleged `(tail, date)` in `following/overlaps.csv`, on the alleged day and the UTC day either side. 69 pairs. Writes `../data/recovery/overlap_recovery_index.json`. |
| `analyse_overlap_recovery.js` | Turns those pulls into the only question that matters — where does the recovered track actually put the aircraft on the day the sheet alleges it was in that American city. Nearest-airport label with the distance attached. Writes `overlap_recovery_analysis.json`. |
| `recover_adsbx_samples.js` | The free ADSBX monthly sample archive: one whole day per month, back to July 2016. **The only free route into 2022.** |
| `ingest_github_backup.js` | Ingests traces out of an adsb.lol GitHub Release tarball — the off-site backup of adsb.lol's own archive. |
| `flightaware_activity.js` | A fifth free route. FlightAware serves scripts (200) and ships its activity log server-rendered in `trackpollBootstrap` — named airports and actual off/on times, no key. **Reaches about one week back**, so it is a CURRENT-activity source, not a recovery route. |
| `control_page_probe.js` | **RUN THIS BEFORE CALLING ANY 403 A REMOVAL.** Asks the same five tracking sites about five aircraft with nothing to do with this case. Writes `../data/recovery/page_control_probe.json`. |
| `extract_wayback_flights.py` | Re-parses the archived tracking-site HTML into flight rows properly, superseding the inline parse in `recover_erased.js`. |
| `build_recovery_report.py` | Assembles everything on disk into `../data/recovery/fleet_recovery_matrix.json` and prints the per-aircraft markdown tables the site publishes. |

### What the harness found, so the next person does not repeat the mistake

`control_page_probe.js` exists because this investigation published that N102DZ's
FlightRadar24 page had been **removed**, on the strength of an HTTP 403. It had not.
**FlightRadar24, RadarBox and Planespotters return 403 to any scripted request** —
five unrelated control aircraft got the identical 403. Opened in a real browser,
**every one of the sixteen aircraft here loads HTTP 200** with a full identity block.
The empty flight table is FlightRadar24's seven-day free tier, which behaves the same
way for an unrelated Gulfstream that has not flown this week.

The browser half cannot be scripted — that is the whole point — so it is recorded as a
capture at `../../browser_capture/captures/fr24_page_availability_2026-08-24.tsv`.

**No aircraft page in this investigation has been found removed from any tracking site.**

## Optional command-line tools

Installed and used here:

    brew install duckdb      # query the spine CSVs and the FAA registry in place
    brew install monolith    # freeze a whole tracking page into one self-contained file

Useful, not required:

    brew install readsb dump1090-fa    # ADS-B decoders. Only do anything with an SDR
                                       # receiver attached — they decode 1090 MHz off
                                       # the air, they do not query anyone's API.
    pipx install waybackpy             # CLI wrapper over the same CDX endpoints
                                       # wayback.js already calls. macOS Python is
                                       # PEP 668 managed — plain `pip3 install` is
                                       # refused, use pipx or a venv.


## Scripts added on 24 August 2026, and the mistakes that produced them

Four scripts joined this directory in one run, and three of them exist because an
earlier run of this pass got something wrong. That is worth stating in the README
rather than in a commit message nobody reads.

### `extract_wayback_flights.py` — because "0 rows" was a parser bug

`recover_erased.js` pulled 42 archived tracking-site pages and wrote
`flight_rows_recovered: 0` (Flightradar24) or `null` (FlightAware) into every one of
their sidecars. **Both numbers were wrong.** The FR24 parser matched a row shape those
pages do not use; the FlightAware captures were never parsed at all. **153 flight legs
were on disk the whole time** — 44 from FR24, 109 from FlightAware.

A zero in a provenance record reads as an absence of evidence. Here it was an absence
of parsing. The rewritten extractor now distinguishes three states that had all been
collapsed into "0":

    POPULATED                                 rows were found
    PRESENT_BUT_EMPTY                         the table is there and has no rows
    JAVASCRIPT_SHELL_NO_SERVER_RENDERED_ROWS  the page is a client-side app; the
                                              archived HTML is ~458 KB of chrome

    python3 extract_wayback_flights.py --dry-run   # report, write nothing
    python3 extract_wayback_flights.py             # rewrite the sidecars

### `lib/airports.js` — resolve a position to a named field

Loads the CC0 OurAirports gazetteer from `../data/ourairports/airports.csv`.
`nearest(lat,lon)`, `label(lat,lon)` and `byCode(icaoOrIata)`.

**This is geometry, not a landing record**, and the library is built to keep saying so:
every label it returns carries its distance in km. A fix 0.2 km from a runway with the
on-ground flag set is as good as this method gets. A fix 14 km away names the closest
field and nothing more. The Provo-versus-Dugway mislabel this investigation already had
to correct is what happens when a nearest-field label is read as a destination.

### `verify_overlaps.js` — test every claimed overlap against position data

Reads `following/overlaps.csv` and, for each of the 85 rows, queries both free archives
for the claimed tail on the claimed date and the day either side, then measures the
aircraft's **closest approach in kilometres** to the claimed field.

Two things in it are worth copying into any similar tool:

**The control basket.** Before any absence is reported, the same date is asked of nine
airframes with nothing to do with this case. If one of them has a track, the archive
holds that date and a missing case aircraft is a genuine absence. If none does, the
archive does not cover the date and the absence says nothing at all. That is the
difference between "the record does not show it" and "we cannot see the record", and
every NOT_HEARD verdict this script emits is backed by it.

**Distance, not identifier matching.** The first version compared ICAO strings and
scored a real arrival at Lincoln as "elsewhere", because the nearest gazetteer entry to
the landing rollout was a private strip next door. It also scored a confirmed St Louis
arrival as "elsewhere" because the source row names three fields in one cell
(`KSTL/KCPS/KSUS`) and the matcher compared that whole string as one identifier. Both
were false refutations, and both were found by reading the output rather than trusting
the verdict.

    node verify_overlaps.js                 # all 85 rows
    node verify_overlaps.js --id OWENS-041
    node verify_overlaps.js --limit 5

### `build_tail_provenance.js` — the per-aircraft ledger

Walks every `.meta.json` under `Planes/*/data/` and answers, per tail: which archives
hold it and over what span, which days only one archive has, which days both have,
where the aircraft actually was, and which tracking-site pages were archived versus
what they serve today. Writes `../data/provenance/tail_provenance.json`, which is what
the aircraft pages' provenance sections are built from.

    node build_tail_provenance.js

### And one fix in `wayback.js`

The CDX queries used `collapse=digest`, which returns only distinct-content captures.
Every count it produced was a floor rather than a total, and — worse — it made the
"did this page stop changing?" test impossible by construction, since adjacent identical
digests are exactly what it throws away. The endpoint also answers **HTTP 504** under
load with an HTML error body, and three of those were logged as `"snapshots": 0`. One of
them was SU-BTT's, the most load-bearing aircraft in the case, which in fact has three
snapshots.

**A failed query is UNKNOWN, not zero.** The function now drops the collapse, retries
with backoff, and says so in the sidecar when it still fails.

## The rule that matters more than any of this

An empty response is not a finding. **An empty response plus the date we asked plus
what the source is capable of holding** is a finding. Every script here writes all
three.
