---
displayed_sidebar: docs
slug: /Planes/following/overlap/20240428_DE_wilmington_owens_027/data/MISSING_DATA
title: "ADS-B gaps for overlap 20240428_DE_wilmington_owens_027"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20240428_DE_wilmington_owens_027 (28 April 2024 — Wilmington, DE)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20240428_DE_wilmington_owens_027"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.121Z by
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
| SU-BTT | 2024-04-27 | 404 | overlap OWENS-027 - Wilmington DE (audited_accurate, audit: accurate) |
| SU-BTT | 2024-04-29 | 404 | day after claimed departure from Provo (KPVU); overlap OWENS-027 - Wilmington DE (audited_accurate, audit: accurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

The empty lookups here belong to [row OWENS-027](/Planes/following/overlap/20240428_DE_wilmington_owens_027/overview), an outbound [Wilmington](/Planes/following/Wilmington_KILG_2022-11-17_to_2025-10-12/overview) customs stop the audit marked accurate, and they are published for the same reason every gap file in [the overlap directory](/Planes/following/overlap/overview) is: [a claim nobody could check is not a claim that failed](/Planes/Flight-Data-Recovery/overview). Wilmington appears on the outbound leg only, twenty-one times across three years and never inbound, which argues for a customs function rather than a tasking, and that counterweight deserves the same prominence as [the claims that foreign flight records were withheld](/CoverUp/Foreign_Flight_Records), [that foreign leads were shut down](/FBI/Foreign_Leads), and [that a foreign service was involved at all](/Theories/Foreign_Intelligence_Claims). The next click is [the Cairo home-field page](/Planes/following/Cairo_HECA_2022-11-13_to_2025-10-12/overview), because every leg in the record begins and ends in Egypt and the rotation kept running after Charlie Kirk died, a fact that cuts against the following claim and is published here anyway, unlike in [the numbers that travelled through the press](/Planes/following/Press_Coverage) or through [the assistants people asked instead](/Planes/following/AI_Assistant_Answers).

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Wilmington, outbound only, twenty-one times](/Planes/following/Wilmington_KILG_2022-11-17_to_2025-10-12/overview)
* [Foreign intelligence involvement claims](/Theories/Foreign_Intelligence_Claims)
* [Media coverage of the case](/Media/overview)

</div>
<div>

* [Organizations and groups involved](/organizations_groups/overview)
* [Vote, and which lawmakers back disclosure](/Vote/overview)
* [Commercial APIs holding the deep history](/Planes/following/apis/proprietary/knowledge)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
