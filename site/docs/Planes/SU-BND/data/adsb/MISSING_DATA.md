---
displayed_sidebar: docs
title: "ADS-B gaps for SU-BND - claimed flights with no primary trace"
sidebar_label: "ADS-B gaps"
description: "Every claimed SU-BND flight date that returned no primary ADS-B trace from the adsb.lol globe history archive, with the exact HTTP result and why we looked."
keywords:
  - "SU-BND"
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
| SU-BND | 2023-04-01 | 404 | overlap SITE-001 - Jefferson City (event) / St. Louis (aircraft) MO (audited_accurate, audit: accurate) |
| SU-BND | 2023-04-02 | 404 | overlap SITE-001 - Jefferson City (event) / St. Louis (aircraft) MO (audited_accurate, audit: accurate) |
| SU-BND | 2023-04-03 | 404 | overlap SITE-001 - Jefferson City (event) / St. Louis (aircraft) MO (audited_accurate, audit: accurate) |
| SU-BND | 2023-05-02 | 404 | overlap OWENS-014 - St. Louis MO (audited_accurate, audit: accurate) |
| SU-BND | 2023-05-04 | 404 | overlap OWENS-014 - St. Louis MO (audited_accurate, audit: accurate) |
| SU-BND | 2023-05-08 | 404 | day before claimed arrival at Happy Valley-Goose Bay (CYYR); overlap OWENS-015 - St. Louis then Goose Bay MO (audited_accurate, audit: accurate) |
| SU-BND | 2023-05-11 | 404 | overlap OWENS-050 - St. Louis MO (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2023-05-13 | 404 | overlap OWENS-050 - St. Louis MO (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2023-06-11 | 404 | overlap OWENS-016 - Provo UT (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2023-06-12 | 404 | overlap OWENS-016 - Provo UT (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2023-06-13 | 404 | overlap OWENS-016 - Provo UT (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2023-06-24 | 404 | overlap OWENS-052 - Wilmington DE (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2023-06-25 | 404 | overlap OWENS-052 - Wilmington DE (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2023-06-26 | 404 | overlap OWENS-052 - Wilmington DE (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2024-04-20 | 404 | overlap OWENS-025 - Provo UT (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2024-04-22 | 404 | overlap SITE-004 - Salt Lake City (event) / Provo (aircraft) UT (audited_accurate, audit: accurate) |
| SU-BND | 2024-04-23 | 404 | overlap SITE-004 - Salt Lake City (event) / Provo (aircraft) UT (audited_accurate, audit: accurate) |
| SU-BND | 2024-04-24 | 404 | overlap SITE-004 - Salt Lake City (event) / Provo (aircraft) UT (audited_accurate, audit: accurate) |
| SU-BND | 2024-05-02 | 404 | overlap OWENS-056 - St. Louis MO (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2024-05-03 | 404 | overlap OWENS-056 - St. Louis MO (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2024-05-04 | 404 | overlap OWENS-056 - St. Louis MO (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2024-05-09 | 404 | overlap OWENS-057 - St. Louis MO (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2024-05-10 | 404 | overlap OWENS-057 - St. Louis MO (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2024-05-11 | 404 | overlap OWENS-057 - St. Louis MO (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2024-07-16 | 404 | day before claimed arrival at Happy Valley-Goose Bay (CYYR) |
| SU-BND | 2024-12-08 | 404 | overlap OWENS-030 - Provo UT (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2024-12-09 | 404 | overlap OWENS-030 - Provo UT (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2025-04-18 | 404 | overlap OWENS-064 - Provo UT (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2025-04-19 | 404 | overlap OWENS-064 - Provo UT (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2025-04-20 | 404 | overlap OWENS-064 - Provo UT (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2025-05-21 | 404 | day before claimed arrival at Le Bourget (LFPB) |
| SU-BND | 2025-05-24 | 404 | day after claimed departure from Le Bourget (LFPB); overlap OWENS-035 - Provo UT (audited_accurate, audit: accurate); overlap OWENS-065 - Provo UT (audited_accurate, audit: accurate) |
| SU-BND | 2025-07-06 | 404 | overlap OWENS-037 - Provo UT (audited_inaccurate, audit: inaccurate); overlap OWENS-066 - Provo UT (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2025-07-07 | 404 | overlap OWENS-037 - Provo UT (audited_inaccurate, audit: inaccurate); overlap OWENS-066 - Provo UT (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2025-07-08 | 404 | overlap OWENS-037 - Provo UT (audited_inaccurate, audit: inaccurate); overlap OWENS-066 - Provo UT (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2025-09-11 | 404 | overlap EXTRA-006 - Provo UT (audited_accurate, audit: accurate); overlap SITE-006 - Orem (event) / Provo (aircraft) UT (audited_accurate, audit: accurate) |
| SU-BND | 2025-09-16 | 404 | day after claimed departure from Le Bourget (LFPB) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

These are the SU-BND dates the free archives had nothing for, kept beside [the blue plane's record](/Planes/SU-BND/overview) so a reader can see what it does not contain as easily as what it does; the equivalent lists for [SU-BTT](/Planes/SU-BTT/data/adsb/MISSING_DATA), [SU-BTU](/Planes/SU-BTU/data/adsb/MISSING_DATA), [SU-BTV](/Planes/SU-BTV/data/adsb/MISSING_DATA) and [SU-BGM](/Planes/SU-BGM/data/adsb/MISSING_DATA) sit under those tails, and [per-aircraft recovery status](/Planes/Flight-Data-Recovery/Per-Aircraft-Status) records how far back each source actually reaches. Several rows already carry an audit verdict of inaccurate, which tells you more about the claim than any silence does — an unheard day is an unheard day, and the [foreign-intelligence index](/intelligence/Investigation_Index), the [Egyptian jets at Provo](/Proof_Intel_Services/Egyptian_Jets_Provo) argument and the [withheld-records claim](/CoverUp/Foreign_Flight_Records) do not get to borrow it. For the sharpest correction this effort produced, read [what a 403 actually means](/Planes/Flight-Data-Recovery/What-A-403-Means): this site published a removal that was not one, five unrelated control aircraft returned the identical status from the identical URL shape, and the retraction is on the page rather than quietly edited around.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Foreign phones reported at UVU that day](/intelligence/Foreign_Phones_UVU)
* [Joe Kent on the halted foreign inquiry](/Proof_Intel_Services/Joe_Kent_Foreign_Inquiry_Shutdown)
* [Media coverage of the Owens plane claims](/Media/Candace-Owens-Israel-Controversies)

</div>
<div>

* [Provo, every documented Egyptian arrival](/Planes/following/Provo_KPVU_2024-04-19_to_2025-09-13/overview)
* [The Candace Owens broadcasts, show by show](/Planes/following/Candace_Owens_Broadcasts)
* [Law 1 and the foreign-aircraft findings](/laws/DoJ_FBI/Law_1_DoJ_FBI)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
