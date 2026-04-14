ROOT_DIR dir is ~/BGit/Bryan_git/charlie-kirk

CK_FILE is file {ROOT_DIR}/Charlie_Kirk.txt

SITE_DIR dir is {ROOT_DIR}/site

CHARLIE_KIRK_FILE is file ~/Library/CloudStorage/Dropbox/Bryan/Personal/Politics/Charlie_Kirk/Charlie_Kirk.txt


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
in skills_storage/. For each .md file found under {ROOT_DIR}/skills_storage/*/*.md:

  1. Check if ~/.claude/commands/{filename} exists and is a symlink pointing to
     the correct file under skills_storage/.
  2. If the symlink is missing or broken, tell the user:
       "Skill '{skill_name}' is not linked. Create symlink at
        ~/.claude/commands/{filename} -> {ROOT_DIR}/skills_storage/{dir}/{filename}?"
  3. If the user says yes, create the symlink:
       ln -s {ROOT_DIR}/skills_storage/{dir}/{filename} ~/.claude/commands/{filename}
  4. If ~/.claude/commands/ does not exist, create it first: mkdir -p ~/.claude/commands/

This ensures anyone who clones the repo gets prompted to set up skills on their
machine without manual steps.

=== Active Skills ===

  * /ck_add_text {text}        - Add new text/notes to {CK_FILE}. Finds the
                                  right section or creates a new one. Never
                                  removes existing content. The file only grows.
                                  Source: skills_storage/ck_add_text/ck_add_text.md
                                  Symlink: ~/.claude/commands/ck_add_text.md


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


~/BGit/Bryan_git/charlie-kirk/prompts/Assess_Manual.md
This is the assessment manual. This is what we're going to assess everything against.

That will be the writing skill. That will mean what pages are laid out this way or that way. Always read this into the context menu, making sure we're aligning pages with these guidelines.


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

