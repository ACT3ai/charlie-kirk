---
displayed_sidebar: docs
slug: /Planes/following/overlap/20250720_NE_lincoln_owens_067/data/MISSING_DATA
title: "ADS-B gaps for overlap 20250720_NE_lincoln_owens_067"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20250720_NE_lincoln_owens_067 (20 July 2025 — Lincoln, NE)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20250720_NE_lincoln_owens_067"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.124Z by
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
| SU-BTT | 2025-07-21 | 404 | day after claimed departure from Le Bourget (LFPB); overlap OWENS-038 - Omaha / Lincoln NE (audited_partial, audit: partial); overlap OWENS-067 - Lincoln NE (audited_accurate, audit: accurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

[OWENS-067](/Planes/following/overlap/20250720_NE_lincoln_owens_067/overview) is a confirmed row — [SU-BTT](/Planes/SU-BTT/overview) really was at [Lincoln](/Planes/following/Lincoln_KLNK_2024-02-09_to_2025-10-11/overview) on 20 July 2025 — and this file records the surrounding days where the archives held nothing, published so the confirmation is never read as coverage it does not have; the [register](/Planes/following/overlap/overview) carries both halves. That is the method of the [flight-data recovery work](/Planes/Flight-Data-Recovery/overview): say which of the three things a blank actually is, never let a refusal read as a deletion, and run a control aircraft before publishing — a discipline the official record here has not matched, from [the sealed warrant calendar](/Legal/Evidence-Sealing-2026) to [the gag order a judge reportedly issued on his own motion](/Censorship/Court_Gag_Orders). [Per-aircraft recovery status](/Planes/Flight-Data-Recovery/Per-Aircraft-Status) goes tail by tail through what each source still holds and how far back it reaches — including the free ADS-B Exchange sample that is the only route into 2022, one day in thirty.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Overlap recovery, pair by pair](/Planes/Flight-Data-Recovery/Overlap-Recovery)
* [What a 403 actually means](/Planes/Flight-Data-Recovery/What-A-403-Means)
* [State v. Tyler Robinson, the court file](/court/overview)

</div>
<div>

* [Official statements made and retracted](/Legal/Official-Statements)
* [Law 1: forced disclosure by DoJ and FBI](/laws/DoJ_FBI/Law_1_DoJ_FBI)
* [How government entities handled evidence](/gov/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
