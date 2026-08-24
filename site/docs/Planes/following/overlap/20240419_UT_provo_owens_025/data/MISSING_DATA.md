---
displayed_sidebar: docs
slug: /Planes/following/overlap/20240419_UT_provo_owens_025/data/MISSING_DATA
title: "ADS-B gaps for overlap 20240419_UT_provo_owens_025"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20240419_UT_provo_owens_025 (19 April 2024 — Provo, UT)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20240419_UT_provo_owens_025"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.111Z by
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
| SU-BND | 2024-04-20 | 404 | overlap OWENS-025 - Provo UT (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

These are the empty lookups behind [row OWENS-025](/Planes/following/overlap/20240419_UT_provo_owens_025/overview), the first documented Utah arrival in the whole [Provo record](/Planes/following/Provo_KPVU_2024-04-19_to_2025-09-13/overview), and an empty result here is a coverage gap in a volunteer network rather than a deletion, a distinction [set out in full on the recovery hub](/Planes/Flight-Data-Recovery/overview). Provo is where the aircraft thread meets the rest of the case: [an Egyptian Falcon crew is reported to have boarded there wearing DoD-liaison badges](/Locations/Provo_Airport), [Utah's governor is claimed to have met Egyptian and French figures thirteen days after the shooting](/Planes/Cox-Foreign-Meetings), [the foreign-involvement leads were reportedly closed off within six days](/Israel/Russell_Brand_Cabinet_Claims), and [the same airport carries the Israel thread's strongest aviation claim](/Israel_Main_Suspect/israel-intel-flights-uvu). Read [Per-Aircraft Recovery Status](/Planes/Flight-Data-Recovery/Per-Aircraft-Status) next, because it says tail by tail how far back each archive reaches, which is the only honest way to tell [a retention boundary from a removal](/Planes/Flight-Data-Recovery/What-A-403-Means), and it is the standard [every claim on this site about missing flight data](/CoverUp/Foreign_Flight_Records) should be held to.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Row OWENS-025, the Provo arrival claim](/Planes/following/overlap/20240419_UT_provo_owens_025/overview)
* [Provo Municipal Airport](/Locations/Provo_Airport)
* [Utah governor's reported foreign meetings](/Planes/Cox-Foreign-Meetings)

</div>
<div>

* [Cover-up claims about withheld records](/CoverUp/overview)
* [Intelligence services in the case](/intelligence/overview)
* [Companies and organizations profiled](/Companies_Organizations/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
