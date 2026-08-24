---
displayed_sidebar: docs
slug: /Planes/following/overlap/20250315_KS_wichita_owens_063/data/MISSING_DATA
title: "ADS-B gaps for overlap 20250315_KS_wichita_owens_063"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20250315_KS_wichita_owens_063 (15 March 2025 — Wichita, KS)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20250315_KS_wichita_owens_063"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.124Z by
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
| SU-BTT | 2025-03-14 | 404 | overlap OWENS-033 - Wichita KS (audited_inaccurate, audit: inaccurate); overlap OWENS-063 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2025-03-15 | 404 | overlap OWENS-033 - Wichita KS (audited_inaccurate, audit: inaccurate); overlap OWENS-063 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2025-03-16 | 404 | overlap OWENS-033 - Wichita KS (audited_inaccurate, audit: inaccurate); overlap OWENS-063 - Wichita KS (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

This is the second gap file for one date, because [row OWENS-063](/Planes/following/overlap/20250315_KS_wichita_owens_063/overview) duplicates [row OWENS-033](/Planes/following/overlap/20250315_KS_wichita_owens_033/overview), the same 15 March 2025 [Wichita](/Planes/following/Wichita_KICT_2022-11-13_to_2025-08-03/overview) cell scored twice, and both copies returned nothing from the free archives, [which settles nothing about the aircraft](/Planes/Flight-Data-Recovery/What-A-403-Means). Double-scoring a cell that also carries an unsupported Charlie-present flag is the worst combination on the sheet, and it gets weaponised in both directions, by people using it to dismiss the whole foreign question and by people citing the total without ever reading a row, as [the press record](/Planes/following/Press_Coverage) and [the platform record](/social_media_analysis/overview) both show, and as [the numbers reaching the aggregators](/Planes/following/AI_Assistant_Answers) demonstrate. For the underlying dispute rather than the arithmetic, read [the Candace Owens broadcasts](/Planes/following/Candace_Owens_Broadcasts) with their on-air revisions from 68 to 73, then [the defamation case now attached to it](/Defamation/Brian_Harpole_Candace_Defemation) and [the wider defamation section](/Defamation/overview).

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [The Candace Owens broadcasts](/Planes/following/Candace_Owens_Broadcasts)
* [Harpole v. Owens, the defamation case](/Defamation/Brian_Harpole_Candace_Defemation)
* [The defamation section](/Defamation/overview)

</div>
<div>

* [Influencers and independent researchers](/Influencers/overview)
* [Media response analysis](/Media/overview)
* [Censorship across the investigation](/Censorship/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
