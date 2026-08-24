---
displayed_sidebar: docs
slug: /Planes/following/overlap/20240318_KS_wichita_owens_022/data/MISSING_DATA
title: "ADS-B gaps for overlap 20240318_KS_wichita_owens_022"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20240318_KS_wichita_owens_022 (18 March 2024 — Wichita, KS)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20240318_KS_wichita_owens_022"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.120Z by
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
| SU-BTT | 2024-03-17 | 404 | overlap OWENS-022 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-03-18 | 404 | overlap OWENS-022 - Wichita KS (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-03-19 | 404 | overlap OWENS-022 - Wichita KS (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

March 2024 is inside archive coverage, so the empty results recorded here for [SU-BTT](/Planes/SU-BTT/overview) are a genuine negative rather than a boundary — [OWENS-022](/Planes/following/overlap/20240318_KS_wichita_owens_022/overview) stays untested in the [overlap index](/Planes/following/overlap/overview), the [free archives](/Planes/following/apis/public_open_source/knowledge) were serving, and the [Wichita record](/Planes/following/Wichita_KICT_2022-11-13_to_2025-08-03/overview) is where the surrounding visits are logged. Negative results get published here for the same reason the [inconclusive ATF report](/Proof_Not_Tyler/ATF_Inconclusive_Ballistics), the [contested Miranda timings](/court/mirandize/mirandize-overview) and the [material sealed until 2026](/Legal/Evidence-Sealing-2026) do: an investigation that only shows its wins is not one, and a reader has to be able to check the arithmetic. The most useful next page is [Overlap Recovery](/Planes/Flight-Data-Recovery/Overlap-Recovery), which reports the whole run at once — 69 testable pairs, both free archives, and how many had never been checked against primary data before.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Overlap recovery, all pairs tested](/Planes/Flight-Data-Recovery/Overlap-Recovery)
* [Wichita, the Falcon service centre](/Planes/following/Wichita_KICT_2022-11-13_to_2025-08-03/overview)
* [ATF ballistics, inconclusive](/Proof_Not_Tyler/ATF_Inconclusive_Ballistics)

</div>
<div>

* [Mirandizing — the court evidence](/court/mirandize/mirandize-overview)
* [Evidence sealing](/Legal/Evidence-Sealing-2026)
* [Proof it was not Tyler Robinson](/Proof_Not_Tyler/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
