---
displayed_sidebar: docs
slug: /Planes/following/overlap/20230725_NE_lincoln_owens_017/data/MISSING_DATA
title: "ADS-B gaps for overlap 20230725_NE_lincoln_owens_017"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20230725_NE_lincoln_owens_017 (25 July 2023 — Lincoln, NE)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20230725_NE_lincoln_owens_017"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.119Z by
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
| SU-BTT | 2023-07-24 | 404 | overlap OWENS-017 - Lincoln NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-07-25 | 404 | overlap OWENS-017 - Lincoln NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-07-26 | 404 | overlap OWENS-017 - Lincoln NE (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

Every lookup on this page returned 404 and every control aircraft returned 404 with it, which makes [OWENS-017](/Planes/following/overlap/20230725_NE_lincoln_owens_017/overview) uncheckable rather than wrong — the [free archives](/Planes/following/apis/public_open_source/knowledge) do not reach July 2023, and almost every 2022 and early-2023 row of the [overlap index](/Planes/following/overlap/overview) lands in the same place, including the earliest entries in the [Lincoln record](/Planes/following/Lincoln_KLNK_2024-02-09_to_2025-10-11/overview). That is a coverage boundary, not suppression, and saying so out loud is what keeps the genuinely documented problems — [foreign leads reportedly halted](/FBI/Foreign_Leads), [warrants sealed until 2026](/Legal/Evidence-Sealing-2026), [an autopsy still unreleased](/Medical/overview) — from being diluted by things that merely resemble them. The one free source that does reach 2022 publishes a full day for the first of each month only, and [flight data recovery](/Planes/Flight-Data-Recovery/overview) explains why that single limitation decides whether the earliest third of this spreadsheet can ever be tested.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Lincoln — seven Egyptian arrivals](/Planes/following/Lincoln_KLNK_2024-02-09_to_2025-10-11/overview)
* [Commercial flight APIs and what they cost](/Planes/following/apis/proprietary/knowledge)
* [Foreign leads reportedly blocked](/FBI/Foreign_Leads)

</div>
<div>

* [Evidence sealed until March 2026](/Legal/Evidence-Sealing-2026)
* [The medical and autopsy record](/Medical/overview)
* [Voting and civic response](/Vote/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
