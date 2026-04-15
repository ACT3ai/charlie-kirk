---
name: ck_add_text
description: Add new text/notes to the Charlie Kirk investigation file — finds the right section or creates a new one, never removes existing content. Also downloads X/Twitter posts, videos, and images.
invocable: true
---

This skill has four modes. Read $ARGUMENTS to decide which mode to run.

  IMPROVE MODE — triggered when the argument mentions improving, fixing, assessing,
  or upgrading pages. Examples:
    * "improve all"
    * "improve all FBI pages"
    * "fix one page"
    * "assess the CoverUp overview"
    * "bring all pages up to standard"
    * "improve [any directory or page name]"

  CREATE MODE — triggered when the argument asks to create new Level 3 pages,
  expand a section with new content pages, or add new topic pages. Examples:
    * "create pages for the Influencers/podcasts section"
    * "add Level 3 pages under [TopicDir]"
    * "create podcast host pages"
    * "add [topic] pages under [directory]"

  X POST MODE — triggered when the argument contains one or more X/Twitter URLs
  (URLs containing /status/ from x.com or twitter.com). This mode downloads the
  post data, any attached videos and images, transcribes videos, and adds all
  content to both the master investigation file AND the Docusaurus site pages.
  Examples:
    * "https://x.com/user/status/1234567890"
    * Multiple URLs separated by newlines
    * A URL plus additional notes text

  ADD TEXT MODE — triggered when the argument is new text, a quote, a note,
  or anything else that is raw investigation content to be stored.

If IMPROVE MODE is detected, skip to the IMPROVE MODE section below.
If CREATE MODE is detected, skip to the CREATE MODE section below.
If X POST MODE is detected, skip to the X POST MODE section below.
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
  {ROOT_DIR}/videos/              — Central video storage (gitignored)
  {ROOT_DIR}/images/              — Central image storage
  {ROOT_DIR}/videos_transcription/ — Transcription files for downloaded videos

CK_FILE is file {ROOT_DIR}/Charlie_Kirk.txt
SITE_DOCS_DIR is dir {ROOT_DIR}/site/docs/
TRANSCRIBE_JS is file ~/BGit/work/tools/Transcription/Transcribe.js


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
STEPS (ADD TEXT MODE)
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
X POST MODE
============================

This mode processes one or more X/Twitter post URLs. For each URL it:
  1. Fetches the post data via the X API
  2. Downloads any video attachments
  3. Downloads any image attachments
  4. Pins media to IPFS for permanent hosting
  5. Transcribes videos automatically
  6. Adds the post text and transcription to {CK_FILE}
  7. Creates or updates Docusaurus site pages with embedded media
  8. Converts .md pages to .mdx when embedding media


============================
X POST STEP 0: PARSE INPUT AND DETECT MULTI-URL MODE
============================

Parse $ARGUMENTS to identify all components:

**Component 1: One or more X/Twitter URLs**
* URLs containing /status/ from x.com or twitter.com
* Examples:
    https://x.com/redpillb0t/status/2039976250429640891
    https://twitter.com/someuser/status/1234567890

**Component 2: Video URL**
* A direct video URL (not an X post URL)
* If the X post already has a video attachment, this is redundant

**Component 2b: Image URL**
* A direct image URL (.jpg/.png/.webp/.gif)
* If the X post already has image attachments, those are handled automatically

**Component 3: Site Section**
* An optional hint about which site/docs/ directory this content belongs in
* E.g., "FBI", "CoverUp", "Israel", "Ballistics"
* If not provided, auto-detect from post content

**Component 4: Text Block**
* Additional text/notes to add alongside the X post content

**Component 5: Transcribe Video**
* Transcription is ON BY DEFAULT for all downloaded videos
* If the input contains "skip transcription" (case-insensitive), set
  TRANSCRIBE_REQUESTED = false
* Otherwise TRANSCRIBE_REQUESTED = true

Parse rules:

  1. Split the input into non-empty tokens by line.

  2. Identify each token as one of:
     - X_URL: a URL containing "/status/" (X.com or Twitter.com post)
     - DIRECT_VIDEO_URL: a video URL not containing "/status/"
     - DIRECT_IMAGE_URL: a direct image URL (.jpg/.png/.webp/.gif)
     - SITE_SECTION: a non-URL token matching a directory name under {SITE_DOCS_DIR}
     - TEXT_BLOCK: a token that doesn't fit any above category
     - SKIP_TRANSCRIPTION_FLAG: the phrase "skip transcription" (case-insensitive)

  3. Build a URL_LIST of all X post URLs found.

  4. If a SITE_SECTION is found, it applies to ALL URLs unless a different section
     is specified per URL (same pairing logic as the text block).

  5. Any TEXT_BLOCK applies to all posts.

* After parsing, output the resolved list:
  ```
  ============================================
  Input Parsed
  ============================================
  URLs to process:
    1. URL: {url}
       Section hint: {section or "auto-detect"}
    2. URL: {url}
       Section hint: {section or "auto-detect"}
  Direct video URL: {url or "none"}
  Direct image URL: {url or "none"}
  Text block: {yes/no — brief summary}
  Transcribe videos: {yes (default) / no}
  Mode: {SINGLE POST | MULTI-POST — {count} posts}
  ============================================
  ```

* **MULTI-POST MODE**: If 2 or more X post URLs are present, run Steps 1 through 9
  independently for EACH URL, one at a time.
  Any global text block applies to ALL posts.
  Output a divider between each post's processing:
  ```
  ############################################
  Processing Post {n} of {total}: {url}
  ############################################
  ```


============================
X POST STEP 1: FETCH THE POST
============================

SKIP IF: No X/Twitter URL for this post.

* Extract the post ID from the URL. X URLs look like:
  - https://x.com/{username}/status/{post_id}
  - https://twitter.com/{username}/status/{post_id}
  - The post_id is the numeric string after /status/

* Fetch the full post data using xurl with expanded fields:
  ```bash
  xurl "/2/tweets/{post_id}?tweet.fields=created_at,author_id,public_metrics,text,entities,conversation_id,lang,note_tweet,attachments&expansions=author_id,attachments.media_keys&user.fields=name,username,description,public_metrics&media.fields=url,preview_image_url,type,width,height,duration_ms,variants" --auth app
  ```

* If xurl fails or returns an error, inform the user and stop processing this post.
  (If in multi-post mode, move to the next post.)

* Output to stdout:
  ```
  ============================================
  X Post Fetched: {post_id}
  ============================================
  Author: @{username} ({display_name})
  Date: {created_at}
  Likes: {like_count} | Retweets: {retweet_count} | Views: {impression_count}
  Has Video: {yes/no}
  Has Images: {yes/no — count if yes}
  -------- POST TEXT --------
  {full text of post — print every word, no truncation}
  ---------------------------
  ============================================
  ```

* Save a TEMP YAML file to /tmp/ck_xpost_{post_id}.yaml with the raw post data:
  ```yaml
  id: '{post_id}'
  url: '{original_url}'
  author:
    username: '{username}'
    name: '{display_name}'
    id: '{author_id}'
  text: |
    {full text of the post}
  created_at: '{created_at}'
  lang: '{lang}'
  public_metrics:
    retweet_count: {n}
    reply_count: {n}
    like_count: {n}
    quote_count: {n}
    bookmark_count: {n}
    impression_count: {n}
  attachments:
    videos:
      - type: video
        media_key: '{media_key}'
        duration_ms: {n}
        preview_image_url: '{url}'
        variants:
          - url: '{variant_url}'
            content_type: '{type}'
            bit_rate: {n}
    images:
      - type: photo
        media_key: '{media_key}'
        url: '{url}'
        width: {n}
        height: {n}
  investigation: 'charlie_kirk'
  added_date: '{today YYYY-MM-DD}'
  ```


============================
X POST STEP 2: OCR IMAGES IF POST TEXT IS SPARSE
============================

SKIP IF: No X post was fetched in Step 1.
SKIP IF: Post text has 20 or more meaningful words.
SKIP IF: Post has no image attachments.

* Many high-value posts are memes or screenshots — the real content is IN the image.

* Count meaningful words in the post text (words longer than 2 characters, excluding
  URLs, @handles, and #hashtags). If fewer than 20, attempt OCR.

* For each image attachment:

  2a. Download to temp:
    ```bash
    TMPIMG=$(mktemp /tmp/ck_ocr_XXXXXX.jpg)
    curl -L -o "$TMPIMG" "{image_url}?format=jpg&name=4096x4096"
    ```

  2b. Run OCR:
    ```bash
    tesseract "$TMPIMG" stdout --psm 3 2>/dev/null
    ```
    If tesseract not installed: "tesseract not found. Install with: brew install tesseract"
    Skip OCR for this image but continue.

  2c. Capture OCR output as OCR_TEXT. If it has more than 5 words:
    - Output to stdout
    - Append to the analysis pool for topic matching
    - Add to temp YAML as ocr_text field

  2d. Clean up: rm -f "$TMPIMG"

* Combine OCR text from all images into one analysis pool.


============================
X POST STEP 3: ANALYZE POST IN CK INVESTIGATION CONTEXT AND DETERMINE PLACEMENT
============================

* ANALYSIS POOL = post text + OCR text (if any) + text block (if provided)

* IMPORTANT: Read the analysis pool carefully in the context of the Charlie Kirk
  investigation. Understand what specific aspect of the investigation this post
  relates to — a specific incident, person, evidence category, timeline event,
  or theory. This understanding drives every placement decision below.

* If SITE_SECTION was provided in the input, use it directly. Resolve to a
  directory under {SITE_DOCS_DIR}.

* Otherwise, analyze the ANALYSIS POOL to determine which CK investigation topic
  this post relates to. Match against these topic directories:

  FBI/          — FBI involvement, cover-up, FBI blocking investigations
  CIA/          — CIA involvement theories
  Israel/       — Israel connections, Mossad
  CoverUp/      — Cover-up evidence, destroyed evidence
  Killer/       — Suspect analysis, Tyler Robinson
  Gun_Bullet/   — Ballistics, gun, bullet analysis
  Planes/       — N1098L, SAM flights, SU-BTT
  Drones/       — Drone sightings
  cameras/      — Surveillance camera analysis
  security/     — Security failures at UVU
  Before/       — Timeline events before the assassination
  After/        — Timeline events after the assassination
  People/       — Key individuals
  Censorship/   — Censorship of the investigation
  Motive/       — Motive analysis
  Proof_Intel_Services/ — Intelligence services involvement proof
  Proof_Not_Tyler/      — Evidence Tyler is not the shooter
  Fix/          — Legal reform proposals
  Influencers/  — Influencer coverage
  Media/        — Media analysis and response

* Store as TARGET_SECTION_DIR.

* LEVEL 2 / LEVEL 3 PAGE DETERMINATION (mandatory for X Post Mode):

  3a. Identify the Level 2 parent page:
    * The Level 2 page is the overview.md (or equivalent parent nav page)
      inside {SITE_DOCS_DIR}/{TARGET_SECTION_DIR}/.
    * Read that Level 2 page. Confirm it exists.
    * NEVER auto-create a new Level 2 page. If no existing Level 2 page is
      a reasonable fit, ASK the user:
        "No existing Level 2 page fits this content well. The closest is
         {TopicDir}/overview.md. Should I use that, or do you want a new
         Level 2 page created? (new Level 2 pages are rare)"
      Wait for the user's response before proceeding.

  3b. Identify or plan the Level 3 page:
    * List all existing .md and .mdx files in {SITE_DOCS_DIR}/{TARGET_SECTION_DIR}/.
    * Determine if an existing Level 3 page covers this specific sub-topic.
      - If YES: plan to add the new content to that existing Level 3 page.
      - If NO: plan to create a new Level 3 page. Choose a succinct, descriptive
        filename that captures the distinct sub-topic. Use lowercase-with-hyphens.
        Examples: uvu-public-contacts.md, fbi-evidence-request-denied.md,
        drone-sighting-sept-9.md
    * Store the decision as TARGET_L3_PAGE (existing path or new filename).

  3c. For roughly 95% of X posts, the right placement is: find the best Level 2
    parent, then create or update a Level 3 page under it. Only in rare cases
    does content belong directly on a Level 2 page.

* Also determine the best matching section in {CK_FILE} for the add-text step.
  Store as CK_SECTION_NAME.


============================
X POST STEP 4: SAVE POST DATA AS YAML
============================

SKIP IF: No X post was fetched in Step 1.

* Create directory if needed: {ROOT_DIR}/Research/x_posts/

* Save the post as a YAML file: {ROOT_DIR}/Research/x_posts/{post_id}.yaml
  Include all fields from the temp YAML plus ocr_text if OCR was performed.

* Delete the temp file:
  ```bash
  rm -f /tmp/ck_xpost_{post_id}.yaml
  ```


============================
X POST STEP 5: ADD POST TEXT TO MASTER INVESTIGATION FILE
============================

* Follow the same logic as ADD TEXT MODE Steps 1-5, using the post text + OCR text
  as the content to add.

* Format the insertion block as:

  Source: {original_url}
  Author: @{username} ({display_name})
  Date: {created_at}
  Likes: {like_count} | Retweets: {retweet_count} | Views: {impression_count}

  {full text of post}

  {OCR text if any, prefixed with "[Image text]: "}

* Insert into the matching section of {CK_FILE} (determined in Step 3 as CK_SECTION_NAME).
  Follow all ADD TEXT MODE rules — purely additive, never remove existing content.


============================
X POST STEP 6: DOWNLOAD VIDEO AND PIN TO IPFS
============================

SKIP IF: No video is available from the post or from a separate video URL.

* All videos go to the central directory: {ROOT_DIR}/videos/
  Never store videos inside site/ or individual topic directories.

* First time setup: create directory and .gitignore if they don't exist:
  ```bash
  mkdir -p {ROOT_DIR}/videos
  ```
  Create {ROOT_DIR}/videos/.gitignore with:
  ```
  *.mp4
  *.mp3
  *.mkv
  *.avi
  *.mov
  *.wav
  *.webm
  ```
  Also ensure {ROOT_DIR}/.gitignore has a line for videos/:
  ```
  videos/
  ```

* Check for duplicate before downloading:

  If {ROOT_DIR}/videos/manifest.yaml exists, check whether this video already exists
  by matching source_url or filename starting with post_id.

  **Case A — Already exists locally:** Skip download. Use existing CID. Output:
    "Video already exists: {filename} (CID: {CID})"

  **Case B — In manifest but missing locally:** Recover from IPFS:
    ```bash
    ipfs get --output={ROOT_DIR}/videos/{filename} {CID}
    ipfs pin add {CID}
    ```

  **Case C — Not in manifest:** Proceed to download.

* 6a. Download using yt-dlp:
  ```bash
  yt-dlp "{video_source_url}" -o "{ROOT_DIR}/videos/{post_id}.%(ext)s"
  ```
  If yt-dlp fails, try with cookies or inform the user.

* 6b. Pin to IPFS:
  ```bash
  brew services list | grep kubo
  ```
  If not running: brew services start kubo
  ```bash
  ipfs add --pin {ROOT_DIR}/videos/{filename}
  ```
  Capture the CID. Verify: ipfs pin ls {CID}

* 6c. Update manifest — append to {ROOT_DIR}/videos/manifest.yaml:
  ```yaml
  - filename: {filename}
    ipfs_cid: {CID}
    ipfs_gateway_url: https://ipfs.io/ipfs/{CID}
    source_url: {source_url}
    source_author: '@{username}'
    description: '{brief description from content}'
    added_date: '{today YYYY-MM-DD}'
    pinned: true
  ```

* 6d. Output:
  ```
  ============================================
  Video Downloaded & Pinned to IPFS
  ============================================
  File: {ROOT_DIR}/videos/{filename}
  Size: {file size}
  IPFS CID: {CID}
  Gateway: https://ipfs.io/ipfs/{CID}
  ============================================
  ```


============================
X POST STEP 6B: DOWNLOAD IMAGES AND PIN TO IPFS
============================

SKIP IF: No images available from the post or from a separate image URL.

* All images go to: {ROOT_DIR}/images/
  Never store images inside site/ or individual topic directories.

* First time setup:
  ```bash
  mkdir -p {ROOT_DIR}/images
  ```

* Image URL extraction from X API response:
  - Images appear in "includes.media" array with type "photo"
  - For highest quality, append "?format=jpg&name=4096x4096" to the base URL
  - Record width and height from the API for aspect ratio in embeds

* Check for duplicates: if {ROOT_DIR}/images/manifest.yaml exists, check
  source_url or filename starting with post_id. Skip if found.

* 6B-a. Download each image:
  ```bash
  curl -L -o "{ROOT_DIR}/images/{post_id}_{index}.jpg" "{image_url}?format=jpg&name=4096x4096"
  ```
  Where {index} is 1, 2, 3... for multiple images from the same post.

* 6B-b. Pin each image to IPFS:
  ```bash
  ipfs add --pin {ROOT_DIR}/images/{filename}
  ```
  Capture the CID.

* 6B-c. Update image manifest — append to {ROOT_DIR}/images/manifest.yaml:
  ```yaml
  - filename: {filename}
    ipfs_cid: {CID}
    ipfs_gateway_url: https://ipfs.io/ipfs/{CID}
    source_url: {source_url}
    source_author: '@{username}'
    description: '{brief description}'
    width: {width_px}
    height: {height_px}
    ocr_text_extracted: {true/false}
    added_date: '{today YYYY-MM-DD}'
    pinned: true
  ```

* 6B-d. Output:
  ```
  ============================================
  Image(s) Downloaded & Pinned to IPFS
  ============================================
  Files: {list of filenames}
  IPFS CIDs: {list of CIDs}
  OCR performed: {yes/no}
  ============================================
  ```


============================
X POST STEP 7: TRANSCRIBE VIDEO
============================

SKIP IF: TRANSCRIBE_REQUESTED is false (user said "skip transcription").
SKIP IF: No video was downloaded in Step 6.
NOTE: Transcription is ON BY DEFAULT for all downloaded videos.

* Create output directory if needed:
  ```bash
  mkdir -p {ROOT_DIR}/videos_transcription
  ```

* Create a temp directory for transcription:
  ```bash
  TRANSC_TMPDIR=$(mktemp -d /tmp/ck_transcribe_XXXXXX)
  ```

* Run the transcription:
  ```bash
  cd "$TRANSC_TMPDIR" && node ~/BGit/work/tools/Transcription/Transcribe.js "{ROOT_DIR}/videos/{video_filename}" transcription.txt
  ```

* Wait for completion. This may take several minutes for long videos.

* Verify output:
  ```bash
  ls -la "$TRANSC_TMPDIR/transcription.txt"
  ```

* If transcription fails, inform the user and continue. Do not block on failure.

* Copy the transcription to the permanent location:
  ```bash
  cp "$TRANSC_TMPDIR/transcription.txt" {ROOT_DIR}/videos_transcription/{post_id}.md
  ```

* Read the transcription into memory.

* Clean up:
  ```bash
  rm -rf "$TRANSC_TMPDIR"
  ```

* Output:
  ```
  ============================================
  Video Transcribed
  ============================================
  Video: {video_filename}
  Transcription: {ROOT_DIR}/videos_transcription/{post_id}.md
  Word count: {approximate word count}
  ============================================
  ```


============================
X POST STEP 8: PROCESS TRANSCRIPTION INTO INVESTIGATION FILE
============================

SKIP IF: Step 7 was skipped or transcription failed.

* Read the full transcription from {ROOT_DIR}/videos_transcription/{post_id}.md.

* Add the transcription content to {CK_FILE} in the same section as the post text
  (determined in Step 3). Format the insertion as:

  [Transcription of video from @{username}, {date}]
  Source: {original_url}

  {transcription text}

* Follow all ADD TEXT MODE rules — purely additive, never remove existing content.

* Analyze the transcription for additional people, facts, quotes, and claims
  that were not in the post text. Note any new people or topics discovered.


============================
X POST STEP 9: CREATE/UPDATE LEVEL 3 SITE PAGE WITH EMBEDDED MEDIA
============================

SKIP IF: No TARGET_SECTION_DIR was determined in Step 3.

This step uses the Level 2 / Level 3 decisions made in Step 3.

* 9a. RESOLVE THE TARGET LEVEL 3 PAGE

  Use TARGET_L3_PAGE from Step 3:

  **Case A — Existing Level 3 page:** Read it. Plan to append the new content
  at an appropriate location (usually at the end, before Related Areas if present).

  **Case B — New Level 3 page:** Create it. Choose a succinct, descriptive
  filename that captures the distinct sub-topic of this post. Use
  lowercase-with-hyphens. The filename should make the topic immediately clear.
  Good examples:
    * uvu-public-contacts.md
    * fbi-evidence-request-denied.md
    * drone-sighting-sept-9.md
    * erika-kirk-ceo-announcement.md

* 9b. MDX CONVERSION (if media is involved)

  If creating a new page or updating an existing page that needs embedded media
  (video or images), use .mdx format:

  - If the target file is .md, convert it to .mdx:
    1. Rename the file from .md to .mdx
    2. Search all files under {SITE_DOCS_DIR} for links pointing to the old .md
       filename and update them to .mdx
    3. Update sidebars.ts if it references the old filename

  - If creating a new page, create it as .mdx from the start

* 9c. PAGE CONTENT — NEAR-VERBATIM FROM THE POST

  IMPORTANT: When the X post or blog post contains substantive text, copy
  it nearly word for word onto the Level 3 page. Do not summarize,
  paraphrase, or condense. The goal is to preserve the full informational
  value of the original post on this page. Only light formatting adjustments
  are allowed (fixing line breaks, adding attribution, etc.).

  Page structure for a NEW Level 3 page:
    - Back button at the very top linking to the parent Level 2 page
    - Page title (H1) — descriptive of the specific sub-topic
    - Source attribution block: author, date, link to original post
    - Full post text (nearly verbatim, attributed: "According to @{username}...")
    - OCR text if extracted (attributed, nearly verbatim)
    - Transcription content if available (key quotes and full relevant passages)
    - Embedded images and/or video (see media embedding rules below)
    - Follow all defamation rules for living persons
    - Related Areas section at the bottom

  Page structure when APPENDING to an existing Level 3 page:
    - Add a ## sub-heading for the new content (e.g., "## @{username} Report, {date}")
    - Source attribution block
    - Full post text (nearly verbatim)
    - Embedded images/video
    - Keep all existing content intact

* 9d. IMAGE HANDLING

  Images from the post MUST be saved to {ROOT_DIR}/images/ (done in Step 6B)
  and embedded on the Level 3 page. Do not skip images — they often contain
  critical evidence (screenshots, documents, photos).

  IMAGE EMBEDDING — use half-width, floated right, text flows around it:
  Single image:
  ```
  <div style={{float: 'right', width: '48%', maxWidth: '480px', marginLeft: '1.5rem', marginBottom: '1rem'}}>
    <img
      src="http://127.0.0.1:8080/ipfs/{CID}"
      alt="{description}"
      style={{width: '100%', height: 'auto', aspectRatio: '{width}/{height}', borderRadius: '4px'}}
    />
    <p style={{fontSize: '0.85rem', color: '#666', marginTop: '0.5rem'}}>
      <em>{Description}. Source: <a href="{original_url}">@{username} on X</a>, {date}.</em>
    </p>
  </div>
  ```

  Multiple images from the same post (up to 4 attachments):
  ```
  <div style={{float: 'right', width: '48%', maxWidth: '480px', marginLeft: '1.5rem', marginBottom: '1rem'}}>
    <div style={{display: 'flex', flexWrap: 'wrap', gap: '0.5rem'}}>
      <img
        src="http://127.0.0.1:8080/ipfs/{CID_1}"
        alt="{description_1}"
        style={{width: 'calc(50% - 0.25rem)', height: 'auto', aspectRatio: '{w1}/{h1}', borderRadius: '4px'}}
      />
      <img
        src="http://127.0.0.1:8080/ipfs/{CID_2}"
        alt="{description_2}"
        style={{width: 'calc(50% - 0.25rem)', height: 'auto', aspectRatio: '{w2}/{h2}', borderRadius: '4px'}}
      />
    </div>
    <p style={{fontSize: '0.85rem', color: '#666', marginTop: '0.5rem'}}>
      <em>{Description}. Source: <a href="{original_url}">@{username} on X</a>, {date}.</em>
    </p>
  </div>
  ```

  Use local IPFS gateway first (http://127.0.0.1:8080/ipfs/{CID}).
  Include fallback gateways as additional <source> tags for video,
  or as a comment noting the fallback URL for images.

* 9e. VIDEO EMBEDDING — use half-width, floated right, with text flowing around it:
  ```
  <div style={{float: 'right', width: '48%', maxWidth: '480px', marginLeft: '1.5rem', marginBottom: '1rem'}}>
    <video controls style={{width: '100%', height: 'auto', display: 'block', borderRadius: '4px'}}>
      <source src="http://127.0.0.1:8080/ipfs/{CID}" type="video/mp4" />
      <source src="https://ipfs.io/ipfs/{CID}" type="video/mp4" />
      <source src="https://dweb.link/ipfs/{CID}" type="video/mp4" />
      Your browser does not support the video tag.
    </video>
    <p style={{fontSize: '0.85rem', color: '#666', marginTop: '0.5rem'}}>
      <em>{Description}. Source: <a href="{original_url}">@{username} on X</a>, {date}.</em>
    </p>
  </div>
  ```
  NEVER use cloudflare-ipfs.com — that gateway was shut down in 2024.
  NEVER use `width="100%"` as an HTML attribute — use style={{width: '100%'}} only.

  Always add clearfix div after the last floated element on the page:
  ```
  <div style={{clear: 'both'}} />
  ```

* 9f. UPDATE THE LEVEL 2 PAGE TOC — MANDATORY FOR NEW LEVEL 3 PAGES

  If a new Level 3 page was created, immediately update the parent Level 2
  page's TOC to include a link to the new page:

  * Read the Level 2 page (overview.md or equivalent).
  * Add a bullet entry for the new Level 3 page in the three-column TOC.
  * Re-balance columns so heights are equal or off by at most one row.
  * If the Level 2 page has no TOC yet, create one from scratch including
    all existing Level 3 pages in that directory plus the new one.
  * Verify: every .md and .mdx file in the directory (except the Level 2 page)
    must be linked from the TOC. If any are missing, add them now.

  This step is NOT optional. A Level 3 page without a link from its parent
  Level 2 page is an orphan and will never be found by readers.

* If the content mentions people who have Details/ profiles, cross-link to them.


============================
X POST STEP 10: FINAL SUMMARY
============================

* Output a complete summary for this post:
  ```
  ============================================
  ck_add_text X Post Complete — Post {n}/{total}
  ============================================
  Post: {post_id} by @{username} on {date}
  URL: {original_url}
  Post text (first 100 chars): {preview...}
  OCR performed: {yes — {word count} words | no}
  YAML saved: {path}
  Added to CK_FILE: {section name}, lines {range}
  Video: {downloaded filename or "none"}
  Video IPFS CID: {CID or "none"}
  Images: {downloaded filenames or "none"}
  Image IPFS CIDs: {CIDs or "none"}
  Transcription: {yes — saved to {path} | no — not requested | failed}
  Site pages updated: {list of files modified/created}
  ============================================
  ```

* In multi-post mode, after all posts processed:
  ```
  ============================================
  ALL POSTS PROCESSED
  ============================================
  Total posts: {n}
  Successful: {n}
  Failed (xurl error): {n} — {list URLs}
  ============================================
  ```


============================
IMPROVE MODE
============================

ASSESSMENT MANUAL — READ THIS FIRST
-------------------------------------
ASSESS_MANUAL is file /Users/bryan/BGit/Bryan_git/charlie-kirk/prompts/Assess_Manual.md

MANDATORY: Read this file FULLY into context before touching any page. The manual
defines all Level 2 and Level 3 page requirements. Every structural decision you
make must be validated against it. The manual is the authority — the summary below
is a quick reference only.

Absolute path: /Users/bryan/BGit/Bryan_git/charlie-kirk/prompts/Assess_Manual.md

SITE_DOCS_DIR is dir /Users/bryan/BGit/Bryan_git/charlie-kirk/site/docs/

Pages are organized as:
  * Level 2: {SITE_DOCS_DIR}/{TopicDir}/overview.md
             OR {SITE_DOCS_DIR}/{TopicDir}/{topic}.md when that file acts as the
             parent navigation page for a group of Level 3 pages.
  * Level 3: {SITE_DOCS_DIR}/{TopicDir}/{specific-page}.md — individual topic pages
             that are linked from a Level 2 TOC.

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
  * Read the full file. Identify whether it is Level 2 (overview.md or acting
    as a parent nav page) or Level 3 (a specific topic page linked from a L2 TOC).

IMPROVE STEP 2: If Level 2 — audit the TOC against actual files on disk
  * List all .md and .mdx files in the same directory.
  * Check: is every existing Level 3 page linked from the TOC?
  * If any are missing from the TOC → add them (fix the TOC in STEP 3).
  * Check: does the TOC link to any files that do not exist? → remove those links.

IMPROVE STEP 3: Run the checklist from the assessment manual for the page's level.
  * List every failing item. If all items pass, output "PASS — no changes needed"
    for this page and skip to the next.

IMPROVE STEP 4: Fix each failing item — do not skip any
  Level 2 fixes (apply all that are needed):
    [ ] Missing or bad orientation paragraph → add one or two sentence intro.
    [ ] Missing three-column TOC → build it from the Level 3 pages that exist
        in this directory. Link to actual existing files only.
    [ ] TOC missing links to existing Level 3 pages → add missing links.
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
    [ ] Page is a .md that contains embedded media → convert to .mdx and update
        all links pointing to it.

  Both levels:
    [ ] Broken internal links → fix the path to match the actual file location.
    [ ] Unclosed MDX tags or rendering issues → close/fix them.

IMPROVE STEP 5: Write the updated file
  * Use the Edit tool (preferred) or Write tool for larger rewrites.
  * Never remove existing body content. Only add missing structure (TOC, back
    button, paragraphs, Related Areas) or rewrite violating sentences in place.
  * Keep the existing page title (H1) exactly as-is.

IMPROVE STEP 6: Report for this page
  * Output a one-line summary:
      FIXED {file_path} — {comma-separated list of items fixed}
    or
      PASS {file_path} — no issues found

IMPROVE STEP 7: Move to next page, repeat until all pages in scope are done.

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
  * When IMPROVE MODE identifies sub-topics that are missing Level 3 pages, note
    them under "Needs Manual Attention" — do not create them during IMPROVE MODE.
    Use CREATE MODE to build new pages.
  * Do not change the Docusaurus front matter (title, sidebar_label, etc.) unless
    it is clearly wrong or missing.
  * Only write to files under {SITE_DOCS_DIR}. Do not touch private files, the
    master Charlie_Kirk.txt, or anything outside the site/docs/ tree.


============================
CREATE MODE
============================

ASSESSMENT MANUAL — READ THIS FIRST
-------------------------------------
ASSESS_MANUAL is file /Users/bryan/BGit/Bryan_git/charlie-kirk/prompts/Assess_Manual.md

MANDATORY: Read this file FULLY before creating any pages. Every new page you
create must comply with the requirements in the manual for its level.

Absolute path: /Users/bryan/BGit/Bryan_git/charlie-kirk/prompts/Assess_Manual.md

WHAT CREATE MODE DOES
---------------------
Create Mode builds new Level 3 pages under an existing Level 2 topic and
immediately updates the Level 2 page's TOC to link to them. It never leaves
orphan pages — every new page must be reachable from a Level 2 TOC entry.

When creating pages that will contain embedded media (videos, images), create
them as .mdx files from the start. Otherwise create as .md.

CREATE STEPS
------------

CREATE STEP 1: Identify scope
  * From $ARGUMENTS, determine:
    - Which Level 2 page is the parent (the .md file whose TOC will be updated).
    - What Level 3 pages need to be created (titles, content, file names).
  * Read the parent Level 2 page fully.
  * List all .md and .mdx files already in the directory to avoid duplicates.

CREATE STEP 2: Create each Level 3 page
  * For each new page, write a fully compliant Level 3 file (see assessment manual):
    - Back button at the very top linking to the parent Level 2 page.
    - Page title (H1) matching the topic.
    - Content organized under ## sub-headings.
    - All factual claims attributed to a source.
    - Defamation-safe language for all living persons.
    - Status field if this is a person profile page.
    - Clearfix div after the last media item (if any).
    - Related Areas section at the bottom: 6 links, 2 columns of 3,
      pointing outside the current section.
  * File naming: use lowercase-with-hyphens, prefixed with the parent topic
    name when pages are siblings in the same directory (e.g., podcasts-tucker-carlson.md).
  * If the page will contain embedded video or images, use .mdx extension.

CREATE STEP 3: Update the parent Level 2 page TOC — MANDATORY
  After creating all Level 3 pages, immediately update the parent Level 2 page:
  * Add a bullet for each new Level 3 page in the three-column TOC.
  * Re-balance columns so heights are equal or off by at most one row.
    Column balance rules:
      - Distribute entries left-to-right (fill column 1 bullet 1, then col 2 bullet 1,
        then col 3 bullet 1, then col 1 bullet 2, etc.)
      - Extra items go to column 1 first, then column 2.
  * If the Level 2 page has no TOC yet, create one from scratch including all
    existing Level 3 pages in that directory plus the new ones.
  * If the Level 2 page is missing other required elements (orientation paragraph,
    three explanatory paragraphs, Related Areas), fix them now.

CREATE STEP 4: Verify no orphans
  * Confirm every .md and .mdx file in the directory (except the Level 2 page itself)
    is linked from the Level 2 TOC. If any are missing, add them.

CREATE STEP 5: Report
  * List every file created and the Level 2 file updated.
  * Note any TOC rebalancing performed.
  * Flag any pages that could not be created due to missing information.

CREATE MODE CONSTRAINTS
-----------------------
  * Never create a Level 3 page without also updating the parent Level 2 TOC.
  * Never link to a file in the TOC that does not exist on disk.
  * Defamation rules apply to all content written — see assessment manual and
    the CLAUDE.md files in the project for full defamation rules.
  * Only write to files under {SITE_DOCS_DIR}.


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

* In CREATE MODE: this skill writes new .md/.mdx files under {SITE_DOCS_DIR} and
  updates the parent Level 2 page. {CK_FILE} and all private files are read-only.

* In X POST MODE: this skill writes to:
  - {CK_FILE} (adding post text and transcriptions)
  - {ROOT_DIR}/Research/x_posts/ (YAML post data)
  - {ROOT_DIR}/videos/ (downloaded videos, gitignored)
  - {ROOT_DIR}/videos_transcription/ (transcription files)
  - {ROOT_DIR}/images/ (downloaded images)
  - {ROOT_DIR}/videos/manifest.yaml (video manifest)
  - {ROOT_DIR}/images/manifest.yaml (image manifest)
  - {SITE_DOCS_DIR}/ (creating/updating .mdx pages with embedded media)
