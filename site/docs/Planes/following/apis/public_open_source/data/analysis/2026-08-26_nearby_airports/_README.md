# Nearby-Airport Overlap Investigation — 26 Aug 2026

Not a published page. The leading underscore keeps Docusaurus from building it.

## The question this run asked

Every earlier analysis started from an EVENT and asked "was a tracked aircraft within 40
miles in the following-window". That shape cannot find an aircraft that landed at an
adjacent field, or three days out. This run INVERTED it: start from every foreign-fleet
ground contact we hold in North America and scan outward to all 139 events.

## The answer

ZERO new plane-to-event pairings. Widening 40 -> 75 -> 100 -> 150 miles across windows of
+/-2, 3, 5 and 7 days added no foreign-fleet ground contacts at any combination. The whole
foreign-fleet ground signal across 3.5 years is two Utah clusters that are already published.

THAT IS NOT PROOF OF ABSENCE. We hold about 9% of the foreign-fleet aircraft-days the 139
event windows need (2022: 0.5%). A null result in a 9%-populated dataset establishes only
that nothing is there IN WHAT WE HOLD.

## Files

* inversion_matrix.csv      one row per (tail, UTC day, airport) ground presence, scored
                            against all 134 geocoded events; distance, signed day-gap, bucket
* inversion_pairs_wide.csv  the surviving visit-to-event pairs
* blind_spot_pairs.csv      pairs that appear at a wider radius but not at 40 miles
* radius_window_matrix.csv  pair counts at every radius x window, both fleets, vs a
                            date-shifted placebo that measures lift over chance
* temporal_series.csv       year-by-year distance-to-nearest-event, coverage-normalised
* erika_class_comparison.csv  events split by attendee class with coverage-normalised rates
* gap_ledger.csv            HELD / ASKED_AND_EMPTY / NEVER_ASKED per tail per year
* gap_ledger_by_event.csv   the same per event
* claims_audit.csv          every overlaps.csv row re-tested against recovered primary ADS-B
* _*.md                     the written analysis behind each CSV
* code/                     the scripts that produced all of the above

## Reading rules that govern every file here

* A trace proves PRESENCE, never PURPOSE, and never OCCUPANCY.
* An absence is not a finding. ASKED_AND_EMPTY and NEVER_ASKED are different facts.
* Nothing here is a REMOVAL unless a control airframe failed identically on the same dates
  and the same endpoint.
* Dates sourced from `adsbexchange-samples` are the 1st of a month only and can never test a
  claim about a specific mid-month date.

Bryan's written answer for this run:
~/BGit/all/politics/charlie_kirk/bryan/spy_planes_near_charlie.txt

## Update, same day — the +/-7 day pull

Every CSV in this directory was computed BEFORE the wider archive pull finished. The pull then
completed: 4,999 requests, 333 new traces, 4,539 asked-and-empty, 127 transport errors (network
failures, NOT misses — those days stay NEVER_ASKED and are retryable). The trace index was
rebuilt to 2,235 aircraft-days and all 139 event yaml files were regenerated.

IT DID NOT CHANGE THE ANSWER. Events with an Egyptian SU- tail inside the radius: still 1 of 139.
Scoring the 42 new foreign-fleet ground-visit days against all 139 events at 150 mi / +/-7 days
yielded one candidate — SU-BTU at KILG on 2025-01-24, 92.5 mi and +4 days from the 2025-01-19
Washington event — which is the documented customs-and-fuel stop, i.e. KNOWN_TRANSIT, not an
overlap. It is NOT proposed as a new row.

What did shift: four new Egyptian-tail Provo days with no Kirk/TPUSA event near them in time or
space (SU-BND 2024-07-17, SU-BTU 2025-04-14, SU-BGM 2025-04-16), across THREE tails. The Provo
visits are therefore not time-locked to Charlie Kirk's calendar. That says the visits are not
explained by his schedule; it does not say what does explain them.

So the CSVs here are the +/-2 baseline. Re-run code/ against the rebuilt index to refresh them.
