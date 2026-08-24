---
displayed_sidebar: docs
slug: /Planes/following/overlap/20250707_UT_provo_owens_037/data/MISSING_DATA
title: "ADS-B gaps for overlap 20250707_UT_provo_owens_037"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20250707_UT_provo_owens_037 (7 July 2025 — Provo, UT)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20250707_UT_provo_owens_037"
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
| SU-BND | 2025-07-06 | 404 | overlap OWENS-037 - Provo UT (audited_inaccurate, audit: inaccurate); overlap OWENS-066 - Provo UT (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2025-07-07 | 404 | overlap OWENS-037 - Provo UT (audited_inaccurate, audit: inaccurate); overlap OWENS-066 - Provo UT (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2025-07-08 | 404 | overlap OWENS-037 - Provo UT (audited_inaccurate, audit: inaccurate); overlap OWENS-066 - Provo UT (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

[OWENS-037](/Planes/following/overlap/20250707_UT_provo_owens_037/overview) came back **not heard** — the archives cover 7 July 2025 and hold no trace for [SU-BND](/Planes/SU-BND/overview) at [Provo](/Planes/following/Provo_KPVU_2024-04-19_to_2025-09-13/overview) — and this page is the itemised form of that silence, tail by tail and status code by status code, so the [register](/Planes/following/overlap/overview) never has to summarise it. Not heard is not refuted, and refusing to blur the two is the same rule that governs how this site handles [the reported remote deletion of witness video](/CoverUp/Videos_Deleted_Remotely) and [the county's "no bodycam footage" admission](/court/mirandize/bodycam-grama-no-footage): an absence is a question, not an answer. The most expensive lesson behind that rule is on [what a 403 actually means](/Planes/Flight-Data-Recovery/What-A-403-Means) — this site called a FlightRadar24 page a documented removal, five unrelated control aircraft returned the identical refusal, and the claim was retracted in public; [the recovery hub](/Planes/Flight-Data-Recovery/overview) sets out the control test that caught it.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Overlap recovery across every testable pair](/Planes/Flight-Data-Recovery/Overlap-Recovery)
* [Pressure reported on witnesses over footage](/Censorship/Witness_Footage_Pressure)
* [A law to preserve digital evidence](/Fix/Digital_Evidence)

</div>
<div>

* [Capturing what the tracking sites show today](/Planes/following/apis/browser_capture/knowledge)
* [The cover-up claims, gathered](/CoverUp/overview)
* [Platform evidence and what it shows](/social_media_analysis/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
