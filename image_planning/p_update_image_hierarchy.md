ROOT_DIR dir is ~/BGit/Bryan_git/charlie-kirk

THIS_DIR dir is {ROOT_DIR}/image_planning
IMAGES_DIR dir is {ROOT_DIR}/images
HIERARCHY_FILE is file {IMAGES_DIR}/images.yaml
  Moved 2026-07-22. It used to be {THIS_DIR}/hierarchy_images.yaml. That old
  name and that old location are both gone — the file is now images.yaml and it
  lives in {IMAGES_DIR}, not in {THIS_DIR}.
GENERATOR_DIR dir is {THIS_DIR}/generator
INVENTORY_TSV is file {GENERATOR_DIR}/inventory.tsv

SITE_DIR dir is {ROOT_DIR}/site
DOCS_DIR dir is {SITE_DIR}/docs
HOME_PAGE is file {DOCS_DIR}/index.mdx
IMAGES_L2_PAGE is file {DOCS_DIR}/Photos/overview.mdx
PAGES_CSV is file {ROOT_DIR}/pages.csv
CK_FILE is file {ROOT_DIR}/Charlie_Kirk.txt
CHARTER_FILE is file {THIS_DIR}/CLAUDE.md

MIRROR_DIR dir is ~/_Mirror/Politics/Charlie_Kirk_Mi
MIRROR_SIDECAR_DIR dir is ~/BGit/Bryan_git/personal_large_files_bridge/_Mirror/Politics/Charlie_Kirk_Mi
REPO_SIDECAR_DIR dir is {ROOT_DIR}/.lfbridge

LFB_DIR dir is ~/BGit/Bryan_git/LargeFileBridge
LFB_PM_DIR dir is {LFB_DIR}/pm
COMPANY_BRIDGE_DIR dir is ~/BGit/act3/act3_large_files_bridge
PERSONAL_BRIDGE_DIR dir is ~/BGit/Bryan_git/personal_large_files_bridge

============================
GOAL
============================

Grow and improve {HIERARCHY_FILE} — the image evidence hierarchy YAML — so it
becomes the most full and complete hierarchy possible over the investigation's
image and video corpus. This prompt runs in multiple stages. Each stage adds to
the YAML or enriches it. Nothing is ever deleted from it. No duplicates are
ever created — when an item already exists, its YAML properties are updated in
place instead.

The end state this YAML is building toward: the site will eventually host an
image page for every image, all living under one Level 2 directory called
images (today that Level 2 is the Photos section, {IMAGES_L2_PAGE}). When we
later create the list-of-images page — the top level of the images area — that
page will be mostly a table of contents: a table with links into the images
directory's Level 3 pages, and those Level 3 pages come directly from the
level_3 nodes of this YAML. This prompt builds the YAML only. It does NOT
create or modify any Docusaurus page, and it does NOT touch sidebars.ts or
{PAGES_CSV}. Page generation is a later, separate prompt.

Convergence priority order (if context runs short, complete in this order):
  1. Stage 3 — site Level 2 sweep into YAML level_3 superset
  2. Stage 5 — filesystem Level 3/4 pages into YAML level_4/level_5 nodes
  3. Stage 6 — page image sweep into YAML image entries
  4. Stage 7 — sidecar file-path properties on every image and video
  5. Stage 8 — image_page path on every image entry
  6. Stage 4 — home page tables of contents into more level_3s
  7. Stage 9 — counts and needs_split
  8. Stage 10 — verify

============================
KNOWLEDGE — THE LEVEL MODEL (READ THIS FIRST)
============================

Two different level systems are in play. Do not confuse them.

The SITE (filesystem) levels:
  * Level 1 — the site home page ({HOME_PAGE}).
  * Level 2 — the top-level sections: the directories directly under
    {DOCS_DIR}. Examples: TPUSA, FBI, UVU, Israel, Mic, Planes, Timeline.
    Photos (images) and Videos are also Level 2s.
  * Level 3 — the pages inside a Level 2 directory (overview.md plus the
    individual analysis pages, and first-level subdirectory overviews).
  * Level 4 — pages one directory deeper.

The YAML ({HIERARCHY_FILE}) levels:
  * There is no level_1 and no level_2 inside the YAML. Level 1 is the site
    home and Level 2 is the images landing page itself, so the YAML's cluster
    tree begins at level_3.
  * "Level two refers to the images directory" — the entire YAML tree hangs
    under the future images Level 2 page. Every YAML level_3 becomes a child
    page of that images Level 2.

THE CORE MAPPING RULE — increment by one:
  We are effectively taking all the Level 2s, Level 3s, and Level 4s that exist
  in the site filesystem outside this YAML and reproducing that same hierarchy
  inside the YAML, but with every level number incremented by one:

    site filesystem Level 2  →  YAML level_3
    site filesystem Level 3  →  YAML level_4
    site filesystem Level 4  →  YAML level_5

  So the YAML's level_3 list is a SUPERSET that includes the site's list of
  Level 2s (except images, videos, and unfiltered/queue categories — see
  Stage 3), the YAML's level_4 nodes correlate to the site's Level 3 pages
  parented hierarchically under their appropriate level_3 parent, and each
  image found on a site Level 3 page becomes a level_5 entry parented on the
  level_4 node that correlates to that filesystem Level 3 page.

  Additionally, image clusters that came from the mirror
  ({MIRROR_DIR}) already exist in the YAML and stay — the site-derived nodes
  merge INTO this tree, they do not replace it.

============================
KNOWLEDGE — THE YAML FILE TODAY
============================

{HIERARCHY_FILE} exists (about 9,000 lines, ~500KB). Read it and learn from it
before changing anything. Its current shape:

  * Root key `level_3:` is an array. Each item is itself keyed `level_3:`.
    A level_3 node may contain a `level_4:` array; a level_4 may contain a
    `level_5:` array. Same shape at every depth.
  * Cluster node fields: title (human readable, spaces allowed), _key
    (underscores, four words or less, unique across the WHOLE file — this is
    the future page_key in {PAGES_CSV}), number_of_images (direct count),
    number_of_images_recursive (subtree count), optional
    needs_split: true (node is over the 12-image ceiling; split on a later
    pass), images (array of image items).
  * Image item fields today: cid (IPFS CID, intentionally empty — IPFS not
    assigned yet; spoken as "SID", it means the CID), sha256 (the identity —
    fingerprint from Large File Bridge is deferred, sha256 stands in),
    file_path (path to the original file, usually under {MIRROR_DIR}),
    ai_description (inline prose text, mostly empty today),
    ai_description_file / ocr_file / transcription_file (paths to the Large
    File Bridge sidecars, "" when the sidecar does not exist — see Stage 7),
    image_page (path to the published Level 5 page that hosts this one image,
    "" when no page exists yet — see Stage 8), optional on_site_pages (list of
    other site pages the image is embedded on), optional ipfs_url (for entries
    that exist only as an IPFS embed with no local file), optional
    also_filed_in (list of other mirror dirs the same sha256 legitimately
    lives in — cross-filing is deliberate and kept).

  * The full property set on an image item, in emission order:

      images:
        - image:
            cid: ""
            sha256: c51ef651e0e2fd9187ac8fa0b5d25908baba279b0c03f1ea93f6522fa3cedbb4
            file_path: "~/_Mirror/Politics/Charlie_Kirk_Mi/Censorship/G3o-JSJWUAA6XUC.jpeg"
            ai_description: "This image shows a wide-angle, daytime view of a crowded outdoor courtyard ..."
            ai_description_file: "~/BGit/Bryan_git/personal_large_files_bridge/_Mirror/Politics/Charlie_Kirk_Mi/Censorship/G3o-JSJWUAA6XUC.jpeg.ai_description"
            ocr_file: "~/BGit/Bryan_git/personal_large_files_bridge/_Mirror/Politics/Charlie_Kirk_Mi/Censorship/G3o-JSJWUAA6XUC.jpeg.ocr"
            transcription_file: ""
            image_page: "~/BGit/Bryan_git/charlie-kirk/site/docs/Photos/FBI/Img_Photo_c51ef6.mdx"

    Every image entry carries every one of these properties. A property that
    has no value is emitted as the empty string "" — never omitted, never
    null. Absence of the key would make later passes unable to tell "not
    looked up yet" from "looked up, does not exist."
  * About 21 level_3 clusters exist today (FBI, The Shot and the Shooter
    Position, Unfiled Backlog, Patsy Candidates, Security Team, TPUSA, Court
    and Legal Proceedings, Aircraft and Flight Evidence, Tyler Robinson,
    Memes and Commentary, Ballistics and the Gun, The UVU Venue, Charlie Kirk
    Himself, People of the Investigation, The Microphone, CIA and US
    Intelligence, Google Search Evidence, The Table Hand Off, Maps and Site
    Geometry, Israel and Mossad, The Truck and Back of Tent). They were
    generated by a first pass from the mirror's own concept filing.
  * Prior art: {GENERATOR_DIR}/gen_hierarchy.js built that first pass from
    {INVENTORY_TSV} (sha256, dir, filename, orig_path, has_desc per image)
    plus a clusters.json merge map. Read both to understand how dedupe was
    done (same sha256 in the SAME dir collapses; same sha256 in DIFFERENT
    concept dirs is deliberate and recorded as also_filed_in) and how unique
    _keys were minted. Reuse those conventions.

Cluster sizing rules (from the charter, {CHARTER_FILE}):
  * Six images per page is the target. Twelve is the ceiling. Over twelve
    means the node is not one concept — mark needs_split: true and split one
    level deeper on a later pass.
  * Clusters are concept clusters. The question is always "what is this
    evidence about," never "when was it downloaded" or "who posted it."
  * Titles may use spaces and full words. Keys use underscores, four words or
    less, unique file-wide.

============================
KNOWLEDGE — SIDECAR FILES (OCR, TRANSCRIPTION, AI DESCRIPTION) AND THE PATH MAPPING
============================

Large File Bridge (the web app at {LFB_DIR}; understand it by reading the
product management specification files in {LFB_PM_DIR} and the code) produces
three sidecar text files per media file. They answer three different questions:

  * .transcription   — "what was SAID" (audio/video speech, verbatim)
  * .ai_description  — "what is SEEN" (a vision model's hyper-detailed prose
                       about the image or video frame)
  * .ocr             — "what does it SAY on screen" (the literal text visible
                       in the pixels, verbatim — screenshots, slides, signs,
                       chyrons, documents)

Naming rule: the sidecar keeps the media file's FULL filename (original
extension kept) and APPENDS the second-level extension:
  Blue_Side.mp4  →  Blue_Side.mp4.transcription
  Blue_Side.mp4  →  Blue_Side.mp4.ai_description
  Blue_Side.mp4  →  Blue_Side.mp4.ocr
  photo.jpg      →  photo.jpg.ai_description  (and photo.jpg.ocr)

Placement rule — where the sidecar lives depends on whether the original is
inside a working git repo (this is the mapping pattern; the authoritative spec
is {LFB_PM_DIR}/artifact_placement_policy.mdx section 0, with
ai_description.mdx, ocr.mdx, Transcribe.mdx, and repo_tracking_scheme.mdx):

  * Original INSIDE a working git repo — the sidecar is path-mirrored under
    that repo's committed .lfbridge/ tracking directory:
      {ROOT_DIR}/videos/X.mp4
        →  {REPO_SIDECAR_DIR}/videos/X.mp4.transcription
      {REPO_SIDECAR_DIR} currently holds videos/ and IPFS/videos/ sidecars.

  * Original OUTSIDE any git repo (the mirror) — there is NO .lfbridge/
    segment. The dedicated bridge repo (an "SDL": a personal or company file
    repo that exists only to hold these files) IS the tracking area, and the
    mirror hangs directly off its root:
      {MIRROR_DIR}/Autopsy/X.jpg
        →  {MIRROR_SIDECAR_DIR}/Autopsy/X.jpg.ai_description
      Personal SDL: {PERSONAL_BRIDGE_DIR}
      Company SDL:  {COMPANY_BRIDGE_DIR}

  * Older files may still sit under a .lfbridge/_Mirror/ path until Large File
    Bridge migrates them. Check both locations before concluding a sidecar is
    missing.

Coverage snapshot at the time this prompt was written (re-count at run time —
these grow constantly): under {MIRROR_SIDECAR_DIR} there were ~1,978
.ai_description files, ~1,795 .ocr files, and ~331 .transcription files.
Coverage is no longer thin — most images now have descriptions and OCR.

WHAT THIS MEANS FOR THE YAML: every image and every video entry in
{HIERARCHY_FILE} gets YAML properties holding the FILE PATH to each sidecar
that exists for it. This is required — the sidecars are how later passes
search, cluster, caption, and publish. The properties are:

  ai_description_file   path to the .ai_description sidecar, or "" if none
  ocr_file              path to the .ocr sidecar, or "" if none
  transcription_file    path to the .transcription sidecar, or "" if none
                        (mostly videos; images rarely have one)

The existing inline ai_description field stays as the short prose text; the
new *_file fields point at the full sidecar files on disk.

============================
KNOWLEDGE — THE SITE'S LEVEL 2 SECTIONS (SNAPSHOT)
============================

Enumerate live at run time (ls {DOCS_DIR}) — the list below is a snapshot so
you know what to expect. Directories directly under {DOCS_DIR}:

  After, analysis_documentation, Before, cameras, campus_university,
  Cause_of_Death, Censorship, Charlie, Companies_Organizations, court,
  CoverUp, Defamation, distraction_people, Drones, Electrocution, FBI, Fix,
  GoogleSearches, gov, Gov_Mind_Control, government_organizations, Gun_Bullet,
  Influencers, intelligence, Iran, Israel, Israel_Main_Suspect,
  key_individuals, Killer, Law_Enforcement, laws, Legal, legal_investigation,
  Locations, maps, Media, Medical, Mic, Motive, Narrative,
  organizations_groups, Other, other_topics, People, Photos, Planes,
  political_context, Proof_Intel_Services, Proof_Not_Tyler,
  security_law_enforcement, Security_Team, social_media_analysis, Suspects,
  Suspicious, technology_surveillance, Tent, Theories, Timeline,
  Topic-Analyses, Topics3, TPUSA, Tyler_Robinson, Tyler_Robinson_Not_Assassin,
  US_Intelligence, US_Intelligence_Assisted, UVU, Videos, Vote, Witnesses,
  Your_Actions_Fix_It

{PAGES_CSV} is the master page index (page_key, parent_key, level, url_path,
file_path, title, ...). Use it alongside the filesystem walk — the CSV gives
you each page's level and parentage directly; the filesystem walk catches any
drift. When they disagree, the filesystem is what actually exists.

============================
STAGE 1 — SETUP AND READ
============================

* Read {CHARTER_FILE} — the image_planning charter. It is the authority on
  the audience model, the level model, the YAML schema, and the hard rules.
* Read {HIERARCHY_FILE} fully. Build an in-memory index of: every _key, every
  node path, every sha256 and the node(s) it lives under.
* Read {GENERATOR_DIR}/gen_hierarchy.js, {GENERATOR_DIR}/clusters.json, and
  the header of {INVENTORY_TSV} — the prior-art conventions.
* Read {PAGES_CSV}.
* Enumerate {DOCS_DIR} top-level directories (the site Level 2s).
* Reference {CK_FILE} as needed throughout — it is the source of truth for
  what the investigation's concepts actually are. The hierarchy must mirror
  the investigation's real concept structure, not an arbitrary photo-album
  structure. Do not read all 400K+ lines up front; consult sections when a
  clustering or parenting decision needs arbitration.

Output to stdout:
============================
STAGE 1 COMPLETE
YAML nodes indexed: N level_3 / N level_4 / N level_5
Images indexed: N unique sha256
Site Level 2 dirs found: N
pages.csv rows: N
============================

============================
STAGE 2 — LEARN THE SIDECAR MAPPING (VERIFY, DON'T ASSUME)
============================

* Read these product management specs in {LFB_PM_DIR} (frontmatter
  description paragraph plus the placement sections are enough):
    ai_description.mdx, ocr.mdx, Transcribe.mdx,
    artifact_placement_policy.mdx, repo_tracking_scheme.mdx
* Confirm the mapping rules from the KNOWLEDGE section above against the
  actual disk: pick 5 sample images under {MIRROR_DIR}, compute their
  expected sidecar paths under {MIRROR_SIDECAR_DIR}, and verify existence.
  Do the same for one repo-internal video against {REPO_SIDECAR_DIR}.
* Count current sidecar coverage: number of .ai_description, .ocr, and
  .transcription files under {MIRROR_SIDECAR_DIR}.
* If a sample is missing, check the legacy .lfbridge/_Mirror/ location
  before concluding it does not exist.

Output to stdout:
============================
STAGE 2 COMPLETE
Mapping verified: N/5 mirror samples, repo sample yes/no
Sidecar counts: ai_description N, ocr N, transcription N
============================

============================
STAGE 3 — SITE LEVEL 2 SWEEP → YAML LEVEL_3 SUPERSET
============================

The YAML's list of level_3 nodes must include ALL of the website's Level 2
sections, except:

  * Photos (the images Level 2 itself — the YAML hierarchy IS its content)
  * Videos (same reasoning — a media Level 2, not a concept)
  * Topics3 (template scaffolding, not a real section — the /Topics3/Photos
    page is unrelated to this hierarchy; do not confuse the two)
  * Any unfiltered / queue / catch-all category EXCEPT Other: we DO include
    one "Other" level_3 in the YAML as the catch-all. Fold other_topics-style
    catch-alls into that single Other node rather than creating several.
  * Non-page files at the docs root (index.mdx, Topics.mdx, image_list.csv,
    video_list.csv, index.html) — these are not sections.

For every remaining site Level 2 (TPUSA, FBI, UVU, Israel, Mic, Timeline,
etc.):

* Check whether a YAML level_3 already covers that concept. Match by _key,
  by title, and by meaning — e.g. existing "TPUSA" covers site TPUSA;
  "The UVU Venue" covers site UVU; "Ballistics and the Gun" covers site
  Gun_Bullet; "Aircraft and Flight Evidence" covers site Planes;
  "CIA and US Intelligence" covers site intelligence / US_Intelligence;
  "Court and Legal Proceedings" covers site court / Legal /
  legal_investigation. Do NOT create a duplicate concept under a second name.
  Record the site-dir-to-level_3 mapping you decide in a comment on the node:
    site_level_2: <dirname>   (add this property to every level_3 node,
    a list if several site dirs map to one node, empty list if the node is
    mirror-only)
* If no existing level_3 covers it, append a new level_3 node: title from the
  section's human-readable name, unique _key (four words max, underscores),
  number_of_images: 0, number_of_images_recursive: 0, images: [],
  site_level_2: [<dirname>].
* Never remove or rename an existing level_3. Grow only. Update properties in
  place when the node already exists.

Output to stdout:
============================
STAGE 3 COMPLETE
Site Level 2s swept: N
Matched to existing level_3: N
New level_3 nodes added: N (list their _keys)
Excluded: Photos, Videos, Topics3, non-page files
Other node present: yes
============================

============================
STAGE 4 — HOME PAGE TABLES OF CONTENTS → MORE LEVEL_3S
============================

The home page {HOME_PAGE} is the site's Level 1 and it carries MORE than one
table of contents — the three-column flex divs under "Biggest Question Marks",
the "## Table of Contents" section, "## Areas of Investigation", the
"Related Areas" and "Related" sections, and the per-thesis link clusters
(Tyler Robinson Not Assassin, Cause of Death, Mossad / Israel Top Suspect,
US Intelligence Assisted, and others). These reflect how the investigation
actually organizes its concepts, and they are likely to surface areas that the
Level 2 directory sweep alone did not.

* Read {HOME_PAGE} fully. Extract every table of contents and every link
  cluster — all of them, not just the first.
* For each linked area/topic in those TOCs, resolve the link target to its
  site section, and check whether a YAML level_3 covers that concept.
* Add a new level_3 for each one not yet covered, using the same rules and
  fields as Stage 3. No dupes — an area already covered by an existing
  level_3 (under any name) is skipped, though you may update that node's
  properties (e.g. append to site_level_2, refine title) if the TOC reveals a
  better human-readable name.
* This stage is expected to ADD items beyond the previous stages — that is
  its purpose. The YAML must end up the most full and complete hierarchy
  possible.

Output to stdout:
============================
STAGE 4 COMPLETE
TOC sections parsed on home page: N
Concepts found: N
Already covered: N
New level_3 nodes added: N (list their _keys)
============================

============================
STAGE 5 — FILESYSTEM LEVEL 3/4 PAGES → YAML LEVEL_4/LEVEL_5 NODES
============================

Apply the increment-by-one mapping rule to the pages inside each site Level 2.

For every site Level 2 that maps to a YAML level_3 (from Stage 3's
site_level_2 property):

* Enumerate its Level 3 pages: overview.md/.mdx plus every other page file
  directly in the directory, plus first-level subdirectory overviews. Use
  {PAGES_CSV} levels as the guide and the filesystem as the check.
* For each site Level 3 page, ensure a YAML level_4 node exists under the
  correct level_3 parent:
    title            the page's title (frontmatter title or first H1)
    _key             unique file-wide, four words max, underscores; prefer
                     the page's page_key from {PAGES_CSV} when it is free
    site_page: <repo-relative file path of the page>
    number_of_images / number_of_images_recursive / images: []
* For each site Level 4 page (one directory deeper), ensure a YAML level_5
  node under the correct level_4 parent, same fields.
* Skip pages that are pure navigation with no evidentiary concept of their
  own only if adding them would create an empty duplicate of their parent;
  when in doubt, include the page.
* Existing mirror-derived level_4/level_5 nodes stay where they are. If a
  site page and an existing mirror node are the same concept, MERGE: keep the
  existing node, add the site_page property to it. No dupes.
* Never remove existing nodes or images. Grow and update only.

Output to stdout:
============================
STAGE 5 COMPLETE
Site Level 3 pages processed: N → level_4 nodes (N new, N merged)
Site Level 4 pages processed: N → level_5 nodes (N new, N merged)
============================

============================
STAGE 6 — PAGE IMAGE SWEEP → IMAGE ENTRIES IN THE YAML
============================

Go through ALL the site's pages and make sure every page that has one or more
images gets those images represented in the YAML hierarchy.

* Scan every page under {DOCS_DIR} for embedded images and videos: markdown
  image syntax, <img> tags, <iframe>/<video> embeds, and static-asset links.
  Resolve each src to the actual file (usually under {SITE_DIR}/internals/
  static/ or {SITE_DIR}/static/).
* For each image found on a page:
    * Compute its sha256. Try to match it back to an original under
      {MIRROR_DIR} — first by sha256 against {INVENTORY_TSV} and the YAML's
      existing entries, then by filename. The mirror original is the
      preferred file_path; if there is no mirror original, use the site
      static file's path.
    * If that sha256 already exists anywhere in the YAML: do NOT add a
      duplicate. Update the existing entry's properties instead — and record
      the page reference by appending the page's repo-relative path to an
      on_site_pages list property on that image entry.
    * If it does not exist yet: add a new image entry under the level_4 (or
      level_5) node that correlates to the page it was found on — per the
      level model, "where those level_5 image entries are parented is on the
      level_4 in the YAML which correlates to the Level 3 page in the file
      system." Fields: cid: "", sha256, file_path, ai_description: "",
      on_site_pages: [<page path>], plus the sidecar path fields (Stage 7
      fills them) and image_page: "" (Stage 8 fills it).
* Videos found on pages get entries too, as `video:` items with the same
  fields (video_list.csv at {DOCS_DIR}/video_list.csv is a starting index;
  the page scan is authoritative).
* Images already embedded ad hoc inside topic pages across the site stay
  where they are on those pages — this hierarchy is the browsable index over
  the corpus, not a relocation of every inline image.

Output to stdout:
============================
STAGE 6 COMPLETE
Pages scanned: N
Images found on pages: N (N matched to mirror originals)
New image entries added: N
Existing entries updated (on_site_pages): N
Video entries added/updated: N
============================

============================
STAGE 7 — SIDECAR FILE-PATH PROPERTIES ON EVERY IMAGE AND VIDEO
============================

For EVERY image and video entry in {HIERARCHY_FILE} (old and new):

* Compute the expected sidecar paths using the mapping learned in Stage 2:
    original under {MIRROR_DIR}       →  {MIRROR_SIDECAR_DIR}/<same relative
                                          path>/<name.ext>.<sidecar>
    original inside {ROOT_DIR}        →  {REPO_SIDECAR_DIR}/<repo-relative
                                          path>/<name.ext>.<sidecar>
    check the legacy .lfbridge/_Mirror/ location as fallback
* Set on each entry:
    ai_description_file   path if the file exists, else ""
    ocr_file              path if the file exists, else ""
    transcription_file    path if the file exists, else ""
* Where the inline ai_description text is empty and an .ai_description
  sidecar exists, fill the inline field with the sidecar's Overview
  paragraph, collapsed to a single paragraph (the readDesc() convention in
  gen_hierarchy.js shows exactly how).
* Do not overwrite a non-empty inline ai_description.

Output to stdout:
============================
STAGE 7 COMPLETE
Entries processed: N
ai_description_file set: N   ocr_file set: N   transcription_file set: N
Inline descriptions filled from sidecars: N
Entries with no sidecars at all: N
============================

============================
STAGE 8 — IMAGE_PAGE: BIND EVERY IMAGE TO ITS LEVEL 5 PAGE
============================

KNOWLEDGE — what an image page is.

Under the images Level 2 ({DOCS_DIR}/Photos) the site publishes one page per
image. That page hosts a single image and nothing else: the image itself, a
title, and prose describing what the image shows and why it matters to the
investigation. We call it the IMAGE PAGE, or the Level 5 page. It is the leaf
of the published hierarchy, the same way an image entry is the leaf of this
YAML.

  Photos                       ← site Level 2 (the images landing page)
    Maps                       ← site Level 3  (a cluster overview page)
      Img_Photo_cf0c99.mdx     ← the IMAGE PAGE — one image, its description

These pages already exist on disk — about 1,100+ of them, generated by
{GENERATOR_DIR}/gen_photos_pages.py from this YAML. This stage does NOT create
them, rename them, or edit them. It READS them and records where each one is,
so the YAML can find its published page later. Reading site pages is allowed;
the no-page-modification hard rule still holds.

THE PROPERTY.

Every image entry gets an `image_page` property whose value is the FULL PATH
FROM ~ to that image's Level 5 page under the images directory:

    image_page: "~/BGit/Bryan_git/charlie-kirk/site/docs/Photos/Maps/Img_Photo_cf0c99.mdx"

Not the URL, not a repo-relative path — the tilde-rooted filesystem path, the
same convention file_path and the sidecar path properties already use. An
entry whose image has no page yet gets image_page: "" (empty string, key still
present).

HOW TO MATCH AN ENTRY TO ITS PAGE.

Each generated image page carries the binding in its frontmatter:

    ck_image_sha256: cf0c994cfd5c6ba50dd08f272f073ceddb0471dcfa7130bf511e874cfa2a5bac
    ck_node_key: Maps

  * Walk every .mdx under {DOCS_DIR}/Photos and index the ones that declare
    ck_image_sha256 — key the index by (ck_image_sha256, ck_node_key).
  * For each image entry in {HIERARCHY_FILE}, look up (its sha256, the _key of
    the node it sits under). That pair is the exact match: it is what makes
    cross-filed images work, since the SAME sha256 legitimately appears under
    several nodes and each of those nodes publishes its own page for it.
  * If the exact pair is not found, fall back to sha256 alone. If that yields
    exactly one page, use it. If it yields several, choose the page whose
    ck_node_key is nearest in the tree (same parent first, then same level_3
    subtree), and leave the others alone.
  * If no page carries that sha256 at all, set image_page: "".
  * Some pages are hand-written or predate the sha256 frontmatter and carry no
    ck_image_sha256. Do not try to guess them by filename. Count them and
    report them; they resolve on a later pass once the page generator restamps
    them.

RULES.

  * image_page is set on EVERY image entry — the existing ones and any added
    by earlier stages. No entry is left without the key.
  * Never invent a path. The file must exist on disk at the moment you write
    the value; verify existence before writing, and write "" if it does not.
  * Never write a page path that lives outside {DOCS_DIR}/Photos. Ad-hoc
    embeds on topic pages elsewhere in the site belong in on_site_pages, not
    here. The two properties answer different questions: on_site_pages is
    "where else does this image appear," image_page is "which page IS this
    image."
  * image_page is an IDENTITY field for sanitization purposes — see the
    OUTPUT SANITIZATION section. It must keep resolving to the real file, so
    any non-ASCII in it is emitted as a visible \uXXXX escape, never replaced.
  * Never delete an existing non-empty image_page in favour of "". If a
    previously recorded page has vanished from disk, report it rather than
    silently clearing it.

Output to stdout:
============================
STAGE 8 COMPLETE
Image pages indexed under Photos: N (N with ck_image_sha256, N without)
Entries with image_page set: N   matched by (sha256,node): N   by sha256 only: N
Entries with image_page "": N (no page exists yet)
Recorded pages now missing from disk: N (listed)
============================

============================
OUTPUT SANITIZATION — NO INVISIBLE UNICODE, EVER (SECURITY RULE)
============================

The emitted {HIERARCHY_FILE} must NEVER contain invisible Unicode characters.
Invisible characters (zero-width spaces, bidi controls, no-break spaces,
word joiners, BOMs, control characters, variation selectors, tag characters)
are a security problem: they can hide content from review, spoof strings,
and smuggle instructions past a human reading the file. Every byte of the
emitted YAML must be visible in a text editor.

The invisible set includes at minimum: U+0000-U+0008, U+000B-U+001F, U+007F-
U+009F, U+00A0, U+00AD, U+034F, U+061C, U+115F, U+1160, U+17B4, U+17B5,
U+180B-U+180E, U+2000-U+200F, U+2028-U+202F (U+202F NARROW NO-BREAK SPACE is
the one macOS puts in screenshot filenames before "AM/PM" — it WILL appear in
the inputs), U+205F-U+206F, U+3000, U+3164, U+FE00-U+FE0F, U+FEFF, U+FFA0,
U+FFF9-U+FFFB, and U+E0000-U+E007F.

Two different treatments, chosen by field kind:

  * PROSE fields (title, ai_description) — sanitize the CONTENT: replace
    space-like invisibles (U+00A0, U+2000-U+200A, U+202F, U+205F, U+3000)
    with a regular space, DELETE zero-width/bidi/control/joiner characters
    outright, then collapse runs of whitespace. Visible non-ASCII (em dashes,
    accented letters) may stay — they are visible and harmless.

  * IDENTITY fields (file_path, ai_description_file, ocr_file,
    transcription_file, image_page, ipfs_url, on_site_pages, also_filed_in,
    site_page, site_level_2) — the value
    must keep matching the real file on disk, so the characters cannot be
    replaced. Instead emit them as visible ASCII escapes inside YAML
    double-quoted scalars (U+202F becomes the six visible characters backslash-u-2-0-2-F, i.e. "\u202F"). The parsed value is unchanged and still resolves the file; the
    file bytes contain nothing invisible. Escape ALL non-ASCII in identity
    fields this way.

MANDATORY validation after every emit: re-scan the written file and hard-fail
if any code point from the invisible set remains anywhere in it. Also
re-parse the YAML and spot-check that an escaped file_path still resolves to
an existing file on disk.

============================
STAGE 9 — COUNTS, NEEDS_SPLIT, INTEGRITY
============================

* Recompute number_of_images (direct) and number_of_images_recursive
  (subtree) on every node. They must be accurate.
* Re-evaluate needs_split on every node: over 12 direct images → true (six
  is the target, twelve the ceiling; over twelve means the node is not one
  concept and gets split one level deeper on a later pass). At or under 12 →
  remove the flag.
* Verify every _key is unique across the whole file.
* Verify no node contains the same sha256 twice. Same sha256 under DIFFERENT
  nodes is legitimate cross-filing — keep it, and keep also_filed_in
  accurate.
* Verify the YAML parses (e.g. python3 -c "import yaml,sys;
  yaml.safe_load(open(sys.argv[1]))" {HIERARCHY_FILE} — or any equivalent).
* Verify every image entry carries the full property set — cid, sha256,
  file_path, ai_description, ai_description_file, ocr_file,
  transcription_file, image_page — with "" standing in for any that has no
  value. No key is ever missing.
* Verify every non-empty image_page resolves to a file that exists on disk
  and lives under {DOCS_DIR}/Photos.
* Run the OUTPUT SANITIZATION validation: scan the emitted file for every
  code point in the invisible set and fail hard if any is found. Confirm at
  least one escaped file_path round-trips: parse the YAML, expanduser the
  path, and check the file exists.

Output to stdout:
============================
STAGE 9 COMPLETE
Counts recomputed: yes
needs_split nodes: N
Duplicate _keys: 0   Duplicate sha256 within a node: 0
YAML parses: yes
============================

============================
STAGE 10 — VERIFY AND REPORT
============================

* Confirm every non-excluded site Level 2 maps to exactly one level_3
  (site_level_2 property present).
* Confirm the Other level_3 exists.
* Confirm every home-page TOC concept resolves to a level_3.
* Confirm every page found with images in Stage 6 has its images reachable in
  the YAML (spot-check 10 pages).
* Confirm no pre-existing node or image entry was removed: the file only
  grows. Diff the node count and image count against Stage 1's index.
* Print a final tree summary: each level_3 _key with its recursive image
  count and child count.

Output to stdout:
============================
STAGE 10 COMPLETE — FINAL REPORT
level_3 nodes: N (was N)   level_4: N (was N)   level_5: N (was N)
Total image entries: N (was N)   video entries: N
Sidecar coverage: ai_description N%, ocr N%, transcription N%
image_page coverage: N% (N of N entries bound to a Level 5 page)
Nothing removed: confirmed
============================

============================
HARD RULES
============================

* {HIERARCHY_FILE} only grows. Never delete a node or an image entry. No
  duplicates — existing items get their properties updated in place.
* This prompt does not create, move, or edit any page under {SITE_DIR}, does
  not touch {SITE_DIR}/sidebars.ts, and does not modify {PAGES_CSV}. The
  YAML is the plan; publishing is a later prompt.
* Do not put Docusaurus pages in {THIS_DIR} and do not put planning notes in
  {SITE_DIR}/docs/Photos/.
* _key uniqueness is file-wide and _keys are the future page_keys — treat
  them like database primary keys. Keys are ASCII-only by construction.
* {HIERARCHY_FILE} must never contain invisible Unicode characters — see the
  OUTPUT SANITIZATION section. Prose is cleaned; identity fields (paths,
  URLs) are emitted with visible \uXXXX escapes; every emit is followed by
  the invisible-character validation scan. This is a security rule, not a
  style rule.
* Clusters are concept clusters, arbitrated by {CK_FILE}. The folder
  proposes, the description decides, {CK_FILE} arbitrates.
* When later prompts publish from this YAML, all public output follows the
  repo defamation rules (attribution language, no stating a living person
  committed a crime, accusations cropped out of images). Raw claims stay
  private in this planning layer or in {CK_FILE}.

============================
BACKGROUND — ORIGINAL DIRECTIVE, KNOWLEDGE PRESERVED
============================

This section preserves the full intent of the directive this prompt was built
from, so no knowledge is lost even where a stage above already encodes it.

* Growing and improving the output YAML file ({HIERARCHY_FILE}) is the goal.
  The prompt has multiple stages and is created to run later.
* "Level 2" refers to the fact that we will eventually put an image-hosted
  page for every image under a Level 2 directory called images. The Level 2
  IS that images directory. Today that is the Photos section.
* We create Level 3s under that images Level 2, and the YAML's level_3 list
  will definitely be a superset that includes the list of the website's
  Level 2s — except images and videos and any unfiltered or catch-all
  category — plus an "Other" entry included as a level_3. The website's
  Level 2s include TPUSA, FBI, UVU, and many more; one stage reads those
  Level 2s and makes sure they are all present as level_3s in the YAML.
* We then take every other Level 2 (outside the images Level 2) and its
  Level 3 pages, and make a level_4 in the YAML for each one, parented
  hierarchically under the appropriate parent.
* We create a level_5 per image: if some Level 3 content page has an image —
  one or more images on the page — we create level_5 YAML for each of those
  images. Where those level_5s are parented is on the level_4 in the YAML
  which correlates to the Level 3 page in the file system.
* We are effectively taking all the Level 2s, Level 3s, and Level 4s in the
  file system outside this YAML and reproducing the hierarchy in the YAML
  with the levels incremented by one: filesystem Level 2 → YAML level_3,
  filesystem Level 3 → YAML level_4, filesystem Level 4 → YAML level_5.
* A further stage goes through all the pages and makes sure that every page
  that has one or more images gets those added to the YAML hierarchy. No
  duplicates — it does not add them if they already exist, but it DOES
  update their YAML properties.
* Learn from the existing YAML file — its structure and conventions carry
  forward.
* These directories often hold the OCR text files, the transcription text
  files, and the AI-description text files:
    ~/BGit/act3/act3_large_files_bridge/
    ~/BGit/Bryan_git/personal_large_files_bridge/
  We want YAML properties for all of those: each image or video entry gets a
  property that is a file path to the sidecar file that correlates to it.
* By reading the product management specification files and the code in
  ~/BGit/Bryan_git/LargeFileBridge/ you learn how we map between the original
  file paths and the mirroring file system in the other place where the
  sidecars are stored. Learn that pattern and fill in those YAML properties.
* The YAML must be built into the most full and complete hierarchy possible.
  Look at the home page and its table of contents — there might be more than
  one table of contents there — and make sure all of those become level_3s
  in the YAML hierarchy too. That is likely to add more items than are found
  in the earlier stages. Never create dupes, but always look for more that
  can be added.
* The end goal: when we create our list-of-images page (the top level), it
  will be mostly a table of contents — a table with links into the images
  directory's Level 3 pages, which come from this YAML file's level_3s.
* There is a property called image_page. These are the pages under the images
  Level 2 directory — the Level 5 pages that each host one image and carry the
  description of it. We add the full path from ~ to that Level 5 page as the
  image_page property on the image entry, so the YAML can find the published
  page for any image later. All YAML properties are kept updated on every
  image entry so everything is findable later — a property with no value is
  written as "" rather than dropped.
