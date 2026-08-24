---
displayed_sidebar: docs
slug: /Planes/following/overlap/20230327_DE_wilmington_owens_048/data/MISSING_DATA
title: "ADS-B gaps for overlap 20230327_DE_wilmington_owens_048"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20230327_DE_wilmington_owens_048 (27 March 2023 — Wilmington, DE)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20230327_DE_wilmington_owens_048"
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
| SU-BTT | 2023-03-26 | 404 | overlap OWENS-048 - Wilmington DE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-03-27 | 404 | overlap OWENS-048 - Wilmington DE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-03-28 | 404 | overlap OWENS-048 - Wilmington DE (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

Fourth Wilmington row, same result: [OWENS-048](/Planes/following/overlap/20230327_DE_wilmington_owens_048/overview) was marked inaccurate on paid data and the free archives above cannot reach March 2023 to say otherwise, leaving [SU-BTT](/Planes/SU-BTT/overview) untested on the [overlap index](/Planes/following/overlap/overview) at a field [whose whole record is outbound legs](/Planes/following/Wilmington_KILG_2022-11-17_to_2025-10-12/overview). Delaware appears on the way out, every time, never inbound — a scoring artefact rather than a pattern, and this investigation has had to catch several of those: a [published removal claim the control test destroyed](/Planes/Flight-Data-Recovery/What-A-403-Means), the [contested minute of impact](/Other/Evidence-Contradictions), the [totals that drifted between 68 and 77 as the story travelled](/Media/overview). The correction that best shows the method working is on [flight data recovery](/Planes/Flight-Data-Recovery/overview) — an entry reading "arrived 1:13pm, departed 1:13pm" turned out to be a flight-duration column misread as a clock time, with real ground time about eighteen minutes.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Press coverage of the plane claim](/Planes/following/Press_Coverage)
* [Independent investigators and influencers](/Influencers/overview)
* [Defamation litigation from the case](/Defamation/overview)

</div>
<div>

* [AI assistants asked about the overlaps](/Planes/following/AI_Assistant_Answers)
* [Topics index for the whole investigation](/Topics)
* [Other topics with no single home](/other_topics/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
