---
displayed_sidebar: docs
slug: /Planes/following/overlap/20240720_NE_omaha_lincoln_owens_028/data/MISSING_DATA
title: "ADS-B gaps for overlap 20240720_NE_omaha_lincoln_owens_028"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20240720_NE_omaha_lincoln_owens_028 (20 July 2024 — Omaha / Lincoln, NE)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20240720_NE_omaha_lincoln_owens_028"
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
| SU-BTT | 2024-07-19 | 404 | overlap OWENS-028 - Omaha / Lincoln NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-07-20 | 404 | overlap OWENS-028 - Omaha / Lincoln NE (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

The lookups here belong to [row OWENS-028](/Planes/following/overlap/20240720_NE_omaha_lincoln_owens_028/overview), which the audit identified as a 2024-dated twin of a real 2025 rotation, meaning the archive was searched for an aircraft-day that probably never existed, and no amount of [recovery work](/Planes/Flight-Data-Recovery/overview) produces a trace for a mistyped date, a point [the overlap index](/Planes/following/overlap/overview) makes about several rows. A date error propagating into a public total is a mundane failure with real consequences, because that total is what fed [press coverage](/Planes/following/Press_Coverage), [platform argument](/social_media_analysis/overview) and eventually [a defamation fight](/Defamation/overview), none of which went back to check the cell and none of which is answered by [the record a disclosure law would force out](/laws/US_Intel/Law_2_US_Intel). For the real version of this rotation see [20 July 2025, Omaha and Lincoln](/Planes/following/overlap/20250720_NE_omaha_lincoln_owens_038/overview), and for the pattern behind it [the Omaha arrival log](/Planes/following/Omaha_KOMA_2024-02-09_to_2025-10-05/overview), where every one of six Egyptian arrivals is followed within twenty minutes by a hop to [Lincoln](/Planes/following/Lincoln_KLNK_2024-02-09_to_2025-10-11/overview).

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Omaha, six arrivals and six hops to Lincoln](/Planes/following/Omaha_KOMA_2024-02-09_to_2025-10-05/overview)
* [Defamation suits tied to the investigation](/Defamation/overview)
* [Press coverage of the Egyptian-plane claim](/Planes/following/Press_Coverage)

</div>
<div>

* [Media response analysis](/Media/overview)
* [Legal proceedings](/Legal/overview)
* [Cross-cutting topics with no single home](/other_topics/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
