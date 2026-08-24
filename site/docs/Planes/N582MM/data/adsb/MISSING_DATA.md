---
displayed_sidebar: docs
title: "ADS-B gaps for N582MM - claimed flights with no primary trace"
sidebar_label: "ADS-B gaps"
description: "Every claimed N582MM flight date that returned no primary ADS-B trace from the adsb.lol globe history archive, with the exact HTTP result and why we looked."
keywords:
  - "N582MM"
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
| N582MM | 2025-09-04 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

One date, 4 September 2025, is the whole of what a volunteer archive did not hold for this tail — a single blank day, listed because the [N582MM page](/Planes/N582MM/overview) rests on thin sourcing and a one-row gap table is still a row somebody can check, unlike much of what sits around it in the [Planes section](/Planes/overview) or in the [TPUSA aircraft question](/Planes/TPUSA-Aircraft/overview). The movement that put this tail into the [proposed disclosure laws](/Fix/overview) is an October 2025 leg reported from [Fort Huachuca](/US_Intelligence/Fort_Huachuca/overview) to Kalispell, more than a month after the date above, and nothing in a September blank speaks to it in either direction — nor to the [US intelligence threads](/US_Intelligence/overview) the reported stop is usually read against. The Fort Huachuca thread is the one worth the click — [the Army counterintelligence school page](/US_Intelligence/Fort_Huachuca/overview) records roughly twelve lieutenant colonels reportedly meeting there about thirty-six hours before the killing, with the Air Force VIP jet [SAM 99-0404](/Planes/SAM-99-0404/overview) tracked in and out on September 8 and 9.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Fort Huachuca, thirty-six hours before](/US_Intelligence/Fort_Huachuca/overview)
* [SAM 99-0404 into Fort Huachuca](/Planes/SAM-99-0404/overview)
* [Turning Point USA in the investigation](/TPUSA/overview)

</div>
<div>

* [The four proposed disclosure laws](/Fix/overview)
* [Law 1: DoJ and FBI forced disclosure](/laws/DoJ_FBI/Law_1_DoJ_FBI)
* [US intelligence threads in the case](/US_Intelligence/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
