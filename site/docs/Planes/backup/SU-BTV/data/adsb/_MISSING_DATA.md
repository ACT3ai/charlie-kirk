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
| SU-BTV | 2024-12-06 | 404 | day before claimed arrival at Le Bourget (LFPB) |
| SU-BTV | 2024-12-09 | 404 | day after claimed departure from Le Bourget (LFPB); day before claimed arrival at Wilmington (KILG) |
| SU-BTV | 2024-12-11 | 404 | day after claimed departure from Wichita (KICT) |
| SU-BTV | 2024-12-16 | 404 | day after claimed departure from Wilmington (KILG) |
| SU-BTV | 2025-02-01 | 404 | day before claimed arrival at Le Bourget (LFPB) |
| SU-BTV | 2025-02-04 | 404 | day after claimed departure from Le Bourget (LFPB) |
| SU-BTV | 2025-02-08 | 404 | day before claimed arrival at Wilmington (KILG) |
| SU-BTV | 2025-02-11 | 404 | day after claimed departure from Wilmington (KILG) |
| SU-BTV | 2025-03-15 | 404 | day before claimed arrival at Le Bourget (LFPB) |
| SU-BTV | 2025-03-18 | 404 | day after claimed departure from Le Bourget (LFPB) |
| SU-BTV | 2025-03-22 | 404 | day before claimed arrival at Wilmington (KILG) |
| SU-BTV | 2025-03-25 | 404 | day after claimed departure from Wilmington (KILG) |
| SU-BTV | 2025-03-28 | 404 | day before claimed arrival at Le Bourget (LFPB) |
| SU-BTV | 2025-03-31 | 404 | day after claimed departure from Le Bourget (LFPB) |
| SU-BTV | 2025-04-02 | 404 | day before claimed arrival at Wilmington (KILG) |
| SU-BTV | 2025-04-04 | 404 | day after claimed departure from Wichita (KICT) |
| SU-BTV | 2025-04-07 | 404 | day after claimed departure from Wilmington (KILG) |
| SU-BTV | 2025-05-25 | 404 | day before claimed arrival at Le Bourget (LFPB) |
| SU-BTV | 2025-05-28 | 404 | day after claimed departure from Le Bourget (LFPB) |
| SU-BTV | 2025-06-01 | 404 | day before claimed arrival at Wilmington (KILG) |
| SU-BTV | 2025-06-04 | 404 | day after claimed departure from Wilmington (KILG) |
| SU-BTV | 2025-07-28 | 404 | day before claimed arrival at Le Bourget (LFPB) |
| SU-BTV | 2025-07-31 | 404 | day after claimed departure from Le Bourget (LFPB) |
| SU-BTV | 2025-08-02 | 404 | day before claimed arrival at Wilmington (KILG) |
| SU-BTV | 2025-08-04 | 404 | day after claimed departure from Wichita (KICT) |
| SU-BTV | 2025-08-07 | 404 | day after claimed departure from Wilmington (KILG) |
| SU-BTV | 2025-10-03 | 404 | day before claimed arrival at Le Bourget (LFPB) |
| SU-BTV | 2025-10-06 | 404 | day after claimed departure from Le Bourget (LFPB) |
| SU-BTV | 2025-10-10 | 404 | day before claimed arrival at Wilmington (KILG) |
| SU-BTV | 2025-10-12 | 403 | day after claimed departure from Lincoln (KLNK); claimed departure from Wilmington (KILG) - flights.csv |
| SU-BTV | 2025-10-13 | 403 | day after claimed departure from Wilmington (KILG) |
