# The Data Gap Ledger — what we HELD, what we ASKED and got nothing, and what we NEVER ASKED

Snapshot taken **2026-08-26 17:34 UTC**, by walking every
`site/docs/Planes/<TAIL>/data/recovered/` directory for the 15 case tails plus the two
control airframes, and reconciling that against the 139 speaking-event `.yaml` coverage
blocks and `_airports_near_summary.csv`.

**The disk is a moving target while you read this.** A `--side following --window 7`
fetch was running during the walk (see §4), so `.miss.json.meta.json` files were being
written as the directories were listed. Every number below is as of the timestamp above.

Files written:

* `gap_ledger.csv` — per tail, per year, the three states plus side and fleet totals (88 rows)
* `gap_ledger_by_event.csv` — per speaking event, all 139, with a testability verdict (139 rows)

---

## 0. The three states, and why they must never be merged

| State | On disk | What it licenses you to say |
|---|---|---|
| **HELD** | `<TAIL>_<DATE>_<source>_trace_full.json[.gz]` | A volunteer receiver network heard this aircraft that day. Positions are real. |
| **ASKED_AND_EMPTY** | `<TAIL>_<DATE>_<source>_trace_full.miss.json.meta.json` | Both free archives were asked and hold nothing. This is a **coverage fact**, not a location fact. Transponder off, outside receiver coverage, and genuinely not flying are indistinguishable from here. |
| **NEVER_ASKED** | neither file exists | **Nothing.** An open question. A finding of "no plane was near this event" built on these days is worth zero. |

An aircraft-day is counted HELD if **either** archive returned a payload; ASKED_AND_EMPTY
only if every source that was asked came back empty.

---

## 1. The ledger

### 1a. Fleet totals — restricted to the aircraft-days the 139 event windows actually need

Denominator = distinct (tail, date) pairs inside the ±2-day event windows, deduplicated
across overlapping windows.

| Side | Tails | Aircraft-days needed | HELD | ASKED_AND_EMPTY | NEVER_ASKED | Coverage | Queried |
|---|---:|---:|---:|---:|---:|---:|---:|
| **following** (SU-BGM/BND/BTT/BTU/BTV, T7-ELL) | 6 | 3,234 | 290 | 2,944 | **0** | **9.0 %** | **100.0 %** |
| **kirk** (N102DZ N40JD N560TW N582MM N872RA N888KG) | 6 | 3,234 | 942 | 2,292 | **0** | 29.1 % | 100.0 % |
| **n1098l thread** (N1098L N2100L N59906) | 3 | 1,617 | 52 | 0 | **1,565** | 3.2 % | **3.2 %** |
| **ALL 15 CASE TAILS** | 15 | **8,085** | **1,284** | **5,236** | **1,565** | **15.9 %** | **80.6 %** |
| control (Ryanair 4ca7b5, Lufthansa 3c6444) | 2 | — | 104 held / 36 empty on disk (every-8th-day probe, not a full window sweep) | | | 74.3 % | — |

**The single largest never-asked block is the whole n1098l thread.** N1098L, N2100L and
N59906 have **not one** `.miss` record anywhere on disk. `fetch_event_windows.py` defaults
to `--side following` and has only ever been run for `following` and `kirk`; `--side
n1098l` exists as a flag and has never been used. The 52 aircraft-days those three tails
DO hold inside event windows came in from the ADS-B Exchange monthly-sample sweep and
other one-off pulls, not from the window fetcher.

That is **1,565 aircraft-days — 19.4 % of everything the windows need — sitting in the
state that licenses no statement at all.** It is also free to close (§3).

### 1b. Per tail, per year (window-restricted)

Full table is in `gap_ledger.csv`. Coverage % = HELD / needed. Shape of it:

| Tail | 2022 | 2023 | 2024 | 2025 |
|---|---:|---:|---:|---:|
| SU-BGM | 0.0 % | 8.3 % | 4.2 % | 8.5 % |
| SU-BND | 0.0 % | 7.0 % | 12.7 % | 18.4 % |
| SU-BTT | 1.0 % | 7.6 % | 9.2 % | 14.2 % |
| SU-BTU | 1.0 % | 14.6 % | 8.5 % | 8.5 % |
| SU-BTV | 1.0 % | 6.4 % | 8.5 % | 11.3 % |
| T7-ELL | 0.0 % | 6.4 % | 23.2 % | 19.9 % |
| N102DZ | 1.0 % | 9.6 % | 47.2 % | 35.5 % |
| N40JD | 1.0 % | 8.3 % | 5.6 % | 44.7 % |
| N560TW | 1.0 % | 36.9 % | 36.6 % | 38.3 % |
| N582MM | 1.0 % | 44.6 % | 73.9 % | 88.7 % |
| N872RA | 2.0 % | 17.8 % | 53.5 % | 49.6 % |
| N888KG | 3.0 % | 21.0 % | 21.1 % | 11.3 % |
| N1098L / N2100L / N59906 | *never asked* | *never asked* | *never asked* | *never asked* |
| **CONTROL (both)** — every-8th-day probe, disk hit rate | **0.0 %** (0/56) | **97.5 %** (39/40) | **94.4 %** (34/36) | **86.1 %** (31/36) |

Two things this table says out loud:

* **The Egyptian fleet is genuinely sparse in these archives — 4–23 % against an 86–97 %
  control from 2023 on.** That is the expected profile of a government VIP aircraft based
  in Egypt, outside volunteer ADS-B receiver coverage for most of its life. It is **not**
  evidence of hiding, and it must never be published as such.
* **The Kirk-side bizjets are 2–3× better covered than the foreign fleet in the same
  windows.** Any "the Egyptian plane was not there" statement therefore rests on a much
  thinner record than the matching "the Kirk plane was there" statement. That asymmetry
  cuts against the thesis and belongs on the page.

### 1c. Reconciliation against the existing coverage accounting — **NO DISAGREEMENT**

Both accountings were re-derived independently from the filesystem and compared to the
generated numbers:

* **134 of 139** event `.yaml` files carry a `coverage:` block. Comparing
  `aircraft_days_needed`, `aircraft_days_held`, `aircraft_days_asked_and_archive_empty`,
  `aircraft_days_never_asked`, and the whole `by_side.following` sub-block:
  **0 disagreements out of 134.**
* `_airports_near_summary.csv` (`aircraft_days_needed`, `aircraft_days_held`,
  `coverage_pct_following_fleet`, `queried_pct_following_fleet`,
  `following_days_never_asked`): **0 disagreements out of 134.**

`airports_near.py`'s coverage accounting is trustworthy. Bryan does not need to pick a
winner.

**One real gap surfaced instead.** Five of the 139 events have **no `search:` block at
all**, so they have no window, no coverage numbers, and were never queried by anything:

| Event | Why |
|---|---|
| `20220519_tpusa_debate_night` | streamed debate, `city: UNKNOWN`, geocode FAILED |
| `20220521_tpusa_debate_night` | same |
| `20220705_tpusa_debate_night` | same |
| `20241015_university_of_nevada` | `city: AMBIGUOUS` — "University of Nevada" is Reno **or** Las Vegas; the title does not say |
| `20250429_tpusa_student_town_h` | `city: UNKNOWN` in `tpusa_events.csv` |

They appear in `_airports_near_summary.csv` with blank coverage columns and are silently
absent from every fleet total. `gap_ledger_by_event.csv` flags them
`NO_SEARCH_WINDOW_GEOCODE_FAILED`. The three debate nights are streamed events and may
have no travel to test; **20241015 and 20250429 are real physical events that nobody has
ever asked the archives about**, and both are cheap to fix by hand-resolving the city.

---

## 2. The 25 ARCHIVE RETENTION BOUNDARY events — control confirmation

**All 25 are in 2022. Every one of them is Charlie or TPUSA; none involves Erika.**

The control test in
`apis/public_open_source/data/recovery/archive_control_probe.json`
(run 2026-08-24, every 8th of the 553 window days, both free archives, two unrelated
airframes) records for **2022: 0 traces, 56 asked-and-empty, hit rate 0.0 %** — against
93.8 % (2023), 94.4 % (2024) and 81.9 % (2025).

I re-derived this from the control directories rather than trusting the JSON. The controls
were probed on **14 distinct 2022 dates** × 2 archives × 2 airframes = 56 requests, and
**every single one is a `.miss` file**:

`2022-01-02, 02-17, 04-02, 04-14, 05-17, 06-01, 07-05, 07-25, 08-14, 09-19, 10-10, 10-18, 10-26, 12-16`

**19 of the 25 retention-boundary events have a control-probe date falling inside their own
±2-day window**, so for those the control failed identically *on the same dates and the
same endpoints*, not merely in the same year:

| Event | Window | Control day inside it |
|---|---|---|
| 20220104_phoenix | 01-02 → 01-06 | 2022-01-02 |
| 20220216_st_charles | 02-14 → 02-18 | 2022-02-17 |
| 20220331_auburn | 03-29 → 04-02 | 2022-04-02 |
| 20220403_st_louis | 04-01 → 04-05 | 2022-04-02 |
| 20220412_boulder | 04-10 → 04-14 | 2022-04-14 |
| 20220413_berkeley | 04-11 → 04-15 | 2022-04-14 |
| 20220414_fullerton | 04-12 → 04-16 | 2022-04-14 |
| 20220602_grapevine | 05-31 → 06-06 | 2022-06-01 |
| 20220722_tampa | 07-20 → 07-26 | 2022-07-25 |
| 20220810_san_diego | 08-08 → 08-14 | 2022-08-14 |
| 20220814_phoenix | 08-12 → 08-16 | 2022-08-14 |
| 20220916_phoenix | 09-14 → 09-19 | 2022-09-19 |
| 20221010_phoenix | 10-08 → 10-12 | 2022-10-10 |
| 20221012_austin | 10-10 → 10-14 | 2022-10-10 |
| 20221017_fargo | 10-15 → 10-19 | 2022-10-18 |
| 20221018_kansas_city | 10-16 → 10-20 | 2022-10-18 |
| 20221020_tallahassee | 10-18 → 10-22 | 2022-10-18 |
| 20221025_charlotte | 10-23 → 10-27 | 2022-10-26 |
| 20221217_phoenix | 12-15 → 12-22 | 2022-12-16 |

**The remaining 6 rest on year-level control inference only**, because no control-probe day
landed inside their window. State it that way and do not upgrade it:
`20220329_colorado_springs`, `20220330_fayetteville`, `20220420_milwaukee`,
`20221003_newark`, `20221013_east_lansing`, `20221130_albuquerque`.

### For the record: which events can never be tested with free sources, and why

**All 28 of the 2022 events**, of which 25 carry the retention verdict and 3 are the
un-geocoded debate nights.

The reason is not the aircraft. **globe.airplanes.live and adsb.lol `globe_history` do not
retain 2022 at all** — the control aircraft prove it, at 0 of 56. The one free route that
reaches 2022, ADS-B Exchange's public sample archive, publishes **one day per month, the
1st**, so it can confirm that an airframe existed and flew somewhere but can never test a
claim about a specific mid-month 2022 date. That sweep is already complete: **all 15 tails
× all 56 months (2022-01 → 2026-08) have been asked, 207 aircraft-days recovered**, and
only 3 of the 28 2022 events got anything out of it (`20220330_fayetteville`,
`20220331_auburn`, `20220403_st_louis` and `20220602_grapevine`/`20221130_albuquerque`
picked up 4–5 aircraft-days each from a 1st-of-month sample landing in-window).

**This is the sharpest constraint on the whole investigation.** Bryan's thesis says the
following behaviour *starts* in 2022 and *changes* in the later years. The free archives
cannot see 2022 at all, so the "before" half of a before/after argument has no free data
behind it. **Any 2022 gap published as suppression would be false**, and any claim that
the later-year pattern differs from 2022 is currently unfalsifiable rather than supported.

### Testability tiers for all 139 events

| Tier | Count | What a null result there means |
|---|---:|---|
| **Testable, some following-fleet trace held** | **100** | An empty answer is a fact about the aircraft (archive healthy, 100 % queried) — still not proof it was elsewhere |
| **Testable, ZERO following-fleet trace held** | **9** | Asked all 30 aircraft-days, got nothing. Weakest usable tier. |
| **2022 archive retention boundary** | **25** | **Untestable for free. Never publish as a removal.** |
| **No search window (geocode failed)** | **5** | **Never asked.** Not a finding in either direction. |

The 9 zero-coverage-but-healthy events, where "no Egyptian jet was near" is technically
asked-and-empty but rests on a *completely* empty record:

`20230321_baton_rouge`, `20230321_new_brunswick`, `20230322_columbus`,
`20240913_manhattan`, `20241030_greenville`, `20241031_high_point`,
`20250228_tallahassee`, `20250303_los_angeles`, `20250313_knoxville`

And the distribution of following-fleet coverage across the 109 testable events:

| Following coverage | Events |
|---|---:|
| 0 % | 9 |
| under 10 % | 39 |
| 10–25 % | 54 |
| 25–50 % | 7 |
| 50 %+ | **0** |

**No event anywhere in this investigation has more than 50 % of its foreign-fleet
aircraft-days on disk.** That is the honest ceiling on everything built from ADS-B traces.

---

## 3. Every remaining route to more data, ranked by ground closed per unit of effort

### THE SINGLE HIGHEST-LEVERAGE ACTION

> **Run `python3 fetch_event_windows.py --run --side n1098l --window 2`.**
>
> Cost: **$0.** Effort: one command. Time: ~1,565 aircraft-days × 2 archives ≈ **3,130
> requests ≈ 16–21 minutes** at the 0.3–0.4 s sleep the harness already uses.
> Closes **1,565 aircraft-days — 100 % of all remaining NEVER_ASKED in the entire
> investigation**, and takes the fleet from 80.6 % queried to **100 % queried**.
>
> It also has real upside: the free monthly-sample sweep already found N1098L on 19
> month-firsts, N2100L on 17 and N59906 on 23 — these are US-registered airframes flying in
> dense US receiver coverage, so their hit rate in the daily archives should land nearer the
> Kirk-side 29 % than the foreign 9 %. Expect **roughly 250–450 new held aircraft-days**.
>
> Caveat that must travel with the result: the n1098l tails are a **DIFFERENT CLAIM** (LASAI
> Aviation II / Fort Huachuca / survey thread). Closing their coverage gap does not add
> anything to the Egyptian-fleet count and the threads must not be merged.

**Second-cheapest:** hand-resolve the city for `20241015_university_of_nevada` and
`20250429_tpusa_student_town_h`, regenerate their yaml, and fetch. Cost $0, ~10 minutes,
closes 2 events that are currently invisible to every total on the site.

### The full route table

| Route | Credential | Cost | Effort | What it would close | Verdict |
|---|---|---|---|---|---|
| **`fetch_event_windows.py --side n1098l`** | none | **$0** | ~20 min, 1 command | **1,565 aircraft-days = every NEVER_ASKED day left** | **DO THIS FIRST** |
| **Geocode the 5 no-window events** | none | **$0** | ~10 min manual | 2 real events (+3 streamed debates likely N/A) | **DO THIS SECOND** |
| **FlightAware AeroAPI v4** | `AEROAPI_KEY` — **EMPTY** | ~$0.002/query advertised; a 15-tail × 56-month sweep is on the order of 1,000–2,000 billed pages ≈ **$2–$20 in query cost** — but **the plan minimum is the real gate and must be read at signup, not assumed** | ~1 day to write + run | **History back to 1 Jan 2011 — the ONLY route that reaches 2022 at day resolution.** Would make all 25 retention-boundary events testable and would test the other 5,236 asked-and-empty days against a denser network. **And it returns flight LEGS with an origin and destination airport, not receiver traces** — which is the only data shape that can directly test Bryan's "landed at a different nearby airport" hypothesis without depending on whether a volunteer heard the descent. | **HIGHEST VALUE PURCHASE. Nothing else substitutes.** |
| **OpenSky Network, OAuth2** | `OPENSKY_CLIENT_ID` / `_SECRET` — **EMPTY** | **FREE** (registered account: 4,000 credits/day vs 400 anonymous; 8,000 for feeders) | ~2 h: register, then `opensky.js` already exists | `/flights/aircraft` by ICAO24 with begin/end, history to 2016. An **independent receiver network** — a genuine cross-check, not another view of the same feed. Coverage of US bizjets is real but patchier than the tar1090 networks; **do not expect it to rescue 2022.** | **BEST FREE ROUTE NOT YET TAKEN. Take it before spending money.** |
| **adsblol GitHub Releases day-tarballs** | none | free, ~2–3 GB streamed per day (filtered, never stored) | ~1 min/date; 22 dates done so far, all `NOT_IN_THE_BACKUP_EITHER` | **NOT INDEPENDENT of adsb.lol's live API — same organisation, same feeders.** Its only real use is dates the live API **403s**: 2025-10-12 → ~2025-12-15. Only **4 of 139 event windows** touch that band, and the last speaking event is 2025-10-31. | **LOW VALUE for events. Keep for spot-checks; do not sweep it.** |
| **ADS-B Exchange free monthly samples** | none | free | already run | **EXHAUSTED.** All 15 tails × all 56 months asked, 207 hits. Nothing left to ask. | **CLOSED** |
| **ADS-B Exchange via RapidAPI** | `ADSBX_RAPIDAPI_KEY` — **EMPTY** | subscription | ~half a day | The RapidAPI surface is mostly **live**, not historical; ADSBX historical is the separate paid tier, and `globe.adsbexchange.com` history has returned 403 to the public since it commercialised. Real value is narrow: several original claims were screenshotted off those now-403 pages, so this is the vendor that could confirm whether the screenshots were read correctly. | **LOW value per dollar for coverage; MODERATE for provenance** |
| **Flightradar24 API** | `FR24_API_TOKEN` — **EMPTY** | credit-metered subscription; the consumer paid tiers (Silver 90 days / Gold 1 yr / Business 3 yrs of history) are separate from the API | ~half a day | The `flight summary` endpoint is the machine-readable form of the aircraft-history table the **original claims were photographed from** — so it is the direct way to check whether those screenshots were read correctly. **Every FR24 observation this investigation holds came from a logged-out free tier showing 7 days**, the weakest view the vendor offers. | **MODERATE. Buy after AeroAPI, for provenance rather than coverage** |
| **Wayback Machine (CDX + `id_` raw)** | none | free | ~1 h per target | Page-level only — recovers **what a site said on a date**, never new trace data. Already produced the one genuine documented removal and 109 pre-2017 FlightAware legs. Modern FR24/FlightAware aircraft pages are client-side apps, so archived copies hold **no server-rendered rows**. | **Keep for removal-proving. Cannot close coverage.** |
| **archive.today / archive.ph** | none | free | ~1 h | Returned **HTTP 429** on both 2026-08-24 attempts. Status today unknown — **untested, not ruled out.** | **RETRY, cheap, low expected yield** |

### Ranked recommendation

1. `--side n1098l` sweep — free, 20 minutes, closes **every** remaining NEVER_ASKED day.
2. Geocode the 2 real un-windowed events — free, 10 minutes.
3. Register an OpenSky account and run `opensky.js` — free, adds an **independent** network.
4. **Buy AeroAPI.** It is the only route to 2022 at day resolution, and the only one that
   returns origin/destination airports rather than receiver traces. Everything Bryan's
   thesis needs and cannot currently get is behind that one key.
5. FR24 API, for provenance on the screenshots the claim was built from.

---

## 4. The ±7-day widening fetch running in the background

Read from `scratchpad/fetch_w7.log` and confirmed against the live process (PID 51871):

```
fetch_event_windows.py --run --side following --window 7 --sleep 0.3
6 aircraft x 973 window days x 2 archives
4999 requests needed (6677 already on disk)
  600/4999  hit=29 miss=571 err=0   9.2 min elapsed, ~68 min left
```

**Progress: 600 of 4,999 requests (12 %) at the time of this snapshot, ~68 minutes
remaining. Not interfered with.**

### What it WILL add

* The following fleet's window denominator goes from **3,234 aircraft-days (±2)** to
  **5,838 (±7)** — about **+2,600 new aircraft-days** asked for the six foreign tails.
* Running hit rate so far is **29 / 600 ≈ 4.8 %**, but the sweep works chronologically and
  the first ~250 requests were 2022 (0 hits, exactly as the retention boundary predicts).
  At the following fleet's established 9.0 % aircraft-day rate, expect roughly
  **200–280 new HELD aircraft-days** when it finishes.
* Every one of the ~4,970 non-hits lands as a `.miss.json.meta.json`, which converts those
  days from NEVER_ASKED to ASKED_AND_EMPTY — i.e. it makes a wider window *sayable*.
* This is the right shape of pull for Bryan's hypothesis 2. A jet that repositions to a
  nearby field days before or after an event is invisible at ±2 and visible at ±7.

### What it will NOT add — and these matter

* **It is `--side following` ONLY.** It does not touch N1098L / N2100L / N59906, so the
  1,565-day NEVER_ASKED hole in §1a is **not** being closed by this run.
* **It does not widen the KIRK side.** When it finishes, the foreign fleet will be queried
  at ±7 while the Kirk-side tails stay at ±2. **Any comparison drawn across that boundary
  is comparing unequal search effort**, and a "the Egyptian jet was there but the Kirk jet
  was not" statement built on it would be an artefact of the windows, not a finding. Either
  re-run the Kirk side at ±7 too, or restrict every comparison to ±2.
* **It cannot touch 2022.** Same two archives, same retention boundary. Widening the window
  in a year the archive does not retain widens nothing.
* **A wider window weakens what a hit means.** A jet at a nearby field 6 days from an event
  is a much weaker association than one 6 hours away. The `overlap` definition in
  `Overlap_Window_Definition.mdx` was written for ±2; **do not let ±7 hits enter an
  overlap count without re-deciding that definition first**, and publish the day-offset
  next to every new pairing.
* It still proves presence only. Never purpose, never occupancy. Erika Kirk's itinerary is
  published nowhere, and no archive anywhere produces it.
