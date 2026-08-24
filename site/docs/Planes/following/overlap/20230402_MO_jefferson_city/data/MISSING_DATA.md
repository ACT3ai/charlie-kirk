---
displayed_sidebar: docs
slug: /Planes/following/overlap/20230402_MO_jefferson_city/data/MISSING_DATA
title: "ADS-B gaps for overlap 20230402_MO_jefferson_city"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20230402_MO_jefferson_city (2 April 2023 — Jefferson City, Missouri)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20230402_MO_jefferson_city"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.110Z by
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
| SU-BND | 2023-04-01 | 404 | overlap SITE-001 - Jefferson City (event) / St. Louis (aircraft) MO (audited_accurate, audit: accurate) |
| SU-BND | 2023-04-02 | 404 | overlap SITE-001 - Jefferson City (event) / St. Louis (aircraft) MO (audited_accurate, audit: accurate) |
| SU-BND | 2023-04-03 | 404 | overlap SITE-001 - Jefferson City (event) / St. Louis (aircraft) MO (audited_accurate, audit: accurate) |
| SU-BTT | 2023-04-02 | 404 | overlap OWENS-010 - St. Louis MO (audited_accurate, audit: accurate); overlap SITE-001 - Jefferson City (event) / St. Louis (aircraft) MO (audited_accurate, audit: accurate) |
| SU-BTT | 2023-04-03 | 404 | overlap SITE-001 - Jefferson City (event) / St. Louis (aircraft) MO (audited_accurate, audit: accurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

The Jefferson City page is unusual in this directory because it has a confirmed [SU-BTT](/Planes/SU-BTT/overview) trace behind it and still declines to call the date an overlap — the jet is at St. Louis, [the TPUSA Faith](/Charlie/Leader_of_Churches) tour launch is 130 miles and two hours' drive west, and [the row page](/Planes/following/overlap/20230402_MO_jefferson_city/overview) says so before it says anything else. That is the standard worth carrying into the rest of the case, where proximity is routinely treated as connection: the [claims built on Google Trends geography](/GoogleSearches/overview), the [inferences drawn from foreign-registered phones near the site](/intelligence/Foreign_Phones_UVU), the [organizational links assembled in the Companies section](/Companies_Organizations/overview). For the arithmetic version of the same discipline, [Turning Point events with the aircraft record beside them](/Planes/following/TPUSA_events) checks 139 sourced appearances date by date and finds exactly one placing Erika Kirk at an event before 10 September 2025 with a firm date — [and her flight logs are reported erased](/Planes/Erika-Flight-Logs-Erased), so even that one cannot be corroborated from her side, a limit the [overlap index](/Planes/following/overlap/overview) repeats on every row.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Overlap recovery — the whole run](/Planes/Flight-Data-Recovery/Overlap-Recovery)
* [Maps and distance testing](/maps/overview)
* [Charlie Kirk and the church network](/Charlie/overview)

</div>
<div>

* [St. Louis field record](/Planes/following/StLouis_KSTL_2022-12-20_to_2025-02-23/overview)
* [Turning Point USA section](/TPUSA/overview)
* [Key individuals roster](/key_individuals/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
