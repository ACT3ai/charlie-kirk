---
displayed_sidebar: docs
title: "ADS-B gaps for SU-BGM - claimed flights with no primary trace"
sidebar_label: "ADS-B gaps"
description: "Every claimed SU-BGM flight date that returned no primary ADS-B trace from the adsb.lol globe history archive, with the exact HTTP result and why we looked."
keywords:
  - "SU-BGM"
  - "ADS-B"
  - "flight tracking"
  - "missing flight data"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.109Z by
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
| SU-BGM | 2025-04-15 | 404 | day before claimed arrival at Happy Valley-Goose Bay (CYYR); day before claimed arrival at Le Bourget (LFPB) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

Every row below is a date this investigation went looking for and came back empty-handed on, published beside [the SU-BGM record](/Planes/SU-BGM/overview) so the gaps in it can be argued with rather than taken on trust — the same list exists for [SU-BTT](/Planes/SU-BTT/data/adsb/MISSING_DATA), [SU-BND](/Planes/SU-BND/data/adsb/MISSING_DATA), [SU-BTU](/Planes/SU-BTU/data/adsb/MISSING_DATA) and [SU-BTV](/Planes/SU-BTV/data/adsb/MISSING_DATA), and the four free archives that did answer are set out on [flight data recovery](/Planes/Flight-Data-Recovery/overview) and [per-aircraft recovery status](/Planes/Flight-Data-Recovery/Per-Aircraft-Status). A missing trace is the weakest thing this investigation owns and the easiest to misread, which is why nothing here is offered to the [withheld-foreign-records claim](/CoverUp/Foreign_Flight_Records), the [Egyptian jets at Provo](/Proof_Intel_Services/Egyptian_Jets_Provo) thread, or the [foreign-intelligence angle](/intelligence/overview): a 404 means a volunteer receiver network heard nothing that UTC day, and parked-and-silent, out-of-coverage, or a wrong claimed date all come first. If one page here is worth the click it is [Overlap Recovery](/Planes/Flight-Data-Recovery/Overlap-Recovery), which put all 69 testable aircraft-and-date pairs from the 73-overlap spreadsheet against two independent daily archives and names the twenty-three that now have a primary trace behind them — the remainder still rest on [what the compilers counted as an overlap](/Planes/following/Overlap_Window_Definition), a jet within 50 to 100 miles and plus or minus three days.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Egyptian foreign operations at Provo, 2025](/intelligence/Egyptian_Foreign_Ops)
* [Foreign leads the FBI reportedly blocked](/FBI/Foreign_Leads)
* [Provo Municipal Airport on the ground](/Locations/Provo_Airport)

</div>
<div>

* [What every plane in this case costs new](/Planes/Aircraft-Costs/overview)
* [Law 2 names these tail numbers](/laws/US_Intel/Law_2_US_Intel)
* [Goose Bay, the Gulfstreams' Atlantic crossing](/Planes/following/GooseBay_CYYR_2023-05-09_to_2025-09-13/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
