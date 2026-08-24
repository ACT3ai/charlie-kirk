---
displayed_sidebar: docs
slug: /Planes/following/overlap/20230225_MO_st_louis_owens_046/data/MISSING_DATA
title: "ADS-B gaps for overlap 20230225_MO_st_louis_owens_046"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20230225_MO_st_louis_owens_046 (25 February 2023 — St. Louis, MO)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20230225_MO_st_louis_owens_046"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.117Z by
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
| SU-BTT | 2023-02-26 | 404 | overlap OWENS-046 - St. Louis MO (audited_partial, audit: partial) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

This gap log sits under one of the rows that actually came back — free ADS-B put [SU-BTT](/Planes/SU-BTT/overview) within 3.1 kilometres of Spirit of St. Louis on the claimed date, both archives agreeing — so the entries above are the surrounding dates that stayed empty, not the row itself, and [the row page](/Planes/following/overlap/20230225_MO_st_louis_owens_046/overview) carries the confirmed trace alongside [the St. Louis field record](/Planes/following/StLouis_KSTL_2022-12-20_to_2025-02-23/overview). A confirmed aircraft is still only an aircraft: no manifest, crew list or FBO log has been produced for any leg of any of these flights, and [Erika Kirk's flight logs are reported erased](/Planes/Erika-Flight-Logs-Erased), so nothing here places a person aboard — the same limit that separates [the foreign phones logged at UVU](/intelligence/Foreign_Phones_UVU) from an identified user and the [Israel main-suspect case](/Israel_Main_Suspect/overview) from a named actor. The full run is [overlap recovery](/Planes/Flight-Data-Recovery/Overlap-Recovery) — 69 testable aircraft-and-date pairs pulled against both free daily archives, twenty-three landing on a primary trace for the first time, indexed row by row from [the overlap dates page](/Planes/following/overlap/overview).

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Per-aircraft recovery status](/Planes/Flight-Data-Recovery/Per-Aircraft-Status)
* [Foreign intelligence involvement claims](/Theories/Foreign_Intelligence_Claims)
* [US intelligence assisted — the argument](/US_Intelligence_Assisted/overview)

</div>
<div>

* [Open ADS-B sources and their reach](/Planes/following/apis/public_open_source/knowledge)
* [Intelligence services section](/intelligence/overview)
* [Geopolitical and intel-service motive theories](/Motive/Geopolitical_Intel_Service_Theories)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
