---
displayed_sidebar: docs
slug: /Planes/following/overlap/20230406_DE_wilmington_owens_011/data/MISSING_DATA
title: "ADS-B gaps for overlap 20230406_DE_wilmington_owens_011"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20230406_DE_wilmington_owens_011 (6 April 2023 — Wilmington, DE)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20230406_DE_wilmington_owens_011"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.117Z by
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
| SU-BTT | 2023-04-05 | 404 | overlap OWENS-011 - Wilmington DE (audited_accurate, audit: accurate) |
| SU-BTT | 2023-04-07 | 404 | overlap OWENS-011 - Wilmington DE (audited_accurate, audit: accurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

The row above this log came back confirmed on free data — [SU-BTT](/Planes/SU-BTT/overview) closing to 1.63 kilometres of Wilmington after departing Spirit of St. Louis — so what is listed here are the empty neighbouring dates, and [the row page](/Planes/following/overlap/20230406_DE_wilmington_owens_011/overview) carries the trace itself, indexed with the rest on the [overlap index](/Planes/following/overlap/overview). The confirmation sharpens the counterargument rather than the accusation: Wilmington is the outbound customs stop, [twenty-one appearances and never once inbound](/Planes/following/Wilmington_KILG_2022-11-17_to_2025-10-12/overview), so a precisely-placed aircraft here is precisely placed at a fuel stop — and being willing to publish the result that weakens the claim is the same standard applied to [the inconclusive ATF fragment comparison](/Gun_Bullet/ATF_Fragment_Inconclusive) and to [the contradictions catalogued in Other](/Other/Evidence-Contradictions). For the rest of that run, [overlap recovery](/Planes/Flight-Data-Recovery/Overlap-Recovery) has every one of the 69 testable pairs with its verdict, and [what a 403 actually means](/Planes/Flight-Data-Recovery/What-A-403-Means) has the retraction that made the method trustworthy.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Gun and bullet analysis](/Gun_Bullet/overview)
* [Proof it was not Tyler Robinson](/Proof_Not_Tyler/overview)
* [Legal proceedings and access](/Legal/overview)

</div>
<div>

* [Per-aircraft recovery status](/Planes/Flight-Data-Recovery/Per-Aircraft-Status)
* [Erika Kirk's flights as claimed on X](/Planes/following/Erika_Kirk_Flights)
* [Witnesses at UVU](/Witnesses/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
