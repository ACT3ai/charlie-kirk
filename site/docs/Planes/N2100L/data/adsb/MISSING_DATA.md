---
displayed_sidebar: docs
title: "ADS-B gaps for N2100L - claimed flights with no primary trace"
sidebar_label: "ADS-B gaps"
description: "Every claimed N2100L flight date that returned no primary ADS-B trace from the adsb.lol globe history archive, with the exact HTTP result and why we looked."
keywords:
  - "N2100L"
  - "ADS-B"
  - "flight tracking"
  - "missing flight data"
image: "/img/docusaurus-social-card.jpg"
hide_table_of_contents: true
---

# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.108Z by
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
| N2100L | 2025-09-01 | 404 | September 2025 window sweep (n1098l side) - not a claimed date, a systematic look |
| N2100L | 2025-09-02 | 404 | September 2025 window sweep (n1098l side) - not a claimed date, a systematic look |
| N2100L | 2025-09-03 | 404 | September 2025 window sweep (n1098l side) - not a claimed date, a systematic look |
| N2100L | 2025-09-06 | 404 | September 2025 window sweep (n1098l side) - not a claimed date, a systematic look |
| N2100L | 2025-09-07 | 404 | September 2025 window sweep (n1098l side) - not a claimed date, a systematic look |
| N2100L | 2025-09-08 | 404 | September 2025 window sweep (n1098l side) - not a claimed date, a systematic look |
| N2100L | 2025-09-09 | 404 | September 2025 window sweep (n1098l side) - not a claimed date, a systematic look |
| N2100L | 2025-09-14 | 404 | September 2025 window sweep (n1098l side) - not a claimed date, a systematic look |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

Eight September 2025 dates came back empty for the LASAI sister ship, and the shape of that list is the point — this airframe was swept because it shares an operator and a type with [N1098L](/Planes/N1098L/overview), not because anyone claimed a flight on those days, and the [N2100L page](/Planes/N2100L/overview) states plainly that no public track places it over Orem at all. For an aircraft with no documented UVU pass, an empty archive day is the least interesting fact available; what would actually matter is operator tasking, and that sits behind the same wall as the [Army HADES program record](/US_Intelligence/US_Army_HADES), the [foreign leads reportedly blocked](/FBI/Foreign_Leads), the [evidence sealed into 2026](/Legal/Evidence-Sealing-2026) and the wider [intelligence-services case](/Proof_Intel_Services/overview). Take the sister-ship question to [the LASAI fleet page](/Planes/LASAI-Fleet/overview), where the FAA registry shows fifteen aircraft across two LASAI entities — three Global 6500s, two Challenger 650s and six King Airs — which is the difference between a one-off charter and a standing contract fleet, and the reason [Law 2](/laws/US_Intel/Law_2_US_Intel) asks for records by operator rather than only by date.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [The LASAI fleet, fifteen aircraft deep](/Planes/LASAI-Fleet/overview)
* [The US Army HADES program](/US_Intelligence/US_Army_HADES)
* [Government organizations in the case](/government_organizations/overview)

</div>
<div>

* [Non-US intelligence threads](/intelligence/overview)
* [Technology and surveillance claims](/technology_surveillance/overview)
* [The intelligence-service involvement case](/Proof_Intel_Services/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
