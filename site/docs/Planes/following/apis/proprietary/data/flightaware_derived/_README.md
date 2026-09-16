# FlightAware AeroAPI — derived tables

These three files are **ours**: counts, dates and airports we computed from FlightAware's
answers. The answers themselves are held privately and are not republished, because
FlightAware's terms do not allow it. The fact-by-fact restatement of each response lives
in `../flightaware_restated/`; this directory is the summary layer above it.

    us_flights.csv             one row per flight by an Egyptian-registered aircraft that
                               touched the United States, 2022-2025
    flights_by_tail_year.csv   per aircraft per year: flights anywhere, US legs, US days
    us_airports_by_year.csv    per US airport: visits in each year and in total

## What produced them

`../../code/build_fleet_us_tables.py`, reading every window bought by
`../../code/aeroapi_fleet_sweep.js` and every flown path bought by
`../../code/aeroapi_fleet_tracks.js`. Airport names come from the open OurAirports
gazetteer already held in this repository, not from the vendor.

## How to read them

* **A visit is one end of one flight.** An aircraft that lands at Wilmington and later
  leaves it counts twice in `us_airports_by_year.csv` — once arriving, once leaving. The
  column is traffic at that field, not separate trips.
* **`us_end`** says which end of the flight was in the United States: `arrival`,
  `departure`, or `both` for a flight inside the country.
* **The path columns describe the flown track we hold for that flight** — how many
  positions FlightAware recorded, the highest altitude, and the first and last position
  times. **The positions themselves are not here.** They are the vendor's data; what is
  published is this summary of them.
* **`from_icao` / `to_icao` can be empty.** FlightAware sometimes has a position instead
  of an airport at one end of a leg. Those rows are kept and left blank rather than
  guessed at, and they are counted separately in the totals.
* **These are FlightAware's records, which are built from filed flight plans and air
  traffic data.** They are not a volunteer receiver network, and the two do not always
  agree. Where they disagree, both are published.
* **No row places any person aboard any aircraft.** A flight record shows where an
  aircraft went. It shows nothing about who was on it or why it went.

## The reason this exists

Every earlier pull asked a per-claim question: was this tail at this field on this claimed
date? That can confirm or refute somebody else's list, and nothing more. It cannot say how
often these aircraft were in the United States at all — the denominator every "N overlaps"
figure is measured against. These tables are that denominator, bought a week at a time
across four calendar years rather than at the dates somebody had already pointed to.
