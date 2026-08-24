---
displayed_sidebar: docs
slug: /Planes/following/overlap/20230315_NE_omaha_owens_047/data/MISSING_DATA
title: "ADS-B gaps for overlap 20230315_NE_omaha_owens_047"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20230315_NE_omaha_owens_047 (15 March 2023 — Omaha, NE)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20230315_NE_omaha_owens_047"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.117Z by
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
| SU-BTT | 2023-03-14 | 404 | overlap OWENS-047 - Omaha NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-03-15 | 404 | overlap OWENS-047 - Omaha NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-03-16 | 404 | overlap OWENS-047 - Omaha NE (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

Omaha is the first row in this batch where the archives genuinely cover the date and still heard nothing from [SU-BTT](/Planes/SU-BTT/overview) — a different result from the 404s that dominate 2022 — and [the row page](/Planes/following/overlap/20230315_NE_omaha_owens_047/overview) states plainly that silence from a volunteer receiver network is not a refutation, which is how the [overlap index](/Planes/following/overlap/overview) files it. Getting that right is the whole reason this investigation runs a control test before publishing, a habit built after a claim on this site had to be withdrawn — see [what a 403 actually means](/Planes/Flight-Data-Recovery/What-A-403-Means) — and it is the standard the rest of the case would benefit from applying to [the missing bodycam footage](/court/mirandize/bodycam-grama-no-footage), the [videos reported deleted from witness phones](/CoverUp/Videos_Deleted_Remotely), and the [sealed evidence catalogue](/Legal/Evidence-Sealing-2026). Omaha itself has an unglamorous explanation waiting on [the Omaha airport page](/Planes/following/Omaha_KOMA_2024-02-09_to_2025-10-05/overview): six arrivals, every one followed within twenty minutes by a hop to [Lincoln](/Planes/following/Lincoln_KLNK_2024-02-09_to_2025-10-11/overview), where Duncan Aviation has held the Egyptian maintenance account since 1999.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Flight data recovery — the four free routes](/Planes/Flight-Data-Recovery/overview)
* [Cover-up claims, sorted](/CoverUp/overview)
* [Court and trial record](/court/overview)

</div>
<div>

* [What the compilers counted as an overlap](/Planes/following/Overlap_Window_Definition)
* [Suspicious conduct by actor](/Suspicious/overview)
* [Law enforcement outside the FBI](/Law_Enforcement/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
