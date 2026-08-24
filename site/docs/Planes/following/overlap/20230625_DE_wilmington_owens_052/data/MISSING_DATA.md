---
displayed_sidebar: docs
slug: /Planes/following/overlap/20230625_DE_wilmington_owens_052/data/MISSING_DATA
title: "ADS-B gaps for overlap 20230625_DE_wilmington_owens_052"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20230625_DE_wilmington_owens_052 (25 June 2023 — Wilmington, DE)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20230625_DE_wilmington_owens_052"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.111Z by
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
| SU-BND | 2023-06-24 | 404 | overlap OWENS-052 - Wilmington DE (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2023-06-25 | 404 | overlap OWENS-052 - Wilmington DE (audited_inaccurate, audit: inaccurate) |
| SU-BND | 2023-06-26 | 404 | overlap OWENS-052 - Wilmington DE (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

These lookups sit under [OWENS-052](/Planes/following/overlap/20230625_DE_wilmington_owens_052/overview), where 25 June 2023 has no archive coverage at all and the refutation therefore rests on the day before — [SU-BND](/Planes/SU-BND/overview) at Cairo West and Helwan, held by the [backup network](/Planes/Flight-Data-Recovery/overview) only, nowhere near Delaware, as the [overlap index](/Planes/following/overlap/overview) records. The row says plainly that it does not rest on the gap, and that plainness is the point: this investigation has already had to retract a [removal claim](/Planes/Flight-Data-Recovery/What-A-403-Means) built on a refusal, a lesson that applies equally to [foreign flight records withheld](/CoverUp/Foreign_Flight_Records) and [filings sealed until 2026](/Legal/Evidence-Sealing-2026). Wilmington is the hook: it is [the most-visited airport in the entire fleet record](/Planes/following/Wilmington_KILG_2022-11-17_to_2025-10-12/overview), appearing on the outbound leg only, twenty-one times in three years, never once inbound.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Wilmington — outbound only, 21 times](/Planes/following/Wilmington_KILG_2022-11-17_to_2025-10-12/overview)
* [Cairo, the home field](/Planes/following/Cairo_HECA_2022-11-13_to_2025-10-12/overview)
* [Foreign flight records withheld](/CoverUp/Foreign_Flight_Records)

</div>
<div>

* [Evidence sealing, 2026](/Legal/Evidence-Sealing-2026)
* [Legal investigation hub](/legal_investigation/overview)
* [Cross-cutting topics with no other home](/other_topics/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
