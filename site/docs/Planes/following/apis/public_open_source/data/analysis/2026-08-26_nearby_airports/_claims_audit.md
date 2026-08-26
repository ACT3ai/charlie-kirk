# Audit of overlaps.csv against recovered primary ADS-B

Run 2026-08-26. Read-only strand. Nothing under `site/docs/Planes/following` was modified.

**Inputs.** All 85 rows of `site/docs/Planes/following/overlaps.csv`; every recovered trace on disk
(`site/docs/Planes/<TAIL>/data/recovered/*_trace_full.json[.gz]`), read fix-by-fix rather than through
the pre-computed index; the miss records (`*_trace_full.miss.json.meta.json`) that record a day the
archive was *asked* and held nothing; `apis/public_open_source/data/recovery/trace_visit_index.json`;
`archive_control_probe.json`. Geometry from `code/lib/geo.py` (OurAirports, CC0). AGL is barometric
altitude minus published field elevation, so it is approximate and can read negative on the surface.

**Method, and why it differs from the run already recorded in the CSV.** For each row I computed the
minimum distance from the claimed field to *every position in every trace held for that tail on the
claimed UTC day*, from all sources, plus the altitude at that point and whether any on-ground fix fell
within 3 km. The existing `adsb_verified_note` column appears to have been generated from a narrower
read — in several rows it reports a closest approach that is simply the first fix of the day, and in ten
rows it rests on the day before or after the claim rather than the claim's own date.

---

## 1. What primary ADS-B can now say, row by row

| Result | Rows |
|---|---:|
| On-ground fix within 3 km of the claimed field, on the claimed day | 10 |
| Departure roll out of the claimed field (was on the ground, archive missed the ground flag) | 2 |
| Approach or departure at the claimed field, no on-ground fix held | 11 |
| Low over the claimed metro, no landing at the claimed field | 2 |
| Descending toward the claimed field, coverage ends before touchdown | 1 |
| Partly confirmed (one leg of a two-leg claim) | 1 |
| Contradicted by same-day primary position data | 1 |
| Weakly contradicted (five minutes of coverage) | 1 |
| **Primary data speaks to the claim at all** | **29** |
| Archives asked for the exact day and held nothing (NOT HEARD — not evidence of absence) | 30 |
| No coverage: 2022 retention boundary, or never queried | 17 |
| Row names no date | 5 |
| Row names no tail | 4 |
| **Silent** | **56** |

Per-row detail is in `claims_audit.csv` (columns `my_verdict`, `closest_km`, `closest_agl`,
`ground_at_claimed`, `evidence`, `detail`, `correction_action`).

I disagree with the recorded `adsb_verified_verdict` on 24 of 85 rows. Most of those disagreements are
bookkeeping — NOT_HEARD versus NO_ARCHIVE_COVERAGE, which matters for honesty but changes no claim.
**Four disagreements change what the site says**, and they are in sections 2 and 3.

---

## 2. Claims the recovered data now CONTRADICTS, or whose published refutation is itself wrong

These matter more than the confirmations. Two directions of error appear, and the second is the larger one:
**the site currently publishes the word "Refuted" on rows the recovered data does not refute.**

### 2.1 Genuinely contradicted by same-day primary data — leave as refuted

**OWENS-050 — SU-BND, 12 May 2023, claimed St. Louis (KSTL).**
Same-day trace (adsb.lol and airplanes.live, identical): airborne out of Paris-Le Bourget 07:25Z, ends
descending into Inshas Air Base, Cairo 11:15Z. Never closer than 7,034 km to St. Louis. The 9 May trace
separately shows the aircraft leaving St. Louis Downtown for Europe. **The existing ELSEWHERE verdict is
correct and is now backed by primary position data rather than an auditor's assertion.**

**OWENS-036 — SU-BTT, 18 June 2025, claimed Omaha (KOMA).** *Weaker than the page implies.*
The whole day's holding is 7 fixes (adsb.lol) / 9 (airplanes.live), spanning 06:23–06:28Z, at FL320
between Alexandria and El Alamein, Egypt — 10,140 km from Omaha.
- Page text to correct: "SU-BTT was tracked on 2025-06-18 and was somewhere else."
- Correction: "**The only ADS-B held for 18 June 2025 is five minutes of it** — 06:23 to 06:28 UTC, at
  32,000 ft between Alexandria and El Alamein, Egypt. That is not a day's track. It places the aircraft
  in Egypt that morning and leaves the rest of the day unobserved."

### 2.2 Published as "Refuted" — the recovered data says the opposite. HIGH PRIORITY.

**OWENS-024 and SITE-003 — SU-BTT, 3 April 2024, claimed Wichita (KICT).**
Page: `site/docs/Planes/following/overlap/20240403_KS_wichita_lawrence_owens_024/overview.mdx`, line 183
and line 226.

Currently published:
> **Refuted.** The aircraft was tracked that day and it was somewhere else. On 3 April 2024 SU-BTT's
> track begins near Jesse Viertel Memorial Airport, Boonville, **Missouri** (16.01 km) and ends at
> **Wilmington, Delaware** (KILG, 1.48 km). Its closest approach to **KICT was 1,852.96 km**. Both
> archives agree.

That is wrong, and "both archives agree" is the part that is wrong. The two archives hold different
amounts of the day. The **airplanes.live** trace opens with the aircraft *climbing out of Wichita*:

| Time (UTC) | Baro alt | Distance to KICT |
|---|---:|---:|
| 13:43:30 | 1,675 ft (342 ft AGL) | **1.4 km** |
| 13:44:04 | 3,525 ft | 4.4 km |
| 13:46:34 | 15,350 ft | over KAAO |
| … FL410 across the country … | | |
| 16:05:35 | 450 ft | 1.1 km from KILG |

The **adsb.lol** trace for the same day does not begin until 14:15:16Z, already at FL410 over Missouri —
after the aircraft had left Kansas. The published 1,852.96 km figure is the closest approach *of the
adsb.lol trace only*.

Exact correction: replace "Refuted … closest approach to KICT was 1,852.96 km. Both archives agree" with
> **Confirmed as a departure, not refuted.** The airplanes.live trace for 3 April 2024 begins with
> SU-BTT climbing out of Wichita — 13:43:30 UTC, 1.4 km from KICT at 342 ft above the field — and runs
> nonstop at FL410 to a landing at Wilmington, Delaware at 16:05 UTC. The adsb.lol trace for the same
> day does not start until 14:15 UTC, over Missouri, which is why an earlier pass over this row reported
> a 1,853 km closest approach. **The two archives do not hold the same trace, and the shorter one was
> read as the whole day.**

Set `adsb_verified_verdict` = AT_CLAIMED_AIRPORT for OWENS-024 and SITE-003 and rewrite both notes.
Note this also removes an internal contradiction: the neighbouring page
`overlap/20240403_KS_lawrence/overview.mdx` already says "the jet really did leave the state the morning
he spoke" — the trace proves that page right and the Wichita page wrong.

**OWENS-012 — SU-BTT, 14 April 2023, claimed Wichita (KICT).**
Page: `site/docs/Planes/following/overlap/20230414_KS_wichita_owens_012/overview.mdx`, lines 206 and 250.

Currently published:
> **Refuted.** … the track begins at Paris–Charles de Gaulle (5.39 km) and ends near Sunset Strip
> Airpark, Topeka, Kansas (10.98 km) — roughly **215 km from Wichita**. Both archives hold the same
> trace. … the measured closest approach to KICT reads **7,411.49 km**.

Three errors. The 7,411 km figure is the distance at the *first fix of the day* (Paris). "Both archives
hold the same trace" is false. And the aircraft got far closer than 215 km:

| Source | Fixes | Last fix | Closest to KICT |
|---|---:|---|---:|
| adsb.lol | 505 | 17:58:13Z, 30,025 ft | 224.5 km |
| airplanes.live | 787 | **18:18:17Z, 5,050 ft (3,717 AGL)** | **27.6 km** |

The airplanes.live trace continues 20 minutes further and shows a continuous descent inbound from Paris,
distance to Wichita falling monotonically (39.7 → 27.6 km) while altitude falls 6,325 → 5,050 ft.
Coverage ends on that descent.

Exact correction: replace with
> **Consistent, not proven, and not refuted.** Inbound from Paris–Charles de Gaulle, the airplanes.live
> trace ends at 18:18:17 UTC on a steady descent **27.6 km from Wichita at 5,050 ft — about 3,700 ft
> above the field — and still closing.** Touchdown is not in the trace. The adsb.lol trace for the same
> day stops twenty minutes earlier at 224 km, which is where an earlier reading of this row got "215 km
> short of Wichita" from. The aircraft was descending into the Wichita area; whether it landed at KICT
> or another field nearby is not shown.

Set `adsb_verified_verdict` = CONSISTENT_NOT_PROVEN.

**OWENS-015 — SU-BND, 9 May 2023, claimed "St. Louis then Goose Bay" (CYYR).**
Currently: "REFUTED. … was somewhere else … Closest approach to CYYR was 3,057 km." The same-day trace
departs **KCPS St. Louis Downtown at 20:02Z** — which confirms the St. Louis half of the row — and ends
over La Tuque, Quebec at 22:10Z, FL410, north-eastbound, 1,063 km from Goose Bay. The next trace picks
the aircraft up over Ireland at 04:18Z on 10 May. A Goose Bay fuel stop fits that gap exactly and is
neither shown nor excluded. Correction: **half confirmed, half untested — not refuted.**

### 2.3 Published as "Refuted" on the evidence of a different day. SIX ROWS.

Ten rows carry an `adsb_verified_note` that cites a date other than the claimed date. Six of those are
labelled **REFUTED**. In every one of the six, the trace is a short local Egyptian sector on the adjacent
day, and the claim is **physically compatible** with it:

| Row | Claim | Note actually uses | Distance | Time available vs. needed |
|---|---|---|---:|---|
| OWENS-016 | SU-BND, Provo, 12 Jun 2023 | 11 Jun (Cairo, ends 09:16Z) | 11,330 km | 38.7 h vs 14.2 h |
| OWENS-030 | SU-BND, Provo, 8 Dec 2024 | 7 Dec (Cairo, ends 17:48Z) | 11,431 km | 30.2 h vs 14.3 h |
| OWENS-052 | SU-BND, Wilmington, 25 Jun 2023 | 24 Jun (Cairo, ends 08:27Z) | 9,228 km | 39.5 h vs 11.5 h |
| OWENS-028 | SU-BTT, Omaha, 20 Jul 2024 | 21 Jul (Cairo, begins 06:33Z) | 10,405 km | 30.7 h vs 13.1 h |
| OWENS-029 | SU-BTT, Omaha, 17 Aug 2024 | 18 Aug (Cairo, begins 09:36Z) | 10,402 km | 33.6 h vs 13.0 h |
| OWENS-055 | SU-BTT, Omaha, 15 Apr 2024 | 16 Apr (Cairo, begins 16:42Z) | 10,400 km | 40.7 h vs 13.0 h |

"Time needed" is straight-line distance at 800 km/h cruise, before any fuel stop — a floor, not an
estimate. Every one of the six leaves hours to spare. **None of them is refuted.** Each should read
NOT TESTED, with the adjacent-day observation kept as context, not as a refutation.

The OWENS-028 page already does this correctly in its body text ("the refutation rests on the adjacent
day … this row is refuted by the day after it, not by the day itself") while still leading with the word
**Refuted**. The lead is the part a reader carries away. Change the lead on all six.

### 2.4 Right metro, wrong airport — a mislabel the CSV records as a confirmation

**OWENS-010 — SU-BTT, 1 April 2023, claimed St. Louis Lambert (KSTL).** Verdict AT_CLAIMED_AIRPORT,
closest approach 0.48 km. The 0.48 km happened **at 3,975 ft baro — 3,357 ft above the field — en route
overhead.** The trace then continues away from Lambert and ends on final approach to a *different*
airport: 2.2 km from **KSUS (Spirit of St. Louis, Chesterfield MO)** at 600 ft, descending, having moved
to 24 km from KSTL. Four independent sources — adsb.lol, airplanes.live, the adsb.lol GitHub backup and
the ADS-B Exchange monthly sample — agree fix for fix.

The aircraft arrived in the St. Louis metro. It did not land at the claimed field. Correction: change
"at the claimed airport" to **"arrived at Spirit of St. Louis (KSUS), 24 km from the claimed Lambert
(KSTL)"**, and note that a 0.48 km closest approach at 3,357 ft AGL is an overflight, not a landing.

**SITE-001 — SU-BTT/SU-BND, 2 April 2023, claimed KSTL/KCPS/KSUS.** Verdict AT_CLAIMED_AIRPORT, note
dated 1 April. **No trace exists for 2 April 2023 for either tail** — both archives were asked and held
nothing. This row's confirmation is borrowed entirely from OWENS-010's day, and OWENS-010's day is
itself a KSUS arrival, not a KSTL one. Change to NOT TESTED.

---

## 3. Claims the recovered data now CONFIRMS with primary position data

These move from "a screenshot of somebody's tracker" to "a position report from a volunteer receiver
network, held by two independent archives". Every one below is corroborated by **both** adsb.lol and
airplanes.live unless stated.

### 3.1 On-ground fix within 3 km of the claimed field, on the claimed day

| Row | Date | Tail | Field | Closest ground fix |
|---|---|---|---|---:|
| OWENS-013 | 2023-04-20 | SU-BTT | KILG Wilmington DE | 0.56 km |
| OWENS-025 | 2024-04-19 | SU-BND | KPVU Provo | 0.02 km |
| OWENS-026 / SITE-004 | 2024-04-23 | SU-BTT | KPVU Provo | 0.00 km |
| OWENS-035 / OWENS-065 | 2025-05-23 | SU-BND | KPVU Provo | 0.03 km |
| OWENS-040 | 2025-09-04 | SU-BTT | KPVU Provo | 0.16 km |
| OWENS-041 / SITE-006 | 2025-09-10 | SU-BTT | KPVU Provo | 0.03 km |
| EXTRA-006 | 2025-09-10 | SU-BND | KPVU Provo | 1.29 km (the parking stand) |

OWENS-035/OWENS-065 and OWENS-026/SITE-004 are the same events entered twice; the site already says so.

### 3.2 Departure roll or approach at the claimed field, no on-ground flag in the archive

Negative AGL below is barometric altitude reading under field elevation — an aircraft on the surface.

| Row | Date | Tail | Field | Closest | AGL |
|---|---|---|---|---:|---:|
| OWENS-024 / SITE-003 | 2024-04-03 | SU-BTT | KICT | 1.43 km | +342 ft (departure) |
| OWENS-011 | 2023-04-06 | SU-BTT | KILG | 1.63 km | −105 ft |
| OWENS-021 | 2024-02-14 | SU-BTT | KILG | 0.82 km | −180 ft |
| OWENS-027 | 2024-04-28 | SU-BTT | KILG | 1.56 km | −80 ft |
| SITE-005 | 2025-09-10 | SU-BTT | KILG | 1.75 km | −105 ft |
| OWENS-046 | 2023-02-25 | SU-BTT | KSUS | 2.22 km | −113 ft |
| OWENS-020 | 2024-02-09 | SU-BTT | KOMA | 0.31 km | +366 ft |
| OWENS-039 | 2025-08-17 | SU-BTT | KOMA | 0.50 km | +391 ft |
| OWENS-038 | 2025-07-20 | SU-BTT | KOMA | 1.33 km | +591 ft |
| OWENS-023 | 2024-03-29 | SU-BTT | KICT | 1.83 km | +267 ft |
| OWENS-042 | 2025-09-13 | SU-BND | KPVU | 0.62 km | +3 ft (departure) |
| OWENS-014 | 2023-05-03 | SU-BND | KCPS | 2.07 km | +1,137 ft |

Two of these carry a caveat the site should keep visible. **OWENS-020 (9 Feb 2024)** shows SU-BTT 0.31 km
from Omaha at 366 ft AGL and then an on-ground fix at **Lincoln (KLNK), 88 km away** — an approach at one
field and a landing at another, in the same visit. **OWENS-038 / OWENS-067 (20 Jul 2025)** are the same
arrival: 1.33 km from Omaha at 591 ft, then 7.2 km from Lincoln at 881 ft. Whichever field it used, the
Omaha and Lincoln rows are one event, not two.

### 3.3 Confirms the aircraft only

Every row above locates an aircraft. **None of them places Charlie Kirk, Erika Kirk, or any person on
board.** Erika Kirk's itinerary is not published anywhere and no archive produces it. The site's existing
"CONFIRMS THE AIRCRAFT ONLY, NOT THE OVERLAP" wording is the right wording and must stay on every one.

---

## 4. The marquee claim, checked from the raw files

**Claim: SU-BND on the ground at KPVU on six consecutive days, 5–10 September 2025, and SU-BTT at KPVU
on 10 September 2025.**

All files opened directly. Provenance: both archives returned HTTP 200 on 2026-08-24; URLs are
`https://adsb.lol/globe_history/2025/09/DD/traces/3e/trace_full_01003e.json` and
`https://globe.airplanes.live/globe_history/2025/09/DD/traces/3e/trace_full_01003e.json`
(SU-BND, ICAO 01003E) and `…/d3/trace_full_0101d3.json` (SU-BTT, ICAO 0101D3).

KPVU reference point 40.218894, −111.722445, elevation 4,497 ft. Runway 13 threshold 40.230202,
−111.732002.

### 4.1 SU-BND — VERDICT: CONFIRMED, and stronger than "six days"

| UTC day | Ground fixes at KPVU | Recorded ground window(s) | Span of recorded ground time | Airborne fixes |
|---|---:|---|---:|---:|
| 04 Sep | — | **no trace; both archives asked, both empty** | — | — |
| 05 Sep | 244 | 18:05:32–18:05:43, 19:14:15–19:22:49, 22:53:06–23:49:20 | 1.08 h | 676 (the 1 h 08 sortie) |
| 06 Sep | 138 | 19:18:00–20:02:38 | 0.74 h | **0** |
| 07 Sep | 244 | 16:31:39–18:13:37 | 1.70 h | **0** |
| 08 Sep | 168 | 18:49:05–19:23:54, 20:01:23–20:08:45 | 0.70 h | **0** |
| 09 Sep | 124 | 20:03:30–20:38:55 | 0.59 h | **0** |
| 10 Sep | 327 | 16:05:35–17:34:09, 19:40:53–20:29:38 | 2.29 h | 1, at 28 ft AGL |
| 11 Sep | — | **no trace; both archives asked, both empty** | — | — |
| 12 Sep | 708 | 13:37:35–16:48:52, 19:03:36–19:20:23, 20:29:23–22:17:03 | 5.26 h | **0** |
| 13 Sep | 0 | departs | — | 1,093 (18:57:40 → eastbound, FL410) |

**Read the "ground time" column correctly, and say so on the page.** It is the span of *recorded* ground
fixes, not time on the ground. A parked aircraft is heard intermittently. The number that actually
carries the claim is the position:

- Median stand position 06–12 Sep: **40.22982, −111.72768** — identical to five decimal places on every
  one of those days, in both archives. 1,293 m from the airport reference point, **369 m from the
  runway 13 threshold**.
- Intra-day spread of the ground fixes: 5 m (6 Sep), 29 m (7 Sep), 6 m (8 Sep), 4 m (9 Sep), 6 m
  (10 Sep), 24 m (12 Sep). That is GPS jitter on a stationary airframe.
- 5 Sep spread is 1,526 m because that day contains the arrival taxi and the round-robin.
- **Zero airborne fixes on 6, 7, 8, 9 and 12 September.** The single airborne fix on 10 September is at
  4,525 ft baro = 28 ft above the field — a mode artefact at the stand, not a flight.

So the honest and stronger statement is not "on the ground six consecutive days" but **"parked on one
spot 369 m from the runway 13 threshold, with no flight recorded, from the afternoon of 5 September to
the afternoon of 12 September."**

**Two things that weaken or complicate it, and belong on the page at the same size:**

1. **5 September was not a stationary day.** SU-BND flew a Provo→Provo round-robin, airborne 18:06:12Z,
   back down 19:14:00Z — 1 h 08 — with a maximum recorded altitude of **45,025 ft**, the certified
   ceiling of a Gulfstream IV-SP. My raw read matches the SU-BND page's existing figures to the second.
   A climb straight to the ceiling and home is the shape of a post-maintenance certification check.
2. **11 September is a hole.** Both archives were asked and held nothing for SU-BND, while the *same
   archives on the same day* returned a full 2,518-fix trace for SU-BTT. So it was not an archive
   outage. It is still **not** evidence of anything: a parked aircraft with its transponder off produces
   exactly this, and it is flanked by the identical stand position on 10 and 12 September, which makes
   movement on the 11th implausible rather than impossible. **Do not publish this as suppression** — no
   control aircraft has been probed for that specific tail-day.

**Cross-source agreement — the whole strength of the claim:**

| Day | Shared timestamps | Max position separation between adsb.lol and airplanes.live |
|---|---:|---:|
| 05 Sep | 155 | 5.1 m |
| 06 Sep | 97 | 0.0 m |
| 07 Sep | 125 | 0.0 m |
| 08 Sep | 145 | 0.0 m |
| 09 Sep | 88 | 0.0 m |
| 10 Sep | 143 | 0.8 m |
| 12 Sep | 384 | 0.0 m |

The two archives agree to the metre. **Be careful how this is described.** adsb.lol and airplanes.live are
two independent volunteer networks, but they can share contributing feeders, so byte-identical positions
are evidence that neither archive altered the record — not two fully independent observations of the
aircraft. Say "two independent archives hold the same record", not "two independent measurements".

### 4.2 SU-BTT on 10 September — CONFIRMED, and it corrects the popular reading

| Time (UTC) | Local (MDT) | Event |
|---|---|---|
| 04 Sep 07:12 | — | departs Paris-Le Bourget |
| 04 Sep 16:03 | — | ground fix at Minot, ND (KMOT) |
| 04 Sep 18:45:52–18:54:07 | 12:45–12:54 | **on the ground at KPVU, 8 min 15 s**, 0.16 km from the field |
| 05–09 Sep | | **no trace at all; both archives asked, both empty, every day** |
| 10 Sep 13:07:53 | **07:07** | trace opens with the aircraft **already on the ground at KPVU** |
| 10 Sep 13:13:16 | **07:13** | last ground fix — departs |
| 10 Sep 13:14:40 | 07:14 | 6,075 ft, climbing out |
| 10 Sep 13:34 – 16:15 | | cruise FL410, Utah → Colorado → Nebraska → Iowa → Illinois → Indiana → Ohio → Pennsylvania |
| 10 Sep 16:50:37 | 10:50 | **on the surface at Wilmington DE (KILG)**, −25 ft baro, 1.7 km from the field |
| **10 Sep 18:23:30** | **12:23:30** | **Charlie Kirk is shot at UVU, Orem** |
| 11 Sep 11:55:35 | | ground fix at KILG, departs 11:59 |
| 11 Sep 21:35 | | descending into Almaza Air Force Base, Cairo (HEAZ) |

**SU-BTT was not at Provo when Charlie Kirk was shot.** It left Provo five hours and ten minutes before
the shot and was on the ground in Delaware one hour and thirty-three minutes before it, and it left the
United States the following morning. The 10 September Provo contact is real and is confirmed by primary
data — the aircraft's own ground fixes, 1.4 km from the field, agreeing between the two archives to
2.0 m over 48 shared timestamps — but the claim as it is usually told, of an Egyptian jet at Provo at the
moment of the killing, applies to **SU-BND**, which never moved, and not to SU-BTT.

Note also that the trace *opens* with SU-BTT already on the ground. The 5 minutes 23 seconds of recorded
ground time is a floor and nothing else: the archive holds no data for 5–9 September, so how long the
aircraft had been at Provo before 13:07:53Z on the 10th is **not known from ADS-B**.

The site page `following/speaking/20250910_orem.mdx` already states this correctly — "SU-BTT departed
Provo (~7 mi) that morning; SU-BND sat at Provo with its transponder on and never took off." That
sentence is now backed by primary position data and should be the sentence every other page copies.

### 4.3 What none of this shows

No trace places any person aboard either aircraft. Nothing here shows why either aircraft was at Provo.
KPVU hosts a Duncan Aviation facility; a long-term maintenance stay produces exactly the stationary
signature in 4.1, and the SU-BND page's own maintenance counter-reading is not weakened by anything
above — a 113-day stay with two flights, one of them a climb to the certified ceiling, fits a heavy check
at least as well as anything else.

---

## 5. Systemic defects found in the existing verification pass

1. **Closest approach was computed on the wrong trace, or on one fix.** OWENS-012 reports 7,411 km (the
   first fix of the day) when the day's minimum is 27.6 km. OWENS-024 reports 1,853 km from a trace that
   starts after the aircraft left the claimed state. **Any claim of "closest approach" must be a minimum
   over all fixes in all sources for that day**, and the CSV should record which source produced it.
2. **"Both archives agree" is asserted where they do not.** On 3 April 2024 and 14 April 2023, adsb.lol
   and airplanes.live hold materially different amounts of the day. airplanes.live is routinely the
   larger of the two (e.g. 787 vs 505 fixes; 1,789 vs 1,229; 2,518 vs 1,399). Where only one archive
   covers the decisive part of the day, say which one.
3. **Ten rows are verdicted on the wrong date, six of them as "Refuted".** A claim about day D can only
   be refuted by day D.
4. **A closest approach at altitude is being read as a landing.** OWENS-010: 0.48 km from KSTL at 3,357 ft
   AGL, while the aircraft actually landed 24 km away at KSUS. Distance without altitude is not a
   landing record — the module `lib/geo.py` says exactly this in its own docstring.
5. **NOT_HEARD and NO_ARCHIVE_COVERAGE are mixed.** 12 rows carry one label where the miss records on
   disk support the other. Asked-and-empty is a coverage fact; never-asked is an open question.
6. **Duplicate rows.** OWENS-035/OWENS-065, OWENS-026/SITE-004, OWENS-041/SITE-006, OWENS-024/SITE-003,
   OWENS-031/OWENS-061 (same tail, same date, same field) inflate the tally without adding an event.

---

## 6. Files written

- `claims_audit.csv` — one row per overlap claim, 24 columns, including `my_verdict`, `agrees`,
  `note_cites_date`, `note_uses_wrong_day`, `correction_action`, `closest_km`, `closest_agl`,
  `ground_at_claimed`, and a per-source `detail` string.
- `claims_audit.json` — the same, structured.
- `marquee_kpvu.txt`, `marquee_detail.txt`, `subtt_sept10.txt`, `subnd_sept05.txt` — the raw
  September 2025 verification output.
- `adjacent_day_feasibility.txt` — the six wrong-day refutations with distances and time budgets.
- `date_mismatch.txt` — the ten rows whose note cites a different date.
- `audit2.py`, `finalize.py` — the code, re-runnable.
