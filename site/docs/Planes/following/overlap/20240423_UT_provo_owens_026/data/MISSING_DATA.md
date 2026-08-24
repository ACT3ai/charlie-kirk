---
displayed_sidebar: docs
slug: /Planes/following/overlap/20240423_UT_provo_owens_026/data/MISSING_DATA
title: "ADS-B gaps for overlap 20240423_UT_provo_owens_026"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20240423_UT_provo_owens_026 (23 April 2024 — Provo, UT)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20240423_UT_provo_owens_026"
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
| SU-BTT | 2024-04-24 | 404 | overlap OWENS-026 - Provo UT (audited_accurate, audit: accurate); overlap SITE-004 - Salt Lake City (event) / Provo (aircraft) UT (audited_accurate, audit: accurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

This is the gap file for [row OWENS-026](/Planes/following/overlap/20240423_UT_provo_owens_026/overview), one of the rows the audit marked correct, and the volunteer archive still returned nothing for the surrounding days, which is a useful reminder that [absence in a free network says nothing about whether the aircraft flew](/Planes/Flight-Data-Recovery/What-A-403-Means). The record that would settle it is commercial or governmental and neither is public: [the deep history sits behind paid archives](/Planes/following/apis/proprietary/knowledge), [government sources have to be requested](/Planes/following/apis/government/knowledge), and [the proposed disclosure laws](/Fix/overview) exist because [the foreign-nexus material has stayed withheld](/CoverUp/Foreign_Flight_Records). Next, read [23 April 2024, Salt Lake City](/Planes/following/overlap/20240423_UT_salt_lake_city/overview): on the same day this row covers, [SU-BTT](/Planes/SU-BTT/overview) landed at Provo at 12:13 pm while Charlie Kirk was 45 miles north at the University of Utah, a same-day, same-region pairing the audit did not dissolve, though a confirmed airframe position still places no person aboard.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Row OWENS-026, the accurate Provo row](/Planes/following/overlap/20240423_UT_provo_owens_026/overview)
* [Commercial flight-data APIs and what they cost](/Planes/following/apis/proprietary/knowledge)
* [The four proposed federal disclosure laws](/Fix/overview)

</div>
<div>

* [Legal investigation and evidence handling](/legal_investigation/overview)
* [Property and locations index](/Locations/overview)
* [How government handled the evidence](/gov/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
