---
displayed_sidebar: docs
slug: /Planes/following/overlap/20240705_KS_wichita_owens_059/data/MISSING_DATA
title: "ADS-B gaps for overlap 20240705_KS_wichita_owens_059"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20240705_KS_wichita_owens_059 (5 July 2024 — Wichita, KS)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20240705_KS_wichita_owens_059"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.122Z by
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
| SU-BTT | 2024-07-04 | 404 | overlap OWENS-059 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-07-05 | 404 | overlap OWENS-059 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-07-06 | 404 | overlap OWENS-059 - Wichita KS (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

These empty results sit under [row OWENS-059](/Planes/following/overlap/20240705_KS_wichita_owens_059/overview), a Wichita claim the auditor answered in three words, still in Egypt, and they are recorded because [an unchecked claim and a checked-and-failed claim have to stay apart](/Planes/Flight-Data-Recovery/overview) if [the count](/Planes/following/73_overlaps) is to mean anything. Wichita has the plainest non-sinister explanation of any field in the record, since it is the Air Capital of the World and home to an FAA Part 145 Dassault Falcon service centre, the kind of ordinary fact that rarely survives contact with [a viral thread](/social_media_analysis/overview), [an aggregator rewrite](/Media/overview), [an AI assistant asked to summarise it](/Planes/following/AI_Assistant_Answers), or [the press that carried the totals](/Planes/following/Press_Coverage). Next, [the Wichita arrival log](/Planes/following/Wichita_KICT_2022-11-13_to_2025-08-03/overview): repeated Falcon 7X visits between 2022 and 2025 to the one American airport with a factory-authorised shop for that exact aircraft type, a coincidence [the following claim](/Planes/Following-Charlie-Erika) has to explain and has not, any more than it explains why the flights continued after he died.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Wichita and its Falcon service centre](/Planes/following/Wichita_KICT_2022-11-13_to_2025-08-03/overview)
* [What AI assistants say about the overlaps](/Planes/following/AI_Assistant_Answers)
* [Media analysis and framing](/Media/overview)

</div>
<div>

* [Social media analysis](/social_media_analysis/overview)
* [Companies and organizations](/Companies_Organizations/overview)
* [Influencers driving the case](/Influencers/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
