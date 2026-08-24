---
displayed_sidebar: docs
slug: /Planes/following/overlap/20230112_KS_wichita_owens_045/data/MISSING_DATA
title: "ADS-B gaps for overlap 20230112_KS_wichita_owens_045"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20230112_KS_wichita_owens_045 (12 January 2023 — Wichita, KS)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20230112_KS_wichita_owens_045"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.116Z by
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
| SU-BTT | 2023-01-11 | 404 | overlap OWENS-045 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-01-12 | 404 | overlap OWENS-045 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-01-13 | 404 | overlap OWENS-045 - Wichita KS (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

The auditor already found the aircraft somewhere else on [row OWENS-045](/Planes/following/overlap/20230112_KS_wichita_owens_045/overview); the 404s above simply mean the free archives cannot independently confirm or contest that, so the recorded verdict stands untouched on the [overlap index](/Planes/following/overlap/overview) and inside [the 73 overlaps](/Planes/following/73_overlaps) tally. Leaving another researcher's verdict in place when your own data cannot reach it is a small thing that matters a great deal in a case where corrections rarely stick — the [rooftop identification treated as settled](/cameras/Tyler_Placeholder), the [contested minute of impact](/Other/Evidence-Contradictions), and the [narrative that formed in real time](/Narrative/overview) all show what happens when they do not. The reason Wichita keeps appearing at all is on [the Wichita airport page](/Planes/following/Wichita_KICT_2022-11-13_to_2025-08-03/overview): the Air Capital of the World, home to an FAA Part 145 Dassault Falcon service centre — the most boring explanation available for [SU-BTT](/Planes/SU-BTT/overview), and the one that has to be excluded before any other is argued, which is exactly what [the window definition](/Planes/following/Overlap_Window_Definition) never required.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Surveillance cameras and footage threads](/cameras/overview)
* [Suspicious conduct by actor](/Suspicious/overview)
* [Other topics with no single home](/other_topics/overview)

</div>
<div>

* [SU-BTU, third of the five tails](/Planes/SU-BTU/overview)
* [Israel — 17 threads mapped](/Israel/overview)
* [Every aircraft page in one index](/Planes/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
