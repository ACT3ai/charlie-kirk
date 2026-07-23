ROOT_DIR dir is ~/BGit/Bryan_git/charlie-kirk

THIS_DIR dir is {ROOT_DIR}/videos_planning
VIDEOS_DIR dir is {ROOT_DIR}/videos
HIERARCHY_FILE is file {VIDEOS_DIR}/videos.yaml
  Created 2026-07-23 as a copy of {ROOT_DIR}/images/images.yaml with only the
  SCHEMA converted to videos. The DATA it carries is still the inherited image
  corpus and is known-stale. Replacing that data with the real video corpus is
  what THIS prompt is for.
VIDEO_MANIFEST is file {VIDEOS_DIR}/manifest.yaml
VIDEO_INDEX_MD is file {VIDEOS_DIR}/videos.md
IPFS_DIR dir is {ROOT_DIR}/IPFS
GENERATOR_DIR dir is {THIS_DIR}/generator
INVENTORY_TSV is file {GENERATOR_DIR}/inventory.tsv

SITE_DIR dir is {ROOT_DIR}/site
DOCS_DIR dir is {SITE_DIR}/docs
HOME_PAGE is file {DOCS_DIR}/index.mdx
VIDEOS_L2_DIR dir is {DOCS_DIR}/Videos
VIDEOS_L2_PAGE is file {VIDEOS_L2_DIR}/overview.mdx
VIDEO_LIST_CSV is file {DOCS_DIR}/video_list.csv
PAGES_CSV is file {ROOT_DIR}/pages.csv
CK_FILE is file {ROOT_DIR}/Charlie_Kirk.txt
CHARTER_FILE is file {THIS_DIR}/CLAUDE.md
EXCLUDE_FILE is file {THIS_DIR}/exclude_videos.txt

MIRROR_DIR dir is ~/_Mirror/Politics/Charlie_Kirk_Mi
MIRROR_SIDECAR_DIR dir is ~/BGit/Bryan_git/personal_large_files_bridge/_Mirror/Politics/Charlie_Kirk_Mi
REPO_SIDECAR_DIR dir is {ROOT_DIR}/.lfbridge

LFB_DIR dir is ~/BGit/Bryan_git/LargeFileBridge
LFB_PM_DIR dir is {LFB_DIR}/pm
COMPANY_BRIDGE_DIR dir is ~/BGit/act3/act3_large_files_bridge
PERSONAL_BRIDGE_DIR dir is ~/BGit/Bryan_git/personal_large_files_bridge

IMAGE_PLANNING_DIR dir is {ROOT_DIR}/image_planning

============================
GOAL
============================

Grow and improve {HIERARCHY_FILE} — the video evidence hierarchy YAML — so it
becomes the most full and complete hierarchy possible over the investigation's
video corpus. This prompt runs in multiple stages. Each stage adds to the YAML
or enriches it. Nothing is ever deleted from it. No duplicates are ever created
— when an item already exists, its YAML properties are updated in place instead.

The end state this YAML is building toward: the site will eventually host a
video page for every video, all living under one Level 2 directory called
videos ({VIDEOS_L2_PAGE}). When we later create the list-of-videos page — the
top level of the videos area — that page will be mostly a table of contents: a
table with links into the videos directory's Level 3 pages, and those Level 3
pages come directly from the level_3 nodes of this YAML. This prompt builds the
YAML only. It does NOT create or modify any Docusaurus page, and it does NOT
touch sidebars.ts or {PAGES_CSV}. Page generation is a later, separate prompt.

Convergence priority order (if context runs short, complete in this order):
  1. Stage 0 — replace the inherited image data with the real video corpus
  2. Stage 3 — CID and pin status on every video (Stage 8 depends on it)
  3. Stage 4 — site Level 2 sweep into YAML level_3 superset
  4. Stage 6 — filesystem Level 3/4 pages into YAML level_4/level_5 nodes
  5. Stage 7 — page video sweep into YAML video entries
  6. Stage 8 — on_pages: every other repo page that shows each video
  7. Stage 9 — sidecar file-path properties on every video
  8. Stage 10 — video_page path on every video entry
  9. Stage 5 — home page tables of contents into more level_3s
 10. Stage 11 — counts and needs_split
 11. Stage 12 — verify

============================
KNOWLEDGE — THE LEVEL MODEL (READ THIS FIRST)
============================

Two different level systems are in play. Do not confuse them.

The SITE (filesystem) levels:
  * Level 1 — the site home page ({HOME_PAGE}).
  * Level 2 — the top-level sections: the directories directly under
    {DOCS_DIR}. Examples: TPUSA, FBI, UVU, Israel, Mic, Planes, Timeline.
    Videos and Photos (images) are also Level 2s.
  * Level 3 — the pages inside a Level 2 directory (overview.mdx plus the
    individual analysis pages, and first-level subdirectory overviews).
  * Level 4 — pages one directory deeper.

The YAML ({HIERARCHY_FILE}) levels:
  * There is no level_1 and no level_2 inside the YAML. Level 1 is the site
    home and Level 2 is the videos landing page itself, so the YAML's cluster
    tree begins at level_3.
  * "Level two refers to the videos directory" — the entire YAML tree hangs
    under the videos Level 2 page. Every YAML level_3 becomes a child page of
    that videos Level 2.

THE CORE MAPPING RULE — increment by one:
  We are effectively taking all the Level 2s, Level 3s, and Level 4s that exist
  in the site filesystem outside this YAML and reproducing that same hierarchy
  inside the YAML, but with every level number incremented by one:

    site filesystem Level 2  →  YAML level_3
    site filesystem Level 3  →  YAML level_4
    site filesystem Level 4  →  YAML level_5

  So the YAML's level_3 list is a SUPERSET that includes the site's list of
  Level 2s (except videos, images, and unfiltered/queue categories — see
  Stage 4), the YAML's level_4 nodes correlate to the site's Level 3 pages
  parented hierarchically under their appropriate level_3 parent, and each
  video found on a site Level 3 page becomes a level_5 entry parented on the
  level_4 node that correlates to that filesystem Level 3 page.

  Additionally, video clusters that came from the corpus itself ({VIDEOS_DIR},
  {IPFS_DIR}/videos, {MIRROR_DIR}) already exist in the YAML and stay — the
  site-derived nodes merge INTO this tree, they do not replace it.

============================
KNOWLEDGE — THE YAML FILE TODAY
============================

{HIERARCHY_FILE} exists (about 30,000 lines, ~2.6MB). Read it and learn from it
before changing anything. Its current shape:

  * Root key `level_3:` is an array. Each item is itself keyed `level_3:`.
    A level_3 node may contain a `level_4:` array; a level_4 may contain a
    `level_5:` array, and so on down to level_7 today. Same shape at every
    depth.
  * Cluster node fields: title (human readable, spaces allowed), _key
    (underscores, four words or less, unique across the WHOLE file — this is
    the future page_key in {PAGES_CSV}), number_of_videos (direct count),
    number_of_videos_recursive (subtree count), optional needs_split: true
    (node is over the 12-video ceiling; split on a later pass), site_level_2
    (list of site docs dirs this cluster covers), site_page (the page a node
    mirrors), videos (array of video items).
  * Video item fields: cid (the IPFS CID — spoken as "SID", it means the CID;
    for video this is the PRIMARY identity because the site plays video off
    public gateways), ipfs_pinned (true/false — whether the local IPFS node
    pins those blocks; a CID exists whether or not it is pinned), sha256
    (content identity of the local file when there is one), file_path (path to
    the original file — {VIDEOS_DIR} for X-sourced video, {MIRROR_DIR} for
    older captures), ai_description (inline prose — what is SEEN),
    ai_description_file / ocr_file / transcription_file (paths to the Large
    File Bridge sidecars, "" when the sidecar does not exist — see Stage 9;
    transcription is the load-bearing one for video), video_page (path to the
    published Level 5 page that hosts this one video, "" when no page exists
    yet — see Stage 10), on_pages (list of every OTHER page in the repo that
    shows this video — see Stage 8), optional ipfs_url (for entries that exist
    only as an IPFS embed with no local file), optional also_filed_in (list of
    other concept dirs the same content legitimately lives in — cross-filing is
    deliberate and kept).

  * The full property set on a video item, in emission order:

      videos:
        - video:
            cid: "QmThpacy26yaTjsRcPSVegJQTNzRRSyXt23tKWjPZcyn3s"
            ipfs_pinned: true
            sha256: ""
            file_path: "~/BGit/Bryan_git/charlie-kirk/videos/2067372027623715212.mp4"
            ai_description: "A vertical phone capture of a studio segment in which ..."
            ai_description_file: "~/BGit/Bryan_git/charlie-kirk/.lfbridge/videos/2067372027623715212.mp4.ai_description"
            ocr_file: ""
            transcription_file: "~/BGit/Bryan_git/charlie-kirk/.lfbridge/videos/2067372027623715212.mp4.transcription"
            video_page: "~/BGit/Bryan_git/charlie-kirk/site/docs/Videos/Mic_Thesis/Vid_Candace_Mic_2067372.mdx"
            on_pages:
              - page: "~/BGit/Bryan_git/charlie-kirk/site/docs/Mic/overview.mdx"
              - page: "~/BGit/Bryan_git/charlie-kirk/site/docs/Killer/israel-mossad.mdx"

    Every video entry carries every one of these properties. A property that
    has no value is emitted as the empty string "" — never omitted, never
    null. Absence of the key would make later passes unable to tell "not
    looked up yet" from "looked up, does not exist." The two exceptions to the
    ""-for-empty rule are the two typed properties: on_pages is a list and
    emits [] when empty, and ipfs_pinned is a boolean and emits false when the
    local node does not pin the CID.

  * THE DATA IS STALE AND YOU MUST NOT TRUST IT. The file was produced by
    copying images/images.yaml and converting the keys. Every one of its ~1,740
    entries and ~1,365 nodes still carries image data: file_paths pointing at
    .jpg/.jpeg/.png files under {MIRROR_DIR}, sha256 and cid values computed
    over image bytes, ai_description prose that literally begins "This image
    shows...", on_pages bindings harvested for images, and counts that count
    images. Every video_page has already been blanked to "". Stage 0 is what
    fixes this. Until Stage 0 has run, treat the tree's SHAPE as a useful
    starting proposal and its CONTENTS as placeholder.

  * Prior art: {IMAGE_PLANNING_DIR}/generator built the images equivalent —
    gen_hierarchy.js from an {INVENTORY_TSV} (sha256, dir, filename, orig_path,
    has_desc per item) plus a clusters.json merge map, and bind_image_pages.py
    which round-trips the YAML byte-for-byte. Read them to understand how
    dedupe was done (same identity in the SAME dir collapses; same identity in
    DIFFERENT concept dirs is deliberate and recorded as also_filed_in), how
    unique _keys were minted, and how to edit a large emitted YAML without
    reformatting the whole file. Reuse those conventions. Never edit anything
    under {IMAGE_PLANNING_DIR}.

Cluster sizing rules (from the charter, {CHARTER_FILE}):
  * Six videos per page is the target. Twelve is the ceiling. Over twelve
    means the node is not one concept — mark needs_split: true and split one
    level deeper on a later pass. A page carrying many IPFS video embeds is
    heavy, so prefer the low end and split earlier than the image hierarchy
    would.
  * Clusters are concept clusters. The question is always "what does this
    footage show or claim," never "when was it downloaded" or "who posted it."
  * Titles may use spaces and full words. Keys use underscores, four words or
    less, unique file-wide.

============================
KNOWLEDGE — SIDECAR FILES (TRANSCRIPTION, AI DESCRIPTION, OCR) AND THE PATH MAPPING
============================

Large File Bridge (the web app at {LFB_DIR}; understand it by reading the
product management specification files in {LFB_PM_DIR} and the code) produces
three sidecar text files per media file. They answer three different questions:

  * .transcription   — "what was SAID" (verbatim speech). FOR VIDEO THIS IS THE
                       PRIMARY SIDECAR. It is what the clustering reasons over,
                       because a video's claim is usually spoken, not shown.
  * .ai_description  — "what is SEEN" (a vision model's hyper-detailed prose
                       about the footage)
  * .ocr             — "what does it SAY on screen" (chyrons, slates, captions
                       burned into the frame). Rare on video; when present it is
                       usually a screen-recorded post rather than filmed footage.

Naming rule: the sidecar keeps the media file's FULL filename (original
extension kept) and APPENDS the second-level extension:
  Blue_Side.mp4  →  Blue_Side.mp4.transcription
  Blue_Side.mp4  →  Blue_Side.mp4.ai_description
  Blue_Side.mp4  →  Blue_Side.mp4.ocr

Placement rule — where the sidecar lives depends on whether the original is
inside a working git repo (this is the mapping pattern; the authoritative spec
is {LFB_PM_DIR}/artifact_placement_policy.mdx section 0, with
Transcribe.mdx, ai_description.mdx, ocr.mdx, and repo_tracking_scheme.mdx):

  * Original INSIDE a working git repo — the sidecar is path-mirrored under
    that repo's committed .lfbridge/ tracking directory. This is the NORMAL
    case for this pipeline, because the video corpus lives in the repo:
      {VIDEOS_DIR}/X.mp4
        →  {REPO_SIDECAR_DIR}/videos/X.mp4.transcription
      {IPFS_DIR}/videos/X.MP4
        →  {REPO_SIDECAR_DIR}/IPFS/videos/X.MP4.transcription
      {REPO_SIDECAR_DIR} currently holds videos/, IPFS/videos/, images/,
      cover_image/, and site/ sidecars.

  * Original OUTSIDE any git repo (the mirror) — there is NO .lfbridge/
    segment. The dedicated bridge repo (an "SDL": a personal or company file
    repo that exists only to hold these files) IS the tracking area, and the
    mirror hangs directly off its root:
      {MIRROR_DIR}/Teachers_Lounge/X.mp4
        →  {MIRROR_SIDECAR_DIR}/Teachers_Lounge/X.mp4.transcription
      Personal SDL: {PERSONAL_BRIDGE_DIR}
      Company SDL:  {COMPANY_BRIDGE_DIR}

  * Older files may still sit under a .lfbridge/_Mirror/ path until Large File
    Bridge migrates them. Check both locations before concluding a sidecar is
    missing.

Coverage snapshot at the time this prompt was written (re-count at run time —
these grow constantly): under {REPO_SIDECAR_DIR}/videos there were ~74
.transcription files, ~44 .ai_description files, and ~2 .ocr files against a
46-video corpus. Transcription coverage is good and it is the richest input this
pipeline has. Mirror-side video coverage is much thinner; count it at run time.

WHAT THIS MEANS FOR THE YAML: every video entry in {HIERARCHY_FILE} gets YAML
properties holding the FILE PATH to each sidecar that exists for it. This is
required — the sidecars are how later passes search, cluster, caption, and
publish. The properties are:

  transcription_file    path to the .transcription sidecar, or "" if none
  ai_description_file   path to the .ai_description sidecar, or "" if none
  ocr_file              path to the .ocr sidecar, or "" if none

The existing inline ai_description field stays as the short prose text; the
*_file fields point at the full sidecar files on disk.

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
STAGE 0 — REPLACE THE INHERITED IMAGE DATA WITH THE REAL VIDEO CORPUS
============================

This stage exists because {HIERARCHY_FILE} was created by copying
images/images.yaml and converting the keys. Every entry in it today describes an
image. Until this stage runs, every later stage would be enriching the wrong
corpus.

This is the ONE stage that is allowed to remove entries, and it may remove only
inherited image entries — never a video entry, never a node.

BUILD THE REAL CORPUS INDEX FIRST.

* {VIDEO_MANIFEST} is the richest machine-readable source. Each record has
  filename, ipfs_cid, ipfs_gateway_url, source_url, source_author, description,
  added_date, pinned. Parse it in full. It seeds cid, file_path, ipfs_pinned,
  and provenance for the X-sourced corpus in one read.
* {VIDEO_INDEX_MD} is the same corpus as a markdown table. Use it to cross-check
  the manifest and to catch anything the manifest missed.
* {IPFS_DIR}/ipfs.txt carries the pull-and-pin commands and the CIDs for the
  larger forensic originals under {IPFS_DIR}/videos.
* Walk {VIDEOS_DIR} for media files. Note the .gitignore there: *.mp4, *.mp3,
  *.mkv, *.avi, *.mov, *.wav, *.webm are NOT committed. On a fresh clone the
  bytes are absent and only the metadata files exist — the pipeline must work
  from the manifest alone in that case, and must not conclude a video does not
  exist merely because the file is not on this machine. Record what is present
  locally versus known-from-manifest, and say which in the report.
* Walk {MIRROR_DIR} for video files (.mp4, .mov, .m4v, .webm, .avi, .mkv).
* Walk {REPO_SIDECAR_DIR}/videos and {REPO_SIDECAR_DIR}/IPFS/videos and
  {MIRROR_SIDECAR_DIR} for .transcription sidecars whose base name ends in a
  video extension — a sidecar proves a video existed even when the media file
  is gitignored or has since moved.
* {VIDEO_LIST_CSV} (12 rows) adds YouTube-hosted material with title,
  description, date, and location. YouTube-only rows have no CID and no local
  file; carry them as entries with cid "" and ipfs_url "" and record the
  YouTube URL in on_pages-adjacent prose, not as a fake CID.

THEN RECONCILE THE YAML AGAINST IT.

* For every existing entry in {HIERARCHY_FILE}, decide what it is:
    * A REAL VIDEO — file_path (or ipfs_url, or cid) resolves to something in
      the corpus index above. Keep it. Update its properties in place from the
      corpus index: correct cid, ipfs_pinned, sha256, file_path.
    * An INHERITED IMAGE — file_path ends in an image extension, or its cid
      resolves to image bytes, or its ai_description describes a still. Remove
      the entry. Count it. These are the ~1,700 placeholders and removing them
      is the entire point of this stage.
    * UNDECIDABLE — no file on this machine and no manifest match. Do NOT
      remove it. Leave it, set a comment on it, and list it in the report for a
      human to arbitrate.
* For every video in the corpus index that has NO entry in the YAML, add one,
  parented on the level_3/level_4 node whose concept it belongs to (use the
  manifest description, the transcription, and {CK_FILE} to decide — see
  the clustering rules in {CHARTER_FILE}).
* NODES ARE KEPT EVEN WHEN THEY EMPTY OUT. A level_3 or level_4 that held only
  inherited images ends this stage with videos: [] and counts of 0. That is
  correct — the node still mirrors a real site section and Stage 7 may well fill
  it. Do not delete nodes.
* Every entry that survives or is added gets video_page: "" unless Stage 10 has
  already bound a page that still exists on disk.

Do this with a script, not by hand. Reuse the round-trip emitter from
{IMAGE_PLANNING_DIR}/generator/bind_image_pages.py so the untouched parts of the
file come back byte-for-byte identical and the diff shows only real changes.

Output to stdout:
============================
STAGE 0 COMPLETE
Corpus index: N from manifest, N from {VIDEOS_DIR} on disk, N from {IPFS_DIR},
              N from mirror, N from transcription sidecars, N from video_list.csv
YAML entries before: N
Inherited image entries removed: N
Real video entries kept and refreshed: N
Undecidable entries left in place: N (listed)
New video entries added: N
Nodes emptied to zero (kept): N     Nodes removed: 0
YAML entries after: N
============================

============================
STAGE 1 — SETUP AND READ
============================

* Read {CHARTER_FILE} — the videos_planning charter. It is the authority on
  the audience model, the level model, the YAML schema, and the hard rules.
* Read {HIERARCHY_FILE} fully. Build an in-memory index of: every _key, every
  node path, every cid and sha256 and the node(s) it lives under.
* Read {VIDEO_MANIFEST}, {VIDEO_INDEX_MD}, {IPFS_DIR}/ipfs.txt, and
  {VIDEO_LIST_CSV}.
* Read {IMAGE_PLANNING_DIR}/generator/gen_hierarchy.js and
  bind_image_pages.py — the prior-art conventions. Read only; never edit.
* Read {PAGES_CSV}.
* Enumerate {DOCS_DIR} top-level directories (the site Level 2s).
* Reference {CK_FILE} as needed throughout — it is the source of truth for
  what the investigation's concepts actually are. The hierarchy must mirror
  the investigation's real concept structure, not an arbitrary video-library
  structure. Do not read all 400K+ lines up front; consult sections when a
  clustering or parenting decision needs arbitration.

Output to stdout:
============================
STAGE 1 COMPLETE
YAML nodes indexed: N level_3 / N level_4 / N level_5+
Videos indexed: N unique cid / N unique sha256
Manifest records: N     Site Level 2 dirs found: N     pages.csv rows: N
============================

============================
STAGE 2 — LEARN THE SIDECAR MAPPING (VERIFY, DON'T ASSUME)
============================

* Read these product management specs in {LFB_PM_DIR} (frontmatter
  description paragraph plus the placement sections are enough):
    Transcribe.mdx, ai_description.mdx, ocr.mdx,
    artifact_placement_policy.mdx, repo_tracking_scheme.mdx
* Confirm the mapping rules from the KNOWLEDGE section above against the
  actual disk: pick 5 sample videos under {VIDEOS_DIR}, compute their expected
  sidecar paths under {REPO_SIDECAR_DIR}/videos, and verify existence. Do the
  same for one {IPFS_DIR}/videos original and one mirror-side video against
  {MIRROR_SIDECAR_DIR}.
* Count current sidecar coverage: number of .transcription, .ai_description,
  and .ocr files under {REPO_SIDECAR_DIR}/videos,
  {REPO_SIDECAR_DIR}/IPFS/videos, and {MIRROR_SIDECAR_DIR}.
* If a sample is missing, check the legacy .lfbridge/_Mirror/ location
  before concluding it does not exist.

Output to stdout:
============================
STAGE 2 COMPLETE
Mapping verified: N/5 repo samples, IPFS sample yes/no, mirror sample yes/no
Sidecar counts: transcription N, ai_description N, ocr N
============================

============================
STAGE 3 — CID: EVERY VIDEO GETS ITS IPFS CID AND PIN STATUS
============================

This stage runs BEFORE the page sweeps on purpose. Site pages embed video
almost exclusively as an IPFS gateway URL (https://ipfs.io/ipfs/<CID>,
https://<CID>.ipfs.dweb.link/...). The later on_pages sweep (Stage 8) has to
recognise a video by its CID, and the page generator needs the CID to build the
player at all. So the CID column has to be populated first, or every embed on
the site is unmatchable and no page can play anything.

For video the CID is not merely an identifier — it is the DELIVERY MECHANISM.
An image can fall back to a static copy in the repo; a video cannot, because the
bytes are gitignored and GitHub Pages is not a video host. No CID means no
playable page.

KNOWLEDGE — how a CID is obtained.

A CID is a content address. It is COMPUTED from the file's bytes — it does not
require the network, a daemon, or the file ever having been published. So
every video with a local file on disk can always get a CID, whether or not it
is pinned anywhere:

    ipfs add -n -Q "<file>"          # compute only, no add, default settings

  -n / --only-hash  computes the CID without writing the block to the node
  -Q / --quiet      prints just the CID

USE THE DEFAULT CID VERSION — CIDv0, the base58 "Qm..." form. That is what
{VIDEO_MANIFEST} records, what {IPFS_DIR}/ipfs.txt pins, and what the site
already embeds. Passing --cid-version=1 produces a DIFFERENT string
(bafkrei.../bafybei...) for the same bytes, because v1 also switches the leaf
codec — it would not match a single URL on the site and Stage 8 would resolve
nothing. If a v1 form is needed for a dweb.link subdomain URL, convert at use
time with `ipfs cid base32 <cid>`; do not store it.

Pinning is a SEPARATE question from having a CID. Pinned means "this node
holds the blocks and rebroadcasts them so a public gateway can serve it."
Check it against the local node:

    ipfs pin ls --type=all <cid>       # exit 0 and prints the cid = pinned
    ipfs block stat <cid>              # blocks present locally

Chunking settings change the CID, so ALWAYS use the same flags on every run
(-n -Q, default chunker, default CIDv0). A CID computed with different flags
will not match the one in a gateway URL.

WHAT TO DO.

* Seed from {VIDEO_MANIFEST} first — it already records ipfs_cid and pinned for
  the X-sourced corpus, and that is authoritative for those files. Then seed
  from {IPFS_DIR}/ipfs.txt for the forensic originals.
* For every video entry with a file_path pointing at a file that exists on
  disk and no CID yet:
    * Compute the CID with the flags above. Write it to the entry's `cid`
      property. This is unconditional — a CID is always obtainable for a local
      file, so an entry with a readable file_path must never be left with
      cid: "".
    * Check pin status against the local IPFS node and record it:
        ipfs_pinned: true      the local node pins it (it is being served)
        ipfs_pinned: false     CID computed, but the node does not pin it
    * Do NOT pin anything in this stage. Pinning publishes content to the
      public IPFS network and it is irreversible in practice — a CID, once
      announced, can be fetched and cached by anyone. Some material in this
      corpus must never be published (see {EXCLUDE_FILE}). This stage RECORDS
      state; it does not change what is public. If a run wants to pin the
      publishable set, that is a separate, explicitly-approved job that must
      first filter out every entry listed in {EXCLUDE_FILE}.
* For entries with NO local file (ipfs_url-only entries harvested from site
  embeds, and manifest records on a fresh clone), the CID is already known —
  parse it out of the URL or take it from the manifest. Set ipfs_pinned by
  asking the local node; if the node does not have it, false.
* For entries whose file_path points at a file that no longer exists on disk
  AND that have no manifest CID: leave cid: "" and report the entry. Never
  invent a CID.
* Also mirror the finding the other way: build a CID -> entry index in memory
  and hold it for Stage 8, which needs to resolve an IPFS URL on a page back
  to the video entry it belongs to.
* Never overwrite a non-empty cid with "". If a recorded CID no longer matches
  the recomputed one, that means the file's bytes changed — report the
  mismatch, keep the recomputed value, and note the old one.

Report the unpinned set prominently. Every unpinned CID is a video page that
will render a dead player for visitors even though it plays perfectly on this
machine.

Output to stdout:
============================
STAGE 3 COMPLETE
Entries seeded from manifest: N   from ipfs.txt: N
Entries with local file: N   CID computed: N   CID already present + matching: N
CID mismatches (bytes changed): N (listed)
Pinned on local node: N   NOT pinned: N (listed — these publish as dead players)
ipfs_url-only entries with CID parsed from URL: N
Entries left cid "" (no file, no manifest record): N (listed)
Nothing pinned by this stage: confirmed
============================

============================
STAGE 4 — SITE LEVEL 2 SWEEP → YAML LEVEL_3 SUPERSET
============================

The YAML's list of level_3 nodes must include ALL of the website's Level 2
sections, except:

  * Videos (the videos Level 2 itself — the YAML hierarchy IS its content)
  * Photos (same reasoning — a media Level 2, not a concept; it is the images
    pipeline's territory)
  * Topics3 (template scaffolding, not a real section — the /Topics3/Videos
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
  Record the site-dir-to-level_3 mapping you decide on the node:
    site_level_2: <dirname>   (this property is on every level_3 node,
    a list if several site dirs map to one node, empty list if the node is
    corpus-only)
* If no existing level_3 covers it, append a new level_3 node: title from the
  section's human-readable name, unique _key (four words max, underscores),
  number_of_videos: 0, number_of_videos_recursive: 0, videos: [],
  site_level_2: [<dirname>].
* Never remove or rename an existing level_3. Grow only. Update properties in
  place when the node already exists.

Output to stdout:
============================
STAGE 4 COMPLETE
Site Level 2s swept: N
Matched to existing level_3: N
New level_3 nodes added: N (list their _keys)
Excluded: Videos, Photos, Topics3, non-page files
Other node present: yes
============================

============================
STAGE 5 — HOME PAGE TABLES OF CONTENTS → MORE LEVEL_3S
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
  fields as Stage 4. No dupes — an area already covered by an existing
  level_3 (under any name) is skipped, though you may update that node's
  properties (e.g. append to site_level_2, refine title) if the TOC reveals a
  better human-readable name.
* This stage is expected to ADD items beyond the previous stages — that is
  its purpose. The YAML must end up the most full and complete hierarchy
  possible.

Output to stdout:
============================
STAGE 5 COMPLETE
TOC sections parsed on home page: N
Concepts found: N
Already covered: N
New level_3 nodes added: N (list their _keys)
============================

============================
STAGE 6 — FILESYSTEM LEVEL 3/4 PAGES → YAML LEVEL_4/LEVEL_5 NODES
============================

Apply the increment-by-one mapping rule to the pages inside each site Level 2.

For every site Level 2 that maps to a YAML level_3 (from Stage 4's
site_level_2 property):

* Enumerate its Level 3 pages: overview.mdx plus every other page file
  directly in the directory, plus first-level subdirectory overviews. Use
  {PAGES_CSV} levels as the guide and the filesystem as the check.
* For each site Level 3 page, ensure a YAML level_4 node exists under the
  correct level_3 parent:
    title            the page's title (frontmatter title or first H1)
    _key             unique file-wide, four words max, underscores; prefer
                     the page's page_key from {PAGES_CSV} when it is free
    site_page: <repo-relative file path of the page>
    number_of_videos / number_of_videos_recursive / videos: []
* For each site Level 4 page (one directory deeper), ensure a YAML level_5
  node under the correct level_4 parent, same fields.
* Skip pages that are pure navigation with no evidentiary concept of their
  own only if adding them would create an empty duplicate of their parent;
  when in doubt, include the page.
* Existing corpus-derived level_4/level_5 nodes stay where they are. If a
  site page and an existing corpus node are the same concept, MERGE: keep the
  existing node, add the site_page property to it. No dupes.
* Never remove existing nodes or video entries. Grow and update only.

Output to stdout:
============================
STAGE 6 COMPLETE
Site Level 3 pages processed: N → level_4 nodes (N new, N merged)
Site Level 4 pages processed: N → level_5 nodes (N new, N merged)
============================

============================
STAGE 7 — PAGE VIDEO SWEEP → VIDEO ENTRIES IN THE YAML
============================

Go through ALL the site's pages and make sure every page that has one or more
videos gets those videos represented in the YAML hierarchy.

* Scan every page under {DOCS_DIR} for embedded video: <video> elements,
  <iframe> embeds (YouTube, Rumble, Odysee, X), IPFS gateway URLs pointing at
  video, markdown links to media files, and poster attributes. Resolve each
  src to what it actually is.
* For each video found on a page:
    * Take its CID from the URL when it is an IPFS embed — that is the exact
      identity. Otherwise resolve to a local file and compute sha256. Try to
      match it back to an original under {VIDEOS_DIR}, {IPFS_DIR}/videos, or
      {MIRROR_DIR} — first by cid against {VIDEO_MANIFEST} and the YAML's
      existing entries, then by sha256, then by filename.
    * If that identity already exists anywhere in the YAML: do NOT add a
      duplicate. Update the existing entry's properties instead — and record
      the page reference by appending the page's tilde-rooted path to the
      on_pages list on that video entry (see Stage 8 for its shape).
    * If it does not exist yet: add a new video entry under the level_4 (or
      level_5) node that correlates to the page it was found on — per the
      level model, "where those level_5 video entries are parented is on the
      level_4 in the YAML which correlates to the Level 3 page in the file
      system." Fields: cid, ipfs_pinned, sha256, file_path, ai_description: "",
      on_pages: [{page: <tilde-rooted page path>}], the sidecar path fields
      (Stage 9 fills them) and video_page: "" (Stage 10 fills it).
* THIRD-PARTY HOSTED VIDEO (YouTube, Rumble, X) is recorded as an entry with
  cid "" and no local file. It is real evidence and it belongs in the
  hierarchy, but it cannot be served from IPFS and its page will carry an
  external embed rather than our player. Mark it clearly so the page generator
  knows which kind it is. {VIDEO_LIST_CSV} is the starting index for these;
  the page scan is authoritative.
* Videos already embedded ad hoc inside topic pages across the site stay
  where they are on those pages — this hierarchy is the browsable index over
  the corpus, not a relocation of every inline embed.

Output to stdout:
============================
STAGE 7 COMPLETE
Pages scanned: N
Videos found on pages: N (N matched to corpus originals)
IPFS-hosted: N   third-party hosted (YouTube/Rumble/X): N
New video entries added: N
Existing entries updated (on_pages): N
============================

============================
STAGE 8 — ON_PAGES: WHERE ELSE IN THE REPO EACH VIDEO IS SHOWN
============================

KNOWLEDGE — what on_pages answers.

Two properties record two different relationships, and they must not be
confused:

  video_page  "which page IS this video" — the one Level 5 page under
              {VIDEOS_L2_DIR} that exists to host this single video. Set in
              Stage 10. Exactly one, or "".
  on_pages    "where ELSE is this video shown" — every OTHER page anywhere in
              the repo that embeds it. Zero to many. Set here.

on_pages covers any page hosted on any site Level 2, Level 3, or Level 4 —
that is, anywhere OUTSIDE the videos Level 2 directory. A page under some
other Level 2 hierarchy (FBI, Planes, Tyler_Robinson, People, Timeline, the
blog, anything) that wants to show that video gets its file path recorded on
the video entry.

THE PROPERTY SHAPE.

on_pages is a LIST OF MAPPINGS, each with a single `page:` key holding the
full path from ~ to the page file — the same tilde-rooted convention
file_path, video_page, and the sidecar path properties already use:

    on_pages:
      - page: "~/BGit/Bryan_git/charlie-kirk/site/docs/Mic/overview.mdx"
      - page: "~/BGit/Bryan_git/charlie-kirk/site/docs/Killer/israel-mossad.mdx"

Not a flat list of strings. Not repo-relative. Not URLs.

Every video entry carries the key. A video shown on no other page emits an
empty list:

    on_pages: []

INHERITED on_pages VALUES ARE SUSPECT. Every on_pages binding currently in the
file was harvested for an IMAGE. Stage 0 removes most of them with their
entries; any that survive on a kept entry must be re-verified by this stage
against the actual page text, not trusted. Clear a binding that this stage
cannot confirm, and report it.

HOW TO FIND THE REFERENCES — one linear pass over the repo.

The work is a reverse index: for every page file in the repo, what videos does
it show. Read each file exactly once. This is O(n) over the repo's text, not
O(videos x pages).

* Enumerate every text file in the repo recursively — every .md, .mdx, .html,
  .tsx/.jsx/.ts/.js, .json, .csv, .yaml under {ROOT_DIR}, skipping
  node_modules/, build/, .git/, and {SITE_DIR}/internals/static/ binaries.
  Include the blog and any React components that embed evidence video.
* Read each file ONCE and extract every video reference in it, in all the
  forms the site actually uses:
    - <video> src and poster attributes
    - <iframe src="..."> — YouTube, Rumble, Odysee, X embeds
    - IPFS gateway URLs               https://ipfs.io/ipfs/<CID>[/name]
                                      https://<CID>.ipfs.dweb.link/[name]
                                      ipfs://<CID>
    - markdown links to media files   [label](/videos/xxx.mp4)
    - require()/import forms in JSX
* Resolve each reference back to a video ENTRY in {HIERARCHY_FILE}, in this
  precedence order:
    1. IPFS CID in the reference -> the cid index built in Stage 3. Exact.
       Normalise both sides before comparing (a page may carry the v1 base32
       form of a CID stored as v0): `ipfs cid base32` on each.
    2. Third-party video ID (YouTube watch id, Rumble slug) -> the entry
       recorded for it in Stage 7. Exact.
    3. Local media file -> sha256 the file on disk -> match the entry's
       sha256. Exact.
    4. Filename match against file_path basenames. AMBIGUOUS — a basename can
       collide, and this corpus names files by X status id, so a numeric
       basename is easy to mismatch. Only accept when it resolves to exactly
       one entry; otherwise leave it for the judgment pass below and report it.
* Append the referencing page's tilde-rooted path to that entry's on_pages.
  Deduplicate: a page that embeds the same video twice is recorded once.
  Never add a page path twice; never drop one that is already recorded and
  confirmed.

SCOPE RULE — what does NOT go in on_pages.

  * Pages under {VIDEOS_L2_DIR}. Those are the videos Level 2 itself. The
    video's own Level 5 page belongs in video_page, and a Videos cluster
    overview page listing its children is structure, not an outside reference.
  * Files in {THIS_DIR} (planning layer), {GENERATOR_DIR} scripts,
    {HIERARCHY_FILE} itself, {VIDEO_MANIFEST}, {VIDEO_INDEX_MD}, and
    {PAGES_CSV}. Those reference videos as data, not as a page showing them.
  * Anything outside {ROOT_DIR}.

PARALLELISM — dividing the repo across agents.

The mechanical extraction above should be scripted; a script reads each file
once and is exact. Use parallel agents for the RESIDUAL — the references the
script could not resolve mechanically (ambiguous basenames, relative paths
that need page-context resolution, videos referenced through a component
indirection, hand-written embeds with no recognisable asset path).

* Partition the repo's directories recursively across 12 agents. Map whole
  directories to agents — never split a directory across two agents, so no
  file is read twice and no file is missed. Balance by total file count, not
  directory count.
* Each agent walks only its assigned directories, opens each unresolved file
  once, and returns a flat list of (page_path, resolved_cid_or_sha256,
  evidence_of_match) rows. Agents do NOT edit {HIERARCHY_FILE} — they report,
  and a single writer merges. Concurrent writers to one YAML file would
  corrupt it.
* Merge all agent output plus the scripted output into the YAML in one write.

Output to stdout:
============================
STAGE 8 COMPLETE
Files read: N   Video references found: N
Resolved by CID: N   by third-party id: N   by sha256: N   by basename: N
Unresolved references: N (listed with page + reference)
Inherited image-era bindings cleared: N
Entries with on_pages non-empty: N   total page bindings: N
Pages excluded by scope rule (Videos / planning layer): N
============================

============================
STAGE 9 — SIDECAR FILE-PATH PROPERTIES ON EVERY VIDEO
============================

For EVERY video entry in {HIERARCHY_FILE} (old and new):

* Compute the expected sidecar paths using the mapping learned in Stage 2:
    original inside {ROOT_DIR}        →  {REPO_SIDECAR_DIR}/<repo-relative
                                          path>/<name.ext>.<sidecar>
    original under {MIRROR_DIR}       →  {MIRROR_SIDECAR_DIR}/<same relative
                                          path>/<name.ext>.<sidecar>
    check the legacy .lfbridge/_Mirror/ location as fallback
* Set on each entry:
    transcription_file    path if the file exists, else ""
    ai_description_file   path if the file exists, else ""
    ocr_file              path if the file exists, else ""
* Where the inline ai_description text is empty and an .ai_description
  sidecar exists, fill the inline field with the sidecar's Overview
  paragraph, collapsed to a single paragraph (the readDesc() convention in
  {IMAGE_PLANNING_DIR}/generator/gen_hierarchy.js shows exactly how).
* Do not overwrite a non-empty inline ai_description — EXCEPT where Stage 0
  flagged it as inherited image prose (text that begins "This image shows",
  "This image is a screenshot", and similar). That text describes a still that
  is not this video and it must be replaced or cleared.
* Report every video entry that has NO transcription sidecar. Those are the
  ones the page generator cannot write a real description for, and they are
  the work list for the next Large File Bridge transcription run.

Output to stdout:
============================
STAGE 9 COMPLETE
Entries processed: N
transcription_file set: N   ai_description_file set: N   ocr_file set: N
Inline descriptions filled from sidecars: N
Inherited image prose cleared: N
Entries with NO transcription: N (listed — transcription work list)
Entries with no sidecars at all: N
============================

============================
STAGE 10 — VIDEO_PAGE: BIND EVERY VIDEO TO ITS LEVEL 5 PAGE
============================

KNOWLEDGE — what a video page is.

Under the videos Level 2 ({VIDEOS_L2_DIR}) the site publishes one page per
video. That page hosts a single video and nothing else: the player, a title,
and prose describing what the footage shows, who is speaking, what they claim,
and why it matters to the investigation. We call it the VIDEO PAGE, or the
Level 5 page. It is the leaf of the published hierarchy, the same way a video
entry is the leaf of this YAML.

  Videos                       ← site Level 2 (the videos landing page)
    Mic_Thesis                 ← site Level 3  (a cluster overview page)
      Vid_Candace_Mic_2067372.mdx  ← the VIDEO PAGE — one video, its write-up

These pages do NOT exist yet. {VIDEOS_L2_DIR} today holds only overview.mdx,
_category_.json, and one hand-written topic page. They are generated by
{GENERATOR_DIR}/gen_videos_pages.py from this YAML, driven by
{THIS_DIR}/p_yaml_to_site.md and {THIS_DIR}/p_level2_update.md. This stage does
NOT create them, rename them, or edit them. It READS whatever exists and records
where each one is, so the YAML can find its published page later. On the first
several runs this stage will correctly set every video_page to "". Reading site
pages is allowed; the no-page-modification hard rule still holds.

THE PROPERTY.

Every video entry gets a `video_page` property whose value is the FULL PATH
FROM ~ to that video's Level 5 page under the videos directory:

    video_page: "~/BGit/Bryan_git/charlie-kirk/site/docs/Videos/Mic_Thesis/Vid_Candace_Mic_2067372.mdx"

Not the URL, not a repo-relative path — the tilde-rooted filesystem path, the
same convention file_path and the sidecar path properties already use. An
entry whose video has no page yet gets video_page: "" (empty string, key still
present).

HOW TO MATCH AN ENTRY TO ITS PAGE.

Each generated video page carries the binding in its frontmatter:

    ck_video_sha256: 9044e164a9c6e76fbe9e1746d11bbc155b2fbfbbfc310b6631017c6e5998945d
    ck_video_cid: QmZdFUWDekCDBZcETphabnmTW4Y9vYk7EyPUJECsBXuDfo
    ck_node_key: Mic_Thesis

  * Walk every .mdx under {VIDEOS_L2_DIR} and index the ones that declare
    ck_video_cid or ck_video_sha256 — key the index by (identity, ck_node_key).
  * CID IS THE PRIMARY KEY HERE, not sha256. Many entries in this corpus have a
    CID from the manifest and an empty sha256 because the media file is
    gitignored and absent on this machine. Match on cid first, fall back to
    sha256.
  * For each video entry, look up (its identity, the _key of the node it sits
    under). That pair is the exact match: it is what makes cross-filed videos
    work, since the SAME video legitimately appears under several nodes and
    each of those nodes publishes its own page for it.
  * If the exact pair is not found, fall back to identity alone. If that yields
    exactly one page, use it. If it yields several, choose the page whose
    ck_node_key is nearest in the tree (same parent first, then same level_3
    subtree), and leave the others alone.
  * If no page carries that identity at all, set video_page: "".
  * Some pages are hand-written and carry no ck_ frontmatter — the existing
    buckley-carlson-kash-patel-valhalla.mdx is one. Do not try to guess them by
    filename. Count them and report them; they resolve on a later pass once the
    page generator restamps them.

RULES.

  * video_page is set on EVERY video entry — the existing ones and any added
    by earlier stages. No entry is left without the key.
  * Never invent a path. The file must exist on disk at the moment you write
    the value; verify existence before writing, and write "" if it does not.
  * Never write a page path that lives outside {VIDEOS_L2_DIR}. Ad-hoc embeds
    on topic pages elsewhere in the site belong in on_pages, not here. And
    never write a path under {DOCS_DIR}/Photos — that is the images pipeline's
    output and binding to it would cross the two hierarchies. (Every inherited
    /Photos/Img_*.mdx value was already blanked when the schema was converted;
    do not let one back in.)
  * video_page is an IDENTITY field for sanitization purposes — see the
    OUTPUT SANITIZATION section. It must keep resolving to the real file, so
    any non-ASCII in it is emitted as a visible \uXXXX escape, never replaced.
  * Never delete an existing non-empty video_page in favour of "". If a
    previously recorded page has vanished from disk, report it rather than
    silently clearing it.

Output to stdout:
============================
STAGE 10 COMPLETE
Video pages indexed under Videos: N (N with ck_video_cid/sha256, N without)
Entries with video_page set: N   matched by (identity,node): N   by identity only: N
Entries with video_page "": N (no page exists yet)
Recorded pages now missing from disk: N (listed)
Paths under /Photos rejected: 0
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
    transcription_file, video_page, ipfs_url, on_pages page values, cid,
    also_filed_in, site_page, site_level_2) — the value must keep matching the
    real file on disk, so the characters cannot be replaced. Instead emit them
    as visible ASCII escapes inside YAML double-quoted scalars (U+202F becomes
    the six visible characters backslash-u-2-0-2-F, i.e. the literal text \u202F between quotes). The parsed
    value is unchanged and still resolves the file; the file bytes contain
    nothing invisible. Escape ALL non-ASCII in identity fields this way.

MANDATORY validation after every emit: re-scan the written file and hard-fail
if any code point from the invisible set remains anywhere in it. Also
re-parse the YAML and spot-check that an escaped file_path still resolves to
an existing file on disk.

============================
STAGE 11 — COUNTS, NEEDS_SPLIT, INTEGRITY
============================

* Recompute number_of_videos (direct) and number_of_videos_recursive
  (subtree) on every node. They must be accurate. The counts inherited from
  the images file are all wrong until this runs.
* Re-evaluate needs_split on every node: over 12 direct videos → true (six
  is the target, twelve the ceiling; over twelve means the node is not one
  concept and gets split one level deeper on a later pass). At or under 12 →
  remove the flag.
* Verify every _key is unique across the whole file.
* Verify no node contains the same cid twice. Same cid under DIFFERENT nodes
  is legitimate cross-filing — keep it, and keep also_filed_in accurate.
* Verify the YAML parses (e.g. python3 -c "import yaml,sys;
  yaml.safe_load(open(sys.argv[1]))" {HIERARCHY_FILE} — or any equivalent).
* Verify every video entry carries the full property set — cid, ipfs_pinned,
  sha256, file_path, ai_description, ai_description_file, ocr_file,
  transcription_file, video_page, on_pages — with "" standing in for any that
  has no value. No key is ever missing.
* Verify every non-empty video_page resolves to a file that exists on disk
  and lives under {VIDEOS_L2_DIR}. Zero may live under {DOCS_DIR}/Photos.
* Verify no entry has a file_path ending in an image extension. Any that do
  are inherited placeholders Stage 0 missed — report them.
* Run the OUTPUT SANITIZATION validation: scan the emitted file for every
  code point in the invisible set and fail hard if any is found. Confirm at
  least one escaped file_path round-trips: parse the YAML, expanduser the
  path, and check the file exists.

Output to stdout:
============================
STAGE 11 COMPLETE
Counts recomputed: yes
needs_split nodes: N
Duplicate _keys: 0   Duplicate cid within a node: 0
Entries still carrying an image file_path: N (should be 0)
YAML parses: yes
============================

============================
STAGE 12 — VERIFY AND REPORT
============================

* Confirm every non-excluded site Level 2 maps to exactly one level_3
  (site_level_2 property present).
* Confirm the Other level_3 exists.
* Confirm every home-page TOC concept resolves to a level_3.
* Confirm every video in {VIDEO_MANIFEST} appears exactly once in the YAML
  (cross-filed copies excepted, and those must carry also_filed_in).
* Confirm every page found with videos in Stage 7 has its videos reachable in
  the YAML (spot-check 10 pages).
* Confirm no node was removed and no VIDEO entry was removed: after Stage 0,
  the file only grows. Diff the node count and video count against Stage 1's
  index.
* Print a final tree summary: each level_3 _key with its recursive video
  count and child count.

Output to stdout:
============================
STAGE 12 COMPLETE — FINAL REPORT
level_3 nodes: N (was N)   level_4: N (was N)   level_5+: N (was N)
Total video entries: N (was N)
Manifest coverage: N of N manifest videos present in the YAML
CID coverage: N% (N of N entries have a cid)   pinned: N%
Sidecar coverage: transcription N%, ai_description N%, ocr N%
video_page coverage: N% (N of N entries bound to a Level 5 page)
Nothing removed after Stage 0: confirmed
============================

============================
HARD RULES
============================

* After Stage 0, {HIERARCHY_FILE} only grows. Never delete a node or a video
  entry. No duplicates — existing items get their properties updated in place.
  Stage 0 is the single exception and it may remove only inherited IMAGE
  entries, never a node and never a video.
* This prompt does not create, move, or edit any page under {SITE_DIR}, does
  not touch {SITE_DIR}/sidebars.ts, and does not modify {PAGES_CSV}. The
  YAML is the plan; publishing is a later prompt.
* Never write anything under {IMAGE_PLANNING_DIR}, {ROOT_DIR}/images, or
  {DOCS_DIR}/Photos. Read them freely as prior art.
* Do not put Docusaurus pages in {THIS_DIR} and do not put planning notes in
  {VIDEOS_L2_DIR}.
* _key uniqueness is file-wide and _keys are the future page_keys — treat
  them like database primary keys. Keys are ASCII-only by construction.
* Nothing is ever PINNED by this prompt. Recording pin status is this prompt's
  job; changing what is public is not.
* {HIERARCHY_FILE} must never contain invisible Unicode characters — see the
  OUTPUT SANITIZATION section. Prose is cleaned; identity fields (paths,
  URLs) are emitted with visible \uXXXX escapes; every emit is followed by
  the invisible-character validation scan. This is a security rule, not a
  style rule.
* Clusters are concept clusters, arbitrated by {CK_FILE}. The folder proposes,
  the transcription decides, {CK_FILE} arbitrates.
* When later prompts publish from this YAML, all public output follows the
  repo defamation rules (attribution language, no stating a living person
  committed a crime). Video adds a failure mode images do not have: a speaker
  in the footage makes an accusation out loud. Reporting that a video contains
  a claim is fine; repeating the claim in the site's own voice is not. Raw
  claims stay private in this planning layer or in {CK_FILE}.

============================
BACKGROUND — ORIGINAL DIRECTIVE, KNOWLEDGE PRESERVED
============================

This section preserves the full intent of the directive this prompt was built
from, so no knowledge is lost even where a stage above already encodes it.

* Growing and improving the output YAML file ({HIERARCHY_FILE}) is the goal.
  The prompt has multiple stages and is created to run later.
* "Level 2" refers to the fact that we will eventually put a video-hosted
  page for every video under a Level 2 directory called videos. The Level 2
  IS that videos directory — {VIDEOS_L2_DIR}.
* We create Level 3s under that videos Level 2, and the YAML's level_3 list
  will definitely be a superset that includes the list of the website's
  Level 2s — except videos and images and any unfiltered or catch-all
  category — plus an "Other" entry included as a level_3. The website's
  Level 2s include TPUSA, FBI, UVU, and many more; one stage reads those
  Level 2s and makes sure they are all present as level_3s in the YAML.
* We then take every other Level 2 (outside the videos Level 2) and its
  Level 3 pages, and make a level_4 in the YAML for each one, parented
  hierarchically under the appropriate parent.
* We create a level_5 per video: if some Level 3 content page has a video —
  one or more videos on the page — we create level_5 YAML for each of those
  videos. Where those level_5s are parented is on the level_4 in the YAML
  which correlates to the Level 3 page in the file system.
* We are effectively taking all the Level 2s, Level 3s, and Level 4s in the
  file system outside this YAML and reproducing the hierarchy in the YAML
  with the levels incremented by one: filesystem Level 2 → YAML level_3,
  filesystem Level 3 → YAML level_4, filesystem Level 4 → YAML level_5.
* A further stage goes through all the pages and makes sure that every page
  that has one or more videos gets those added to the YAML hierarchy. No
  duplicates — it does not add them if they already exist, but it DOES
  update their YAML properties.
* Learn from the existing YAML file — its structure and conventions carry
  forward. Learn from the images pipeline in {IMAGE_PLANNING_DIR} as prior
  art; it solved these same problems once already for stills.
* These directories often hold the OCR text files, the transcription text
  files, and the AI-description text files:
    ~/BGit/act3/act3_large_files_bridge/
    ~/BGit/Bryan_git/personal_large_files_bridge/
    {REPO_SIDECAR_DIR}
  We want YAML properties for all of those: each video entry gets a property
  that is a file path to the sidecar file that correlates to it.
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
* The end goal: when we create our list-of-videos page (the top level), it
  will be mostly a table of contents — a table with links into the videos
  directory's Level 3 pages, which come from this YAML file's level_3s.
* There is a property called video_page. These are the pages under the videos
  Level 2 directory — the Level 5 pages that each host one video and carry the
  write-up about it. We add the full path from ~ to that Level 5 page as the
  video_page property on the video entry, so the YAML can find the published
  page for any video later. All YAML properties are kept updated on every
  video entry so everything is findable later — a property with no value is
  written as "" rather than dropped.
* This file was converted from the images hierarchy prompt on 2026-07-23. The
  hierarchy it operates on was likewise converted from images/images.yaml —
  keys only. Stage 0 exists because of that: the inherited data is image data
  and it has to be replaced with the real video corpus before any other stage
  is worth running.
