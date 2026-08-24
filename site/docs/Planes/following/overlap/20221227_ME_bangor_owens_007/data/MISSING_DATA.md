---
displayed_sidebar: docs
slug: /Planes/following/overlap/20221227_ME_bangor_owens_007/data/MISSING_DATA
title: "ADS-B gaps for overlap 20221227_ME_bangor_owens_007"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20221227_ME_bangor_owens_007 (27 December 2022 — Bangor, ME)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20221227_ME_bangor_owens_007"
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
| SU-BTT | 2022-12-26 | 404 | overlap OWENS-007 - Bangor ME (audited_accurate, audit: accurate) |
| SU-BTT | 2022-12-27 | 404 | overlap OWENS-007 - Bangor ME (audited_accurate, audit: accurate) |
| SU-BTT | 2022-12-28 | 404 | overlap OWENS-007 - Bangor ME (audited_accurate, audit: accurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

Bangor is a transatlantic fuel stop, and [row OWENS-007](/Planes/following/overlap/20221227_ME_bangor_owens_007/overview) is one the audit upheld on aircraft position even though the free archives above returned nothing for [SU-BTT](/Planes/SU-BTT/overview) — the same pattern as [Goose Bay](/Planes/following/GooseBay_CYYR_2023-05-09_to_2025-09-13/overview), where the two Egyptian Gulfstreams crossed the Atlantic and the three Falcons never did, and the same status the [overlap index](/Planes/following/overlap/overview) records for most of 2022. Route geography is the strongest counterargument in this whole thread and it deserves stating as plainly as the accusation: fuel stops, customs fields and maintenance shops explain a great deal, which is why the case's more durable claims are the ones with paperwork — [the DoD purchase order for miniaturized demolition charges](/Mic/DoD_Contract), [the ATF fragment comparison that came back inconclusive](/Gun_Bullet/ATF_Fragment_Inconclusive), the [court filings tracked under Legal](/Legal/overview). For the aircraft version of a paperwork claim, [Law 2](/laws/US_Intel/Law_2_US_Intel) names SU-BTT, SU-BND, SU-BTU and SU-BGM explicitly and would require the intelligence community to say what, if anything, it holds on them — a far firmer footing than [the 73 overlaps](/Planes/following/73_overlaps) tally.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Paris–Le Bourget — eighteen recorded stops](/Planes/following/Paris_LFPB_2022-10-05_to_2025-10-05/overview)
* [The exploding-mic theory hub](/Mic/overview)
* [Medical, autopsy, and forensic questions](/Medical/overview)

</div>
<div>

* [Aircraft costs — what each plane is worth new](/Planes/Aircraft-Costs/overview)
* [The four forced-disclosure laws](/laws/)
* [Your actions — what to do about it](/Your_Actions_Fix_It/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
