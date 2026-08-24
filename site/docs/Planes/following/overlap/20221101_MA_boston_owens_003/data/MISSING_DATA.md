---
displayed_sidebar: docs
slug: /Planes/following/overlap/20221101_MA_boston_owens_003/data/MISSING_DATA
title: "ADS-B gaps for overlap 20221101_MA_boston_owens_003"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20221101_MA_boston_owens_003 (1 November 2022 — Boston, MA)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20221101_MA_boston_owens_003"
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
| SU-BTT | 2022-10-31 | 404 | overlap OWENS-003 - Boston MA (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2022-11-01 | 404 | overlap OWENS-003 - Boston MA (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2022-11-02 | 404 | overlap OWENS-003 - Boston MA (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

The three rows above close out the earliest cluster of the sheet — [row OWENS-003](/Planes/following/overlap/20221101_MA_boston_owens_003/overview), Boston, [SU-BTT](/Planes/SU-BTT/overview) looked for and not found because no free archive reaches November 2022, not because a transponder went quiet, and the [overlap index](/Planes/following/overlap/overview) says so on its face. Getting that distinction right in public is the one thing this investigation cannot afford to fumble, which is why [what a 403 actually means](/Planes/Flight-Data-Recovery/What-A-403-Means) exists at all, and why claims about vanishing evidence elsewhere in the case — the [10 inches of dirt removed before the pavers](/Tent/Dirt_Removed_Before_Pavers), the [crime-scene handling timeline](/Timeline/scene-changes-paving-timeline), the wider [cover-up hub](/CoverUp/overview) — count for more once the mundane explanation has been ruled out first. From here, [flight data recovery](/Planes/Flight-Data-Recovery/overview) shows the method paying off: four free routes, a control test, one page on this site retracted because the control failed the same way the target did, and the per-row results collected on [overlap recovery](/Planes/Flight-Data-Recovery/Overlap-Recovery).

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Per-aircraft recovery status, tail by tail](/Planes/Flight-Data-Recovery/Per-Aircraft-Status)
* [Technology and surveillance claims](/technology_surveillance/overview)
* [Government handling of the evidence](/gov/overview)

</div>
<div>

* [The tent and the courtyard paved over](/Tent/overview)
* [Utah Valley University on September 10](/UVU/overview)
* [Cairo — the home field for every leg](/Planes/following/Cairo_HECA_2022-11-13_to_2025-10-12/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
