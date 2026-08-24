---
displayed_sidebar: docs
slug: /Planes/following/overlap/20240329_KS_wichita_owens_023/data/MISSING_DATA
title: "ADS-B gaps for overlap 20240329_KS_wichita_owens_023"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20240329_KS_wichita_owens_023 (29 March 2024 — Wichita, KS)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20240329_KS_wichita_owens_023"
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
| SU-BTT | 2024-03-30 | 404 | overlap OWENS-023 - Wichita KS (audited_accurate, audit: accurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

One 404 sits under a row that stands up: [OWENS-023](/Planes/following/overlap/20240329_KS_wichita_owens_023/overview) put [SU-BTT](/Planes/SU-BTT/overview) 2.27 km from [Wichita](/Planes/following/Wichita_KICT_2022-11-13_to_2025-08-03/overview) on 29 March 2024, inbound from Beauvais in France, with both [free archives](/Planes/following/apis/public_open_source/knowledge) agreeing, the paid audit calling it accurate, and the [overlap index](/Planes/following/overlap/overview) recording it as confirmed. It is also one of the thirteen rows where [Charlie Kirk](/Charlie/overview) rather than Erika Kirk is the person claimed present, which makes it more checkable than most — a public appearance leaves a record, and the [Turning Point calendar](/TPUSA/overview) behind the [speaking-events catalog](/Planes/following/speaking/overview) is a document anyone can audit. The payoff is on [3 April 2024 — Lawrence](/Planes/following/overlap/20240403_KS_lawrence/overview): the same aircraft was still at Wichita when Kirk spoke at the University of Kansas five days later, then departed at 8:43 that morning and flew out of the state.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [3 April 2024 — the wrong-direction pairing](/Planes/following/overlap/20240403_KS_lawrence/overview)
* [Speaking events catalog](/Planes/following/speaking/overview)
* [Charlie Kirk section](/Charlie/overview)

</div>
<div>

* [Turning Point USA](/TPUSA/overview)
* [Timeline overview](/Timeline/overview)
* [Key individuals](/key_individuals/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
