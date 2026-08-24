---
displayed_sidebar: docs
slug: /Planes/following/overlap/20221020_IL_chicago_owens_002/data/MISSING_DATA
title: "ADS-B gaps for overlap 20221020_IL_chicago_owens_002"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20221020_IL_chicago_owens_002 (20 October 2022 — Chicago, IL)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20221020_IL_chicago_owens_002"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.115Z by
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
| SU-BTT | 2022-10-19 | 404 | overlap OWENS-002 - Chicago IL (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2022-10-20 | 404 | overlap OWENS-002 - Chicago IL (audited_inaccurate, audit: inaccurate) |
| SU-BTT | 2022-10-21 | 404 | overlap OWENS-002 - Chicago IL (audited_inaccurate, audit: inaccurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

Three lookups for [SU-BTT](/Planes/SU-BTT/overview), three 404s, and a control basket of unrelated airframes that failed identically — that is the whole content of this page, and it is why [row OWENS-002](/Planes/following/overlap/20221020_IL_chicago_owens_002/overview) sits on the [overlap index](/Planes/following/overlap/overview) as untested rather than refuted. Writing an absence down is not busywork: the same discipline separates a retention boundary from a deletion in [flight data recovery](/Planes/Flight-Data-Recovery/overview), and it is precisely what the investigation lacks on [witness phone video reported deleted remotely](/CoverUp/Videos_Deleted_Remotely), the [4K footage a witness says the FBI asked him to erase](/Censorship/Ryne_Simmons_FBI_Video), and the sealed material tracked under [legal investigation](/legal_investigation/overview). The page worth clicking from here is [the Candace Owens broadcasts](/Planes/following/Candace_Owens_Broadcasts), where the count moved from 68 to 73 on air without a single underlying row in [the 73 overlaps](/Planes/following/73_overlaps) reconstruction changing.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Getting the data — the four verification passes](/Planes/following/apis/overview)
* [Witness footage pressure at UVU](/Censorship/Witness_Footage_Pressure)
* [Social media analysis of the case](/social_media_analysis/overview)

</div>
<div>

* [St. Louis — the closest documented Kirk pairing](/Planes/following/StLouis_KSTL_2022-12-20_to_2025-02-23/overview)
* [Media coverage and how it drifted](/Media/overview)
* [Organizations and groups in the case](/organizations_groups/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
