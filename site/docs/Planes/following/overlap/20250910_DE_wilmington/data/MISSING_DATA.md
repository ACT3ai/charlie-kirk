---
displayed_sidebar: docs
slug: /Planes/following/overlap/20250910_DE_wilmington/data/MISSING_DATA
title: "ADS-B gaps for overlap 20250910_DE_wilmington"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20250910_DE_wilmington (10 September 2025 — Wilmington, Delaware)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20250910_DE_wilmington"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.125Z by
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
| SU-BTT | 2025-09-09 | 404 | day before claimed arrival at Wilmington (KILG); overlap OWENS-041 - Provo then Wilmington UT/DE (audited_inaccurate, audit: inaccurate); overlap SITE-005 - Wilmington DE (claimed, audit: partial); overlap SITE-006 - Orem (event) / Provo (aircraft) UT (audited_accurate, audit: accurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

This is the gap sheet for [10 September 2025 — Wilmington](/Planes/following/overlap/20250910_DE_wilmington/overview), the leg [SU-BTT](/Planes/SU-BTT/overview) flew out of [Provo](/Planes/following/Provo_KPVU_2024-04-19_to_2025-09-13/overview) on the day Charlie Kirk was killed; the flight itself is confirmed in the [register](/Planes/following/overlap/overview), and what is listed below is only the surrounding days the archives could not answer for. The Erika Kirk half of that pairing has no archive at all — [her flight logs are reported erased](/Planes/Erika-Flight-Logs-Erased) — so no recovery route on this site, and none anywhere, can produce the one document that would settle it, which is equally true of [the FBI Form 302 interviews](/analysis_documentation/overview) and [the full autopsy](/Medical/overview). [Wilmington](/Planes/following/Wilmington_KILG_2022-11-17_to_2025-10-12/overview) is the page that reframes the whole claim: the most-visited airport in the entire Egyptian fleet record, appearing on the outbound leg only, twenty-one times across three years, never once inbound.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Erika Kirk's whereabouts on 10 September](/Planes/following/Erika_Sept10_Whereabouts)
* [Cairo, the home field](/Planes/following/Cairo_HECA_2022-11-13_to_2025-10-12/overview)
* [Timpanogos Regional Hospital, Orem](/Locations/Timpanogos_Regional_Hospital)

</div>
<div>

* [The medical and death timeline](/Timeline/medical-death-timeline)
* [Gag orders and hearing secrecy](/After/Legal_Process_Gag_Orders_And_Secrecy)
* [Everything that happened after 12:23 PM](/After/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
