---
displayed_sidebar: docs
slug: /Planes/following/overlap/20240510_MO_st_louis_owens_057/data/MISSING_DATA
title: "ADS-B gaps for overlap 20240510_MO_st_louis_owens_057"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20240510_MO_st_louis_owens_057 (10 May 2024 — St. Louis, MO)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20240510_MO_st_louis_owens_057"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.112Z by
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
| SU-BND | 2024-05-09 | 404 | overlap OWENS-057 - St. Louis MO (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2024-05-10 | 404 | overlap OWENS-057 - St. Louis MO (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2024-05-11 | 404 | overlap OWENS-057 - St. Louis MO (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

This gap list belongs to [row OWENS-057](/Planes/following/overlap/20240510_MO_st_louis_owens_057/overview), where the audit put [SU-BND](/Planes/SU-BND/overview) at Provo from 19 April to 17 July while the sheet claimed Missouri, so the archive silence recorded here changes nothing either way, which is the whole reason [the gap files are published separately](/Planes/Flight-Data-Recovery/overview) from the claims and alongside [the St. Louis field record](/Planes/following/StLouis_KSTL_2022-12-20_to_2025-02-23/overview). Behind every one of these 404s sits a paywall or a records request rather than a conspiracy: [the commercial archives hold the deep history](/Planes/following/apis/proprietary/knowledge), [government sources have to be asked for](/Planes/following/apis/government/knowledge), and [nobody has produced the flight and manifest material](/CoverUp/Foreign_Flight_Records) that would end the argument outright. Read [What A 403 Actually Means](/Planes/Flight-Data-Recovery/What-A-403-Means) next, because this site published a removal claim about a tracking page, ran the control test, and retracted it, and that retraction is more useful than the claim was in a case where [contradictions pile up faster than corrections](/Other/Evidence-Contradictions) and [four proposed laws](/Fix/overview) are the only route to the primary record.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Row OWENS-057, the Missouri claim](/Planes/following/overlap/20240510_MO_st_louis_owens_057/overview)
* [Government flight records, download or FOIA](/Planes/following/apis/government/knowledge)
* [The four proposed federal disclosure laws](/Fix/overview)

</div>
<div>

* [Legal proceedings and evidence handling](/Legal/overview)
* [How government handled the evidence](/gov/overview)
* [Cross-cutting topics with no single home](/other_topics/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
