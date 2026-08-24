---
displayed_sidebar: docs
slug: /Planes/following/overlap/20250112_KS_wichita_owens_031/data/MISSING_DATA
title: "ADS-B gaps for overlap 20250112_KS_wichita_owens_031"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20250112_KS_wichita_owens_031 (12 January 2025 — Wichita, KS)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20250112_KS_wichita_owens_031"
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
| SU-BTT | 2025-01-11 | 404 | overlap OWENS-031 - Wichita KS (audited_inaccurate, audit: inaccurate); overlap OWENS-061 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2025-01-12 | 404 | overlap OWENS-031 - Wichita KS (audited_inaccurate, audit: inaccurate); overlap OWENS-061 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2025-01-13 | 404 | overlap OWENS-031 - Wichita KS (audited_inaccurate, audit: inaccurate); overlap OWENS-061 - Wichita KS (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

This gap file belongs to [row OWENS-031](/Planes/following/overlap/20250112_KS_wichita_owens_031/overview), which the audit found to be one half of a duplicated pair, since [row OWENS-061 carries the same date and city](/Planes/following/overlap/20250112_KS_wichita_owens_061/overview), so the empty archive results are recorded twice for one claimed movement that [the audit placed in Egypt anyway](/Planes/following/73_overlaps) and that sits beside [every other tested row](/Planes/following/overlap/overview). A mechanical double-count is not a lie, but it inflates a public figure, and public figures in this case travel fast and get corrected slowly, the same pattern behind [the disputed impact minute](/Other/Evidence-Contradictions), [the competing accounts of where Charlie Kirk was struck](/Witnesses/overview), and [the arguments about what the ballistics actually showed](/Gun_Bullet/overview). Read [the Wichita arrival log](/Planes/following/Wichita_KICT_2022-11-13_to_2025-08-03/overview) next, because an FAA Part 145 Dassault Falcon service centre at the field these Falcon 7X jets keep returning to is a documented commercial reason for the whole Kansas cluster, and it is the strongest counterargument [the following claim](/Planes/Following-Charlie-Erika) has to beat before any of it reaches [the disclosure-law argument](/laws/US_Intel/Law_2_US_Intel).

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Row OWENS-061, the duplicate of this date](/Planes/following/overlap/20250112_KS_wichita_owens_061/overview)
* [Evidence contradictions in the case](/Other/Evidence-Contradictions)
* [Gun and bullet analysis](/Gun_Bullet/overview)

</div>
<div>

* [Witness accounts from UVU](/Witnesses/overview)
* [Law 2, Intelligence Services Disclosure](/laws/US_Intel/Law_2_US_Intel)
* [Vote and civic response](/Vote/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
