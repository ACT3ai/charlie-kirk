---
displayed_sidebar: docs
slug: /Planes/following/overlap/20250910_UT_orem/data/MISSING_DATA
title: "ADS-B gaps for overlap 20250910_UT_orem"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20250910_UT_orem (10 September 2025 — Orem, Utah)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20250910_UT_orem"
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
| SU-BND | 2025-09-11 | 404 | overlap EXTRA-006 - Provo UT (audited_accurate, audit: accurate); overlap SITE-006 - Orem (event) / Provo (aircraft) UT (audited_accurate, audit: accurate) |
| SU-BTT | 2025-09-09 | 404 | day before claimed arrival at Wilmington (KILG); overlap OWENS-041 - Provo then Wilmington UT/DE (audited_inaccurate, audit: inaccurate); overlap SITE-005 - Wilmington DE (claimed, audit: partial); overlap SITE-006 - Orem (event) / Provo (aircraft) UT (audited_accurate, audit: accurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

The archive blanks for [10 September 2025 — Orem](/Planes/following/overlap/20250910_UT_orem/overview) are published here because the strongest date in this directory deserves its empty columns stated as loudly as its full ones: [SU-BTT](/Planes/SU-BTT/overview) and [SU-BND](/Planes/SU-BND/overview) were both at [Provo](/Planes/following/Provo_KPVU_2024-04-19_to_2025-09-13/overview) that week, and not every surrounding day has a trace. No archive on earth answers the questions this date actually raises — who was aboard, why [a jet parked 110 days](/Planes/following/overlap/20250910_UT_provo_extra_006/overview) had its transponder reportedly cycling twenty-one minutes before the shot, and what [the reported DoD-liaison contractors at the airport](/Locations/Provo_Airport) were doing — and those belong to [a disclosure law](/laws/US_Intel/Law_2_US_Intel), not to a volunteer ADS-B network. For what the free archives can and cannot reach, [open flight data](/Planes/following/apis/public_open_source/knowledge) is the honest accounting, including why a 2022 claim on this same sheet can never be tested the way a 2025 one was.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [The flight-data recovery hub](/Planes/Flight-Data-Recovery/overview)
* [Government flight records and FOIA routes](/Planes/following/apis/government/knowledge)
* [The September 10 event timeline](/Topic-Analyses/September_10_Event_Timeline)

</div>
<div>

* [Drones reported over UVU](/Drones/overview)
* [Technology and surveillance claims](/technology_surveillance/overview)
* [Law 1: forced disclosure by DoJ and FBI](/laws/DoJ_FBI/Law_1_DoJ_FBI)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
