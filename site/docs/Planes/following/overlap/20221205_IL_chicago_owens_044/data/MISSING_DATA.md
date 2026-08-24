---
displayed_sidebar: docs
slug: /Planes/following/overlap/20221205_IL_chicago_owens_044/data/MISSING_DATA
title: "ADS-B gaps for overlap 20221205_IL_chicago_owens_044"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20221205_IL_chicago_owens_044 (5 December 2022 — Chicago, IL)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20221205_IL_chicago_owens_044"
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
| SU-BTT | 2022-12-04 | 404 | overlap OWENS-044 - Chicago IL (claimed, audit: archive_gap) |
| SU-BTT | 2022-12-05 | 404 | overlap OWENS-044 - Chicago IL (claimed, audit: archive_gap) |
| SU-BTT | 2022-12-06 | 404 | overlap OWENS-044 - Chicago IL (claimed, audit: archive_gap) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

Another row where the audit and the free archives both came back empty — [OWENS-044, Chicago](/Planes/following/overlap/20221205_IL_chicago_owens_044/overview), [SU-BTT](/Planes/SU-BTT/overview) — and the honest label for it on the [overlap index](/Planes/following/overlap/overview) is neither supported nor refuted but untested, exactly as [the open flight-data page](/Planes/following/apis/public_open_source/knowledge) says free archives will behave before mid-2023. That label is unglamorous, and it is why this material can be trusted on the days it does say something, in a case where far too much circulates as settled — the [confession timing dispute](/Gov_Mind_Control/discord-confession-timing), the [contested impact minute](/Other/Evidence-Contradictions), the [competing witness descriptions of the wound](/Witnesses/overview). If you want the run that did produce results, [overlap recovery](/Planes/Flight-Data-Recovery/Overlap-Recovery) tested all 69 checkable aircraft-and-date pairs from [the 73 overlaps](/Planes/following/73_overlaps) sheet against both free daily archives and put twenty-three of them on a primary trace for the first time.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Omaha — always a short hop from Lincoln](/Planes/following/Omaha_KOMA_2024-02-09_to_2025-10-05/overview)
* [Government mind-control claims and the Discord timing](/Gov_Mind_Control/overview)
* [Media response and the drifting numbers](/Media/overview)

</div>
<div>

* [Per-aircraft recovery status](/Planes/Flight-Data-Recovery/Per-Aircraft-Status)
* [Independent investigators driving the case](/Influencers/overview)
* [Topic analyses and deep dives](/Topic-Analyses)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
