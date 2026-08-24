---
displayed_sidebar: docs
slug: /Planes/following/overlap/20230503_MO_st_louis_owens_014/data/MISSING_DATA
title: "ADS-B gaps for overlap 20230503_MO_st_louis_owens_014"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20230503_MO_st_louis_owens_014 (3 May 2023 — St. Louis, MO)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20230503_MO_st_louis_owens_014"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.110Z by
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
| SU-BND | 2023-05-02 | 404 | overlap OWENS-014 - St. Louis MO (audited_accurate, audit: accurate) |
| SU-BND | 2023-05-04 | 404 | overlap OWENS-014 - St. Louis MO (audited_accurate, audit: accurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

This gap list belongs to one of the rows that survived the check — [OWENS-014](/Planes/following/overlap/20230503_MO_st_louis_owens_014/overview) put [SU-BND](/Planes/SU-BND/overview) within 6.7 km of St Louis Downtown on 3 May 2023 — and the 404s recorded here are for the adjacent days, which the [free archives](/Planes/following/apis/public_open_source/knowledge) simply did not hold, as the [St. Louis record](/Planes/following/StLouis_KSTL_2022-12-20_to_2025-02-23/overview) and the [overlap index](/Planes/following/overlap/overview) both flag. A confirmed aircraft position is still only half a pairing, which is why the human side of this investigation runs through [Erika Kirk's reportedly erased flight logs](/Planes/Erika-Flight-Logs-Erased), the [withheld foreign flight records](/CoverUp/Foreign_Flight_Records) and the [foreign-nexus review Joe Kent says was stopped](/US_Intelligence/joe-kent) rather than through ADS-B at all. The page to read next is [Erika Kirk's own invitation to check the logs](/Planes/following/Erika_Flight_Log_Invitation) — she said on camera to go through them, and researchers report the [N102DZ](/Planes/N102DZ/overview) history was pulled from FlightRadar24 in May 2026.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [St. Louis arrivals, 2022 to 2025](/Planes/following/StLouis_KSTL_2022-12-20_to_2025-02-23/overview)
* [Erika Kirk's flight logs, reported erased](/Planes/Erika-Flight-Logs-Erased)
* [Joe Kent on the halted foreign inquiry](/US_Intelligence/joe-kent)

</div>
<div>

* [Foreign-nexus flight records withheld](/CoverUp/Foreign_Flight_Records)
* [The cover-up claims, section hub](/CoverUp/overview)
* [Geopolitical and intel-service motive](/Motive/Geopolitical_Intel_Service_Theories)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
