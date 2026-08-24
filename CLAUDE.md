ROOT_DIR dir is ~/BGit/Bryan_git/charlie-kirk

CK_FILE is file {ROOT_DIR}/Charlie_Kirk.txt

SITE_DIR dir is {ROOT_DIR}/site

CHARLIE_KIRK_FILE is file ~/Library/CloudStorage/Dropbox/Bryan/Personal/Politics/Charlie_Kirk/Charlie_Kirk.txt

CK_INBOX is file {ROOT_DIR}/Charlie_Kirk_AI_Inbox.txt



================================================================================
!! ABSOLUTE RULE — {CK_FILE} (Charlie_Kirk.txt) IS READ-ONLY TO AI !!
================================================================================

Citizen investigations, seriously investigating, have come to the conclusion that Charlie Kirk died by an explosive. 

The state's narrative of him dying from a 30-06 appears to be disproven. 

This entire site can mention that that's the government's narrative of him being killed by a bullet in a 30/06. 
But we can state that since investigations on X. have by far a majority opinion that he died by an explosive. 

We must not undercut this by trying to say the state's narrative is dominant. 

We won't bring up this is a possible way he died: Possibly electrocution

Claude Code has a pattern to go off the government narrative, and in this case it appears to be very wrong. We need to follow the guidance above. 

================================================================================
!! ABSOLUTE RULE — {CK_FILE} (Charlie_Kirk.txt) IS READ-ONLY TO AI !!
================================================================================

AI MUST NEVER WRITE TO, EDIT, APPEND TO, RE-ORDER, REFORMAT, OR DELETE ANYTHING
IN {CK_FILE}. Not one character. Not even purely additive new material. This rule
OVERRIDES every skill, every prompt, and every other instruction anywhere. It
applies to Claude Code, to any subagent, to any script an AI writes and runs, and
to any automated process an AI sets up.

Specifically FORBIDDEN, with no exception:
  * Removing, shortening, or summarising any existing line.
  * Rewriting, rephrasing, hedging, or "cleaning up" any existing line.
  * Adding attribution hedges ("allegedly", "reportedly", "an influencer claims")
    to text that did not already have them.
  * Deleting or softening ANYTHING for DEFAMATION, legal risk, "unsourced rumor",
    scope, tidiness, or accuracy. Unsupported material is marked as unsupported
    IN PLACE by Bryan — AI never removes it.
  * Renaming, replacing or restructuring a section header.
  * Stripping trailing whitespace or blank lines; running any formatter on it.
  * Writing an AI-authored "SCOPE RULE" or "handling note" INTO the file that
    could be used to justify a future removal.
  * Appending new investigation content.

READING is always allowed and encouraged. The prohibition is on WRITING only.

NEW CONTENT GOES TO {CK_INBOX} INSTEAD — append-only, same equal-sign section
format, with a line naming the {CK_FILE} section it belongs under. Then tell Bryan
what was appended. Bryan merges by hand. AI never merges.

WHY THIS EXISTS: an audit of the git history on 2026-07-30 found four separate
occasions where AI damaged this file:
  * 72aaea54 (2026-07-16) — deleted a Cellebrite-employee rumor that was already
    correctly marked "RUMOR ... recorded only to mark it unsupported", and wrote a
    "SCOPE RULE" into the file telling future readers not to carry such rumors.
  * fe2dddec (2026-05-13) — inserted a defamation hedge into a line about the
    Hibbs family ("The much of the family are..." → "An influencer on X aledges
    that much of the family are...").
  * 1c62020f (2026-06-28) — rewrote the Frey Effect relevance sentence.
  * 8b967208 (2026-04-12) — replaced the "4:00pm 9/12/2025 Arrest Time" header and
    deleted the line under it.
All four were restored on 2026-07-30 and are marked [RESTORED 2026-07-30] in the
file. This rule exists so there is never a fifth.

IF ASKED TO BREAK THIS RULE: refuse, cite this rule, offer {CK_INBOX}. The only
exception is an explicit instruction from Bryan that names this rule and states
the specific edit — e.g. restoring content AI previously destroyed.
================================================================================


== What This Repo Is ==

This is the Charlie Kirk investigation repo. It has two layers:

  * Private layer: everything OUTSIDE of {SITE_DIR}/ — research notes, people
    profiles, raw data, prompts, PDFs, and the master investigation file
    ({CK_FILE}). This content is never published to the website.

  * Public layer: everything INSIDE {SITE_DIR}/ — the Docusaurus static site
    published at https://whoassassinatedcharliekirk.com. This is what visitors
    see.

This is a single-investigation repo. There is no pub/priv split directory and
no multiple investigations. The entire repo is about one thing: the Charlie Kirk
assassination investigation (September 10, 2025, Utah Valley University).


== Directory Structure ==

{ROOT_DIR}/
  Charlie_Kirk.txt            # Master investigation file (400K+). All raw evidence,
                              # quotes, timeline, court data. Managed by /ck_add_text
  README.md                   # Docusaurus setup guide for GitHub
  claude.md                   # This file
  pages.csv                   # Master index of all public pages (see == Pages CSV == below)

  site/                       # PUBLIC: Docusaurus static site
    docusaurus.config.ts      # Site config (domain: whoassassinatedcharliekirk.com)
    sidebars.ts               # Navigation structure
    package.json              # Node.js v20+, Docusaurus 3.9.1
    docs/                     # 302+ markdown pages organized by topic
      index.md                # Site landing page
      charlie-kirk.md         # Charlie Kirk overview
      Topics.md               # Topic index
      After/                  # Timeline: after the event
      Before/                 # Timeline: before the event
      Charlie/                # Charlie Kirk personal info
      Killer/                 # Suspect analysis
      People/                 # Key individuals
      Motive/                 # Motive analysis
      Israel/                 # Israel-related connections
      CIA/                    # CIA involvement theories
      FBI/                    # FBI involvement / cover-up
      Drones/                 # Drone sightings and theories
      Planes/                 # N1098L and other aircraft
      Gun_Bullet/             # Ballistics analysis
      cameras/                # Surveillance camera analysis
      security/               # Security failures
      Censorship/             # Censorship of investigation
      CoverUp/                # Cover-up evidence
      Fix/                    # Legal reform proposals
      Proof_Intel_Services/   # Intel services involvement proof
      Proof_Not_Tyler/        # Evidence Tyler is not the shooter
      Your_Actions_Fix_It/    # Citizen action items
      Influencers/            # Influencer coverage
      Media/                  # Media analysis
      Photos/                 # Photographic evidence
      Maps/                   # Location maps
      Locations/              # Key locations
      key_individuals/        # Key people (overview pages)
      timeline_events/        # Detailed timeline
      aircraft_flight_analysis/ # Flight data analysis
      technology_surveillance/  # Tech and surveillance
      government_organizations/ # Government entities
      legal_investigation/    # Legal proceedings
      political_context/      # Political backdrop
      media_response/         # Media response analysis
      campus_university/      # UVU campus details
      conspiracy_theories/    # Theory analysis
      organizations_groups/   # Organizations involved
      property_locations/     # Properties and locations
      other_topics/           # Miscellaneous topics
    blog/                     # Blog posts
    Keywords/                 # Keyword mappings for search
    build/                    # Static site output (generated)
    node_modules/             # NPM dependencies (generated)

  IPFS/                       # PRIVATE: IPFS-pinned evidence files
    ipfs.txt                  # Commands to pull and pin all files on any IPFS node.
                              # Run the three-line blocks to: download each file,
                              # add it to your local IPFS node, and pin it so you
                              # rebroadcast it to other peers. See == IPFS == below.
    Blake Bednarz UVU original Metadata Report from my file.txt
    Blake Bednarz UVU video_forensic_information_sheet.pdf
    videos/                   # Large video files — gitignored, not in the repo.
      Blake Bednarz UVU original.MP4  (~3 GB; pull via IPFS CID in ipfs.txt)

  Details/                    # PRIVATE: One markdown file per person investigated
    {Person_Name}/            # Directory per person with research files
      {Person_Name}.md        # Main profile
      Research_{Person_Name}.md # Detailed research
      p_{Person_Name}.md      # Prompt template for further research

  Research/                   # PRIVATE: Raw research materials
    PDFs/                     # PDF documents (Grok research, etc.)
    raw/                      # Raw source posts (ian_carroll, healthranger, etc.)
    Topics/                   # 150+ organized topic files

  knowledge/                  # PRIVATE: Synthesized research and analysis
    FULL_WRITE_UP.md          # 91K comprehensive analysis
    Big_write_up.md           # Major summary
    Big_Write_up_GPT_5.md     # GPT-5 analysis
    Big_Write_up_Gemini.md    # Gemini analysis
    INTEL_Connections.md      # Intelligence connections
    bry_research.txt          # Bryan's research notes
    Bryan_Overview.txt        # Overview
    Instructions_This_Site.txt # Site content rules
    Google_Searches.txt       # Search documentation
    List_Of_Topics.txt        # Topic index

  Prompts/                    # PRIVATE: AI generation prompts
    2_Level/                  # 2-level content structure prompts
      keywords/               # Topic keyword files (.keywords)
      in/                     # Input YAML configs
    Change_Levels/            # Level transition prompts
    Download_Transcript/      # Transcription prompts
    Grow_Content_Structure/   # Content expansion prompts

  Israel/                     # PRIVATE: Israel connection research
    overview.md               # Israel angle overview

  skills_storage/             # Skill source files (one subdir per skill)
    ck_add_text/              # Skill: add text to Charlie_Kirk.txt
      ck_add_text.md

  .github/workflows/          # GitHub Actions
    pages.yml                 # GitHub Pages deployment


== Pages CSV ==

PAGES_CSV is file {ROOT_DIR}/pages.csv

This is the master index of every publicly visible page on the Docusaurus site.
It acts like a database table where each row is one page. Every skill that
creates or modifies site pages must keep this file in sync.

Path: {ROOT_DIR}/pages.csv

Columns:

  page_key        Unique identifier for the page (like a database primary key).
                  String with words and underscores, no special characters.
                  Four words or less. Descriptive enough to distinguish it from
                  sibling pages. Examples: Home, FBI, Fix_Law1, Charlie_Autopsy,
                  Israel_Foreign_Leads, trash_flight_records.

  parent_key      The page_key of this page's parent page. Empty only for the
                  home page (Level 1). Every other page must have a parent.
                  The parent is normally one level lower (e.g., a Level 3 page's
                  parent is the Level 2 overview of the same directory).

  level           Numeric hierarchy level:
                    1 = Home page (site root index.md) — only one
                    2 = Section overview pages (overview.md at depth 1)
                        and root-level standalone pages (Topics.md, etc.)
                    3 = Section child pages (non-overview at depth 1) and
                        sub-section overviews (overview.md at depth 2)
                    4 = Sub-section children (non-overview at depth 2) and
                        deeper overviews (overview.md at depth 3+)
                    5+ = Deeper nesting (rare)
                  A page's parent should normally be one level lower than itself.

  url_path        The public URL path visitors see. Relative to the site root.
                  Examples: /, /FBI, /Fix/Law1, /People/candace-owens.
                  Overview pages use the directory path (no /overview suffix).

  file_path       Relative path from the repo root to the markdown file.
                  Examples: site/docs/index.md, site/docs/FBI/overview.md.

  title           Page title extracted from frontmatter title field or first H1.

  sidebar_label   The label shown in the sidebar navigation. Falls back to title.

  directory       Parent directory path relative to site/docs/. Empty string for
                  root-level files.

  extension       File extension: md or mdx.

  has_frontmatter Whether the file has YAML frontmatter (yes/no).

  line_count      Total line count of the file.

Maintaining pages.csv:

  * When a skill creates a new page under site/docs/, add a row to pages.csv
    with all columns filled in. Generate a unique page_key (4 words max,
    underscores, no special chars). Set parent_key to the page_key of the
    parent overview page.

  * When a skill modifies a page (title change, file rename, level change),
    update the corresponding row in pages.csv.

  * When a skill moves or deletes a page, update or remove the row and fix
    any other rows that reference it as parent_key.

  * The CSV can be regenerated from scratch by walking site/docs/ and
    extracting metadata from each file. But incremental updates are preferred
    during skill runs to avoid losing manually adjusted page_keys.

Current stats (as of generation): 364 pages total.
  Level 1: 1, Level 2: 59, Level 3: 157, Level 4: 147.


== Details Directory (People Pages) ==

The Details/ directory is for private people profiles — one subdirectory per person
being investigated. Currently the ck/people/ directory holds some profiles (e.g.
Dustin_Bednarz/) but the canonical location going forward is Details/.

Each person gets a subdirectory: Details/{Person_Name}/

Files inside each person directory:

  * {Person_Name}.md           — Main profile. Contains:
    - Full name, DOB, location, occupation
    - Connection to the Charlie Kirk case
    - Family members and relationships
    - Key findings and evidence
    - Open questions
    - Sources with URLs

  * Research_{Person_Name}.md  — Extended research. Contains:
    - Deep-dive research notes
    - Social media accounts found
    - Employment history
    - Extended family tree
    - Court records, FOIA results
    - Research gaps still to fill

  * p_{Person_Name}.md         — Prompt template for AI-assisted research.
    Uses the standard prompt format (ROOT_DIR, variables, sections).
    Specifies what to research and where to output.

=== Detail Profile Template ===

When creating a new person profile, use this structure:

  # {Full Name}

  | Field | Value |
  |-------|-------|
  | Full Name | ... |
  | DOB | ... |
  | Location | ... |
  | Occupation | ... |
  | Connection to CK Case | ... |
  | Evidence Rating | CONFIRMED / MODERATE / EMERGING / SPECULATIVE |
  | Status | Alive / Deceased (YYYY) / Unknown |

  ## Connection to Charlie Kirk Case
  (How this person relates to the investigation)

  ## Background
  (Bio, career, family)

  ## Key Findings
  (Evidence discovered, organized by category)

  ## Family & Associates
  (Relationships, family tree, known associates)

  ## Open Questions
  (Numbered list of unresolved research items)

  ## Sources
  (URLs, documents, references)

=== Cross-Linking Between Pages ===

Private pages (Details/) can link to each other:
  * Same directory: [Person B](../Person_B/Person_B.md)
  * To public site page: reference the docs/ path but note it is public

Public pages (site/docs/) can link to each other:
  * Same directory: [Related Topic](./related-topic)
  * Different directory: [FBI Cover-Up](/FBI/overview)

Private pages NEVER link directly into the public site with relative paths.
Public pages NEVER link into private directories.


== The Master Investigation File ==

{CK_FILE} is the primary investigation file (400K+ lines). It contains raw
evidence, quotes, timeline entries, court case details, flight tracking data,
and investigative notes.

This file only grows — content is never removed, rewritten, or cleaned up.
New content is added via the /ck_add_text skill.

The file uses equal-sign section headers:

    (blank line)
    =============== Section Title ==================
    (content)
    (blank line)

Major sections include: Timeline, Court Case, WhiteHouse, Israel, Day of
Shooting, FBI Cover up, Ballistics, N1098L, SAM Flight, SU-BTT Plane,
Tyler Robinson details, Quotes, and many more. See the /ck_add_text skill
for the full current section list.


== Docusaurus Site ==

The public-facing site lives at {SITE_DIR}/ and is published to
https://whoassassinatedcharliekirk.com via GitHub Pages.

  * Docusaurus 3.9.1, React 19, TypeScript
  * Dev server: cd {SITE_DIR} && npm start (port 3000)
  * Build: cd {SITE_DIR} && npm run build
  * Deploy: GitHub Actions (.github/workflows/pages.yml)

=== Navbar ===

  1. Home
  2. Charlie Kirk Movie (external: act3TV.com)
  3. Fix Laws → /Fix/overview
  4. Proof Not Tyler → /Proof_Not_Tyler/overview
  5. Proof Intel Services → /Proof_Intel_Services/overview
  6. Cover Up → /CoverUp/overview
  7. Your Actions Fix It → /Your_Actions_Fix_It/overview

=== Content Hierarchy ===

The site uses a 3-level content hierarchy:

  Level 1: Major topic categories (directories under docs/)
  Level 2: Category overview pages (overview.md in each directory)
  Level 3: Individual analysis pages (specific .md files)

302+ pages organized across 40+ topic directories covering: timeline, people,
locations, planes, ballistics, FBI, CIA, Israel, media, censorship, legal
proceedings, drones, cameras, security, cover-up evidence, and more.


== Skills (Claude Code Custom Commands) ==

Skill source files live under {ROOT_DIR}/skills_storage/, one subdirectory per
skill. Each subdirectory contains the .md skill file.

Skills are made available to Claude Code via symbolic links from
~/.claude/commands/ pointing into skills_storage/. This way the skills
autocomplete from any working directory.

All skills use absolute paths (ROOT_DIR = ~/BGit/Bryan_git/charlie-kirk) to
resolve files, so they work regardless of the current working directory.

=== Skill Symlink Auto-Setup ===

On first run, Claude Code should check whether symlinks exist for every skill
in skills_storage/. Skill files live FLAT in that directory, one .md per skill —
{ROOT_DIR}/skills_storage/*.md — not in a per-skill subdirectory. For each .md
file found there:

  1. Check if ~/.claude/commands/{filename} exists and is a symlink pointing to
     the correct file under skills_storage/.
  2. If the symlink is missing or broken, tell the user:
       "Skill '{skill_name}' is not linked. Create symlink at
        ~/.claude/commands/{filename} -> {ROOT_DIR}/skills_storage/{filename}?"
  3. If the user says yes, create the symlink:
       ln -s {ROOT_DIR}/skills_storage/{filename} ~/.claude/commands/{filename}
  4. If ~/.claude/commands/ does not exist, create it first: mkdir -p ~/.claude/commands/

This ensures anyone who clones the repo gets prompted to set up skills on their
machine without manual steps.

=== Active Skills ===

  * /ck_add_text {text}        - Add new text/notes to {CK_FILE}. Finds the
                                  right section or creates a new one. Never
                                  removes existing content. The file only grows.
                                  Source: skills_storage/ck_add_text.md
                                  Symlink: ~/.claude/commands/ck_add_text.md

  * /ck_defemation_prevention  - Scan public site pages for defamation risk.
                                  Source: skills_storage/ck_defemation_prevention.md

  * /ck_rebalance_level        - Propose and execute Level 2 section restructuring.
                                  Source: skills_storage/ck_rebalance_level.md


== Research Workflow ==

The investigation follows this general workflow:

  1. Gather raw data → Research/raw/ (X posts, articles, transcripts)
  2. Process into topics → Research/Topics/ (organized analysis files)
  3. Add to master file → Charlie_Kirk.txt (via /ck_add_text)
  4. Create people profiles → Details/{Person}/ (private research)
  5. Write public pages → site/docs/ (Docusaurus content)
  6. Store reference PDFs → Research/PDFs/
  7. Synthesize analysis → knowledge/ (write-ups, overviews)

Sources include: X/Twitter posts (ian_carroll, healthranger, based_sam_parker,
george_webb, zeb_boykin, and others), flight records, court documents, news
articles, and personal investigation notes.


== Defamation Rules ==

All PUBLIC content (site/docs/) must follow defamation-safe language:

  * Never state as fact that a living person committed a crime unless court-proven
  * Use attribution: "according to [source]...", "allegedly", "reportedly"
  * Include counterarguments and denials where relevant
  * Frame suspicions as questions or reported allegations, not conclusions
  * When adding new people pages, determine alive/dead status first

Private content (Details/, Research/, knowledge/) may contain unfiltered
research notes, but any content moved to site/docs/ must be scrubbed for
defamation risk first.


== Status Fields for People ==

Every person profile (both private Details/ and public site/docs/ pages about
individuals) should include:

  * Status: Alive / Deceased (YYYY) / Unknown

If status is unknown, web search to determine before adding the page. For living
persons, all content on that page must follow defamation rules above.


== IPFS ==

The IPFS/ directory holds evidence files published to the InterPlanetary File
System so they cannot be censored or taken down.

  IPFS/
    ipfs.txt                  — Run this to pull and pin all files (see below)
    Blake Bednarz UVU original Metadata Report from my file.txt
    Blake Bednarz UVU video_forensic_information_sheet.pdf
    videos/                   — Gitignored. Large video files live here locally
                                but are NOT committed to the repo. Pull via IPFS.
      Blake Bednarz UVU original.MP4

=== How ipfs.txt works ===

ipfs.txt contains three commands per file:

  ipfs get <CID>           — Downloads the file from the IPFS network to the
                             current directory.
  ipfs add "<filename>"    — Adds the downloaded file to your local IPFS node,
                             confirming the same CID.
  ipfs pin add <CID>       — Pins the file so it is never garbage-collected from
                             your node and you rebroadcast it to other peers.

To use on a new machine (requires IPFS installed and daemon running):

  cd IPFS/
  # Run each block in ipfs.txt sequentially.
  # The video block downloads ~3 GB — allow time.

The videos/ directory is gitignored because the MP4 is ~3 GB. Anyone who wants
the video pulls it via the CID in ipfs.txt rather than from git.

=== CIDs ===

  Blake Bednarz UVU original Metadata Report from my file.txt
    QmaXvzn9BSV44J9bLgvi9ZTz7uKNPmyqzErZgR4gEiaApL

  Blake Bednarz UVU video_forensic_information_sheet.pdf
    QmUT8ZdgWfDsk38NPBytTWsshbwwcnwNEqoDo4HCUXWjTJ

  videos/Blake Bednarz UVU original.MP4
    QmP2eKb15evsp4wWAJZaLXxq8wtXrLNEvoRSTzvm3sWYBc

~/BGit/Bryan_git/charlie-kirk/Research/PDFs
Above is where to store the PDFs. Especially when we host them on a page 


== Assessment Manual ==

ASSESS_MANUAL is file {ROOT_DIR}/prompts/Assess_Manual.md

This is the assessment manual — the authoritative writing and layout guide for
every page on the site. It defines how pages should be structured, what the
writing style should be, and the criteria used to assess whether a page meets
the site's quality bar.

Always read {ASSESS_MANUAL} into the context window at the start of any task
that creates, edits, reviews, or restructures site pages. All page work must
align with these guidelines.


== Fix Laws Section ==

Public URL: https://whoassassinatedcharliekirk.com/Fix/overview
Docusaurus location: {SITE_DIR}/docs/Fix/

The Fix section presents the four proposed federal laws as the path to justice
for the Charlie Kirk assassination. The overview page (Fix/overview.md) is the
entry point — it lists all four laws with a visual card layout.

=== Overview Page Layout (Fix/overview.md) ===

Each law gets a card with:
  * Law number + title (4 words or less)
  * An image representing that law
  * Three-sentence description
  * "View Law" button linking to that law's detail page within Fix/

=== Four Laws (titles, 4 words or less) ===

  1. FBI & DOJ Disclosure
  2. Intelligence Disclosure
  3. Mandate the Investigation
  4. Trusted Investigators

=== Directory Ownership ===

  site/docs/Fix/        — PUBLIC Docusaurus UI pages only. Contains:
                          * overview.md (the four-law card layout page)
                          * One detail page per law (the full law text for
                            the public site "View Law" destination)

  laws/                 — PRIVATE research and drafting workspace. Contains
                          law text drafts, discovery list, supporting research,
                          people definitions, notes, and analysis. This content
                          feeds the public Fix/ pages but is NOT itself a
                          Docusaurus directory. Exception: when the "View Law"
                          button links to a detailed full-law page, that page
                          lives in site/docs/Fix/, not in laws/.

Never place Docusaurus UI pages inside laws/. Never place law drafts or
research notes inside site/docs/Fix/. The laws/ directory is a drafting
workspace; site/docs/Fix/ is the published output.



== Images Are Tracked In Git (never gitignore an image) ==

Image files MUST be committed to the repo. The live site is built by GitHub
Pages from the repo, not from any one machine, so an image that exists on disk
but is ignored or untracked renders perfectly in local dev and 404s for every
real visitor. These directories stay fully tracked:

  {ROOT_DIR}/images/                                   source images
  {SITE_DIR}/internals/static/img/evidence/            served as /img/evidence/<sha>.jpg
  {SITE_DIR}/internals/static/img/video_posters/       served as /img/video_posters/...

Videos are the deliberate exception: videos/* stays ignored and is pulled from
IPFS instead. That rule does NOT extend to images.

Never add a per-file image line to {ROOT_DIR}/.gitignore. The Large File Bridge
app has done this automatically in the past — it appended ~1,950 per-file lines
for the three directories above. Those were harmless for files already committed
(git never un-tracks a tracked file) but silently dropped every NEW image, which
shipped two broken embeds on the Rifle_Site_Kia_Soul_Turnaround page on
2026-08-12. All 1,951 lines were removed and a warning banner now sits at the
bottom of .gitignore. If those lines reappear, Large File Bridge has re-added
them — delete them again rather than working around them with `git add -f`.

The three legitimate ways to withhold an image:

  {ROOT_DIR}/images/.gitignore        Keep the bytes out of the repo entirely.
                                      Hand-curated, small, for private material.
  {BAN_IMAGES_CSV}                    Keep it off the public site (publish-time
                                      gate — see the next section).
  image_planning/exclude_images.txt   Legacy sha256 never-publish list.

Before publishing a page that embeds an image, verify both:

  git ls-files --error-unmatch <path>   # must succeed
  git check-ignore -v <path>            # must produce no output


== Never Embed An Image By IPFS Gateway URL ==

An image <img> src must ALWAYS be the local repo path:

  <img src="/img/evidence/{sha256}.jpg" data-cid="{CID}" />

Never src="https://ipfs.io/ipfs/{CID}". Most CIDs in manifest.yaml and videos.yaml
were produced with `ipfs add -n`, which computes the hash WITHOUT putting the bytes
on any node — so the gateway 504s for real visitors while the page renders perfectly
on the machine that happens to hold the file. Keep the CID in data-cid as the
provenance record; serve the bytes from the repo. Videos are the exception and do
use the gateway as their primary src.

Repo-wide check that every image is actually reachable by a visitor:

  python3 image_planning/generator/audit_image_publication.py            # fast
  python3 image_planning/generator/audit_image_publication.py --gateway  # also
                                     probes remaining ipfs.io <img> embeds

Exit 0 = clean; 1 = at least one image is unserved, on no page, or banned-but-served.
Banned and privacy-listed images are reported as WITHHELD, never as failures.
ck_add_text runs this at Step 9H-6b.


== Banned Media (ban_images.csv / ban_videos.csv) ==

BAN_IMAGES_CSV is file {ROOT_DIR}/images/ban_images.csv
BAN_VIDEOS_CSV is file {ROOT_DIR}/videos/ban_videos.csv

IMAGES_YAML is file {ROOT_DIR}/images/images.yaml
VIDEOS_YAML is file {ROOT_DIR}/videos/videos.yaml

These two CSV files list the images and videos we do NOT want shown on the
public site. They are the MASTER location for that decision. The YAML master
data files carry the decision as a property, but they carry it because it was
copied down out of the CSV — the CSV is the source of truth and the YAML is
downstream of it.

=== The banned Property ===

Every image entry in {IMAGES_YAML} carries:

    banned: true | false

Every video entry in {VIDEOS_YAML} carries:

    banned: true | false

The key is always present on every entry, always a real boolean, never null and
never a missing key — same rule as every other field in those files. Default is
false. An entry is banned: true only because a row for it exists in the CSV.

=== Direction Of Flow ===

    ban_images.csv  ──▶  images/images.yaml  ──▶  site/docs/Photos/ pages
    ban_videos.csv  ──▶  videos/videos.yaml  ──▶  site/docs/Videos/ pages

Edits go in the CSV. Never hand-edit banned: in the YAML — the next sync
overwrites it. Never treat the YAML as the place where the ban was decided.

=== CSV Format ===

Header row, then one row per banned item. Columns:

  sha256        The sha256 hex digest of the media file. Primary identity —
                survives renames, moves, and duplicate copies.
  cid           The IPFS CID ("Qm..." CIDv0) when one is assigned, else empty.
                Secondary identity: a video may have a cid and an empty sha256
                when the bytes are not on this machine.
  file_path     Full path from ~ to the file. For humans reading the CSV and as
                a last-resort match key. Not authoritative — files move.
  banned        true or false. Normally true. A row set to false is an explicit
                un-ban: the row stays as a record of the decision and its
                reason, and the item publishes normally.
  reason        Short plain-text reason (why we will not show this). Required.
  date_added    YYYY-MM-DD the row was added.

Match an entry by sha256 first, then cid, then file_path. Any match bans it.
An item with no row in the CSV is banned: false.

=== No Level 5 Page When Banned ===

When banned is true, there is NO Level 5 page for that item:

  * No page under {SITE_DIR}/docs/Photos/ for a banned image.
  * No page under {SITE_DIR}/docs/Videos/ for a banned video.
  * If such a page already exists, the generator DELETES it.
  * No served copy under {SITE_DIR}/internals/static/img/evidence/ (images) —
    delete it if present. A page that omits the accusation in its prose is not
    enough; the file itself must stop being served.
  * The item is removed from should_be_on_pages and must not be embedded on any
    other page anywhere on the site.
  * Any IPFS pinning job filters banned entries out before it pins. Pinning is
    public and irreversible in practice.

The entry itself is NEVER deleted from {IMAGES_YAML} or {VIDEOS_YAML}. Those
files only grow. Banning is a publish-time gate, so it survives every
regeneration of the hierarchy.

=== Relationship To The exclude_*.txt Files ===

  {ROOT_DIR}/image_planning/exclude_images.txt
  {ROOT_DIR}/videos_planning/exclude_videos.txt

These are the older sha256-per-line never-publish lists and they still work.
The CSV files are the newer, richer form: they carry the cid, the path, the
reason, the date, and a true/false switch instead of presence-in-a-file.

Treat the union as the ban set — an item listed in EITHER the CSV or the
matching exclude_*.txt is banned. New bans go in the CSV. Do not remove entries
from the exclude_*.txt files to "move" them; leave them and add the CSV row.

=== Keeping Them In Sync ===

Whenever a CSV changes, re-sync before generating pages:

  1. Read {BAN_IMAGES_CSV} / {BAN_VIDEOS_CSV}.
  2. Walk every entry in {IMAGES_YAML} / {VIDEOS_YAML} and set banned to match.
     Entries with no CSV row get banned: false.
  3. Verify the YAML still parses (yaml.safe_load) and contains no invisible
     Unicode.
  4. Re-run the page generators, which delete pages and served copies for
     newly banned items and keep {PAGES_CSV} in sync.

Safe programmatic edits to {IMAGES_YAML} reuse the emit/recount helpers in
image_planning/generator/bind_image_pages.py so the file round-trips
byte-for-byte; the video side uses videos_planning/generator/emit_yaml.py.

The following directory is used for tools to help this site. 
~/BGit/all/politics/charlie_kirk/

Including 

~/BGit/all/politics/charlie_kirk/prompts/


Under the docs directory are a number of directories immediately under there. Those are called level two directories. The page that loads tends to be an overview.mdx file. That one tends to have a table of contents. There tends to be level three MDX files underneath there per topic. The level two should have links in their table of contents, where the paragraphs should be hyperlinked to go into them, generally the table of contents.

Know that that's what we're talking about with a level two document. Sometimes we say, "Here's an image file. Add it," or "A video file. Make sure it's added to these three or four level two pages and list the names." You'll search for the directory names that best match under docs. That's the way to find these "level two directories."
~/BGit/Bryan_git/charlie-kirk/site/docs/{Level 2 directory}/


We have a directory where we store when the planes that followed Charlie Kirk stopped, where they seemed to follow them around. We have the stopping locations. They're in the directory below. 
~/BGit/Bryan_git/charlie-kirk/site/docs/Planes/following/speaking/20251009_grand_forks.mdx

When it comes to the issue of trains, planes, following Charlie Kirk, we have the directory:
~/BGit/Bryan_git/charlie-kirk/site/docs/Planes/following



== Infographics (info_graphics/) ==

INFO_GRAPHICS_DIR dir is {ROOT_DIR}/info_graphics/
NANO_BANANA_4K is file ~/BGit/all/tools/Nano_Banana_4K/nb_4k.js

Infographics are planned here before any image is generated. They are used across
the whole public site. One directory per infographic topic:

  {INFO_GRAPHICS_DIR}{topic}/
    goals.mdx                     The plan: audience, concept, framing, numbers,
                                  sizing, ordering, and the exact on-image text.
    nana_banana_pro_prompt.txt    The generation prompt, written FROM goals.mdx.

TOPIC is the directory name and behaves like a page key: one or two words,
underscores between them, no spaces and no special characters. Examples:
Following_Planes, Bullet_vs_Explosive, Sept10_Timeline, Erika_Overlaps.

Always 16:9. Always 2K. Every infographic on this site uses that shape so they
sit together consistently on the pages, and 2K is the readable-but-not-enormous
tier for a wide graphic embedded in a Docusaurus page.

=== goals.mdx — what it must contain ===

The first line of real content is the FULL PATH to the page the infographic is
being made for — the file we are targeting, from ~ or from {ROOT_DIR}. If it
targets more than one page, list every one of them.

Then these sections, in this order. Each is a real planning section, not a label:

  * Audience — who is looking at this. What they already believe, what they
    already know, and what they are scanning for.
  * What they should learn — the takeaway, stated as the sentence the reader
    should be able to say out loud after four seconds of looking.
  * Conceptual framing — how we frame it. The metaphor, the structure, the
    shape of the argument the picture makes.
  * What we are educating on — the actual content being taught.
  * Perspective — what the reader gets perspective ON. What they currently
    cannot see that this image makes visible.
  * Polarity and scope — the size of the thing. Are we zooming IN on one
    detail, or widening OUT to show scale? Often both, and the tension between
    the two is the graphic. Say how the zoom level is expressed visually.
  * Numbers — every number that appears, what it means, and how it is
    communicated (a big numeral, a count of repeated marks, a bar, a ratio).
    Numbers we deliberately leave out get named here too.
  * Sizing — what is bigger and what is smaller, and why. Size carries
    importance; state the importance ranking that drives it.
  * Framing and placement — what is frame left, what is frame right, what sits
    higher and what sits lower. What is inside a frame/box/card and what is
    unframed and bleeds. Timelines: say explicitly how time is expressed —
    left-to-right axis, stacked bands, a spiral, converging lines.
  * Screen percentages — roughly what share of the frame each concept takes.
    One concept might be 33%, another 22%. Assign these and reconcile them
    against the frame-left / frame-right decision above.

  These are GENERAL guidelines, not hard constraints. They exist to force the
  planning, not to be obeyed to the pixel.

  * Order of understanding — a NUMBERED list, most important first. Number 1
    introduces the concept and the issue the reader should be trying to
    understand. Number 2 is the first thing they should actually understand.
    Then 3, 4, 5. This ordering is what drives sizing and placement above:
    higher priority gets larger and lands where the eye goes first.
  * On-image text — every word that appears in the image. The title across the
    top, the subline if there is one, section labels, callouts, the source
    line. People scan; the title alone has to tell them what this is about.
    Phrase it deliberately and write the final wording here, not a description
    of the wording.

=== nana_banana_pro_prompt.txt — how to write it ===

Written from goals.mdx, after goals.mdx is finished. It is raw text — the whole
file is sent to the model as the prompt, so no markdown syntax, no headers, no
code fences. Prose and plain lines only.

It must carry everything the model needs: the layout, the framing and placement,
the relative sizing, the percentages, the visual treatment, the timeline
mechanics if there is one, and the EXACT text strings to render, quoted so the
model spells them correctly. State 16:9 in the prompt itself as well as passing
it on the command line.

=== Generating the image ===

  node {NANO_BANANA_4K} \
    {INFO_GRAPHICS_DIR}{topic}/nana_banana_pro_prompt.txt \
    {INFO_GRAPHICS_DIR}{topic}/{topic}.jpg \
    --size 2K --aspect 16:9

The tool defaults to 4K and 16:9, so --size 2K must be passed explicitly.
Uppercase K is required by the API. Model defaults to nano-banana-pro
(gemini-3-pro-image), which is the one that honours 2K/4K.

Once generated, the image is committed like any other site image — see
"Images Are Tracked In Git" above — and embedded by local repo path, never by
an IPFS gateway URL.

Plane flight records have been erased. We are doing a serious investigate to keep documenting when they are claimed on twitter or documented early. But scrubbed and erased later.

We want to track discrpencies in the per flight dir:
~/BGit/Bryan_git/charlie-kirk/site/docs/Planes/{plane}/

We want to store data from each serve we download and indicate in filenames or other ways which source brought the data down. Then see if we can hunt down when data was deleted.

it may have been deleted from the proprietary flight tracker, but available in the open source flight tracker system.

Or the open source flight tracker system may no longer diisplay the data, but the peer-to-peer tools used to collect and report the data may have it.

Or it may be in the waybackmachine.

We want to find and prove when data we removed. And try to get that data back.

See if online if there are backups for this reason.



================================================================================
== File & Directory Map — What Does What ==
================================================================================

A map of the files and directories in this repo that DO something — generators,
registries, charters, pipelines, and master data — as opposed to ordinary
content. Read this before hunting for "where is the thing that builds X".

Paths are relative to {ROOT_DIR} (~/BGit/Bryan_git/charlie-kirk) unless a full
path from ~ is given.


=== Nested CLAUDE.md Charters ===

Several directories carry their OWN CLAUDE.md. These are area charters and they
GOVERN work inside that directory. Read the nested charter before touching
anything in its subtree — the root CLAUDE.md does not repeat their rules.

DIR:
* images/CLAUDE.md: Charter for the image pipeline. Defines IMAGES_YAML,
  PLANNING_DIR, GENERATOR_DIR, PHOTOS_DIR and how they relate.
* image_planning/CLAUDE.md: Charter for the image hierarchy planning pipeline.
  Records that the hierarchy YAML MOVED to images/images.yaml on 2026-07-22 —
  anything still saying "hierarchy_images.yaml" is stale.
* videos_planning/CLAUDE.md: Charter for the video pipeline. Opens with a
  self-check banner: if its first variable line says "image_planning", this file
  was clobbered by a copy from the images side and must be restored. The two
  pipelines are siblings, never copies of each other.
* site/docs/laws/CLAUDE.md: Charter for the four-federal-laws drafting project —
  the Epstein Files Transparency Act (PL 119-38) model, case 251403576, and what
  the laws must force disclosed.
* site/docs/Charlie/CLAUDE.md: Directory tree map for the Charlie section,
  including the Comments/ subtree of per-remark pages.
* site/docs/Planes/following/CLAUDE.md: Charter for the public page-per-location
  follow log. Two rules: everything here is PUBLIC Docusaurus (no scratchpads,
  no raw dumps), and ALL info that can safely be public SHOULD go here — do not
  hold material back for tidiness or because it is only a fragment.
* site/docs/Planes/following/apis/CLAUDE.md: Charter for how flight data is
  actually fetched. Declares the variable block (FLIGHTS_CSV, OVERLAPS_CSV,
  OVERLAP_DIR) used by the four API-source subdirectories.
* site/docs/After/house/CLAUDE.md: Charter for 691 W 925 S St, Orem UT 84058 —
  the staging-house line of inquiry. One .mdx per topic, parent Level 2 = After.


=== Root-Level Master Data Files ===

FILE:
* pages.csv: Master index of every public page. See the "Pages CSV" section
  above for the column contract. ~2 MB — grep it, do not read it whole.
* interesting_pages.csv: Ranked shortlist of the most compelling pages, with a
  why_interesting column holding the single strongest hook for each page and a
  use_count tracking how often it has been surfaced. This is the file to pull
  from when picking what to feature, tweet, or link.
* people.csv: person_key → name → url_path → file_path for every person page
  under site/docs/People/. The lookup table for people cross-linking.
* planes.csv: plane_key, phrase, aliases, target page, aircraft type, operator,
  category, autolink_terms, link_enabled. Drives tail-number autolinking across
  the site — add a row here to make a tail number link itself everywhere.
* planes.yaml: Long-form per-aircraft record (type, program, operator, observed
  behavior). The narrative companion to planes.csv.
* aircraft_costs.csv: Per-tail FAA registration facts (type, year, serial,
  registered owner, status, seats) plus in-production status, nearest comparable
  new aircraft, and today's new-build cost. Feeds the Planes/Aircraft-Costs page
  and answers "who could afford to fly this".
* videos.csv: Every video → its IPFS CID, gateway URL, the page it appears on,
  its Level 2 parent, a not_on_any_page flag, description, and source X URL.
* timeslines.csv: Registry of the "likelihood-of-when" timeline SVGs
  (km-*-timeline.svg) — event_key, event, path to the SVG, and what the curve
  actually claims. Written and consumed by prompts/p_timeline_create.md.
* file_list.yaml: Maps each Large File Bridge "One Repo → Metrics" tile to the
  exact absolute file paths behind it.
* missing_videos.txt: Report of IPFS video embeds on the site whose bytes could
  NOT be pulled from the network and are not in the repo. Broken-evidence list.
* 404_Investigation_Report.txt: Google Search Console 404 investigation for
  whoassassinatedcharliekirk.com — which URLs Google has that the site does not.
* ck_main_progress.txt: Running progress notes on the Level 2 build-out.
* Charlie_Kirk_AI_Inbox.txt: {CK_INBOX}. Append-only staging file for new
  investigation content. AI writes HERE, never to Charlie_Kirk.txt. Bryan merges
  by hand. See the ABSOLUTE RULE at the top of this file.
* .gitignore: Carries a warning banner at the bottom. If ~1,950 per-image lines
  reappear, Large File Bridge re-added them — delete them, do not work around
  them with `git add -f`. See "Images Are Tracked In Git" above.


=== Image Pipeline ===

DIR:
* images/: The image files themselves plus their master data. Tracked in git —
  never gitignore an image.
* images/GPT_Imagine/, images/laws/, images/ico/: Generated/illustrative art —
  law card images, favicons, and GPT-generated law graphics.
* image_planning/generator/: The Python/JS toolchain that turns images.yaml into
  live pages. ~20 scripts, each one stage of the pipeline.

FILE:
* images/images.yaml: {IMAGES_YAML}. Master hierarchy of every image — its
  placement, its cluster, its should_be_on_pages list, and its banned flag.
  Edit programmatically via bind_image_pages.py's emit/recount helpers so the
  file round-trips byte-for-byte.
* images/manifest.yaml: Per-image provenance — filename, IPFS CID, gateway URL,
  source X post URL, source author, description. The chain-of-custody record.
  Note: most CIDs here came from `ipfs add -n` and are NOT retrievable from a
  gateway — serve images from the repo path, keep the CID in data-cid only.
* images/ban_images.csv: {BAN_IMAGES_CSV}. MASTER never-publish list for images.
  See "Banned Media" above. Edits go here, never into images.yaml.
* image_planning/exclude_images.txt: Legacy sha256-per-line never-publish list.
  Still honoured — the ban set is the UNION of this and ban_images.csv.
* image_planning/layout_guidelines.txt: Authoritative standard for how an image
  sits on its Level 5 /Photos page and how big it gets. Every rule in it was
  written after a real visible defect shipped — treat it as a defect log, not a
  style preference.
* image_planning/findings_for_hierarchy.md: Open data/clustering problems in
  images.yaml, raised by page-generation runs that treat the YAML as read-only.
* image_planning/generator/audit_image_publication.py: Repo-wide check that every
  image a visitor should see is actually reachable. Exit 0 clean, 1 broken.
  `--gateway` also probes any remaining ipfs.io <img> embeds. Run by ck_add_text
  at step 9H-6b.
* image_planning/generator/bind_image_pages.py: Binds images to pages and holds
  the emit/recount helpers that keep images.yaml byte-stable.
* image_planning/generator/gen_photos_pages.py: Generates the Level 5 one-image
  pages under site/docs/Photos/, deleting pages for newly banned images.
* image_planning/generator/ban_set.py: Computes the effective ban set (CSV ∪
  exclude_images.txt) that every other stage filters against.
* image_planning/generator/plan_should_be.py / place_should_be_images.py:
  Decide which pages an image SHOULD appear on, then actually place it.
* image_planning/generator/grow_hierarchy.py / update_hierarchy.py /
  fixup_hierarchy.py: Grow, refresh, and repair the images.yaml tree.
* image_planning/generator/add_orphan_images.py: Files images that exist on disk
  but appear in no hierarchy entry.
* image_planning/generator/refresh_pages_csv.py: Re-syncs pages.csv after the
  image pipeline creates or deletes pages.
* image_planning/generator/verify_photos.py / verify_on_pages.py /
  verify_stage_12_13.py: Verification passes for the Photos tree.


=== Video Pipeline ===

DIR:
* videos/: The video files (gitignored — pulled from IPFS) plus their master
  data and .transcription / .ai_description sidecars.
* videos_transcription/: One .md transcript per video, named by the X status ID.
  114 files. This is where to grep for "who said what on video".
* videos_planning/generator/: The Python toolchain for the video pipeline, plus
  its stage report JSONs (stage2/3/10_report.json, verify_report.json) which are
  the audit trail of the last run.

FILE:
* videos/videos.yaml: {VIDEOS_YAML}. Master video hierarchy — the video-side
  twin of images.yaml, carrying placement and the banned flag.
* videos/manifest.yaml: Per-video provenance — filename, CID, gateway URL,
  source X URL, source author, description.
* videos/videos.md: Human-readable video evidence index with access instructions.
* videos/ban_videos.csv: {BAN_VIDEOS_CSV}. MASTER never-publish list for videos.
* videos_planning/exclude_videos.txt: Legacy sha256 never-publish list for
  videos. Union with the CSV, same as the image side.
* videos_planning/generator/emit_yaml.py: The safe programmatic writer for
  videos.yaml — use it instead of hand-editing.
* videos_planning/generator/audit_video_registration.py: Checks every video on
  the site is registered, hosted, and not banned.
* videos_planning/generator/compute_cids.py: Computes IPFS CIDs; hash_cache.json
  caches the expensive hashing between runs.
* videos_planning/generator/harvest_sidecars.py: Pulls .transcription and
  .ai_description sidecars produced by Large File Bridge into the pipeline.
* videos_planning/generator/gen_videos_pages.py / bind_video_pages.py /
  stage56_host_pages.py: Generate and bind the Level 5 video pages.
* videos_planning/layout_guidelines.txt: Video-page layout standard, same role
  as the image one.


=== Site Build & Page Tooling ===

FILE:
* site/_ck_mdxcheck.mjs: Compiles pages exactly the way the real Docusaurus
  build does, so MDX breakage is caught locally. Deliberately does NOT enable
  @slorber/remark-comment — adding it once made every laws/*.md page pass
  locally and fail the deploy. `node site/_ck_mdxcheck.mjs <files...>`.
* site/inject_nav_gallery.py: Idempotently injects two-column nav galleries into
  every non-root overview.mdx under Photos/ and Videos/, between CK_NAV_GALLERY
  markers, above "Related Areas" and below the in-body TOC. Computes real aspect
  ratios from the actual pixels.
* site/sidebars.ts: Navigation structure.
* site/docusaurus.config.ts: Site config — domain, navbar, OG social card.
* .github/workflows/pages.yml: GitHub Pages deploy. The live site is built from
  the REPO, not from any one machine — an untracked image 404s for every visitor.

DIR:
* site/internals/static/img/evidence/: Served evidence images, /img/evidence/<sha>.jpg.
* site/internals/static/img/video_posters/: Video poster frames.
* site/internals/static/img/km-timelines/: The likelihood-of-when timeline SVGs
  registered in timeslines.csv.
* site/internals/static/img/infographics/: Published infographic outputs.
* site/internals/static/court/: Court exhibit assets (bindover/, mirandize/).
* site/internals/static/data/: Site-served datasets, e.g.
  apple-podcast-removed-episodes.csv.
* site/internals/src/: The site's React/CSS layer — custom.css, HomepageFeatures,
  and the 404 page.
* site/Content_Structure/: CS_After.yaml, CS_Before.yaml, Describe.yaml — the
  planned content structure for those Level 2 areas.
* site/keywords/: Per-topic .keywords files (Israel, Media, People, TPUSA,
  Tyler_Robinson) used for search/keyword mapping.
* site/Download_Transcript/: Self-contained transcription tool with its own
  README/USAGE/QUICK_START, a script/ dir, and to_transcribe/ + transcribed_out/
  working directories.


=== Prompts ===

DIR:
* prompts/: The prompt library that drives most site-wide work.
* prompts/four_squares/: The live working state of the four-squares card build —
  ledger.csv, card_index.csv, routes.txt, teasers/, batches/, plus ~15 repair
  scripts. This is a RUN IN PROGRESS, not a finished artifact.
* prompts/2_Level/, prompts/Change_Levels/, prompts/Grow_Content_Structure/,
  prompts/Download_Transcript/: Prompt sets for building Level 2 pages, moving
  pages between levels, growing the content structure, and transcription.
* prompts/backup/: Superseded prompt versions kept for reference.

FILE:
* prompts/Assess_Manual.md: {ASSESS_MANUAL}. The authoritative writing and layout
  guide. Read it into context at the START of any task that creates, edits,
  reviews, or restructures a page.
* prompts/p_4_squares.md: The four-squares card-block system — adds four
  standard blocks to every page. Run by 12 parallel agents.
* prompts/four_squares/AGENT_BRIEF.md: Operational summary handed to each of the
  12 agents running p_4_squares.md.
* prompts/four_squares/RESUME.md: Checkpoint state — pages complete, cards on
  site, teasers banked. Read this to know where the run stopped.
* prompts/four_squares/GOLDEN_EXAMPLE.mdx: The reference output every generated
  page is matched against.
* prompts/p_timeline_create.md: Builds the site-wide likelihood-of-when timeline
  SVGs and their registry rows. Marked DO NOT RUN YET at the top — check that
  line before running it.
* prompts/p_Mirandize.md: The Miranda-timing line of inquiry (the 6:25 PM bodycam
  vs the 8:02 PM identification call).
* prompts/p_more_level_2.txt + prompts/more_level_2.yaml: Mines sources for
  proposed new Level 2 sections and Level 3 pages. The YAML only GROWS and
  nothing in it is applied to the site automatically — it is a proposal queue.
* prompts/grok_write.mdx: Staged writing prompt; the runner passes INPUT_TEXT to
  say what this run focuses on.
* prompts/Create_Topic_Pages.txt / Write_Level_2_page.txt: Page-creation prompts.


=== Planes / Flight Data ===

DIR:
* site/docs/Planes/{TAIL}/: One directory per aircraft. overview.mdx plus a
  data/ subdir (e.g. N1098L/data/adsb/) holding the RAW downloads. Filenames
  must record WHICH SOURCE the data came from, so deletions can be proven.
* site/docs/Planes/following/: The public page-per-location follow log. Governed
  by its own CLAUDE.md.
* site/docs/Planes/following/speaking/: One .mdx per Charlie speaking event,
  named {YYYYMMDD}_{city}.mdx.
* site/docs/Planes/following/overlap/: One directory per plane/person overlap,
  named {YYYYMMDD}_{ST}_{city}_{person}_{NNN}.
* site/docs/Planes/following/apis/: Four data-source lanes — government/,
  proprietary/, public_open_source/, browser_capture/ — each with knowledge.mdx
  (what this source is and what it holds), p_get_data.mdx (the prompt that pulls
  from it), code/, data/, and where applicable requests/ or captures/.
* site/docs/Planes/Aircraft-Costs/, site/docs/Planes/LASAI-Fleet/,
  site/docs/Planes/TPUSA-Aircraft/: Cross-cutting Planes pages — cost analysis,
  the LASAI Aviation II fleet, and TPUSA's own aircraft.

FILE:
* site/docs/Planes/following/flights.csv: The flight records themselves.
* site/docs/Planes/following/overlaps.csv: Computed plane/person overlaps.
* site/docs/Planes/following/airports.csv: Airport reference table.
* site/docs/Planes/following/tpusa_events.csv: TPUSA event dates and locations —
  the ground truth the flights are matched against.
* site/docs/Planes/following/planes.csv: The following-specific plane list
  (distinct from the root planes.csv, which drives autolinking).
* site/docs/Planes/following/Overlap_Window_Definition.mdx: Defines exactly what
  counts as an "overlap". Read it before computing or disputing one.


=== Infographics ===

DIR:
* info_graphics/{Topic}/: One directory per infographic — goals.mdx (the plan),
  nana_banana_pro_prompt.txt (the generation prompt written FROM goals.mdx), and
  the generated .jpg/.png. See the "Infographics" section above.
* info_graphics/Overlap_Timeline/: Also carries generate_overlap_timeline.py —
  a deterministic Python renderer, showing an infographic can be CODE-generated
  rather than model-generated when the data must be exact.


=== IPFS & Large Files ===

DIR:
* IPFS/: Evidence files published to IPFS so they cannot be taken down.
* IPFS/videos/: Large source videos (gitignored) — the Blake Bednarz UVU
  original and its transcription, chain_of_evil.mp4.
* .lfbridge/: Large File Bridge quarantine mirror. Sidecars for files inside
  this repo land here, mirroring the path — e.g. videos/X.mp4 →
  .lfbridge/videos/X.mp4.transcription. Not hand-maintained.

FILE:
* IPFS/ipfs.txt: The pull-and-pin command blocks for every published file.
* IPFS/ipfs.sh: Runnable version of the same — `ipfs pin add <CID>` per file,
  with notes on `ipfs get -o` if you also want the bytes on disk.


=== Research & Private Layer ===

DIR:
* Research/raw/, Research/x_posts/, Research/Topics/, Research/PDFs/,
  Research/evidence/: Raw sources → organized topics → hosted PDFs.
  PDFs we host on a page go in Research/PDFs/.
* knowledge/: Synthesized long-form analysis (FULL_WRITE_UP.md, the per-model
  Big_Write_up_*.md files, INTEL_Connections.md).
* Details/: Private per-person profiles. See the template above.
* ck/people/: Older per-person location, superseded by Details/.
* tmp/: Per-question research runs, one directory per line of inquiry
  (kill_me_research/, future_president_research/, groyper_research/,
  leader_of_churches_research/, ...). tmp/kill_me_research/ holds the KM-01..13
  research files behind the km-*-timeline.svg registry in timeslines.csv.
* analysis/: One-off analyses, e.g. analysis/seo.txt.
* Backup/: STALE — UX design page specs for an unrelated "backup viewer" app
  that drifted into this repo. Not part of the investigation.
* cover_image/: NanoBanana prompts and the generated OG social card. The site's
  docusaurus-social-card.jpg symlinks back to cover_image/cover.jpg.


=== External Tooling (outside this repo) ===

DIR:
* ~/BGit/all/politics/charlie_kirk/: The working/tooling side of this
  investigation. Holds prompts/, research/ (Google_Searches, podcast and Discord
  transcripts, Egyptoin_Flights, Shootings_Political), laws/ (law_fixes.txt,
  thomas_massey/), Letters/ (Tyler, Defense_Attorneys, Amicus), emails/,
  defemation/ (scan output + progress.txt), tweets/, podcasts/, info_graphics/,
  fort_hauchuca/, aiattorney/, ck_Marketing_Videos/, and offline/.
* ~/_Mirror/Politics/Charlie_Kirk_Mi/: Original source media files.
* ~/BGit/Bryan_git/personal_large_files_bridge/_Mirror/Politics/Charlie_Kirk_Mi/:
  The matching transcriptions, AI descriptions, and OCR text for those files.
