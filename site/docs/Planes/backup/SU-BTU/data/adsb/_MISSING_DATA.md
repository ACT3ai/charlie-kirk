# Claimed flights we could NOT retrieve a primary ADS-B trace for

Generated 2026-08-24T16:03:53.125Z by
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
| SU-BTU | 2024-11-24 | 404 | day before claimed arrival at Le Bourget (LFPB) |
| SU-BTU | 2024-11-27 | 404 | day after claimed departure from Le Bourget (LFPB) |
| SU-BTU | 2024-11-30 | 404 | day before claimed arrival at Wilmington (KILG) |
| SU-BTU | 2024-12-02 | 404 | day after claimed departure from Lincoln (KLNK) |
| SU-BTU | 2024-12-04 | 404 | day after claimed departure from Wilmington (KILG) |
| SU-BTU | 2025-01-15 | 404 | day before claimed arrival at Le Bourget (LFPB) |
| SU-BTU | 2025-01-18 | 404 | day after claimed departure from Le Bourget (LFPB) |
| SU-BTU | 2025-01-22 | 404 | day before claimed arrival at Wilmington (KILG) |
| SU-BTU | 2025-01-25 | 404 | day after claimed departure from Wilmington (KILG) |
| SU-BTU | 2025-02-14 | 404 | day before claimed arrival at Le Bourget (LFPB) |
| SU-BTU | 2025-02-17 | 404 | day after claimed departure from Le Bourget (LFPB) |
| SU-BTU | 2025-02-21 | 404 | day before claimed arrival at Wilmington (KILG) |
| SU-BTU | 2025-02-24 | 404 | day after claimed departure from Wilmington (KILG) |
| SU-BTU | 2025-04-06 | 404 | day before claimed arrival at Le Bourget (LFPB) |
| SU-BTU | 2025-04-09 | 404 | day after claimed departure from Le Bourget (LFPB) |
| SU-BTU | 2025-04-13 | 404 | day before claimed arrival at Wilmington (KILG) |
| SU-BTU | 2025-04-16 | 404 | day after claimed departure from Wilmington (KILG) |
| SU-BTU | 2025-04-22 | 404 | day before claimed arrival at Le Bourget (LFPB) |
| SU-BTU | 2025-04-25 | 404 | day after claimed departure from Le Bourget (LFPB) |
| SU-BTU | 2025-04-29 | 404 | day before claimed arrival at Wilmington (KILG) |
| SU-BTU | 2025-05-02 | 404 | day after claimed departure from Wilmington (KILG) |
