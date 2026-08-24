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
| `fetch_event_windows.py` | adsb.lol + globe.airplanes.live | **Pulls the aircraft-days the speaking-event windows need.** Works out every (tail, date) inside +/- N days of every sourced Kirk/TPUSA speaking event, skips what is on disk, pulls the rest from both free archives. Records a MISS as a `.miss.json.meta.json` so "asked and got nothing" never gets confused with "never asked". `--control` runs the same dates against unrelated aircraft. |
| `airports_near.py` | local (OurAirports + Census + the recovered traces) | **Builds one `.yaml` beside every speaking-event page**: the field they probably landed at, every airport within 40 miles a private jet could also use, and every tracked tail found at any of them inside the window. Governed by `prompts/p_airports_near.md`. |
| `lib/geo.py` | OurAirports + US Census 2024 Gazetteer | Airport geometry and city geocoding. Every answer carries its distance and its method — a nearest-field label is never returned bare. |
| `lib/traces.py` | the recovered traces on disk | Turns raw ADS-B traces into airport VISITS: on-ground runs resolved to a field with the median distance attached, plus low passes reported separately. |
| `query_speaking_weeks.py` | xAI Grok `x_search` | One Grok query per calendar week, Jan 2022–Oct 2025, for Charlie Kirk / TPUSA speaking posts on X. Writes `speaking/week/{year}/week_{NN}.md`. Resume-safe. |

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
| `sweep_github_backup.py` | Asks adsb.lol's own OFF-SITE GitHub Release backup about every alleged-overlap date that both free daily archives missed. Streams each ~2 GB release through `tar` without storing it. **Releases are often SPLIT into `.tar.aa`/`.tar.ab`** — the asset list is read from the GitHub API, because asking for a single `.tar` 404s and that looks exactly like "the day is not published". |
| `write_recovered_readmes.py` | Writes the `README.md` index in each `site/docs/Planes/<TAIL>/data/recovered/` — which sources are represented, how many files and days each carries, and what that source's silence does and does not mean. |
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


## The speaking-event airport sweep, added 24 August 2026

`airports_near.py` and `fetch_event_windows.py` answer one question across all 139
sourced speaking events at once: **for each place Charlie Kirk, Erika Kirk, or TPUSA
spoke, which airports could a private jet have used, and was any tracked aircraft at one
of them within two days.**

    python3 fetch_event_windows.py --plan        # what the windows still need
    python3 fetch_event_windows.py --run         # pull it (nothing is overwritten)
    python3 airports_near.py --rebuild-traces --report

The full contract — the yaml hierarchy, what each block may and may not be read as
saying, and how to add a new location — is `{ROOT_DIR}/prompts/p_airports_near.md`.

**Three design decisions worth defending, because each one exists to stop a specific
wrong conclusion:**

* **The radius is soft.** KSLC to KPVU is 41.6 miles. At a flat 40-mile cutoff the
  23 April 2024 Salt Lake City pairing — one of only two in this repo's own data that
  survives a same-metro test — disappears by 1.6 miles. The search therefore runs to 60
  miles and reports the outer ring in a separate `just_outside_the_radius` block that is
  explicitly not a hit. A hard radius creates a cliff, and a cliff hides evidence.
* **Two archives are merged, and their disagreement is published.** The same
  aircraft-day usually comes back from both adsb.lol and airplanes.live. They are merged
  into one record carrying `cross_source_agreement`. Where the two disagree by more than
  two minutes on first contact, the file says DISAGREE and by how much. It never picks
  one.
* **Every file carries a `coverage` block.** `aircraft_days_needed` versus
  `aircraft_days_held`. An empty result with low coverage is an unasked question, not a
  negative finding, and the block is what stops the next reader treating it as one.

**What the first full run found, reported as it must be — as a fraction:** an Egyptian
SU- tail inside 40 miles and 2 days of **1 of 139** sourced speaking events (10 Sep 2025,
Orem/UVU, KPVU), plus **one near miss** in the outer ring (23 Apr 2024, Salt Lake City —
SU-BTT and SU-BND on the ground at Provo, 41.3 and 41.6 miles from KSLC, gap 0 days).
Both are Utah. That reproduces the sceptics' result off this repo's own primary data, and
it is a statement about what can currently be proven, not about what happened: 139 rows
is every Kirk/TPUSA location this repo can source and it is nowhere near every location
the Kirks were at, with exactly one row placing Erika Kirk anywhere before 10 Sep 2025.
