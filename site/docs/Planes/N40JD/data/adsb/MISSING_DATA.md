---
displayed_sidebar: docs
title: "ADS-B gaps for N40JD - claimed flights with no primary trace"
sidebar_label: "ADS-B gaps"
description: "Every claimed N40JD flight date that returned no primary ADS-B trace from the adsb.lol globe history archive, with the exact HTTP result and why we looked."
keywords:
  - "N40JD"
  - "ADS-B"
  - "flight tracking"
  - "missing flight data"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.108Z by
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
| N40JD | 2025-09-01 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |
| N40JD | 2025-09-03 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |
| N40JD | 2025-09-07 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |
| N40JD | 2025-09-08 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |
| N40JD | 2025-09-12 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |
| N40JD | 2025-09-13 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

Six blank September dates for a six-seat Beechcraft Premier 1 is what an unremarkable light jet looks like inside a volunteer archive, and the sweep was run anyway so the [N40JD arrival record](/Planes/N40JD/overview) stands on the same footing as every other tail in the [Provo arrival cluster](/Planes/Sept10-Flight-Timeline) and the wider [Planes section](/Planes/overview). None of those dates is the 10th, and none touches the only reason this tail is on a list at all — a 2:29 p.m. arrival at [Provo Municipal Airport](/Locations/Provo_Airport) that a circulating screenshot paired with an Egyptian jet's transponder minute, a pairing critics attribute to [time-zone errors in the underlying logs](/Other/Evidence-Contradictions) rather than to anything in the [day-of timeline](/Topic-Analyses/September_10_Event_Timeline). The overlap logic is worth more than any single tail: [what the compilers counted as an overlap](/Planes/following/Overlap_Window_Definition) records that the spreadsheet accepted a jet within 50 to 100 miles and within plus or minus three days of a claimed location — a window wide enough that coincidence is the expected result, which is why [every alleged following-flight was retested](/Planes/Flight-Data-Recovery/Overlap-Recovery).

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Provo Municipal Airport and its ramp reports](/Locations/Provo_Airport)
* [Evidence contradictions across the case](/Other/Evidence-Contradictions)
* [Maps and route feasibility tests](/maps/overview)

</div>
<div>

* [What actually counted as an overlap](/Planes/following/Overlap_Window_Definition)
* [What Turning Point actually owned](/Planes/TPUSA-Aircraft/overview)
* [Turning Point USA in the investigation](/TPUSA/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
