---
displayed_sidebar: docs
slug: /Planes/following/overlap/20250817_NE_omaha_lincoln_owens_039/data/MISSING_DATA
title: "ADS-B gaps for overlap 20250817_NE_omaha_lincoln_owens_039"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20250817_NE_omaha_lincoln_owens_039 (17 August 2025 — Omaha / Lincoln, NE)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20250817_NE_omaha_lincoln_owens_039"
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
| SU-BTT | 2025-08-18 | 404 | day after claimed departure from Le Bourget (LFPB); overlap OWENS-039 - Omaha / Lincoln NE (audited_partial, audit: partial) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

The blank lookups for [OWENS-039](/Planes/following/overlap/20250817_NE_omaha_lincoln_owens_039/overview) — 17 August 2025, [SU-BTT](/Planes/SU-BTT/overview), the last [Lincoln](/Planes/following/Lincoln_KLNK_2024-02-09_to_2025-10-11/overview) rotation before Charlie Kirk was killed — are listed here rather than folded into the row's verdict, because a checked-and-empty date and an unchecked date are not the same claim. Three weeks after this rotation the aircraft thread arrives at [10 September](/Topic-Analyses/September_10_Event_Timeline), where the questions stop being about maintenance schedules and become questions about [what the intelligence services knew](/Proof_Intel_Services/overview) and [why a foreign-nexus review was reportedly stopped](/FBI/Foreign_Leads). [The 73 overlaps](/Planes/following/73_overlaps) shows what this rotation looked like before anyone tested it — every date, city, airport and tail the spreadsheet published, reconstructed line by line and now carrying [a primary-data verdict each](/Planes/following/overlap/overview).

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Provo, April 2024 to September 2025](/Planes/following/Provo_KPVU_2024-04-19_to_2025-09-13/overview)
* [The flight-data recovery hub](/Planes/Flight-Data-Recovery/overview)
* [Pre-assassination context, September 3 to 9](/Topic-Analyses/Pre_Assassination_Context)

</div>
<div>

* [Heightened political tension before UVU](/Before/Heightened-Political-Tensions)
* [The chronological hub for the whole case](/Timeline/overview)
* [Everything flagged suspicious, sorted by actor](/Suspicious/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
