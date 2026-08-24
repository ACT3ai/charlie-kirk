---
displayed_sidebar: docs
title: "ADS-B gaps for SU-BTT - claimed flights with no primary trace"
sidebar_label: "ADS-B gaps"
description: "Every claimed SU-BTT flight date that returned no primary ADS-B trace from the adsb.lol globe history archive, with the exact HTTP result and why we looked."
keywords:
  - "SU-BTT"
  - "ADS-B"
  - "flight tracking"
  - "missing flight data"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.114Z by
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
| SU-BTT | 2022-10-04 | 404 | overlap OWENS-001 - New York NY (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2022-10-05 | 404 | overlap OWENS-001 - New York NY (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2022-10-06 | 404 | overlap OWENS-001 - New York NY (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2022-10-19 | 404 | overlap OWENS-002 - Chicago IL (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2022-10-20 | 404 | overlap OWENS-002 - Chicago IL (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2022-10-21 | 404 | overlap OWENS-002 - Chicago IL (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2022-10-31 | 404 | overlap OWENS-003 - Boston MA (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2022-11-01 | 404 | overlap OWENS-003 - Boston MA (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2022-11-02 | 404 | overlap OWENS-003 - Boston MA (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2022-11-12 | 404 | overlap OWENS-004 - Wichita KS (audited_accurate, audit: accurate) |
| SU-BTT | 2022-11-13 | 404 | overlap OWENS-004 - Wichita KS (audited_accurate, audit: accurate) |
| SU-BTT | 2022-11-14 | 404 | overlap OWENS-004 - Wichita KS (audited_accurate, audit: accurate) |
| SU-BTT | 2022-11-16 | 404 | overlap OWENS-005 - Wilmington DE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2022-11-17 | 404 | overlap OWENS-005 - Wilmington DE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2022-11-18 | 404 | overlap OWENS-005 - Wilmington DE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2022-11-24 | 404 | overlap OWENS-043 - Wilmington DE (claimed, audit: archive_gap) |
| SU-BTT | 2022-11-25 | 404 | overlap OWENS-043 - Wilmington DE (claimed, audit: archive_gap) |
| SU-BTT | 2022-11-26 | 404 | overlap OWENS-043 - Wilmington DE (claimed, audit: archive_gap) |
| SU-BTT | 2022-12-04 | 404 | overlap OWENS-044 - Chicago IL (claimed, audit: archive_gap) |
| SU-BTT | 2022-12-05 | 404 | overlap OWENS-044 - Chicago IL (claimed, audit: archive_gap) |
| SU-BTT | 2022-12-06 | 404 | overlap OWENS-044 - Chicago IL (claimed, audit: archive_gap) |
| SU-BTT | 2022-12-19 | 404 | overlap OWENS-006 - St. Louis MO (audited_accurate, audit: accurate) |
| SU-BTT | 2022-12-20 | 404 | overlap OWENS-006 - St. Louis MO (audited_accurate, audit: accurate) |
| SU-BTT | 2022-12-21 | 404 | overlap OWENS-006 - St. Louis MO (audited_accurate, audit: accurate) |
| SU-BTT | 2022-12-26 | 404 | overlap OWENS-007 - Bangor ME (audited_accurate, audit: accurate) |
| SU-BTT | 2022-12-27 | 404 | overlap OWENS-007 - Bangor ME (audited_accurate, audit: accurate) |
| SU-BTT | 2022-12-28 | 404 | overlap OWENS-007 - Bangor ME (audited_accurate, audit: accurate) |
| SU-BTT | 2023-01-11 | 404 | overlap OWENS-045 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-01-12 | 404 | overlap OWENS-045 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-01-13 | 404 | overlap OWENS-045 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-01-14 | 404 | overlap OWENS-008 - Atlanta GA (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-01-15 | 404 | overlap OWENS-008 - Atlanta GA (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-01-16 | 404 | overlap OWENS-008 - Atlanta GA (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-02-09 | 404 | overlap OWENS-009 - Wilmington DE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-02-10 | 404 | overlap OWENS-009 - Wilmington DE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-02-11 | 404 | overlap OWENS-009 - Wilmington DE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-02-26 | 404 | overlap OWENS-046 - St. Louis MO (audited_partial, audit: partial) |
| SU-BTT | 2023-03-14 | 404 | overlap OWENS-047 - Omaha NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-03-15 | 404 | overlap OWENS-047 - Omaha NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-03-16 | 404 | overlap OWENS-047 - Omaha NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-03-26 | 404 | overlap OWENS-048 - Wilmington DE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-03-27 | 404 | overlap OWENS-048 - Wilmington DE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-03-28 | 404 | overlap OWENS-048 - Wilmington DE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-04-02 | 404 | overlap OWENS-010 - St. Louis MO (audited_accurate, audit: accurate); overlap SITE-001 - Jefferson City (event) / St. Louis (aircraft) MO (audited_accurate, audit: accurate) |
| SU-BTT | 2023-04-03 | 404 | overlap SITE-001 - Jefferson City (event) / St. Louis (aircraft) MO (audited_accurate, audit: accurate) |
| SU-BTT | 2023-04-05 | 404 | overlap OWENS-011 - Wilmington DE (audited_accurate, audit: accurate) |
| SU-BTT | 2023-04-07 | 404 | overlap OWENS-011 - Wilmington DE (audited_accurate, audit: accurate) |
| SU-BTT | 2023-04-15 | 404 | overlap OWENS-012 - Wichita KS (audited_accurate, audit: accurate) |
| SU-BTT | 2023-04-19 | 404 | overlap OWENS-013 - Wilmington DE (audited_accurate, audit: accurate) |
| SU-BTT | 2023-04-22 | 404 | overlap EXTRA-003 - Topeka KS (claimed, audit: untested) |
| SU-BTT | 2023-04-23 | 404 | overlap EXTRA-003 - Topeka KS (claimed, audit: untested) |
| SU-BTT | 2023-04-24 | 404 | overlap OWENS-049 - Wichita KS (audited_inaccurate, audit: inaccurate); overlap EXTRA-003 - Topeka KS (claimed, audit: untested) |
| SU-BTT | 2023-04-25 | 404 | overlap OWENS-049 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-04-26 | 404 | overlap OWENS-049 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-06-07 | 404 | overlap OWENS-051 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-06-08 | 404 | overlap OWENS-051 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-06-09 | 404 | overlap OWENS-051 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-07-24 | 404 | overlap OWENS-017 - Lincoln NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-07-25 | 404 | overlap OWENS-017 - Lincoln NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-07-26 | 404 | overlap OWENS-017 - Lincoln NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-08-24 | 404 | overlap EXTRA-005 - Lincoln NE (claimed, audit: inaccurate) |
| SU-BTT | 2023-08-25 | 404 | overlap EXTRA-005 - Lincoln NE (claimed, audit: inaccurate) |
| SU-BTT | 2023-08-26 | 404 | overlap EXTRA-005 - Lincoln NE (claimed, audit: inaccurate) |
| SU-BTT | 2023-09-02 | 404 | overlap OWENS-018 - Wilmington DE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-09-03 | 404 | overlap OWENS-018 - Wilmington DE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-09-04 | 404 | overlap OWENS-018 - Wilmington DE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-01-09 | 404 | overlap OWENS-019 - Sacramento CA (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-01-10 | 404 | overlap OWENS-019 - Sacramento CA (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-01-11 | 404 | overlap OWENS-019 - Sacramento CA (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-02-10 | 404 | overlap OWENS-020 - Omaha / Lincoln NE (audited_partial, audit: partial); overlap SITE-002 - Lincoln NE (audited_partial, audit: partial) |
| SU-BTT | 2024-02-11 | 404 | overlap SITE-002 - Lincoln NE (audited_partial, audit: partial) |
| SU-BTT | 2024-02-12 | 404 | overlap SITE-002 - Lincoln NE (audited_partial, audit: partial) |
| SU-BTT | 2024-02-13 | 404 | overlap OWENS-021 - Wilmington DE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-02-15 | 404 | overlap OWENS-021 - Wilmington DE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-03-09 | 404 | overlap OWENS-053 - St. Louis MO (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-03-10 | 404 | overlap OWENS-053 - St. Louis MO (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-03-11 | 404 | overlap OWENS-053 - St. Louis MO (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-03-17 | 404 | overlap OWENS-022 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-03-18 | 404 | overlap OWENS-022 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-03-19 | 404 | overlap OWENS-022 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-03-21 | 404 | overlap OWENS-054 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-03-22 | 404 | overlap OWENS-054 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-03-23 | 404 | overlap OWENS-054 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-03-30 | 404 | overlap OWENS-023 - Wichita KS (audited_accurate, audit: accurate) |
| SU-BTT | 2024-03-31 | 404 | day before claimed arrival at Provo (KPVU) |
| SU-BTT | 2024-04-01 | 404 | claimed arrival at Provo (KPVU) - flights.csv |
| SU-BTT | 2024-04-02 | 404 | overlap OWENS-024 - Wichita / Lawrence KS (audited_partial, audit: partial); overlap SITE-003 - Lawrence (event) / Wichita (aircraft) KS (audited_partial, audit: partial) |
| SU-BTT | 2024-04-04 | 404 | overlap OWENS-024 - Wichita / Lawrence KS (audited_partial, audit: partial); overlap SITE-003 - Lawrence (event) / Wichita (aircraft) KS (audited_partial, audit: partial) |
| SU-BTT | 2024-04-14 | 404 | overlap OWENS-055 - Omaha NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-04-15 | 404 | overlap OWENS-055 - Omaha NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-04-16 | 404 | overlap OWENS-055 - Omaha NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-04-24 | 404 | overlap OWENS-026 - Provo UT (audited_accurate, audit: accurate); overlap SITE-004 - Salt Lake City (event) / Provo (aircraft) UT (audited_accurate, audit: accurate) |
| SU-BTT | 2024-04-27 | 404 | overlap OWENS-027 - Wilmington DE (audited_accurate, audit: accurate) |
| SU-BTT | 2024-04-29 | 404 | day after claimed departure from Provo (KPVU); overlap OWENS-027 - Wilmington DE (audited_accurate, audit: accurate) |
| SU-BTT | 2024-06-17 | 404 | overlap OWENS-058 - Lincoln NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-06-18 | 404 | overlap OWENS-058 - Lincoln NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-06-19 | 404 | overlap OWENS-058 - Lincoln NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-07-04 | 404 | overlap OWENS-059 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-07-05 | 404 | overlap OWENS-059 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-07-06 | 404 | overlap OWENS-059 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-07-19 | 404 | overlap OWENS-028 - Omaha / Lincoln NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-07-20 | 404 | overlap OWENS-028 - Omaha / Lincoln NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-07-24 | 404 | overlap OWENS-060 - Omaha / Lincoln NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-07-25 | 404 | overlap OWENS-060 - Omaha / Lincoln NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-07-26 | 404 | overlap OWENS-060 - Omaha / Lincoln NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-08-16 | 404 | overlap OWENS-029 - Omaha / Lincoln NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-08-17 | 404 | overlap OWENS-029 - Omaha / Lincoln NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-08-18 | 404 | overlap OWENS-029 - Omaha / Lincoln NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2025-01-11 | 404 | overlap OWENS-031 - Wichita KS (audited_inaccurate, audit: inaccurate); overlap OWENS-061 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2025-01-12 | 404 | overlap OWENS-031 - Wichita KS (audited_inaccurate, audit: inaccurate); overlap OWENS-061 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2025-01-13 | 404 | overlap OWENS-031 - Wichita KS (audited_inaccurate, audit: inaccurate); overlap OWENS-061 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2025-01-16 | 404 | overlap OWENS-032 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2025-01-17 | 404 | overlap OWENS-032 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2025-01-18 | 404 | overlap OWENS-032 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2025-02-07 | 404 | overlap OWENS-062 - Omaha NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2025-02-08 | 404 | overlap OWENS-062 - Omaha NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2025-02-09 | 404 | overlap OWENS-062 - Omaha NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2025-03-14 | 404 | overlap OWENS-033 - Wichita KS (audited_inaccurate, audit: inaccurate); overlap OWENS-063 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2025-03-15 | 404 | overlap OWENS-033 - Wichita KS (audited_inaccurate, audit: inaccurate); overlap OWENS-063 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2025-03-16 | 404 | overlap OWENS-033 - Wichita KS (audited_inaccurate, audit: inaccurate); overlap OWENS-063 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2025-03-21 | 404 | overlap OWENS-034 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2025-03-22 | 404 | overlap OWENS-034 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2025-03-23 | 404 | overlap OWENS-034 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2025-06-17 | 404 | overlap OWENS-036 - Omaha / Lincoln NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2025-06-19 | 404 | overlap OWENS-036 - Omaha / Lincoln NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2025-07-18 | 404 | day before claimed arrival at Le Bourget (LFPB) |
| SU-BTT | 2025-07-21 | 404 | day after claimed departure from Le Bourget (LFPB); overlap OWENS-038 - Omaha / Lincoln NE (audited_partial, audit: partial); overlap OWENS-067 - Lincoln NE (audited_accurate, audit: accurate) |
| SU-BTT | 2025-07-25 | 404 | day before claimed arrival at Wilmington (KILG) |
| SU-BTT | 2025-07-28 | 404 | day after claimed departure from Wilmington (KILG) |
| SU-BTT | 2025-08-15 | 404 | day before claimed arrival at Le Bourget (LFPB) |
| SU-BTT | 2025-08-18 | 404 | day after claimed departure from Le Bourget (LFPB); overlap OWENS-039 - Omaha / Lincoln NE (audited_partial, audit: partial) |
| SU-BTT | 2025-08-22 | 404 | day before claimed arrival at Wilmington (KILG) |
| SU-BTT | 2025-08-25 | 404 | day after claimed departure from Wilmington (KILG) |
| SU-BTT | 2025-09-02 | 404 | day before claimed arrival at Le Bourget (LFPB) |
| SU-BTT | 2025-09-05 | 404 | day after claimed departure from Le Bourget (LFPB); overlap OWENS-040 - Provo UT (audited_accurate, audit: accurate) |
| SU-BTT | 2025-09-09 | 404 | day before claimed arrival at Wilmington (KILG); overlap OWENS-041 - Provo then Wilmington UT/DE (audited_inaccurate, audit: inaccurate); overlap SITE-005 - Wilmington DE (claimed, audit: partial); overlap SITE-006 - Orem (event) / Provo (aircraft) UT (audited_accurate, audit: accurate) |
| SU-BTT | 2025-09-12 | 404 | day after claimed departure from Wilmington (KILG) |
| SU-BTT | 2025-09-30 | 404 | day before claimed arrival at Wichita (KICT) |
| SU-BTT | 2025-10-01 | 404 | claimed arrival at Wichita (KICT) - flights.csv |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

SU-BTT is the most-claimed tail in this investigation and therefore the one with the longest list of dates that came back empty; every row is published beside [the SU-BTT page](/Planes/SU-BTT/overview) rather than dropped, the same discipline produced gap lists for [SU-BND](/Planes/SU-BND/data/adsb/MISSING_DATA), [SU-BTU](/Planes/SU-BTU/data/adsb/MISSING_DATA), [SU-BTV](/Planes/SU-BTV/data/adsb/MISSING_DATA) and [SU-BGM](/Planes/SU-BGM/data/adsb/MISSING_DATA), and [per-aircraft recovery status](/Planes/Flight-Data-Recovery/Per-Aircraft-Status) sets out what every source still holds for each. Nothing on this list should be carried into the [day-of event timeline](/Topic-Analyses/September_10_Event_Timeline), the [Egyptian jets at Provo](/Proof_Intel_Services/Egyptian_Jets_Provo) thread, or the [claim that foreign flight records were withheld](/CoverUp/Foreign_Flight_Records): a 404 means volunteer receivers heard nothing that UTC day, and parked-and-silent, outside-coverage and wrong-claimed-date all come before suppression. The two pages that do carry weight are [Overlap Recovery](/Planes/Flight-Data-Recovery/Overlap-Recovery), where 69 aircraft-and-date pairs were tested against two independent archives, and [what a 403 actually means](/Planes/Flight-Data-Recovery/What-A-403-Means), which retracts a removal this site had already published after five control aircraft with no connection to the case failed in exactly the same way.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Minot, the 2025 point of US entry](/Planes/following/Minot_KMOT_2025-04-08_to_2025-09-04/overview)
* [Joe Kent and the NCTC foreign review](/US_Intelligence/joe-kent)
* [Israel intel flights and UVU](/Israel_Main_Suspect/israel-intel-flights-uvu)

</div>
<div>

* [Sharm el-Sheikh, beside Air Force One](/Planes/following/SharmElSheikh_HESH_2025-10-13_to_2025-10-13/overview)
* [State Department and diplomatic response](/Before/State-Department-Response)
* [Sixteen Israeli-registered phones at UVU (claims)](/Suspicious/Israel/israeli-phones-at-uvu)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
