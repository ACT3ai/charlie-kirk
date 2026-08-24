---
displayed_sidebar: docs
title: "ADS-B gaps for N560TW - claimed flights with no primary trace"
sidebar_label: "ADS-B gaps"
description: "Every claimed N560TW flight date that returned no primary ADS-B trace from the adsb.lol globe history archive, with the exact HTTP result and why we looked."
keywords:
  - "N560TW"
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
| N560TW | 2025-09-03 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |
| N560TW | 2025-09-04 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |
| N560TW | 2025-09-06 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |
| N560TW | 2025-09-08 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |
| N560TW | 2025-09-09 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |
| N560TW | 2025-09-11 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |
| N560TW | 2025-09-14 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |
| N560TW | 2025-09-15 | 404 | September 2025 window sweep (kirk side) - not a claimed date, a systematic look |

{/* CK_PAGE_FOOTER_START */}

## Where this page fits

Eight September 2025 dates returned nothing for this Citation XLS and none of them is the 10th — the morning Scottsdale to Provo to Santa Barbara out-and-back that put the tail on [Candace Owens](/People/candace-owens)' program is set out on the [N560TW page](/Planes/N560TW/overview) with primary data behind it, so the rows above audit the surrounding fortnight rather than the claim itself. A twin-jet on a short regional hop is routinely missed by volunteer receivers at low altitude, and treating a blank day as a hidden flight would put this page exactly where the [larger overlap tallies](/Planes/following/73_overlaps) ended up once [critics showed the criteria were loose](/Other/Evidence-Contradictions) — a mistake the [day-of timeline](/Topic-Analyses/September_10_Event_Timeline) and the [political context around the donors](/political_context/overview) can survive and a reputation cannot. What this tail already produced is an archive find rather than a gap: the [recovery hub](/Planes/Flight-Data-Recovery/overview) records an Internet Archive snapshot preserving a 2016 precedent for the same Scottsdale-Provo routing, the kind of thing no live tracker will show you now, and [per-aircraft status](/Planes/Flight-Data-Recovery/Per-Aircraft-Status) says how far back each source actually reaches.

## Related Areas

<div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
marginTop:'0.5rem'}}>
<div>

* [Candace Owens and the aircraft claims](/People/candace-owens)
* [Turning Point USA in the investigation](/TPUSA/overview)
* [Donor pressure on the AmFest lineup](/Amfest/donor-pressure-bookings)

</div>
<div>

* [What Turning Point actually owned](/Planes/TPUSA-Aircraft/overview)
* [Political context before September 10](/political_context/overview)
* [The recovery effort, source by source](/Planes/Flight-Data-Recovery/overview)

</div>
</div>

{/* CK_PAGE_FOOTER_END */}
