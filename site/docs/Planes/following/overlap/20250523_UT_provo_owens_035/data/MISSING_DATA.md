---
displayed_sidebar: docs
slug: /Planes/following/overlap/20250523_UT_provo_owens_035/data/MISSING_DATA
title: "ADS-B gaps for overlap 20250523_UT_provo_owens_035"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20250523_UT_provo_owens_035 (23 May 2025 — Provo, UT)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20250523_UT_provo_owens_035"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.113Z by
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
| SU-BND | 2025-05-24 | 404 | day after claimed departure from Le Bourget (LFPB); overlap OWENS-035 - Provo UT (audited_accurate, audit: accurate); overlap OWENS-065 - Provo UT (audited_accurate, audit: accurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

Even a row the archives confirmed has an empty column, and this is it for [OWENS-035](/Planes/following/overlap/20250523_UT_provo_owens_035/overview) — the dates around 23 May 2025 where [SU-BND](/Planes/SU-BND/overview) produced no trace at [Provo](/Planes/following/Provo_KPVU_2024-04-19_to_2025-09-13/overview) at all, kept in public beside the hit rather than quietly dropped from the [register](/Planes/following/overlap/overview). That discipline is the whole point of the [flight-data recovery effort](/Planes/Flight-Data-Recovery/overview): the first thing the backup network did was knock four claims out of the count, which is worth more to a reader than another confirmation, and it is a standard the sealed side of this case — [warrants reportedly sealed to March 2026](/Legal/Evidence-Sealing-2026), [the foreign-nexus review that was stopped](/FBI/Foreign_Leads) — has never been held to. The confirmed half of this same date is worth the click: SU-BND measured **0.03 km** from the Provo ramp, a co-location so tight it was entered on the sheet twice and counted twice — see [the duplicate row OWENS-065](/Planes/following/overlap/20250523_UT_provo_owens_065/overview).

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Overlap recovery, every testable pair tested](/Planes/Flight-Data-Recovery/Overlap-Recovery)
* [Commercial flight APIs and what they would settle](/Planes/following/apis/proprietary/knowledge)
* [How government entities handled the evidence](/gov/overview)

</div>
<div>

* [Law 3 would mandate the investigation itself](/laws/Require_to_Investigate/Law_3_Require_to_Investigate)
* [The sealed autopsy and how people vote on it](/Vote/overview)
* [Legal proceedings and evidence handling](/legal_investigation/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
