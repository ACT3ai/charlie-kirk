---
displayed_sidebar: docs
slug: /Planes/following/overlap/20230512_MO_st_louis_owens_050/data/MISSING_DATA
title: "ADS-B gaps for overlap 20230512_MO_st_louis_owens_050"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20230512_MO_st_louis_owens_050 (12 May 2023 — St. Louis, MO)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20230512_MO_st_louis_owens_050"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.111Z by
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
| SU-BND | 2023-05-11 | 404 | overlap OWENS-050 - St. Louis MO (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2023-05-13 | 404 | overlap OWENS-050 - St. Louis MO (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

The 404s listed here are the outer days around [OWENS-050](/Planes/following/overlap/20230512_MO_st_louis_owens_050/overview), a row that did not need them to fall: on the claimed date itself both [free archives](/Planes/following/apis/public_open_source/knowledge) hold [SU-BND](/Planes/SU-BND/overview) flying [Paris-Le Bourget](/Planes/following/Paris_LFPB_2022-10-05_to_2025-10-05/overview) to Greece, nowhere near [St Louis](/Planes/following/StLouis_KSTL_2022-12-20_to_2025-02-23/overview). A refutation built on a tracked position is a different object from an empty archive, and keeping the two apart is the same discipline this site applies to [evidence sealed until 2026](/Legal/Evidence-Sealing-2026), [airborne surveillance records withheld over UVU](/CoverUp/Airborne_Surveillance_Records) and the [autopsy that has never been released](/Medical/overview). For the case where this site got that wrong and had to say so, read [what a 403 actually means](/Planes/Flight-Data-Recovery/What-A-403-Means) — a published removal claim collapsed once five control aircraft returned the identical refusal.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Paris-Le Bourget staging stops](/Planes/following/Paris_LFPB_2022-10-05_to_2025-10-05/overview)
* [What a 403 actually means](/Planes/Flight-Data-Recovery/What-A-403-Means)
* [Airborne surveillance records withheld](/CoverUp/Airborne_Surveillance_Records)

</div>
<div>

* [Evidence sealed until 2026](/Legal/Evidence-Sealing-2026)
* [Medical, autopsy and wound questions](/Medical/overview)
* [The legal dimension of the case](/Legal/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
