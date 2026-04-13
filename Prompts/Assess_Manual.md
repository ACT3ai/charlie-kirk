This is the assessment manual. This is what we're going to assess everything against.
Every page on the site — level 2 and level 3 — must be evaluated against these rules before
it is considered complete.


============================
SITE CONTENT HIERARCHY
============================

Level 1: Home page
  * The root landing page.
  * Has three-column panels linking into Level 2 areas.
  * Each panel represents a major investigation category.

Level 2: Category overview pages (overview.md in each topic directory)
  * Reached from the home page panels or the left sidebar when you enter an area.
  * Purpose: orient the reader and let them self-select into what they care about.
  * Must have the three-column bullet list (see below).

Level 3: Individual analysis pages (specific .md files inside topic directories)
  * Reached by clicking a bullet in a Level 2 three-column list.
  * Purpose: deliver focused information on one specific sub-topic.
  * Must get straight to the point. No broad overview rehash.
  * Must have links off to related Level 2 or Level 3 pages at the bottom.


============================
LEVEL 2 PAGE REQUIREMENTS
============================

Every Level 2 page must open with a brief one- or two-sentence orientation paragraph,
then immediately present the three-column bullet list.

The three-column list is the primary navigation mechanism on a Level 2 page. Its job
is to let a reader scan quickly, spot what they care about, and click through.

* Each column is a bullet list of Level 3 page links.
* Each bullet is a short phrase or title — enough to understand the sub-topic.
* Bullets may have a one-line sub-description if needed for clarity, but keep it tight.
* The three columns must be the same height, plus or minus one row.
* Distribute entries left-to-right across columns as you add them so that column
  heights stay balanced. Do not fill column one before starting column two.
* If the total count does not divide evenly by three, put the extra item in column one,
  then column two — never leave column three taller than the others.

After the three-column list, a Level 2 page may have a short "About this section"
paragraph and links to related Level 2 areas, but the three-column list always comes first.

Docusaurus MDX syntax for three equal columns:

  <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: '1rem'}}>
  <div>

  * [Topic A](./topic-a)
  * [Topic B](./topic-b)
  * [Topic C](./topic-c)

  </div>
  <div>

  * [Topic D](./topic-d)
  * [Topic E](./topic-e)
  * [Topic F](./topic-f)

  </div>
  <div>

  * [Topic G](./topic-g)
  * [Topic H](./topic-h)
  * [Topic I](./topic-i)

  </div>
  </div>

Balance check: count bullets in each column after drafting. If any column is more than
one row taller than another, move the last bullet of the tall column to the top of the
next column.


============================
LEVEL 3 PAGE REQUIREMENTS
============================

* Open directly with the substance — no long preamble, no re-stating the site theme.
* Structured with clear sub-headings for each major point or category of evidence.
* Every factual claim attributed to a source (link or inline citation).
* Defamation rules apply for any living person (see CLAUDE.md).
* At the bottom: a "Related Pages" or "See Also" section with three to six links to
  other Level 2 or Level 3 pages the reader is likely to want next.
* Status field required for any person profile page: Alive / Deceased (YYYY) / Unknown.


============================
PAGE CONTENT AUDIT CHECKLIST
============================

When assessing any page, go through each item:

Level 2 checklist:
  [ ] Opens with a short orientation paragraph (1-2 sentences).
  [ ] Three-column bullet list present and links to Level 3 pages.
  [ ] Column heights are equal or off by at most one row.
  [ ] Bullets are distributed left-to-right to maintain balance.
  [ ] Each bullet label is clear enough to know the sub-topic without clicking.
  [ ] After the list: optional short "About this section" and related-area links.
  [ ] No wall of prose before the three-column list.

Level 3 checklist:
  [ ] Gets straight to the specific sub-topic — no broad site overview rehash.
  [ ] Sub-headings break up the content into clear sections.
  [ ] All factual claims attributed to a source.
  [ ] Living persons: defamation-safe language throughout (see CLAUDE.md).
  [ ] Status field present on any person profile page.
  [ ] "Related Pages" section at the bottom with 3-6 links.
  [ ] Does not duplicate content that belongs on a different Level 3 page.

Both levels:
  [ ] Page title and file name match the sub-topic focus.
  [ ] Internal links use correct Docusaurus relative paths.
  [ ] No broken links.
  [ ] No markdown rendering issues (escaped characters, unclosed tags).


============================
BALANCING THE THREE COLUMNS — WORKED EXAMPLE
============================

If you have 10 bullets to place across three columns:
  Column 1: 4 bullets  (gets the extra one)
  Column 2: 3 bullets
  Column 3: 3 bullets

If you have 11 bullets:
  Column 1: 4 bullets
  Column 2: 4 bullets
  Column 3: 3 bullets

If you have 9 bullets:
  Column 1: 3 bullets
  Column 2: 3 bullets
  Column 3: 3 bullets

When placing bullets, go across: first bullet of each column, then second bullet of
each column, and so on. This way if you stop mid-row, columns are naturally even.


============================
CONTENT COVERAGE AUDIT
============================

For every Level 2 page, ask:
  * Does this section have all the sub-topics a reader would expect to find here?
  * Are any sub-topics missing that deserve a Level 3 page?
  * Are any sub-topics covered here that actually belong under a different Level 2?
  * Is every existing Level 3 page in this section linked from the three-column list?

For every Level 3 page, ask:
  * Is this the right home for this content, or does it belong under a different Level 2?
  * Does the page cover the full scope of its sub-topic, or is it thin?
  * Are there closely related Level 3 pages that should be cross-linked?
  * Is the page doing too much — should it be split into two Level 3 pages?


============================
WRITING STYLE ON PAGES
============================

* Plain, direct writing. No filler phrases.
* Active voice preferred.
* Short paragraphs — three to five sentences max before a new sub-heading or break.
* Bullet lists for evidence, timelines, and enumerated facts.
* Bold for key names, dates, and terms on first use in a section.
* No markdown headers above H2 (##) inside page body — H1 is the page title only.
* No emojis unless explicitly requested.
