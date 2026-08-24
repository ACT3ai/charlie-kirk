---
displayed_sidebar: docs
slug: /Planes/following/overlap/20230612_UT_provo_owens_016/data/MISSING_DATA
title: "ADS-B gaps for overlap 20230612_UT_provo_owens_016"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20230612_UT_provo_owens_016 (12 June 2023 — Provo, UT)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20230612_UT_provo_owens_016"
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
| SU-BND | 2023-06-11 | 404 | overlap OWENS-016 - Provo UT (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2023-06-12 | 404 | overlap OWENS-016 - Provo UT (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2023-06-13 | 404 | overlap OWENS-016 - Provo UT (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

The 404s here are the reason [OWENS-016](/Planes/following/overlap/20230612_UT_provo_owens_016/overview) had to be decided on the adjacent day: neither archive reaches 12 June 2023, but the [backup volunteer network](/Planes/Flight-Data-Recovery/overview) holds [SU-BND](/Planes/SU-BND/overview) at Inshas Air Base in Egypt the day before, roughly 11,000 km from [Provo](/Planes/following/Provo_KPVU_2024-04-19_to_2025-09-13/overview), as the [overlap index](/Planes/following/overlap/overview) records. Provo is where this thread meets the rest of the investigation — the field where [Egyptian jets sat for days](/intelligence/Egyptian_Foreign_Ops), where the [ramp and passport claims](/Locations/Provo_Airport) originate, and where the [foreign-intelligence theories](/Theories/Foreign_Intelligence_Claims) about September 10 begin. The page to open next is [flight data recovery](/Planes/Flight-Data-Recovery/overview): four free routes were found in a single afternoon, and one of them is the only reason four rows in this entire run could be checked at all.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Provo arrivals and departures](/Planes/following/Provo_KPVU_2024-04-19_to_2025-09-13/overview)
* [Flight data recovery — the four free routes](/Planes/Flight-Data-Recovery/overview)
* [Provo Municipal Airport](/Locations/Provo_Airport)

</div>
<div>

* [Egyptian foreign operations, 2025](/intelligence/Egyptian_Foreign_Ops)
* [Non-US intelligence threads](/intelligence/overview)
* [Property and locations index](/Locations/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
