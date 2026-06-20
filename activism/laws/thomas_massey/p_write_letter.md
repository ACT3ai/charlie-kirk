ROOT_DIR dir is ~/BGit/Bryan_git/charlie-kirk

WORK_DIR dir is {ROOT_DIR}/activism/laws/thomas_massey

NEEDS_FILE is file {WORK_DIR}/needs.txt
LETTER_FILE is file {WORK_DIR}/letter.md
INFO_FILE is file {WORK_DIR}/massy_info.yaml
ENVELOPES_FILE is file {WORK_DIR}/envelops.yaml
EMAILS_DIR is directory {WORK_DIR}/emails

AUTHOR is Bryan Starbuck
RECIPIENT is Representative Thomas Massie
CAMPAIGN_SITE is https://whoassassinatedcharliekirk.com
FIX_OVERVIEW is https://whoassassinatedcharliekirk.com/Fix/overview
YOUTUBE_LINK is https://www.youtube.com/watch?v=1RbDMiEReys

============================
GOAL
============================

This prompt produces FOUR outputs:

  1. {LETTER_FILE}     — a finished, ready-to-mail personal letter from
                         {AUTHOR} to {RECIPIENT}, written FROM {NEEDS_FILE}.
  2. {INFO_FILE}       — a YAML file of researched contact information about
                         {RECIPIENT}: every place we can mail a letter, and
                         every staff/campaign person and job title we should
                         address a letter to.
  3. {ENVELOPES_FILE}  — a YAML mailing list of ENVELOPES. One envelope per
                         (person × location) pairing: every person we can
                         address, at every location where that person can
                         actually receive mail. This is the address book a
                         print-and-mail run iterates over. Built by
                         multiplying the locations in {INFO_FILE} by the
                         people in {INFO_FILE} and assigning each person to
                         the location(s) where mailing them makes sense.
  4. {EMAILS_DIR}/*.eml — one email per PERSON (the email version of the
                         letter), each slightly tailored to that person and
                         their role, with To/Subject headers pre-filled from
                         that person's verified email when we have one.

WEB SEARCH IS ENABLED AND REQUIRED for {INFO_FILE}. Use WebSearch and
WebFetch to find current, real, verifiable contact information. Never
fabricate an address, a name, or a title — if it cannot be verified,
mark it unverified (see STAGE 6).

Read {NEEDS_FILE} and write {LETTER_FILE}: a finished, ready-to-mail
personal letter from {AUTHOR} to {RECIPIENT}.

{NEEDS_FILE} is the requirements/checklist for the letter. It is NOT the
letter. It lists everything the letter must contain and accomplish. The
letter is written FROM that file, and the finished {LETTER_FILE} must
comply with EVERY need listed in {NEEDS_FILE}.

The output is a PERSONAL LETTER that will be physically printed and mailed.
It is not a web page, not a memo, not an email. It reads like one serious
citizen writing to one Congressman. Warm where warmth is earned, direct
everywhere, never fawning, never form-letter.

============================
STAGE 1 — READ THE NEEDS
============================

* Read {NEEDS_FILE} in full.
* Extract and hold in memory:
    GOAL_OF_LETTER     — the ask (championing/sponsoring the four laws, or
                         at minimum proposing them) and why "at least
                         propose" still wins (the forcing-function argument).
    FRAMING_TONE       — how to frame Massie and the overall tone.
    AUTHOR_INTRO       — how to introduce {AUTHOR}.
    THE_FOUR_LAWS      — the four law titles and the {FIX_OVERVIEW} link.
    YOUTUBE            — {YOUTUBE_LINK}.
    THE_OFFER          — what {AUTHOR} commits to do for Massie.
    THE_AI_TIP         — the ChatGPT/AI pass-over-the-law tip.
    FORCING_FUNCTION   — the strategic integrity-test argument.
    CHECKLIST          — the compliance checklist (Section 9 of {NEEDS_FILE}).
* Note the "OPEN ITEMS / TO CONFIRM" section. Treat any unconfirmed item
  with a sensible, safe default (see STAGE 4) rather than blocking.

Output to stdout:
============================
STAGE 1 COMPLETE
Needs file loaded: yes
Checklist items found: N
Open items noted: N
============================

============================
STAGE 2 — PLAN THE LETTER
============================

Decide the letter's structure before writing. A personal letter, top to
bottom, roughly:

  1. Sender block + date (top-left, mailing-letter format).
  2. Recipient block (Rep. Thomas Massie + office address).
  3. Salutation ("Dear Representative Massie,").
  4. Opening — who I am and why I am writing (AUTHOR_INTRO), kept short
     and credible.
  5. Why him — the FRAMING_TONE: betrayed by election fraud, one of the
     last uncorrupted, fights for the people, not controlled by a puppet
     master. Honest and serious, not flattering.
  6. The ask — GOAL_OF_LETTER: champion/sponsor the four laws, or at
     minimum propose them.
  7. The forcing-function argument — FORCING_FUNCTION: proposing the laws
     puts every member on record, separates honest from corrupt even
     inside the Republican party.
  8. The four laws — name them and point to {FIX_OVERVIEW}; include the
     {YOUTUBE_LINK} explainer video. Note they are modeled on the Epstein
     disclosure approach.
  9. The AI tip — THE_AI_TIP: he or his staff can run ChatGPT passes over
     the law text to pressure-test it and build/refine the tiers fast.
 10. My offer — THE_OFFER: phone calls, answer anything, do the work,
     help navigate the legislative process and drafting.
 11. Close — earnest, patriotic sign-off and signature block for {AUTHOR}.

Keep it to roughly one to two pages when printed. Every paragraph earns
its place. No filler.

Output to stdout:  STAGE 2 COMPLETE — letter outline planned (11 parts)

============================
STAGE 3 — WRITE THE LETTER
============================

Write {LETTER_FILE} following the STAGE 2 plan and satisfying every item
in CHECKLIST.

Required content (all must appear):
  * Addressed to {RECIPIENT}.
  * Framing: betrayed by election fraud; one of the last uncorrupted;
    fights for the people; not controlled by a puppet master.
  * Clear ASK: champion/sponsor the four laws — or at least propose them.
  * Forcing-function rationale, stated explicitly.
  * Introduces {AUTHOR}: technology/engineering background, leading the
    "Who Assassinated Charlie Kirk" effort, heavy citizen investigator of
    the Sept 10, 2025 Utah Valley University assassination, site
    {CAMPAIGN_SITE}.
  * The four laws by name:
      1. FBI & DOJ Disclosure
      2. Intelligence Disclosure
      3. Mandate the Investigation
      4. Trusted Investigators
  * Link to the laws: {FIX_OVERVIEW}
  * Explainer video: {YOUTUBE_LINK}
  * My offer: phone calls, answer anything, do the work, navigate the law.
  * ChatGPT tip: use it to vet the law and build the tiers fast.
  * Respectful, direct, patriotic tone throughout.

Output to stdout:  STAGE 3 COMPLETE — {LETTER_FILE} written

============================
STAGE 4 — UNCONFIRMED ITEMS (SAFE DEFAULTS)
============================

For any item under "OPEN ITEMS / TO CONFIRM" in {NEEDS_FILE} that is not
yet confirmed, use these defaults so the letter is complete and never
blocks on a missing fact:

  * Bryan's background line: a brief, credible technology/engineering
    descriptor only. Do not invent specific employers, titles, dates, or
    credentials that are not stated in {NEEDS_FILE}.
  * Massie's office address: insert a clearly marked placeholder block,
    e.g.:
        [Rep. Thomas Massie — confirm current office mailing address]
    so the author can fill it before printing. Do NOT fabricate an address.
  * Law URLs: list the {FIX_OVERVIEW} entry point. Listing the four
    individual deep-links is optional; only add them if {NEEDS_FILE}
    supplies them.

At the very BOTTOM of {LETTER_FILE}, after the signature, add a short
HTML-comment block (not part of the printed letter) listing every
placeholder/assumption used, so the author knows exactly what to confirm
before mailing:

  <!--
  BEFORE MAILING — CONFIRM:
  - Massie's correct office mailing address (placeholder above).
  - Bryan's professional background line.
  - (any other defaulted item)
  -->

Output to stdout:  STAGE 4 COMPLETE — defaults applied, confirm-block added

============================
STAGE 5 — VERIFY AGAINST THE CHECKLIST
============================

Re-read {LETTER_FILE} and confirm EVERY CHECKLIST item from {NEEDS_FILE}
is satisfied. Walk the list literally, one box at a time:

  [ ] Addressed to Rep. Thomas Massie.
  [ ] Framing present (election fraud betrayal; uncorrupted; fights for
      the people; no puppet master).
  [ ] Clear ASK present (champion/sponsor — or at least propose).
  [ ] Forcing-function rationale present.
  [ ] Bryan introduced (background + leading campaign + investigator).
  [ ] Laws link present: {FIX_OVERVIEW}
  [ ] YouTube link present: {YOUTUBE_LINK}
  [ ] Offer present (calls, answer anything, do the work, navigate law).
  [ ] ChatGPT tip present (vet law + build tiers fast).
  [ ] Respectful, direct, patriotic tone.

If any item is missing, edit {LETTER_FILE} to add it, then re-verify.

Output to stdout:
============================
STAGE 5 COMPLETE
Checklist items satisfied: 10/10
Missing items fixed: N
Letter ready to mail: yes (pending confirm-block items)
============================

============================
STAGE 6 — RESEARCH MASSIE CONTACTS (WEB SEARCH) → WRITE INFO_FILE
============================

WEB SEARCH IS REQUIRED HERE. Use WebSearch and WebFetch to research
{RECIPIENT} and write {INFO_FILE} as YAML.

PURPOSE
  We want to mail this letter to as MANY valid destinations as possible,
  and to as MANY of the right PEOPLE (by name and by job title) as
  possible. {INFO_FILE} is the address book that drives that mailing.

WHAT TO FIND — ADDRESSES (find as many as you can):
  * The official U.S. House / Congressional offices — the Washington, D.C.
    office AND every Kentucky district office. The D.C. congressional
    office is the one we use to "sign off and send to Congress for him
    exactly" — mark it as best_for_congress.
  * His CAMPAIGN office address(es) (the re-election campaign / "Massie
    for Congress" committee mailing address).
  * His campaign FINANCE / committee treasurer address (often on FEC
    filings).
  * His HOME / residence (Garrison / Lewis County, KY area) IF it can be
    found from public sources. If not reliably found, say so — do not guess.
  * Any other valid place a constituent letter can be mailed (PO boxes,
    additional district offices, etc.).

WHAT TO FIND — PHONE, EMAIL, WEBSITES (for every office and person you can):
  * Phone numbers — D.C. office, each district office, campaign, and any
    direct staff lines you can verify.
  * Email addresses — official contact emails, the house.gov web-form URL
    (most House offices use a contact form rather than a public email),
    campaign email, and any verifiable staff/press emails.
  * Websites — official site (massie.house.gov), the campaign website, his
    contact/web-form page, FEC committee page, and official social media
    profile URLs (X/Twitter, Facebook, etc.).

WHAT TO FIND — HOW TO ADDRESS THE LETTER:
  * The correct formal salutation and envelope/recipient lines for a sitting
    U.S. Representative (e.g. envelope "The Honorable Thomas Massie",
    salutation "Dear Representative Massie:" or "Dear Congressman Massie:").
  * The correct way to address a letter to a staff member or campaign role
    by title when no name is known.
  * Capture this in the how_to_address section of {INFO_FILE} (below) so the
    mailing uses correct, respectful form.

WHAT TO FIND — PEOPLE & JOB TITLES (find as many as you can):
  * Named staff: Chief of Staff, District Director, Communications
    Director / Press Secretary (PR people), Legislative Director,
    Scheduler, and any others.
  * Campaign staff: campaign manager, campaign finance manager / finance
    director, treasurer, fundraising/PR staff — everyone you can verify
    on the campaign and campaign-finance side.
  * The distinct JOB TITLES themselves. We will write a letter to each
    job title even when we do not have a person's name — addressing it to
    the top title in that office (e.g. "Chief of Staff", "Campaign
    Finance Director", "Press Secretary").

SEARCH GUIDANCE
  * Suggested queries: "Thomas Massie district office address",
    "Thomas Massie Washington DC office Rayburn", "Massie for Congress
    campaign address", "Thomas Massie campaign finance director treasurer
    FEC", "Thomas Massie chief of staff communications director",
    "Thomas Massie press secretary".
  * Prefer authoritative sources: massie.house.gov, the official House
    directory, FEC.gov filings, Ballotpedia, LegiStorm, reputable news.
  * Cross-check each address/name against at least one source; record the
    source URL.

OUTPUT — {INFO_FILE} (YAML)
  Single root key: thomas_massie. Properties nested at level 2 / level 3
  under it. Use this shape (extend lists with as many real entries as you
  verify):

    thomas_massie:
      full_name: Thomas Harold Massie
      office: U.S. Representative, Kentucky's 4th Congressional District
      party: Republican

      # How to correctly address the letter (formal form).
      how_to_address:
        envelope_recipient_line: The Honorable Thomas Massie
        inside_address_lines:
          - The Honorable Thomas Massie
          - U.S. House of Representatives
          - <D.C. office street + room>
          - Washington, DC <zip>
        salutation: "Dear Representative Massie:"   # or "Dear Congressman Massie:"
        addressing_a_staffer_by_title: "Dear <Title> (e.g. Dear Chief of Staff):"
        source: <url>
        verified: true

      # Phone / email / websites / social, rolled up for quick reference.
      contact_channels:
        websites:
          - label: Official House site
            url: https://massie.house.gov
            source: <url>
            verified: true
          - label: Contact web form
            url: <house.gov contact form url>
            source: <url>
            verified: true
          - label: Campaign website
            url: <url or null>
            source: <url>
            verified: true
          - label: FEC committee page
            url: <url or null>
            source: <url>
            verified: true
        social_media:
          - platform: X (Twitter)
            url: <url or null>
            verified: true
          - platform: Facebook
            url: <url or null>
            verified: true
        emails:
          - label: <office/campaign/press>
            email: <email or null — many House offices use a web form only>
            source: <url>
            verified: true
        phones:
          - label: Washington, D.C. Office
            phone: <phone or null>
            source: <url>
            verified: true
          - label: <District Office — city>
            phone: <phone or null>
            source: <url>
            verified: true

      mailing_addresses:
        congressional:
          - label: Washington, D.C. Office
            best_for_congress: true   # the one to send to Congress for him
            recipient_line: The Honorable Thomas Massie
            street: <building, room/suite, street>
            city_state_zip: Washington, DC <zip>
            phone: <phone if found>
            email_or_form: <email or web-form url if found>
            website: <office page url>
            source: <url>
            verified: true            # true | unverified
          - label: <District Office — city>, KY
            best_for_congress: false
            street: <...>
            city_state_zip: <...>
            phone: <...>
            email_or_form: <...>
            website: <...>
            source: <url>
            verified: true
        campaign:
          - label: Massie for Congress (campaign)
            street: <...>
            city_state_zip: <...>
            phone: <...>
            email_or_form: <...>
            website: <...>
            source: <url>
            verified: true
        campaign_finance:
          - label: Campaign committee / treasurer (FEC)
            street: <...>
            city_state_zip: <...>
            phone: <...>
            source: <url>
            verified: true
        home:
          - label: Residence
            city_area: <Garrison / Lewis County, KY, etc.>
            street: <street if reliably found, else null>
            source: <url>
            verified: unverified      # only set true if well-sourced

      people:
        congressional_staff:
          - name: <full name or null>
            title: Chief of Staff
            office: Washington, D.C.
            phone: <phone or null>
            email: <email or null>
            source: <url>
            verified: true
          - name: <full name or null>
            title: Communications Director / Press Secretary
            phone: <phone or null>
            email: <email or null>
            source: <url>
            verified: true
        campaign_staff:
          - name: <full name or null>
            title: Campaign Manager
            phone: <phone or null>
            email: <email or null>
            source: <url>
            verified: true
          - name: <full name or null>
            title: Campaign Finance Director
            phone: <phone or null>
            email: <email or null>
            source: <url>
            verified: true

      # Every distinct job title we will address a letter to, even when
      # no person's name is known (address it to the title at the top
      # office). One letter per title.
      job_titles_to_mail:
        - The Honorable Thomas Massie
        - Chief of Staff
        - District Director
        - Communications Director / Press Secretary
        - Legislative Director
        - Campaign Manager
        - Campaign Finance Director
        - Campaign Treasurer

NEVER FABRICATE. If a field is not verified, set its value to null and set
verified: unverified, and (if useful) add a note: line explaining what is
missing. It is correct and expected for some fields (especially home) to
be null.

Output to stdout:
============================
STAGE 6 COMPLETE
Mailing addresses found: N (congressional: N, campaign: N, finance: N, home: N)
best_for_congress address set: yes/no
Phones found: N | Emails/forms found: N | Websites found: N | Social: N
how_to_address captured: yes
Named people found: N
Distinct job titles to mail: N
Unverified fields flagged: N
============================

============================
STAGE 7 — VERIFY INFO_FILE
============================

* Confirm {INFO_FILE} is valid YAML with single root key thomas_massie.
* Confirm at least one congressional address exists and exactly one entry
  has best_for_congress: true.
* Confirm campaign and campaign_finance sections are present (entries or
  an explicit empty/unverified note if nothing could be found).
* Confirm contact_channels (websites, emails/web-form, phones, social) and
  how_to_address (envelope line, inside address, salutation) are present.
* Confirm every address/person entry carries a source and a verified flag.
* Confirm job_titles_to_mail lists every distinct title gathered, with at
  minimum: the Congressman himself, Chief of Staff, and a Press/PR title.
* Spot-check that no address or name is fabricated — each verified: true
  entry must trace to a source URL.

Output to stdout:
============================
STAGE 7 COMPLETE
INFO_FILE valid YAML: yes
best_for_congress entries: 1
Sourced entries: N/N
Job titles to mail: N
Fabrication check: passed
============================

============================
STAGE 8 — BUILD THE ENVELOPES (PEOPLE × LOCATIONS) → {ENVELOPES_FILE}
============================

PURPOSE
  Produce {ENVELOPES_FILE}: the mailing list. We want to mail the letter to
  as MANY of the right PEOPLE, at as MANY valid PLACES, as we can. So we
  build the CROSS PRODUCT of locations and people:

      envelopes = { (person, location) : person can receive mail at location }

  One envelope (one array entry) per (person, location) pairing. The same
  person who can be reached at two places (e.g. someone who travels between
  the Washington, D.C. office and the Kentucky home-state district office)
  gets an envelope at BOTH places, so a letter reaches them wherever they
  are. Massie himself gets an envelope at every location we have.

INPUTS — pull entirely from {INFO_FILE} (do not re-research, do not invent):
  * LOCATIONS = every entry under mailing_addresses:
      - each congressional office (the D.C. office and EACH district office),
      - each campaign address,
      - the campaign_finance / treasurer address,
      - home ONLY if a real, verified street address exists (it usually does
        not — skip home if street is null).
  * PEOPLE = the Congressman himself, plus every entry under people
      (congressional_staff + campaign_staff), plus every distinct entry in
      job_titles_to_mail that is not already covered by a named person.
      A title with no known name is still a person to mail — address it to
      the title.

ASSIGN EACH PERSON TO LOCATION(S) — who is at which place:
  * The Honorable Thomas Massie (the Congressman): mail at EVERY location —
    the D.C. office, every district office, every campaign address, and the
    finance/treasurer address. He receives everywhere.
  * Chief of Staff, Legislative Director, Communications Director / Press
    Secretary, Scheduler, and other Washington staff: the D.C. office. If a
    person plausibly splits time between D.C. and the district (commonly the
    Chief of Staff and the District Director), give them an envelope at BOTH
    the D.C. office AND the primary district office.
  * District Director and district-based staff: each district office.
  * Campaign Manager, Campaign Finance Director: the campaign mailing
    address.
  * Campaign Treasurer: the campaign_finance / FEC treasurer address (and
    the campaign address if distinct).
  * NEVER pair a person with a location that does not exist in {INFO_FILE}.
    Only real, listed locations. If the only sensible location for a person
    is itself unverified, still emit the envelope but carry that unverified
    status into the description.

OUTPUT — {ENVELOPES_FILE} (YAML)
  Single root key: envelopes. Its value is an ARRAY. Each array entry is
  named Mail_1, Mail_2, Mail_3 … (carried in the mail_id field) and has
  EXACTLY these Level-3 properties, in this order:

    envelopes:
      - mail_id: Mail_1
        name: <addressee line — person's full name + title if known;
               otherwise the title alone, e.g. "Chief of Staff, Office of
               Rep. Thomas Massie". For the Congressman: "The Honorable
               Thomas Massie">
        mailing_address_line_1: <street / building + room / PO box>
        mailing_address_line_2: <city, state ZIP — or null if unknown>
        phone_number: <best phone for this location, or null>
        email_address: <verified email for this person/location, or null —
               House offices typically have none; put the web form in
               website, not here>
        website: <relevant site: official office page, campaign site, FEC
               page, or the contact web-form URL>
        description: >
          One to two sentences: WHO this addressee is (role), HOW we are
          reaching them (this location / channel and why it fits them), and
          WHY we are writing them (their part in moving the four laws). End
          with the verification status of the address (verified or
          unverified, mirroring {INFO_FILE}).
      - mail_id: Mail_2
        ...

  ORDER the entries: the Congressman first (D.C., then each district, then
  campaign, then finance), then D.C. staff, then district staff, then
  campaign staff. Number mail_id sequentially in that final order.

NEVER FABRICATE. Every address, phone, email, and website must trace to a
verified entry in {INFO_FILE}. Use null for anything unknown and say so in
the description. Do not invent a person, a title, or a place.

Output to stdout:
============================
STAGE 8 COMPLETE
Locations used: N | People used: N
Envelopes (person × location pairings) written: N
Massie envelopes (one per location): N
Entries with a verified address: N/N
============================

============================
STAGE 9 — WRITE ONE EMAIL PER PERSON (.eml) → {EMAILS_DIR}/
============================

PURPOSE
  The email version of the letter. ONE email per PERSON (not per location —
  email is per person; a person reachable at two locations still gets ONE
  email). Each email is tailored slightly to that person and their role.

PEOPLE = the same distinct set used for the envelopes: the Congressman, each
named staffer, and each distinct job title to mail. Dedupe across locations
so each person/title is emailed exactly once.

CONTENT — adapt the letter into email prose, a little shorter than the
printed letter, KEEPING every required element from STAGE 3 (the four laws
by name, the {FIX_OVERVIEW} link, the {YOUTUBE_LINK} video, {AUTHOR}'s
intro, the offer, the ChatGPT tip, the forcing-function argument). Tailor
the ask to the recipient's role:
  * To the Congressman: the full personal ask — champion/sponsor the four
    laws, or at minimum propose them.
  * To a Chief of Staff / Legislative Director: ask them to put this in
    front of the Congressman and help move it through the process.
  * To a Communications Director / Press Secretary: lead with the public
    forcing-function value and the explainer video.
  * To campaign staff (Manager / Finance Director / Treasurer): the same
    mission, framed for the campaign side, asking them to route it to Massie.

FILE FORMAT — a valid .eml (RFC-822-style) file per person:

    To: "<Name or Title>" <email-if-verified-else-leave-blank>
    From: Bryan Starbuck <fill before sending>
    Subject: <specific, serious subject tailored to the person>
    X-Intended-Recipient: <Name and/or Title, and the office/campaign>
    X-Note: <only when no verified email — say the address is a placeholder
             and to use the office web form {INFO_FILE} lists>
    (blank line)
    <email body — the tailored email letter, signed by {AUTHOR} with the
     {CAMPAIGN_SITE} link>

  * PRE-FILL the To: and Subject: lines. Pull the To: email from the
    person's verified email in {INFO_FILE} when one exists. Most House staff
    emails are NOT public — when no verified email exists, write To: with the
    name/title and an empty or clearly-marked placeholder address, and add
    the X-Note header pointing to the web form. Never invent an email.
  * Subject example: "Four laws to force an honest Charlie Kirk
    investigation — a request for Rep. Massie".

FILE NAMING — {EMAILS_DIR}/{person_name}.eml, where {person_name} is the
person's full name when known, otherwise their job title, with EVERY space
and special character replaced by a single underscore. Examples:
  Thomas_Massie.eml
  Matt_Gurtler.eml
  Chief_of_Staff.eml
  Communications_Director_Press_Secretary.eml
Create {EMAILS_DIR} if it does not exist.

Output to stdout:
============================
STAGE 9 COMPLETE
Emails written: N
Filenames: <list>
With a verified To: email: N | With placeholder + X-Note: N
============================

============================
STAGE 10 — VERIFY ENVELOPES + EMAILS
============================

* Confirm {ENVELOPES_FILE} is valid YAML with single root key envelopes
  whose value is an array.
* Confirm every entry has all eight fields (mail_id + the seven properties)
  and that mail_id values are Mail_1..Mail_N with no gaps.
* Confirm the Congressman appears once per location (D.C., each district,
  each campaign, finance).
* Confirm no envelope pairs a person with a location absent from {INFO_FILE},
  and no address/phone/email/website was fabricated.
* Confirm {EMAILS_DIR}/ contains exactly one .eml per distinct person/title,
  every filename uses underscores only (no spaces or special characters),
  and every file has To:, From:, and Subject: headers plus a body.
* Confirm each email carries every required content element from STAGE 3.

Output to stdout:
============================
STAGE 10 COMPLETE
Envelopes valid YAML: yes | Envelopes: N | mail_id sequence intact: yes
Emails: N | All filenames sanitized: yes | All headers present: yes
Fabrication check: passed
============================

============================
CONTENT RULES
============================

* The output is a personal, physically-mailed letter — write it as prose
  letters are written, not as a web page or bulleted memo. Light, sparing
  use of a short list is fine (e.g. naming the four laws or the offer), but
  the body is paragraphs.
* Tone: respectful, direct, patriotic, earnest. One citizen who fights for
  the country writing to a Congressman who does the same. Not fawning.
* First person ({AUTHOR}) throughout.
* Never fabricate facts about {AUTHOR}, about Massie, or about the case.
  Use only what {NEEDS_FILE} supplies; placeholder anything unknown.
* Defamation-safe: this letter references the Charlie Kirk assassination
  investigation. Do not state as established fact that any living person
  committed a crime. Frame the investigation as the citizen effort it is.
* Include all required URLs exactly as written:
    {FIX_OVERVIEW}
    {YOUTUBE_LINK}
    {CAMPAIGN_SITE}
* No emojis. No decorative formatting. Plain, serious letter formatting.
* This prompt has FOUR outputs, all regenerated each run:
    - {LETTER_FILE}, written from {NEEDS_FILE}.
    - {INFO_FILE}, the YAML contact research (web search required).
    - {ENVELOPES_FILE}, the YAML envelope list (people × locations) built
      from {INFO_FILE}.
    - {EMAILS_DIR}/*.eml, one tailored email per person.
* {INFO_FILE} must never contain a fabricated address, name, title, phone,
  email, or URL. Anything unverified is null with verified: unverified.
  Every verified: true entry must trace to a real source URL.
* {ENVELOPES_FILE} and the .eml emails are built ONLY from verified data in
  {INFO_FILE}. Never pair a person with a location not in {INFO_FILE}, and
  never invent an email address for a To: line — leave it blank with an
  X-Note when unknown.
* Every .eml is the email version of the same letter and must still satisfy
  every CHECKLIST item from {NEEDS_FILE}, tailored to its recipient's role.
* .eml filenames use underscores only — no spaces or special characters.
