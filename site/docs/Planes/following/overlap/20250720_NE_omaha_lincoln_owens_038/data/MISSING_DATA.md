---
displayed_sidebar: docs
slug: /Planes/following/overlap/20250720_NE_omaha_lincoln_owens_038/data/MISSING_DATA
title: "ADS-B gaps for overlap 20250720_NE_omaha_lincoln_owens_038"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20250720_NE_omaha_lincoln_owens_038 (20 July 2025 — Omaha / Lincoln, NE)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20250720_NE_omaha_lincoln_owens_038"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.124Z by
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
| SU-BTT | 2025-07-21 | 404 | day after claimed departure from Le Bourget (LFPB); overlap OWENS-038 - Omaha / Lincoln NE (audited_partial, audit: partial); overlap OWENS-067 - Lincoln NE (audited_accurate, audit: accurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

These are the empty lookups for [OWENS-038](/Planes/following/overlap/20250720_NE_omaha_lincoln_owens_038/overview), the 20 July 2025 [Omaha](/Planes/following/Omaha_KOMA_2024-02-09_to_2025-10-05/overview)-and-[Lincoln](/Planes/following/Lincoln_KLNK_2024-02-09_to_2025-10-11/overview) row whose [SU-BTT](/Planes/SU-BTT/overview) half the archives confirmed — a reminder that a confirmed row still has days around it nobody can see. Coverage gaps run through the human side of this case too, and they are usually the more consequential ones: [the FBI Form 302 interviews that have never been released](/analysis_documentation/overview), [the full autopsy that is still not public](/Vote/overview), [the device and location warrants reportedly sealed to March 2026](/Legal/Evidence-Sealing-2026). Where the flight-side gaps do get closed is [flight data recovery](/Planes/Flight-Data-Recovery/overview) — four free routes, one of them a complete public mirror of an archive whose live API refuses the very same dates.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Which open flight sources hold history](/Planes/following/apis/public_open_source/knowledge)
* [The four passes used to check the claims](/Planes/following/apis/overview)
* [Forensic analysis gaps in the official record](/Other/Forensic-Analysis-Gaps)

</div>
<div>

* [Law 3 would mandate the investigation](/laws/Require_to_Investigate/Law_3_Require_to_Investigate)
* [The legal investigation hub](/legal_investigation/overview)
* [Government evidence handling](/gov/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
