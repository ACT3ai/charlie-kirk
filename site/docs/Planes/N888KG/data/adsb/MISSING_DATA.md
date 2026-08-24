---
displayed_sidebar: docs
title: "ADS-B gaps for N888KG - claimed flights with no primary trace"
sidebar_label: "ADS-B gaps"
description: "Every claimed N888KG flight date that returned no primary ADS-B trace from the adsb.lol globe history archive, with the exact HTTP result and why we looked."
keywords:
  - "N888KG"
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
| N888KG | 2025-09-01 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |
| N888KG | 2025-09-02 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |
| N888KG | 2025-09-03 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |
| N888KG | 2025-09-04 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |
| N888KG | 2025-09-05 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |
| N888KG | 2025-09-06 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |
| N888KG | 2025-09-09 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |
| N888KG | 2025-09-11 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |
| N888KG | 2025-09-12 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |
| N888KG | 2025-09-13 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |
| N888KG | 2025-09-14 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |
| N888KG | 2025-09-15 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

Twelve September 2025 dates returned nothing for this Challenger 300, and the 10th is deliberately not among them — the [Provo departure and the mid-flight signal gap](/Planes/N888KG/overview) that made this the Provo Vanish are documented from recovered primary data, so the rows above cover the surrounding month rather than the event, at an airport whose ramp activity is tracked separately on [Provo Municipal Airport](/Locations/Provo_Airport). This airframe is formally blocked from public tracking under an FAA programme any owner may join, which is its own explanation for thin archive coverage, and it is a wholly different claim from the [HADES aircraft over UVU](/Proof_Intel_Services/N1098L_HADES_Over_UVU), the [Egyptian jets at Provo](/intelligence/Egyptian_Foreign_Ops) or the [eighteen-month following pattern](/Planes/Following-Charlie-Erika) — separate arguments about separate sets of aircraft, and merging them helps nobody, least of all the [day-of timeline](/Topic-Analyses/September_10_Event_Timeline). The recovery run made this the most instructive case on the site: what looked like the strongest removal anywhere in the investigation dissolved under a control test, and [what a 403 actually means](/Planes/Flight-Data-Recovery/What-A-403-Means) with [per-aircraft recovery status](/Planes/Flight-Data-Recovery/Per-Aircraft-Status) records exactly how, which is why sixty further legs here are logged as recorded-as-nothing rather than as erased.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Provo Municipal Airport and its ramp reports](/Locations/Provo_Airport)
* [Foreign intelligence involvement claims](/Theories/Foreign_Intelligence_Claims)
* [Kash Patel's public statements on the case](/People/kash-patel)

</div>
<div>

* [The recovery hub, source by source](/Planes/Flight-Data-Recovery/overview)
* [How this investigation pulls flight data](/Planes/following/apis/overview)
* [The timeline hub for the whole case](/Timeline/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
