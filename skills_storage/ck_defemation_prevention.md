---
name: ck_add_text
description: Add new text/notes to the Charlie Kirk investigation file — finds the right section or creates a new one, never removes existing content
invocable: true
---

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

* This skill is READ-ONLY on all files except {CK_FILE}. Do not modify any
  other file.
