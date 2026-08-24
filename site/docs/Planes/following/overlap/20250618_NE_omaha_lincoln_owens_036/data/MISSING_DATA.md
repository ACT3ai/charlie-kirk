---
displayed_sidebar: docs
slug: /Planes/following/overlap/20250618_NE_omaha_lincoln_owens_036/data/MISSING_DATA
title: "ADS-B gaps for overlap 20250618_NE_omaha_lincoln_owens_036"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20250618_NE_omaha_lincoln_owens_036 (18 June 2025 — Omaha / Lincoln, NE)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20250618_NE_omaha_lincoln_owens_036"
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
| SU-BTT | 2025-06-17 | 404 | overlap OWENS-036 - Omaha / Lincoln NE (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2025-06-19 | 404 | overlap OWENS-036 - Omaha / Lincoln NE (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

This gap list belongs to [OWENS-036](/Planes/following/overlap/20250618_NE_omaha_lincoln_owens_036/overview), one of the twelve rows the archives actually refuted — [SU-BTT](/Planes/SU-BTT/overview) was tracked on 18 June 2025 and it was not at [Omaha](/Planes/following/Omaha_KOMA_2024-02-09_to_2025-10-05/overview) — so the empty lookups here sit beside a positive answer rather than instead of one, and the [register](/Planes/following/overlap/overview) records both. Publishing misses next to hits is the standard this investigation asks of the government and rarely gets: [the foreign-nexus review reportedly ordered stopped](/Proof_Intel_Services/Joe_Kent_Foreign_Inquiry_Shutdown), [the warrants sealed into 2026](/Legal/Evidence-Sealing-2026) and [the ATF comparison that came back inconclusive](/Proof_Not_Tyler/ATF_Inconclusive_Ballistics) are all places where the negative result was the one that mattered. [Overlap recovery](/Planes/Flight-Data-Recovery/Overlap-Recovery) is the page to read next: it tested every checkable aircraft-and-date pair, and four of the twelve refutations exist only because a backup network held a trace the primary archive did not.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Per-aircraft recovery status](/Planes/Flight-Data-Recovery/Per-Aircraft-Status)
* [Joe Kent on the foreign-ties review](/US_Intelligence/joe-kent)
* [Patel reportedly closed the Kent probe](/Suspicious/FBI/patel-shut-down-kent-probe)

</div>
<div>

* [Which open flight sources hold history](/Planes/following/apis/public_open_source/knowledge)
* [A whistleblower-protection law](/Fix/Whistleblower)
* [The government bodies in this case](/government_organizations/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
