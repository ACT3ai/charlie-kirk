ROOT_DIR dir is ~/BGit/Bryan_git/charlie-kirk

WORK_DIR dir is {ROOT_DIR}/activism/laws/thomas_massey

LETTER_FILE is file {WORK_DIR}/letter.md
ENVELOPES_FILE is file {WORK_DIR}/envelops.yaml
INFO_FILE is file {WORK_DIR}/massy_info.yaml
LETTERS_DIR is directory {WORK_DIR}/letters

PER_LETTER_MD is the file name "letter2.md"   (the per-recipient markdown letter)
PER_LETTER_DOCX is the file name "letter2.docx" (the Word version of that letter)

AUTHOR is Bryan Starbuck
AUTHOR_PHONE is 425-949-6801
AUTHOR_EMAIL is Bryan@TheStarbucks.com
AUTHOR_ADDRESS is 16430 NE 50th, Redmond, WA 98052
PRINCIPAL is Representative Thomas Massie
CAMPAIGN_SITE is https://WhoAssassinatedCharlieKirk.com
FIX_OVERVIEW is https://WhoAssassinatedCharlieKirk.com/Fix/overview
YOUTUBE_LINK is https://www.youtube.com/watch?v=1RbDMiEReys

DOCX_TOOL is the command "pandoc" (md -> docx). Confirm it exists with
  "which pandoc" before STAGE 6; pandoc 3.x is installed on this machine.

============================
GOAL
============================

The master letter {LETTER_FILE} is ALREADY WRITTEN and we are happy with it.
It is the finished, ready-to-mail letter from {AUTHOR} to {PRINCIPAL}.

This prompt does NOT rewrite {LETTER_FILE}. It FANS IT OUT. For every
addressee in {ENVELOPES_FILE} — that is, every (person x location) pairing
already built for the mailing — it produces a private, customized copy of the
letter in its own directory, then renders that copy to a Word document:

    {LETTERS_DIR}/{name}/{location}/{PER_LETTER_MD}     (customized markdown)
    {LETTERS_DIR}/{name}/{location}/{PER_LETTER_DOCX}   (Word version)

  {name}     = the recipient (the PERSON), one directory per person/title.
  {location} = a unique, human-readable place name (the LOCATION), one
               subdirectory per place that person receives mail.

We are taking ONE person and sending the letter to EACH of their locations.
The same person reachable at two places gets a copy under each location
subdirectory. {PRINCIPAL} himself gets a copy under every location.

THE FOCUS IS THOMAS MASSIE AND HIS PEOPLE. The mailing already covers Massie,
his named congressional staff, his named campaign staff, and several roles we
only know by JOB TITLE (e.g. "Campaign Manager"). We mail those title-only
roles too — addressed to the title. STAGE 2 may discover MORE of his staff
(named or title-only) and fold them in; never fabricate one.

WHAT THIS PROMPT MUST NEVER DO:
  * It must NEVER modify {LETTER_FILE} in {WORK_DIR}. The master stays
    untouched. All edits happen only in the per-recipient copies under
    {LETTERS_DIR}/.
  * It must NEVER append a comments block, a notes block, an HTML comment, a
    "BEFORE MAILING / CONFIRM" block, a TODO, or ANY commentary to a
    {PER_LETTER_MD}. The per-recipient markdown contains the letter and
    nothing else. (Stray notes leak into the Word document and ruin it.)
    See APPENDIX B — THE NO-NOTES RULE.

============================
STAGE 1 — READ THE INPUTS
============================

* Read {LETTER_FILE} in full. This is the master. Hold its full text in
  memory. Identify its parts so you can customize precisely:
    - the date line at the top,
    - the salutation ("Dear Representative Massie:"),
    - the opening ASK paragraph,
    - the body (why-him framing, forcing-function, the four laws + links +
      video, the ChatGPT tip, the "who I am" + offer paragraph),
    - the signature block ({AUTHOR}, phone, email, CamelCase site),
    - the bottom From: block ({AUTHOR} + {AUTHOR_ADDRESS}),
    - the bottom To: block ({PRINCIPAL} + office address).
  Confirm the master has NO trailing comment/notes block. If it somehow does,
  do NOT copy that block into any per-recipient letter (and do NOT edit the
  master).

* Read {ENVELOPES_FILE}. Its root key is envelopes, an array. Each entry has:
    mail_id, name, mailing_address_line_1, mailing_address_line_2,
    phone_number, email_address, website, description.
  This array is the authoritative list of recipients to fan out to.

* Read {INFO_FILE} for supporting facts (how_to_address, the named staff and
  their titles, which address is best_for_congress). Use it to choose the
  right salutation and role framing per recipient. Do NOT invent anything not
  traceable to {INFO_FILE} or {ENVELOPES_FILE}.

Output to stdout:
============================
STAGE 1 COMPLETE
Master letter loaded: yes
Master has no trailing notes/comment block: yes/no
Envelopes loaded: N
Distinct people: N | Distinct locations: N
============================

============================
STAGE 2 — (OPTIONAL) DISCOVER MORE OF MASSIE'S STAFF
============================

PURPOSE
  We want to reach as many of Massie's real people as possible. {ENVELOPES_FILE}
  is the starting set. If you can verify ADDITIONAL staff (congressional or
  campaign), add them — by name when known, otherwise by JOB TITLE — so they
  get a letter too.

HOW (only if web search is available; skip cleanly if it is not):
  * Search for additional Massie staff and offices: "Thomas Massie scheduler",
    "Thomas Massie deputy chief of staff", "Thomas Massie legislative
    assistant", "Thomas Massie district offices KY-4 addresses",
    "Massie for Congress campaign manager finance director".
  * Cross-check each new person/title and each new address against at least
    one authoritative source (massie.house.gov, the House clerk directory,
    FEC.gov, LegiStorm, Ballotpedia, reputable news). Record the source.
  * For any NEW verified person/title or NEW verified location:
      - add it to {INFO_FILE} (people / mailing_addresses) with source +
        verified flag, mirroring that file's existing shape, AND
      - add the corresponding (person x location) envelope(s) to
        {ENVELOPES_FILE}, continuing the Mail_N numbering, following the
        same assignment logic already used there (Massie everywhere; D.C.
        staff at D.C., commonly also the district; district staff at the
        district offices; campaign staff at the campaign address).
  * NEVER FABRICATE. If a name, title, or address cannot be verified, do not
    add it. It is correct to add nothing in this stage.

  After this stage, {ENVELOPES_FILE} is the final, authoritative recipient
  list the rest of the prompt fans out over.

Output to stdout:
============================
STAGE 2 COMPLETE
Web search available: yes/no
New verified people/titles added: N
New verified locations added: N
New envelopes added: N (Mail_X .. Mail_Y)
Total envelopes now: N
============================

============================
STAGE 3 — BUILD THE DIRECTORY MAP (name x location)
============================

Turn each envelope into one output directory
{LETTERS_DIR}/{name}/{location}/ using these naming rules. Compute the map
fully BEFORE writing any file, so names are consistent and unique.

{name} — THE PERSON (one directory per person/title):
  * If the envelope names a real person, use that person's name:
      "The Honorable Thomas Massie"  -> Thomas_Massie
      "Matt Gurtler, Chief of Staff" -> Matt_Gurtler
      "Chris McCane, District Director" -> Chris_McCane
  * If the envelope is addressed only by a JOB TITLE (no person name), use the
      title:
      "Campaign Manager, Thomas Massie for Congress" -> Campaign_Manager
      "Campaign Finance Director, ..."               -> Campaign_Finance_Director
  * Sanitize: keep the name/title words only; drop the "Office of ...",
    "Thomas Massie for Congress", "c/o ...", and any trailing org text. Replace
    every space and special character with a single underscore. No commas, no
    slashes (write "Communications Director / Press Secretary" as
    Communications_Director_Press_Secretary).

{location} — THE PLACE (one subdirectory per place the person receives mail):
  * Derive a unique, human-readable place name from the envelope's address:
      Washington, DC (2371 Rayburn HOB)  -> Washington_DC   (Capitol / D.C. office)
      La Grange, KY                       -> La_Grange_KY
      Ashland, KY                         -> Ashland_KY
      campaign / committee PO box (Newport, KY) -> Campaign_Newport_KY
  * Rule: the Washington, D.C. congressional office is always Washington_DC.
    For any other place, build "{City}_{ST}" from the address. If two distinct
    addresses would collapse to the same {City}_{ST} for the same person (e.g.
    a district office and a campaign PO box in the same town), prefix the
    non-office one to keep it unique (Campaign_{City}_{ST}, Finance_{City}_{ST}).
  * Location names must be unique and clearly different from one another so no
    two of a person's locations ever collide.

Create directories as needed (mkdir -p). One leaf directory per envelope.

Output to stdout:
============================
STAGE 3 COMPLETE
Directories planned: N (one per envelope)
People dirs: <list of {name}>
Sample paths:
  letters/Thomas_Massie/Washington_DC/
  letters/Matt_Gurtler/Washington_DC/
  ...
Name/location collisions: 0
============================

============================
STAGE 4 — WRITE EACH CUSTOMIZED letter2.md
============================

For EVERY envelope, write {LETTERS_DIR}/{name}/{location}/{PER_LETTER_MD} by
copying the master {LETTER_FILE} and customizing it for THAT person at THAT
location. Apply APPENDIX A (CUSTOMIZATION BY RECIPIENT) and APPENDIX B (THE
NO-NOTES RULE).

What stays identical to the master (do not weaken the letter):
  * The four laws by name, in order.
  * The links exactly: {FIX_OVERVIEW}, {YOUTUBE_LINK}, and the CamelCase
    {CAMPAIGN_SITE}.
  * The forcing-function argument and the ChatGPT/AI tip.
  * The "who I am" + offer content (placed late, per the master).
  * The signature block: {AUTHOR}, {AUTHOR_PHONE}, {AUTHOR_EMAIL},
    WhoAssassinatedCharlieKirk.com.
  * The bottom From: block: {AUTHOR} + {AUTHOR_ADDRESS} (unchanged).

What you CHANGE for this recipient:
  1. SALUTATION — match the recipient:
       - {PRINCIPAL} himself: "Dear Representative Massie:" (as the master).
       - A named staffer: "Dear Mr./Ms. {LastName}:" when an honorific is
         reasonably known/inferable; otherwise "Dear {Full Name}:".
       - A title-only recipient: "Dear {Title}:" (e.g. "Dear Campaign
         Manager:").
  2. OPENING ASK + FRAMING — rewrite ENOUGH to be appropriate for who is
     reading it (see APPENDIX A). For Massie, keep the direct personal ask.
     For staff/campaign people, the ask becomes: put this in front of the
     Congressman and help move it — while keeping every required element.
     Adjust pronouns so "you" is the reader and Massie is referred to as
     "the Congressman" / "Rep. Massie" when the reader is NOT Massie.
  3. BOTTOM To: BLOCK — replace with THIS envelope's addressee and address:
       To:
         {envelope name}
         {mailing_address_line_1}
         {mailing_address_line_2}
     Use the exact name and address lines from this envelope in
     {ENVELOPES_FILE}. Do not substitute a different office.

The file ends immediately after the bottom To: block. NOTHING follows it —
no comment, no note, no confirm-block. (APPENDIX B.)

Repeat for every envelope. Each writes its own letter2.md; the master and all
other copies are unaffected.

Output to stdout:
============================
STAGE 4 COMPLETE
letter2.md files written: N
Customized salutations: N | Title-only salutations: N
Every file ends at the To: block (no notes appended): yes
Master letter.md unchanged: yes
============================

============================
STAGE 5 — VERIFY EACH letter2.md (BEFORE WORD CONVERSION)
============================

Walk every {LETTERS_DIR}/{name}/{location}/{PER_LETTER_MD} and confirm:
  [ ] Salutation matches the recipient (name or title).
  [ ] Required elements all present: four laws by name; {FIX_OVERVIEW};
      {YOUTUBE_LINK}; {CAMPAIGN_SITE} in CamelCase; forcing-function;
      ChatGPT tip; author intro + offer; signature block.
  [ ] Phrase "puppet master" does NOT appear anywhere.
  [ ] Bottom To: block matches this envelope's name + address lines.
  [ ] Bottom From: block is {AUTHOR} + {AUTHOR_ADDRESS}.
  [ ] The file ENDS at the To: block — NO HTML comment (<!-- -->), NO "BEFORE
      MAILING", NO "CONFIRM", NO "Notes", NO "TODO", nothing after it.
      (Grep each file for "<!--", "BEFORE MAILING", "CONFIRM", "TODO",
      "Note:" — there must be zero hits in the letter copies.)
  [ ] {LETTER_FILE} (the master) is byte-for-byte unchanged from STAGE 1.

Fix any file that fails, then re-verify it.

Output to stdout:
============================
STAGE 5 COMPLETE
Files checked: N | Passed: N
No-notes check (zero stray comment/notes hits): passed
Master unchanged: yes
============================

============================
STAGE 6 — RENDER EACH letter2.docx (WORD)
============================

Confirm DOCX_TOOL exists ("which pandoc"). For EVERY letter2.md that passed
STAGE 5, render the Word version IN THE SAME DIRECTORY:

  pandoc "{LETTERS_DIR}/{name}/{location}/{PER_LETTER_MD}" \
    -o "{LETTERS_DIR}/{name}/{location}/{PER_LETTER_DOCX}"

Notes:
  * Convert from the verified {PER_LETTER_MD} ONLY. Never hand-edit the docx,
    and never inject extra text during conversion.
  * Because each {PER_LETTER_MD} ends cleanly at the To: block, the resulting
    {PER_LETTER_DOCX} carries the letter and nothing else — no notes, no
    comments. (APPENDIX B.)
  * If pandoc is missing, stop and report it rather than producing partial
    output; soffice (LibreOffice) is a fallback only if explicitly chosen.

Output to stdout:
============================
STAGE 6 COMPLETE
DOCX tool: pandoc <version>
letter2.docx files written: N / N
============================

============================
STAGE 7 — FINAL VERIFY
============================

* Confirm every envelope produced exactly one directory containing BOTH
  {PER_LETTER_MD} and {PER_LETTER_DOCX}.
* Confirm directory count == envelope count, with unique {name}/{location}
  paths and no collisions.
* Spot-open 2-3 of the .docx files (or convert back to text) and confirm the
  body is the letter, the recipient/address match the envelope, and there is
  NO trailing notes/comment text.
* Confirm {LETTER_FILE} is still unchanged.

Output to stdout:
============================
STAGE 7 COMPLETE
Envelopes: N | Directories: N | letter2.md: N | letter2.docx: N
Recipient/address match: passed | No-notes in docx: passed
Master letter.md unchanged: yes
ALL DONE
============================

============================
CONTENT RULES
============================

* The master {LETTER_FILE} is READ-ONLY for this prompt. Never edit it. Every
  change lives only in a per-recipient copy under {LETTERS_DIR}/.
* One directory per envelope: {LETTERS_DIR}/{name}/{location}/. {name} is the
  person (or title); {location} is the unique place name. Same person + many
  places = many location subdirectories under that person.
* Customize each copy enough to be appropriate for who is reading it — the
  salutation, the opening ask/framing, and the bottom To: block — while
  keeping every required element (four laws, links, video, forcing-function,
  ChatGPT tip, author intro + offer, signature) intact.
* Never fabricate a person, a title, an address, a phone, an email, or a URL.
  Use only what {ENVELOPES_FILE} / {INFO_FILE} verify. STAGE 2 may add only
  web-verified, sourced people/places.
* The phrase "puppet master" is banned from all output.
* The campaign domain is ALWAYS displayed in CamelCase:
  WhoAssassinatedCharlieKirk.com.
* Defamation-safe: do not state as established fact that any living person
  committed a crime; frame the investigation as the citizen effort it is.
* CRITICAL — NO NOTES IN THE LETTER FILES. A {PER_LETTER_MD} contains the
  letter and ends at the bottom To: block. Do NOT append a comments section,
  notes, an HTML comment, a confirm/BEFORE-MAILING block, a TODO, or any other
  commentary. Anything appended will surface in the Word document and break it.
  See APPENDIX B.

============================
APPENDIX A — CUSTOMIZATION BY RECIPIENT
============================

Rewrite the SALUTATION and the OPENING ASK/FRAMING to fit the reader. Keep the
body's required elements and the late author-intro + offer. Mirror the tone
already used in the {WORK_DIR}/emails/*.eml tailoring.

A1. {PRINCIPAL} himself (e.g. Washington_DC, La_Grange_KY, Ashland_KY,
    Campaign_Newport_KY copies addressed to "The Honorable Thomas Massie"):
  * Salutation: "Dear Representative Massie:".
  * Keep the master's direct, personal ask: that HE recommend and pass the
    four laws, or at minimum formally propose them; the laws are already
    written; he can adopt as-is or upgrade.

A2. Named congressional staff (Chief of Staff, Legislative Director,
    Communications Director / Press Secretary, District Director, etc.):
  * Salutation: "Dear Mr./Ms. {LastName}:" (or "Dear {Full Name}:").
  * Opening ask: that THEY put the four drafted laws in front of the
    Congressman and help move them through the process — he can adopt them
    as-is or upgrade them, but the writing is done; the ask is that he
    recommend and pass them, or at minimum propose them.
  * For a Communications Director / Press Secretary, lead the framing with the
    PUBLIC forcing-function value and the explainer video.

A3. Campaign staff (Campaign Manager, Campaign Finance Director, Campaign
    Treasurer — named or title-only):
  * Salutation: "Dear {Name}:" if known, else "Dear {Title}:".
  * Opening ask: same mission, framed for the campaign side — route the four
    laws and the explainer video to Rep. Massie and his team.

A4. Title-only recipients (no verified name):
  * Salutation: "Dear {Title}:" (e.g. "Dear Campaign Manager:").
  * Body acknowledges we are reaching the office/role and asks them to carry
    the request to the Congressman.

A5. Pronouns: when the reader is NOT Massie, "you" is the staffer/role and
    Massie is "the Congressman" / "Rep. Massie". When the reader IS Massie,
    "you" is Massie (as in the master).

A6. The author intro + offer paragraph stays LATE (near the close), as in the
    master: {AUTHOR} owns and runs WhoAssassinatedCharlieKirk.com; the offer
    of calls, answers on any schedule, the work itself, and help navigating
    the drafting and the legislative process.

============================
APPENDIX B — THE NO-NOTES RULE (CRITICAL)
============================

The whole point of letter2.md is to render a CLEAN letter2.docx. Anything
extra in the markdown shows up in Word.

  * A {PER_LETTER_MD} contains, in order: the date, the salutation, the body,
    the signature block, the bottom From: block, the bottom To: block — and
    then it ENDS. The last line of the file is the last line of the To: block.
  * Do NOT append, anywhere in the file (top or bottom):
      - HTML comments (<!-- ... -->),
      - a "BEFORE MAILING" / "CONFIRM" block,
      - "Notes:", "TODO", reviewer comments, changelog, or metadata,
      - a horizontal-rule-and-commentary footer.
  * The only divider allowed is the same plain dashed separator the master
    uses between the signature and the From:/To: address blocks.
  * Before STAGE 6, grep each letter copy for "<!--", "BEFORE MAILING",
    "CONFIRM", "TODO", and "Note:" — every count must be zero. If any are
    present, delete them from that copy (never from the master) before
    rendering the docx.
