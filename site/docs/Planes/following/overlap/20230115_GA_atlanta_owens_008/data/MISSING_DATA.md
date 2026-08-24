---
displayed_sidebar: docs
slug: /Planes/following/overlap/20230115_GA_atlanta_owens_008/data/MISSING_DATA
title: "ADS-B gaps for overlap 20230115_GA_atlanta_owens_008"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20230115_GA_atlanta_owens_008 (15 January 2023 — Atlanta, GA)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20230115_GA_atlanta_owens_008"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.116Z by
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
| SU-BTT | 2023-01-14 | 404 | overlap OWENS-008 - Atlanta GA (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-01-15 | 404 | overlap OWENS-008 - Atlanta GA (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-01-16 | 404 | overlap OWENS-008 - Atlanta GA (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

Atlanta is [row OWENS-008](/Planes/following/overlap/20230115_GA_atlanta_owens_008/overview), already marked inaccurate by the paid audit, and the three 404s above are a coverage boundary rather than a second opinion — [the open flight-data page](/Planes/following/apis/public_open_source/knowledge) sets out exactly where the free archives for [SU-BTT](/Planes/SU-BTT/overview) start and stop, and the [overlap index](/Planes/following/overlap/overview) records the row accordingly. Georgia is also a state with no sourced Turning Point appearance anywhere near the date, which drops the row out of [the speaking-events catalog](/Planes/following/speaking/overview) entirely and leaves the claim resting on a spreadsheet cell — the same evidentiary thinness that dogs the [unproduced kill-me screenshots](/Messages/sept-9-they-are-going-to-kill-me), the [anonymous surgeon behind the body-stopped-it story](/People/unnamed-surgeon), and much of what circulates in the [media response](/Media/overview). For the version with receipts, [the September 8 donor group chat](/Messages/sept-8-donor-group-chat) is a rare case where TPUSA's own spokesman reportedly confirmed the texts as genuine.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Messages and threats hub](/Messages/overview)
* [Charlie Kirk's reported quotes and warnings](/Charlie/Reported_Quotes_and_Warnings)
* [Witnesses at UVU](/Witnesses/overview)

</div>
<div>

* [What the compilers counted as an overlap](/Planes/following/Overlap_Window_Definition)
* [TPUSA events beside the aircraft record](/Planes/following/TPUSA_events)
* [Before September 10 — the pressure field](/Before/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
