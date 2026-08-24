---
displayed_sidebar: docs
slug: /Planes/following/overlap/20240209_NE_omaha_lincoln_owens_020/data/MISSING_DATA
title: "ADS-B gaps for overlap 20240209_NE_omaha_lincoln_owens_020"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20240209_NE_omaha_lincoln_owens_020 (9 February 2024 — Omaha / Lincoln, NE)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20240209_NE_omaha_lincoln_owens_020"
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

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

The single empty lookup on this page belongs to a row that did not need it: [OWENS-020](/Planes/following/overlap/20240209_NE_omaha_lincoln_owens_020/overview) is a confirmation, with [SU-BTT](/Planes/SU-BTT/overview) closing to 0.31 km of [Omaha](/Planes/following/Omaha_KOMA_2024-02-09_to_2025-10-05/overview) on 9 February 2024 and both archives holding the same Paris-to-[Lincoln](/Planes/following/Lincoln_KLNK_2024-02-09_to_2025-10-11/overview) track, as the [overlap index](/Planes/following/overlap/overview) records. A confirmed position still places no person aboard, which is why the human half of every one of these rows has to come from somewhere else — [Instagram-derived locations](/Planes/following/Erika_Location_From_Instagram), a [reported erasure of the flight logs](/Planes/Erika-Flight-Logs-Erased), a [Turning Point event calendar](/TPUSA/overview) that names organisations rather than passengers, and a [key-individuals roster](/key_individuals/overview) assembled from public reporting. Worth the click: [Overlap Recovery](/Planes/Flight-Data-Recovery/Overlap-Recovery), where all 69 testable aircraft-and-date pairs were pulled against both free archives at once and twenty-three came back with a primary trace for the first time.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Overlap recovery — all 69 testable pairs](/Planes/Flight-Data-Recovery/Overlap-Recovery)
* [Omaha, February 2024 to October 2025](/Planes/following/Omaha_KOMA_2024-02-09_to_2025-10-05/overview)
* [Turning Point USA](/TPUSA/overview)

</div>
<div>

* [Key individuals roster](/key_individuals/overview)
* [Legal investigation hub](/legal_investigation/overview)
* [What a citizen can actually do](/Your_Actions_Fix_It/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
