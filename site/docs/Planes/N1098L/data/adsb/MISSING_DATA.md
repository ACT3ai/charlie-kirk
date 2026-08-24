---
displayed_sidebar: docs
title: "ADS-B gaps for N1098L - claimed flights with no primary trace"
sidebar_label: "ADS-B gaps"
description: "Every claimed N1098L flight date that returned no primary ADS-B trace from the adsb.lol globe history archive, with the exact HTTP result and why we looked."
keywords:
  - "N1098L"
  - "ADS-B"
  - "flight tracking"
  - "missing flight data"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.107Z by
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
| N1098L | 2025-09-01 | 404 | September 2025 window sweep (n1098l side) - not a claimed date, a systematic look |
| N1098L | 2025-09-07 | 404 | September 2025 window sweep (n1098l side) - not a claimed date, a systematic look |
| N1098L | 2025-09-14 | 404 | September 2025 window sweep (n1098l side) - not a claimed date, a systematic look |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

Three September 2025 dates returned nothing for the Army-contracted Global 6500 — the 1st, the 7th and the 14th — and none of them is the 10th, the day the [N1098L record](/Planes/N1098L/overview) actually turns on and for which a primary trace exists; the surrounding fortnight was swept anyway so the [ISR program context](/Planes/ISR-Operations) and the [LASAI fleet](/Planes/LASAI-Fleet/overview) could be checked on the same terms as every other tail. A contract ISR jet operating out of [Biggs Army Airfield](/Planes/Airport-Biggs-Army-Airfield) is exactly the airframe a volunteer network misses on a quiet day, and a blank date proves nothing about the [low passes near UVU](/Proof_Intel_Services/N1098L_HADES_Over_UVU), the [air-launched drone claims](/Drones/N1098L_Air_Launched_Drones), or the [foreign-nexus inquiry reportedly shut down](/FBI/Foreign_Leads). The thing a trace can never do is name who was aboard or who tasked the flight — which is precisely the record [Law 2, the intelligence disclosure act](/laws/US_Intel/Law_2_US_Intel) would compel, naming this tail in statute, and which [per-aircraft recovery status](/Planes/Flight-Data-Recovery/Per-Aircraft-Status) still marks as missing.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [The Army HADES program and its fleet](/US_Intelligence/US_Army_HADES)
* [Sixteen drones reported over the campus](/Topics3/Drones/overview)
* [Joe Kent on the halted foreign inquiry](/US_Intelligence/joe-kent)

</div>
<div>

* [Biggs Army Airfield, the morning departure](/Planes/Airport-Biggs-Army-Airfield)
* [Law 2: intelligence services disclosure](/laws/US_Intel/Law_2_US_Intel)
* [How government evidence was handled](/gov/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
