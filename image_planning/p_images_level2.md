ROOT_DIR dir is ~/BGit/Bryan_git/charlie-kirk

THIS_DIR dir is {ROOT_DIR}/image_planning
HIERARCHY_FILE is file {THIS_DIR}/hierarchy_images.yaml
LAYOUT_GUIDELINES is file {THIS_DIR}/layout_guidelines.txt
CHARTER_FILE is file {THIS_DIR}/CLAUDE.md
EXCLUDE_FILE is file {THIS_DIR}/exclude_images.txt
FINDINGS_FILE is file {THIS_DIR}/findings_for_hierarchy.md

SITE_DIR dir is {ROOT_DIR}/site
DOCS_DIR dir is {SITE_DIR}/docs
PHOTOS_DIR dir is {DOCS_DIR}/Photos
IMAGES_L2_PAGE is file {PHOTOS_DIR}/overview.mdx
STATIC_IMG_DIR dir is {SITE_DIR}/static/img/evidence
PAGES_CSV is file {ROOT_DIR}/pages.csv
CK_FILE is file {ROOT_DIR}/Charlie_Kirk.txt
ASSESS_MANUAL is file {ROOT_DIR}/prompts/Assess_Manual.md

MIRROR_DIR dir is ~/_Mirror/Politics/Charlie_Kirk_Mi
MIRROR_SIDECAR_DIR dir is ~/BGit/Bryan_git/personal_large_files_bridge/_Mirror/Politics/Charlie_Kirk_Mi
REPO_SIDECAR_DIR dir is {ROOT_DIR}/.lfbridge

MAX_AGENTS is ... = 12

============================
GOAL
============================

Generate and keep regenerating the published image pages of the site's images
Level 2 (today the Photos section, rooted at {IMAGES_L2_PAGE}) from
{HIERARCHY_FILE}. By the time this prompt runs, the YAML is already built and
holds all the data needed: the cluster tree (level_3 / level_4 / level_5), and
for every image its sha256, file_path, inline ai_description, sidecar file
paths (ai_description_file, ocr_file, transcription_file), on_site_pages,
also_filed_in, and site_level_2 / site_page bindings. This prompt READS the
YAML and WRITES pages. It does not grow or edit the YAML (except recording
published-page bookkeeping fields explicitly listed below).

Two kinds of pages get produced under {PHOTOS_DIR}:

  * Cluster pages — one .mdx page per YAML node (level_3, level_4, level_5).
    Mostly navigation: a titled page with a table of contents linking to the
    node's peers, its child clusters, and its image pages.
  * Image pages — one .mdx page per image entry. Each hosts exactly one image
    at the layout spec below, plus a written description of what the image is,
    what it relates to, and hyperlinks into the rest of the investigation.

This prompt runs MANY times. Pages will usually already exist from earlier
runs, written before additional data existed. Rerunning must read each
existing page in, then rewrite it against the current YAML data and the
current {LAYOUT_GUIDELINES}. The run is idempotent: same inputs, same pages.

============================
KNOWLEDGE — READ FIRST, IN THIS ORDER
============================

At the very start of every run, read into the context window:

  1. {LAYOUT_GUIDELINES} — the standards file for images pages. It starts
     nearly empty and grows over time. Whatever rules it contains are followed
     and they OVERRIDE any conflicting rule in this prompt. Read it first,
     every run, before writing anything.
  2. {CK_FILE} — the master investigation file. This is very important
     knowledge for understanding the entire Charlie Kirk assassination, and it
     must be in the context window at the very start. It is the source of
     truth for what every concept, cluster, and open question actually is, and
     it is what the image descriptions are grounded in. It is 400K+ lines; the
     orchestrator loads the section headers plus the sections relevant to the
     clusters being processed, and each parallel agent loads the sections
     relevant to ITS clusters before writing a word.
  3. {CHARTER_FILE} — the image_planning charter: audience model, level
     model, YAML schema, hard rules.
  4. {ASSESS_MANUAL} — the site-wide writing and layout guide. All published
     pages must meet it.
  5. {HIERARCHY_FILE} — parse fully. Index every node (_key, title, depth,
     parentage) and every image (sha256, file_path, sidecar paths,
     on_site_pages, also_filed_in).
  6. {PAGES_CSV} — the master page index. Needed to resolve link targets and
     to keep in sync afterward.

============================
KNOWLEDGE — THE PAGE MODEL
============================

The site levels: Level 1 is the site home, Level 2 is the images landing page
({IMAGES_L2_PAGE}, url /Photos, left-bar label "Photos"). The YAML's level_3
nodes become the pages directly under it, level_4 under those, level_5 under
those. Image pages hang off whichever node owns the image.

Directory and file layout under {PHOTOS_DIR}:

  {PHOTOS_DIR}/overview.mdx                       the Level 2 landing page
  {PHOTOS_DIR}/{L3_key}/overview.mdx              level_3 cluster page
  {PHOTOS_DIR}/{L3_key}/{L4_key}/overview.mdx     level_4 cluster page
  {PHOTOS_DIR}/{L3_key}/{L4_key}/{L5_key}/overview.mdx   level_5 cluster page
  {node dir}/{image_key}.mdx                      image page, in its node's dir

  * {L3_key} etc. are the node's _key from the YAML, used verbatim.
  * {image_key} is a stable per-image page key: derive it from the image
    filename stem, sanitized to [A-Za-z0-9_], four words or less, made unique
    within the whole site by appending the first 8 hex chars of the sha256
    when the stem alone collides or is meaningless (screenshots, hash-named
    files). Once minted, an image_key never changes across runs — on rerun,
    reuse the existing page's key (match existing pages to YAML entries by
    the sha256 recorded in the page, see BOOKKEEPING below).

Navigation rules (from the charter — a visitor never dead-ends):

  * Every cluster page carries a table of contents with hyperlinks to its
    PEERS (other nodes at its level under the same parent), its PARENT, its
    CHILD clusters, and its own image pages.
  * Every image page links to its parent cluster page, and to its peer image
    pages (previous / next within the cluster is enough).
  * The Level 2 landing page {IMAGES_L2_PAGE} keeps its existing prose and
    gains/refreshes a table of contents section: a table linking to every
    level_3 page with its title and recursive image count. Regenerate only
    that TOC section between clear markers ({/* PHOTOS_TOC_START */} and
    {/* PHOTOS_TOC_END */}); never touch the prose outside the markers.

Two arrival paths must both work (the charter's audience model): a visitor
browsing cold from the left bar down through the Level 2 page, and a visitor
arriving from a topic page elsewhere on the site who wants to SEE the evidence
for that topic, one click, already grouped.

============================
KNOWLEDGE — IMAGE PAGE LAYOUT SPEC
============================

Every image page hosts exactly one image and follows this layout. Where
{LAYOUT_GUIDELINES} adds or contradicts, {LAYOUT_GUIDELINES} wins.

  * No right bar. Set hide_table_of_contents: true in the frontmatter so the
    page renders without the right-hand TOC rail.
  * The image keeps its true aspect ratio. Never stretch, never crop.
  * The image's RIGHT edge aligns with the page's right side: 5px to the left
    of the right edge of the browser window. That is where the image's right
    side sits.
  * The image sizes itself inside a bounding box defined by:
      - width: no more than 70% of the MAIN AREA width. The main area is the
        full browser width minus the left bar.
      - height: no taller than the box; the BOTTOM of the bounding rectangle
        is 10px up from the bottom of the browser page.
  * The image fills however much of that box its aspect ratio allows — it
    will often not need the full width or the full height. A wide image hits
    the 70% width limit first; a tall image hits the height limit first.
  * Implement with CSS on the page (or a small shared component under
    {SITE_DIR}/src/ reused by every image page — preferred, so a later change
    to the spec is one edit). The behavior in CSS terms: a container pinned
    toward the viewport's bottom-right (right: 5px equivalent, bottom offset
    10px), image with width:auto, height:auto, max-width: 70% of the main
    content area, max-height: viewport height minus the page-top offset minus
    10px, object-fit: contain.
  * The written description occupies the remaining main-area space to the
    left of / above the image and must remain readable at laptop widths.
  * Test at least one wide image and one tall image visually after the first
    run of a new layout implementation (npm start, eyeball, or screenshot).

============================
KNOWLEDGE — THE EXCLUSION GATE (NOT EVERYTHING IN THE YAML MAY BE PUBLISHED)
============================

{EXCLUDE_FILE} lists sha256 values that must never be published, one per line,
with a comment saying why. The run reads it before generating anything. An
excluded image gets no page and no static copy, and any page or static copy
that already exists for it is DELETED.

This gate exists because the mirror is a years-long personal filing area and
private material has been swept into it by accident — bank and health-account
dashboards, booking confirmations, billing portals, video calls showing named
participants' faces. Eleven such entries were found published during the first
full run.

Two rules follow from that episode:

  * Careful prose is NOT sufficient protection. A description can omit every
    account number and name and the page is still an exposure, because the
    image itself is served full size at a public URL. The image is the payload.
  * The gate lives here, not in the YAML. {HIERARCHY_FILE} is read-only to this
    prompt, so an exclusion recorded only there would be undone by the next
    hierarchy pass. Recording it in {EXCLUDE_FILE} makes it survive every
    regeneration.

When a run finds material that should not be published — private personal
documents, an unrelated third party's records, anything whose subject has no
connection to the investigation — add the sha256 to {EXCLUDE_FILE} with a
reason, and record it in {FINDINGS_FILE} so the hierarchy can drop the entry
at its source.

============================
KNOWLEDGE — HOSTING THE IMAGE FILE
============================

The originals live outside the repo (mostly under {MIRROR_DIR}), so each
published image needs a servable copy:

  * Copy the original to {STATIC_IMG_DIR}/{sha256}.{ext} (lowercase original
    extension). The sha256 name is ASCII-safe, deduplicates automatically
    (cross-filed images copy once), and dodges the invisible-Unicode
    filenames the mirror contains (macOS screenshot names carry U+202F).
  * Reference it from the page as /img/evidence/{sha256}.{ext}.
  * Skip the copy when the target already exists (rerun-friendly).
  * If an entry has no local file but has an ipfs_url, embed the IPFS URL
    directly (ipfs.io primary; the site's existing IPFS embeds show the
    pattern). If it has neither, the image page is still generated with the
    description and a "media pending" note, so the hierarchy stays complete.
  * Do not commit multi-megabyte originals into {DOCS_DIR}; static assets go
    only under {STATIC_IMG_DIR}. If an original exceeds ~2MB, write a
    downscaled copy (longest side 2000px, quality ~85) instead — the page
    serves the web copy; the mirror keeps the original.

============================
KNOWLEDGE — WRITING THE DESCRIPTION
============================

Every image page gets a written description of what the image is and what it
is related to. Build it from ALL of these sources:

  * The inline ai_description in the YAML — the starting point.
  * The sidecar files pointed to by the YAML — when the entry has an
    ai_description_file, ocr_file, or transcription_file path, READ those
    files whenever they would improve the write-up. The OCR gives the literal
    on-screen text (screenshots, documents, chyrons) and is often the richest
    source; quote from it where it helps.
  * The hosting pages — this image often came from some other Level 2 or
    Level 3 document outside the images Level 2. The YAML records these in
    on_site_pages (and the node's site_page / site_level_2). Read each hosting
    page, understand its topic, and explain in the description how this image
    relates to the page(s) it was hosted on. An image may be hosted on
    multiple pages — cover each relationship.
  * {CK_FILE} — the bigger Charlie Kirk investigation. Use it to the best of
    our ability to understand the image, the area of the investigation it
    belongs to, and to describe that area accurately.

The description carries HYPERLINKS off to other Level 2s and Level 3s of the
site — the sections and pages this image connects to. Link section overviews
as /X/overview (not the bare /X); resolve every target against {PAGES_CSV}
and prefer routes that are known to build.

Safe-writing rules for every description (mandatory, from the repo charter):

  * The word "defamation" must NOT appear anywhere in the article text.
  * Never write that any person KNEW anything before the crime, or DID
    anything immoral or illegal. Check the writing specifically for these two
    failure modes and remove them.
  * Never state as fact that a living person committed a crime unless
    court-proven. Use attribution language: "according to ...", "allegedly",
    "reportedly", "researchers have questioned ...". Frame suspicions as
    questions or reported claims, not conclusions.
  * Within those limits, include as MUCH information as possible. The rules
    constrain phrasing, not depth — do not solve the problem by writing less.
  * Raw unfiltered claims stay private in {CK_FILE} and the planning layer;
    only scrubbed writing is published.

Style: follow {ASSESS_MANUAL}. MDX gotcha: comments in .mdx must be
{/* ... */} — HTML <!-- --> comments fail the MDX compile and break deploy.

============================
KNOWLEDGE — BOOKKEEPING FIELDS ON PAGES
============================

So reruns can match pages to YAML entries and rewrite them safely, every
generated page embeds machine-readable frontmatter:

  * Cluster page frontmatter: title, plus custom fields
      ck_node_key: <_key>
  * Image page frontmatter: title, hide_table_of_contents: true, plus
      ck_image_sha256: <sha256>
      ck_node_key: <owning node _key>

On rerun, an existing page is matched by ck_image_sha256 / ck_node_key first,
filename second. A rerun REFRESHES STRUCTURE BUT PRESERVES PROSE:

  * Regenerated every run (always current, always safe to overwrite): slug and
    the mechanical frontmatter fields, the back button, the image block's src
    and href, the layout classNames and the text column's maxWidth, the
    "Where This Image Appears" list, "Related Areas", the peer/child tables of
    contents, and the previous/next navigation.
  * Carried forward when the existing page has them: the page title,
    sidebar_label and frontmatter description, the img alt text, the prose
    under "## What This Image Shows" on image pages, and the three paragraphs
    under "## About This Cluster" on cluster pages.

This matters because the writing pass costs far more than the generation pass
and is done against sources the generator never reads (OCR sidecars, host
pages, {CK_FILE}). A regeneration must never throw that away, and it must
never resurrect raw YAML text over prose that was deliberately scrubbed for
safe-writing reasons. Baseline (unenriched) prose IS replaced — the generator
recognizes its own boilerplate and refreshes it from current YAML data.

Pages under {PHOTOS_DIR} that the current YAML no longer accounts for are
removed as orphans (they can only come from a renamed key or a removed node,
and leaving them strands dead pages in the build); their removal is counted
and reported every run.

============================
STAGE 1 — SETUP AND READ
============================

* Read, in order: {LAYOUT_GUIDELINES}, {CK_FILE} (see READ FIRST for how),
  {CHARTER_FILE}, {ASSESS_MANUAL}, {HIERARCHY_FILE}, {PAGES_CSV}.
* Parse the YAML into an index: every node with depth, parent, _key, title,
  site bindings; every image with sha256, file_path, sidecars, on_site_pages.
* Inventory the existing pages under {PHOTOS_DIR}: for each, extract
  ck_node_key / ck_image_sha256 from frontmatter. Build the existing-page map.
* Verify {STATIC_IMG_DIR} exists (create if missing).

Output to stdout:
============================
STAGE 1 COMPLETE
Layout guidelines lines: N
YAML nodes: N level_3 / N level_4 / N level_5   images: N unique sha256
Existing pages found: N cluster / N image
============================

============================
STAGE 2 — PARTITION THE WORK
============================

* Partition the level_3 nodes (each with its whole subtree) into up to
  {MAX_AGENTS} partitions, balanced by number_of_images_recursive so the
  agents finish at roughly the same time. Fewer partitions when there are
  fewer level_3s or the corpus is small; up to 12 in parallel is expected and
  encouraged on full runs.
* A node subtree never splits across two agents — every image page and its
  cluster pages are written by one agent, so peer links within a subtree are
  consistent.
* Give every agent its OWN scratch subdirectory and tell it never to write to
  the shared scratchpad root. Agents independently invent the same helper
  filenames (apply.py, dump.py, out.json); in a 12-way parallel run those
  collide and one agent's file silently replaces another's mid-run. This has
  actually happened — isolate the directories up front.
* Cross-partition links (peer level_3s, links into other site sections) are
  resolvable from the YAML index and {PAGES_CSV}, which every agent receives.

Output to stdout:
============================
STAGE 2 COMPLETE
Partitions: N   (list: partition -> level_3 _keys -> recursive image count)
============================

============================
STAGE 3 — PARALLEL PAGE GENERATION (UP TO {MAX_AGENTS} AGENTS)
============================

Launch the partitions as parallel agents in a single burst. Each agent
receives: its partition's YAML subtree(s), the full node index (for
cross-links), the layout spec, the {LAYOUT_GUIDELINES} contents, the writing
rules, the existing-page map for its subtree, and pointers to {CK_FILE},
{PAGES_CSV}, {ASSESS_MANUAL}.

Each agent, for its subtree, working top-down:

* Read the {CK_FILE} sections relevant to its clusters.
* For every cluster node: create or rewrite the cluster overview.mdx with
  title, a short concept paragraph (grounded in {CK_FILE}, safe-writing rules
  apply), and the full TOC — parent, peers, child clusters, image pages.
* For every image entry:
    * Ensure the static copy exists per HOSTING THE IMAGE FILE.
    * If a page for this sha256 already exists in this node's dir, read it in
      first, then rewrite it. Otherwise mint the image_key and create it.
    * Apply the IMAGE PAGE LAYOUT SPEC exactly.
    * Write the description per WRITING THE DESCRIPTION — reading the
      sidecar OCR / ai_description files when they help, reading the
      on_site_pages hosting pages, explaining the relationships, hyperlinking
      to related Level 2s and Level 3s.
    * Run the safe-writing check on the finished text: no "defamation" word,
      no prior-knowledge claims, no immoral/illegal-conduct claims about any
      person, attribution language throughout.
* Return to the orchestrator (do not write {PAGES_CSV} or {IMAGES_L2_PAGE}
  directly — the orchestrator owns shared files to avoid write collisions):
    * The list of pages created / rewritten / unchanged, with for each: the
      page_key ( = node _key or image_key), parent_key, level, url_path,
      file_path, title, sidebar_label, directory, extension, line_count.
    * Any orphan pages, missing originals, missing sidecars, or unresolvable
      links it hit.

Output to stdout (after all agents return):
============================
STAGE 3 COMPLETE
Agents run: N
Cluster pages: N created, N rewritten
Image pages: N created, N rewritten
Static copies written: N (N downscaled)   IPFS embeds: N   media pending: N
Problems reported: N (list)
============================

============================
STAGE 4 — SHARED FILES: LANDING PAGE AND PAGES.CSV
============================

Orchestrator only, single-threaded:

* Regenerate the TOC section of {IMAGES_L2_PAGE} between the
  PHOTOS_TOC_START / PHOTOS_TOC_END markers (insert the markers before the
  final paragraph if this is the first run). Table of every level_3: title
  linked to its page, recursive image count. Prose outside markers untouched.
* Merge every agent's page rows into {PAGES_CSV}: add rows for new pages,
  update rows for retitled/moved pages, following the CSV schema in
  {ROOT_DIR}/claude.md (page_key = node _key or image_key, parent_key = the
  parent node's _key — image pages parent to their owning node; level = node
  depth, or node depth + 1 for image pages). Never remove rows for pages that
  still exist; report rows whose files vanished instead of deleting blindly.

Output to stdout:
============================
STAGE 4 COMPLETE
Landing page TOC rows: N
pages.csv: N rows added, N updated, N flagged
============================

============================
OUTPUT SANITIZATION — NO INVISIBLE UNICODE, EVER (SECURITY RULE)
============================

Every emitted file — every .mdx page, {PAGES_CSV} rows, and any component or
CSS written — must never contain invisible Unicode characters (zero-width
spaces, bidi controls, no-break spaces including U+202F, word joiners, BOMs,
control characters, variation selectors, tag characters). They can hide
content from review and smuggle instructions past a human reading the file.

  * Prose: replace space-like invisibles with a regular space, delete
    zero-width/bidi/control characters, collapse whitespace. Visible
    non-ASCII (em dashes, accented letters) may stay.
  * Paths and URLs that must keep matching disk: this prompt sidesteps the
    problem by serving sha256-named static copies, so published pages never
    contain mirror filenames. If a mirror path must appear in a page for any
    reason, emit non-ASCII as visible escapes instead.

After every emit pass, re-scan all written files for the invisible set and
hard-fail if any code point remains. (The invisible set is enumerated in
{THIS_DIR}/p_create_image_hierarchy.md — same list applies here.)

============================
STAGE 5 — BUILD, VERIFY, REPORT
============================

* Run the Docusaurus build: cd {SITE_DIR} && npm run build. It must pass.
  Broken links and MDX compile errors (e.g. a stray <!-- --> comment) surface
  here — fix and rebuild until green.
* Spot-check 10 image pages across different partitions: frontmatter fields
  present, hide_table_of_contents true, image src resolves to an existing
  static file or IPFS URL, layout component/CSS applied, description has at
  least one hyperlink to another Level 2/Level 3, safe-writing check passes,
  the word "defamation" absent.
* Spot-check 5 cluster pages: TOC lists all peers, children, and image pages;
  every link resolves.
* Confirm {PAGES_CSV} row count change matches pages created.
* Run the invisible-Unicode scan over everything written this run.
* Confirm nothing outside {PHOTOS_DIR}, {STATIC_IMG_DIR}, {PAGES_CSV}, and
  (marker section only) {IMAGES_L2_PAGE} was modified. sidebars.ts untouched.

Output to stdout:
============================
STAGE 5 COMPLETE — FINAL REPORT
Build: PASS/FAIL
Pages now under /Photos: N cluster + N image = N total
Images published: N of N in YAML (N pending media)
Spot-checks: image pages N/10 pass, cluster pages N/5 pass
pages.csv in sync: yes   sidebars.ts untouched: yes   invisible scan: clean
============================

============================
HARD RULES
============================

* {LAYOUT_GUIDELINES} is read at the very start of every run and its rules
  override this prompt where they conflict. It grows over time; never edit it
  from this prompt.
* {CK_FILE} is read into the context window at the very start — it is the
  knowledge base for understanding the entire assassination and every
  description is grounded in it.
* This prompt writes ONLY: pages under {PHOTOS_DIR}, static copies under
  {STATIC_IMG_DIR}, the marked TOC section of {IMAGES_L2_PAGE}, a shared
  layout component/CSS under {SITE_DIR}/src/ if used, and {PAGES_CSV} rows.
  It never modifies {HIERARCHY_FILE}'s data (read-only input), never touches
  {SITE_DIR}/sidebars.ts, and never writes planning notes into the site or
  Docusaurus pages into {THIS_DIR}.
* Reruns refresh structure and PRESERVE authored prose (see BOOKKEEPING
  FIELDS ON PAGES). An enrichment pass's writing, and any safe-writing scrub
  applied to a page, must survive every later regeneration. Orphan removals
  are counted and reported.
* Every image page: one image, no right bar, aspect ratio true, right edge
  5px from the browser's right edge, max 70% of main-area width, bounding box
  bottom 10px above the browser bottom.
* Every description: maximum information within the safe-writing rules; the
  word "defamation" never appears; no claims of prior knowledge or of
  immoral/illegal conduct; attribution language; links to related Level 2s
  and Level 3s as /X/overview-style routes verified against {PAGES_CSV}.
* Nothing listed in {EXCLUDE_FILE} is ever published, and anything found
  during a run that should not be public is added to it before the run ends.
  Prose care does not substitute for withholding the image.
* The YAML is an input, not an authority on what is true or publishable. Its
  inline ai_description text is model output and has been wrong about people,
  places and events; its clustering sometimes files an image as supporting a
  thesis that the image's own contents contradict. Write what the evidence
  actually shows, say so on the page when it differs from the filing, and
  record the discrepancy in {FINDINGS_FILE}.
* Up to {MAX_AGENTS} parallel agents, partitioned by YAML subtree; shared
  files ({PAGES_CSV}, {IMAGES_L2_PAGE}) are written only by the orchestrator.
* No invisible Unicode in any emitted file — scan after every emit.
* The build must pass before the run is declared complete.

============================
BACKGROUND — ORIGINAL DIRECTIVE, KNOWLEDGE PRESERVED
============================

This section preserves the full intent of the directive this prompt was built
from, so no knowledge is lost even where a stage above already encodes it.

* Create this prompt file but do not run it yet. Learn from the entire
  image_planning directory. By the time this prompt runs, the YAML file will
  already be built and it has all the data we need.
* In our charlie-kirk Docusaurus we have a Level 2 directory called images
  (today: Photos). The goal is to create the .mdx pages under that images
  Level 2 directory. The content comes from the YAML file.
* The goal is to host the image. These pages should not have a right bar. The
  image must be the right aspect ratio. The right side of the image aligns
  with the webpage's right side, 5px left of the right edge of the browser —
  that is where the image's right side is.
* There is an area where the image can go; it fills however much is
  appropriate, defined by: no more than 70% of the width of the main area
  (the main area is the full browser width minus the left bar); it won't be
  taller than the box; the bottom of the bounding rectangle is 10px up from
  the bottom of the browser page. That is the bounding box. The image often
  will not need the full width or the full height, depending on its aspect
  ratio.
* Each page carries a description of the content: what the image is and what
  it is related to. The description has hyperlinks off to other Level 2s and
  Level 3s. The image often came from some other Level 2 or Level 3 document
  outside the images Level 2; if that other page hosted this image, we want
  to understand that topic and explain this image and how it relates to the
  page it was hosted on. It might be hosted on multiple pages. The bigger
  Charlie Kirk investigation is used, to the best of our ability, to
  understand the image and where it is hosted — that also gives context. We
  describe that area of the investigation.
* We make no defamatory claims. The word "defamation" should not appear in
  the article. The writing must not say anybody knew anything before the
  crime or did anything immoral or illegal — check the writing for exactly
  that — while including as much information as possible without causing
  those problems.
* When the YAML has pointers to the OCR file, the AI description file, or the
  inline AI description, we sometimes read those files in order to build the
  best writing for the page's write-up.
* layout_guidelines.txt lives in this directory (created with three empty
  lines). Over time it will explain more standards for our images pages. When
  this prompt runs, that file is read into the context window right away, and
  whatever rules it has are followed.
* When this prompt runs it can run up to 12 different agents in parallel, and
  it probably could and should: take different sections of the YAML file,
  partition them among the 12 agents, and each agent works its section —
  updating the pages under the Level 2 images, making sure the image is
  hosted on the page, the image size is correct, and the content written on
  the page is updated.
* This prompt will often run multiple times, so it has to rewrite pages. The
  pages are often pre-existing, written earlier before additional data was
  there, and the run needs to read them in.
* {CK_FILE} (~/BGit/Bryan_git/charlie-kirk/Charlie_Kirk.txt) is very
  important and must be read into the context window at the very start of the
  run. It is the knowledge needed to understand the entire Charlie Kirk
  assassination.
