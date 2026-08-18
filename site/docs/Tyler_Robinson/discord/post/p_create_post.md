p_create_post.md

Create the X post (one long post) that we will publish about the Tyler Robinson
Discord material. This prompt file IS the mission. Fill in the WHAT I NEED
section below, then run this prompt file. It writes the post into this same
directory.


===========================
VARIABLES
===========================

ROOT_DIR dir is ~/BGit/Bryan_git/charlie-kirk

POST_DIR dir is {ROOT_DIR}/site/docs/Tyler_Robinson/discord/post
  The directory this prompt file sits in. Every output file goes here.

DISCORD_DIR dir is {ROOT_DIR}/site/docs/Tyler_Robinson/discord
TYLER_DIR   dir is {ROOT_DIR}/site/docs/Tyler_Robinson
CK_FILE     is file {ROOT_DIR}/Charlie_Kirk.txt
  READ ONLY. Never write, edit, append, reorder, or reformat this file.
  That rule is absolute and overrides everything in this prompt.

TWEET_SKILL_FILE is file ~/BGit/Bryan_git/Personal/tweet/skill/tweet_bryan/SKILL.md
TWEET_NOTES_FILE is file ~/BGit/Bryan_git/Personal/tweet/notes.txt
TWEET_ROOT dir is ~/BGit/Bryan_git/Personal/tweet/

OUTPUT_FILE is file {POST_DIR}/bad_tweet.txt
  The draft this prompt writes. Called "bad" because Bryan hand-upgrades it.

GOOD_FILE is file {POST_DIR}/good_tweet.txt
  The human-upgraded version that actually gets posted. NEVER overwrite it.
  If it does not exist, create it as a copy of {OUTPUT_FILE}.

IMAGE_PROMPT_FILE is file {POST_DIR}/p_create_nano_banaa.md
  The companion prompt that makes the image that goes with this post.
  This prompt does not run it.

SITE_URL is the value https://whoassassinatedcharliekirk.com
X_HANDLE is the value @HolonCitizen


===========================
WHAT I NEED  (Bryan fills this in)
===========================

* Mission:

* The single most important thing the reader must take away:

* Points to make (keep my wording nearly exact):

* Facts, quotes, screenshots, links to use:

* Who this post is aimed at:

* Call to action:

* Anything to leave OUT:


Rules for this section:
* Whatever is written here wins over every default in this prompt file.
* If a point is written out here, it survives into the draft. Do not compress
  it, reorder it, or rewrite it into a punchier style. Fix typos, grammar
  slips and branding only.
* If this section is empty, do not guess a mission. Stop and say the WHAT I
  NEED section is empty.


===========================
STAGE 1: LEARN THE STYLE
===========================

* Read {TWEET_SKILL_FILE} in full FIRST. That skill is the authority on how
  Bryan writes a post. Everything in it applies here.
* Read {TWEET_NOTES_FILE} if deeper style grounding is needed.
* Walk {TWEET_ROOT} and find directories that hold BOTH bad_tweet.txt and
  good_tweet.txt. Diff each pair. The differences are exactly how the human
  rewrites AI drafts. Prefer pairs older than 4 hours (the human has had time
  to upgrade them). Apply those patterns.
* Read every {POST_DIR}/bad_*.txt already present. Those are REJECTED drafts.
  Learn what was wrong and never repeat it.
* Read {POST_DIR}/CLAUDE.md and any CLAUDE.md walking up to {ROOT_DIR}. Obey
  them. The charlie-kirk repo rules on defamation and on Charlie Kirk's cause
  of death apply to this post.


===========================
STAGE 2: GATHER THE FACTS
===========================

* Read every file already in {POST_DIR}: notes, screenshots, .txt transcripts,
  pasted post text, links.
* Read every .mdx page under {DISCORD_DIR}.
* Read the Discord-related pages under {TYLER_DIR}, at least:
  {TYLER_DIR}/Discord_Messages.mdx, {TYLER_DIR}/Messages/,
  {TYLER_DIR}/overview.mdx, {TYLER_DIR}/Investigation_Index.mdx.
* Search {CK_FILE} for the Discord material and read those sections. Read only.
* For any .mp4 named in the mission, read its Large File Bridge artifacts:
  {name}.mp4.transcription, {name}.mp4.ocr, {name}.mp4.ai_description.
  In a working git repo they live under <repo_root>/.lfbridge/ path-mirrored,
  so {ROOT_DIR}/videos/x.mp4 maps to {ROOT_DIR}/.lfbridge/videos/x.mp4.transcription.
* Never invent a fact, a number, a date, a username, or a quote. Every claim
  must trace back to an input file or to the WHAT I NEED section.
* Do not web search unless the mission asks for it.
* Never pause to ask whether to write the post. The answer is always yes.
  Run every stage end to end.


===========================
STAGE 3: PLAN
===========================

* Decide the register: standalone post, reply post, or long write-up. Default
  is a standalone post unless the mission says otherwise.
* List every candidate point, then rank by impact. Strongest material goes
  highest.
* Assume the reader has never heard of this investigation, but do not
  over-explain what this audience already knows about the Kirk case.
* Decide which one image the post is paired with, and note it at the bottom of
  the draft as a comment-free plain line only if the mission asks for it.
  Otherwise the image is handled entirely by {IMAGE_PROMPT_FILE}.


===========================
STAGE 4: WRITE THE POST
===========================

Hard format rules, never broken:
* ONE long post. Never a numbered thread. No "1/", no "/1", no "THREAD:".
* Plain text only. No markdown. Bullets are asterisk-space ("* "), never
  dashes.
* No emojis. No hashtags.
* No meta references to the transcript, the prompt, or the writing process.

The hook:
* The first sentence and the first 40 words do all the work even if the reader
  stops there. The post shows truncated at roughly 60 words.
* First 8 to 12 words bridge to the reader's exact concern.
* Then 1 to 3 sentences saying plainly what this is, then a blank line, then
  the bullets.
* Do not invent a title line the mission did not ask for.

The body:
* Every sentence earns its place. Active voice. Plain words. No hype words.
  Strip adverbs and intensifiers.
* Bullets: one distinct point each, most important first. 7 words ideal, 14
  acceptable, 21 too long. Pick the strongest 6 to 12. That length target
  applies to bullets YOU compose, not to wording Bryan supplied.
* Bryan's bullets may be full conversational sentences in "We ..." / "You can
  ..." voice. Keep that voice where the mission uses it.

Defamation safety, mandatory:
* Never state as fact that a living person committed a crime or acted
  illegally or immorally. Use "allegedly", "reportedly", "evidence suggests",
  "I am not claiming".
* Tyler Robinson has not been convicted. Every reference to him and to anyone
  named in the Discord material is framed as allegation, court filing, or
  reported claim, with the source named.
* When naming living people in an accusatory context, include an explicit
  hedge sentence, such as: "None of this is saying that any of these people
  did anything illegal or immoral."
* Quote a Discord message only as what a filing or a source says it says.
  Never assert that a screenshot is authentic; say who published it.

The close:
* Call to action fitted to the mission.
* Standing CTA for censored political topics: "I'm heavily censored on this —
  reposts are the only way this reaches anyone. Please hit that repost button."
* Attribution and link each on their own bare line: {X_HANDLE} and the page on
  {SITE_URL} that this post is about.
* When citing an X post as a source, put it at the end of that same line:
  X post by @handle (ID: ...): https://x.com/.../status/...


===========================
STAGE 5: SELF REVIEW
===========================

Check the draft against every item, fix, then re-check:
* One continuous post. No thread numbering anywhere.
* The first 40 words carry the whole post alone.
* Every bullet under 14 words (21 absolute max). 12 bullets or fewer, sorted
  by impact.
* No emojis, hashtags, markdown, dash bullets, hype words.
* No unhedged claim about any living person. Tyler Robinson framed as accused,
  not convicted.
* No invented facts. Every claim traceable to an input file or the mission.
* Nothing repeated from any bad_*.txt rejected draft in {POST_DIR}.
* Every point written in WHAT I NEED survived into the draft.
* Nothing in {CK_FILE} was written, changed, or deleted.


===========================
STAGE 6: OUTPUT
===========================

* Write the final post to {OUTPUT_FILE}, replacing any existing one. The file
  holds ONLY the post text, ready to paste into X.
* If {GOOD_FILE} does not exist, copy {OUTPUT_FILE} to {GOOD_FILE}. If it does
  exist, never touch it.
* Output to stdout one line: the output file path and the word count. Do not
  print the whole post to stdout.
* Then output to stdout:
  ==============================================================
  Post written. Image prompt is a separate run: p_create_nano_banaa.md
  ==============================================================
