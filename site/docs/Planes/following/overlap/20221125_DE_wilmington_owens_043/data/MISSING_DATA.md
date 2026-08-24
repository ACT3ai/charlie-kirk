---
displayed_sidebar: docs
slug: /Planes/following/overlap/20221125_DE_wilmington_owens_043/data/MISSING_DATA
title: "ADS-B gaps for overlap 20221125_DE_wilmington_owens_043"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20221125_DE_wilmington_owens_043 (25 November 2022 — Wilmington, DE)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20221125_DE_wilmington_owens_043"
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
| SU-BTT | 2022-11-24 | 404 | overlap OWENS-043 - Wilmington DE (claimed, audit: archive_gap) |
| SU-BTT | 2022-11-25 | 404 | overlap OWENS-043 - Wilmington DE (claimed, audit: archive_gap) |
| SU-BTT | 2022-11-26 | 404 | overlap OWENS-043 - Wilmington DE (claimed, audit: archive_gap) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

This is the unusual case where both checks came back the same way: the paid audit recorded [row OWENS-043](/Planes/following/overlap/20221125_DE_wilmington_owens_043/overview) as not assessable, and the free archives above returned nothing for [SU-BTT](/Planes/SU-BTT/overview) either, so it sits on the [overlap index](/Planes/following/overlap/overview) with no verdict in either direction and none of the standing that [the window definition](/Planes/following/Overlap_Window_Definition) requires. Two independent sources of silence are still only silence — the governing rule here, and one that applies just as hard to the parts of the case where nothing was recovered, from the [bodycam the county said did not exist](/court/mirandize/bodycam-grama-no-footage) to the [witness phone videos reported deleted remotely](/CoverUp/Videos_Deleted_Remotely) to the sealed material catalogued under [legal investigation](/legal_investigation/overview). For the opposite outcome — an archive that did give something back — [flight data recovery](/Planes/Flight-Data-Recovery/overview) documents the four free routes and the one genuine removal they proved, while [what a 403 actually means](/Planes/Flight-Data-Recovery/What-A-403-Means) documents the finding this site had to retract.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Court and trial proceedings](/court/overview)
* [The Miranda-timing conflict](/court/mirandize/mirandize-overview)
* [Detroit as a 2025 entry point](/Planes/following/Detroit_KDTW_2025-02-03_to_2025-03-30/overview)

</div>
<div>

* [Censorship of the investigation](/Censorship/overview)
* [What AI assistants say about the overlaps](/Planes/following/AI_Assistant_Answers)
* [Suspicious conduct, sorted by actor](/Suspicious/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
