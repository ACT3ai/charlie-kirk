---
displayed_sidebar: docs
title: "ADS-B gaps for SU-BTU - claimed flights with no primary trace"
sidebar_label: "ADS-B gaps"
description: "Every claimed SU-BTU flight date that returned no primary ADS-B trace from the adsb.lol globe history archive, with the exact HTTP result and why we looked."
keywords:
  - "SU-BTU"
  - "ADS-B"
  - "flight tracking"
  - "missing flight data"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.125Z by
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
| SU-BTU | 2024-11-24 | 404 | day before claimed arrival at Le Bourget (LFPB) |
| SU-BTU | 2024-11-27 | 404 | day after claimed departure from Le Bourget (LFPB) |
| SU-BTU | 2024-11-30 | 404 | day before claimed arrival at Wilmington (KILG) |
| SU-BTU | 2024-12-02 | 404 | day after claimed departure from Lincoln (KLNK) |
| SU-BTU | 2024-12-04 | 404 | day after claimed departure from Wilmington (KILG) |
| SU-BTU | 2025-01-15 | 404 | day before claimed arrival at Le Bourget (LFPB) |
| SU-BTU | 2025-01-18 | 404 | day after claimed departure from Le Bourget (LFPB) |
| SU-BTU | 2025-01-22 | 404 | day before claimed arrival at Wilmington (KILG) |
| SU-BTU | 2025-01-25 | 404 | day after claimed departure from Wilmington (KILG) |
| SU-BTU | 2025-02-14 | 404 | day before claimed arrival at Le Bourget (LFPB) |
| SU-BTU | 2025-02-17 | 404 | day after claimed departure from Le Bourget (LFPB) |
| SU-BTU | 2025-02-21 | 404 | day before claimed arrival at Wilmington (KILG) |
| SU-BTU | 2025-02-24 | 404 | day after claimed departure from Wilmington (KILG) |
| SU-BTU | 2025-04-06 | 404 | day before claimed arrival at Le Bourget (LFPB) |
| SU-BTU | 2025-04-09 | 404 | day after claimed departure from Le Bourget (LFPB) |
| SU-BTU | 2025-04-13 | 404 | day before claimed arrival at Wilmington (KILG) |
| SU-BTU | 2025-04-16 | 404 | day after claimed departure from Wilmington (KILG) |
| SU-BTU | 2025-04-22 | 404 | day before claimed arrival at Le Bourget (LFPB) |
| SU-BTU | 2025-04-25 | 404 | day after claimed departure from Le Bourget (LFPB) |
| SU-BTU | 2025-04-29 | 404 | day before claimed arrival at Wilmington (KILG) |
| SU-BTU | 2025-05-02 | 404 | day after claimed departure from Wilmington (KILG) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

SU-BTU's gap list is short and unusually regular — almost every row is the day before a claimed [Le Bourget](/Planes/following/Paris_LFPB_2022-10-05_to_2025-10-05/overview) arrival or the day after a claimed [Wilmington](/Planes/following/Wilmington_KILG_2022-11-17_to_2025-10-12/overview) departure, which is the shape of ocean crossings flown outside volunteer receiver coverage rather than of anything hidden; [the SU-BTU page](/Planes/SU-BTU/overview) carries what did come back and [per-aircraft recovery status](/Planes/Flight-Data-Recovery/Per-Aircraft-Status) says which archive reaches how far. None of it belongs in the [Egyptian jets at Provo](/Proof_Intel_Services/Egyptian_Jets_Provo) case, the [withheld-foreign-records claim](/CoverUp/Foreign_Flight_Records), or the [Israel foreign-leads thread](/Israel/foreign-leads) — most of the Atlantic and most of North Africa simply go unheard, and this investigation says so before anyone else has to. Read [what a 403 actually means](/Planes/Flight-Data-Recovery/What-A-403-Means) next: it is where this site retracted a removal it had already published, after five unrelated control aircraft returned the same status from the same URL, and it is why the sibling lists for [SU-BTT](/Planes/SU-BTT/data/adsb/MISSING_DATA), [SU-BTV](/Planes/SU-BTV/data/adsb/MISSING_DATA), [SU-BND](/Planes/SU-BND/data/adsb/MISSING_DATA) and [SU-BGM](/Planes/SU-BGM/data/adsb/MISSING_DATA) are published rather than quietly binned.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Wichita, the Dassault service centre](/Planes/following/Wichita_KICT_2022-11-13_to_2025-08-03/overview)
* [Foreign intelligence investigation index](/intelligence/Investigation_Index)
* [Geopolitical and intel-service motive theories](/Motive/Geopolitical_Intel_Service_Theories)

</div>
<div>

* [Everyone named in the following material](/Planes/following/Named_People)
* [Foreign influence transparency reform](/Fix/Foreign_Influence)
* [Provo Municipal Airport on the ground](/Locations/Provo_Airport)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
