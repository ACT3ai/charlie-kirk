---
displayed_sidebar: docs
slug: /Planes/following/overlap/20230423_KS_topeka_extra_003/data/MISSING_DATA
title: "ADS-B gaps for overlap 20230423_KS_topeka_extra_003"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20230423_KS_topeka_extra_003 (23 April 2023 — Topeka, KS)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20230423_KS_topeka_extra_003"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.118Z by
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
| SU-BTT | 2023-04-22 | 404 | overlap EXTRA-003 - Topeka KS (claimed, audit: untested) |
| SU-BTT | 2023-04-23 | 404 | overlap EXTRA-003 - Topeka KS (claimed, audit: untested) |
| SU-BTT | 2023-04-24 | 404 | overlap OWENS-049 - Wichita KS (audited_inaccurate, audit: inaccurate); overlap EXTRA-003 - Topeka KS (claimed, audit: untested) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

Topeka is an EXTRA row rather than a numbered one — a Turning Point event date with neither Kirk claimed present — and it has never been assessed by anyone: the paid audit skipped it and the free archives above do not reach April 2023, so it sits on the [overlap index](/Planes/following/overlap/overview) with no verdict at all, admitted by [the window definition](/Planes/following/Overlap_Window_Definition) and counted in [the 73 overlaps](/Planes/following/73_overlaps) regardless. Unassessed rows are the quiet majority of this material and they are why the headline figure should never have been quoted as a finding, in a case where numbers move on their own — 68, then 73, then 77, then one — across [press coverage](/Media/overview), [influencer threads](/Influencers/overview), and the [social-media record](/social_media_analysis/overview). Nine days earlier the same [SU-BTT](/Planes/SU-BTT/overview) ended its day near this very city while the sheet claimed Wichita, which is the correction sitting on [14 April 2023](/Planes/following/overlap/20230414_KS_wichita_owens_012/overview) — a misattribution, not an invention, and the most useful thing this directory has produced, alongside the date-by-date checking on [TPUSA events](/Planes/following/TPUSA_events).

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Wichita and the Falcon service centre](/Planes/following/Wichita_KICT_2022-11-13_to_2025-08-03/overview)
* [Turning Point USA — the organization](/TPUSA/overview)
* [AmFest year-by-year timeline](/Amfest/amfest-year-timeline)

</div>
<div>

* [Speaking events catalog](/Planes/following/speaking/overview)
* [Key individuals roster](/key_individuals/overview)
* [Vote — track who backs disclosure](/Vote/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
