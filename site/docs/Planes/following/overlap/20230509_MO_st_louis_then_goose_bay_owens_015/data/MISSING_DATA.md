---
displayed_sidebar: docs
slug: /Planes/following/overlap/20230509_MO_st_louis_then_goose_bay_owens_015/data/MISSING_DATA
title: "ADS-B gaps for overlap 20230509_MO_st_louis_then_goose_bay_owens_015"
sidebar_label: "ADS-B gaps"
description: "Archive lookups that returned no primary ADS-B trace for the aircraft and dates claimed in overlap row 20230509_MO_st_louis_then_goose_bay_owens_015 (9 May 2023 — St. Louis then Goose Bay, MO)."
keywords:
  - "ADS-B"
  - "overlap"
  - "flight tracking"
  - "missing flight data"
  - "20230509_MO_st_louis_then_goose_bay_owens_015"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.110Z by
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
| SU-BND | 2023-05-08 | 404 | day before claimed arrival at Happy Valley-Goose Bay (CYYR); overlap OWENS-015 - St. Louis then Goose Bay MO (audited_accurate, audit: accurate) |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

One 404 sits behind [OWENS-015](/Planes/following/overlap/20230509_MO_st_louis_then_goose_bay_owens_015/overview), the row where the St Louis half of the claim was corroborated and the Labrador half was not — [SU-BND](/Planes/SU-BND/overview) came no closer than 3,057 km to Goose Bay, which is the sort of split the [overlap index](/Planes/following/overlap/overview) exists to record rather than round off, and which the [St. Louis record](/Planes/following/StLouis_KSTL_2022-12-20_to_2025-02-23/overview) and the [73-overlap reconstruction](/Planes/following/73_overlaps) both carry. Half-right rows are the reason this investigation keeps its threads apart: the [18-month following pattern](/Planes/Following-Charlie-Erika) is not the [September 10 day-of timeline](/Topic-Analyses/September_10_Event_Timeline), and neither is the [HADES surveillance jet over UVU](/Proof_Intel_Services/N1098L_HADES_Over_UVU) or the [FBI's reportedly halted foreign-lead review](/FBI/Foreign_Leads). Worth the click: [Goose Bay](/Planes/following/GooseBay_CYYR_2023-05-09_to_2025-09-13/overview) shows the two Egyptian Gulfstreams crossed the Atlantic through a Canadian Forces base and the three Falcons never did — the cleanest aircraft-type split in the whole record.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Goose Bay — the transatlantic split](/Planes/following/GooseBay_CYYR_2023-05-09_to_2025-09-13/overview)
* [Paris-Le Bourget, eighteen staging stops](/Planes/following/Paris_LFPB_2022-10-05_to_2025-10-05/overview)
* [The September 10 day-of timeline](/Topic-Analyses/September_10_Event_Timeline)

</div>
<div>

* [HADES spy plane over UVU](/Proof_Intel_Services/N1098L_HADES_Over_UVU)
* [Foreign leads reportedly blocked](/FBI/Foreign_Leads)
* [Government organizations in the case](/government_organizations/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
