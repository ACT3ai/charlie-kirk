---
displayed_sidebar: docs
slug: /Planes/following/overlap/20221113_KS_wichita_owens_004/data/MISSING_DATA
title: "ADS-B gaps for overlap 20221113_KS_wichita_owens_004"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20221113_KS_wichita_owens_004 (13 November 2022 — Wichita, KS)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20221113_KS_wichita_owens_004"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.115Z by
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
| SU-BTT | 2022-11-12 | 404 | overlap OWENS-004 - Wichita KS (audited_accurate, audit: accurate) |
| SU-BTT | 2022-11-13 | 404 | overlap OWENS-004 - Wichita KS (audited_accurate, audit: accurate) |
| SU-BTT | 2022-11-14 | 404 | overlap OWENS-004 - Wichita KS (audited_accurate, audit: accurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

This gap report belongs to one of the rows the independent auditor actually upheld — [OWENS-004, Wichita](/Planes/following/overlap/20221113_KS_wichita_owens_004/overview) — and the 404s above change nothing about that, because paid archives reach 2022 and the free ones do not, a limit spelled out on [commercial flight-data APIs](/Planes/following/apis/proprietary/knowledge) and on [the open-source flight data page](/Planes/following/apis/public_open_source/knowledge), with the row itself still listed on the [overlap index](/Planes/following/overlap/overview). The whole case has this shape: the record that would settle a question exists and sits behind a paywall, a seal or an agency — [device warrants sealed into 2026](/Legal/Evidence-Sealing-2026), the [unreleased autopsy and medical-examiner material](/Medical/overview), the [files the cover-up section tracks](/CoverUp/overview) — so citizens buy what they can and document what they cannot. For the concrete remedy, [Law 1](/laws/DoJ_FBI/Law_1_DoJ_FBI) is the proposed statute forcing DoJ and FBI disclosure, and its findings already cite foreign military aircraft and roughly twelve foreign-registered phones at the shooting site as grounds, with [the Wichita field record](/Planes/following/Wichita_KICT_2022-11-13_to_2025-08-03/overview) supplying the aircraft side.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Wilmington — outbound leg only, twenty-one times](/Planes/following/Wilmington_KILG_2022-11-17_to_2025-10-12/overview)
* [Congress and the four disclosure laws](/laws/)
* [What citizens can actually do about it](/Your_Actions_Fix_It/overview)

</div>
<div>

* [Overlap recovery — every claimed pair tested](/Planes/Flight-Data-Recovery/Overlap-Recovery)
* [Vote — tracking who backs disclosure](/Vote/overview)
* [Companies and organizations profiled](/Companies_Organizations/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
