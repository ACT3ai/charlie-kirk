---
displayed_sidebar: docs
title: "ADS-B gaps for N102DZ - claimed flights with no primary trace"
sidebar_label: "ADS-B gaps"
description: "Every claimed N102DZ flight date that returned no primary ADS-B trace from the adsb.lol globe history archive, with the exact HTTP result and why we looked."
keywords:
  - "N102DZ"
  - "ADS-B"
  - "flight tracking"
  - "missing flight data"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.107Z by
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
| N102DZ | 2025-09-06 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |
| N102DZ | 2025-09-07 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |
| N102DZ | 2025-09-09 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |
| N102DZ | 2025-09-12 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |
| N102DZ | 2025-09-13 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

Every row above is a September 2025 date on which a volunteer receiver network held no trace for the Kirk family Gulfstream V — a systematic window sweep rather than a list of claimed flights, published so the [N102DZ record](/Planes/N102DZ/overview) can be argued with instead of taken on trust, alongside the [September 10 flight timeline](/Planes/Sept10-Flight-Timeline) and the rest of the [Planes section](/Planes/overview). A 404 for a privately owned jet that sits on a ramp most days is the ordinary result, and it is not the same thing as the [reported removal of this tail's public flight history](/Planes/Erika-Flight-Logs-Erased) — Erika Kirk's own itinerary is the document nobody has produced — nor does it bear on the [day-of timeline at UVU](/Topic-Analyses/September_10_Event_Timeline) or the [evidence sealed into 2026](/Legal/Evidence-Sealing-2026). If you want the part of this that did move, [what a 403 actually means](/Planes/Flight-Data-Recovery/What-A-403-Means) records the day this site published a removal and had to retract it after seven unrelated control aircraft returned the identical refusal, and that discipline now runs the whole [recovery effort](/Planes/Flight-Data-Recovery/overview), tail by tail in [per-aircraft status](/Planes/Flight-Data-Recovery/Per-Aircraft-Status).

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Commercial trackers and what they would settle](/Planes/following/apis/proprietary/knowledge)
* [Provo Municipal Airport and its ramp reports](/Locations/Provo_Airport)
* [Technology and surveillance claims in the case](/technology_surveillance/overview)

</div>
<div>

* [Google Trends deletion and scrubbing claims](/Censorship/Google_Search_Trends_Scrubbing)
* [Evidence contradictions across the case](/Other/Evidence-Contradictions)
* [Law 1: DoJ and FBI forced disclosure](/laws/DoJ_FBI/Law_1_DoJ_FBI)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
