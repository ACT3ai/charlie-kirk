---
displayed_sidebar: docs
slug: /Planes/following/overlap/20240310_MO_st_louis_owens_053/data/MISSING_DATA
title: "ADS-B gaps for overlap 20240310_MO_st_louis_owens_053"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20240310_MO_st_louis_owens_053 (10 March 2024 — St. Louis, MO)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20240310_MO_st_louis_owens_053"
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
| SU-BTT | 2024-03-09 | 404 | overlap OWENS-053 - St. Louis MO (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-03-10 | 404 | overlap OWENS-053 - St. Louis MO (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-03-11 | 404 | overlap OWENS-053 - St. Louis MO (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

Three covered dates and no trace of [SU-BTT](/Planes/SU-BTT/overview) is what this page records for [OWENS-053](/Planes/following/overlap/20240310_MO_st_louis_owens_053/overview), and the [overlap index](/Planes/following/overlap/overview) files it untested — the [free archives](/Planes/following/apis/public_open_source/knowledge) were serving normally, so the silence belongs to the airframe rather than the network, and the [St. Louis record](/Planes/following/StLouis_KSTL_2022-12-20_to_2025-02-23/overview) holds the visits that were real. Twenty-two of the eighty-five rows checked in the August 2026 run landed exactly here, a bigger number than either side of this argument usually admits, and the reason the [cover-up section](/CoverUp/overview), the [Israel thread](/Israel/overview) and the [proposed disclosure laws](/laws/) all lean on records nobody has yet produced. For the fix, read the [commercial flight-data APIs page](/Planes/following/apis/proprietary/knowledge): Flightradar24 and FlightAware hold the deep history the volunteer networks do not, including the whole 2022 window this spreadsheet starts in, and it prices what settling the question would actually cost.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Commercial APIs and what they would settle](/Planes/following/apis/proprietary/knowledge)
* [St. Louis, 2022 to 2025](/Planes/following/StLouis_KSTL_2022-12-20_to_2025-02-23/overview)
* [Cover-up section hub](/CoverUp/overview)

</div>
<div>

* [The four proposed disclosure laws](/laws/)
* [The Israel section](/Israel/overview)
* [Voting and civic response](/Vote/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
