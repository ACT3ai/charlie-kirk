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

## The rule that matters more than any of this

An empty response is not a finding. **An empty response plus the date we asked plus
what the source is capable of holding** is a finding. Every script here writes all
three.
