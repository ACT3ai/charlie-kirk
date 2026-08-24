---
displayed_sidebar: docs
slug: /Planes/following/overlap/20250112_KS_wichita_owens_061/data/MISSING_DATA
title: "ADS-B gaps for overlap 20250112_KS_wichita_owens_061"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20250112_KS_wichita_owens_061 (12 January 2025 — Wichita, KS)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20250112_KS_wichita_owens_061"
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
| SU-BTT | 2025-01-11 | 404 | overlap OWENS-031 - Wichita KS (audited_inaccurate, audit: inaccurate); overlap OWENS-061 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2025-01-12 | 404 | overlap OWENS-031 - Wichita KS (audited_inaccurate, audit: inaccurate); overlap OWENS-061 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2025-01-13 | 404 | overlap OWENS-031 - Wichita KS (audited_inaccurate, audit: inaccurate); overlap OWENS-061 - Wichita KS (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

These lookups duplicate the ones filed under [row OWENS-031](/Planes/following/overlap/20250112_KS_wichita_owens_031/overview), because the sheet carried the same 12 January 2025 [Wichita](/Planes/following/Wichita_KICT_2022-11-13_to_2025-08-03/overview) claim twice, and both copies were tested against the same free archives with the same empty result, which [proves nothing about the aircraft in either direction](/Planes/Flight-Data-Recovery/What-A-403-Means). Keeping both copies visible is deliberate, because a reader checking a public number needs to see where it was padded, and that habit is the difference between this and the parts of the record where nobody can now reconstruct what was removed, such as [the withheld foreign-nexus material](/CoverUp/Foreign_Flight_Records), [the sealed evidence](/Legal/Evidence-Sealing-2026), [the withheld HD campus footage](/CoverUp/UVU_HD_Footage_Withheld) and [the unreleased surrender video](/CoverUp/Sheriff_Video_Withheld). The next page is [Overlap Recovery](/Planes/Flight-Data-Recovery/Overlap-Recovery), where all 69 testable aircraft-and-date pairs from this sheet were pulled against both free daily archives and the report names which ones came back, rather than [asserting a total](/Planes/following/73_overlaps) or [letting an assistant summarise it](/Planes/following/AI_Assistant_Answers).

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [UVU HD surveillance never released](/CoverUp/UVU_HD_Footage_Withheld)
* [Surrender video not publicly released](/CoverUp/Sheriff_Video_Withheld)
* [Cover-up claims index](/CoverUp/overview)

</div>
<div>

* [Censorship across the investigation](/Censorship/overview)
* [Overlap Recovery, every pair tested](/Planes/Flight-Data-Recovery/Overlap-Recovery)
* [Legal proceedings](/Legal/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
