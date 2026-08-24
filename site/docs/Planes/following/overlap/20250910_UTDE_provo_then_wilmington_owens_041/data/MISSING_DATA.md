---
displayed_sidebar: docs
slug: /Planes/following/overlap/20250910_UTDE_provo_then_wilmington_owens_041/data/MISSING_DATA
title: "ADS-B gaps for overlap 20250910_UTDE_provo_then_wilmington_owens_041"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20250910_UTDE_provo_then_wilmington_owens_041 (10 September 2025 — Provo then Wilmington, UT/DE)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20250910_UTDE_provo_then_wilmington_owens_041"
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
| SU-BTT | 2025-09-09 | 404 | day before claimed arrival at Wilmington (KILG); overlap OWENS-041 - Provo then Wilmington UT/DE (audited_inaccurate, audit: inaccurate); overlap SITE-005 - Wilmington DE (claimed, audit: partial); overlap SITE-006 - Orem (event) / Provo (aircraft) UT (audited_accurate, audit: accurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

These are the archive blanks around [OWENS-041](/Planes/following/overlap/20250910_UTDE_provo_then_wilmington_owens_041/overview), the row that puts both Kirks on the Provo-then-[Wilmington](/Planes/following/Wilmington_KILG_2022-11-17_to_2025-10-12/overview) day; the [SU-BTT](/Planes/SU-BTT/overview) flight is confirmed, the sheet's stated origin was wrong, and the rest of the row is what this file cannot fill in. The two facts nobody has recovered are the ones that would matter most — who was aboard any of these aircraft, and where Erika Kirk actually was, which [the reported erasure of her flight logs](/Planes/Erika-Flight-Logs-Erased) puts out of reach — and the same shape of hole runs through [the sealed device warrants](/Legal/Evidence-Sealing-2026), [the unreleased Form 302 interviews](/analysis_documentation/overview) and [the foreign-nexus review reportedly stopped at NCTC](/Proof_Intel_Services/Joe_Kent_Foreign_Inquiry_Shutdown). [10 September 2025 — Orem](/Planes/following/overlap/20250910_UT_orem/overview) holds the part of that day which is documented to the second: Charlie Kirk shot at 12:23:30 PM MDT, one Egyptian jet gone that morning, a second parked on the same ramp for 110 days with its transponder reportedly cycling twenty-one minutes before the shot.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [The flight-data recovery hub](/Planes/Flight-Data-Recovery/overview)
* [SU-BND, the jet that sat at Provo](/Planes/SU-BND/overview)
* [Provo Municipal Airport](/Locations/Provo_Airport)

</div>
<div>

* [Foreign intelligence involvement claims](/Theories/Foreign_Intelligence_Claims)
* [Indicators of intelligence-service involvement](/Proof_Intel_Services/overview)
* [The government bodies in this case](/government_organizations/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
