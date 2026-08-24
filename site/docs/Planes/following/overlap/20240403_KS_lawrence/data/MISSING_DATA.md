---
displayed_sidebar: docs
slug: /Planes/following/overlap/20240403_KS_lawrence/data/MISSING_DATA
title: "ADS-B gaps for overlap 20240403_KS_lawrence"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20240403_KS_lawrence (3 April 2024 — Lawrence, Kansas)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20240403_KS_lawrence"
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
| SU-BTT | 2024-04-02 | 404 | overlap OWENS-024 - Wichita / Lawrence KS (audited_partial, audit: partial); overlap SITE-003 - Lawrence (event) / Wichita (aircraft) KS (audited_partial, audit: partial) |
| SU-BTT | 2024-04-04 | 404 | overlap OWENS-024 - Wichita / Lawrence KS (audited_partial, audit: partial); overlap SITE-003 - Lawrence (event) / Wichita (aircraft) KS (audited_partial, audit: partial) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

The lookups on this page belong to the Lawrence pairing, where the [free archives](/Planes/following/apis/public_open_source/knowledge) did in the end hold the day: on 3 April 2024 [SU-BTT](/Planes/SU-BTT/overview) ran east across Missouri and landed 1.48 km from [Wilmington, Delaware](/Planes/following/Wilmington_KILG_2022-11-17_to_2025-10-12/overview), with a closest approach to Wichita of 1,852.96 km — so [the row](/Planes/following/overlap/20240403_KS_lawrence/overview) is refuted on position rather than on silence, as the [overlap index](/Planes/following/overlap/overview) records. Refuting a claim on a tracked position is the only kind of refutation this site accepts, for the same reason the [ATF fragment result](/Gun_Bullet/ATF_Fragment_Inconclusive), the [disputed impact second](/Other/Evidence-Contradictions) and the [day-of chronology](/Timeline/overview) reward careful reading: the strength of a claim is the strength of what was actually measured. The next page is [3 April 2024 — Wichita / Lawrence](/Planes/following/overlap/20240403_KS_wichita_lawrence_owens_024/overview), the spreadsheet's own version of the same date, which the audit called partially accurate and the archives call a real US day at the wrong field.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [The spreadsheet's own version of this date](/Planes/following/overlap/20240403_KS_wichita_lawrence_owens_024/overview)
* [Wilmington, outbound every time](/Planes/following/Wilmington_KILG_2022-11-17_to_2025-10-12/overview)
* [ATF fragment, inconclusive](/Gun_Bullet/ATF_Fragment_Inconclusive)

</div>
<div>

* [Evidence contradictions in the case](/Other/Evidence-Contradictions)
* [Timeline overview](/Timeline/overview)
* [Maps and route testing](/maps/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
