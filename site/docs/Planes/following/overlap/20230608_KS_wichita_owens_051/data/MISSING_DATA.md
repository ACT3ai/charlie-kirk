---
displayed_sidebar: docs
slug: /Planes/following/overlap/20230608_KS_wichita_owens_051/data/MISSING_DATA
title: "ADS-B gaps for overlap 20230608_KS_wichita_owens_051"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20230608_KS_wichita_owens_051 (8 June 2023 — Wichita, KS)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20230608_KS_wichita_owens_051"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.119Z by
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
| SU-BTT | 2023-06-07 | 404 | overlap OWENS-051 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-06-08 | 404 | overlap OWENS-051 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-06-09 | 404 | overlap OWENS-051 - Wichita KS (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

Three empty lookups for [SU-BTT](/Planes/SU-BTT/overview) in June 2023 back [OWENS-051](/Planes/following/overlap/20230608_KS_wichita_owens_051/overview), and they are worth reading precisely because they prove nothing — the [free archives](/Planes/following/apis/public_open_source/knowledge) served a control basket normally on the same days, so this is a silent airframe rather than a silent archive, and the [overlap index](/Planes/following/overlap/overview) files it untested rather than refuted. Refusing to convert silence into a finding is the same rule that governs the [drone reports over UVU](/Drones/overview), the [GRAMA admission that no bodycam footage was found](/court/mirandize/bodycam-grama-no-footage) and the [FBI records still withheld](/FBI/overview) — absence has ordinary explanations and they come first. Then read [the Wichita record](/Planes/following/Wichita_KICT_2022-11-13_to_2025-08-03/overview): the Kansas field these jets kept returning to is the Air Capital of the World and holds an FAA Part 145 Dassault service centre, a competing explanation with paperwork behind it.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [The Wichita visits](/Planes/following/Wichita_KICT_2022-11-13_to_2025-08-03/overview)
* [Per-aircraft recovery status](/Planes/Flight-Data-Recovery/Per-Aircraft-Status)
* [Drones reported over UVU](/Drones/overview)

</div>
<div>

* [The missing bodycam GRAMA admission](/court/mirandize/bodycam-grama-no-footage)
* [The FBI's role in the case](/FBI/overview)
* [Non-FBI law enforcement handling](/Law_Enforcement/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
