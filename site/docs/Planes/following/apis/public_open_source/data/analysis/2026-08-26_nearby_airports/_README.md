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
