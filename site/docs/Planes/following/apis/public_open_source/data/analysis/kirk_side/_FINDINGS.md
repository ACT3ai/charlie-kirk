# Kirk-side jets: full record, her plane, privacy dates, Adelson claim

Run 17 September 2026. Tasks from the 16 September 2026 call with Bryan Starbuck.
Free volunteer ADS-B only (globe.airplanes.live, adsb.lol, ADS-B Exchange monthly sample).
Every day from 2023-02-06 to 2026-09-16 was asked for every tail below; `coverage.csv`
has held / asked-empty per tail. A trace proves where an aircraft was, never who was aboard.

Code: `../../../code/sweep_tail_days.py`, `analyse_kirk_side_record.py`, `privacy_flag_timeline.py`.

## 1. When each plane went private (`privacy_flag_timeline.csv`)

Read from the `dbFlags` / `ownOp` header each archive writes into every day's trace. The
change sits between the last day seen without the flag and the first day seen with it.

| Tail | LADD flag appears | Other |
|---|---|---|
| N102DZ | ADS-B Exchange DB: between 2025-12-01 and 2026-04-01. airplanes.live DB: between 2026-05-18 and 2026-05-20 | Owner string GV 555 LLC -> REGISTRATION PENDING 13-15 Oct 2025 -> ELDERBERRY CHESTNUT LLC 22-30 Nov 2025. FlightAware block already visible 14 Jan 2026 (Wayback) - FlightAware's own block list, separate from LADD |
| N888KG | Already LADD between 2022-07-01 and 2022-12-01 | Private long before 10 Sep 2025 |
| N582MM | Never LADD in any archive | FlightAware still blocks it (own list) |
| T7-ELL | ADSBX: 2026-02-01..2026-05-01; airplanes.live: 2026-07-04..07-10 | |
| N79SC | airplanes.live: 2026-05-01..2026-06-01 | Owner D E Magarin Asset Mgmt -> First State Bank (Jan-Apr 2026) -> TVPX trustee (28-30 Apr 2026) -> Bank of Utah trustee (Jul-Aug 2026) |

Two archives refresh their copy of the FAA list on different schedules, so the flag
brackets the FAA change; it is not the FAA effective date. airplanes.live wrote empty
headers for EVERY tail 12 Sep - 3 Oct 2023: an archive outage, not a signal.

Blocked-period movements are in `stops.csv` (filter by tail and date).

## 2. His plane and her plane

* **N582MM (Learjet 60)** is on the ground at the event airport on ~50 dated Charlie Kirk
  stops, 2023 to Sep 2025 (`kirk_stop_class.csv`, EVENT_CHARLIE_*). It is the tour plane.
* **N79SC (Learjet 60)** is the aircraft at Erika Kirk's away events where Charlie was not:
  * BLOOM Women's Conference, San Clemente CA, 21-22 Mar 2025: N79SC Scottsdale -> Santa Ana
    afternoon 21 Mar, back to Scottsdale afternoon 22 Mar. Same days N582MM went
    Phoenix -> Van Nuys -> **Duluth MN**. Two jets, two halves of the country.
  * Medal of Freedom, Washington DC, 14 Oct 2025: N79SC at Dulles same day.
  * Hannity, New York, 8 Dec 2025: N79SC at Teterboro same day.
* **N102DZ** only joins Kirk events from Sep 2025 (fits Baron Coleman: a charter aircraft
  first used just before 10 Sep 2025). 10 Nov 2025 DC: N102DZ at Dulles.
* Erika's documented away appearances before Sep 2025 are very few (`erika_events.csv`,
  11 rows pre-shooting, none in 2022). The comparison is therefore a handful of dates.

## 3. Trips with no event, and the Adelson "meet-up" claim

Claim, from the source video (YouTube DNPjKLuDNC8, The Jimmy Dore Show guest-hosted by Garland
Nixon, Stew Peters, 1 Aug 2026; transcript in the private `all` repo under
`politics/charlie_kirk/flights/sources/`): since Charlie Kirk's death, "Turning Point" jets
Erika Kirk travels on land alone at 1-2 AM for 35-60 min at untowered fields in Arkansas and
the Florida panhandle, then at a larger airport sit 2-4 h beside Adelson Boeing business jets
"at a hangar ... Sands Air, which is in Las Vegas", after which the Adelson jet "goes straight
to Tel Aviv, and then it comes back ... the next day. This happens 27 times." **The video names
no date, airport or tail number.**

Adelson / Las Vegas Sands fleet (FAA registry 15 Sep 2026): N804MS (767), N108MS, N885LS,
N889LS (737s), N336LS-N339LS (G550s). All eight are BLOCKED on FlightAware (AeroAPI, 17 Sep 2026),
as is N79SC, so no paid route exists for them; this rests on free ADS-B only.

Result across 7 Kirk-side and 8 Adelson jets, 6 Feb 2023 - 16 Sep 2026:

* **Small fields.** No Kirk-side stop at any small Arkansas field. One Florida-panhandle stop:
  N40JD, Crestview KCEW, 3 May 2024, midday.
* **Same field, same time.** A Kirk-side and an Adelson jet within 3 h at one field: 70. Heard on
  the ground at the same moment: 16. Longest: 87 min (N102DZ and G550 N339LS, Las Vegas,
  23 Aug 2026, afternoon). Fields: Las Vegas 30, Van Nuys 21, Dallas Love 6, others 13. **None
  at night. One at a small field (Scottsdale, 2 h apart).** Las Vegas is the Sands base.
* **"Straight to Tel Aviv".** The Adelson jets arrived at Tel Aviv 134 times in the held record.
  For 27 the last field heard before was in the US. **In none of the 27 was a Kirk-side jet heard
  at that field in the 6 hours before** (`adelson_to_israel_departures.csv`). Of the 70
  co-locations, the Adelson jet's next foreign stop was Tel Aviv twice, both days later via
  LAX / Las Vegas.
* Night quick turns by Kirk-side jets away from home fields: 38, almost all at large airports.

The claimed pattern is not visible in free ADS-B. Limits: receivers miss ramps and remote
fields at night (heard ground time is a floor); 2022 is not covered; the claimants never
published the 27 dates, so they cannot be checked one by one.

## 4. Gaps that remain

* **2022 and night coverage** - FlightAware blocks every plane that matters, so it cannot fill
  them. Only FAA radar records or operator logs would.
* **Exact LADD dates** - FOIA draft to the FAA: `all/politics/charlie_kirk/flights/requests/faa_ladd_foia_draft.md` (not sent).
* **Erika's itinerary** - a second research pass (her Instagram @mrserikakirk, podcast notes,
  church and TPUSA event archives) found no new located appearance before Sep 2025
  (`_erika_events_notes_pass2.md`; first pass `_erika_events_notes.md`). N79SC as her plane therefore rests on 3-4 dates.
* **Blocked-period movements** - now listed per plane in `private_period_stops.csv`
  (N102DZ 345 stops, N888KG 215, N582MM 1,210, T7-ELL 61, N79SC 2).
