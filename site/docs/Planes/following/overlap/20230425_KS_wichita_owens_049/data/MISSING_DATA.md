---
displayed_sidebar: docs
slug: /Planes/following/overlap/20230425_KS_wichita_owens_049/data/MISSING_DATA
title: "ADS-B gaps for overlap 20230425_KS_wichita_owens_049"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20230425_KS_wichita_owens_049 (25 April 2023 — Wichita, KS)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20230425_KS_wichita_owens_049"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.118Z by
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
| SU-BTT | 2023-04-24 | 404 | overlap OWENS-049 - Wichita KS (audited_inaccurate, audit: inaccurate); overlap EXTRA-003 - Topeka KS (claimed, audit: untested) |
| SU-BTT | 2023-04-25 | 404 | overlap OWENS-049 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2023-04-26 | 404 | overlap OWENS-049 - Wichita KS (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

Three HTTP 404s for [SU-BTT](/Planes/SU-BTT/overview) across 24-26 April 2023 are the whole of this page, and they are published so the [Wichita row](/Planes/following/overlap/20230425_KS_wichita_owens_049/overview) is filed as untestable rather than counted beside the rows the [overlap index](/Planes/following/overlap/overview) actually resolved — the [free archives](/Planes/following/apis/public_open_source/knowledge) do not reach spring 2023, as the [Wichita location record](/Planes/following/Wichita_KICT_2022-11-13_to_2025-08-03/overview) and the [73-overlap reconstruction](/Planes/following/73_overlaps) both note. The distinction matters well past aviation: the same reasoning governs how this site treats [withheld foreign flight records](/CoverUp/Foreign_Flight_Records), [evidence sealed until 2026](/Legal/Evidence-Sealing-2026) and the [halted foreign-nexus review](/FBI/Foreign_Leads) — a missing document is a gap, never a finding. To see that principle cost this investigation a headline, read [what a 403 actually means](/Planes/Flight-Data-Recovery/What-A-403-Means): a published removal claim was retracted after five unrelated control aircraft returned the identical refusal, and [flight data recovery](/Planes/Flight-Data-Recovery/overview) sets out the control test that caught it.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [How the four free ADS-B archives were found](/Planes/Flight-Data-Recovery/overview)
* [The Wichita visits, 2022 to 2025](/Planes/following/Wichita_KICT_2022-11-13_to_2025-08-03/overview)
* [Foreign flight records reportedly withheld](/CoverUp/Foreign_Flight_Records)

</div>
<div>

* [Evidence sealed until March 2026](/Legal/Evidence-Sealing-2026)
* [The NCTC review that was shut down](/FBI/Foreign_Leads)
* [Government organizations in the case](/government_organizations/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
