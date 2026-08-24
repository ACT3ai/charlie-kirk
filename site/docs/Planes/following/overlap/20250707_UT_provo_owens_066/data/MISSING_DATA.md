---
displayed_sidebar: docs
slug: /Planes/following/overlap/20250707_UT_provo_owens_066/data/MISSING_DATA
title: "ADS-B gaps for overlap 20250707_UT_provo_owens_066"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20250707_UT_provo_owens_066 (7 July 2025 — Provo, UT)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20250707_UT_provo_owens_066"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.113Z by
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
| SU-BND | 2025-07-06 | 404 | overlap OWENS-037 - Provo UT (audited_inaccurate, audit: inaccurate); overlap OWENS-066 - Provo UT (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2025-07-07 | 404 | overlap OWENS-037 - Provo UT (audited_inaccurate, audit: inaccurate); overlap OWENS-066 - Provo UT (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2025-07-08 | 404 | overlap OWENS-037 - Provo UT (audited_inaccurate, audit: inaccurate); overlap OWENS-066 - Provo UT (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

The archive misses recorded here belong to [OWENS-066](/Planes/following/overlap/20250707_UT_provo_owens_066/overview), which is the same 7 July 2025 [Provo](/Planes/following/Provo_KPVU_2024-04-19_to_2025-09-13/overview) claim as [OWENS-037](/Planes/following/overlap/20250707_UT_provo_owens_037/overview) — one claim, two rows in the [register](/Planes/following/overlap/overview), and both came back **not heard** for [SU-BND](/Planes/SU-BND/overview). Nothing about an empty lookup implies concealment; a parked airframe with its transponder off produces exactly this, and readers who want documented cases of records genuinely going missing should look at the human side of the file instead — [the witness reportedly asked to delete his 4K footage](/Suspicious/FBI/simmons-video-deletion), or [the county's answer that no bodycam footage existed](/court/mirandize/bodycam-grama-no-footage). For the mechanics, [open flight data](/Planes/following/apis/public_open_source/knowledge) sets out which free sources hold history and which hold only live positions — the reason a 2022 claim on this sheet can never be tested the way a 2025 one was.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Commercial APIs and what they would settle](/Planes/following/apis/proprietary/knowledge)
* [Government flight records and FOIA routes](/Planes/following/apis/government/knowledge)
* [Reported FBI pressure on a witness](/Legal/FBI-Witness-Intimidation)

</div>
<div>

* [Media censorship of the investigation](/Media/Censorship)
* [Eyewitness and mobile phone video](/cameras/Eyewitness_Mobile_Video)
* [Actions that would force disclosure](/Your_Actions_Fix_It/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
