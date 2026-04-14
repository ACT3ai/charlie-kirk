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

After the three-column list, every Level 2 page must have exactly three paragraphs that
explain the area in depth. These paragraphs come after the TOC, never before it. Think of
them as the "why this matters" body of the page — once a reader has scanned the TOC and
may not have clicked yet, these paragraphs give them enough context to understand the
section and confirm they are in the right place.

Guidelines for the three paragraphs:
  * Paragraph 1: What this area covers and why it is significant to the investigation.
  * Paragraph 2: The key evidence, patterns, or findings in this area — the substance.
  * Paragraph 3: What the reader should do next — which Level 3 pages to prioritize,
    or what questions this area is trying to answer.
  * Each paragraph: three to five sentences. No bullet lists inside these paragraphs.
  * Do not restate the bullet labels from the TOC verbatim — add new context and depth.

After the three paragraphs, every Level 2 page must end with the Related Areas section
(see RELATED AREAS SECTION below).

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
* Status field required for any person profile page: Alive / Deceased (YYYY) / Unknown.

--- Back button ---

At the very top of every Level 3 page, immediately before any content, include a
back-navigation button that reads as the Level 2 topic name this page belongs to.
Clicking it returns the reader to the parent Level 2 overview page.

Use this MDX pattern (replace label and path as appropriate):

  <a href="../overview" style={{display:'inline-block', marginBottom:'1rem',
  padding:'0.35rem 0.9rem', background:'#1a73e8', color:'#fff',
  borderRadius:'4px', textDecoration:'none', fontSize:'0.9rem'}}>
  ← FBI Cover-Up
  </a>

The label should be the short title of the Level 2 area, prefixed with a left arrow.
Do not use a plain markdown link — it must render as a button so it is visually distinct
from body text.

--- Images and video on Level 3 pages ---

Level 3 pages may include up to three media items (images, real video files, or
YouTube embeds). Each media item:

  * Floats to the RIGHT half of the center content column only.
  * Body text wraps around the left side of the media.
  * Maximum width: 48% of the center content area. Never wider than half.
  * Never use .typ files — too rigid. Use .mdx (preferred) or .md with MDX enabled.

Float-right pattern for an image:

  <img src="/img/some-image.jpg"
    style={{float:'right', width:'48%', marginLeft:'1.5rem', marginBottom:'1rem'}}
    alt="Description of image" />

Float-right pattern for a YouTube embed:

  <div style={{float:'right', width:'48%', marginLeft:'1.5rem', marginBottom:'1rem'}}>
  <iframe width="100%" style={{aspectRatio:'16/9'}}
    src="https://www.youtube.com/embed/VIDEO_ID"
    frameborder="0" allowfullscreen />
  </div>

Float-right pattern for a local video file:

  <video controls style={{float:'right', width:'48%',
    marginLeft:'1.5rem', marginBottom:'1rem'}}>
    <source src="/video/some-file.mp4" type="video/mp4" />
  </video>

After the last media item on a page, add a clearfix so the next section starts below
all floated content:

  <div style={{clear:'both'}} />

Every Level 3 page must end with the Related Areas section (see RELATED AREAS SECTION below).


============================
RELATED AREAS SECTION
============================

Every Level 2 and every Level 3 page must end with a "Related Areas" section. This
appears at the very bottom of the page, after all body content.

Layout: six links arranged in two columns, three per column. Left column on the left,
right column on the right.

  ## Related Areas

  <div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem',
  marginTop:'0.5rem'}}>
  <div>

  * [Phrase for Link 1](../path/to/page)
  * [Phrase for Link 2](../path/to/page)
  * [Phrase for Link 3](../path/to/page)

  </div>
  <div>

  * [Phrase for Link 4](../path/to/page)
  * [Phrase for Link 5](../path/to/page)
  * [Phrase for Link 6](../path/to/page)

  </div>
  </div>

Rules for choosing the six links:

  * Mix Level 2 and Level 3 destinations — do not use all of one type.
  * Do NOT link to pages within the current Level 2 section (those are already in
    the TOC or body). Jump to a different part of the site tree.
  * Lean toward pages that have few inbound links from other pages — this spreads
    link equity across the site and surfaces under-linked content.
  * Choose pages that share a thematic connection to the current page but come from
    a different angle — a reader who finished this page would likely find value there.
  * Phrase each link as a short, descriptive label (4-8 words). Not the raw page title
    if the title is vague — write a phrase that makes the destination clear.
  * Never use "click here" or generic labels. Every phrase must communicate the destination.

How to identify low-inbound-link pages:
  * Pages that are only reachable from one TOC are candidates.
  * Pages that are new or recently created are likely low-linked.
  * Pages that are deep in a rarely-visited section are candidates.
  * Prefer linking to these over linking to pages that already appear prominently
    in the navbar or the home page panels.

Do not list the same destination in Related Areas on two adjacent pages.


============================
PAGE CONTENT AUDIT CHECKLIST
============================

When assessing any page, go through each item:

Level 2 checklist:
  [ ] Opens with a short orientation paragraph (1-2 sentences).
  [ ] Three-column bullet list (TOC) present immediately after the orientation paragraph.
  [ ] Every existing Level 3 page in this section is linked from the TOC.
  [ ] TOC bullet phrases are clear enough to know the sub-topic without clicking.
  [ ] No missing sub-topics — all sub-areas a reader would expect are represented.
  [ ] No bullets in the TOC that point to non-existent or placeholder pages.
  [ ] Column heights are equal or off by at most one row.
  [ ] Bullets are distributed left-to-right to maintain balance.
  [ ] After the TOC: exactly three explanatory paragraphs (what, substance, next steps).
  [ ] Three paragraphs do not duplicate TOC bullet labels — they add context and depth.
  [ ] Related Areas section at the bottom: 6 links, two columns of three.
  [ ] Related Areas links jump to a different section of the site, not this section.
  [ ] Related Areas includes a mix of Level 2 and Level 3 destinations.
  [ ] No wall of prose before the three-column TOC.

Level 3 checklist:
  [ ] Back button at the very top linking to the parent Level 2 overview page.
  [ ] Back button label is the Level 2 topic name, prefixed with a left arrow.
  [ ] Gets straight to the specific sub-topic — no broad site overview rehash.
  [ ] Sub-headings break up the content into clear sections.
  [ ] All factual claims attributed to a source.
  [ ] Living persons: defamation-safe language throughout (see CLAUDE.md).
  [ ] Status field present on any person profile page.
  [ ] Media items (if any): max three, each floated right at 48% width, text wraps left.
  [ ] No .typ files — use .mdx or .md with MDX enabled.
  [ ] Clearfix div after the last media item.
  [ ] Related Areas section at the bottom: 6 links, two columns of three.
  [ ] Related Areas links jump to a different section of the site, not the current one.
  [ ] Related Areas includes a mix of Level 2 and Level 3 destinations.
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
  * Is every existing Level 3 page in this section linked from the TOC?
  * Are TOC bullet phrases specific enough — short, descriptive, unambiguous?
  * Do the three explanatory paragraphs cover what, substance, and next steps?
  * Do the paragraphs add depth beyond what the TOC bullets already communicate?

For every Level 3 page, ask:
  * Is this the right home for this content, or does it belong under a different Level 2?
  * Does the page cover the full scope of its sub-topic, or is it thin?
  * Is the page doing too much — should it be split into two Level 3 pages?
  * Does the back button exist and point to the correct Level 2 overview?
  * Are media items (if present) floated right at max 48% width with text wrapping left?
  * Do the Related Areas links go outside the current section to under-linked pages?


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


============================
WRITING STYLE ON PAGES
============================

The page will often have this boilerplate template below content. Assume that we want to get rid of that, but look at those and analyze if we really need them or not. 



Key Areas
Podcast episodes
Host analysis
Coverage quality
Evidence presented
Audience reach
Status
 Initial research
 Evidence collection
 Analysis
 Documentation
Edit this page

