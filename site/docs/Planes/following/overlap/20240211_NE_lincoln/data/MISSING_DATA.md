---
displayed_sidebar: docs
slug: /Planes/following/overlap/20240211_NE_lincoln/data/MISSING_DATA
title: "ADS-B gaps for overlap 20240211_NE_lincoln"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20240211_NE_lincoln (11 February 2024 — Lincoln, Nebraska)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20240211_NE_lincoln"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.120Z by
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
| SU-BTT | 2024-02-10 | 404 | overlap OWENS-020 - Omaha / Lincoln NE (audited_partial, audit: partial); overlap SITE-002 - Lincoln NE (audited_partial, audit: partial) |
| SU-BTT | 2024-02-11 | 404 | overlap SITE-002 - Lincoln NE (audited_partial, audit: partial) |
| SU-BTT | 2024-02-12 | 404 | overlap SITE-002 - Lincoln NE (audited_partial, audit: partial) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

Three covered days and three empty results is the whole finding here, and it is a real one: the [free archives](/Planes/following/apis/public_open_source/knowledge) held 10, 11 and 12 February 2024 for a control basket and heard nothing from [SU-BTT](/Planes/SU-BTT/overview), leaving [the Lincoln chapter row](/Planes/following/overlap/20240211_NE_lincoln/overview) neither supported nor refuted inside the [overlap index](/Planes/following/overlap/overview). That result is compatible with a jet parked in a maintenance hangar and with a jet running dark, and this case has no shortage of places where those two readings collide — the [transponder claims](/Theories/Foreign_Intelligence_Claims), the [airborne surveillance records withheld over UVU](/CoverUp/Airborne_Surveillance_Records), the [drone reports](/Drones/overview). Read [the Lincoln location page](/Planes/following/Lincoln_KLNK_2024-02-09_to_2025-10-11/overview): Duncan Aviation has held the Egyptian Air Force's maintenance contract since 1999 and its headquarters plant is on that field, the strongest innocent explanation anywhere in this directory.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Lincoln and the Duncan Aviation contract](/Planes/following/Lincoln_KLNK_2024-02-09_to_2025-10-11/overview)
* [Open flight data — what the free sources hold](/Planes/following/apis/public_open_source/knowledge)
* [Airborne surveillance records withheld](/CoverUp/Airborne_Surveillance_Records)

</div>
<div>

* [Drones over UVU](/Drones/overview)
* [Foreign intelligence claims](/Theories/Foreign_Intelligence_Claims)
* [Companies and organizations](/Companies_Organizations/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
