# `Planes/following/apis/` — How We Actually Go And Get The Flight Data

    ROOT_DIR dir is ~/BGit/Bryan_git/charlie-kirk/
    SITE_DOCS dir is {ROOT_DIR}site/docs/
    SITE_PLANES dir is {SITE_DOCS}Planes/
    FOLLOWING_DIR dir is {SITE_PLANES}following/
    THIS_DIR dir is {FOLLOWING_DIR}apis/          ← this directory
    OVERLAP_DIR dir is {FOLLOWING_DIR}overlap/
    PAGES_CSV is file {ROOT_DIR}pages.csv
    CK_FILE is file {ROOT_DIR}Charlie_Kirk.txt    ← READ-ONLY TO AI. NEVER WRITE.
    CK_INBOX is file {ROOT_DIR}Charlie_Kirk_AI_Inbox.txt
    ASSESS_MANUAL is file {ROOT_DIR}prompts/Assess_Manual.md
    FLIGHTS_CSV is file {FOLLOWING_DIR}flights.csv
    OVERLAPS_CSV is file {FOLLOWING_DIR}overlaps.csv
    PLANES_CSV is file {FOLLOWING_DIR}planes.csv
    AIRPORTS_CSV is file {FOLLOWING_DIR}airports.csv
    SOURCES_CSV is file {FOLLOWING_DIR}sources.csv

Read `{FOLLOWING_DIR}CLAUDE.md` in full before doing anything in here. Everything it says about
public content, attribution, counterarguments, the counts being trackers' tallies, and never
merging the four separate aircraft threads applies to every page in this directory too.

## Why this directory exists

The whole following-planes claim rests on **third-hand readings of flight-tracking websites**.
Somebody screenshotted a Flightradar24 aircraft-history table, somebody else typed the rows into a
spreadsheet, a third person tallied the spreadsheet, and a fourth person put a number on television.
Every step of that chain is a place the data could have been misread — and the published audits say
it *was* misread, at a rate of roughly two rows in three.

**This directory replaces that chain with primary data pulled by us, from named sources, with the
raw response saved to disk.** When we say an aircraft was at a field on a date, we want to be able to
point at the JSON we got back and the timestamp we got it.

It exists for a second reason that matters just as much: **some of this data is no longer
available.** Free-tier history windows roll off. Aircraft get added to blocking programmes. Sites
change their terms. When a record we could once see is gone, **the disappearance is itself a
finding**, and we want it captured — with a screenshot, a date, and a Wayback comparison — rather
than quietly lost.

## The two things that are true at once

* **ALL INFO WE CAN MAKE PUBLIC, WE WANT PUBLIC.** The `knowledge.mdx` pages here are deliberately
  public. A reader who does not believe us should be able to repeat every pull we made, with the
  same free tools, and get the same answer. That is the point.
* **Nothing published here may assert what the data does not show.** An empty API response means
  the API had nothing, not that the aircraft was hidden. Say which.

## The passes

The work is organised as **passes**, not as one job. Each pass is a different way of getting at the
same underlying question — which aircraft, at which field, on which date — and each pass has its own
subdirectory, its own knowledge page, its own prompt file, and its own code.

    PASS 1  public_open_source/   Free and open APIs. Community ADS-B networks, open aviation
                                  datasets, the Internet Archive. No money, no contract, no NDA.
                                  ALWAYS RUN THIS PASS FIRST. It is repeatable by any reader.

    PASS 2  proprietary/          Commercial APIs. Flightradar24, FlightAware, ADS-B Exchange via
                                  RapidBAPI, RadarBox, Cirium. These hold the deep history the free
                                  networks do not. They cost money and their terms restrict
                                  redistribution — READ THE TERMS SECTION before publishing a byte.

    PASS 3  government/           Government and public-record sources. FAA registries and airport
                                  data, operations counts, and the records-request routes: federal
                                  FOIA, and state public-records law at the city- and
                                  authority-owned airports in this case. THIS IS THE PASS THAT
                                  PRODUCES RECORDS RATHER THAN READINGS, and a record outranks
                                  every reading.

    PASS 4  browser_capture/      Claude Code driving a real browser at the tracking websites.
                                  Screenshots, page text, and network captures of what the public
                                  map actually showed on the day we looked. This is how we
                                  DOCUMENT THAT DATA IS GONE — and how we capture sites that have
                                  no API at all.

A pass is never "instead of" another pass. **The same claim checked four ways, agreeing, is the
strongest thing this investigation can produce. The same claim checked four ways and disagreeing is
the second strongest, and it gets published too.**

## Directory layout — the same shape in every pass

    {THIS_DIR}
      CLAUDE.md                 this file
      overview.mdx              PUBLIC index page for the whole API effort
      _category_.json
      public_open_source/
        knowledge.mdx           PUBLIC. The knowledge of these sites.
        p_get_data.mdx          PRIVATE prompt. Docusaurus excludes **/p_*.{md,mdx}.
        code/                   runnable clients. _README.md, not README.md (see below).
        data/                   raw responses land here, one subdirectory per source
      proprietary/              same four
      government/               same four
      browser_capture/          same four, plus captures/

### What `knowledge.mdx` must answer

It is the knowledge of those sites, and it answers exactly four questions, in this order:

1. **What APIs do they have?** Every endpoint we care about, named, with what it returns and what
   its history window is.
2. **How do you use them?** Auth, rate limits, the exact call, and the gotchas. Written so a reader
   with a terminal can do it.
3. **What did we get so far?** The pulls we actually made, when we made them, and where the raw
   response is saved in this repo.
4. **What did we NOT get?** The holes. Blocked tails, expired windows, paywalls, empty responses,
   and — separately — **data that used to be there and is not any more.**

Question 4 is not the apology section. It is the most valuable section on the page.

### What `p_get_data.mdx` is

The prompt file that drives the pass. Repo prompt style: plain text, asterisk bullets never dashes,
`====` dividers not markdown headers, `ROOT_DIR` defined first, every other path referenced through
`{VARIABLE}` braces. It lives inside `site/docs/` but **is never published** — the docs plugin in
`site/docusaurus.config.ts` excludes `**/p_*.{md,mdx}`, `**/prompts/**` and `**/CLAUDE.md`.

Because MDX would try to evaluate `{VARIABLE}` as JavaScript, the prompt body is wrapped in a fenced
code block. That keeps the file safe even if the exclude rule is ever removed.

### Why `_README.md` and not `README.md` inside `code/`

Anything ending `.md` or `.mdx` under `site/docs/` becomes a page. A leading underscore is the
Docusaurus default exclude (`**/_*.{js,jsx,ts,tsx,md,mdx}`), so `code/_README.md` is documentation
for the code without becoming a public page.

## Where the data lands

Raw responses go under the pass that produced them:

    {THIS_DIR}<pass>/data/<source>/<tail>/<YYYY-MM-DD>_<endpoint>.json

One file per pull. **Never overwrite a previous pull** — the diff between two pulls of the same
endpoint on two different dates is the evidence of scrubbing. Alongside each pull, the fetcher
writes a `.meta.json` recording the URL, the HTTP status, the byte count, and the UTC time of the
request.

Findings extracted from those pulls are promoted into the five spine CSVs in `{FOLLOWING_DIR}` —
`flights.csv`, `overlaps.csv`, `planes.csv`, `airports.csv`, `sources.csv` — and only then onto a
page. **Research first, publication second.** A new source gets a row in `{SOURCES_CSV}` with its
`evidence_class` before anything it says appears on a page.

`evidence_class` ranking, from `{FOLLOWING_DIR}CLAUDE.md`, and the reason this directory exists:

    adsb_public_history > facility_record > broadcast_video_frame > subject_denial
      > broadcast_claim > press_relay > social_post_unverified > document_quoting_claim

Everything this directory pulls is `adsb_public_history` or `facility_record` — **the top two
tiers.** Everything the claim currently rests on is in the bottom three.

## The one-page-per-thing rule, and the directories that now exist

Every plane, every layover location, and every claimed overlap **is a directory**, not a file. The
main page is `overview.mdx` inside it, so the directory has room to hold that item's own pulled
data, screenshots, and notes next to its page.

    {SITE_PLANES}SU-BTT/overview.mdx                      one directory per aircraft
    {FOLLOWING_DIR}Provo_KPVU_2024-04-19_to_2025-09-13/overview.mdx   one per location + date range
    {OVERLAP_DIR}20250910_UT_orem/overview.mdx            one per claimed overlap

Each carries a `_category_.json` linking to its `overview`. **The old flat URLs still resolve** —
`createRedirects` in `site/docusaurus.config.ts` maps every `/x/overview` back from `/x`, so
`/Planes/SU-BTT` redirects to `/Planes/SU-BTT/overview` without a new redirect entry.

**These directory names are stable IDs. Never rename one.** They are the join key between
`{PAGES_CSV}`, the `site_page` / `mdx_page` / `overlap_page` columns of the spine CSVs, and every
inbound link on the site.

When a pull produces something about one specific aircraft, location, or overlap, **the extract
belongs in that item's directory** and the raw response stays under the pass's `data/`.

## Sourcing and the terms of use

* **Public open source data may be republished.** Say which network, which endpoint, which date.
* **Commercial API responses generally may NOT be republished verbatim.** Most terms allow you to
  use the data and state a conclusion; they do not allow you to mirror the feed. Publish the
  finding and the citation, not the payload. The payload stays in `data/` for our own audit trail.
  Where a licence is unclear, treat it as restrictive and say on the page that the underlying
  response is held but not published.
* **Government data is public domain** and may be republished in full. Records obtained by FOIA or
  a state public-records request may be published as received, and should be — including the
  request letter, the tracking number, and the agency's response, refusal, or silence.
* **Screenshots of a third-party site** are captured for evidentiary purposes. Always record the URL
  and the UTC capture time in the image's page text.

## Rules inherited, and not negotiable here

* Every disputed claim is **ALLEGED** and presented as a reported claim.
* **The counts are trackers' tallies, not records.** 73, 72, 70+, 68, 29, 23. Show the conflict;
  never average it.
* **One overlap is not evidence. The pattern is the claim.**
* **Every page carries its counterargument.** Including these pages: the counterargument to an
  empty API result is that the aircraft simply was not there.
* **ADS-B has holes and the holes cut both ways.** Absence of a track is not proof of a covert leg.
* **Do not merge the threads.** The 18-month following pattern, the Sept 10 day-of timeline, the
  N1098L drone thread, and the N888KG Wendover departure are four different claims.
* **Erika's side is the weak side** — her logs are reported erased. Say so on every Erika pairing.
* Never assert who tasked an aircraft. Never name a living person as the accused. Aircraft owners,
  crew, passengers and ground staff stay unnamed except where already publicly on the record.
* Images are tracked in git and embedded by local repo path, never by an IPFS gateway URL. Never
  `127.0.0.1` or `localhost` for an IPFS URL. Check the ban CSVs before embedding anything.
* Keep every `<div>` and `</div>` at column 0 in MDX. An indented closing tag breaks the build and
  only `npm run build` catches it.
* Build before declaring done: `cd {ROOT_DIR}site && npm run build`.
* Keep `{PAGES_CSV}` in sync for every page created, moved, or deleted here.

## What may be written from here

1. Files inside `{THIS_DIR}`.
2. Extract files inside the specific plane / location / overlap directory a pull is about.
3. Rows in the five spine CSVs in `{FOLLOWING_DIR}`.
4. The matching rows in `{PAGES_CSV}`.

Everything else — `{CK_FILE}` above all — is read-only source material. New material for the master
file goes to `{CK_INBOX}` and a human merges it.

## The source register — every site, API and dataset found, with its status

Checked **24 August 2026**. Anything here without a date beside it is untrustworthy six months from
now; re-check and re-date rather than assuming.

### Pass 1 — free and open

| Source | Endpoint | History? | Auth | Status |
|---|---|---|---|---|
| **adsb.lol globe history** | `adsb.lol/globe_history/YYYY/MM/DD/traces/hh/trace_full_HEX.json` | **YES** | none | **200 — the workhorse.** Gzip JSON, self-identifies `r`/`t`. Coverage seen: 2023-02-24 → 2025-10-11, then a 403 band, then normal again by 2025-12-31. |
| adsb.lol v2 | `api.adsb.lol/v2/hex/HEX`, `/v2/reg/REG` | live only | none | 200; empty array when not airborne |
| adsb.fi | `opendata.adsb.fi/api/v2/hex/HEX` | live only | none | 200; same empty-means-parked trap |
| airplanes.live | `api.airplanes.live/v2/reg/REG` | live only | **gated** | **403** — asks you to email first. Was open before. |
| OpenSky | `opensky-network.org/api/flights/aircraft` | yes | **OAuth2** | **403 anonymous.** Basic auth removed 18 Mar 2026. Credits: 400 anon / 4,000 registered / 8,000 feeders. |
| OpenSky | `/api/states/all` | live only | optional | 200 |
| adsbdb | `api.adsbdb.com/v0/aircraft/REG`, `/v0/callsign/CS` | metadata only | none | 200. Tail → hex, type, owner. **Its SU-BTT hex disagrees with the trace.** |
| OurAirports | `davidmegginson.github.io/ourairports-data/airports.csv`, `runways.csv` | reference | none | 200, CC0 |
| Internet Archive | `web.archive.org/cdx/search/cdx` | snapshots | none | 200 |

### Pass 2 — commercial

| Vendor | Endpoint | History | Credential | Status |
|---|---|---|---|---|
| Flightradar24 | `fr24api.flightradar24.com/api/flight-summary/full` | deep | `FR24_API_TOKEN` | **not held** |
| FlightAware AeroAPI v4 | `aeroapi.flightaware.com/aeroapi/aircraft/REG/flights` | **to 2011** | `AEROAPI_KEY` | **not held — highest value unopened door** |
| ADS-B Exchange | RapidAPI + `globe_history` | deep | `ADSBX_RAPIDAPI_KEY` | **403 to the public.** Several original screenshots came from here while it was open. |
| RadarBox, Cirium, OAG, Spire | — | — | — | not investigated |

**Where those credentials live.** Not in this repo, and not in any file under it. Every client
resolves its credential through `public_open_source/code/lib/credentials.js`, which reads the
environment first and then `~/.credentials/charlie_kirk.json` — mode `600`, outside every git repo,
one key per vendor under `charlie_kirk.flight_apis`. `CK_CREDENTIALS_FILE` overrides the path.
The loader warns if the file is group- or world-readable, and a missing credential is reported by
NAME only; no script ever prints a value. **Never paste a key into a script, a page, a prompt file,
a CSV, or a commit — put it in the store and let the loader find it.**

### Pass 3 — government and public records

| Source | What it is | Access | Status |
|---|---|---|---|
| **FAA Releasable Aircraft Database** | `registry.faa.gov/database/ReleasableAircraft.zip` — daily, ~70 MB, `MASTER.txt` + `ACFTREF.txt` | free download, **public domain** | **200. Pulled. All 10 tracked N-tails extracted.** |
| FAA aircraft inquiry | `registry.faa.gov/aircraftinquiry` | web lookup | single-record UI, use the bulk file instead |
| FAA airport / facility data | NFDC airport and facility subscription files | free download | **not pulled yet** |
| FAA operations counts | agency operations and delay reporting systems | free, web UI | **not pulled yet** — could show foreign itinerant operations by field |
| Federal air traffic agency | flight strips, radar, recordings | **FOIA** | **no request filed** |
| Federal border agency | customs processing of international arrivals | **FOIA** | **no request filed.** Note: 2025 Provo arrivals cleared customs at the northern entry field, not at Provo. |
| Federal foreign-affairs department | diplomatic clearance for foreign state aircraft | **FOIA** | **no request filed** |
| **The airports themselves** | landing fees, fuel tickets, ramp assignment, hangar, **badge access** | **STATE public-records law** | **no request filed. This is the most under-used route in the whole investigation.** Most fields here are city-owned or run by a public airport authority, which makes state law — not federal FOIA — the route, and it is faster and cheaper. |
| Egyptian civil aviation registry | — | — | **no public equivalent exists.** The five SU- tails at the centre of the claim cannot be resolved by any free government download. |

### Pass 4 — sites to capture

`browser_capture/code/targets.json` — 128 targets across 8 sites and 16 aircraft: Flightradar24,
ADS-B Exchange, FlightAware, RadarBox, Planespotters, JetPhotos, adsb.lol globe, airplanes.live globe.

### Installed command-line tools

    brew install duckdb      # query the spine CSVs and the FAA registry in place
    brew install monolith    # freeze a tracking page into one self-contained file

Available and not required: `readsb`, `dump1090-fa` (decode 1090 MHz off the air — they need an SDR
receiver and query nobody's API), `pipx install waybackpy` (CLI over the same CDX endpoints
`wayback.js` already calls; macOS Python is PEP 668 managed so plain `pip3 install` is refused).

### Standing findings that must not be misreported

* **Free ADS-B networks are live-only except adsb.lol globe history.** An empty result means NOT
  AIRBORNE NOW. It is not an absence from history and it is not evidence of suppression.
* **The adsb.lol archive returns 403 for roughly 12 Oct – 15 Dec 2025 for EVERY aircraft**, including
  ones with no connection to this case. **Archive-wide condition, not suppression.** It happens to
  cover the claimed Sharm el-Sheikh dates. Never report it as scrubbing.
* **The archive does not reach 2022.** Earliest trace obtained anywhere: 2023-02-24. Every 2022 claim
  on this site rests on a screenshot, not on data we hold.
* **FAA registrant names differ from community-database owner strings** for most N-tails. The FAA is
  the record; a community database may carry a former owner, an operator, or a management company.
  Name the FAA one and give the retrieval date.
* **A registrant is often a holding LLC. A holding company is not a person, and we do not go behind
  one to name private individuals.**
