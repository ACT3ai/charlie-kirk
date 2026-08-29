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
