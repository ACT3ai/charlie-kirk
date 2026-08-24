---
displayed_sidebar: docs
slug: /Planes/following/overlap/20240817_NE_omaha_lincoln_owens_029/data/MISSING_DATA
title: "ADS-B gaps for overlap 20240817_NE_omaha_lincoln_owens_029"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20240817_NE_omaha_lincoln_owens_029 (17 August 2024 — Omaha / Lincoln, NE)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20240817_NE_omaha_lincoln_owens_029"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.122Z by
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
| SU-BTT | 2024-08-16 | 404 | overlap OWENS-029 - Omaha / Lincoln NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-08-17 | 404 | overlap OWENS-029 - Omaha / Lincoln NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-08-18 | 404 | overlap OWENS-029 - Omaha / Lincoln NE (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

These lookups belong to [row OWENS-029](/Planes/following/overlap/20240817_NE_omaha_lincoln_owens_029/overview), which the audit calls a year-shifted copy of a real August 2025 rotation, so the archive was queried for a date the aircraft was almost certainly not flying, and the resulting silence is [a coverage fact and nothing more](/Planes/Flight-Data-Recovery/What-A-403-Means), best read alongside [the Lincoln field record](/Planes/following/Lincoln_KLNK_2024-02-09_to_2025-10-11/overview). The distinction matters far beyond aircraft, because this case is full of claims where absence was read as proof, from [a body camera that stopped recording on the roof](/Law_Enforcement/officer-bagley-bodycam) to [footage a county says it searched for and could not find](/court/mirandize/bodycam-grama-no-footage), and the discipline separating a missing record from a destroyed one has to be applied identically to [the flight archives](/Planes/Flight-Data-Recovery/overview) and to [the cover-up claims](/CoverUp/overview). The real August rotation is on [17 August 2025, Omaha and Lincoln](/Planes/following/overlap/20250817_NE_omaha_lincoln_owens_039/overview), audited partially accurate, which is the more interesting verdict of the two because a partial hit is where the compilers' method and the primary record actually disagree, and it sits inside [the same overlap index](/Planes/following/overlap/overview) tested by [the same two free archives](/Planes/following/apis/public_open_source/knowledge).

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Officer Bagley's body camera on the roof](/Law_Enforcement/officer-bagley-bodycam)
* [Missing bodycam and the GRAMA admission](/court/mirandize/bodycam-grama-no-footage)
* [Cover-up claims index](/CoverUp/overview)

</div>
<div>

* [Law enforcement outside the FBI](/Law_Enforcement/overview)
* [17 August 2025, the real rotation](/Planes/following/overlap/20250817_NE_omaha_lincoln_owens_039/overview)
* [Court and trial record](/court/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
