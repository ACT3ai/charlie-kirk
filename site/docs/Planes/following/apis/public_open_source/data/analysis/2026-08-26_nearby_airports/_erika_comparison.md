# The Erika Comparison, and the Post-Death Record

Strand report. Read-only analysis of existing data. No fetches, no site edits.
Generated 2026-08-26 from `tpusa_events.csv`, `speaking/_airports_near_summary.csv`,
`speaking/*.yaml`, and `apis/public_open_source/data/recovery/trace_visit_index.json`
plus the raw traces under `site/docs/Planes/<TAIL>/data/recovered/`.

---

## HEADLINE

**Hypothesis 3 cannot be tested, and the post-death record cuts against the whole
"following Charlie" framing.**

There is exactly **one** Erika-only event and **one** joint event in the entire
139-event catalog. The comparison Bryan wants has no sample. Meanwhile SU-BND was
at Provo on **five separate days in May and June 2026** — nine months after Charlie
Kirk was killed — flying a sortie profile that matches the September 2025 one almost
exactly. And the September 5 2025 flight that this site currently calls "the single
flight on this page that nobody has adequately explained" **is now explained**: we
hold the raw track, and it is a climb to FL450 and back.

---

## 1. The split by attendee_class — and why the comparison dies here

From `tpusa_events.csv`, all 139 rows:

| attendee_class | n | date range |
|---|---|---|
| CHARLIE_ONLY | **113** | 2022-01-04 → 2025-09-10 |
| TPUSA_NO_KIRK | **24** | 2022-10-03 → 2025-10-29 |
| CHARLIE_AND_ERIKA | **1** | 2025-06-13→15, Young Women's Leadership Summit, Grapevine TX (KDFW) |
| ERIKA_ONLY | **1** | 2025-09-21, Charlie Kirk stadium memorial, Glendale AZ (KGEU) |

`erika_present == yes` on exactly those two rows. 113 rows say `not_documented`
and 13 say `unknown`.

**The Erika sample is n=1 solo event, and that one event is her husband's memorial
service.** It is not a speaking tour stop. It is a single, publicly announced,
one-off event eleven days after the assassination. Even if it produced a clean
result it would not generalise to "how the aircraft behaved around Erika Kirk
2022–2025", which is what the 68/70/72/73 tallies claim to be about.

The 24 TPUSA_NO_KIRK rows split into two genuinely different populations, and this
turns out to matter more than the Erika rows do:

* **11 pre-death** (2022-10 → 2024-03) — mostly Candace Owens *Live Free Tour* stops.
* **13 post-death** (2025-09-11 → 2025-10-29) — the resumed *Turning Point Tour*.

That second group is the closest thing this dataset has to a **natural control**:
same organisation, same tour format, same venues class, Charlie Kirk absent because
he is dead.

---

## 2. Presence rate by class, normalised by archive coverage

Two hits exist in the entire catalog. Both are Utah. Both are Provo.

| slug | class | airport | result |
|---|---|---|---|
| `20250910_orem` | CHARLIE_ONLY | KPVU | **`su_found_in_radius = yes`** — 5 SU ground contacts, 3 claimed overlaps |
| `20240423_salt_lake_city` | CHARLIE_ONLY | KSLC | **`su_just_outside_radius = 3`** — SU-BND;SU-BTT at Provo, 45 mi from the SLC 40-mile ring |

**137 of 139 events have no foreign-fleet aircraft anywhere near them.**

Coverage-normalised. "Effective covered events" = Σ (per-event
`coverage_pct_following_fleet` / 100). It converts sparse aircraft-day coverage into
the number of events we would have seen *completely*.

| group | n | in-radius hits | ac-days needed | held | held % | effective covered events |
|---|---|---|---|---|---|---|
| CHARLIE_ONLY | 113 | **1** | 9,825 | 1,589 | 16.2% | **9.36** |
| TPUSA no Kirk, PRE-death | 11 | 0 | 825 | 84 | 10.2% | 0.47 |
| TPUSA no Kirk, POST-death | 13 | 0 | 990 | 278 | **28.1%** | **2.67** |
| CHARLIE_AND_ERIKA | 1 | 0 | 105 | 25 | 23.8% | 0.14 |
| ERIKA_ONLY | 1 | 0 | 75 | 23 | 30.7% | 0.30 |

Charlie's coverage-normalised in-radius rate is **1 / 9.36 = 0.107**.

### The power calculation — this is the whole answer to hypothesis 3

If the aircraft followed Erika *exactly as much as* they followed Charlie, what is
the chance we would still observe zero hits?

| group | effective covered events | expected hits at Charlie's rate | **P(observe 0 anyway)** |
|---|---|---|---|
| ERIKA_ONLY | 0.30 | 0.032 | **96.7%** |
| CHARLIE_AND_ERIKA | 0.14 | 0.015 | **98.4%** |
| **Erika combined** | **0.44** | **0.047** | **95.2%** |
| TPUSA post-death | 2.67 | 0.285 | 74.0% |
| TPUSA pre-death | 0.47 | 0.050 | 94.8% |

**Zero Erika hits is what you get 95% of the time even under the hypothesis that the
following is real and identical for both Kirks.** The observation carries essentially
no information. This is a *cannot test*, not a *contradicted* and emphatically not a
*confirmed*.

> **VERDICT ON HYPOTHESIS 3: CANNOT TEST.** The Erika sample is one memorial service.
> Reporting "the nearby-airport behaviour did not happen around Erika" as a finding
> would be manufacturing a contrast out of a sample of one.

### The selection effect that must be stated with the table

Coverage is not evenly distributed, and it is **highest where we went looking**:

* Utah events: mean following-fleet coverage **14.5%** (n=3)
* Everywhere else: mean **9.2%** (n=136)
* The single hit, `20250910_orem`: **20.0%** following-fleet, **48.0%** all-tails —
  roughly 2.5x and 6x the site-wide mean.

The recovery sweep concentrated on the dates and places the claim already pointed at.
So "the only hit is at Provo on September 10" is partly a statement about where the
archive was interrogated hardest. It does not make the hit false. It does mean the
1-in-139 ratio is **not** a clean base rate.

### What the fleet was actually doing on the one Erika date

2025-09-21, the Glendale AZ memorial. We hold traces for three of the six foreign tails:

* **SU-BND** — 80 points, lat 30.7–31.4 N, lon 29.7–30.7 E. **Nile Delta, Egypt.**
* **SU-BTT** — 64 points, lat 29.0–30.8 N, lon 30.6–32.9 E. **Egypt.**
* **T7-ELL** — on the ground at **OMDW, Dubai World Central.**

Not one foreign-fleet aircraft was on the North American continent that day.
**That is one data point, from one event, and it is an anecdote — not a test.**
It is recorded because it is the only direct observation the Erika question has.

---

## 3. THE POST-DEATH RECORD — the strongest innocent explanation in the case

### 3a. What the traces show

SU-BND, ICAO hex `01003E`, Gulfstream IV-SP, at **KPVU (Provo Municipal)**:

| date | source | ground points | UTC window | position |
|---|---|---|---|---|
| 2026-05-13 | airplanes-live | 42 | 23:12:54–23:59:05 | 40.22968, -111.72755 |
| 2026-05-14 | airplanes-live | 1 | 00:00:14 | 40.22968, -111.72755 |
| 2026-05-20 | airplanes-live | 1,019 | 13:46:33–18:14:01 | 40.20894, -111.72333 |
| 2026-06-02 | airplanes-live | 9 + 160 | 17:04:34–17:06:38, 18:15:58–18:23:59 | 40.23040 / 40.22651 |
| 2026-06-04 | airplanes-live | 168 | 21:16:57–22:12:34 | 40.22725, -111.72828 |

**Charlie Kirk was killed on 10 September 2025. These are eight and nine months later.**

**Coverage caveat, stated plainly.** Only **six** days in 2026 were queried for
SU-BND at all, and all six returned payloads — there are **zero** `.miss` records for
this tail in 2026. Five of those six days put it at Provo; the sixth (2026-07-01,
from the adsbexchange monthly sample) puts it at HEAZ, Almaza AFB, Cairo. So the
honest sentence is **"on five of the six days in 2026 that anyone asked about, SU-BND
was at Provo"** — not "SU-BND visited Provo five times in 2026." The sampling was
opportunistic, not systematic. The denominator is tiny and it is not random.

### 3b. The sortie profile — and why it settles an open question on this site

I reconstructed the flight profile from the raw `trace_full` files by phase
(ground/air), with distance from KPVU and max barometric altitude.
Script: `scratchpad/sortie_profile.py`.

| aircraft-day | profile | max dist from KPVU | max alt |
|---|---|---|---|
| **SU-BGM 2025-04-10** | airborne 53.5 min → **lands KPVU** | 267.5 km | **FL410** |
| **SU-BND 2025-09-05** | KPVU → airborne 67.8 min → **KPVU** | 381.4 km | **FL450** |
| **SU-BND 2026-06-02** | KPVU → airborne 68.8 min → **KPVU** | 333.0 km | **FL410** |
| **SU-BND 2026-06-04** | KPVU → airborne 35.6 min → **KPVU** | 89.1 km | **FL320** |

**The 5 September 2025 sortie and the 2 June 2026 sortie are the same flight, flown
nine months apart, with Charlie Kirk alive for one and dead for the other.**
68.8 vs 67.8 minutes. FL410 vs FL450. 333 vs 381 km. Same field, out and back.

The Provo page (`Provo_KPVU_2024-04-19_to_2025-09-13/overview.mdx`) currently says,
under "the counter to the counterargument":

> "**The 5 September SU-BND sortie.** A 68-minute closed-loop flight by an aircraft
> dormant for three months, five days before the event, has been characterised by one
> analyst as consistent with a corridor mapping run or an electronic sweep. It is also
> consistent with a check flight. **Nobody has published the raw track that would
> distinguish them.**"

**We now hold that raw track, and it distinguishes them.** A corridor-mapping run or
an electronic sweep of Provo / UVU is a *low, local, slow* profile over the target.
This aircraft climbed to **45,025 ft** and went **381 km** from Provo before turning
around. That is a pressurisation-and-systems check to service ceiling — the textbook
post-maintenance functional check flight — and it is not a surveillance profile over
a campus five miles from the field.

That is a result that **weakens** a claim this site has been carrying, and it belongs
on the page at the same prominence as the claim it retires.

### 3c. SU-BND did not fly on 10 September 2025

| date | max dist from KPVU | ground points | verdict |
|---|---|---|---|
| 2025-09-06 | 1.4 km | 138/138 | parked |
| 2025-09-07 | 1.4 km | 244/244 | parked |
| 2025-09-08 | 1.4 km | 168/168 | parked |
| 2025-09-09 | 1.4 km | 124/124 | parked |
| **2025-09-10** | **1.4 km** | **327/328** | **parked** |
| 2025-09-12 | 1.4 km | 708/708 | parked |

On 10 September SU-BND held a **single continuous ground run of 263.7 minutes**,
16:05:35 → 20:29:17 UTC = **10:05 am → 2:29 pm MDT**. Charlie Kirk was shot at
approximately **12:23 pm MDT**. The aircraft was on the ramp, transponder
transmitting, throughout. The one non-ground point in the whole day is a single
sample at 4,525 ft — Provo's field elevation is ~4,500 ft MSL — i.e. a transponder
artefact, not a flight.

And the parking coordinate is **identical to five decimal places** across 6, 7, 8, 9
and 10 September: **40.22982 / -111.72768**. It did not move between stands. The
2026-05-13 position, 40.22968 / -111.72755, is roughly **20 metres** from that same
spot.

> **This corrects a framing that appears in the lead of this workflow's own brief and
> in site prose:** *"2025-09-05, 06, 07, 08, 09, 10 KPVU (six consecutive days ending
> on the day Charlie Kirk was killed)."* Read as six days of presence that is true.
> Read as six days of *activity* it is false. **It is one parked aircraft, mid-stay,
> on the same stand, in a 113-day maintenance stay that began 23 May 2025 and ended
> 13 September 2025.** The only movement in that entire window is the 5 September
> check flight.

### 3d. What is actually at Provo

Already documented in `airports.csv` (KPVU row) and on the Provo page, and the
recovered data now supports it rather than merely coexisting with it:

* **Duncan Aviation operates a full-service MRO on the field** — airframe, engine,
  avionics, paint, interior.
* Duncan has **held the Egyptian Air Force maintenance account since 1999**, under a
  five-year direct contract announced in an October 2015 trade release, in which
  Duncan's own manager notes the EAF *"has chosen to fly over closer maintenance
  companies"* to reach its facilities.
* The hostile line-by-line auditor of the overlap sheet volunteered the same reading
  unprompted: **"ACCURATE POSS BROKEN JET GROUNDED IN PROVO."**

**The 2026 record is the confirmation that was previously unavailable.** Every prior
version of the maintenance argument was an *inference* about intent from a pattern
recorded while Charlie Kirk was alive. The May–June 2026 visits are the same pattern
recorded when he could not be followed. A relationship that survives the death of the
person it was supposedly tracking is a relationship with **the airport**, not with
the person.

**Stated at full strength, as required:** the Provo presence tracks a standing
maintenance relationship between an Egyptian VIP fleet and a maintenance provider on
that field. It predates the assassination by years, it continues after it, and it
explains the dwell times, the closed-loop sorties, the 113-day stay, and the choice
of a regional field with no customs infrastructure — because every one of these
aircraft cleared US customs somewhere else (Minot, Salt Lake City) and reached Provo
on a **domestic** leg.

### 3e. What the post-death record does NOT settle

Fairness runs both ways, and three things survive:

1. **Why Provo rather than Lincoln.** Duncan's main plant is Lincoln, NE (KLNK), and
   this fleet used it three times in 2025 plus Wichita. The 2024–2026 Utah rotations
   are a change nobody has explained. Duncan does operate at Provo; the question is
   why *this* work went there.
2. **The 10 September 07:14 departure of SU-BTT.** The recovered trace confirms it
   — SU-BTT ground at KPVU 13:07–13:13 UTC (07:07–07:13 MDT), then departs the
   region (max 3,060 km). Maintenance explains why it was *at* Provo. It does not
   address the timing.
3. **Occupancy.** No trace anywhere puts a person on any of these aircraft. Not
   Charlie Kirk, not Erika Kirk, not anyone.

### 3f. One claim the recovered data cannot reach

The Provo page lists a **10 June 2025 Provo→Provo flight** with "no duration logged."
There is **no file of any kind** for SU-BND on 2025-06-10 — not a payload, not a
`.miss`. The nearest records are `.miss` files for 2025-06-11 onward.
**That date was never queried.** Per the standing rule this is an *open question*,
not a coverage fact, and it must not be reported as "the archive holds nothing."

---

## 4. Where the existing site already answers this, and where it needs correcting

### Already correct — do not touch

* **`following/Erika_Kirk_Flights.mdx`** already carries the decisive sentence:
  *"Of 139 sourced Turning Point appearances… **exactly one** places her at an event
  before 10 September 2025 with a firm date. Do not treat Charlie Kirk's itinerary as
  a stand-in for hers."* That is exactly the finding of section 1 above, reached
  independently. It also correctly logs the seven irreconcilable tallies (68 / 29-of-68
  / 60+ / ~70 / 72 / 73), Liz Wheeler's same-airport-same-day reduction to **one**, and
  KanekoaTheGreat's 66% aircraft-side error rate.
* **`following/Erika_Tracked_Not_Charlie.mdx`** is properly framed as a record of what
  X accounts posted, not a finding, with the Duncan counterargument present.
* **`following/Erika_Overseas_Overlaps.mdx`** correctly reports that exactly **one**
  dated overseas cell was ever published ("Wichita / DE / potentially Giza",
  20 April 2023) and treats the hole as the finding.
* **`following/Erika_Flight_Log_Invitation.mdx`** and
  **`Erika-Flight-Logs-Erased.mdx`** already carry the retraction of the
  "erased in May 2026" claim, correctly attributed to FR24's blanket 403 on scripted
  clients and its seven-day free tier, with control aircraft named. This is the
  earlier failure handled properly.

### Needs correcting or extending

| # | Page | What it says now | What the recovered data says |
|---|---|---|---|
| **1** | `following/Provo_KPVU_2024-04-19_to_2025-09-13/overview.mdx` — "counter to the counterargument", point 2 | *"Nobody has published the raw track that would distinguish"* check flight from corridor-mapping/electronic sweep | **We hold it.** FL450, 381 km out, 67.8 min, returned to KPVU. Consistent with a functional check flight; **not** consistent with a local sweep. Retire the open question and say why. |
| **2** | Same page — title, scope, and the arrivals table | Window ends **September 2025**; 5 tails, 7 arrivals | **SU-BND returned in May–June 2026** — 5 ground days at KPVU, plus a 2 June closed-loop sortie matching the 5 Sept one to within a minute. The page's date range is now stale and the strongest evidence for its own counterargument is missing from it. |
| **3** | Same page — "In those 113 days, SU-BND flew exactly twice… one on 10 June (no duration logged)" | Implies the 10 June flight is a recorded-but-incomplete event | **2025-06-10 was never queried by the recovery sweep.** No payload, no `.miss`. Mark it as untested, not as a gap in the data. |
| **4** | Any page rendering the September KPVU block as "six consecutive days" of presence | Reads as six days of activity | **One parked aircraft on one stand**, 40.22982/-111.72768 identical across 6–10 Sept; a single 263.7-minute continuous ground run spanning the shooting on 10 Sept. SU-BND **did not fly that day.** |
| **5** | `following/Erika_Kirk_Flights.mdx`, `Erika_Tracked_Not_Charlie.mdx` | The 68/73 tally is unauditable because her itinerary was never published | Still true — **and now quantified.** Add: against 139 sourced events the Erika sample is **n=1 solo + n=1 joint**, effective coverage 0.44 events, and **zero hits is the expected observation 95% of the time even if the following were real.** The tally is not merely unpublished; it is **untestable with the data that exists.** |
| **6** | `Planes/Flight-Data-Recovery/overview.mdx` | Carries the three-way removal/retention/coverage split | Add the Provo 2026 result as a **recovery that weakens a site claim** — the category the charter says must be published as prominently as the confirming ones. |

**None of these are defamation issues.** Every correction moves a claim *toward* the
innocent explanation or *toward* "cannot test." Nothing here adds an allegation about
a living person.

---

## 5. What this strand could not test

* **Hypothesis 3 itself.** n=1. No amount of analysis fixes a sample of one memorial
  service. The only fix is more sourced Erika appearances in `tpusa_events.csv`.
* **Whether anyone was aboard anything.** No trace places Charlie Kirk, Erika Kirk, or
  any named person on any airframe. Erika Kirk's itinerary remains unpublished and no
  backup route produces it.
* **A complete 2026 Provo count.** Six days queried, five hits. Opportunistic sampling.
  A systematic 2026 sweep of SU-BND against airplanes.live would settle whether the
  Provo relationship is continuous or episodic — and it is the single cheapest
  outstanding question in this strand.
* **2025-06-10.** Never asked.
* **Whether the 2026 visits are the *same* maintenance event.** 13 May → 4 June 2026
  is a three-week span consistent with one visit, but the gaps were not queried.
* **Duncan Aviation work orders.** Not public. They would settle most of section 3.
* **The 25 events with `ARCHIVE RETENTION BOUNDARY`** (22 of them CHARLIE_ONLY, mostly
  2022) remain untestable by any free route.
