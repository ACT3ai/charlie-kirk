---
displayed_sidebar: docs
slug: /Planes/following/overlap/20230420_DE_wilmington_owens_013/data/MISSING_DATA
title: "ADS-B gaps for overlap 20230420_DE_wilmington_owens_013"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20230420_DE_wilmington_owens_013 (20 April 2023 — Wilmington, DE)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20230420_DE_wilmington_owens_013"
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
| SU-BTT | 2023-04-19 | 404 | overlap OWENS-013 - Wilmington DE (audited_accurate, audit: accurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

The row above came back confirmed with [SU-BTT](/Planes/SU-BTT/overview) actually on the ground at Wilmington, 0.56 kilometres from the field, after a leg out of Kansas — so this log is the surrounding empty dates rather than the finding, and [the row page](/Planes/following/overlap/20230420_DE_wilmington_owens_013/overview) has the trace, with [the field's outbound-only record](/Planes/following/Wilmington_KILG_2022-11-17_to_2025-10-12/overview) and [the Wichita service centre](/Planes/following/Wichita_KICT_2022-11-13_to_2025-08-03/overview) explaining both ends of the leg. A ground fix is the strongest thing free ADS-B can give and it still does not open the cabin door: no FBO log, crew list or badge record has been produced for any leg by anyone, which is why the pages that matter most in the wider case are the ones with a document attached — [the DoD purchase order for miniaturized demolition charges](/Mic/DoD_Contract), [the ATF fragment report](/Gun_Bullet/ATF_Fragment_Inconclusive), [the sealed-warrant record](/Legal/Evidence-Sealing-2026). The equivalent on the aircraft side would be a ramp record, and [government flight records](/Planes/following/apis/government/knowledge) sets out which of those download freely today and which have to be prised out by FOIA or a state records request, with every row's status tracked on the [overlap index](/Planes/following/overlap/overview).

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [The exploding-mic theory hub](/Mic/overview)
* [Medical and autopsy questions](/Medical/overview)
* [Fix — the four proposed laws](/Fix/overview)

</div>
<div>

* [Capturing what the tracking sites show](/Planes/following/apis/browser_capture/knowledge)
* [Commercial APIs and what they cost](/Planes/following/apis/proprietary/knowledge)
* [Your actions — records you can request](/Your_Actions_Fix_It/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
