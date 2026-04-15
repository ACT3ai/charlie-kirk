---
name: ck_rebalance_level
description: Analyze a Level 2 section of the Charlie Kirk investigation site, propose structural rebalancing (new cluster sub-sections, Level 3 to Level 4 demotions, TOC rebuilds), wait for user approval, then execute the changes.
invocable: true
---

This skill analyzes a Level 2 section and its children, then proposes
structural rebalancing. It does NOT auto-execute. It comes back with a
proposal first. The user reviews, approves, or adjusts. Only then does
it carry out the changes.

The input text ($ARGUMENTS) is flexible:
  * A directory name or path to focus on
  * A description of a problem ("Influencers has too many pages")
  * General guidance ("look at the whole FBI section")
  * A mix of the above
  * Nothing at all (analyze the most obvious candidate)

Whatever text comes in, use it as guidance for where to focus and what
the user sees as the issue. It shapes the analysis but does not replace
the analytical thinking.


============================
MANDATORY: READ THESE FIRST
============================

Before doing ANY analysis, read BOTH of these files fully into context:

ASSESS_MANUAL is file {ROOT_DIR}/prompts/Assess_Manual.md
CK_FILE is file {ROOT_DIR}/Charlie_Kirk.txt

The Assessment Manual defines page structure requirements. The master
investigation file provides the context needed to understand what topics
belong together, what natural clusters exist, and what the investigation
actually covers. You cannot make good rebalancing decisions without both.


============================
DIRECTORY CONTEXT
============================

ROOT_DIR dir is ~/BGit/Bryan_git/charlie-kirk

SITE_DOCS_DIR dir is {ROOT_DIR}/site/docs

SIDEBARS_FILE is file {ROOT_DIR}/site/sidebars.ts


============================
CONTENT HIERARCHY REFRESHER
============================

Level 1: Home page (site root index.md)
Level 2: Category overview pages (overview.md in each topic directory)
          These are the major investigation categories.
Level 3: Individual analysis pages (.md/.mdx files inside a Level 2 dir)
          These are focused sub-topic pages linked from a Level 2 TOC.
Level 4: Pages inside a nested subdirectory under a Level 2.
          The subdirectory has its own overview.md (a sub-Level-2), and
          its children are Level 4 pages. From the parent Level 2's
          perspective, the whole subdirectory is ONE TOC entry.

Example:
  Tyler_Robinson/              <- Level 2
    overview.md                <- Level 2 page
    Travel.md                  <- Level 3
    Recruited.md               <- Level 3
    Girlfriend/                <- sub-Level-2 (cluster topic)
      overview.md              <- sub-Level-2 page
      timeline.md              <- Level 4
      known-contacts.md        <- Level 4
    Trial/                     <- sub-Level-2 (cluster topic)
      overview.md              <- sub-Level-2 page
      hearings.md              <- Level 4
      defense-team.md          <- Level 4

In the parent Tyler_Robinson/overview.md TOC, Girlfriend and Trial each
get ONE entry pointing to their overview. Their internal pages are NOT
listed in the parent TOC.


============================
WHAT REBALANCING MEANS
============================

Rebalancing is about structural reorganization, not just TOC formatting.
The core questions are:

  1. CLUSTER DETECTION: Are there Level 3 pages that naturally cluster
     around a sub-theme? If 4+ pages share a topic thread, they may
     warrant their own sub-Level-2 directory.

  2. DEMOTION: Which current Level 3 pages should become Level 4 pages
     (pushed down into a new cluster subdirectory)?

  3. PROMOTION: Is there content buried on a Level 3 page that deserves
     its own section, or content on the overview that should be a
     Level 3 page?

  4. TOO MANY CHILDREN: A Level 2 with more than ~12 direct Level 3
     pages is hard to navigate. Clustering reduces cognitive load.

  5. TOO FEW CHILDREN: A Level 2 with 0-2 Level 3 pages might be better
     merged into a parent section or filled out with new pages.

  6. MISPLACED CONTENT: Pages that belong under a different Level 2
     entirely.

  7. DUPLICATE COVERAGE: Two pages covering the same sub-topic, or two
     Level 2 directories covering overlapping territory.

  8. TOC COMPLIANCE: After structural changes, does the TOC match the
     Assessment Manual requirements (three-column grid, balanced columns,
     orientation paragraph, three explanatory paragraphs, Related Areas)?


============================
SIGNALS THAT REBALANCING IS NEEDED
============================

When analyzing a Level 2 section, look for these signals:

  * MORE THAN 12 Level 3 pages — the TOC is too long to scan. Group
    related pages into cluster subdirectories.

  * NAMING PATTERNS — if multiple filenames share a prefix (e.g.,
    podcasts-tucker-carlson.md, podcasts-candace-owens.md, podcasts-ian-
    carroll.md), they are a natural cluster.

  * THEMATIC OVERLAP — if you read the Level 3 pages and several are
    really about the same sub-theme from different angles, they should
    share a subdirectory.

  * ORPHAN SUBDIRECTORIES — a subdirectory with an overview.md but zero
    Level 4 pages. Either fill it or flatten it.

  * FAT OVERVIEW — an overview.md with 100+ lines of substantive content
    that should be on Level 3 pages instead.

  * STUB OVERVIEW — an overview.md that is just boilerplate with no
    investigation context.

  * ZERO CHILDREN — a Level 2 with no Level 3 pages at all. Candidate
    for merging or content creation.

  * DUPLICATE DIRECTORIES — two directories covering the same topic
    (e.g., Tyler/ and Tyler_Robinson/, Plane/ and Planes/).


=======================================
PHASE 1: ANALYSIS AND PROPOSAL
=======================================

This phase reads everything, thinks, and presents a proposal. It writes
NOTHING to disk.


STEP 1: PARSE INPUT AND DETERMINE SCOPE

* Read $ARGUMENTS.
* Extract:
    - TARGET: which Level 2 directory (or directories) to analyze.
      If input names a specific dir, use it. If input is a problem
      description, figure out which dir(s) it applies to. If input is
      empty, scan {SITE_DOCS_DIR} for the Level 2 section most in need
      of rebalancing (highest Level 3 count, worst structural compliance).
    - GUIDANCE: any specific concerns, problems, or direction from the
      user's text. This shapes the analysis lens.

* Output:
    ```
    ============================================
    Scope
    ============================================
    Target: {directory or directories}
    User guidance: {summary of input guidance, or "none — general analysis"}
    ============================================
    ```


STEP 2: DEEP INVENTORY

For the target Level 2 directory:

* 2a. List ALL files and subdirectories recursively.

* 2b. For each .md/.mdx file (not overview.md):
    - Read it. Extract: H1, sidebar_label, word count, key topics
      covered, whether it has media (images/video), and a 1-sentence
      content summary.

* 2c. For each subdirectory with overview.md:
    - Read the sub-overview. Count its children.
    - Summarize what the sub-section covers.

* 2d. Read the parent overview.md fully. Tag its sections (frontmatter,
  back button, title, orientation, TOC, body, boilerplate, related areas).

* 2e. Read relevant sections of {CK_FILE} to understand what the
  investigation covers in this topic area. This helps identify:
    - Sub-topics that have pages but could be grouped better
    - Sub-topics in {CK_FILE} that have NO page yet
    - Natural thematic clusters

* Output a structured inventory:
    ```
    ============================================
    Inventory: {dirname}
    ============================================
    Overview word count: {N}
    Level 3 pages: {count}
      {filename} — {title} — {word count} — {1-line summary}
      ...
    Nested sub-sections: {count}
      {subdir}/ — {title} — {child count} children
      ...
    Boilerplate detected: {yes/no — what}
    TOC present: {yes — {format} / no}
    TOC matches disk: {yes / no — {mismatches}}
    Assessment Manual compliance: {list of failing items}
    ============================================
    ```


STEP 3: ANALYZE AND IDENTIFY REBALANCING OPPORTUNITIES

Using the inventory, the user's guidance, the investigation context from
{CK_FILE}, and the Assessment Manual requirements:

* 3a. CLUSTER ANALYSIS: Group the Level 3 pages by thematic similarity.
  Look for natural clusters of 3+ pages that share a sub-theme. Consider
  filename prefixes, content overlap, and investigation topic threads.

* 3b. SIZE ANALYSIS: Is the section too large (>12 direct children)?
  Too small (0-2 children)? Is the overview bloated or a stub?

* 3c. MISPLACEMENT ANALYSIS: Are any Level 3 pages here that really
  belong under a different Level 2? Are any pages from other sections
  that should be here?

* 3d. DUPLICATE ANALYSIS: Are there overlapping pages or overlapping
  Level 2 directories?

* 3e. GAP ANALYSIS: Based on {CK_FILE} content for this topic, are
  there important sub-topics with no Level 3 page at all?

* 3f. STRUCTURAL ANALYSIS: What Assessment Manual requirements are
  failing? (missing TOC, wrong format, no three paragraphs, no
  Related Areas, boilerplate present)


STEP 4: BUILD THE PROPOSAL

Synthesize the analysis into a concrete, actionable proposal. The
proposal has these sections:

  PROPOSAL SECTION 1: NEW CLUSTER SUBDIRECTORIES
  For each proposed new sub-Level-2:
    * Directory name (lowercase-with-hyphens or matching existing
      conventions in the site)
    * What it covers (1-2 sentences)
    * Which existing Level 3 pages move into it (demoted to Level 4)
    * Whether new Level 4 pages should be created (list topics)
    * What its overview.md would contain (brief description)

  PROPOSAL SECTION 2: LEVEL 3 DEMOTIONS TO LEVEL 4
  For each page being moved:
    * Current filename and location
    * New location (which cluster subdirectory)
    * Reason for the move

  PROPOSAL SECTION 3: PAGES STAYING AT LEVEL 3
  List the pages that remain as direct Level 3 children of this Level 2.
  Explain why they stay (they are distinct enough not to cluster, or they
  are the only page on their sub-topic).

  PROPOSAL SECTION 4: SUGGESTED NEW PAGES
  Any Level 3 or Level 4 pages that should be created based on gap
  analysis. Mark these as optional — the user can accept or skip.

  PROPOSAL SECTION 5: MISPLACED OR DUPLICATE CONTENT
  Pages that should move to a different Level 2 entirely, or duplicate
  directories/pages that should be merged or removed.

  PROPOSAL SECTION 6: OVERVIEW PAGE CHANGES
  How the parent overview.md will change:
    * New three-column TOC layout (show the proposed TOC)
    * Boilerplate to remove
    * Orientation paragraph and three paragraphs (new or kept)
    * Related Areas (new or kept)

  PROPOSAL SECTION 7: LINK AND SIDEBAR UPDATES
  What other files need link updates (pages that linked to moved files,
  sidebars.ts changes, etc.)


STEP 5: PRESENT THE PROPOSAL

* Output the full proposal in a clear, readable format.

* End with:
    ```
    ============================================
    AWAITING APPROVAL
    ============================================
    Reply with:
      * "yes" or "approved" — execute the proposal as-is
      * "yes, but [changes]" — execute with your modifications
      * Specific feedback — I will revise the proposal
    ============================================
    ```

* STOP HERE. Do not proceed to Phase 2 until the user responds.


=======================================
PHASE 2: EXECUTION (after user approval)
=======================================

Only enter this phase when the user has approved the proposal (with or
without modifications). If they gave modifications, incorporate them
first.


EXEC STEP 1: CREATE NEW CLUSTER SUBDIRECTORIES

For each new sub-Level-2 directory in the approved proposal:

* Create the directory under {SITE_DOCS_DIR}/{parent_dir}/.

* Create the overview.md for the new sub-Level-2:
    - Frontmatter with sidebar_label
    - Back button pointing to parent Level 2
    - H1 title
    - Orientation paragraph
    - Three-column TOC (from the pages that will live here)
    - Three explanatory paragraphs
    - Related Areas section
    - Follow all Assessment Manual requirements


EXEC STEP 2: MOVE LEVEL 3 PAGES TO NEW LOCATIONS

For each page being demoted to Level 4:

* Move the file: rename from {parent_dir}/{file} to
  {parent_dir}/{cluster_dir}/{file}

* Update the back button on the moved page to point to the new
  cluster overview instead of the parent overview.

* Search ALL files under {SITE_DOCS_DIR} for links pointing to the
  old path. Update each one to the new path. This includes:
    - Other Level 3 pages that cross-linked
    - Overview pages
    - Related Areas sections
    - sidebars.ts


EXEC STEP 3: REBUILD PARENT LEVEL 2 OVERVIEW

Apply the full Assessment Manual structure to the parent overview.md:

* Keep: frontmatter, back button, H1 title
* Remove: all boilerplate
* Build: three-column TOC from the new set of direct children
  (remaining Level 3 pages + new cluster subdirectory overview links)
* Write: orientation paragraph (keep existing if good, write new if stub)
* Write: three explanatory paragraphs (keep existing if good)
* Preserve: substantive body content under ## sub-headings
* Write: Related Areas section


EXEC STEP 4: UPDATE SIDEBARS

* Read {SIDEBARS_FILE}.
* If the restructured directories need sidebar changes, update the file.
* New subdirectories with overview.md should appear in the sidebar
  navigation.


EXEC STEP 5: VERIFY INTEGRITY

* For every .md/.mdx file that was moved or updated:
    - Verify the file exists at its new location
    - Verify its back button points to the correct parent
    - Verify it appears in its parent's TOC

* For every overview.md that was written:
    - Verify every child file is in the TOC
    - Verify no TOC entry points to a non-existent file
    - Verify column balance
    - Verify three paragraphs and Related Areas are present

* Search for any broken links across {SITE_DOCS_DIR} that reference
  old paths of moved files. Fix any found.


EXEC STEP 6: EXECUTION REPORT

* Output:
    ```
    ============================================
    REBALANCE EXECUTED
    ============================================
    New subdirectories created: {count}
      {list with paths}
    Pages moved (Level 3 -> Level 4): {count}
      {old path} -> {new path}
      ...
    Overview pages rewritten: {count}
      {list}
    New overview pages created: {count}
      {list}
    Links updated across site: {count}
    Sidebars updated: {yes/no}
    Broken links found and fixed: {count}
    ============================================
    ```


============================
RULES
============================

* NEVER delete substantive content. Prose, evidence, quotes, timelines,
  analysis, and investigative questions are substantive. Move them to the
  correct structural slot — do not remove them.

* ALWAYS delete boilerplate. The following patterns are boilerplate:
    - "Key Areas" sections with generic bullets like "Evidence collection",
      "Analysis", "Documentation"
    - "Status" sections with empty checkboxes
    - Placeholder text like "This document contains information about..."
    - "Edit this page" footers

* The three-column TOC is the SINGLE SOURCE OF TRUTH for what children
  exist in a directory. Every .md/.mdx file (except overview.md, index.md)
  MUST appear in the TOC. Every subdirectory with an overview.md gets
  ONE entry. No dead links allowed.

* Subdirectory overview.md pages get ONE entry in the parent TOC
  linking to their overview, not individual entries for their children.

* Follow all defamation rules from CLAUDE.md.

* Only write to files under {SITE_DOCS_DIR}. Never touch {CK_FILE}
  (read only). Never touch private research files.

* PROPOSAL FIRST. Never skip to execution without user approval.


============================
COLUMN BALANCING RULES
============================

Distribute entries across three columns left-to-right:

  * Go across: first bullet of each column, then second bullet of each
    column, and so on.
  * If total does not divide evenly by 3:
    - Remainder 1: column 1 gets the extra
    - Remainder 2: columns 1 and 2 each get one extra
  * No column more than one row taller than another.

Examples:
  * 9 items:  3 / 3 / 3
  * 10 items: 4 / 3 / 3
  * 11 items: 4 / 4 / 3
  * 7 items:  3 / 2 / 2
  * 4 items:  2 / 1 / 1
  * < 3 items: use fewer columns accordingly


============================
REQUIRED PAGE STRUCTURE (from Assessment Manual)
============================

Every Level 2 page (including new sub-Level-2 overviews) must have:

  1. FRONTMATTER with sidebar_label
  2. BACK BUTTON at top
  3. H1 PAGE TITLE
  4. ORIENTATION PARAGRAPH (1-2 sentences, immediately after H1)
  5. THREE-COLUMN TOC (grid MDX syntax, balanced columns)
  6. THREE EXPLANATORY PARAGRAPHS (what / substance / next-steps)
  7. BODY CONTENT (if any, under ## sub-headings)
  8. RELATED AREAS (6 links, 2 columns of 3, outside this section)

MDX grid syntax for TOC:

  <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: '1rem'}}>
  <div>

  * [Topic A](./topic-a)

  </div>
  <div>

  * [Topic B](./topic-b)

  </div>
  <div>

  * [Topic C](./topic-c)

  </div>
  </div>

MDX grid syntax for Related Areas:

  ## Related Areas

  <div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
  marginTop:'0.5rem'}}>
  <div>

  * [Link 1](../path)
  * [Link 2](../path)
  * [Link 3](../path)

  </div>
  <div>

  * [Link 4](../path)
  * [Link 5](../path)
  * [Link 6](../path)

  </div>
  </div>


============================
TOC ENTRY LABELING
============================

Each TOC bullet label should be:

  * The page's sidebar_label or H1 if clear and descriptive
  * A short phrase (4-8 words) if the title is vague
  * Enough to understand the sub-topic WITHOUT clicking

For cluster subdirectory entries, label with the cluster topic name.


============================
EDGE CASES
============================

* Section has ZERO Level 3 pages: still analyze. Propose whether it
  should be merged into another Level 2 or filled with new pages.

* Section has 1-2 Level 3 pages: probably does not need clustering.
  Focus on TOC compliance and whether the section should be merged.

* Input text is empty: scan all Level 2 directories and pick the one
  most in need (highest child count, worst compliance, most obvious
  clustering opportunity). Tell the user which one you picked and why.

* User says "all": analyze the top 3-5 most needy sections and present
  proposals for each. Do not try to rebalance 90 sections at once.

* Duplicate directories (e.g., Tyler/ and Tyler_Robinson/): flag this
  prominently in the proposal. Recommend which one to keep.

* User provides guidance that conflicts with the analysis: present both
  your recommendation and the user's preference, explain the tradeoff,
  and let them decide.


============================
IMPORTANT
============================

* If the symlink ~/.claude/commands/ck_rebalance_level.md does not exist,
  ask the user:
  "The ck_rebalance_level skill symlink is not installed. Create it? (y/n)"
  If yes, run:
    ln -s ~/BGit/Bryan_git/charlie-kirk/skills_storage/ck_rebalance_level.md ~/.claude/commands/ck_rebalance_level.md

* ALWAYS read {ASSESS_MANUAL} and {CK_FILE} before doing any analysis.
  The manual defines structure. The investigation file defines content
  context. Both are required for good rebalancing decisions.

* ALWAYS present a proposal and wait for approval before writing any
  files. This is a two-phase skill: analyze then execute.

* This skill writes to files under {SITE_DOCS_DIR} during execution
  phase only. It reads {CK_FILE} for context but never modifies it.

* When in doubt about whether to cluster or leave flat, lean toward
  clustering when there are 4+ pages on the same sub-theme. Lean toward
  flat when pages are each genuinely distinct topics.

* When in doubt about whether content is substantive or boilerplate,
  keep it. Better to preserve something unnecessary than delete
  something valuable.
