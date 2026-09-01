ROOT_DIR dir is ~/BGit/Bryan_git/charlie-kirk

SITE_DIR dir is {ROOT_DIR}/site
DOCS_DIR dir is {SITE_DIR}/docs
COURT_DIR dir is {DOCS_DIR}/court
AIATT_DIR dir is {COURT_DIR}/ai_attorney

COURT_CHARTER is file {COURT_DIR}/CLAUDE.md
ROOT_CHARTER is file {ROOT_DIR}/CLAUDE.md
ASSESS_MANUAL is file {ROOT_DIR}/prompts/Assess_Manual.md
CK_FILE is file {ROOT_DIR}/Charlie_Kirk.txt
CK_INBOX is file {ROOT_DIR}/Charlie_Kirk_AI_Inbox.txt

PAGES_CSV is file {ROOT_DIR}/pages.csv
LEVEL_2_CSV is file {ROOT_DIR}/level_2.csv
PEOPLE_CSV is file {ROOT_DIR}/people.csv

LEGAL_DOCS_DIR dir is {COURT_DIR}/legal_docs
LEGAL_MD_DIR dir is {LEGAL_DOCS_DIR}/_markdown
LEGAL_TEXT_DIR dir is {LEGAL_DOCS_DIR}/_text
LEGAL_WORK_DIR dir is {LEGAL_DOCS_DIR}/_work
TRACKING_TXT is file {LEGAL_DOCS_DIR}/tracking.txt
FILINGS_PDF_DIR dir is {SITE_DIR}/internals/static/court/filings

DAYS_DIR dir is {COURT_DIR}/Days_in_Court
PRELIM_DIR dir is {COURT_DIR}/Preliminary_Hearing
MIRANDIZE_DIR dir is {COURT_DIR}/mirandize
SCORE_CARD_DIR dir is {COURT_DIR}/score_card

WORK_DIR dir is {AIATT_DIR}/_work
LEDGER_CSV is file {WORK_DIR}/ledger.csv
THESIS_MAP_CSV is file {WORK_DIR}/thesis_map.csv
EVIDENCE_CSV is file {WORK_DIR}/evidence_links.csv
RUN_LOG is file {WORK_DIR}/run_log.md
MDX_CHECK is file {SITE_DIR}/_ck_mdxcheck.mjs

THIS_PROMPT is file {AIATT_DIR}/p_ai_attorney.md

CASE_NO is the value 251403576
CASE_NAME is the value "State of Utah v. Tyler James Robinson"
COURT_NAME is the value "Fourth Judicial District Court, Utah County, Provo"
JUDGE is the value "Hon. Tony F. Graf, Jr."

AS_OF_DATE is the date this run is executed. Write it out in full on every page
  that states a case posture. The last run stated a posture as of 2026-08-31.

AGENT_COUNT is 9        (one agent per APPENDIX A thesis; grows with Appendix A)
EFFORT is high
MAX_SENTENCE_WORDS is 22

Read these into the context window BEFORE writing anything:
  * {COURT_CHARTER}   - the charter for this whole court directory
  * {ROOT_CHARTER}    - the Pages CSV contract, the page-level contract, the
                        CK_FILE read-only rule, and the meeting no-names rule
  * {ASSESS_MANUAL}   - the site-wide writing and layout standard
  * {AIATT_DIR}/method.mdx and {AIATT_DIR}/trial-cursor.mdx - the rules and the
                        case posture this section already publishes


============================
GOAL
============================

Run an AI DEFENSE ATTORNEY as a separate, imaginary defense team for
{CASE_NAME}, Case No. {CASE_NO} - a different team from the real lawyers of
record for Tyler Robinson - and publish what that team would do, page by page,
under {AIATT_DIR}.

The output is a GAP ANALYSIS in two halves, and every page in this section is
built around that split:

  LEFT   what our AI defense attorney would do. The motion it would file, the
         record it would demand, the witness it would call, and the exact
         question it would ask that witness.

  RIGHT  what the real-world record shows. Has that stage of the case happened
         yet or is it still upcoming? Did that witness actually take the stand?
         On what date? Does the material we hold show the question being asked?

The section exists because this site's evidence review concludes that Charlie
Kirk was killed by an explosive device - most plausibly a shaped charge in or
on the microphone - and not by the rifle round of the government's account.
That is a physical claim. Physical claims are decided in courtrooms by motions,
subpoenas and experts. This section is about those instruments.

It also exists because, on the public record as we can see it, the defense has
litigated the case inside the frame the State built. Nothing visible to us
questions foreign involvement, the intelligence services, or the federal
handling of the scene. Whether that is strategy, sealing, or a decision we
cannot see is exactly what a reader is invited to judge - and what the
{SCORE_CARD_DIR} section is for.

THIS PROMPT IS RUN REPEATEDLY. It is not a one-shot generator. Most of this
section already exists and much of it is good. A re-run REVIEWS AND IMPROVES.
It does not clear the ground and start over. See PRESERVATION CONTRACT below.


============================
WHERE THIS FILE LIVES, AND WHY IT DOES NOT PUBLISH
============================

{THIS_PROMPT} sits inside a Docusaurus docs directory, which would normally
make it a live page. It does not become one: {SITE_DIR}/docusaurus.config.ts
excludes "**/p_*.{md,mdx}" and "**/_*/**". That is what keeps this prompt and
{WORK_DIR} private.

  * Keep the p_ prefix on this file. Renaming it publishes it.
  * Keep the underscore on {WORK_DIR}. Renaming it publishes the ledger.
  * Never create any other .md or .mdx under {AIATT_DIR} that is not meant to
    be a public page.


============================
WHAT ALREADY EXISTS - DO NOT REBUILD IT
============================

As of the last run {AIATT_DIR} holds 25 published pages. Open them before
writing. They are the reference implementation and the house voice.

FOUR SPINE PAGES:

  overview.mdx        the section front door: the cursor block, the checklist
                      table, the clustered link list, the full page index
  method.mdx          the rules this section follows, and the section that
                      states plainly what the real defense team is doing WELL
  trial-cursor.mdx    where the case is right now, and the 15-row stage table
  case-stage-map.mdx  which file tracks which stage of the case

TWENTY-ONE INSTRUMENT PAGES, in four clusters:

  Cluster A - mechanism of death
    explosive-residue-testing, soil-excavation-subpoena, security-team-clothing,
    transport-suv-custody, independent-autopsy-review,
    microphone-hardware-subpoena, blast-and-acoustics-experts,
    scene-alteration-spoliation
  Cluster B - the federal witnesses nobody called
    fbi-agents-on-the-stand, bomb-dogs-and-eod-sweep,
    hospital-and-transport-record
  Cluster C - the foreign-nexus defense
    alternative-perpetrator-notice, nctc-halted-inquiry-subpoena,
    tpusa-organizational-subpoenas, family-and-organization-witnesses,
    fort-huachuca-records
  Cluster D - forensics, suppression and process
    ballistics-daubert-challenge, confession-suppression-motion,
    independent-device-reexamination, brady-enforcement-and-sanctions,
    gag-order-and-publicity

Every one of those 21 pages already carries the same eight H2 sections in the
same order. That template is settled. Do not invent a new one.

WHAT IS MISSING, and what this prompt exists to add: the 21 pages are
INSTRUMENTS. They are individual motions and subpoenas. There is no page that
carries ONE THESIS end to end - the chain of reasoning from what we contend, to
the facts on this site that support it, to every question we would ask to prove
it, to whether anyone asked. APPENDIX A is that list of theses, and the THESIS
PAGES are the layer this prompt adds on top of the instruments.

Concrete coverage gap measured at the last run: APPENDIX A theses 5, 6, 7 and 8
- the two drivers the police were sent after, the aircraft and rental cars, the
Israeli-registered handsets on campus, and the university-owned house - have NO
instrument page and NO thesis page anywhere in {AIATT_DIR}. Those are the
largest holes in the section.


============================
THE THREE PAGE FAMILIES
============================

FAMILY 1 - SPINE PAGES. The four listed above. Rebuilt in STAGE 7 to stay
consistent with whatever the run changed. Never deleted.

FAMILY 2 - THESIS PAGES. One page per APPENDIX A item. Level 3, in
{AIATT_DIR}, filename is the thesis slug from APPENDIX A. This is the page
family this prompt is chiefly about, and THE TABLE below is its centre. A
thesis page answers: we contend X - what would we do to prove X in a courtroom,
and what does the record show actually happened?

FAMILY 3 - INSTRUMENT PAGES. The 21 above, plus new ones. One page per single
motion, subpoena, expert retention or witness. An instrument usually serves more
than one thesis, and a thesis usually needs several instruments. That
many-to-many mapping is recorded in {THESIS_MAP_CSV} and is what lets a thesis
page link to its instruments instead of repeating them.

A thesis page NEVER duplicates the body of an instrument page. It states the
chain of reasoning, carries THE TABLE, and links out.


============================
THE TABLE - THE HEART OF A THESIS PAGE
============================

Every thesis page carries one table, headed "## The Gap Analysis". It is the
left-and-right comparison this whole section is built to deliver. One row per
question or demand. Rows are ordered by how load-bearing they are, most
important first, not chronologically.

Canonical column set. Use exactly these headers, in this order:

| # | What we would do, and of whom | Stage and date | Witness took the stand? | Asked on the record we hold? | How we checked |

  #                             row number, stable across runs so a reader can
                                cite "thesis 4, row 7"
  What we would do, and of whom the actual question in quotation marks, or the
                                actual demand, plus the named target. Write the
                                question the way it would be spoken in a
                                courtroom. Not a topic label.
  Stage and date                which stage of the case this belongs to, and the
                                date it happened or the note that it is not yet
                                due. Link the date to its {DAYS_DIR} page when
                                one exists.
  Witness took the stand?       Yes with the date, No, or n/a for a records
                                demand with no witness.
  Asked on the record we hold?  Not found / Asked / Partly / Not yet due. See
                                the VERIFICATION TIERS rule - this column is
                                about OUR MATERIAL, never about counsel.
  How we checked                the tier letter and the source. "T1 - certified
                                transcript, Day 4, searched" is a real answer.
                                "T4 - sealed" is also a real answer.

Below the table, always, three short blocks:

  ### Where this chain breaks the State's case
     Two or three sentences. If every row on the left came back the way we
     expect, what does the prosecution lose? Name the link in the causal chain.

  ### What would defeat this thesis
     Written honestly and made to bite. The single result that would end this
     thesis as a physical or legal proposition. A thesis with no such row is not
     a thesis, it is an assertion, and it should be marked as one.

  ### The instruments that serve this thesis
     A bullet list of links to the FAMILY 3 pages that carry the actual motions,
     from {THESIS_MAP_CSV}.


============================
THE PAGE TEMPLATE - INSTRUMENT PAGES
============================

Copy {AIATT_DIR}/explosive-residue-testing.mdx and follow it exactly. It is the
golden example. The eight H2 sections, in this order, none omitted, none added
without a note in the run log:

  ## The One Thing We Would Do Differently
       One blockquote stating the single step, in one sentence. Then two to
       four paragraphs of why.
  ## What The Defense Team Did Instead
       What the real record shows, in the permitted language only. Always ends
       by stating that this is an observation about the public record and that
       the filings are gagged and partly sealed.
  ## Where This Belongs In The Case
       Four-row table: stage / when that stage runs / status of this step.
  ## Witness Or Discovery Target
       Table: how it would be done / target / took the stand? / status on the
       record we hold.
  ## The Questions That Were Not Asked
       A numbered list of the actual cross-examination questions. Written as
       spoken questions, addressed to a named witness where one exists.
  ## Why A Defense Attorney Would Want This
       The strategic case. Two or three paragraphs.
  ## The Honest Counterargument
       Written to persuade, not to be knocked down. Why competent counsel might
       deliberately not do this. This section is mandatory and it is never
       token. On several pages it is the stronger argument and the page says so.
  ## Sources On This Site
       Bullet list of internal links, verified to resolve.

Every page in both families also carries, in this order:

  * the frontmatter block, matching the existing pages field for field
  * the ck-full-bleed marker div
  * the blue back button to /court/ai_attorney/overview
  * the H1
  * the :::caution Legal Disclaimer block, verbatim from the existing pages
  * the body
  * the horizontal rule, then the :::danger Theoretical Exercise Only block,
    verbatim - see the DISCLAIMER CONTRACT in STAGE 2
  * the {/* CK_AUTHOR_CREDIT */} marker and the author credit line


============================
VERIFICATION TIERS - HOW WE ARE ALLOWED TO SAY "NOT ASKED"
============================

This is the honesty rule of the section and it constrains every right-hand
column on every page.

We hold only TWO certified preliminary-hearing transcripts - Day 4 and Day 5,
under {LEGAL_MD_DIR}/transcripts. We do not hold certified transcripts for
Days 1, 2 and 3. Anything said about those days comes from press and pool
reporting, and press reporting does not record every question asked.

Tag every right-hand assertion with a tier:

  T1  CERTIFIED. A certified transcript we hold covers that witness on that day,
      and a search of it shows the line present or absent. This is the only tier
      that supports the words "was not asked".
  T2  FILING. A filed document in {LEGAL_MD_DIR} or {FILINGS_PDF_DIR} shows the
      motion made or not on the docket we hold.
  T3  PRESS. Press, pool or secondary reporting only.
  T4  NOT CHECKABLE. Sealed, gagged, or a stage not yet reached.

Rules that follow from the tiers, and they are absolute:

  * At T1 you may write "the transcript does not show this line being pursued".
  * At T2 you may write "no filing in the archive we hold requests this".
  * At T3 and T4 you may ONLY write "not found in the material we hold" or "not
    visible on the public record". Never "the defense did not", never "counsel
    failed to", never "was never asked".
  * Where a stage has not been reached, the right-hand cell is "Not yet due",
    and the page says so plainly. A step that is not yet due HAS NOT been
    missed, and every page repeats that.
  * Absence of a filing in an archive that holds 258 of 867 docket entries is
    weak evidence of anything. Say the ratio when leaning on absence.


============================
PRESERVATION CONTRACT - THIS PROMPT RUNS MANY TIMES
============================

A re-run must leave the section strictly better than it found it. The failure
mode this contract exists to prevent is a later run regenerating a page from
scratch and losing research that an earlier run did well.

  * READ THE WHOLE EXISTING PAGE BEFORE CHANGING ONE LINE OF IT. Every re-run
    begins by reading the current file top to bottom.
  * IMPROVE IN PLACE. Add rows, sharpen questions, upgrade a T3 claim to T1
    when a transcript arrives, correct a date, tighten prose. Do not rewrite a
    section that is already right just to make it sound like this run wrote it.
  * NEVER DELETE RESEARCH TO MAKE A PAGE TIDIER. Length is not a defect.
  * A DELETION IS A LOGGED EVENT. Removing a page, a table row, a numbered
    question or an H2 section requires a row in {LEDGER_CSV} naming what was
    removed and why, and a line in {RUN_LOG}. Legitimate reasons: it was wrong,
    it was superseded by a better-sourced version, it was a duplicate, it broke
    a rule in STAGE 2. "It did not fit my outline" is not a reason.
  * WHEN THE RECORD CONTRADICTS AN EARLIER RUN, SAY SO ON THE PAGE. Do not edit
    around it. Write the correction plainly - a witness did testify after all, a
    motion was in fact filed, a date was wrong. This site corrects itself in the
    open. See the equivalent rule for flight-data recovery in {ROOT_CHARTER}.
  * NEVER TOUCH {SITE_DIR}/sidebars.ts.
  * NEVER WRITE TO {CK_FILE}. It is read-only to AI, without exception. New
    investigation content goes to {CK_INBOX}. See {ROOT_CHARTER}.
  * DO NOT COMMIT. An external auto-commit sweeper handles the working tree.


============================
HARD PROHIBITIONS
============================

* NEVER write to {CK_FILE}. Read only. Append to {CK_INBOX} instead.
* NEVER touch {SITE_DIR}/sidebars.ts.
* NEVER use an HTML comment in a .mdx or .md file under {DOCS_DIR}. A bare
  <!-- --> compiles locally and fails the GitHub Pages MDX build, which freezes
  the ENTIRE live site on its last good commit. Use {/* */} everywhere.
* NEVER name an attendee or likely attendee of the possible September 9, 2025
  Fort Huachuca meeting. Not a full name, not a first name, not initials, not a
  handle, not a rank or job description narrow enough to identify one person.
  This rule comes from {ROOT_CHARTER} and it governs this section too. The
  existing fort-huachuca-records.mdx obeys it by demanding DOCUMENTS - visitor
  logs, flight manifests, scheduling records - and naming nobody. Match that.
* NEVER state as fact that any living person committed a crime, destroyed
  evidence, lied, or acted improperly. See STAGE 2.
* NEVER assert that the real defense team erred, was negligent, was compromised,
  or is failing its client. See STAGE 2.
* NEVER put a page under {AIATT_DIR} without the closing disclaimer block.
* NEVER indent a closing </div> to any column but zero. Only the real build
  catches an indented closing tag and it fails the deploy.
* Do not create new CSS. Reuse ck-full-bleed and the existing inline styles.


============================
STAGE 0 - GROUND TRUTH AND THE RUN LEDGER
============================

Done once by the coordinator, before any agent is launched. Deterministic work
only. No agent redoes it.

* mkdir -p {WORK_DIR}
* Read {COURT_CHARTER}, {ROOT_CHARTER}, {ASSESS_MANUAL}.
* Read the four spine pages in {AIATT_DIR} in full.
* Inventory the section:
    ls {AIATT_DIR}/*.mdx
    for f in {AIATT_DIR}/*.mdx; do grep -c '^## ' "$f"; done
  Record every page, its H2 count, its line count, and whether it carries the
  closing disclaimer block.
* Build or refresh {LEDGER_CSV}. One row per page under {AIATT_DIR}:

    page_key,file,family,thesis_ids,last_run_date,state,verify_tier_high,
    disclaimer_ok,notes

    family        spine | thesis | instrument
    thesis_ids    semicolon-separated APPENDIX A ids this page serves, e.g. T1;T2
    state         missing | draft | complete | needs_rework
    verify_tier_high  the BEST tier any claim on the page rests on
    disclaimer_ok yes|no

  The ledger is what makes the run resumable. A wave that stops early is not a
  failure so long as the ledger says exactly what is done and what is not.
* Build or refresh {THESIS_MAP_CSV}:

    thesis_id,thesis_slug,instrument_page_key,relationship,note

    relationship  primary | supporting | gateway
    gateway       means the instrument must be filed FIRST or everything
                  downstream of it is irrelevant and gets quashed. The
                  alternative-perpetrator notice is the gateway for T3, T4, T6
                  and T7. Mark it that way and never let a thesis page propose a
                  foreign-nexus subpoena without pointing at its gateway first.
* Read {THIS_PROMPT}'s APPENDIX A and check every thesis has a row.
* Append a dated header to {RUN_LOG} for this run.


============================
STAGE 1 - REFRESH THE RECORD BEFORE WRITING ABOUT IT
============================

The case moves. A page that states a stale posture is worse than no page. This
stage runs on every execution of this prompt, before any page is touched.

* Read {TRACKING_TXT}. It carries the completeness scoreboard - at the last
  count 867 docket entries known, 62 sealed, 258 with a public PDF ever posted,
  374 unique PDFs held, 378 markdown conversions - and a CONFIRMED GAPS list.
  That gap list is where a defense attorney would push, and it feeds APPENDIX C.
* Regenerate the held-files index if the archive changed on disk:
    python3 {LEGAL_WORK_DIR}/gen_tracking.py
  Everything below the hand-maintained sentinel in {TRACKING_TXT} is preserved
  across runs. Never hand-edit the FILES HELD block.
* HUNT FOR WHAT IS NEW SINCE THE LAST RUN. Utah's courts publish nothing
  directly. The two working sources are the Burkhart substack docket
  reconstruction and charliefiles.com; see the "Court docket sources" material
  and the fetch logs and manifests under {LEGAL_WORK_DIR}. Look for:
    - any ruling on bind-over
    - any new certified transcript, especially Days 1, 2 and 3, which would
      upgrade a large number of T3 claims to T1
    - any newly unsealed filing
    - any new hearing date
* DOWNLOAD AND KEEP EVERYTHING. New PDFs go under {FILINGS_PDF_DIR}, one
  markdown conversion each under {LEGAL_MD_DIR} on the same relative path.
  NEVER overwrite or delete a document already held. If a filing is re-posted in
  a different form, keep both and let the difference be the record. A PDF placed
  under {DOCS_DIR} is not served and 404s for every visitor - that is why PDFs
  live under {SITE_DIR}/internals/static/.
* Re-read {DAYS_DIR}, {PRELIM_DIR} and {MIRANDIZE_DIR} for anything the rest of
  the site learned since the last run.
* UPDATE THE CURSOR. If anything moved, rewrite trial-cursor.mdx now - the
  posture block, the 15-row stage table, the next date - and restate the
  AS_OF_DATE. Every other page in this section keys off it.
* Write to {RUN_LOG} what was found, what was downloaded, and what changed. If
  nothing moved, say that: "no docket movement since <date>" is a real result.


============================
STAGE 2 - THE FRAMING AND DEFAMATION PASS
============================

This stage is mandatory, it runs on EVERY execution, and it runs TWICE: once
here, over what already exists, and again in STAGE 9 over what this run wrote.
Nothing publishes without it.

WHAT THIS SECTION IS, IN ITS OWN WORDS. Every page states, and every page must
remain consistent with, this framing:

  This is an ACADEMIC EXERCISE and a COMPARISON ANALYSIS. It is a written model
  of how an idealised defense attorney might approach this case, published so a
  reader can compare it against the real one and reach their own conclusions.
  It is a study of what MAY WELL HAVE BEEN DONE DIFFERENTLY.

  WE MAKE NO CLAIM THAT ANYTHING UNETHICAL OR ILLEGAL WAS DONE BY ANYBODY. Not
  by the defense team, not by the prosecution, not by the court, not by any
  agency, not by any witness, not by any named or unnamed individual.

THE DISCLAIMER CONTRACT. Every single page under {AIATT_DIR} - spine, thesis and
instrument alike, with no exception - carries BOTH of these blocks:

  * Near the top, immediately under the H1, the :::caution Legal Disclaimer
    block: Tyler Robinson is charged, not convicted, and is presumed innocent;
    nothing on the page states as fact that any living person committed a crime,
    destroyed evidence, or acted improperly; filings are gagged and sealed so
    the public record is incomplete by design.

  * At the very bottom, above the author credit, after a horizontal rule, the
    :::danger Theoretical Exercise Only block. It states that the page is a
    theoretical exercise; that WE MAKE NO CLAIM THAT THERE IS ANY PROBLEM WITH
    THE CURRENT DEFENSE ATTORNEY, any member of the defense team, or any
    decision they have made; that real capital defense runs under a gag order,
    with sealed filings, on full discovery the public has never seen; that
    counsel of record know facts we do not; that a step described as "not on the
    public record" may already have been taken privately, may have been
    considered and rejected for good reason, or may not yet be due; that silence
    in the public record is NOT evidence of a failure; and that nothing here is
    legal advice, a criticism of any licensed attorney, or an allegation of
    professional misconduct.

  Copy both blocks VERBATIM from the existing pages. Do not paraphrase them, do
  not shorten them, do not let a page carry a variant wording. They are boiler
  plate on purpose - identical text on every page is what makes the disclaimer
  credible rather than decorative.

  Verify mechanically, and treat any failure as a blocking defect:

    for f in {AIATT_DIR}/*.mdx; do
      grep -q 'Theoretical Exercise Only' "$f" || echo "MISSING BOTTOM: $f"
      grep -q 'Legal Disclaimer' "$f"         || echo "MISSING TOP: $f"
    done

BANNED LANGUAGE. Scan every page this run touched, and in this stage every page
in the directory, for these constructions and rewrite each one:

  * "the defense failed to", "counsel neglected", "they should have", "an
    obvious miss", "incompetent", "ineffective assistance", "malpractice",
    "sandbagging", "throwing the case", "compromised counsel"
  * any sentence that makes silence in the public record into a finding about a
    lawyer rather than a fact about our own visibility
  * "X covered it up", "X destroyed evidence", "X lied", "X ordered the
    killing", "X is an operative", stated flat about any living person
  * "hand off" / "handed off" in any description of the security detail reaching
    Charlie Kirk - it implies a deliberate transfer. Write "the security team
    reaching Charlie" instead.

PERMITTED REPLACEMENTS. These are the phrases the section uses, and they are
sufficient for everything it needs to say:

  * "not visible on the public record"
  * "not found in the material we hold"
  * "the certified transcript we hold does not show this line being pursued"
  * "no filing in the archive we hold requests this"
  * "not yet due at this stage of the case"
  * "citizen investigators contend", "according to <source>", "reportedly"
  * "our AI defense attorney would ask" - the whole left column is written in
    this conditional voice and never as an accusation

THE THESES ARE OURS, AND THEY ARE POSITIONS, NOT FINDINGS. APPENDIX A contains
strong contentions about foreign involvement, intelligence services and federal
conduct. They are published as the positions an imaginary defense team would
ADVANCE and would have to PROVE. Every thesis page must:

  * open by saying it is a contention this exercise would attempt to prove, and
    what evidence would be required to prove it
  * carry the "What would defeat this thesis" block, written to bite
  * attribute every underlying factual claim to the page on this site that
    carries it, so the claim rests where it was made and is not re-asserted here
  * name no living private individual as a participant in a crime. A thesis may
    say what an ORGANISATION or a STATE is contended to have done, and may
    demand records from it. It may not accuse a person.

THE CURRENT DEFENSE POSTURE - HOW TO SAY IT. It is fair and necessary to
observe that nothing visible to us shows the defense questioning foreign
involvement, the intelligence services, or the federal handling of the scene,
and that the visible litigation sits inside the frame the State built. Say it
in that form - an observation about what WE can see - and immediately pair it
with the reasons competent counsel might choose exactly that: a gag order, an
alternative-perpetrator notice that has not come due, the risk of two
inconsistent stories in front of one jury, and the plain fact that counsel hold
full discovery we have never seen.

WHAT THE DEFENSE IS DOING WELL STAYS ON THE PAGE. method.mdx carries a section
naming the real team's genuine wins - the inconclusive ATF comparison that is in
the record because the DEFENSE called the examiner, three defense-called
forensic experts, the custody-and-confession-timing attack, the April 2026
motion to stop further testing of the bullet jacket fragment. That section is
part of the method, not a courtesy. Keep it, and add to it whenever STAGE 1
turns up another one.


============================
STAGE 3 - RECONCILE APPENDIX A AGAINST WHAT EXISTS
============================

* For each thesis in APPENDIX A, decide its state:
    - has a thesis page, current           -> improve in STAGE 5
    - has a thesis page, stale             -> rework in STAGE 5
    - has instruments but no thesis page   -> write the thesis page in STAGE 5
    - has neither                          -> write both, thesis first
* Record the decision in {LEDGER_CSV} and in {RUN_LOG}.
* MAP EVERY EXISTING INSTRUMENT PAGE TO ITS THESES in {THESIS_MAP_CSV}. An
  instrument with no thesis is a signal in both directions: either APPENDIX A is
  missing a thesis, or the instrument belongs to conventional capital defense
  and its thesis_ids column is simply "-". Cluster D is mostly the latter and
  that is fine.
* GROW APPENDIX A WHEN THE RECORD SUPPORTS IT. This prompt's APPENDIX A is not
  frozen. A new thesis is added when all four hold:
    1. it is a contention about the case that a defense could actually advance,
    2. it is supported by material already published somewhere on this site,
    3. there is at least one concrete instrument - a motion, a subpoena, a named
       witness, a records demand - that would test it, and
    4. it can be written without naming a living private individual as a
       participant in a crime.
  Append it to APPENDIX A in {THIS_PROMPT} with the next free id, a slug, and a
  one-paragraph statement. Note it in {RUN_LOG}. Never renumber existing ids -
  readers and {THESIS_MAP_CSV} both cite them.
* A thesis may also be RETIRED, if the record has closed it. Retiring means
  marking it retired in APPENDIX A with the date and the reason, and rewriting
  its page to say plainly what closed it. It does NOT mean deleting either one.
  A thesis this site advanced and then abandoned is part of the record.


============================
STAGE 4 - PARTITION THE WORK ACROSS AGENTS
============================

* Launch one agent per APPENDIX A thesis that STAGE 3 marked as needing work,
  up to {AGENT_COUNT} in parallel. Each agent owns exactly one thesis: its
  thesis page, plus any NEW instrument page that thesis needs.
* An instrument page has exactly ONE owning agent, recorded in {THESIS_MAP_CSV}
  as its primary thesis. Two agents must never edit the same file. Where an
  instrument serves several theses, the non-owning agents link to it and do not
  touch it - if they need a change there, they write the request to {RUN_LOG}
  and the coordinator applies it in STAGE 7.
* Every agent is handed, in its brief: this prompt's STAGE 2, the VERIFICATION
  TIERS, the PRESERVATION CONTRACT, the page template, its own APPENDIX A
  entry, its rows from {THESIS_MAP_CSV}, and the golden example
  {AIATT_DIR}/explosive-residue-testing.mdx.
* Agents do not edit spine pages, {LEDGER_CSV}, {PAGES_CSV} or APPENDIX A. They
  report what those need; the coordinator applies it in STAGE 7 and STAGE 9.
* An agent that finishes reports: files written, rows added to THE TABLE, the
  highest verification tier it reached, every claim it could not source, and
  every question it wanted to ask but could not ask without naming someone.


============================
STAGE 5 - BUILD OR IMPROVE ONE THESIS PAGE
============================

This is the per-agent stage. Everything here is done for ONE thesis.

STEP 1 - READ BEFORE WRITING.
  * If the page exists, read it top to bottom, all of it, before touching a
    line. Note what is already good. The PRESERVATION CONTRACT applies from
    this moment.
  * Read every instrument page mapped to this thesis.
  * Read the Level 2 areas named in the thesis's APPENDIX A entry. Use
    {LEVEL_2_CSV} to find them - it is far cheaper than walking the tree and its
    description column exists to answer exactly this question.
  * Read the certified transcripts under {LEGAL_MD_DIR}/transcripts for every
    witness this thesis would cross. That is the only way to reach tier T1.
  * Search {CK_FILE} for the thesis subject. It is read-only and it is the
    densest source in the repo.

STEP 2 - BUILD THE CHAIN OF REASONING.
  Before writing prose, write down, as a numbered chain: the facts this site
  already holds, in the order they build, ending in the contention. Each link
  cites the page on this site that carries it. A link with no page behind it is
  either research to do first or a link to drop. This chain is what separates a
  thesis page from an opinion.

STEP 3 - BUILD THE TABLE.
  Every row starts on the left with a real, speakable question or a specific,
  servable demand. Then fill the right side against the VERIFICATION TIERS, and
  do it honestly - a table where every row says "not found" is a table that has
  not been checked.
  * Aim for eight to twenty rows on a mature thesis page.
  * On a re-run, keep existing rows and their numbers. Add new rows at the
    bottom. Upgrade a tier in place when better material arrives and note the
    upgrade in {RUN_LOG}.
  * A row whose right side changed since the last run is the most valuable
    thing this section produces. Say so on the page.

STEP 4 - WRITE THE PAGE.
  Section order for a thesis page:

    ## What We Contend
         The thesis in one blockquote, then two or three paragraphs. Opens by
         saying it is a contention this exercise would attempt to prove.
    ## The Chain Of Reasoning
         The numbered chain from STEP 2, every link hyperlinked to its source
         page on this site.
    ## The Gap Analysis
         THE TABLE, then the three blocks under it - where this chain breaks
         the State's case, what would defeat this thesis, the instruments that
         serve it.
    ## What Would Have To Be Obtained
         The evidence that does not exist in any public form and would have to
         be compelled. Distinguish the reachable from the unreachable: a private
         organisation's contracts are reachable; an agency's classified holdings
         mostly are not, and the page says which it is asking for.
    ## The Honest Counterargument
         Mandatory, same standard as the instrument pages. Written to persuade.
    ## Sources On This Site
         Verified internal links.

STEP 5 - SEQUENCE DISCIPLINE.
  The most common error in public discussion of this case is proposing an
  intelligence subpoena with no procedural step to make it relevant. Any thesis
  whose {THESIS_MAP_CSV} row names a gateway instrument must point at that
  gateway BEFORE it proposes anything downstream, and must say plainly that
  without it the downstream subpoena is irrelevant and gets quashed. Write in
  the order a court would require, not the order the internet argues it.

STEP 6 - SELF-CHECK against STAGE 2 before reporting done.


============================
STAGE 6 - BUILD OR IMPROVE AN INSTRUMENT PAGE
============================

Same reading discipline as STAGE 5 STEP 1. Then the eight-section template
under THE PAGE TEMPLATE, no deviation.

Priority order for NEW instruments, because it matches what a court would
actually grant and what is still physically testable:

  1. Things that are perishable. Items that still exist but may not later -
     residue on retained items, a vehicle not yet released, footage inside a
     retention window. These are always first.
  2. Things reachable without fighting any agency. Subpoenas duces tecum to
     private parties - the university, the event organiser, the AV vendor, the
     hotel, the rental company, the carrier. Courts grant these routinely.
  3. Things that need only the court and the State. Rule 16 motions, motions to
     compel, sanctions practice, independent re-examination of items the State
     already holds.
  4. Things that need the gateway first. Every foreign-nexus and intelligence
     demand. Never write one of these without pointing at the gateway.
  5. Things a court would almost certainly refuse. Write these anyway when they
     matter, and say on the page that they would likely be refused and why. A
     demand that will be denied still creates a record of the refusal, and the
     refusal is itself a publishable fact.

The four known missing instrument clusters, from the last coverage measurement:

  * T5 - the two drivers police were sent after. Instruments: the dispatch and
    CAD record, the sequence of who directed that pursuit and when, the
    detention and release records, and the question of who was already at the
    address on arrival. Written as a records demand about DECISIONS AND TIMING,
    naming no private individual as a participant in anything.
  * T6 - aircraft and vehicles. Instruments: subpoena to the rental companies
    for agreements in the window, airport ground-handling and FBO records, and
    the ADS-B material this site has already recovered under {DOCS_DIR}/Planes.
    That recovery work is unusually strong evidence-handling and the instrument
    page should lean on it and link to it.
  * T7 - handsets on campus. Instruments: the demand for the tower dumps and any
    cell-site material the State holds, the extraction reports, and the
    foundational question of what was collected versus what was analysed. Write
    this one with particular care: it is the thesis most likely to slide into
    naming people, and it must stay a demand for RECORDS.
  * T8 - the university-owned house. Instruments: subpoena to the university for
    occupancy, keying, booking and access records for the property in the
    window; any camera coverage of the frontage; and the vehicle records
    associated with it. {DOCS_DIR}/After/house carries this line of inquiry and
    has its own charter - read it first.


============================
STAGE 7 - REBUILD THE SPINE
============================

Coordinator only, after every agent has reported.

* overview.mdx
    - The cursor block at the top, restated from trial-cursor.mdx. These two
      must never disagree.
    - A NEW top section, "The Nine Contentions" (or however many APPENDIX A
      holds), listing every thesis in APPENDIX A order, each hyperlinked to its
      thesis page, each with one line saying what it contends. This is the table
      of contents that correlates one-to-one with APPENDIX A and it goes ABOVE
      the instrument checklist.
    - The existing instrument checklist table, updated: one row per instrument,
      its cluster, its link, its position. Keep the three defined position
      values and their definitions.
    - The clustered link list with its one-line summaries.
    - The full page index.
    - The peer-directory block and Related Areas.
* method.mdx - fold in any new rule this run adopted, and any new item for the
  "what the defense team is actually doing well" section.
* trial-cursor.mdx - already refreshed in STAGE 1. Confirm it still matches.
* case-stage-map.mdx - add every new page to the stage mapping.
* Apply any change an agent requested to a file it did not own.
* Cross-link the peers, in both directions where it makes sense:
    {SCORE_CARD_DIR}   the reader's own scoring sheet - this section supplies
                       the areas, the score card is where the reader decides
    {LEGAL_DOCS_DIR}   the primary sources every claim should be checkable
                       against
    {DAYS_DIR}, {PRELIM_DIR}, {MIRANDIZE_DIR}


============================
STAGE 8 - APPENDIX C, THE EVIDENCE LINKAGE
============================

APPENDIX C is a placeholder that grows on every run. It is the bridge between a
row in THE TABLE and the actual artefact that would prove it.

* Maintain {EVIDENCE_CSV}:

    evidence_key,thesis_ids,kind,title,held,location,tier,page_links,note

    kind      filing | transcript | exhibit | image | video | dataset |
              record_demand | external
    held      yes | no | partial
    location  repo path if held; the CONFIRMED GAPS entry in {TRACKING_TXT} or
              the custodian if not
    tier      the verification tier this artefact can support

* Every run, do three things and only these three:
    1. Add a row for each new artefact STAGE 1 downloaded.
    2. Add a row, with held=no, for each thing a thesis page said would have to
       be obtained. That is the section's own discovery list, and it is the most
       useful output this exercise produces for anyone else.
    3. Reconcile against the CONFIRMED GAPS list in {TRACKING_TXT}, so the two
       do not drift apart.
* Do not publish {EVIDENCE_CSV} as a page yet. When it is rich enough to be
  worth reading, it becomes a Level 3 page under {AIATT_DIR} and this stage
  gains a step. Until then it is working state under {WORK_DIR}.


============================
STAGE 9 - VERIFY BEFORE REPORTING DONE
============================

Nothing is reported complete until every check here passes.

* DISCLAIMERS. Run the two-grep loop from STAGE 2 over every .mdx in
  {AIATT_DIR}. Any MISSING line is a blocking defect.
* BANNED LANGUAGE. Grep the directory for the banned constructions in STAGE 2.
  Every hit is either rewritten or justified in {RUN_LOG}.
* NO ATTENDEE NAMES. Re-read every page that touches the September 9 meeting
  and confirm no person is named or described into identifiability.
* NO HTML COMMENTS:
    grep -rn '<!--' {AIATT_DIR} && echo "BLOCKING: convert to {/* */}"
* MDX COMPILES:
    node {MDX_CHECK} {AIATT_DIR}/*.mdx
  It compiles pages the way the real Docusaurus build does. Then, when the run
  changed anything structural:
    cd {SITE_DIR} && npm run build
* LINKS RESOLVE. Check every internal link this run added against
  {SITE_DIR}/.docusaurus/routes.js, which is ground truth and takes seconds
  rather than a full build. Link a section overview as /X/overview, never as a
  bare /X.
* PAGES CSV. Add a row for every new page and refresh line_count on every page
  edited. Columns and the page_key convention are defined in {ROOT_CHARTER}.
  Existing keys use the aiatty_ prefix for this section - keep it.
* TIER AUDIT. No page asserts "was not asked" on anything below T1. Grep for the
  banned assertive forms and confirm each survivor has a T1 citation.
* TABLE INTEGRITY. Every thesis page has a Gap Analysis table; every row has all
  six columns filled; no row's right side is blank.
* LEDGER AND LOG. {LEDGER_CSV} matches what is on disk. {RUN_LOG} records: pages
  written, pages improved, rows added, tiers upgraded, deletions with reasons,
  theses added or retired, documents downloaded, and everything that could not
  be sourced.
* REPORT TO THE USER, in this shape:
    - what moved in the case since the last run
    - which theses were worked and what changed on each
    - new pages created
    - the strongest single finding this run produced
    - the strongest counterargument this run had to concede
    - what is blocked, and what would unblock it


============================
APPENDIX A - THE CONTENTIONS OUR AI DEFENSE ATTORNEY WOULD ADVANCE
============================

Nine theses. One page each. One agent each. Ids are permanent and are cited by
{THESIS_MAP_CSV}, by {LEDGER_CSV} and by readers - never renumber them.

Every entry below is a POSITION THIS EXERCISE WOULD ATTEMPT TO PROVE, not a
finding this site asserts, and every thesis page says so in its first paragraph.
None of them may be written in a way that accuses a living private individual of
a crime. See STAGE 2.

Format of each entry:
  id | slug | one-line statement
  CONTENTION      what the defense team would argue
  WOULD REQUIRE   what would actually have to be proved to a court
  READ FIRST      the Level 2 areas on this site that hold the material
  GATEWAY         the instrument that must come first, or "-"

----------------------------------------------------------------------
T1 | mechanism-of-death-explosive
    Charlie Kirk was killed by a shaped charge detonating in or on the
    microphone, and no bullet entered his body.

  CONTENTION    The fatal wound was caused by an explosive device at chest
                height, not by a .30-06 round fired from a rooftop. The
                mechanism of death in the State's theory is wrong.
  WOULD REQUIRE Wound morphology inconsistent with a rifle round; energetic
                residue on retained items, or a documented refusal to test for
                it; blast and acoustic analysis of the recorded sound; the
                microphone hardware itself and its custody chain.
  READ FIRST    Cause_of_Death, Mic, Proof_Not_Tyler, Gun_Bullet
  GATEWAY       -
  NOTE          This is the load-bearing thesis of the entire site. If it
                fails, the identity of the person on the roof starts mattering
                again and most of the rest of this section becomes secondary.
                It is also the most testable thesis here, by the cheapest
                procedure in forensic chemistry. Its instrument pages are the
                strongest in the section - build outward from them.

----------------------------------------------------------------------
T2 | federal-handling-and-nondisclosure
    Federal handling of the scene and of discovery has kept material out of the
    case, including the removal of roughly ten inches of earth.

  CONTENTION    The scene was altered and material was routed or withheld in a
                way that has left the defense unable to test the State's own
                theory - the excavated soil, the seized clothing, the transport
                vehicle, and documents not produced.
  WOULD REQUIRE The excavation work order and hauling manifest; the evidence
                inventory and lab request logs; the Brady record; and testimony
                from the people who made the routing decisions.
  READ FIRST    CoverUp, FBI, Proof_Intel_Services, Cause_of_Death
  GATEWAY       -
  NOTE          Write this as a DISCOVERY AND SPOLIATION thesis, which is what a
                court would hear, not as an accusation of a cover-up. The
                remedy sought is production, sanctions and an adverse-inference
                instruction. Those are real, grantable requests. "The FBI
                covered it up" is not a request a judge can rule on.

----------------------------------------------------------------------
T3 | foreign-decision-and-notification
    A foreign state decided on the assassination and key people in the United
    States were informed beforehand.

  CONTENTION    The decision originated outside the United States and there was
                advance notification inside it.
  WOULD REQUIRE Advance-knowledge evidence: the halted foreign-nexus inquiry and
                who halted it; communications records; the pattern of aircraft
                movements; and testimony from the official who has publicly said
                his inquiry was stopped.
  READ FIRST    Israel, Israel_Main_Suspect, Proof_Intel_Services, Motive,
                US_Intelligence
  GATEWAY       alternative-perpetrator-notice
  NOTE          The strongest ON-RECORD thread in this whole area is a named
                official stating publicly that a foreign-nexus inquiry was
                halted. That is a subpoena to a person who has already spoken,
                about his own statement - the most grantable request in the
                foreign-nexus family. Lead with it. Keep this page about STATES
                AND ORGANISATIONS and about records; it names no private person.

----------------------------------------------------------------------
T4 | direction-of-us-military-intelligence
    US military intelligence acted on foreign direction, including the
    procurement path of the microphone and the presence of particular personnel.

  CONTENTION    Elements of US military intelligence acted at foreign direction,
                and that direction reaches the hardware: the ordering of the
                microphone, the contracting and funding path behind it, and who
                was present.
  WOULD REQUIRE The full procurement chain for the AV equipment - purchase
                orders, contract vehicles, funding source, delivery and custody;
                and records establishing which units and personnel were present.
  READ FIRST    Mic, US_Intelligence, US_Intelligence_Assisted,
                Proof_Intel_Services, meeting
  GATEWAY       alternative-perpetrator-notice
  NOTE          The procurement half of this thesis is DOCUMENTARY and reachable
                - contracts, purchase orders and delivery records are ordinary
                subpoena targets against private vendors. The direction half is
                mostly unreachable and the page must say which half it is
                asking for in every demand. The meeting no-names rule applies in
                full anywhere this touches September 9, 2025.

----------------------------------------------------------------------
T5 | the-diverted-pursuit
    Police were sent after two people who were driving around, and that pursuit
    consumed the critical hours.

  CONTENTION    The direction of local police effort toward two individuals
                absorbed the first hours of the investigation, and federal
                personnel were already at the address when police arrived.
  WOULD REQUIRE The CAD and dispatch record; the sequence of who directed that
                pursuit and at what time; the detention and release
                documentation; and the arrival-order record at the address.
  READ FIRST    After, FBI, CoverUp, Killer, timeline_events
  GATEWAY       -
  NOTE          NO PAGE EXISTS FOR THIS YET. Write it as a TIMING AND
                DIRECTION-OF-EFFORT thesis built on dispatch records. Both
                individuals are living private people who have not been charged
                with anything: they are not named, not described into
                identifiability, and nothing about their state of mind is
                asserted. The demand is for records about DECISIONS, not about
                persons.

----------------------------------------------------------------------
T6 | aircraft-and-ground-vehicles
    Foreign intelligence used aircraft in support before and on the day, and
    associated ground vehicles were rented.

  CONTENTION    A pattern of aircraft movements supported the operation, and
                specific rental vehicles are associated with it.
  WOULD REQUIRE Flight records for the window, including the ADS-B material this
                site has recovered from archives after it was removed from live
                trackers; FBO and ground-handling records; and rental agreements
                for the window from the named companies.
  READ FIRST    Planes, Planes/following, Proof_Intel_Services, Israel
  GATEWAY       alternative-perpetrator-notice
  NOTE          NO PAGE EXISTS FOR THIS YET. This thesis has the best
                evidence-handling behind it of anything on this site - see the
                flight-data recovery work and its control-aircraft discipline in
                {ROOT_CHARTER}. CARRY THAT DISCIPLINE ONTO THE PAGE: never call
                a missing record a removal until a control aircraft has failed
                the same way, and publish the results that weaken the thesis as
                prominently as the ones that support it. Rental records are an
                ordinary subpoena to a private company and are the reachable
                half of this thesis.

----------------------------------------------------------------------
T7 | foreign-registered-handsets-on-campus
    Handsets purchased and registered on a foreign carrier were present on the
    UVU campus.

  CONTENTION    Devices registered to a foreign telecom were operating on campus
                and were connected to the operation.
  WOULD REQUIRE What cell-site and tower-dump material the State collected; what
                was analysed versus merely collected; the extraction reports;
                and the foundational testimony of whoever handled that material.
  READ FIRST    Proof_Intel_Services, technology_surveillance, Israel,
                court/Phone_Extraction, court/Robinson_Phone_Devices
  GATEWAY       alternative-perpetrator-notice
  NOTE          NO PAGE EXISTS FOR THIS YET, and this is the thesis most likely
                to slide into naming people. It must stay a demand for RECORDS
                and a set of foundational questions about collection and
                analysis. The genuinely strong and grantable question underneath
                it is narrow and answerable: what was collected, what was
                analysed, and what happened to the difference.

----------------------------------------------------------------------
T8 | the-university-owned-house
    A university-owned property close to the site was likely used, with operator
    vehicles in front of it.

  CONTENTION    A specific university-owned property near the site was used in
                connection with the operation.
  WOULD REQUIRE Occupancy, booking, keying and access records for the property
                in the window; camera coverage of its frontage; and the vehicle
                records associated with it.
  READ FIRST    After/house, Locations, property_locations, After
  GATEWAY       -
  NOTE          NO PAGE EXISTS FOR THIS YET. {DOCS_DIR}/After/house has its own
                charter - read it before writing. This is one of the most
                REACHABLE theses in Appendix A: a subpoena duces tecum to a
                university for its own property records is routine and does not
                require fighting any agency. Write it that way. Any current or
                former occupant is a living private person and is not named.

----------------------------------------------------------------------
T9 | withheld-exculpatory-material
    Exculpatory material exists in UVU footage and in federal holdings and has
    not been provided.

  CONTENTION    Material tending to exculpate exists - in campus video, and in
                intelligence and military holdings concerning the aircraft and
                the foreign nexus - and has not been produced to the defense.
  WOULD REQUIRE The full campus camera inventory and retention record; the
                production log against it; the Brady demands already made and
                the responses; and, for the federal holdings, the gateway first.
  READ FIRST    cameras, CoverUp, court/discovery-brady-disputes,
                Proof_Intel_Services
  GATEWAY       alternative-perpetrator-notice, for the federal half only
  NOTE          Split this page cleanly in two. The CAMPUS half is ordinary
                Brady and spoliation practice against a reachable custodian and
                is close to a certainty as a motion. The FEDERAL half is the
                hard one and depends on the gateway. Keeping them separate on
                the page is what keeps the reachable half from being dismissed
                along with the unreachable half.

----------------------------------------------------------------------
GROWING THIS APPENDIX. See STAGE 3. New ids continue at T10. Record every
addition and every retirement in {RUN_LOG} with the date and the reason.


============================
APPENDIX B - THE RECORD, AND WHERE TO GO GET MORE OF IT
============================

The court directory, which is the working material for this whole exercise:

  {COURT_DIR}/
    ai_attorney/        this section
      _work/            ledger, thesis map, evidence list, run log - private
      p_ai_attorney.md  this prompt - private, never publishes
    Days_in_Court/      one page per reported court date, 2025-09-16 onward
    legal_docs/         the primary-source archive - see below
      _markdown/        one .md per PDF: 2025/, 2026/, transcripts/, warrants/,
                        mirandize/, analysis/, misc/
      _text/            pdftotext and OCR sidecars
      _work/            docket reconstructions, fetch logs, manifests,
                        gen_tracking.py
      tracking.txt      the archive index and the completeness scoreboard
    mirandize/          the custody-timing line: if he was in custody with his
                        phone seized, who typed the message
    Preliminary_Hearing/ Day 1 through Day 4 pages
    score_card/         the reader's own scoring sheet
    plus the case-level Level 3 pages: ballistics-atf-cbla, case-overview,
    Cellebrite, defense-bindover-brief-aggravator, defense-team,
    discord-evidence-court, discovery-brady-disputes, gag-orders-sealing,
    hearing-witnesses, investigation-index, jaxson-fox-informant-order,
    judges, judge-tony-graf, judge-robert-lunnen, people-on-witness-stand,
    Phone_Extraction, preliminary-hearing-motions, prosecution-team,
    Robinson_Phone_Devices, testimony, Twiggs_Phone, utah-county-jail-custody

READING THESE IS THE WORK. The archive is what makes the right-hand column of
THE TABLE possible at all. An agent that writes a thesis page without opening
the transcripts has written an opinion piece.

WHAT WE HOLD, AT THE LAST COUNT. 867 docket entries known to exist; 62 marked
private or sealed; 258 with a public PDF ever posted; 374 unique PDFs held; 378
markdown conversions. The substantive shortfall is the CONFIRMED GAPS list in
{TRACKING_TXT}, not the raw arithmetic. Quote the ratio whenever a page leans on
the absence of a filing.

THE TRANSCRIPT SITUATION, AND WHY IT DOMINATES THE TIERS. We hold certified
transcripts for preliminary hearing Day 4 and Day 5 only, plus a redacted
transcript of the 2025-10-24 sealed-motion hearing. Days 1, 2 and 3 are covered
by press and pool reporting alone. That is why almost every "not asked" claim in
this section sits at T3 and must be worded as "not found in the material we
hold". OBTAINING THE DAY 1, 2 AND 3 CERTIFIED TRANSCRIPTS IS THE SINGLE HIGHEST
-VALUE ACQUISITION AVAILABLE TO THIS SECTION - it would upgrade a large number of
claims from T3 to T1 in one step. Make it the first item of STAGE 1 on every run
until it is done.

WHERE NEW DOCUMENTS COME FROM. Utah's courts publish nothing directly. The
working sources are the Burkhart substack docket reconstruction and
charliefiles.com; the fetch logs, TSVs and manifests under {LEGAL_WORK_DIR}
record what was pulled and when. Signed orders are frequently image-only and
need OCR. Keep every copy; never overwrite one.

OUTSIDE THIS REPO, but part of the same investigation:
  ~/BGit/all/politics/charlie_kirk/          prompts, research, laws, letters
  ~/BGit/all/politics/charlie_kirk/aiattorney/   an earlier question-and-answer
                                             run with its own input documents


============================
APPENDIX C - EVIDENCE LINKAGE (PLACEHOLDER, GROWS EVERY RUN)
============================

Maintained as {EVIDENCE_CSV} by STAGE 8. It starts thin and thickens. The point
is that every row of THE TABLE eventually points at a real artefact - held or
named-and-missing - instead of at a memory.

Seed rows to create on the first run that reaches this stage:

  evidence_key                    thesis  kind           held  note
  prelim_transcript_day4          T1;T2   transcript     yes   certified
  prelim_transcript_day5          T1;T2   transcript     yes   certified
  prelim_transcript_day1_3        T1;T2   transcript     no    HIGHEST PRIORITY
  ballistics_motion_apr2026       T1      filing         yes   defense motion to
                                                               stop further
                                                               testing of the
                                                               bullet jacket
  atf_comparison_result           T1      exhibit        partial sealed in part
  soil_excavation_workorder       T2      record_demand  no    custodian unknown
  lab_request_log                 T1;T2   record_demand  no    the list of tests
                                                               actually ordered
  microphone_hardware             T1;T4   exhibit        no    the device itself
  av_procurement_chain            T4      record_demand  no    private vendors -
                                                               reachable
  campus_camera_inventory         T9      record_demand  no    reachable
  cad_dispatch_record             T5      record_demand  no    reachable
  rental_agreements_window        T6      record_demand  no    reachable
  adsb_recovered_traces           T6      dataset        yes   in-repo, under
                                                               Planes
  university_property_records     T8      record_demand  no    reachable
  halted_inquiry_testimony        T3      external       no    the official has
                                                               already spoken
                                                               publicly

The "held=no, reachable" rows are, collectively, this exercise's discovery list.
That list is the most directly useful thing this section produces for anyone
else working the case, and it is why APPENDIX C exists.


============================
APPENDIX D - THE RUN LOG FORMAT
============================

{RUN_LOG} is append-only markdown. One block per run:

  ## Run <YYYY-MM-DD>

  Case movement since last run:
  Theses worked:
  Pages created:
  Pages improved:
  Table rows added / tiers upgraded:
  Deletions, with reasons:
  Appendix A changes:
  Documents downloaded:
  Could not source:
  Strongest finding this run:
  Strongest counterargument conceded this run:
  Blocked on:

The last two lines are not decoration. A run that produced no counterargument
worth conceding did not look hard enough, and a section that only ever confirms
what it already believed is a section a careful reader will stop trusting.


============================
APPENDIX Z - THE ORIGINAL DICTATION THIS PROMPT WAS BUILT FROM
============================

Kept verbatim so the intent behind the structure above is never lost. Where this
appendix and the stages above disagree, the stages above win - but read this
first if you are unsure why something is the way it is.

  This prompt file is about acting as an AI attorney, defense attorney. That's
  going to be a different team than the human AI attorneys that Tyler Robinson
  has. The goal here is that we're going to take it that there are certain
  things. We'll have an appendix A that has a certain thing, as well as the
  things that are true.

  This is about taking the ai_attorney directory and putting files in there. The
  question is: we have an Appendix A, and there could be more in Appendix A. The
  idea here is that when we want to create almost a table in the left and the
  right, the left is what you would do as this ai_defense_attorney in this
  specific case. We'll tackle each of these listed in Appendix A as a different
  table on a different page. We'll have the overview.mdx in that ai_attorney
  directory have a list that correlates to the list in Appendix A. Each
  hyperlink you click on goes off to a page, and it'll have that table that'll
  go to one number in Appendix A. You'll have a table there on the left: what
  the AI attorney would do as far as asking questions of certain people in order
  to prove that case.

  On the right column, it's a matter of: Did that stage in the trial happen in
  the past, or is it upcoming? Did that witness get on stage? Did the real-life
  defense attorney ask that question or not? You might put a date and the
  personnel on the stand, and make a note that the defense attorney did not ask
  that question that you would have asked. In the left cell of the table, you're
  putting in the question you would have asked of the attorney of that person on
  that date.

  Your analysis below is: as a defense attorney, would this hold up as a legal
  defense? Cross-index all the facts across the whole site that are relevant or
  support it. What would you ask, or what would you pull out of the evidence?
  Assume that a lot of evidence was not provided. What would you make requests
  for evidence?

  We're looking for the gap analysis. We want to have that chain of reasoning of
  what the attorney would do, and also that gap analysis of where the human and
  real-world one may well seem to have skipped that. On this whole page, you're
  writing at the level 3 MDX under this ai_attorney directory. It will be one of
  these chains of thought and chain, and the real-life defense attorney will
  cover it fully, or what parts did they miss? What would the defense attorney
  have done?

  You can grow Appendix A if there are more of these. Learn from the current
  pattern.

  Right now, it seems like the defense attorney is not willing to question
  Israel or the government or intelligence services, and they're mostly sticking
  within the scope of the government's narrative.

  There's a directory tree below. You can turn that into Appendix B. Note that
  reading those is very valuable to do this when you're running this: doing more
  research, finding the newest court documents, and downloading them. We want to
  have a copy of old court documents. We should have them up to a certain date,
  as of August 29th, and you can read into them for an income analysis so far
  and so on.

  We will have Appendix C create a placeholder one. Over time, we'll put in
  linkages to evidence that are relevant.

  Have this run in stages. Have it build up the output for the most part as
  AI_Attorney telling that story. We have those pages to cover each one of
  these, and then the overview below the table that goes off links to them. You
  can go give a summary of that and put it on all these pages. This is only the
  personal opinions of AI, and it's just a thought analysis. We make no claims
  of any unethical or illegal behavior by the defense team for Tyler Robinson or
  anybody else.
