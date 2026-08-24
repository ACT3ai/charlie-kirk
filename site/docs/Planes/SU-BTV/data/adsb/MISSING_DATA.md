---
displayed_sidebar: docs
title: "ADS-B gaps for SU-BTV - claimed flights with no primary trace"
sidebar_label: "ADS-B gaps"
description: "Every claimed SU-BTV flight date that returned no primary ADS-B trace from the adsb.lol globe history archive, with the exact HTTP result and why we looked."
keywords:
  - "SU-BTV"
  - "ADS-B"
  - "flight tracking"
  - "missing flight data"
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
| SU-BTV | 2024-12-06 | 404 | day before claimed arrival at Le Bourget (LFPB) |
| SU-BTV | 2024-12-09 | 404 | day after claimed departure from Le Bourget (LFPB); day before claimed arrival at Wilmington (KILG) |
| SU-BTV | 2024-12-11 | 404 | day after claimed departure from Wichita (KICT) |
| SU-BTV | 2024-12-16 | 404 | day after claimed departure from Wilmington (KILG) |
| SU-BTV | 2025-02-01 | 404 | day before claimed arrival at Le Bourget (LFPB) |
| SU-BTV | 2025-02-04 | 404 | day after claimed departure from Le Bourget (LFPB) |
| SU-BTV | 2025-02-08 | 404 | day before claimed arrival at Wilmington (KILG) |
| SU-BTV | 2025-02-11 | 404 | day after claimed departure from Wilmington (KILG) |
| SU-BTV | 2025-03-15 | 404 | day before claimed arrival at Le Bourget (LFPB) |
| SU-BTV | 2025-03-18 | 404 | day after claimed departure from Le Bourget (LFPB) |
| SU-BTV | 2025-03-22 | 404 | day before claimed arrival at Wilmington (KILG) |
| SU-BTV | 2025-03-25 | 404 | day after claimed departure from Wilmington (KILG) |
| SU-BTV | 2025-03-28 | 404 | day before claimed arrival at Le Bourget (LFPB) |
| SU-BTV | 2025-03-31 | 404 | day after claimed departure from Le Bourget (LFPB) |
| SU-BTV | 2025-04-02 | 404 | day before claimed arrival at Wilmington (KILG) |
| SU-BTV | 2025-04-04 | 404 | day after claimed departure from Wichita (KICT) |
| SU-BTV | 2025-04-07 | 404 | day after claimed departure from Wilmington (KILG) |
| SU-BTV | 2025-05-25 | 404 | day before claimed arrival at Le Bourget (LFPB) |
| SU-BTV | 2025-05-28 | 404 | day after claimed departure from Le Bourget (LFPB) |
| SU-BTV | 2025-06-01 | 404 | day before claimed arrival at Wilmington (KILG) |
| SU-BTV | 2025-06-04 | 404 | day after claimed departure from Wilmington (KILG) |
| SU-BTV | 2025-07-28 | 404 | day before claimed arrival at Le Bourget (LFPB) |
| SU-BTV | 2025-07-31 | 404 | day after claimed departure from Le Bourget (LFPB) |
| SU-BTV | 2025-08-02 | 404 | day before claimed arrival at Wilmington (KILG) |
| SU-BTV | 2025-08-04 | 404 | day after claimed departure from Wichita (KICT) |
| SU-BTV | 2025-08-07 | 404 | day after claimed departure from Wilmington (KILG) |
| SU-BTV | 2025-10-03 | 404 | day before claimed arrival at Le Bourget (LFPB) |
| SU-BTV | 2025-10-06 | 404 | day after claimed departure from Le Bourget (LFPB) |
| SU-BTV | 2025-10-10 | 404 | day before claimed arrival at Wilmington (KILG) |
| SU-BTV | 2025-10-12 | 403 | day after claimed departure from Lincoln (KLNK); claimed departure from Wilmington (KILG) - flights.csv |
| SU-BTV | 2025-10-13 | 403 | day after claimed departure from Wilmington (KILG) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

The last two rows on this list are 403s rather than 404s, and that difference is most of the reason the page exists — a refusal and a deletion look identical from outside, which [what a 403 actually means](/Planes/Flight-Data-Recovery/What-A-403-Means) demonstrates with five unrelated control aircraft failing in exactly the same way; the rest of [the SU-BTV record](/Planes/SU-BTV/overview) and the fleetmate lists for [SU-BTT](/Planes/SU-BTT/data/adsb/MISSING_DATA), [SU-BND](/Planes/SU-BND/data/adsb/MISSING_DATA), [SU-BTU](/Planes/SU-BTU/data/adsb/MISSING_DATA) and [SU-BGM](/Planes/SU-BGM/data/adsb/MISSING_DATA) are published on the same terms. That discipline is what the rest of the case is entitled to expect from this section, because the [Egyptian jets at Provo](/Proof_Intel_Services/Egyptian_Jets_Provo) thread, the [withheld-foreign-records claim](/CoverUp/Foreign_Flight_Records) and the [foreign-intelligence index](/intelligence/Investigation_Index) all lean on flight data somewhere, and a borrowed absence is worth nothing to any of them. [Overlap Recovery](/Planes/Flight-Data-Recovery/Overlap-Recovery) is the page to read next — 69 testable aircraft-and-date pairs from the 73-overlap spreadsheet, pulled against two independent daily archives, with the pairs that failed reported as plainly as the twenty-three that came back with a primary trace.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Detroit, SU-BTV's early-2025 entry point](/Planes/following/Detroit_KDTW_2025-02-03_to_2025-03-30/overview)
* [Cover-up claims and evidence gaps](/CoverUp/overview)
* [The full case timeline](/Timeline/overview)

</div>
<div>

* [Capturing what the tracking sites showed](/Planes/following/apis/browser_capture/knowledge)
* [Foreign intelligence services hub](/intelligence/overview)
* [What citizens can actually do about it](/Your_Actions_Fix_It/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
