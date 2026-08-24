---
displayed_sidebar: docs
slug: /Planes/following/overlap/20240214_DE_wilmington_owens_021/data/MISSING_DATA
title: "ADS-B gaps for overlap 20240214_DE_wilmington_owens_021"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20240214_DE_wilmington_owens_021 (14 February 2024 — Wilmington, DE)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20240214_DE_wilmington_owens_021"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.120Z by
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
| SU-BTT | 2024-02-13 | 404 | overlap OWENS-021 - Wilmington DE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-02-15 | 404 | overlap OWENS-021 - Wilmington DE (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

The two 404s here sit beside one of the run's more awkward results: free ADS-B confirms [OWENS-021](/Planes/following/overlap/20240214_DE_wilmington_owens_021/overview) — [SU-BTT](/Planes/SU-BTT/overview) 0.82 km from [Wilmington](/Planes/following/Wilmington_KILG_2022-11-17_to_2025-10-12/overview) on 14 February 2024, inbound from [Lincoln](/Planes/following/Lincoln_KLNK_2024-02-09_to_2025-10-11/overview) — while the paid-archive audit had called the row inaccurate. Publishing the disagreement instead of choosing a winner is the rule here, and it is the same rule governing contested ground elsewhere: the [ATF fragment that could neither be identified nor excluded](/Gun_Bullet/ATF_Fragment_Inconclusive), the [witness accounts that do not match](/Witnesses/overview), the [conflicting Miranda timings](/Tyler_Robinson/Surrender). For the method, read [flight data recovery](/Planes/Flight-Data-Recovery/overview): two independent routes on the same aircraft-day agreed to the second on first contact, and where two routes disagree the disagreement itself is what gets published.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Flight data recovery — the method](/Planes/Flight-Data-Recovery/overview)
* [Wilmington, outbound only](/Planes/following/Wilmington_KILG_2022-11-17_to_2025-10-12/overview)
* [ATF fragment — inconclusive match](/Gun_Bullet/ATF_Fragment_Inconclusive)

</div>
<div>

* [Witness accounts that conflict](/Witnesses/overview)
* [Tyler Robinson's surrender timeline](/Tyler_Robinson/Surrender)
* [Evidence contradictions in the case](/Other/Evidence-Contradictions)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
