# FlightAware AeroAPI — restated data

Every file here restates one response from FlightAware's paid AeroAPI in our own layout.
**The facts are FlightAware's. The layout and wording are ours.** FlightAware's terms do
not allow republishing their responses, so the raw responses are held privately and are
not in this repo.

    <TAIL>/<START>_to_<END>_flights_page<N>.yaml   every flight FlightAware holds for the tail in that 7-day UTC window
    <TAIL>/tracking_block_status.yaml              whether the tail is on FlightAware's display block list
    <TAIL>/registered_owner.yaml                   the registered owner FlightAware lists (US tails only)

How to read a flight file:

* Flights are **oldest first**. Each has `takeoff` / `landing` (runway times) and, where
  recorded, `left_gate` / `reached_gate`, each with `scheduled`, `estimated` and `actual`
  times in UTC plus the airport's local time.
* `from` / `to` with a `position_only_point` instead of an airport code means FlightAware
  had a position there, not an airport.
* `flight_plan` altitudes are feet, speeds knots, distances statute miles.
* **An empty window is not proof the aircraft stayed on the ground.** Parked, not tracked,
  and blocked from display all look the same.
* **No file here places any person aboard any aircraft.** Flight data holds no passengers.

How we know nothing was lost or added: `../../code/check_restated.py` rebuilds the expected
content of every file from the raw response and compares it field by field. Every file is
written by `p_restate_flight_data.md` and must pass that check before it is committed.
