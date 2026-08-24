---
displayed_sidebar: docs
slug: /Planes/following/overlap/20221005_NY_new_york_owens_001/data/MISSING_DATA
title: "ADS-B gaps for overlap 20221005_NY_new_york_owens_001"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20221005_NY_new_york_owens_001 (5 October 2022 — New York, NY)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20221005_NY_new_york_owens_001"
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
| SU-BTT | 2022-10-04 | 404 | overlap OWENS-001 - New York NY (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2022-10-05 | 404 | overlap OWENS-001 - New York NY (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2022-10-06 | 404 | overlap OWENS-001 - New York NY (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

The table above is the empty half of [row OWENS-001](/Planes/following/overlap/20221005_NY_new_york_owens_001/overview) — three consecutive 404s for [SU-BTT](/Planes/SU-BTT/overview) on a date the independent auditor places the aircraft in France, and the reason the [overlap index](/Planes/following/overlap/overview) files almost every 2022 row as untested rather than disproved, exactly as [the 73 overlaps](/Planes/following/73_overlaps) reconstruction predicts. That rule reaches well past the aircraft thread — it is the same reasoning behind [what a 403 actually means](/Planes/Flight-Data-Recovery/What-A-403-Means), the sealed device warrants on [evidence sealing](/Legal/Evidence-Sealing-2026), the [court gag orders](/Censorship/Court_Gag_Orders), and the wider [cover-up section](/CoverUp/overview): a record nobody can see is not a record that says nothing happened. For the version of this argument with a document attached instead of a blank, [Law 2](/laws/US_Intel/Law_2_US_Intel) names SU-BTT, SU-BND, SU-BTU, SU-BGM and Army jet [N1098L](/Planes/N1098L/overview) as the tails Congress would be forced to account for.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [What the compilers counted as an overlap](/Planes/following/Overlap_Window_Definition)
* [Candace Owens — profile and claims](/People/candace-owens)
* [Egyptian foreign operations at Provo](/intelligence/Egyptian_Foreign_Ops)

</div>
<div>

* [The four proposed forced-disclosure laws](/laws/)
* [Legal proceedings and evidence handling](/Legal/overview)
* [Free ADS-B sources and how far they reach](/Planes/following/apis/public_open_source/knowledge)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
