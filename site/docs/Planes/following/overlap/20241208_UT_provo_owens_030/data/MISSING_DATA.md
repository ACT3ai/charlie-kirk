---
displayed_sidebar: docs
slug: /Planes/following/overlap/20241208_UT_provo_owens_030/data/MISSING_DATA
title: "ADS-B gaps for overlap 20241208_UT_provo_owens_030"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20241208_UT_provo_owens_030 (8 December 2024 — Provo, UT)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20241208_UT_provo_owens_030"
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
| SU-BND | 2024-12-08 | 404 | overlap OWENS-030 - Provo UT (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2024-12-09 | 404 | overlap OWENS-030 - Provo UT (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

These are the lookups for [row OWENS-030](/Planes/following/overlap/20241208_UT_provo_owens_030/overview), a December 2024 Provo claim the audit answered with one word, Cairo, and the empty archive results add nothing to it because [a free network holding no trace is not evidence about the aircraft](/Planes/Flight-Data-Recovery/What-A-403-Means), a rule applied identically across [every gap file in this directory](/Planes/following/overlap/overview) and [the recovery hub](/Planes/Flight-Data-Recovery/overview). December 2024 is not an idle month elsewhere in this case, because [researchers report an Israeli-geography search spike for the attorney who would later defend the accused](/GoogleSearches/kathryn-nester-searches) months before the shooting, the kind of dated, checkable claim the aircraft rows mostly are not, and it belongs to [a different thread entirely](/GoogleSearches/overview). For the Utah aircraft record that does hold, read [the Provo arrival log](/Planes/following/Provo_KPVU_2024-04-19_to_2025-09-13/overview) and then [Overlap Recovery](/Planes/Flight-Data-Recovery/Overlap-Recovery), which says which of those aircraft-days now have a primary trace and which are gone unless [the paid archives open](/Planes/following/apis/proprietary/knowledge).

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Kathryn Nester and the December 2024 spike](/GoogleSearches/kathryn-nester-searches)
* [The Google searches section](/GoogleSearches/overview)
* [Provo arrivals, 2024 to 2025](/Planes/following/Provo_KPVU_2024-04-19_to_2025-09-13/overview)

</div>
<div>

* [Before September 10, the run-up](/Before/overview)
* [Legal proceedings and defense counsel](/Legal/overview)
* [Key individuals roster](/key_individuals/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
