---
displayed_sidebar: docs
slug: /Planes/following/overlap/20230401_MO_st_louis_owens_010/data/MISSING_DATA
title: "ADS-B gaps for overlap 20230401_MO_st_louis_owens_010"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20230401_MO_st_louis_owens_010 (1 April 2023 — St. Louis, MO)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20230401_MO_st_louis_owens_010"
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
| SU-BTT | 2023-04-02 | 404 | overlap OWENS-010 - St. Louis MO (audited_accurate, audit: accurate); overlap SITE-001 - Jefferson City (event) / St. Louis (aircraft) MO (audited_accurate, audit: accurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

The row this belongs to came back confirmed, and it is one of the better results in the whole run — [SU-BTT](/Planes/SU-BTT/overview) closing to 0.48 kilometres of Lambert International on 1 April 2023, both archives agreeing, on a track that starts at an airfield in France and stages through [Paris–Le Bourget](/Planes/following/Paris_LFPB_2022-10-05_to_2025-10-05/overview) — so read [the row page](/Planes/following/overlap/20230401_MO_st_louis_owens_010/overview) rather than this list, which only records surrounding dates that stayed empty. Note what the row does not claim: neither Kirk is placed here, it is a Turning Point event date, and an aircraft at a field says nothing about who was aboard — the object-versus-person distinction that also governs [the foreign-registered phones logged at UVU](/intelligence/Foreign_Phones_UVU) and every claim in the [Israel main-suspect section](/Israel_Main_Suspect/overview). The following day is the interesting one: [Jefferson City](/Planes/following/overlap/20230402_MO_jefferson_city/overview), where [TPUSA Faith](/Charlie/Leader_of_Churches) launched its tour — and where the page measures 130 miles of driving between the jet and the stage instead of letting the date carry the argument, the test the [overlap index](/Planes/following/overlap/overview) now applies throughout.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [St. Louis field record, 2022 to 2025](/Planes/following/StLouis_KSTL_2022-12-20_to_2025-02-23/overview)
* [Turning Point USA — the organization](/TPUSA/overview)
* [Charlie Kirk as motive anchor](/Charlie/overview)

</div>
<div>

* [Overlap recovery — all 69 pairs tested](/Planes/Flight-Data-Recovery/Overlap-Recovery)
* [AmericaFest and the TPUSA event calendar](/Amfest/overview)
* [Organizations and groups](/organizations_groups/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
