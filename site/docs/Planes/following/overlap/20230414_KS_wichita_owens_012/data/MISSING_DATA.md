---
displayed_sidebar: docs
slug: /Planes/following/overlap/20230414_KS_wichita_owens_012/data/MISSING_DATA
title: "ADS-B gaps for overlap 20230414_KS_wichita_owens_012"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20230414_KS_wichita_owens_012 (14 April 2023 — Wichita, KS)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20230414_KS_wichita_owens_012"
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
| SU-BTT | 2023-04-15 | 404 | overlap OWENS-012 - Wichita KS (audited_accurate, audit: accurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

This is the row where the free archives overturned the paid audit rather than agreeing with it — the audit marked Wichita correct, the trace puts [SU-BTT](/Planes/SU-BTT/overview) finishing its day near Topeka, roughly 215 kilometres away, and [the row page](/Planes/following/overlap/20230414_KS_wichita_owens_012/overview) carries the correction in full, with [the Wichita field record](/Planes/following/Wichita_KICT_2022-11-13_to_2025-08-03/overview) supplying the maintenance-shop explanation for why the field is in the sheet at all. Publishing a result that contradicts the source you have been relying on is the point of doing the work, and this case is short of it — the [drifting overlap totals](/Media/overview), the [unauthenticated kill-me screenshots](/Charlie/Text_Messages/kill-me-07-sept-9-all-caps), and the [contradictions logged in Other](/Other/Evidence-Contradictions) all persist because corrections rarely travel as far as claims. Note also what the correction is not: a misattribution, not an invention — the jet really was in Kansas that day, just at the wrong field — which is the difference [the window definition](/Planes/following/Overlap_Window_Definition) exists to police and [the 73 overlaps](/Planes/following/73_overlaps) reconstruction tallies row by row.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Overlap recovery — all 69 pairs](/Planes/Flight-Data-Recovery/Overlap-Recovery)
* [Influencers driving the investigation](/Influencers/overview)
* [Narrative framing in real time](/Narrative/overview)

</div>
<div>

* [Candace Owens broadcasts](/Planes/following/Candace_Owens_Broadcasts)
* [Defamation suits from the case](/Defamation/overview)
* [Social media analysis](/social_media_analysis/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
