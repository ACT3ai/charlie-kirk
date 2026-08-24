---
displayed_sidebar: docs
slug: /Planes/following/overlap/20230210_DE_wilmington_owens_009/data/MISSING_DATA
title: "ADS-B gaps for overlap 20230210_DE_wilmington_owens_009"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20230210_DE_wilmington_owens_009 (10 February 2023 — Wilmington, DE)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20230210_DE_wilmington_owens_009"
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
| SU-BTT | 2023-02-09 | 404 | overlap OWENS-009 - Wilmington DE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-02-10 | 404 | overlap OWENS-009 - Wilmington DE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-02-11 | 404 | overlap OWENS-009 - Wilmington DE (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

Wilmington again, and again untestable from free data — [row OWENS-009](/Planes/following/overlap/20230210_DE_wilmington_owens_009/overview) was marked inaccurate on paid archives, the 404s above for [SU-BTT](/Planes/SU-BTT/overview) neither support nor contest that, and it is the status most of the sheet's first eighteen months share on the [overlap index](/Planes/following/overlap/overview), at a field [whose record shows outbound legs only](/Planes/following/Wilmington_KILG_2022-11-17_to_2025-10-12/overview). The reason to keep publishing pages like this one is that a documented gap is itself evidence about the record-keeping, and this case has a great deal of that — [warrants sealed into 2026](/Legal/Evidence-Sealing-2026), a [gag order issued on the court's own motion](/Censorship/Court_Gag_Orders), and the [withheld files the Vote page uses to score lawmakers](/Vote/overview). Then read [what a 403 actually means](/Planes/Flight-Data-Recovery/What-A-403-Means), the page where this site retracts its own published finding that a FlightRadar24 page had been removed — five unrelated control aircraft failed the identical way and the claim did not survive, which is the standard [flight data recovery](/Planes/Flight-Data-Recovery/overview) now applies to everything.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Censorship across platforms and courts](/Censorship/overview)
* [Legal investigation and evidence handling](/legal_investigation/overview)
* [What citizens can do about it](/Your_Actions_Fix_It/overview)

</div>
<div>

* [Capturing what the tracking sites show today](/Planes/following/apis/browser_capture/knowledge)
* [Government records — FOIA and GRAMA routes](/Planes/following/apis/government/knowledge)
* [Government handling of the evidence](/gov/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
