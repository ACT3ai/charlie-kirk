---
displayed_sidebar: docs
slug: /Planes/following/overlap/20250904_UT_provo_owens_040/data/MISSING_DATA
title: "ADS-B gaps for overlap 20250904_UT_provo_owens_040"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20250904_UT_provo_owens_040 (4 September 2025 — Provo, UT)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20250904_UT_provo_owens_040"
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
| SU-BTT | 2025-09-05 | 404 | day after claimed departure from Le Bourget (LFPB); overlap OWENS-040 - Provo UT (audited_accurate, audit: accurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

One lookup, one 404: [OWENS-040](/Planes/following/overlap/20250904_UT_provo_owens_040/overview) is a confirmed row in the [register](/Planes/following/overlap/overview) — [SU-BTT](/Planes/SU-BTT/overview) measured 0.16 km from the [Provo](/Planes/following/Provo_KPVU_2024-04-19_to_2025-09-13/overview) ramp on 4 September 2025 — and all this page records is that the following day produced nothing. That single blank sits six days before the killing, in the week when [contractors reportedly carrying "US DoD Liaison" badges](/Locations/Provo_Airport) were said to be dropped at this field and [counter-UAS equipment was reportedly tested there](/technology_surveillance/overview) — claims published here as claims, with no badge list and no test log obtained by anyone. The date all of it converges on is [10 September 2025 — Orem](/Planes/following/overlap/20250910_UT_orem/overview), the only same-day same-airport overlap in the whole record by any definition, including the one [Liz Wheeler](/People/liz-wheeler) uses to cut the tally to a single row.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Where the Egyptian crews reportedly stayed](/Planes/Egyptian-Crew-Hotel)
* [Minot, the 2025 US entry field](/Planes/following/Minot_KMOT_2025-04-08_to_2025-09-04/overview)
* [Drones reported over the campus](/Drones/overview)

</div>
<div>

* [Egyptian foreign operations at Provo](/intelligence/Egyptian_Foreign_Ops)
* [Israel intel flights and UVU](/Israel_Main_Suspect/israel-intel-flights-uvu)
* [Foreign intelligence involvement claims](/Theories/Foreign_Intelligence_Claims)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
