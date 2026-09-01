================================================================================
== CHARTER — site/docs/people_analysis/  ("People's Analysis")
================================================================================

THIS_DIR dir is ~/BGit/Bryan_git/charlie-kirk/site/docs/people_analysis/
ROOT_DIR dir is ~/BGit/Bryan_git/charlie-kirk
SITE_DIR dir is {ROOT_DIR}/site

This is a LEVEL 2 directory. Its overview.mdx is the Level 2 page. Everything
else in here is a LEVEL 3 page, and there is ONE LEVEL 3 PAGE PER PERSON.

Display name: "People's Analysis"
Directory name: people_analysis  (the display name with no spaces, no
apostrophe, no special characters — lowercase with an underscore)


================================================================================
WHAT THIS SECTION IS
================================================================================

One page per person who gives their opinion on what happened to Charlie Kirk.

Each Level 3 page carries that ONE person's analysis: who they are, the video
or videos in which they give it, the transcript of what they actually said, and
a plain summary of the position they are taking. The page is a record of THEIR
view. It is not the site's view.

People get to give their opinion here. That is the entire point of the section.
We are not the arbiter of whether they are right.


================================================================================
!! THE DISCLAIMER — REQUIRED ON EVERY PAGE IN THIS DIRECTORY !!
================================================================================

overview.mdx AND every Level 3 page carries the disclaimer. No exceptions, and
no page ships without it.

The substance it must convey, in these words or very close to them:

    These are only people's opinions. We do want them to be able to give their
    opinions. This website does not take any stand behind them being true — but
    we do want people to challenge them and think about whether they are true
    or not.

Place it near the TOP of the page, above the analysis, where a reader cannot
miss it and cannot mistake the person's claims for the site's findings.

WHY IT MATTERS: the pages in this section carry serious allegations about
living people and organizations. The disclaimer plus attribution language is
what makes it safe and honest to host them. A page here that reads as though
the SITE is asserting the claim is a defect, not a style preference.


================================================================================
ATTRIBUTION IS MANDATORY — NEVER WRITE A CLAIM IN THE SITE'S VOICE
================================================================================

Every substantive claim on a page in this directory is attributed to the person
whose page it is, in the sentence itself:

    GOOD: PB says he believes Tyler Robinson's life was infiltrated.
    GOOD: In his view, TPUSA was a target of a takeover.
    GOOD: He alleges, without presenting documentary evidence, that ...
    BAD:  Tyler Robinson's life was infiltrated.
    BAD:  TPUSA was the target of a takeover.

Follow the site-wide defamation rules in {ROOT_DIR}/CLAUDE.md in full. For any
LIVING person named inside someone's opinion: never state as fact that they
committed a crime unless it is court-proven. Say who is making the claim, say
it is a claim, and where a denial or counter-argument exists, include it.

Where a speaker's factual premise is checkable and known to be contested, say
so in a short editorial note marked clearly as the site's note, not theirs.


================================================================================
LEVEL 3 PAGE STRUCTURE (one per person)
================================================================================

  1. Back button to /people_analysis/overview
  2. H1 — the person's name / handle
  3. The DISCLAIMER block
  4. Who they are — short, factual, sourced
  5. The video, embedded, with its poster
  6. What they argue — their position, in attributed prose, near-verbatim
     where they are quoted
  7. Transcript, or the substantive passages of it, attributed
  8. Source links (the X post, their channel)
  9. "X.com posts:" section
 10. Related Areas

FILE NAMING: lowercase-with-hyphens, from the person's name or handle.
    pb-onpoint.mdx, jane-doe.mdx


================================================================================
overview.mdx — TABLE OF CONTENTS, THEN THE CASCADING VIDEO WALL
================================================================================

The overview page has TWO required parts, in this order:

  A. A TABLE OF CONTENTS linking to EVERY Level 3 page in this directory.
     Every person page must be reachable from it. No orphans, ever. When a new
     person page is added, the TOC entry is added in the SAME run.

  B. BELOW the TOC, the videos are RE-HOSTED — the same video that is on each
     person's Level 3 page plays again here.

     LAYOUT: one on the LEFT, the next on the RIGHT, alternating, cascading
     from top to bottom down the page. Each floated player sits beside that
     person's blurb, and each entry clears before the next begins so the
     alternation stays clean. On narrow screens they stack full-width.

     The order of the video wall matches the order of the TOC.


================================================================================
MEDIA RULES
================================================================================

Videos follow the site-wide video pipeline; see {ROOT_DIR}/CLAUDE.md.

  * Video files live in {ROOT_DIR}/videos/ and are GITIGNORED (videos/* in
    {ROOT_DIR}/.gitignore). They are never committed. They are pulled from IPFS.
  * Every video is `ipfs add --pin`ed — NEVER `ipfs add -n`, which is a dry run
    that prints a real-looking CID while storing no bytes.
  * Announce with `ipfs routing provide {CID}`, then VERIFY through a public
    gateway before publishing. Local `ipfs pin ls` proves nothing about what a
    visitor sees.
  * Embeds use the CIDv1 base32 subdomain gateways, matching the rest of the
    site:
        https://{bafybei...}.ipfs.dweb.link/     (primary)
        https://{bafybei...}.ipfs.w3s.link/      (fallback)
  * Every player gets a poster frame at
    {SITE_DIR}/internals/static/img/video_posters/{sha256 of the video}.jpg
    The poster IS committed to git — posters are images, and images are tracked.
  * Register the video in {ROOT_DIR}/videos/manifest.yaml, {ROOT_DIR}/IPFS/ipfs.txt,
    {ROOT_DIR}/videos/videos.md, and queue it into the videos.yaml hierarchy.
  * TRANSCRIBE every video (~/BGit/all/tools/Transcription/Transcribe.js) and
    save the transcript to {ROOT_DIR}/videos_transcription/{post_id}.md.
    A transcript is what makes an opinion checkable — it is not optional here.
  * Note transcription artifacts rather than silently "correcting" a speaker.
    Speech recognition mangles names and coinages; say when a rendering is
    uncertain.


================================================================================
REGISTRY UPKEEP
================================================================================

Adding a person page means updating, in the same run:

  * {THIS_DIR}overview.mdx        — TOC entry AND video-wall entry
  * {ROOT_DIR}/pages.csv          — a row for the new page
  * {ROOT_DIR}/level_2.csv        — only if this section's description changes
  * the video registries listed under MEDIA RULES above

Then `cd {SITE_DIR} && npm run build` before calling the work done. Keep every
<div> and </div> at column 0; only the build catches an indented closing tag.


================================================================================
WHAT DOES NOT BELONG HERE
================================================================================

  * Site findings, evidence analysis, or anything written in the site's own
    voice. That belongs in the evidence Level 2 sections.
  * A page about a person who is a SUBJECT of the investigation rather than a
    COMMENTATOR on it. Those go in /People/ or the relevant evidence section.
    This directory is for people giving their ANALYSIS of what happened.
  * Any page without the disclaimer.
