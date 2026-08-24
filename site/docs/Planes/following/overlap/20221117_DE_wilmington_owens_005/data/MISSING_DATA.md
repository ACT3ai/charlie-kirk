---
displayed_sidebar: docs
slug: /Planes/following/overlap/20221117_DE_wilmington_owens_005/data/MISSING_DATA
title: "ADS-B gaps for overlap 20221117_DE_wilmington_owens_005"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20221117_DE_wilmington_owens_005 (17 November 2022 — Wilmington, DE)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20221117_DE_wilmington_owens_005"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.115Z by
`site/docs/Planes/following/apis/public_open_source/code/pull_all.js`.

**Source tried:** adsb.lol globe history —
`https://adsb.lol/globe_history/YYYY/MM/DD/traces/<hh>/trace_full_<hex>.json`

This is the only free, no-account source of historical ADS-B tracks we have found.
It serves only what its volunteer feeder network actually received.

**WHAT AN EMPTY RESULT DOES AND DOES NOT MEAN.** A 404 here means adsb.lol holds no
trace for that airframe on that UTC day. It does **not** establish that the aircraft
did not fly, and it does **not** establish that a transponder was switched off. The
ordinary explanations come first: the aircraft was parked and silent, it flew outside
volunteer receiver coverage (most of the Atlantic, most of North Africa, much of the
rural US at low altitude), or the claimed date is simply wrong. Several of the rows
below are already recorded in `overlaps.csv` as audited inaccurate.

**The claim is what is listed. The absence is what we found. Neither is proof.**

| Tail | UTC date | HTTP | Why we looked |
|---|---|---|---|
| SU-BTT | 2022-11-16 | 404 | overlap OWENS-005 - Wilmington DE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2022-11-17 | 404 | overlap OWENS-005 - Wilmington DE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2022-11-18 | 404 | overlap OWENS-005 - Wilmington DE (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

Wilmington is the most-visited field in the entire Egyptian fleet record and it appears on the outbound leg only, twenty-one times in three years — [the airport page](/Planes/following/Wilmington_KILG_2022-11-17_to_2025-10-12/overview) makes that case — so the 404s above stop [row OWENS-005](/Planes/following/overlap/20221117_DE_wilmington_owens_005/overview) from ever being tested at exactly the field where a customs-and-fuel stop is being counted as a destination, and the [overlap index](/Planes/following/overlap/overview) carries it that way. That is a scoring problem rather than a data problem, and scoring problems are everywhere in this case: the [disputed 12:23 versus 12:27 impact minute](/Other/Evidence-Contradictions), the [totals that drifted as the story travelled](/Media/overview), the [competing witness accounts of a chest wound versus a neck wound](/Witnesses/overview). Read [what the compilers counted as an overlap](/Planes/following/Overlap_Window_Definition) next — same state, plus or minus three days — which is how [SU-BTT](/Planes/SU-BTT/overview) sitting hundreds of miles away and three days late became one of the seventy-three counted in [the 73 overlaps](/Planes/following/73_overlaps).

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Goose Bay and the aircraft-type split](/Planes/following/GooseBay_CYYR_2023-05-09_to_2025-09-13/overview)
* [Narrative framing in real time](/Narrative/overview)
* [Other topics and cross-cutting leads](/Other/overview)

</div>
<div>

* [Press coverage of the Egyptian-plane claim](/Planes/following/Press_Coverage)
* [Defamation suits and what they can subpoena](/Defamation/overview)
* [How the case timeline was assembled](/Timeline/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
