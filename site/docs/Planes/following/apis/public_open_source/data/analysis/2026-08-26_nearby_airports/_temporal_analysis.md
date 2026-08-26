# Did the behaviour actually change over time?

Strand: temporal test of Bryan's hypotheses 1 and 2 — that Charlie Kirk noticed the
aircraft, and that in the later years they stopped landing at *his* airport and started
landing at a *different nearby* airport instead.

Data snapshot: 2026-08-26. All figures re-derived from
`site/docs/Planes/following/apis/public_open_source/data/recovery/trace_visit_index.json`,
the per-tail `data/recovered/*.meta.json` files (for coverage), the 139
`speaking/*.yaml` event records, and `speaking/_airports_near_summary.csv`.
A ±7-day widening pull for the foreign fleet was still running in the background when
this snapshot was taken; nothing below depends on its results and all of it should be
re-run when it lands.

---

## HEADLINE

**The change Bryan predicts is not in the data, and where the data can speak at all it
points the other way.** Across 3.5 years the foreign fleet has exactly **two** North
American ground contacts within 250 miles of a Kirk/TPUSA event, and the *nearby-airport*
one (Apr 2024, 35.9 mi) comes **before** the *same-airport* one (Sep 2025, 4.9 mi) —
the reverse of the predicted same→nearby drift. The same-airport share **rises** with
time and survives coverage normalisation; the nearby-airport share is a single record
and does not trend at all.

**And the deeper result is that this is not a "following the tour" pattern in the first
place. It is a Utah pattern.** Only 3 of the 139 events are in Utah, 2 of those 3 have
foreign-fleet presence, and **0 of the other 136 events anywhere in the country do.**
The Provo visits then **continue after Charlie Kirk was killed** — SU-BND was on the
ground at KPVU on five separate days in May and June 2026. Provo also holds Duncan
Aviation, which has run the Egyptian Air Force maintenance account since ~1999
(`airports.csv`, KPVU row). A pattern that is confined to one MRO city and outlives the
person it is said to follow is much better explained by the shop than by the man.

---

## 1. The chronological series

`temporal_series.csv` — one row per foreign-fleet North American **ground visit**
(on-ground positions resolved to a field), 2022-02-01 → 2026-06-04.
69 visit records over **51 distinct tail-days**, six tails
(SU-BGM, SU-BND, SU-BTT, SU-BTU, SU-BTV, T7-ELL).

Each row carries the airport, the nearest **North American** Kirk/TPUSA event within
±0/1/2/3/7 days, the great-circle miles from the visit to that event's city, whether the
visited field is inside that event's own 40-mile airport list, and a classification.

Airport mix by year (visit records):

| year | airports |
|---|---|
| 2022 | KTUS:2 KLAX:2 KILG:1 KICT:1 |
| 2023 | KILG:10 KLAX:3 KBGR:3 |
| 2024 | KPVU:4 KLNK:2 KILG:2 KSLC:1 |
| 2025 | KPVU:18 KILG:6 KIAD:3 KORD:2 KMOT:1 |
| 2026 | KPVU:6 MMUN:2 |

Read the airport column before the distance column. KILG is the documented transatlantic
customs-and-fuel stop; KLNK is Duncan Aviation's headquarters plant; KICT holds a
Falcon-authorised service centre; KTUS holds Bombardier's largest service centre and the
only tail there is T7-ELL, a Bombardier Global; KBGR and KMOT are customs entry fields;
KPVU holds Duncan Aviation Provo. **Almost the entire North American ground record of
this fleet sits on maintenance and customs fields.**

---

## 2. Does distance from the nearest event grow over the years? No — it shrinks.

Distance from each visit to the nearest North American Kirk/TPUSA event within ±2 days:

| year | records | median mi | mean mi | min mi | ≤40mi | 40–100 | 100–250 | >250 | no NA event in ±2d |
|---|---|---|---|---|---|---|---|---|---|
| 2022 | 6 | 1279.3 | 1279.3 | 1279.3 | 0 | 0 | 0 | 1 | 5 |
| 2023 | 16 | 1116.6 | 1239.2 | 636.2 | 0 | 0 | 0 | 13 | 3 |
| 2024 | 9 | 1005.2 | 1005.2 | 35.9 | 1 | 0 | 0 | 1 | 7 |
| 2025 | 30 | 607.3 | 804.6 | 4.9 | 8 | 0 | 0 | 13 | 9 |
| 2026 | 8 | — | — | — | 0 | 0 | 0 | 0 | 8 |

Excluding KILG (the customs stop, which inflates early distances):

| year | records | median mi | mean mi | min mi |
|---|---|---|---|---|
| 2022 | 5 | — | — | — |
| 2023 | 6 | 1116.8 | 1141.4 | 1116.6 |
| 2024 | 7 | 35.9 | 35.9 | 35.9 |
| 2025 | 24 | 305.9 | 560.0 | 4.9 |
| 2026 | 8 | — | — | — |

The median **falls** from ~1,279 mi (2022) to ~607 mi (2025). That is the opposite of
"the planes moved further away as he wised up". It is also almost entirely one week:
strip the 2025-09-04→09-12 Provo cluster and 2025 has no record under 250 miles.

The distribution is bimodal and empty in the middle: every record is either ≤40 mi
(9 records, all Utah) or ≥250 mi (28 records). **There is no "nearby airport" band to
find a trend in.** The 40–250 mile zone — exactly where a deliberate
land-at-the-next-field-over behaviour would show up — is **empty in all four years.**

---

## 3. SAME_AIRPORT vs NEARBY_AIRPORT, normalised by coverage

Coverage denominator = distinct foreign-fleet (tail, date) pairs for which an archive
actually returned a trace ("held"), out of pairs the archive was asked for ("asked").
Counting is per **tail-day**, not per record.

| year | asked | held | cov% | NA visit-days | visit-days per 100 held | days ≤100 mi of an event | per 100 held | SAME_AIRPORT days | NEARBY_AIRPORT days |
|---|---|---|---|---|---|---|---|---|---|
| 2022 | 793 | 10 | 1.3 | 5 | 50.0 | 0 | 0.00 | 0 | 0 |
| 2023 | 1016 | 94 | 9.3 | 13 | 13.8 | 0 | 0.00 | 0 | 0 |
| 2024 | 866 | 108 | 12.5 | 6 | 5.6 | 1 | 0.93 | 0 | **1** |
| 2025 | 874 | 130 | 14.9 | 21 | 16.2 | 5 | 3.85 | **5** | 0 |
| 2026 | 41 | 41 | 100.0* | 6 | 14.6 | 0 | 0.00 | 0 | 0 |

\* **The 2026 row is not a rate.** There are **zero** `.miss` records for 2026 across all
six tails — only days that returned data were saved. 2026 was never systematically swept,
so its "100% coverage" is an artefact and its rate column is meaningless. The *existence*
of the 2026 Provo visits is a fact; the *frequency* is not measurable from this archive.

### Does the trend survive normalisation?

**The same-airport rise does.** 2025 holds 130 aircraft-days against 2024's 108 — a
1.2× coverage increase — while the near-event rate goes 0.93 → 3.85 per 100 held days,
a 4.1× increase. Coverage cannot manufacture that ratio.

**But it survives on n = 1 cluster.** All five SAME_AIRPORT tail-days are the same field
(KPVU) in the same eight days (2025-09-08 → 2025-09-12) around the same single event
(Orem, 2025-09-10) with two tails. This is one event, not a trend. A "rate" computed off
one cluster is arithmetic, not evidence, and it must never be published as a rate.

**The nearby-airport trend does not exist at all.** One record, in 2024, and nothing
before or after it. There is no series to normalise.

---

## 4. The two proximity records, in full

Every foreign-fleet North American ground visit within 250 miles of a North American
Kirk/TPUSA event, 2022-01 → 2026-06:

| date | tail | field | class | miles | gap | event | event class | inferred arrival airport |
|---|---|---|---|---|---|---|---|---|
| 2024-04-23 | SU-BTT | KPVU | NEARBY_AIRPORT | 35.9 | 0 d | 20240423_salt_lake_city | CHARLIE_ONLY | KSLC |
| 2025-09-08 | SU-BND | KPVU | SAME_AIRPORT | 4.9 | −2 d | 20250910_orem | CHARLIE_ONLY | KPVU |
| 2025-09-09 | SU-BND | KPVU | SAME_AIRPORT | 4.9 | −1 d | 20250910_orem | CHARLIE_ONLY | KPVU |
| 2025-09-10 | SU-BND | KPVU | SAME_AIRPORT | 4.9 | 0 d | 20250910_orem | CHARLIE_ONLY | KPVU |
| 2025-09-10 | SU-BTT | KPVU | SAME_AIRPORT | 5.0 | 0 d | 20250910_orem | CHARLIE_ONLY | KPVU |
| 2025-09-12 | SU-BND | KPVU | SAME_AIRPORT | 4.9 | +2 d | 20250910_orem | CHARLIE_ONLY | KPVU |

That is the whole of it. Six rows, five tail-days, two events, one metro.

Note on the 2024-04-23 row: it is the **only** record in the entire series that looks
like the behaviour Bryan describes — the event's inferred arrival field is Salt Lake City
(KSLC) and the aircraft is 35.9 miles away at Provo. `speaking/20240423_salt_lake_city.yaml`
records it as `su_just_outside_radius: 3` (SU-BND, SU-BTT), i.e. **outside** the 40-mile
ring drawn around KSLC, because the ring is centred on the airport rather than on the
city. Whether it counts as "nearby" depends on which centre you use, and that ambiguity
should be stated wherever this record is published. It is one record either way, and it
is **earlier** than every same-airport record, which is the wrong order for the thesis.

Both events are `CHARLIE_ONLY`. Neither is an Erika event. That cuts against the
widely-repeated "the planes were tracking Erika" framing as much as it cuts against
hypothesis 2 — but with n = 2 it is far too thin to carry either way.

---

## 5. The post-death test — the strongest single result in this strand

If the aircraft were following Charlie Kirk, the pattern should stop when he was killed
on 2025-09-10. It does not.

| period | asked | held | cov% | NA visit-days | KPVU days | KPVU per 100 held |
|---|---|---|---|---|---|---|
| 2022-01-01 → 2025-09-10 | 3277 | 282 | 8.6 | 38 | 14 | 4.96 |
| 2025-09-11 → 2025-12-31 | 272 | 60 | 22.1 | 7 | 1 | 1.67 |
| 2026 (NOT a systematic sweep) | 41 | 41 | — | 6 | 5 | — |

SU-BND was on the ground at Provo Municipal on **2026-05-13, 2026-05-14, 2026-05-20,
2026-06-02 and 2026-06-04** — eight to nine months after Charlie Kirk's death, and
several months after Erika Kirk had become TPUSA CEO. Source for the 2026-05-13 record:
`https://globe.airplanes.live/globe_history/2026/05/13/traces/3e/trace_full_01003e.json`,
HTTP 200, 42 points, first and last position on the ground at 40.2297 / −111.7275.

Honest reading of that table:
* The **existence** of continued Provo visits is solid and coverage-independent.
* The **rates** are not comparable across the three rows. The pre-death denominator is
  built from an event-clustered ±2-day sweep; the late-2025 denominator is the same sweep
  at higher archive availability; the 2026 denominator is a hit-only pull with no misses.
* The one thing the rates do rule out is a **collapse**. Provo visits did not stop.

This is the result that most weakens Bryan's thesis, and per the site's own rules it
belongs in the headline, not a footnote.

---

## 6. The Utah confinement — what the pattern actually is

* 139 events in the record; **3 are in Utah** (Salt Lake City 2024-04-23, Orem
  2025-09-10, Logan 2025-09-30).
* **2 of those 3** have foreign-fleet ground presence within ±2 days.
* **0 of the other 136** do — not at ≤40 mi, not at 40–100 mi, not at 100–250 mi.
* 22 of the 51 foreign-fleet North American visit-days are at KPVU, and several of them
  (2025-04-08, 2025-04-10, 2025-05-23, all six 2026 days) have **no** Kirk/TPUSA event
  within ±2 days at any distance.
* `airports.csv` records the Provo innocent explanation in the repo's own words: Duncan
  Aviation on the field, holding the Egyptian Air Force maintenance account since ~1999,
  and two Provo→Provo closed-loop sorties (SU-BGM 10 Apr 2025, 55 min; SU-BND 5 Sep 2025,
  68 min) with "the classic post-maintenance functional check-flight signature."

So the honest description of the whole 3.5-year record is: **this fleet's North American
footprint is a maintenance-and-customs footprint (Wilmington, Lincoln, Wichita, Tucson,
Bangor, Minot, Provo, Le Bourget), and the one city where it repeatedly coincides with a
Kirk event is also the city where its maintenance shop is.** The 6-day September 2025
Provo stay ending on the day Charlie Kirk was killed is not explained away by that, and
this strand does not attempt to explain it away — but it is one stay, and the rest of the
record does not corroborate a touring-surveillance pattern.

---

## 7. The coverage confound, stated at full strength

Coverage is radically uneven and everything above is bounded by it.

| year | events | aircraft-days needed | held | cov% | control verdict = ARCHIVE RETENTION BOUNDARY |
|---|---|---|---|---|---|
| 2022 | 28 | 2025 | 22 | 1.1 | 25 of 28 |
| 2023 | 29 | 3255 | 411 | 12.6 | 0 |
| 2024 | 41 | 3255 | 718 | 22.1 | 0 |
| 2025 | 41 | 3285 | 848 | 25.8 | 0 |

(from `speaking/_airports_near_summary.csv`; these are all-15-tail figures, the
foreign-fleet-only figures in §3 are lower.)

* **36 of the 139 events have ZERO following-fleet coverage.** Nothing at all is known
  about those days.
* 103 events have any coverage at all; 61 have ≥10%; **25 have ≥20%; only 3 have ≥30%;
  none have ≥50%.**
* Of the 103 events with any coverage, 2 have foreign-fleet presence. Of the 61 with
  ≥10%, 1 does. Of the 25 with ≥20%, 1 does.
* **2022 is effectively untested.** 25 of its 28 events carry a control-probe verdict of
  ARCHIVE RETENTION BOUNDARY — the archive has nothing for anybody on those dates, which
  the control aircraft confirm. Nothing in this document says anything about 2022
  behaviour, and no year-over-year statement that leans on 2022 is safe.

**What this means for the trend claims.** The apparent same-airport *rise* survives
normalisation between 2024 and 2025 (§3) but rests on one cluster. The apparent
distance *shrink* (§2) is driven by that same cluster. The absence of nearby-airport
behaviour is a **weak** negative for 2022 (untested) and a **moderate** negative for
2023–2025, where ~10–26% of aircraft-days were actually held and the ±2-day sweep was
deliberately centred on the event dates — i.e. the sampling was biased *toward* finding
event proximity, and still found almost none.

**An absence here is not a finding.** A miss means a volunteer receiver network heard
nothing. Parked with the transponder off, outside receiver coverage, and a wrong claimed
event date all look identical from the archive. None of the 136 non-Utah events with no
foreign-fleet contact is evidence that no aircraft was there.

---

## 8. Did Charlie Kirk ever say he was being followed by aircraft?

**No such statement was found.** Searched:

* `Charlie_Kirk.txt` (read-only, never written to) — full-text search for being followed,
  followed him, following me, tailing, surveilled, tracked, noticed a plane/jet, wised up.
* `knowledge/` (FULL_WRITE_UP.md, the per-model big write-ups, INTEL_Connections.md,
  bry_research.txt, Bryan_Overview.txt).
* `Research/` including `Research/raw/`, `Research/evidence/`, `Research/Topics/`.
* `site/docs/Planes/following/x_discussions.mdx` — the full public log of the X argument.
* `site/docs/Planes/following/speaking/week/**` — **203 weekly Grok X-search dumps
  covering 2022–2025, 365 post blocks authored by @charliekirk11 (1,640 lines mentioning him).** This is the best
  corpus of Charlie Kirk's own words in the repo. Filtering his own posts for
  plane / jet / aircraft / tail number / followed / tracked / surveillance returned
  **12 blocks, all false positives** — the only literal hit is
  *"nearly 80% of students I spoke with said they followed me on TikTok"*
  (@charliekirk11, Wed, 27 Nov 2024 19:03:34 GMT,
  `site/docs/Planes/following/speaking/week/2024/week_48.md`).

The two closest documentary items in the repo are **about phones and threats, not
aircraft**, and both are anonymous relays:

1. `Charlie_Kirk.txt`, section *"Charlie Won't make it until Christmas / Phone Tapped"* —
   an unnamed TPUSA mega-donor, voice and image digitally altered, relayed second-hand:
   > "And get this: Charlie said his phone went haywire—battery overheating out of
   > nowhere, draining in minutes, weird feedback on calls. He even found a SECOND SIM
   > CARD in a backup phone he NEVER installed. Hacked? 100%."

   No date, no name, no aircraft, no airports. It is a claim about phone compromise.

2. `Charlie_Kirk.txt`, section *"Candace & Macrons / France"*:
   > "Charlie Kirk was murdered within 24 hours of telling his inner circle he knew who
   > was coming for him."

   No date, no named source, no aircraft.

**Conclusion for hypothesis 1: the documentary basis does not exist in this repo.** There
is no recorded statement by Charlie Kirk — or by anyone quoting him — that he noticed
aircraft following him, was upset about aircraft following him, or changed anything in
response. Hypothesis 1 is currently an inference from the flight data, and the flight
data (§2–§5) does not support it either. If it is to be published at all it must be
published as Bryan's hypothesis with an explicit "no statement by Charlie Kirk on this
has been found."

Where to look next if someone wants to close this: full-text search of Charlie Kirk's own
podcast transcripts (`~/BGit/all/politics/charlie_kirk/research/` holds podcast and
Discord transcripts not covered by the weekly X dumps), and TPUSA staff/security
interviews. The X-post corpus is now exhausted for this question.

---

## 9. What this strand cannot test

* **2022 entirely.** 1.1–1.3% coverage, 25 of 28 events at an archive retention boundary.
* **Any claim about a specific mid-month date before 2023.** The only 2022 source is
  `adsbexchange-samples`, which publishes the 1st of each month. Every 2022 row in
  `temporal_series.csv` is a 1st-of-month or a 2022-02-01/06-01/08-01/09-01 sample day.
* **Occupancy.** No trace anywhere places Charlie Kirk, Erika Kirk, or any named person
  aboard any of these aircraft, and Erika Kirk's itinerary is not published. Every
  proximity in §4 is aircraft-to-city, not person-to-person.
* **Purpose.** Presence is all that is shown. Nothing here speaks to why any aircraft was
  anywhere.
* **The nearby-airport hypothesis as a rate.** With one qualifying record in 3.5 years
  there is no denominator that makes a rate meaningful.
* **Whether more overlaps hide at adjacent airports (hypothesis 4).** This strand looked
  for them across the full 3.5-year event history at 40, 100 and 250 miles and the
  40–250 mile band is empty in every year. That is a negative result *within the held
  archive*, and the held archive is 10–26% of the aircraft-days needed.
* **2026 frequency.** Hit-only pull, no misses recorded, no systematic sweep run.

---

## Files

* `temporal_series.csv` — 69 foreign-fleet North American ground-visit records,
  chronological, with per-visit nearest-event distance at five time windows.
* `_coverage_days.json` — the asked/held (tail, date) sets behind every normalisation.
* `_agg_output.txt` — raw output of the aggregation script.
* `build_temporal2.py`, `agg.py` — the scripts. Re-run after the ±7-day widening pull
  completes; nothing in this document is expected to be stable against new data.
