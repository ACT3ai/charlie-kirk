---
displayed_sidebar: docs
slug: /Planes/following/overlap/20250117_KS_wichita_owens_032/data/MISSING_DATA
title: "ADS-B gaps for overlap 20250117_KS_wichita_owens_032"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20250117_KS_wichita_owens_032 (17 January 2025 — Wichita, KS)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20250117_KS_wichita_owens_032"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.123Z by
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
| SU-BTT | 2025-01-16 | 404 | overlap OWENS-032 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2025-01-17 | 404 | overlap OWENS-032 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2025-01-18 | 404 | overlap OWENS-032 - Wichita KS (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

The archive lookups here support [row OWENS-032](/Planes/following/overlap/20250117_KS_wichita_owens_032/overview), where the audit placed the aircraft at Cairo and Berenice Airbase in Egypt rather than at [Wichita](/Planes/following/Wichita_KICT_2022-11-13_to_2025-08-03/overview), the most specific counter-location recorded against any row in this batch and one the free archives can neither confirm nor deny, which is [the standing limitation of every source used here](/Planes/following/apis/public_open_source/knowledge) and is noted beside [the failed rows around it](/Planes/following/overlap/overview). A named foreign military airfield in an audit note is the sort of detail that would matter enormously if the primary records were open, and they are not: [the foreign flight material has never been produced](/CoverUp/Foreign_Flight_Records), [the intelligence review was reportedly halted](/FBI/Foreign_Leads), and [proposed Law 2 exists to force exactly this category into the open](/laws/US_Intel/Law_2_US_Intel). Read [Getting the data](/Planes/following/apis/overview) next for the four passes this investigation uses, free open sources through commercial APIs to government records and browser capture, and the honest accounting of what each can and cannot settle about [a tail number on a date](/Planes/Flight-Data-Recovery/Per-Aircraft-Status), including [the 2022 window nothing free can reach](/Planes/following/apis/proprietary/knowledge).

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Getting the data, the four passes](/Planes/following/apis/overview)
* [Foreign flight records withheld](/CoverUp/Foreign_Flight_Records)
* [FBI, foreign leads blocked](/FBI/Foreign_Leads)

</div>
<div>

* [Law 1, DoJ and FBI forced disclosure](/laws/DoJ_FBI/Law_1_DoJ_FBI)
* [Government organizations map](/government_organizations/overview)
* [What citizens can actually do about it](/Your_Actions_Fix_It/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
