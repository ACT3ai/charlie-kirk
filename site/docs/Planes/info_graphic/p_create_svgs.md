Create the Plane Overlap infographic SVGs.

This prompt walks the overlap records for the Charlie Kirk investigation and, for
each one, writes an info.yaml and renders the 16:9 Plane Overlap SVG from it.

The CODE and the TEMPLATE already exist. This prompt NEVER writes them, never
rewrites them, and never re-derives them. It reads them and it uses them. If the
generator is missing or broken, stop and say so — do not write a replacement.

====================================================================
VARIABLES
====================================================================

ROOT_DIR dir is ~/BGit/Bryan_git/charlie-kirk

SITE_DIR dir is {ROOT_DIR}/site
PLANES_DIR dir is {SITE_DIR}/docs/Planes
FOLLOWING_DIR dir is {PLANES_DIR}/following
WORK_DIR dir is {PLANES_DIR}/info_graphic
OUT_ROOT dir is {SITE_DIR}/internals/static/img/infographics/overlaps

GENERATOR is file {WORK_DIR}/code/build_overlap_svg.ts
TEMPLATE_SVG is file {WORK_DIR}/template.svg

OVERLAPS_CSV is file {FOLLOWING_DIR}/overlaps.csv
FLIGHTS_CSV is file {FOLLOWING_DIR}/flights.csv
AIRPORTS_CSV is file {FOLLOWING_DIR}/airports.csv
TPUSA_EVENTS_CSV is file {FOLLOWING_DIR}/tpusa_events.csv
PLANES_CSV is file {ROOT_DIR}/planes.csv
PROXIMITY_CSV is file {FOLLOWING_DIR}/apis/public_open_source/data/analysis/master_proximity.csv

RECOVERED_DIR dir is {PLANES_DIR}/{TAIL}/data/recovered
LEDGER_FILE is file {OUT_ROOT}/ledger.csv

ROOT_CHARTER is file {ROOT_DIR}/CLAUDE.md
PLANES_CHARTER is file {PLANES_DIR}/CLAUDE.md

MAX_AGENTS is ... = 12

====================================================================
WHAT ONE GRAPHIC IS
====================================================================

* Exactly ONE following / intelligence aircraft.
* Exactly ONE instance of overlap - one airport, one date window.
* Exactly ONE Kirk side - Charlie, or Erika, or both.
* Never two overlaps in one graphic. Never two following aircraft in one
  graphic. The triple is the identity of the graphic.

One directory per graphic, under {OUT_ROOT}. The directory name is:

  {YYYY}_{MM}_{DD}_{AIRPORT}_{Person}_{ST}_{city}

  * {YYYY}_{MM}_{DD} is the overlap date from {OVERLAPS_CSV}, zero padded.
  * {AIRPORT} is the ICAO code, uppercase, e.g. KPVU. Use UNKNOWN when the row
    has no airport code, and say so in the yaml.
  * {Person} is exactly one of Charlie, Erika, Both.
  * {ST} is the two letter state, uppercase.
  * {city} is the city, lowercase, spaces and punctuation to underscores.

  Example: 2025_09_10_KPVU_Charlie_UT_provo

Inside the directory:

  info.yaml                 everything the graphic is made of. Written by this
                            prompt.
  {directory name}.svg      the graphic. Written by {GENERATOR}, never by hand.

Why {OUT_ROOT} and not {WORK_DIR}: docusaurus.config.ts sets
staticDirectories to internals/static, so a file under {OUT_ROOT} is served at
/img/infographics/overlaps/{DIR}/{DIR}.svg. An SVG left under {SITE_DIR}/docs/
is not served at all - it renders locally and 404s for every real visitor.

====================================================================
STAGE 0 - READ BEFORE DOING ANYTHING
====================================================================

* Read {PLANES_CHARTER}, the whole "Plane Overlap Infographic Template" section
  of {ROOT_CHARTER}, and the "Recovering Deleted / Unavailable Flight Data"
  section of {ROOT_CHARTER}.
* Read {TEMPLATE_SVG}. Its header comment is the anatomy of the graphic.
* Read the header comment of {GENERATOR}. It states the three things the
  generator refuses to do. Do not try to work around any of them.
* Confirm both files exist. If either is missing:
    Output to stdout "==================================================="
    Output to stdout "STOP - the generator or the template is missing."
    Output to stdout "This prompt does not build them. Fix that first."
    Output to stdout "==================================================="
  and stop.

====================================================================
STAGE 1 - WORK OUT THE RUN SCOPE
====================================================================

The scope comes from TEXT_INPUT_TO_SKILL, the text the run was started with.

* DEFAULT, and this is what happens when nothing is said: ALL overlaps.
* One overlap: an overlap_id such as "OWENS-041" or "EXTRA-006".
* One aircraft: a tail such as "SU-BTT" - every overlap for that tail.
* One person: "all the Charlie ones", "Erika only", "both" - filter on the
  subject column.
* One airport or city: "just Provo", "KILG".
* A date range: "2025", "everything after Sept 2025".
* A rebuild: "rebuild the SVGs" - re-run {GENERATOR} over the existing
  info.yaml files and write nothing else.

Print the scope back before doing any work:

    Output to stdout "SCOPE: {what was selected} - {N} overlaps in this run"

====================================================================
STAGE 2 - BUILD THE WORK LIST
====================================================================

* Read {OVERLAPS_CSV}. One row is one candidate graphic.
* Columns that matter: overlap_id, date, airport_code, airport_name, city,
  state, subject, foreign_tail, kirk_tail, charlie_present, erika_present,
  audit_verdict, adsb_verified_verdict, overlap_page.
* Map the subject column to {Person}:
    subject Charlie -> Charlie
    subject Erika   -> Erika
    subject Both    -> Both
    subject TPUSA   -> SKIP unless charlie_present or erika_present says
                       otherwise. A TPUSA event with neither Kirk claimed is
                       not a Charlie-or-Erika overlap and this template does not
                       cover it. Record it as skipped with the reason.
* Rows with date UNKNOWN are SKIPPED. There is no date window to plot and there
  is no honest way to invent one. Record them.
* Rows with no foreign_tail, or foreign_tail UNKNOWN, are SKIPPED. There is no
  following aircraft to draw. Record them.
* Write the work list into {LEDGER_FILE} with columns:
    overlap_id,dir_name,person,following_tail,kirk_tail,airport_code,date,
    times_status,drawable,built_date,skip_reason
  Status uses bracket notation in the progress printout: [     ] not started,
  [IN-PR] in progress, [ DONE] built, [ SKIP] skipped with a reason.

====================================================================
STAGE 3 - RESOLVE THE TIMES - THE STAGE THAT DECIDES EVERYTHING
====================================================================

This is where the graphic is either honest or worthless. Read this stage twice.

The graphic is built from FOUR THINGS PER AIRCRAFT: every ground contact it had
in the window, each one with a start instant and an end instant. Everything else
on the picture is furniture.

* WHERE THE TIMES COME FROM, in this order:
  1. {PROXIMITY_CSV} - the best source. One row per tail per ground contact,
     with first_seen_utc, last_seen_utc, airport_code, ground_points, sources,
     archives_agreeing. Match on tail plus airport_code plus the date window.
  2. The recovered traces under {RECOVERED_DIR} when the proximity file has no
     row and a trace does exist. Say in the yaml which file the times came from.
  3. Nothing else. {OVERLAPS_CSV} carries DATES, NOT CLOCK TIMES. A date is not
     a time and must never be widened into one.

* NEVER INVENT, ESTIMATE, ROUND, OR INFER A TIME. Not "about midday", not "the
  event was at noon so call it 11am", not a plausible turnaround. A drawn bar is
  a claim about a duration. If a time is not in the data, the graphic does not
  get made. Set times_status to none or partial, write the skip reason into
  {LEDGER_FILE}, and move on. The generator will refuse it anyway - do not try
  to satisfy the generator by filling a gap.

* NEVER MERGE TWO GROUND CONTACTS ON ONE DAY. Each one is its own segment in the
  yaml. A gap between two contacts is a FLIGHT, not a wait. SU-BND at KPVU on
  2025-09-10 is exactly this case - two contacts, 16:05-17:34Z and 19:40-20:29Z.
  Merging them would erase a whole flight.

* NEVER WRITE "ARRIVED" OR "DEPARTED" FOR ADS-B DATA. What the archives hold is
  the first and last position a volunteer receiver HEARD. Set
  evidence_basis: adsb_ground_contact and the generator words every label as
  "first heard" and "last heard". Use published_flight_record ONLY when a real
  arrival or departure record exists, and name it in the sources list.

* THE KIRK-SIDE AIRCRAFT IS USUALLY THE HARD ONE. The kirk_tail column in
  {OVERLAPS_CSV} is empty on almost every row, because the claim behind those
  rows is about a person being in a city, not about a Kirk aircraft. So:
    - Use {PLANES_CSV} to find aircraft in the "Private / Kirk party" category.
      N102DZ is the main one.
    - Look for that tail in {PROXIMITY_CSV} at the same airport in the same
      window.
    - IF THERE IS NO KIRK-SIDE AIRCRAFT IN THE DATA, THERE IS NO SECOND BAR AND
      THERE IS NO GRAPHIC. Skip the row with skip_reason "no Kirk-side aircraft
      ground contact in the recovered data". Do NOT substitute the person's
      claimed presence for an aircraft. The lower bar is an AIRCRAFT, and a
      claimed itinerary is not one.

* TIME ZONES. Write every instant into the yaml as an ABSOLUTE UTC INSTANT
  ending in Z, exactly as the source recorded it, and let the generator convert.
  Never write a local clock time into the yaml. The generator resolves the
  airport zone from the airport.timezone key, so that key must be the correct
  IANA zone for that field - America/Denver, America/Chicago, America/New_York,
  America/Los_Angeles, Europe/Paris and so on. Get it from {AIRPORTS_CSV} or the
  OurAirports data the flight pipeline already downloaded. Do not guess it from
  the state, and never assume the machine's own zone - the machine this was
  built on runs on Hawaii time.

* POPULATION. town_population is a real sourced figure - US Census place
  population - with town_population_source naming it. If there is no sourced
  figure, write unknown and the generator omits the line. Never guess it.

* Write info.yaml. The shape, and every key the generator reads:

    overlap_id: EXTRA-006
    date: 2025-09-10
    person: charlie                    # charlie | erika | both
    dir_name: 2025_09_10_KPVU_Charlie_UT_provo
    evidence_basis: adsb_ground_contact   # or published_flight_record
    airport:
      code: KPVU
      name: Provo Municipal Airport
      city: Provo
      state: UT
      state_name: Utah
      timezone: America/Denver
      town_population: 115162
      town_population_source: US Census 2020
    following_plane:
      tail: SU-BND
      type: Gulfstream G550
      operator: Egyptian / foreign VIP
      segments:
        - from: {utc: 2025-09-10T16:05:35Z, source_zone: UTC}
          to:   {utc: 2025-09-10T17:34:09Z, source_zone: UTC}
          ground_points: 100
          sources: adsb-lol|airplanes-live
        - from: {utc: 2025-09-10T19:40:53Z, source_zone: UTC}
          to:   {utc: 2025-09-10T20:29:38Z, source_zone: UTC}
          ground_points: 156
          sources: adsb-lol|airplanes-live
    kirk_plane:
      tail: N102DZ
      type: Gulfstream V
      operator: Private / Kirk party
      segments:
        - from: {utc: 2025-09-10T21:30:43Z, source_zone: UTC}
          to:   {utc: 2025-09-10T22:10:12Z, source_zone: UTC}
          ground_points: 133
          sources: adsb-lol|airplanes-live
    times_status: complete             # complete | partial | none
    as_of: {today}
    source_line: "Source: ..."
    sources:
      - {every file each number came from, path from the repo root}
    notes: >-
      What this overlap is, and anything a reader of the yaml needs in order to
      not misread it.

* Every number in that file is traceable to a file in this repo. The sources
  list is not optional and it is not a formality - it is the reason a reader can
  check us.

====================================================================
STAGE 4 - RENDER
====================================================================

* Run the generator over each finished directory:

    node {GENERATOR} {OUT_ROOT}/{DIR}

* Or over everything at once:

    node {GENERATOR} --all {OUT_ROOT}

* Dry run, writes nothing, reports what is drawable:

    node {GENERATOR} --all {OUT_ROOT} --check

* Exit 0 means every requested graphic was written. Exit 2 means at least one
  input was not drawable, and the message says which key failed. Exit 3 is bad
  usage.

* READ EVERY WARN LINE. They are findings, not noise:
    - "NEVER HEARD ON THE GROUND AT THE SAME MOMENT" means the two aircraft were
      at the same field on the same day but not at the same time. That is a real
      and publishable result and it usually WEAKENS the following claim. It goes
      on the page at the same size as anything that supports the claim.
    - "N separate ground contacts" means the aircraft flew during the window.
    - "too short to draw to scale" means a contact was widened to a visible
      minimum, so its width is no longer proportional. Say so if the page leans
      on that contact.
    - "pushed apart to stay legible" is cosmetic only.

* If the generator refuses a directory, DO NOT EDIT THE YAML TO GET PAST IT.
  It refuses missing times, unzoned times, and empty segment lists on purpose.
  Record the refusal in {LEDGER_FILE} and move on.

====================================================================
STAGE 5 - INSPECT WHAT WAS ACTUALLY DRAWN
====================================================================

Do not declare a graphic finished without looking at it.

* Rasterise and look at it:

    rsvg-convert -w 1600 {OUT_ROOT}/{DIR}/{DIR}.svg -o /tmp/check.png

* Check, on the picture and not in the yaml:
    - The title reads across the top and names the right person.
    - The frame-left name block is 2 rows for one name, 3 for both, and does not
      run wider than 15% of the frame.
    - The frame-right block reads airport, state, city, year, top to bottom, and
      does not run wider than 50% of the frame.
    - The YEAR appears ONLY in that right-hand block. No date around the bars
      carries a year.
    - Nothing collides with anything. Long airport names, long tail-and-type
      labels, and early or late inner labels are the three that break first.
    - The bar proportions match the yaml. Take the window, take one contact, and
      check the percentage by eye against the axis.
    - The centre of the frame is clear.

====================================================================
STAGE 6 - RUNNING IT WIDE
====================================================================

* Up to {MAX_AGENTS} agents may run in parallel. It is not required and a small
  scope should not use them.
* Partition by overlap, never by stage. One agent owns a set of overlap_ids end
  to end - resolve, write yaml, render, inspect - so no two agents touch one
  directory.
* Each agent appends its own rows to {LEDGER_FILE}. Merge at the end; do not
  have twelve agents rewriting one file at once.
* Every agent gets Stage 0 and Stage 3 in full. The rules in Stage 3 are the
  whole point of the run and an agent that has not read them will produce a
  confident, wrong graphic.

====================================================================
STAGE 7 - REPORT
====================================================================

    Output to stdout "==================================================="
    Output to stdout "PLANE OVERLAP SVGS"
    Output to stdout "  built     {N}"
    Output to stdout "  skipped   {N}   (no times {N}, no Kirk aircraft {N},"
    Output to stdout "                   no date {N}, no following tail {N})"
    Output to stdout "  warnings  {N}   (never simultaneous {N}, multi-contact {N})"
    Output to stdout "==================================================="

* Then list, in plain sentences, every overlap where the data CONTRADICTS or
  WEAKENS the following claim. That list is the most valuable output of the run
  and it goes first, not last.
* Name every skipped overlap and why. A skip is a coverage fact and it is worth
  publishing; it is not a failure to hide.

====================================================================
WHAT THIS PROMPT DOES NOT DO
====================================================================

* It does not build {GENERATOR}. The code already exists.
* It does not build or edit {TEMPLATE_SVG}. The template already exists.
* It does not hand-edit any .svg under {OUT_ROOT}. The next run overwrites it.
* It does not embed anything on any page. Putting a graphic on a page is a
  separate, deliberate act - it changes what the public sees. List the target
  pages in the report and let the human choose. The natural targets are the
  overlap's own page under {FOLLOWING_DIR}/overlap/ and the aircraft's page at
  {PLANES_DIR}/{TAIL}/overview.mdx.
* It does not assert intent. We can show two aircraft were on the ground at one
  field. We cannot see why, and a trace never places a person aboard.
