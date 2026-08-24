---
displayed_sidebar: docs
slug: /Planes/following/overlap/20240423_UT_salt_lake_city/data/MISSING_DATA
title: "ADS-B gaps for overlap 20240423_UT_salt_lake_city"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20240423_UT_salt_lake_city (23 April 2024 — Salt Lake City, Utah)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20240423_UT_salt_lake_city"
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
| SU-BND | 2024-04-22 | 404 | overlap SITE-004 - Salt Lake City (event) / Provo (aircraft) UT (audited_accurate, audit: accurate) |
| SU-BND | 2024-04-23 | 404 | overlap SITE-004 - Salt Lake City (event) / Provo (aircraft) UT (audited_accurate, audit: accurate) |
| SU-BND | 2024-04-24 | 404 | overlap SITE-004 - Salt Lake City (event) / Provo (aircraft) UT (audited_accurate, audit: accurate) |
| SU-BTT | 2024-04-24 | 404 | overlap OWENS-026 - Provo UT (audited_accurate, audit: accurate); overlap SITE-004 - Salt Lake City (event) / Provo (aircraft) UT (audited_accurate, audit: accurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

These lookups sit under [the strongest pre-2025 pairing on the site](/Planes/following/overlap/20240423_UT_salt_lake_city/overview), and what they show is that the free archive held nothing for [SU-BND](/Planes/SU-BND/overview) across 22 to 24 April 2024 even though the aircraft was demonstrably parked at Provo, a plain illustration of why [this investigation refuses to read a 404 as a removal](/Planes/Flight-Data-Recovery/What-A-403-Means). The control test that keeps that rule honest is the same discipline missing from most of the case's public argument, where [claims about withheld records](/CoverUp/Foreign_Flight_Records), [halted foreign leads](/FBI/Foreign_Leads) and [sealed evidence](/Legal/Evidence-Sealing-2026) get flattened into one story by people [who never ran a control](/Influencers/overview). Go to [Overlap Recovery](/Planes/Flight-Data-Recovery/Overlap-Recovery) next, where every testable aircraft-and-date pair in the sheet was run against both free daily archives, and which names the dates that now have a primary trace and the ones that never will without [the paid history](/Planes/following/apis/proprietary/knowledge) that [the disclosure laws are written to reach past](/laws/US_Intel/Law_2_US_Intel).

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [The Salt Lake City pairing itself](/Planes/following/overlap/20240423_UT_salt_lake_city/overview)
* [Evidence sealed into 2026](/Legal/Evidence-Sealing-2026)
* [Foreign leads blocked at the FBI](/FBI/Foreign_Leads)

</div>
<div>

* [Maps and route feasibility](/maps/overview)
* [Chronology of the whole case](/Timeline/overview)
* [Per-aircraft recovery status](/Planes/Flight-Data-Recovery/Per-Aircraft-Status)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
