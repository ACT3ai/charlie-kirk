---
displayed_sidebar: docs
slug: /Planes/following/overlap/20240725_NE_omaha_lincoln_owens_060/data/MISSING_DATA
title: "ADS-B gaps for overlap 20240725_NE_omaha_lincoln_owens_060"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20240725_NE_omaha_lincoln_owens_060 (25 July 2024 — Omaha / Lincoln, NE)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20240725_NE_omaha_lincoln_owens_060"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.122Z by
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
| SU-BTT | 2024-07-24 | 404 | overlap OWENS-060 - Omaha / Lincoln NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-07-25 | 404 | overlap OWENS-060 - Omaha / Lincoln NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2024-07-26 | 404 | overlap OWENS-060 - Omaha / Lincoln NE (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

This gap file backs [row OWENS-060](/Planes/following/overlap/20240725_NE_omaha_lincoln_owens_060/overview), a claimed Paris to Omaha to Lincoln to Wilmington to Cairo rotation the auditor placed in Egypt outright, and the 404s recorded here neither confirm nor contradict that, because all they say is that [a volunteer network heard nothing](/Planes/Flight-Data-Recovery/What-A-403-Means) on days already recorded as inaccurate in [the overlap directory](/Planes/following/overlap/overview). The honest position is that the free archives cannot settle mid-2024 at all for these tails, which is why [the paid history](/Planes/following/apis/proprietary/knowledge), [the government records route](/Planes/following/apis/government/knowledge) and ultimately [a forced-disclosure statute](/laws/US_Intel/Law_2_US_Intel) are the only ways this ends, the same conclusion the case reaches on [sealed evidence](/Legal/Evidence-Sealing-2026). Read [Per-Aircraft Recovery Status](/Planes/Flight-Data-Recovery/Per-Aircraft-Status) next, one section per tail saying exactly how far back each source reaches, the document that stops an ordinary retention boundary being written up as suppression, a mistake [this site made once and corrected in public](/Planes/Flight-Data-Recovery/overview) and the standard [every recovery page here](/Planes/Flight-Data-Recovery/Overlap-Recovery) is held to.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Row OWENS-060, the claimed rotation](/Planes/following/overlap/20240725_NE_omaha_lincoln_owens_060/overview)
* [Commercial flight-data APIs and their cost](/Planes/following/apis/proprietary/knowledge)
* [Evidence sealed into 2026](/Legal/Evidence-Sealing-2026)

</div>
<div>

* [How government handled the evidence](/gov/overview)
* [The four proposed disclosure laws](/Fix/overview)
* [Foreign influence transparency](/Fix/Foreign_Influence)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
