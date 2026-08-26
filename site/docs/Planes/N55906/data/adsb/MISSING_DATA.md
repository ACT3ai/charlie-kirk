---
displayed_sidebar: docs
title: "ADS-B gaps for N55906 - claimed flights with no primary trace"
sidebar_label: "ADS-B gaps"
description: "Every claimed N55906 flight date that returned no primary ADS-B trace from the adsb.lol globe history archive, with the exact HTTP result and why we looked."
keywords:
  - "N55906"
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
| N55906 | 2025-09-01 | 404 | September 2025 window sweep (n1098l side) - not a claimed date, a systematic look |
| N55906 | 2025-09-02 | 404 | September 2025 window sweep (n1098l side) - not a claimed date, a systematic look |
| N55906 | 2025-09-03 | 404 | September 2025 window sweep (n1098l side) - not a claimed date, a systematic look |
| N55906 | 2025-09-04 | 404 | September 2025 window sweep (n1098l side) - not a claimed date, a systematic look |
| N55906 | 2025-09-05 | 404 | September 2025 window sweep (n1098l side) - not a claimed date, a systematic look |
| N55906 | 2025-09-06 | 404 | September 2025 window sweep (n1098l side) - not a claimed date, a systematic look |
| N55906 | 2025-09-07 | 404 | September 2025 window sweep (n1098l side) - not a claimed date, a systematic look |
| N55906 | 2025-09-08 | 404 | September 2025 window sweep (n1098l side) - not a claimed date, a systematic look |
| N55906 | 2025-09-09 | 404 | September 2025 window sweep (n1098l side) - not a claimed date, a systematic look |
| N55906 | 2025-09-10 | 404 | September 2025 window sweep (n1098l side) - not a claimed date, a systematic look |
| N55906 | 2025-09-11 | 404 | September 2025 window sweep (n1098l side) - not a claimed date, a systematic look |
| N55906 | 2025-09-12 | 404 | September 2025 window sweep (n1098l side) - not a claimed date, a systematic look |
| N55906 | 2025-09-13 | 404 | September 2025 window sweep (n1098l side) - not a claimed date, a systematic look |
| N55906 | 2025-09-14 | 404 | September 2025 window sweep (n1098l side) - not a claimed date, a systematic look |
| N55906 | 2025-09-15 | 404 | September 2025 window sweep (n1098l side) - not a claimed date, a systematic look |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

Fifteen consecutive September 2025 days returned nothing for N55906 — the longest empty run of any tail in the [Planes section](/Planes/overview) — and that is the single most useful line of evidence on the [N55906 page](/Planes/N55906/overview): it is what a receiver network looks like when the tail being asked about may not be the tail that actually flew. The near-twin [N59906](/Planes/N59906/overview), one digit apart, has a full primary record across the same window, so the honest reading is a probable digit transposition rather than a hidden aircraft, and nothing here supports treating the blank as suppression of the kind alleged around the [foreign leads reportedly blocked](/FBI/Foreign_Leads), the [sealed case evidence](/Legal/Evidence-Sealing-2026) or the [cover-up material](/CoverUp/overview). The lesson generalises: [what a 403 actually means](/Planes/Flight-Data-Recovery/What-A-403-Means) is this site's own record of publishing a removal it had to retract after seven control aircraft returned the identical refusal, and [per-aircraft recovery status](/Planes/Flight-Data-Recovery/Per-Aircraft-Status) now states, tail by tail, how far back each archive reaches before anyone calls a gap a deletion.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [The survey plane one digit away](/Planes/N59906/overview)
* [Independent investigators and X researchers](/Influencers/overview)

</div>
<div>

* [Evidence contradictions across the case](/Other/Evidence-Contradictions)
* [Technology and surveillance claims](/technology_surveillance/overview)
* [What a 403 actually means](/Planes/Flight-Data-Recovery/What-A-403-Means)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
