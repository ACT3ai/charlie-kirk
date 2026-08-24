---
displayed_sidebar: docs
slug: /Planes/following/overlap/20240110_CA_sacramento_owens_019/data/MISSING_DATA
title: "ADS-B gaps for overlap 20240110_CA_sacramento_owens_019"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20240110_CA_sacramento_owens_019 (10 January 2024 — Sacramento, CA)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20240110_CA_sacramento_owens_019"
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
| SU-BTT | 2024-01-09 | 404 | overlap OWENS-019 - Sacramento CA (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-01-10 | 404 | overlap OWENS-019 - Sacramento CA (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-01-11 | 404 | overlap OWENS-019 - Sacramento CA (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

By January 2024 the [free archives](/Planes/following/apis/public_open_source/knowledge) do cover the dates, so the empty results listed here for [SU-BTT](/Planes/SU-BTT/overview) mean something narrower and more interesting than the 2023 gaps: the network was listening and heard nothing, leaving [OWENS-019](/Planes/following/overlap/20240110_CA_sacramento_owens_019/overview) untested inside the [overlap index](/Planes/following/overlap/overview) rather than refuted, and outside the confirmed column of [the 73 overlaps](/Planes/following/73_overlaps). An aircraft in a hangar and an aircraft with its transponder off produce identical silence, worth remembering wherever this case reads a switched-off signal as intent — the [transponder claims at Provo](/Theories/Foreign_Intelligence_Claims), the [N888KG departure](/Planes/N888KG/overview), the [drone reports](/Drones/overview). The page that pays off here is [per-aircraft recovery status](/Planes/Flight-Data-Recovery/Per-Aircraft-Status): one row per tail showing exactly how far back each archive reaches, which turns a shrug into a boundary you can cite.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Per-aircraft recovery status](/Planes/Flight-Data-Recovery/Per-Aircraft-Status)
* [N888KG and the transponder that went dark](/Planes/N888KG/overview)
* [Drone reports around UVU](/Drones/overview)

</div>
<div>

* [Foreign intelligence involvement claims](/Theories/Foreign_Intelligence_Claims)
* [Technology and surveillance](/technology_surveillance/overview)
* [Suspicious, sorted by actor](/Suspicious/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
