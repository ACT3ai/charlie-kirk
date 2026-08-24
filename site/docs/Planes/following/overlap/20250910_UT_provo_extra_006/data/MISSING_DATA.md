---
displayed_sidebar: docs
slug: /Planes/following/overlap/20250910_UT_provo_extra_006/data/MISSING_DATA
title: "ADS-B gaps for overlap 20250910_UT_provo_extra_006"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20250910_UT_provo_extra_006 (10 September 2025 — Provo, UT)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20250910_UT_provo_extra_006"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.114Z by
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
| SU-BND | 2025-09-11 | 404 | overlap EXTRA-006 - Provo UT (audited_accurate, audit: accurate); overlap SITE-006 - Orem (event) / Provo (aircraft) UT (audited_accurate, audit: accurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

This gap file belongs to [EXTRA-006](/Planes/following/overlap/20250910_UT_provo_extra_006/overview), the 10 September [Provo](/Planes/following/Provo_KPVU_2024-04-19_to_2025-09-13/overview) row for [SU-BND](/Planes/SU-BND/overview) — an aircraft that did not fly that day, which is the exact circumstance a volunteer ADS-B network is least able to record, and the [register](/Planes/following/overlap/overview) marks it accordingly. A parked airframe with an intermittent transponder produces silence in an archive and a claim on X at the same time, and separating those two is the same job the site does on [the reported remote deletion of witness videos](/CoverUp/Videos_Deleted_Remotely) and [the county's "no bodycam footage" answer](/court/mirandize/bodycam-grama-no-footage) — plausible, unproven, and worth documenting either way, which is also the argument of [what a 403 actually means](/Planes/Flight-Data-Recovery/What-A-403-Means). The transponder claim itself, reported as coming on about twenty-one minutes before the shot and powering down an hour after, is set out with its ordinary explanations intact on [10 September 2025 — Orem](/Planes/following/overlap/20250910_UT_orem/overview).

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [The Israel thread of the aircraft investigation](/Planes/Israel-Planes)
* [Which open flight sources hold history](/Planes/following/apis/public_open_source/knowledge)
* [Cover-up claims, gathered in one place](/CoverUp/overview)

</div>
<div>

* [Technology and surveillance claims](/technology_surveillance/overview)
* [Foreign intelligence involvement claims](/Theories/Foreign_Intelligence_Claims)
* [Everything flagged suspicious, by actor](/Suspicious/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
