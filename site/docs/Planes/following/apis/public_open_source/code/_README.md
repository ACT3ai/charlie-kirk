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
