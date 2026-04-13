---
name: ck_add_text
description: Add new text/notes to the Charlie Kirk investigation file — finds the right section or creates a new one, never removes existing content
invocable: true
---

This skill has two modes. Read $ARGUMENTS to decide which mode to run.

  IMPROVE MODE — triggered when the argument mentions improving, fixing, assessing,
  or upgrading pages. Examples:
    * "improve all"
    * "improve all FBI pages"
    * "fix one page"
    * "assess the CoverUp overview"
    * "bring all pages up to standard"
    * "improve [any directory or page name]"

  ADD TEXT MODE — triggered when the argument is new text, a URL, a quote, a note,
  or anything else that is raw investigation content to be stored.

If IMPROVE MODE is detected, skip to the IMPROVE MODE section below.
If ADD TEXT MODE is detected (or the mode is ambiguous), continue with the add-text
flow immediately below.


============================
ADD TEXT MODE
============================

You are helping the user add new information to the Charlie Kirk investigation file.

The user provides text content as an argument: $ARGUMENTS

This text may come from an X post, a news article, a transcript, personal notes,
or any other source. Your job is to insert it into the correct place in the file,
preserving all existing content.


============================
DIRECTORY CONTEXT
============================

ROOT_DIR dir is ~/BGit/Bryan_git/charlie-kirk

This is the Charlie Kirk assassination investigation repo (September 10, 2025,
Utah Valley University). It has two layers:

  * Private layer: everything OUTSIDE of {ROOT_DIR}/site/ — research notes,
    people profiles, raw data, prompts, PDFs, and the master investigation file.
    This content is never published to the website.

  * Public layer: everything INSIDE {ROOT_DIR}/site/ — the Docusaurus static
    site published at https://whoassassinatedcharliekirk.com.

Key directories:
  {ROOT_DIR}/Charlie_Kirk.txt     — Master investigation file (this skill's target)
  {ROOT_DIR}/Details/             — Private people profiles, one subdir per person
  {ROOT_DIR}/Research/            — Raw research (PDFs/, raw/, Topics/)
  {ROOT_DIR}/knowledge/           — Synthesized write-ups and analysis
  {ROOT_DIR}/Prompts/             — AI generation prompts
  {ROOT_DIR}/site/docs/           — Public Docusaurus pages (302+ files)
  {ROOT_DIR}/skills_storage/      — Skill source files (symlinked to ~/.claude/commands/)

CK_FILE is file {ROOT_DIR}/Charlie_Kirk.txt


============================
RULES
============================

* NEVER remove, delete, or reduce any existing text in {CK_FILE}. This skill
  only GROWS the file. Every character that existed before must still exist after.

* NEVER rewrite, rephrase, or "clean up" existing content. Existing text stays
  exactly as-is, typos and all.

* The new text you insert should be lightly formatted to match the style of the
  file (plain text, no markdown headers, asterisk bullets if needed) but preserve
  the user's words and meaning.

* If the user provides a source URL, include it on its own line near the top of
  the inserted block.


============================
SECTION FORMAT
============================

The file uses equal-sign section headers. The pattern is:

    (blank line)
    =============== Section Title ==================
    (content lines)
    (blank line before next section)

The number of equal signs varies slightly but aim for roughly this pattern:
  * At least 12 equal signs before the title
  * At least 12 equal signs after the title
  * A space between the equal signs and the title text
  * One blank line before the header line
  * Content starts on the next line after the header
  * One or more blank lines before the next section header


============================
STEPS
============================

STEP 1: Read the file
* Read {CK_FILE} fully. Note every section header and its line number.
* Build a mental list of sections and their topics.

STEP 2: Analyze the new text
* Determine the topic(s) of the text the user wants to add.
* Identify which existing section is the best match.
* If no existing section is a reasonable match, decide on a new section title.

STEP 3: Decide placement
* If an existing section matches:
  - Insert the new text at the END of that section (before the blank lines
    that precede the next section header).
  - Do NOT insert in the middle of existing content.
* If creating a new section:
  - Place it immediately AFTER the most related existing section.
  - MANDATORY: Before writing any content, FIRST insert a section header line
    using the equal-sign format. Example:
      =============== Your Section Title ==================
    The header MUST appear before any new content. Never add content without
    its own section header when creating a new section.
  - Choose a short, descriptive title matching the style of existing headers.

STEP 4: Insert the text
* Use the Edit tool to insert text. The edit must be purely additive.
* After editing, verify that:
  - No existing text was removed or changed.
  - The new text appears in the correct location.
  - Section header formatting is consistent with the rest of the file.

STEP 5: Confirm to the user
* Tell the user:
  - Which section the text was added to (existing or new).
  - The line number range of the insertion.
  - A one-line summary of what was added.


============================
IMPROVE MODE
============================

ASSESSMENT MANUAL
-----------------
ASSESS_MANUAL is file ~/BGit/Bryan_git/charlie-kirk/prompts/Assess_Manual.md

Read the assessment manual fully before touching any page. Every fix you make must
satisfy the rules in that file. The manual is the authority. This section summarizes
the rules for quick reference but the manual takes precedence.

SITE_DOCS_DIR is dir ~/BGit/Bryan_git/charlie-kirk/site/docs/

Pages are organized as:
  * Level 2: {SITE_DOCS_DIR}/{TopicDir}/overview.md
  * Level 3: {SITE_DOCS_DIR}/{TopicDir}/{specific-page}.md

SCOPE PARSING — decide which pages to process based on $ARGUMENTS:

  * "improve all" or "all pages" or "every page"
      → collect every overview.md (Level 2) and every other .md (Level 3)
        under {SITE_DOCS_DIR}, excluding index.md at root.
  * "improve all {TopicDir} pages" or "fix {TopicDir}"
      → collect all .md files inside {SITE_DOCS_DIR}/{TopicDir}/.
  * "improve [one page]" or a specific file name / path
      → process that single page only.
  * "improve overview pages" or "all level 2"
      → collect every overview.md across all topic directories.
  * "improve level 3" or "all detail pages"
      → collect every non-overview .md under each topic directory.

When the scope is large (more than 10 pages), tell the user the count and ask:
  "Found {N} pages to improve. Process all at once, or start with {TopicDir} first?"
Proceed when they confirm.

IMPROVE STEPS FOR EACH PAGE
----------------------------

For every page in scope, run these steps in order:

IMPROVE STEP 1: Read the page
  * Read the full file. Identify whether it is Level 2 (overview.md) or Level 3.

IMPROVE STEP 2: Run the checklist
  * Apply the checklist from the assessment manual for the page's level.
  * List every failing item. If all items pass, output "PASS — no changes needed"
    for this page and skip to the next.

IMPROVE STEP 3: Fix each failing item — do not skip any
  Level 2 fixes (apply all that are needed):
    [ ] Missing or bad orientation paragraph → add one or two sentence intro.
    [ ] Missing three-column TOC → build it from the Level 3 pages that exist
        in this directory. Link to actual existing files only.
    [ ] TOC columns unbalanced → redistribute bullets left-to-right.
    [ ] Prose before the TOC → move it to after the TOC.
    [ ] Missing three explanatory paragraphs after TOC → write them (what /
        substance / next steps). Do not duplicate TOC bullet text.
    [ ] Missing or wrong Related Areas section → add or fix it (6 links,
        2 columns of 3, pointing outside this section).

  Level 3 fixes (apply all that are needed):
    [ ] Missing back button → add it at the very top using the MDX button pattern.
    [ ] Back button links to wrong page → correct the href.
    [ ] No sub-headings → add ## sub-headings to break up the content.
    [ ] Unsourced factual claims → add inline "(source needed)" flags or known
        source links.
    [ ] Living person, defamation violations → rewrite to use attribution language
        ("reportedly", "according to", "allegedly"). Never state as fact that a
        living person committed a crime unless court-proven.
    [ ] Missing Status field on a person profile page → add Status: Alive /
        Deceased (YYYY) / Unknown.
    [ ] Media items wider than 48% or not floated right → fix inline styles.
    [ ] Missing clearfix after last media item → add the clearfix div.
    [ ] Missing or wrong Related Areas section → add or fix it.
    [ ] Page is a .typ file → note this to the user; do not rename files, but
        alert them to convert to .mdx or .md.

  Both levels:
    [ ] Broken internal links → fix the path to match the actual file location.
    [ ] Unclosed MDX tags or rendering issues → close/fix them.

IMPROVE STEP 4: Write the updated file
  * Use the Edit tool (preferred) or Write tool for larger rewrites.
  * Never remove existing body content. Only add missing structure (TOC, back
    button, paragraphs, Related Areas) or rewrite violating sentences in place.
  * Keep the existing page title (H1) exactly as-is.

IMPROVE STEP 5: Report for this page
  * Output a one-line summary:
      FIXED {file_path} — {comma-separated list of items fixed}
    or
      PASS {file_path} — no issues found

IMPROVE STEP 6: Move to next page, repeat until all pages in scope are done.

FINAL IMPROVE REPORT
--------------------
After processing all pages, output a summary table:

  Pages assessed:  {N}
  Pages fixed:     {N}
  Pages passed:    {N}
  Items fixed:     {list each fix type and how many times it was applied}

If any pages could not be fully fixed (e.g., a .typ extension, a linked page that
does not exist), list them separately under "Needs Manual Attention".

IMPROVE MODE CONSTRAINTS
------------------------
  * Never delete body content that conveys factual information.
  * Adding structure (TOC, back button, paragraphs, Related Areas) is always safe.
  * Rewriting a sentence for defamation safety is required for living persons —
    rewrite the minimum needed; do not paraphrase the whole page.
  * Do not create new Level 3 pages — only fix existing ones and add links to
    pages that already exist.
  * Do not change the Docusaurus front matter (title, sidebar_label, etc.) unless
    it is clearly wrong or missing.
  * Only write to files under {SITE_DOCS_DIR}. Do not touch private files, the
    master Charlie_Kirk.txt, or anything outside the site/docs/ tree.


============================
EXISTING SECTIONS (reference)
============================

These are the major sections currently in the file (for quick reference during
topic matching). Always re-read the file for the current list since it grows
over time.

* SUPER Strange events
* Strange events
* Accoustics shows direction of bullet
* Timeline
* Court Case
* WhiteHouse
* Israel
* Day of Shooting
* Mossad Quotes World Stage Puppet Master
* Mic Explode pulls shirt
* Gun Mauser Model 98
* Tylers Backpack
* Tylers Timeline that day and clothes
* Tylers Clothing
* Coincidences or NOT (Right after death)
* Quotes OTHER
* Quotes Charlies / Verified
* They were going to kill him TOMORROW
* Quotes from Charlie
* Quotes from NON-CHARLIE
* Rick Cutler : Hand Trigger
* FBI Cover up
* Ballistics: FBI CBLA Test
* Shawn Sipes / Blake
* SUV Destroyed
* Tyler Robinson did not turn himself in
* MiniVan / SUV: Back Hatch : Tyler M Sipes
* Judges
* 3419 S River Road
* N1098L
* FBI Blocking Investigations
* Phil Lyman
* Other Suspect. Roof top? construction site?
* Charlie Quotes
* Landscaping cement under Tent / UVU
* Monopod Camera / Truck
* Terryl (Fonsworth?) / Michael Olbert
* Tyler Clothing changes
* SAM Flight
* SU-BTT Plane
* N1098
* Stairs Guy and Backpack prove not him
* Tyler trip after assassination


============================
IMPORTANT
============================

* If the symlink ~/.claude/commands/ck_add_text.md does not exist, ask the user:
  "The ck_add_text skill symlink is not installed. Create it? (y/n)"
  If yes, run:
    ln -s ~/BGit/Bryan_git/charlie-kirk/skills_storage/ck_add_text/ck_add_text.md ~/.claude/commands/ck_add_text.md

* In ADD TEXT MODE: this skill writes only to {CK_FILE}. All other files are
  read-only.

* In IMPROVE MODE: this skill writes only to files under {SITE_DOCS_DIR}
  (~/BGit/Bryan_git/charlie-kirk/site/docs/). {CK_FILE} and all private files
  outside site/ are read-only.
