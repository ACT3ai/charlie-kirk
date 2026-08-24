---
displayed_sidebar: docs
slug: /Planes/following/overlap/20240322_KS_wichita_owens_054/data/MISSING_DATA
title: "ADS-B gaps for overlap 20240322_KS_wichita_owens_054"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20240322_KS_wichita_owens_054 (22 March 2024 — Wichita, KS)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20240322_KS_wichita_owens_054"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.121Z by
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
| SU-BTT | 2024-03-21 | 404 | overlap OWENS-054 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-03-22 | 404 | overlap OWENS-054 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-03-23 | 404 | overlap OWENS-054 - Wichita KS (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

Four days after the last Wichita row the result is identical — covered dates, no [SU-BTT](/Planes/SU-BTT/overview) trace in either [free archive](/Planes/following/apis/public_open_source/knowledge) — which keeps [OWENS-054](/Planes/following/overlap/20240322_KS_wichita_owens_054/overview) untested in the [overlap index](/Planes/following/overlap/overview) rather than counted as a hit or a miss against the [Wichita record](/Planes/following/Wichita_KICT_2022-11-13_to_2025-08-03/overview). Two near-identical rows four days apart also raise a duplication question the tally never answers, and duplicate counting is exactly the sort of methodological problem that turned a broadcast number into [press coverage](/Media/overview), then into [arguments about foreign involvement](/Israel_Main_Suspect/overview), then into [proposed federal law](/laws/US_Intel/Law_2_US_Intel). Read [the 73 overlaps](/Planes/following/73_overlaps): it reconstructs the whole spreadsheet row by row, and it is where the 73, 72, 70-plus, 68 and 77 versions of the same figure are finally lined up against each other.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [The 73 overlaps, row by row](/Planes/following/73_overlaps)
* [X discussions of the following planes](/Planes/following/x_discussions)
* [Media coverage analysis](/Media/overview)

</div>
<div>

* [Israel main suspect](/Israel_Main_Suspect/overview)
* [Law 2 — intelligence disclosure](/laws/US_Intel/Law_2_US_Intel)
* [Influencers and citizen researchers](/Influencers/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
