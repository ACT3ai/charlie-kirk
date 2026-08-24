---
displayed_sidebar: docs
title: "ADS-B gaps for N59906 - claimed flights with no primary trace"
sidebar_label: "ADS-B gaps"
description: "Every claimed N59906 flight date that returned no primary ADS-B trace from the adsb.lol globe history archive, with the exact HTTP result and why we looked."
keywords:
  - "N59906"
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
| N59906 | 2025-09-04 | 404 | September 2025 window sweep (n1098l side) - not a claimed date, a systematic look |
| N59906 | 2025-09-05 | 404 | September 2025 window sweep (n1098l side) - not a claimed date, a systematic look |
| N59906 | 2025-09-07 | 404 | September 2025 window sweep (n1098l side) - not a claimed date, a systematic look |
| N59906 | 2025-09-09 | 404 | September 2025 window sweep (n1098l side) - not a claimed date, a systematic look |
| N59906 | 2025-09-11 | 404 | September 2025 window sweep (n1098l side) - not a claimed date, a systematic look |
| N59906 | 2025-09-12 | 404 | September 2025 window sweep (n1098l side) - not a claimed date, a systematic look |
| N59906 | 2025-09-13 | 404 | September 2025 window sweep (n1098l side) - not a claimed date, a systematic look |
| N59906 | 2025-09-15 | 404 | September 2025 window sweep (n1098l side) - not a claimed date, a systematic look |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

Eight September 2025 dates came back empty for the MARC survey Navajo, and the 10th is not among them — the [five mapping passes over UVU that morning](/Planes/N59906/overview) are confirmed from primary data to the minute, which makes the rows above an audit of a contractor's ordinary working month rather than a hole in anything on the [September 10 flight timeline](/Planes/Sept10-Flight-Timeline). A piston twin flying low survey grids is precisely the aircraft a volunteer receiver network drops in and out of, and reading those blanks as concealment would undercut the far better-supported questions about [who tasked the flight](/technology_surveillance/overview), what its cameras recorded, why none of it appears in the [government evidence record](/gov/overview), and how it squares with the [campus surveillance footage](/cameras/UVU_Surveillance) or the [reported drone counts](/Topics3/Drones/overview). The genuinely striking result is on the parent page and it cuts against the drama: six further 2022 survey days recovered from the free archives show the same mundane contract-mapping pattern, which is exactly what the [recovery effort](/Planes/Flight-Data-Recovery/overview) publishes as prominently as any result that helps a claim — see [per-aircraft status](/Planes/Flight-Data-Recovery/Per-Aircraft-Status).

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [The news helicopter over the same campus](/Planes/N155TV/overview)
* [UVU campus surveillance cameras](/cameras/UVU_Surveillance)
* [Technology and surveillance claims](/technology_surveillance/overview)

</div>
<div>

* [Sixteen drones reported over UVU](/Topics3/Drones/overview)
* [Military drones on video](/Drones/Military_Drones_On_Video)
* [How government evidence was handled](/gov/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
