---
displayed_sidebar: docs
slug: /Planes/following/overlap/20250322_KS_wichita_owens_034/data/MISSING_DATA
title: "ADS-B gaps for overlap 20250322_KS_wichita_owens_034"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20250322_KS_wichita_owens_034 (22 March 2025 — Wichita, KS)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20250322_KS_wichita_owens_034"
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
| SU-BTT | 2025-03-21 | 404 | overlap OWENS-034 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2025-03-22 | 404 | overlap OWENS-034 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2025-03-23 | 404 | overlap OWENS-034 - Wichita KS (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

The three empty lookups here belong to [row OWENS-034](/Planes/following/overlap/20250322_KS_wichita_owens_034/overview), a 22 March 2025 [Wichita](/Planes/following/Wichita_KICT_2022-11-13_to_2025-08-03/overview) claim already recorded as inaccurate, so this file documents a limit of the free archives rather than a discovery, which is how [every gap report in this directory](/Planes/following/overlap/overview) is meant to be read alongside [what a 403 actually means](/Planes/Flight-Data-Recovery/What-A-403-Means). The sheet moves on after this date but the underlying question does not, because no manifest, FBO log, crew list or badge record has ever been obtained for any leg of any of these flights, which puts the aircraft thread in the same category as [the withheld foreign-nexus material](/CoverUp/Foreign_Flight_Records), [the sealed forensic record](/Legal/Evidence-Sealing-2026), and [the reportedly halted intelligence review](/FBI/Foreign_Leads). End at [Flight Data Recovery](/Planes/Flight-Data-Recovery/overview), where sixteen aircraft were checked against four free backup routes, one genuine page removal was found and one loudly published removal claim had to be retracted after a control test, and the retraction is the most useful thing on it, more useful than [the total this row belongs to](/Planes/following/73_overlaps) or [the claims still circulating about it](/Planes/following/x_discussions).

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Flight Data Recovery, what was erased and what was not](/Planes/Flight-Data-Recovery/overview)
* [Foreign flight records withheld](/CoverUp/Foreign_Flight_Records)
* [Evidence sealed into 2026](/Legal/Evidence-Sealing-2026)

</div>
<div>

* [FBI, foreign leads blocked](/FBI/Foreign_Leads)
* [What citizens can actually do about it](/Your_Actions_Fix_It/overview)
* [Government organizations map](/government_organizations/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
