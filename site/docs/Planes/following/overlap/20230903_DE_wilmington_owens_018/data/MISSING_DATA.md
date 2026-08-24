---
displayed_sidebar: docs
slug: /Planes/following/overlap/20230903_DE_wilmington_owens_018/data/MISSING_DATA
title: "ADS-B gaps for overlap 20230903_DE_wilmington_owens_018"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20230903_DE_wilmington_owens_018 (3 September 2023 — Wilmington, DE)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20230903_DE_wilmington_owens_018"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.119Z by
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
| SU-BTT | 2023-09-02 | 404 | overlap OWENS-018 - Wilmington DE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-09-03 | 404 | overlap OWENS-018 - Wilmington DE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-09-04 | 404 | overlap OWENS-018 - Wilmington DE (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

Three 404s for [SU-BTT](/Planes/SU-BTT/overview) in early September 2023 stand behind [OWENS-018](/Planes/following/overlap/20230903_DE_wilmington_owens_018/overview), and they are archive-range 404s — the control basket returned the same, so nothing here speaks to the [Wilmington](/Planes/following/Wilmington_KILG_2022-11-17_to_2025-10-12/overview) claim in either direction, as the [overlap index](/Planes/following/overlap/overview) notes. This site publishes its dead ends because a claim that has been tested and failed is a different object from a claim nobody can reach, and that distinction runs straight through the [cover-up allegations](/CoverUp/overview), the [censorship record](/Censorship/overview) and the [account of a witness asked to delete his video](/CoverUp/FBI_Asked_Delete_Video). Read [what a 403 actually means](/Planes/Flight-Data-Recovery/What-A-403-Means) for the case that cost this investigation a published headline: flightradar24.com returns 403 to every scripted client, including its own homepage, while the page loads normally in a browser — the whole reason [browser capture](/Planes/following/apis/browser_capture/knowledge) exists as a separate pass.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [What a 403 actually means](/Planes/Flight-Data-Recovery/What-A-403-Means)
* [Capturing the tracking sites in a real browser](/Planes/following/apis/browser_capture/knowledge)
* [The FBI and a witness's deleted video](/CoverUp/FBI_Asked_Delete_Video)

</div>
<div>

* [Censorship of the investigation](/Censorship/overview)
* [Cover-up section hub](/CoverUp/overview)
* [Technology and surveillance](/technology_surveillance/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
