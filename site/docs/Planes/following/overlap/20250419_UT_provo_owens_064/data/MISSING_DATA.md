---
displayed_sidebar: docs
slug: /Planes/following/overlap/20250419_UT_provo_owens_064/data/MISSING_DATA
title: "ADS-B gaps for overlap 20250419_UT_provo_owens_064"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20250419_UT_provo_owens_064 (19 April 2025 — Provo, UT)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20250419_UT_provo_owens_064"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.113Z by
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
| SU-BND | 2025-04-18 | 404 | overlap OWENS-064 - Provo UT (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2025-04-19 | 404 | overlap OWENS-064 - Provo UT (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2025-04-20 | 404 | overlap OWENS-064 - Provo UT (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

This is the empty half of [row OWENS-064](/Planes/following/overlap/20250419_UT_provo_owens_064/overview) — the archive lookups that returned nothing for [SU-BND](/Planes/SU-BND/overview) around 19 April 2025 — published apart from the [overlap register](/Planes/following/overlap/overview) because a claim nobody could check is a different animal from a claim that was checked and failed, and the person named on the row is Erika Kirk, whose [flight logs are reported erased](/Planes/Erika-Flight-Logs-Erased). Silence in a volunteer ADS-B network is the ordinary case — a parked airframe, a receiver-coverage hole, a wrong date — and it carries none of the weight that [the foreign-intelligence claims](/Theories/Foreign_Intelligence_Claims) about these tails or [the Egyptian operations reported at Provo](/intelligence/Egyptian_Foreign_Ops) are asked to bear; [Law 2](/laws/US_Intel/Law_2_US_Intel) would compel the government to say what it actually holds instead. [What a 403 actually means](/Planes/Flight-Data-Recovery/What-A-403-Means) is the page that earned this caution the hard way: this site published a FlightRadar24 page as a documented removal, five unrelated control aircraft returned the identical refusal, and the finding had to be retracted — the method that caught it is set out across [the four free archives](/Planes/Flight-Data-Recovery/overview).

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Per-aircraft recovery status, tail by tail](/Planes/Flight-Data-Recovery/Per-Aircraft-Status)
* [Erika Kirk's flight logs, reported erased](/Planes/Erika-Flight-Logs-Erased)
* [Device warrants reportedly sealed to March 2026](/Legal/Evidence-Sealing-2026)

</div>
<div>

* [The FBI's blocked foreign-nexus leads](/FBI/Foreign_Leads)
* [A law to preserve digital evidence](/Fix/Digital_Evidence)
* [Every company and organization in the case](/Companies_Organizations/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
