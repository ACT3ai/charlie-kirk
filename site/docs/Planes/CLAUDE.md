================================================================================
== Planes — Area Charter ==
================================================================================

ROOT_DIR dir is ~/BGit/Bryan_git/charlie-kirk
SITE_DIR dir is {ROOT_DIR}/site
PLANES_DIR dir is {SITE_DIR}/docs/Planes

This is the Level 2 section for every aircraft in the Charlie Kirk assassination
investigation: the jets claimed to have followed Charlie and Erika Kirk, the SAM
military flights, the Egyptian and foreign tails, the airports and ground
contacts recovered out of ADS-B archives, and the flight records that have been
erased.

The ROOT charter at {ROOT_DIR}/CLAUDE.md governs everything here and is NOT
repeated in this file. Read it as well. In particular read, before doing any
work in this directory:

  * "Recovering Deleted / Unavailable Flight Data" — the control test, the four
    free archive routes, the three traps, and the retraction that produced them.
  * "Generated Plane Pages (added 2026-08-28)" — most of what a reader sees
    under /Planes/ is GENERATED. Run rebuild_plane_pages.sh, not the individual
    scripts.
  * "Images Are Tracked In Git" and "Never Embed An Image By IPFS Gateway URL".
  * "Page Levels — Level 2 / 3 / 4 / 5".

This file is excluded from the site — `**/CLAUDE.md` is in the Docusaurus docs
`exclude` list — so it is a charter, not a page.


================================================================================
== Infographics For The Planes Section ==
================================================================================

There are TWO directories, and they do different jobs. Do not put the contents
of one in the other.

  {PLANES_DIR}/info_graphic/
      TEMPLATES ONLY. The pattern library. Nothing here is a finished
      infographic and nothing here is published.

  {SITE_DIR}/internals/static/img/infographics/{TAIL}_{Type}/
      REAL INFOGRAPHICS. One directory per (aircraft, infographic type) pair,
      holding the prompt we built up AND the output image, at a location
      Docusaurus serves over a public URL.

MOVED 2026-08-28. The infographic working directory used to be
{ROOT_DIR}/info_graphics/{Topic}/, which is OUTSIDE the site tree and therefore
could not serve its own image — the picture had to be copied to a second place
before a page could show it. `Overlap_Timeline` was moved whole from
{ROOT_DIR}/info_graphics/Overlap_Timeline/ to
{SITE_DIR}/internals/static/img/infographics/Overlap_Timeline/, and
{ROOT_DIR}/info_graphics/ no longer exists. Anything still naming the old path
is stale. The root CLAUDE.md "Infographics (info_graphics/)" section describes
the goals.mdx and prompt CONTRACT, which is unchanged and still authoritative —
only the location moved.


=== Why the static directory ===

`docusaurus.config.ts` sets `staticDirectories: ["internals/static"]`. Every
file under {SITE_DIR}/internals/static/ is copied VERBATIM into the build and
served from the site root. So:

  file    {SITE_DIR}/internals/static/img/infographics/N1098L_Flight_Record/N1098L_Flight_Record.jpg
  URL     /img/infographics/N1098L_Flight_Record/N1098L_Flight_Record.jpg

That is the only place in this repo where dropping an image file in a directory
makes it fetchable at a stable URL with no import, no build step and no copy.
An image left under {SITE_DIR}/docs/ is NOT served that way — a literal
`<img src="...">` in MDX is not processed by webpack, so it 404s for every real
visitor while looking fine in a local editor. Put the image in static.

Everything else in the infographic directory travels with it — the goals, the
prompt, any generator script. Those files also become fetchable, which is
intended: this is a public investigation and how a graphic was planned and
generated is part of the record. Never put anything in one of these directories
that is not safe to publish.


=== Directory naming ===

    {TAIL}_{Type}

The aircraft tail (or the topic, when the graphic is not about one airframe)
plus the infographic type. Underscores between words, no spaces, no special
characters. It behaves like a page key. One or two words for the type.

    N1098L_Flight_Record
    N102DZ_Erased_Record
    SU_BTT_Ground_Contacts
    Overlap_Timeline            (topic, not a single tail)

Most of the time there is one infographic type per plane, and a plane may have
several types over time. One directory each — never two graphics in one
directory.


=== What is in a real infographic directory ===

    {SITE_DIR}/internals/static/img/infographics/{TAIL}_{Type}/
      goals.mdx                     The plan. Written FIRST, in full.
      nana_banana_pro_prompt.txt    The generation prompt, written FROM goals.mdx.
      {TAIL}_{Type}.jpg             The output image.
      generate_*.py                 Optional — present when the graphic is
                                    PLOTTED from a CSV rather than model-drawn.

Templates for the first two are in {PLANES_DIR}/info_graphic/. Copy them, do not
write from memory.


=== Generating ===

Always 16:9. Always 2K. Every infographic on this site uses that shape so they
sit together consistently on the pages, and 2K is the readable-but-not-enormous
tier for a wide graphic embedded in a Docusaurus page.

  node ~/BGit/all/tools/Nano_Banana_4K/nb_4k.js \
    {SITE_DIR}/internals/static/img/infographics/{TAIL}_{Type}/nana_banana_pro_prompt.txt \
    {SITE_DIR}/internals/static/img/infographics/{TAIL}_{Type}/{TAIL}_{Type}.jpg \
    --size 2K --aspect 16:9

The tool defaults to 4K, so `--size 2K` must be passed explicitly. Uppercase K
is required by the API. The model defaults to nano-banana-pro
(gemini-3-pro-image), which is the one that honours 2K/4K.


=== Embedding on a page ===

  <img src="/img/infographics/{TAIL}_{Type}/{TAIL}_{Type}.jpg"
       alt="{a full, literal description of what the graphic shows}"
       style={{width:'100%', height:'auto', display:'block', borderRadius:'4px'}}
       loading="lazy" />

Absolute path from the site root, always. Never an IPFS gateway URL — see the
root charter. The alt text on this site is long and literal on purpose: it is
what a reader with images off, a screen reader, or a search engine gets, and on
an evidence site that is not a place to be brief.

The image file is committed to git like every other image. An untracked image
renders perfectly on this machine and 404s for every visitor, because the live
site is built by GitHub Pages from the REPO.


=== PLOTTED vs MODEL-GENERATED — read this before publishing one ===

This distinction has already cost this site a graphic, and it is the most
important rule in this section.

  PLOTTED           Rendered by a script straight out of a CSV in this repo.
                    Every mark is real and it moves when the data moves.
                    Re-running the script is the whole update procedure.

  MODEL-GENERATED   Rendered by NanoBanana / GPT Imagine from the prompt.

A GENERATIVE MODEL DRAWS A PLAUSIBLE CHART. IT DOES NOT PLOT A REAL ONE.

The 26 August 2026 Overlap_Timeline render is the worked example. It set the
type and the composition beautifully and it rendered every quoted string
correctly — and it invented its own monthly distribution: amber bars in months
that have none, and a lower trace drawn mostly solid where the real one is
mostly dotted. Every string was right and every bar was wrong.

So:

  * A graphic a reader would read VALUES off must be PLOTTED. The JPG in
    Overlap_Timeline/ is a DESIGN REFERENCE ONLY. Do not swap it onto a page and
    do not read a number off it. The published artefact is the SVG at
    /img/infographics/Overlap_Timeline.svg, generated by
    Overlap_Timeline/generate_overlap_timeline.py out of
    {PLANES_DIR}/following/overlaps.csv.
  * A conceptual, diagrammatic or illustrative graphic — no readable values —
    may be model-generated.
  * goals.mdx must state which of the two it is. The template has the section.

On a site whose entire argument is that the record was not checked carefully
enough, publishing a hand-waved chart would be the single worst available own
goal.


=== Evidence rules that apply to a picture exactly as they apply to prose ===

Every rule in the root charter's recovery section applies to an infographic. A
graphic is read faster and trusted harder than a paragraph, so the rules bite
harder here, not softer.

  * EVERY NUMBER IS TRACEABLE to a file in this repo — overlaps.csv,
    flights.csv, tpusa_events.csv, airports.csv, aircraft_costs.csv, or a
    recovered trace under {PLANES_DIR}/{TAIL}/data/recovered/. goals.mdx names
    the file each number came from.
  * SAY WHICH OF THE THREE IT IS — a real removal, an archive retention
    boundary, or a coverage gap. Never draw a 403 in a way a reader will take as
    a deletion.
  * AN ABSENCE IS NOT A FINDING. A gap means a volunteer network heard nothing.
    Parked and silent, outside receiver coverage, or a wrong claimed date come
    first, every time. Draw absence as absence — dotted, hollow, greyed — never
    as a zero and never as a refutation.
  * A TRACE PROVES PRESENCE, NEVER PURPOSE, AND NEVER OCCUPANCY. No infographic
    places any person aboard any aircraft.
  * PUBLISH THE RESULT THAT WEAKENS THE CLAIM as prominently as the one that
    supports it. If the data cuts against the headline, the picture shows it at
    the same size.
  * NEVER ASSERT INTENT. We can show a page was public and is not any more. We
    cannot see why.
  * SCOPE THE CLAIM TO WHAT WAS CHECKED. If only one archive was queried, the
    source line says that archive.

Every infographic carries a source line in its on-image text saying what the
data is and as of when.


=== After making one ===

  1. Embed it on its target pages — the primary page from goals.mdx first, then
     any secondary pages.
  2. `git add` the image. Verify it is really tracked and really not ignored:
         git ls-files --error-unmatch <path>     # must succeed
         git check-ignore -v <path>              # must produce no output
  3. Refresh `line_count` in {ROOT_DIR}/pages.csv for every page edited, and add
     a row for any new page.
  4. `cd site && npm run build` before declaring done. Keep every <div> and
     </div> at column 0 — only the build catches an indented closing tag.


================================================================================
== Map Of This Directory ==
================================================================================

  overview.mdx                    The Level 2 page and its table of contents.
                                  Every child page should be linked from it.
  info_graphic/                   Infographic TEMPLATES (this charter, above).
  {TAIL}/                         One directory per aircraft — overview.mdx plus
                                  data/recovered/ holding the RAW archive pulls.
                                  The SOURCE IS PART OF THE FILENAME on purpose.
  Airports/                       Generated. One page per airport a case
                                  aircraft was on the ground at or flew a
                                  recovered leg through. 290 pages.
  Incidents/                      Generated. One page per (tail, UTC date,
                                  field) ground contact within 50 miles of a
                                  sourced event. 110 pages, 147 contacts.
  following/                      The public page-per-location follow log, the
                                  CSV spine (flights, overlaps, airports,
                                  tpusa_events), and the four API source lanes.
                                  Has its OWN CLAUDE.md — read it.
  Flight-Data-Recovery/           The hub page for the erased-records effort.
  CONTROL-RYANAIR/                The control aircraft. They exist so a
  CONTROL-LUFTHANSA/              retention boundary is never published as
                                  suppression. Never delete them.
  Aircraft-Costs/                 Who could afford to fly this.
  LASAI-Fleet/  TPUSA-Aircraft/   Cross-cutting fleet pages.
  SAM-*/  99-0004-Vance/          Military and government flights.

Generated pages write ONLY between their own markers and every generator is
idempotent. To rebuild them:

  sh {PLANES_DIR}/following/apis/public_open_source/code/rebuild_plane_pages.sh

Order matters in that script — the airport and incident pages must exist before
any table links to them, because links are gated on page existence. Run the
script, not the individual builders.


================================================================================
== The "Plane Overlap" Infographic Template ==
================================================================================

Added 2026-08-29. The FIRST NAMED TEMPLATE in the pattern library, and the only
one with a real generator behind it. Every instance has the same composition,
the same bar mechanics and the same text furniture; only the aircraft, the
place, the person and the times change.

WHAT ONE INSTANCE IS. Exactly one following/intelligence aircraft, at exactly
one instance of overlap, against exactly one Kirk side — Charlie, or Erika, or
both. Never two overlaps in one graphic and never two following aircraft in one
graphic. That triple IS the identity of the graphic and the directory name
carries it, so the identity is visible without opening anything.


=== The four files, and which one does what ===

  {PLANES_DIR}/info_graphic/p_create_svgs.md
        THE PROMPT. Walks the overlap records, resolves the ground-contact times
        out of the flight data, writes one info.yaml per overlap and renders it.
        Runs for ALL overlaps by default; can be scoped to one overlap_id, one
        tail, one person, one airport, or a date range. May fan out to 12
        agents, partitioned by overlap, never by stage.
        IT DOES NOT BUILD THE CODE OR THE TEMPLATE. Both already exist. If
        either is missing the prompt stops rather than writing a replacement.

  {PLANES_DIR}/info_graphic/template.svg
        THE PATTERN, two-bar case. A real rendering, annotated. Its header
        comment is the anatomy of the graphic, top to bottom. Every STRING in it
        is illustrative; every POSITION in it is authoritative and mirrors the
        LAYOUT block in the generator. Change one, change the other.

  {PLANES_DIR}/info_graphic/template_no_kirk_aircraft.svg
        THE PATTERN, NO KIRK-SIDE AIRCRAFT. Added 2026-08-29 and it exists
        because of a measured result, not a design preference: across the twelve
        field-years where Erika Kirk is claimed at one field twice in one year,
        56 claimed overlaps produce exactly ONE date with both a following
        aircraft and a Kirk-party aircraft on the ground - 10 September 2025 at
        Provo - and that date is a Charlie / Both row. NO ERIKA-CLAIMED OVERLAP
        HAS A KIRK-SIDE AIRCRAFT AT ALL. Drawing nothing would have hidden that.
        This template shows both declared variants: the HOLLOW DASHED Kirk band
        (absence drawn as absence, with the tails actually queried named inside
        it) and a HATCHED near-field pass (heard within 15 km of the field while
        AIRBORNE - a measured window, and never a landing).

  {PLANES_DIR}/info_graphic/code/build_info_yaml.py
        Writes the info.yaml files by MEASURING the windows out of the recovered
        traces, so a digit cannot be transposed between the archive and the
        picture, and writes ledger.csv covering every candidate row - drawn or
        skipped, with the skip reasons kept distinct.
            python3 build_info_yaml.py [--check]

  {PLANES_DIR}/info_graphic/code/build_overlap_svg.ts
        THE GENERATOR. Reads info.yaml, writes the SVG. Node 22+ runs the .ts
        directly; code/package.json marks the directory ESM and js-yaml
        resolves from site/node_modules.
            node build_overlap_svg.ts <dir>                  one graphic
            node build_overlap_svg.ts --all <root>           everything
            node build_overlap_svg.ts --all <root> --check   report only
        Exit 0 = written, 2 = something was not drawable, 3 = bad usage.

  {SITE_DIR}/internals/static/img/infographics/overlaps/{DIR}/
        THE OUTPUT, one directory per graphic, holding info.yaml and {DIR}.svg,
        plus ledger.csv one level up recording every overlap and its status.

{DIR} is the overlap, spelled out:

    {YYYY}_{MM}_{DD}_{AIRPORT}_{Person}_{ST}_{city}

    2025_09_10_KPVU_Charlie_UT_provo
    2025_09_08_KILG_Both_DE_wilmington

{Person} is exactly Charlie, Erika or Both. {AIRPORT} is the ICAO code. The
directory behaves like a page key — underscores, no spaces, no special
characters. Served at /img/infographics/overlaps/{DIR}/{DIR}.svg. An SVG left
under {SITE_DIR}/docs/ is NOT served and 404s for every real visitor, which is
why the output does not live beside the generator.

Aspect 16:9, viewBox 1920x1080. Fixed.


=== It is a HYBRID: model-generated scene, PLOTTED bars ===

Read the PLOTTED vs MODEL-GENERATED rule above before touching one. This
template deliberately straddles it:

  * THE BACKGROUND SCENE is MODEL-GENERATED — NanoBanana Pro draws the town, the
    airport and the sky. No readable values, so a plausible drawing is honest.
    NOT BUILT YET. Until it exists the ground is a flat medium green, chosen so
    the white-with-black-pen-edge type will still read once a photograph sits
    behind it. The generator emits a commented-out <image> slot at the top of
    every SVG; drop {DIR}_bg.jpg in the directory and uncomment it.
  * THE BARS, TIMES, DATES AND LABELS ARE VALUES A READER READS OFF THE PICTURE.
    They are PLOTTED by the generator from info.yaml. A generative model draws a
    plausible bar, not a real one — the 26 Aug 2026 Overlap_Timeline render got
    every string right and every bar wrong, and this is where that would repeat.

A NanoBanana-only version may be made as a DESIGN REFERENCE while a composition
is being worked out. It is never the published artefact and no number is ever
read off it.


=== The anatomy ===

  TITLE, centred across the whole frame: "Following plane overlaps with
  {Charlie Kirk | Erika Kirk | Charlie and Erika Kirk}".

  BIG NAME BLOCK, frame LEFT, under the title. NEVER WIDER THAN 15% OF THE
  FRAME. Wraps onto rows — 2 rows for one name, 3 rows for both. The generator
  shrinks the type until it fits, so a long name cannot break the layout.

  PLACE BLOCK, frame RIGHT, high up, under the title. NEVER WIDER THAN 50% OF
  THE FRAME. Four right-aligned rows, in this order: airport name, state, city,
  YEAR — the year set largest. THE YEAR APPEARS ONLY HERE. That is precisely why
  no date anywhere around the bars carries a year, and the generator's date
  formatter has no year in it at all.

  THE TOWN, left of centre, between the frame centre and the top: a label rising
  out of the town centre on a leader line, giving the town and its population.
  The population line is OMITTED when we have no sourced figure — never guessed.

  THE CENTRE OF THE FRAME IS DELIBERATELY EMPTY. That is where the scene goes.

  CAPTION AND SOURCE, two left-aligned lines above the axis. The caption is not
  decoration: a trace proves presence, never occupancy.

  THE SHARED TIME AXIS, drawn twice. Left edge = the earlier of the two
  aircraft's first ground contact. Right edge = the later of the two last
  contacts. Date over time, centred on each edge, leader line straight down.
  BOTH BACKGROUND RECTANGLES SHARE THE SAME LEFT AND RIGHT EDGES — one axis,
  drawn twice, which is what makes the two bars comparable at a glance. Light
  grey at 50% transparency with a thick black pen edge.

  UPPER BAR = the FOLLOWING / intelligence aircraft, dark red #9B1B1E.
  LOWER BAR = the CHARLIE / ERIKA / BOTH aircraft, bright yellow #FFE21F.
  A label sits just above each rectangle naming the aircraft and its type.

  THE BOTTOM 5% BAND belongs to the INNER TIME LABELS and nothing else. They
  mark the two events that are NOT the axis ends — the later first-contact and
  the earlier last-contact — on a tick line dropped from the bar. Time alone
  inside one day; date and time when the window is longer. Never a year.


=== The three things the generator REFUSES to do ===

Each one is a rule from the root charter expressed as code, and each one is a
place a prettier graphic would quietly lie. Do not work around them, and do not
edit an info.yaml to get past a refusal.

  1. IT WILL NOT DRAW A BAR FROM A MISSING OR "unknown" TIME. A drawn bar is a
     claim about a duration. overlaps.csv holds DATES, NOT CLOCK TIMES, so most
     rows will not be drawable until their times are recovered — and that is the
     correct outcome, recorded in ledger.csv, not a problem to route around.
  2. IT WILL NOT MERGE TWO GROUND CONTACTS IN A DAY. Every contact is its own
     filled block on the axis. A gap between two blocks is a FLIGHT, not a wait.
     SU-BND at KPVU on 2025-09-10 is exactly that case — two contacts, 16:05 to
     17:34Z and 19:40 to 20:29Z — and merging them would erase a whole flight.
  3. IT WILL NOT SAY "arrived" OR "departed" FOR ADS-B DATA. What the archives
     hold is the first and last position a volunteer receiver HEARD. With
     evidence_basis: adsb_ground_contact every label reads "first heard" and
     "last heard". Use published_flight_record only when a real arrival or
     departure record exists, and name it in the sources list.

It also WARNS, and the warnings are findings rather than noise. "THE TWO
AIRCRAFT WERE NEVER HEARD ON THE GROUND AT THE SAME MOMENT" means same field,
same day, different hours — a real, publishable result that usually WEAKENS the
following claim, and it goes on the page at the same size as anything that
supports it.


=== Times and time zones ===

  * info.yaml stores every instant as an ABSOLUTE UTC INSTANT ENDING IN Z,
    exactly as the source recorded it. Never a local clock time.
  * The generator converts to the AIRPORT'S OWN LOCAL TIME for display, from the
    airport.timezone IANA key. Every date and time on the graphic is local.
  * The YAML is loaded with js-yaml CORE_SCHEMA on purpose. The DEFAULT schema
    parses an ISO timestamp into a JS Date, which throws the written zone away
    and would let an unzoned local clock time through as though it were an
    instant. An instant with no Z and no offset is REFUSED.
  * Never trust the machine's own zone. The machine this was built on runs on
    Hawaii time, which is how that bug was found in the first place.


=== The Kirk-side aircraft is the hard one ===

The kirk_tail column in overlaps.csv is EMPTY on nearly every row, because the
claim behind those rows is about a PERSON being in a CITY, not about a Kirk
aircraft. The lower bar is an AIRCRAFT. A claimed itinerary is not one, and must
never be substituted for one. If no Kirk-side aircraft has a ground contact in
the data, there is no second bar and THERE IS NO GRAPHIC — skip the row and
record why. planes.csv category "Private / Kirk party" is where to look;
N102DZ is the main one.


=== Where the numbers come from ===

  * following/apis/public_open_source/data/analysis/master_proximity.csv — the
    best source. One row per tail per ground contact, with first_seen_utc,
    last_seen_utc, airport_code, ground_points, sources, archives_agreeing.
  * {PLANES_DIR}/{TAIL}/data/recovered/ — the traces themselves.
  * following/overlaps.csv, flights.csv, airports.csv, tpusa_events.csv, and
    the root planes.csv for tails, types and categories.

info.yaml carries a sources list naming the file every number came from. It is
not a formality — it is the reason a reader can check us.


=== Build order ===

  1. Run {PLANES_DIR}/info_graphic/p_create_svgs.md, scoped or for everything.
  2. LOOK AT WHAT WAS DRAWN. rsvg-convert -w 1600 <svg> -o /tmp/check.png and
     open it. Long airport names, long tail-and-type labels, and early or late
     inner labels are the three things that break first.
  3. Read every WARN line and decide what each one means for the page.
  4. Commit the SVG and its info.yaml like any other tracked file.
  5. EMBEDDING IS A SEPARATE, DELIBERATE ACT — it changes what the public sees.
     The prompt lists target pages and does not touch them. The natural targets
     are the overlap's own page under following/overlap/ and the aircraft's
     {PLANES_DIR}/{TAIL}/overview.mdx. When a page is edited, refresh its
     line_count in pages.csv and run `cd site && npm run build`.
