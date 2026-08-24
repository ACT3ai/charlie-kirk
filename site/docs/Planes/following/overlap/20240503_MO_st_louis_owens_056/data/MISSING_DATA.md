---
displayed_sidebar: docs
slug: /Planes/following/overlap/20240503_MO_st_louis_owens_056/data/MISSING_DATA
title: "ADS-B gaps for overlap 20240503_MO_st_louis_owens_056"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20240503_MO_st_louis_owens_056 (3 May 2024 — St. Louis, MO)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20240503_MO_st_louis_owens_056"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.112Z by
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
| SU-BND | 2024-05-02 | 404 | overlap OWENS-056 - St. Louis MO (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2024-05-03 | 404 | overlap OWENS-056 - St. Louis MO (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2024-05-04 | 404 | overlap OWENS-056 - St. Louis MO (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

These lookups underpin [row OWENS-056](/Planes/following/overlap/20240503_MO_st_louis_owens_056/overview), which the audit found to be a year-shifted duplicate with the aircraft actually parked at [Provo](/Planes/following/Provo_KPVU_2024-04-19_to_2025-09-13/overview), and the archive silence recorded here is coverage rather than concealment, a distinction [spelled out for 403s and 404s alike](/Planes/Flight-Data-Recovery/What-A-403-Means) across [the recovery work](/Planes/Flight-Data-Recovery/overview). Duplicate rows inflate a total, and a total is what actually travelled: 73, 72, 70-plus and 68 all circulated as facts through [press coverage](/Planes/following/Press_Coverage) and [social platforms](/social_media_analysis/overview) while the underlying cells went unchecked, the same failure mode as [every unsourced number elsewhere in the case](/Other/Evidence-Contradictions). The page to read next is [the 73 overlaps](/Planes/following/73_overlaps), which sets out the arithmetic row by row, including how many rows duplicate each other, and pairs with [Missouri's own arrival log](/Planes/following/StLouis_KSTL_2022-12-20_to_2025-02-23/overview) and [the definition of an overlap the compilers used](/Planes/following/Overlap_Window_Definition).

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Row OWENS-056, the duplicated St. Louis claim](/Planes/following/overlap/20240503_MO_st_louis_owens_056/overview)
* [Evidence contradictions across the case](/Other/Evidence-Contradictions)
* [Social media analysis](/social_media_analysis/overview)

</div>
<div>

* [Press coverage of the plane claim](/Planes/following/Press_Coverage)
* [Influencers driving the investigation](/Influencers/overview)
* [Media response and framing](/Media/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
