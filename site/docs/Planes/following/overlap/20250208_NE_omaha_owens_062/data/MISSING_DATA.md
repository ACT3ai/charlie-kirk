---
displayed_sidebar: docs
slug: /Planes/following/overlap/20250208_NE_omaha_owens_062/data/MISSING_DATA
title: "ADS-B gaps for overlap 20250208_NE_omaha_owens_062"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20250208_NE_omaha_owens_062 (8 February 2025 — Omaha, NE)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20250208_NE_omaha_owens_062"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.123Z by
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
| SU-BTT | 2025-02-07 | 404 | overlap OWENS-062 - Omaha NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2025-02-08 | 404 | overlap OWENS-062 - Omaha NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2025-02-09 | 404 | overlap OWENS-062 - Omaha NE (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

These lookups cover [row OWENS-062](/Planes/following/overlap/20250208_NE_omaha_owens_062/overview), a claimed Paris to [Omaha](/Planes/following/Omaha_KOMA_2024-02-09_to_2025-10-05/overview) to Cairo rotation the audit placed in Egypt, and the 404s recorded here are what a volunteer receiver network looks like over the rural Midwest in winter, [not a finding](/Planes/Flight-Data-Recovery/What-A-403-Means), and filed the same way as [every other gap report in this directory](/Planes/following/overlap/overview). February 2025 is also when [SU-BTV was arriving at Detroit](/Planes/following/Detroit_KDTW_2025-02-03_to_2025-03-30/overview) as an entry point for onward hops to Lincoln and Wichita, a documented movement with no Kirk pairing ever offered for it, the sort of unclaimed fact a count built only from hits will never contain and that [the disclosure laws](/Fix/overview) would put on the record properly. Read [Per-Aircraft Recovery Status](/Planes/Flight-Data-Recovery/Per-Aircraft-Status) next, one section per tail saying what every source still holds and how far back it reaches, and where the 2022 window sits that [no free archive can reach](/Planes/following/apis/proprietary/knowledge), the single largest hole in [the whole following claim](/Planes/Following-Charlie-Erika).

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Detroit, the February 2025 entry point](/Planes/following/Detroit_KDTW_2025-02-03_to_2025-03-30/overview)
* [The four proposed disclosure laws](/Fix/overview)
* [Foreign influence transparency](/Fix/Foreign_Influence)

</div>
<div>

* [Government flight records and the FOIA route](/Planes/following/apis/government/knowledge)
* [How government handled the evidence](/gov/overview)
* [Vote, tracking disclosure votes](/Vote/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
