---
displayed_sidebar: docs
title: "ADS-B gaps for N872RA - claimed flights with no primary trace"
sidebar_label: "ADS-B gaps"
description: "Every claimed N872RA flight date that returned no primary ADS-B trace from the adsb.lol globe history archive, with the exact HTTP result and why we looked."
keywords:
  - "N872RA"
  - "ADS-B"
  - "flight tracking"
  - "missing flight data"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.109Z by
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
| N872RA | 2025-09-03 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |
| N872RA | 2025-09-04 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |
| N872RA | 2025-09-09 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |
| N872RA | 2025-09-14 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |
| N872RA | 2025-09-15 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

Five September 2025 dates held nothing for this Hawker and the 10th is not one of them — the [Provo arrival that afternoon](/Planes/N872RA/overview) is what put the tail on a list at all, grouped with [N40JD](/Planes/N40JD/overview) and [N560TW](/Planes/N560TW/overview) purely by shared destination and date. For a light business jet with no operator publicly identified, a blank archive day is unremarkable and is evidence of nothing about [Provo airport that afternoon](/Locations/Provo_Airport), the [foreign-aircraft claims](/Theories/Foreign_Intelligence_Claims) built around it, or the [day-of timeline](/Topic-Analyses/September_10_Event_Timeline). This tail also has no archived tracking-page snapshots at all, and the recovery work says plainly what that does and does not mean — read [what a 403 actually means](/Planes/Flight-Data-Recovery/What-A-403-Means) and [per-aircraft recovery status](/Planes/Flight-Data-Recovery/Per-Aircraft-Status) before treating any of it as removal, because a page nobody archived was never taken down.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Provo Municipal Airport and its ramp reports](/Locations/Provo_Airport)
* [Foreign intelligence involvement claims](/Theories/Foreign_Intelligence_Claims)
* [Evidence contradictions across the case](/Other/Evidence-Contradictions)

</div>
<div>

* [The Scottsdale jet Owens flagged](/Planes/N560TW/overview)
* [Every alleged following-flight, retested](/Planes/Flight-Data-Recovery/Overlap-Recovery)
* [The timeline hub for the whole case](/Timeline/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
