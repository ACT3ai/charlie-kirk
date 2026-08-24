---
displayed_sidebar: docs
slug: /Planes/following/overlap/20240415_NE_omaha_owens_055/data/MISSING_DATA
title: "ADS-B gaps for overlap 20240415_NE_omaha_owens_055"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20240415_NE_omaha_owens_055 (15 April 2024 — Omaha, NE)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20240415_NE_omaha_owens_055"
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
| SU-BTT | 2024-04-14 | 404 | overlap OWENS-055 - Omaha NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-04-15 | 404 | overlap OWENS-055 - Omaha NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-04-16 | 404 | overlap OWENS-055 - Omaha NE (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

This gap report backs [row OWENS-055](/Planes/following/overlap/20240415_NE_omaha_owens_055/overview) with three UTC days of lookups that returned nothing for SU-BTT, and it is published rather than buried because [an unretrievable claim and a failed claim are different things](/Planes/Flight-Data-Recovery/What-A-403-Means), a distinction the whole [flight data recovery effort](/Planes/Flight-Data-Recovery/overview) turns on. The reason a volunteer network is all we have is that the primary record never came out: [foreign flight leads rest on public ADS-B alone](/CoverUp/Foreign_Flight_Records), [the NCTC's foreign-ties inquiry was reportedly stopped](/FBI/Foreign_Leads), and [proposed Law 2 names these tails specifically](/laws/US_Intel/Law_2_US_Intel) so that [Congress](/Vote/overview) would have to explain them. The page worth clicking next is [Overlap Recovery](/Planes/Flight-Data-Recovery/Overlap-Recovery), where all 69 testable aircraft-and-date pairs were pulled against both free daily archives: twenty-three came back with a primary trace, and [the commercial archives that hold the rest](/Planes/following/apis/proprietary/knowledge) are the ones behind a paywall, which is itself part of [how this investigation gets its data](/Planes/following/apis/overview).

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Row OWENS-055, the Omaha claim itself](/Planes/following/overlap/20240415_NE_omaha_owens_055/overview)
* [Open flight data and what it can settle](/Planes/following/apis/public_open_source/knowledge)
* [Egyptian foreign operations at Provo, 2025](/intelligence/Egyptian_Foreign_Ops)

</div>
<div>

* [Withheld airborne surveillance records](/CoverUp/Airborne_Surveillance_Records)
* [Law 2, the Intelligence Services Disclosure Act](/laws/US_Intel/Law_2_US_Intel)
* [Media coverage and how it framed this](/Media/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
