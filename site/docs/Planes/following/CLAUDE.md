# `Planes/following/` — The Public Page-Per-Location Log Of The Planes That Followed Them

**THIS DIRECTORY IS THE PUBLIC DOCUSAURUS FOR PAGES WE PUBLISH PUBLICLY.** Everything in here is
public Docusaurus content, built and served to the world at `https://whoassassinatedcharliekirk.com/Planes/following/...`. There is
no private layer in this directory. Nothing here is a scratchpad, a research dump, a raw source
file, or a note-to-self. If you would not want a hostile reader, a journalist, or a defamation
lawyer reading it, it does not go in this directory.

The flip side of that rule, and it is the more important half:

> **ALL INFO WE CAN MAKE PUBLIC, WE WANT TO GO IN THIS DIRECTORY.**

Do not hold material back for tidiness, for length, or because it is only a fragment. If a fact
about a location, a date, an airport, a tail number, or a pairing can be published safely and
sourced honestly, publish it here. The bar is "can this be made public", not "is this
important enough". Sparse pages are the failure mode we are correcting, not the goal.

## What this directory covers

**Foreign intelligence aircraft that shadowed Charlie Kirk, Erika Kirk, and TPUSA events across
the United States** in the roughly 18 months to 2 years before September 10, 2025.

The pattern, stated plainly:

* A foreign-government-registered jet — the Israel/Egyptian aircraft **SU-BTT** (the "yellow
  plane"), **SU-BND** (the "blue plane"), **SU-BTU**, **SU-BTV**, **SU-BGM**, and others — flies
  into **the same airport** that Charlie's, Erika's, or TPUSA's aircraft flies into.
* Very often that airport is **small** — a regional field or an Army airfield, not a major hub —
  which is what makes the coincidence hard to explain away.
* The arrival is **the same day, the day before, or the day after** the Kirk/TPUSA arrival.
* It happens again. And again. Trackers count **up to 73 overlaps with Erika Kirk** and roughly
  **23 with Charlie Kirk**, over a window researchers variously describe as **2022 through
  September 2025**, tightening sharply in the **final two months**.

That repetition — not any single flight — is the claim. One overlap is a coincidence.
Seventy-three is a tasking order.

**THIS DIRECTORY IS NOT ABOUT THE UVU COURTYARD.** No soil excavation, no landscaping crew, no
pavers, no "by Monday" deadline. That is a different topic entirely. If you find that material
here, it is misfiled — remove it from this directory rather than working on it here.

## Variables

    SITE_ROOT dir is ~/BGit/Bryan_git/charlie-kirk/
    SITE_DOCS dir is {SITE_ROOT}site/docs/
    SITE_PLANES dir is {SITE_DOCS}Planes/
    THIS_DIR dir is {SITE_PLANES}following/            ← this directory. PUBLIC.
    OVERVIEW_FILE is file {THIS_DIR}overview.mdx       ← the Level 2 landing page
    CATEGORY_FILE is file {THIS_DIR}_category_.json
    HUB_FILE is file {SITE_PLANES}Following-Charlie-Erika.mdx
                                                       (the existing hub page for this exact
                                                        claim. These pages hang off it.)
    SISTER_DIR dir is ~/BGit/all/movies/m/charlie_kirk_movie/research/18_month_follow_planes
    SISTER_CLAUDE is file {SISTER_DIR}/CLAUDE.md
    SISTER_DOCS dir is {SISTER_DIR}/docs/
    SISTER_INFO is file {SISTER_DIR}/docs/information.yaml
    SISTER_OVERLAPS is file {SISTER_DIR}/docs/overlaps.csv    (THE SPINE — one row per claimed
                                                               overlap event)
    SISTER_RESEARCH dir is {SISTER_DIR}/research/             (raw source dumps)
    CK_FILE is file {SITE_ROOT}Charlie_Kirk.txt        ← the master investigation file. READ-ONLY.
    PAGES_CSV is file {SITE_ROOT}pages.csv
    ASSESS_MANUAL is file {SITE_ROOT}prompts/Assess_Manual.md
    BAN_IMAGES_CSV is file {SITE_ROOT}images/ban_images.csv
    BAN_VIDEOS_CSV is file {SITE_ROOT}videos/ban_videos.csv

## The sister directory — learn from it, never write to it

`{SISTER_DIR}` is this directory's **sister directory**. It is the private research and
movie-beat workspace for the same topic, living in the Charlie Kirk movie repo. Read
`{SISTER_CLAUDE}` in full before doing any work here.

**The relationship, and the direction of flow:**

    {SISTER_DIR}  ── research, verify, source ──▶  {THIS_DIR}  ──▶  the public web
    (PRIVATE: raw dumps, overlaps.csv,             (PUBLIC: one page per location,
     information.yaml, beat drafts KB73/KB407)      the overview index)

* **Learn from the sister.** Its research standards, its counts, its counterarguments, its
  sourcing discipline, its list of what is already known, and its rules about what may and may
  not be asserted are the standards this directory inherits. When this file is silent on a
  question, `{SISTER_CLAUDE}` is the fallback authority.
* **`{SISTER_OVERLAPS}` is the spine.** It is the per-overlap-event record every page in this
  directory is built from. Columns: `overlap_id, date, airport_code, airport_name,
  airport_class, city, state, subject (Charlie|Erika|TPUSA|Both), event, venue, kirk_tail,
  foreign_tail, foreign_type, registry, gap (same_day|day_before|day_after|other), arrived_from,
  departed_to, transponder, source, source_url, confidence, counterargument, site_page`.
  `overlap_id` is permanent once assigned — **never renumber it**, it is the join key between
  the private research and these public pages.
* **`{SISTER_INFO}` is the hierarchical research record.** All new facts land there, with a
  source, BEFORE they appear on a page here. Research first, publication second. A page in this
  directory must not assert anything that is not already recorded in `{SISTER_INFO}` with its
  origin.
* **`{SISTER_RESEARCH}` is INPUT and is never modified** — raw Grok/X capture dumps and ADS-B
  exports, numbered `1.md`, `2.md`, ….
* The sister directory also owns the **movie beats** — **KB73** ("Egyptian Planes Following
  Erika & Charlie; 18 months", Act 2B, layer `INTEL DID IT`, Andrew / Alaska / FIntel, 55.0%,
  order 67, assigned Rijan, category `Intel / Edu` — **the primary beat**) and **KB407**
  ("INTEL: Intelligence Planes following TPUSA", Act 2B, `INTEL DID IT`, Rijan — the
  TPUSA-events half of the same claim). KB73 is the Kirks; KB407 is the organization; they are
  one research problem. **Beat drafts, dictation, and visual grammar are the sister's job, not
  ours.** Nothing about camera coverage, on-screen counters, or reconstruction cards belongs on
  a public page.
* Neighbouring beats to be aware of and **not** write: **KB36** (Act 2A, intro to the Egyptian
  flights, Utah airport security), **KB81** (Egyptian planes, rental cars, true destination
  Israel, military US airports), **KB147** (just a shell company; transponder off), **KB59 /
  KB430** (the N1098L / drone / Fort Huachuca thread and its Act 3 courtroom payoff — different
  aircraft, different claim; **do not merge N1098L into the following-pattern**).
* **Never write into `{SISTER_DIR}`, `{CK_FILE}`, or anywhere else outside `{THIS_DIR}` from
  here.** This directory writes exactly two kinds of thing: files inside `{THIS_DIR}`, and the
  matching rows in `{PAGES_CSV}`. Everything else is read-only source material.

## `overview.mdx` — the Level 2 landing page

`{OVERVIEW_FILE}` **is the "Following" Level 2 page.** In this repo's vocabulary, a directory
directly under `site/docs/` is a Level 2 directory and the page that loads for it is its
`overview.mdx` — a landing page carrying a **table of contents whose entries are hyperlinked
paragraphs / rows leading down into the Level 3 pages beneath it**. `following/` sits one step
deeper (under `Planes/`), but it behaves exactly the same way: **`overview.mdx` is the door,
and every page in this directory is reachable from it.**

`{OVERVIEW_FILE}` must contain:

1. **The claim, in a few sentences at the top** — what the shadowing pattern is, whose tallies
   the counts come from, and the fact that they are researcher claims from public ADS-B data.
2. **The master index table**, sortable and complete — one row per page in this directory:
   `location · airport code · city / state · date range · who (Charlie | Erika | TPUSA | Both) ·
   foreign tails · overlap count · confidence`, with the location cell hyperlinked to the page.
3. **A chronological view and a geographic view.** The filenames sort by place; the overview is
   where the reader gets the timeline. Cluster the geography explicitly — the states and cities
   named in the research (**Missouri, Delaware, Utah, Nebraska, Kansas**; **Omaha, Wichita,
   Provo**) — and mark that clustering as unverified.
4. **The count dispute, shown as a dispute** — 73/~23, 72, "70+", 68/29 — never averaged, never
   silently reconciled.
5. **Prose paragraphs that hyperlink down into the individual pages.** Not a bare table. A
   reader who never clicks a row should still leave the overview understanding the pattern.
6. **Links up** to `{HUB_FILE}` and `{SITE_PLANES}overview.mdx`, and **sideways** to each tail
   number's page.
7. **The counterargument section**, at overview level as well as on every child page.

`{CATEGORY_FILE}` must exist, with label `"Following"`, a `position`, `"collapsed": true`, and a
`link` of type `doc` to id `Planes/following/overview` — the same shape as
`{SITE_PLANES}N1098L/_category_.json`:

    {
      "label": "Following",
      "position": 2,
      "collapsed": true,
      "link": {
        "type": "doc",
        "id": "Planes/following/overview"
      }
    }

## ONE PAGE = ONE LOCATION, WITH ITS DATE RANGE

**Each aspect of the following-pattern gets its own separate page. We want a separate page for
every location — with a date range — at which foreign planes are alleged to have followed
Charlie, Erika, or TPUSA around.**

That is the governing rule for this directory and it beats every other page-splitting scheme.

* **The page identity is the LOCATION.** One airport / city where the shadowing is alleged to
  have happened.
* **The date range is part of that identity.** A page covers one contiguous window of alleged
  following at that location. If the same location was shadowed in two clearly separate
  campaigns far apart in time, that is **two pages**, each with its own range. If a location
  was hit repeatedly inside one window, that is **one page** listing every one of those
  arrivals — the accumulation at a single field is exactly what the page exists to show.
* **Not one page per aircraft.** The tail numbers already have their own pages at
  `{SITE_PLANES}` — `SU-BTT.mdx`, `SU-BND.mdx`, `SU-BTU.mdx`, `SU-BTV.mdx`, `SU-BGM.mdx`,
  `N888KG.mdx`, `N560TW.mdx`, `N1098L/`, and the rest. Link to them; do not duplicate them.
* **Not one page per month.** Time is the overview's axis, not the directory's.
* **Multiple tails at one location go on the same page.** If SU-BTT and SU-BND were both at
  Provo inside the window, that is one Provo page covering both, not two pages.

> **Divergence from the sister directory, stated on purpose so nobody "corrects" it back:**
> `{SISTER_CLAUDE}` describes a page-per-overlap-event scheme with date-first filenames. **This
> directory does not use that.** Here the unit is the **location plus its date range**, and the
> per-overlap rows of `{SISTER_OVERLAPS}` are the *contents* of a location page rather than
> pages of their own. The sister's `overlap_id` values still travel with each entry so the two
> sides stay joined.

### Page naming

    {THIS_DIR}<City>_<ICAO-or-IATA>_<YYYY-MM-DD>_to_<YYYY-MM-DD>.mdx

Examples:

    Provo_KPVU_2025-05-27_to_2025-09-11.mdx
    Lincoln_KLNK_2025-07-20_to_2025-08-24.mdx
    Omaha_KOMA_2024-03-11_to_2025-08-23.mdx
    Wilmington_KILG_2025-08-23_to_2025-09-11.mdx

Location-first so the directory groups by place, which is how the pages are actually read.
Chronology is the overview's job. Use the ICAO identifier where one exists; fall back to IATA.
Use underscores, no spaces, no special characters. Once a filename ships it is a **stable ID** —
the URL is a join key. Never rename a published page; if the date range grows, widen the range
inside the page and leave the filename alone unless a human approves the rename and the
redirect.

### What every location page must contain

1. **The pairing, in one sentence at the top.** Who was at this location, which foreign tail
   numbers were there, over what window, and how far apart in time.
2. **The airport.** Name, ICAO/IATA code, size class (regional / municipal / Army airfield /
   international), runway count, distance to the Kirk or TPUSA venue, and — this is the point —
   **how unusual it is for a foreign government jet to be there at all.** A single strip with a
   windsock and no terminal is the argument; say so with facts, not adjectives.
3. **The Kirk / TPUSA side.** Every event at this location inside the window: the event, the
   venue, the date, and the aircraft they arrived on if known.
4. **The foreign side.** Every tail number, aircraft type, registry, where it came from, where
   it went next, and whether the transponder was on.
5. **The overlap table** — the heart of the page. One row per arrival pairing at this location:
   `date · foreign tail · foreign arrival time · Kirk/TPUSA arrival or event time · gap
   (same day | day before | day after) · arrived from · departed to · transponder · confidence ·
   overlap_id`. Both timestamps stated explicitly. This is where the accumulation at a single
   field becomes visible.
6. **The gap, stated explicitly** for each pairing — same day, day before, day after — with both
   timestamps, never just "around".
7. **Sourcing on every claim.** ADS-B screenshot, X post with author and date, a Candace Owens
   segment, or `{CK_FILE}`. **Say which.** An unattributed sentence does not ship.
8. **The counterargument.** Every page carries the innocent explanation: diplomatic travel,
   scheduled maintenance, a hub-and-spoke coincidence, a tracker misreading a
   nearest-public-airport label (as happened with the Provo-vs-Dugway SU-BTT departure). **A page
   without its counterargument is propaganda instead of research, and does not ship.**
9. **What we do not know.** The holes, named. Which legs have no ADS-B coverage, which Kirk-side
   locations are inferred rather than recorded, which tallies conflict.
10. **Links.** Up to `{OVERVIEW_FILE}` and `{HUB_FILE}`, sideways to each tail number's page
    under `{SITE_PLANES}`, and out to the relevant `{SITE_DOCS}TPUSA/` event page.

## Site conventions every page here must match

* **Frontmatter**, copied in shape from `{SITE_PLANES}SU-BTT.mdx`:

      ---
      displayed_sidebar: docs
      title: "..."
      sidebar_label: "..."
      description: "..."
      keywords:
        - Charlie Kirk
        - ...
      image: "/img/docusaurus-social-card.jpg"
      hide_table_of_contents: true
      ---

* **The full-bleed marker**, immediately after the frontmatter, exactly as the sibling pages
  have it:

      {/* Full-bleed marker: activates the site-wide full-width + text-wrap
          layout in custom.css (full width + overflow-safe side videos). Scoped
          via CSS :has(). */}
      <div className="ck-full-bleed" />

* **The back button block**, exactly as the sibling pages have it — for pages in this
  directory it points back at the following overview:

      <a href="/Planes/following/overview" style={{display:'inline-block', marginBottom:'1rem',
      padding:'0.35rem 0.9rem', background:'#1a73e8', color:'#fff',
      borderRadius:'4px', textDecoration:'none', fontSize:'0.9rem'}}>← Following</a>

  `{OVERVIEW_FILE}` itself uses `← Planes` pointing at `/Planes/overview`.

* **MDX gotcha — keep every `<div>` and `</div>` at column 0.** An indented closing `</div>`
  breaks the Docusaurus build, and only `npm run build` catches it — the dev server does not.

* **Build before declaring done:**

      cd {SITE_ROOT}site && npm run build

* **Read `{ASSESS_MANUAL}` first.** It is the authoritative writing and layout guide for every
  page on this site. Load it into context at the start of any task that creates, edits, reviews,
  or restructures a page in this directory.

## `pages.csv` — keep it in sync, every time

`{PAGES_CSV}` is the master index of every publicly visible page on the site. Every page created
in this directory gets a row; every page renamed, re-levelled, or deleted gets its row fixed.

Columns: `page_key, parent_key, level, level2_parent, level2_section, page_type, url_path,
file_path, title, sidebar_label, directory, extension, has_frontmatter, line_count, description`.

For this directory:

* `page_key` — unique, four words or less, underscores only, no special characters. Prefix
  everything here `Planes_Following_` — e.g. `Planes_Following_Index` for the overview,
  `Planes_Following_Provo`, `Planes_Following_Lincoln`.
* `parent_key` — `{OVERVIEW_FILE}`'s parent is `Planes`. Every location page's parent is the
  overview's page_key.
* `level` — the overview is **3** (an overview at depth 2). Each location page is **4** (a
  non-overview at depth 2).
* `level2_parent` / `level2_section` — both `Planes`.
* `url_path` — `/Planes/following/overview` for the overview, `/Planes/following/<filename
  without extension>` for each location page.
* `file_path` — `site/docs/Planes/following/<filename>`, relative to the repo root.
* `directory` — `Planes/following`.
* `extension` — `mdx`. Everything in this directory is `.mdx`, never `.md`.

Prefer incremental updates over regenerating the CSV, so hand-adjusted page_keys survive.

## Rules for what may be published here

These are inherited from `{SISTER_CLAUDE}` and from the repo's public-content rules, and they
are not optional on a public page.

* **Every disputed claim is ALLEGED, and is presented as a REPORTED CLAIM, not an established
  fact.**
* **THE COUNTS ARE TRACKERS' TALLIES, NOT RECORDS.** 73, 72, 70+, 68, 29, 23 — amateur readings
  of public ADS-B history by independent researchers. We may say what they counted. We may not
  say it as a verified total. **Where tallies conflict, show the conflict.** The disagreement is
  itself a finding — report it, do not average it.
* **ONE OVERLAP IS NOT EVIDENCE. THE PATTERN IS THE CLAIM.** Never build a page on a single
  dramatic flight as though it proved anything. Any individual pairing has an innocent
  explanation and a reader who will find it.
* **EVERY PAGE CARRIES ITS COUNTERARGUMENT.** No exceptions.
* **ADS-B HAS HOLES, AND THE HOLES CUT BOTH WAYS.** Transponders off, military fields not
  reporting, coverage gaps. An absence in the data is not proof of a covert leg; a presence is
  not proof of intent. Say which we have.
* **DO NOT MERGE THE THREADS.** The 18-month following pattern (KB73/KB407), the Sept 10 day-of
  timeline, the N1098L drone/HADES plane, and the N888KG Wendover departure are **four different
  claims about four different aircraft sets.** Merging them is how the whole angle gets
  dismissed at once. Link across; never blend.
* **ERIKA'S SIDE IS THE WEAK SIDE.** Her flight logs are reported as erased, so the Erika
  overlaps rest on the *foreign* aircraft's track plus a claimed location for her. **Say so on
  every page carrying an Erika pairing**, and link
  `{SITE_PLANES}Erika-Flight-Logs-Erased.mdx`.
* **A SWORN DECLARATION OR A PRIMARY RECORD OUTRANKS A RELAYED ACCOUNT.** An FAA registry entry,
  an FBO log, or an airport badge record beats an X post about the same flight. Where they
  disagree, the record wins and the disagreement gets written down.
* **Never assert who tasked an aircraft.** No public record establishes tasking in either
  direction.
* **Never name a living person as the accused.** Tyler Robinson is CHARGED, not convicted.
* **Aircraft owners, crew, passengers, and ground staff are unnamed living persons and stay
  unnamed** — except where they have been publicly and on-the-record identified in a way the
  site already carries (e.g. Walid Mahmoud aboard SU-BTU), and then only as reported. Candace
  Owens made these claims publicly under her own name and may be named as the person who made
  them.
* **Defamation-safe language throughout**, per the repo rule for all public content: attribute
  ("according to…", "trackers say…", "reportedly"), include denials and counterarguments, frame
  suspicion as a question or a reported allegation, never as a conclusion.
* **Keep every stable ID unchanged** — page paths, URLs, `overlap_id`, KB_IDs. They are the
  join keys.

## Images, videos, and IPFS on these pages

* **Images are tracked in git.** Never gitignore an image, never add a per-file image line to
  `{SITE_ROOT}.gitignore`. An image that exists on disk but is untracked renders locally and
  404s for every real visitor, because the live site is built by GitHub Pages from the repo.
* **Never embed an image by IPFS gateway URL.** Always the local repo path, with the CID kept as
  provenance:

      <img src="/img/evidence/{sha256}.jpg" data-cid="{CID}" />

  Videos are the deliberate exception and do use the gateway as their primary src.
* **Never use `127.0.0.1` or `localhost` for an IPFS URL.** Use the public gateways:
  `https://ipfs.io/ipfs/<CID>/<path>` or `https://<CID>.ipfs.dweb.link/<path>`.
* **Check the ban lists before embedding anything.** `{BAN_IMAGES_CSV}` and `{BAN_VIDEOS_CSV}`
  are the master record of media we will not publish; the union of those CSVs and the legacy
  `image_planning/exclude_images.txt` / `videos_planning/exclude_videos.txt` is the ban set. A
  banned item gets no page, no embed, and no served copy.
* Audit before shipping:

      python3 {SITE_ROOT}image_planning/generator/audit_image_publication.py

## Related site pages to read before writing anything

* `{HUB_FILE}` — **the existing hub for this exact claim. Read it first and in full.** The pages
  in this directory must not contradict it; when they add detail, the hub links down to them.
* `{SITE_PLANES}overview.mdx` · `Planes_Investigation_Index.mdx` — the aircraft index.
* `{SITE_PLANES}SU-BTT.mdx` · `SU-BND.mdx` · `SU-BTU.mdx` · `SU-BTV.mdx` · `SU-BGM.mdx` — the
  tail-number pages. Every location page links to these.
* `{SITE_PLANES}Israel-Planes.mdx` — the Israel leg of the same aircraft, going dark over the
  eastern Mediterranean.
* `{SITE_PLANES}Sept10-Flight-Timeline.mdx` — the minute-by-minute of the final day. **The final
  day is that page's job, not ours.** This directory is the 18-month run-up. Link, do not
  restate.
* `{SITE_PLANES}Erika-Flight-Logs-Erased.mdx` — why the Erika side of the pairing is hard to
  verify.
* `{SITE_PLANES}Egyptian-Crew-Hotel.mdx` · `Cox-Foreign-Meetings.mdx` · `ISR-Operations.mdx` ·
  the `Airport-*.mdx` pages.
* `{SITE_DOCS}TPUSA/` — the event side of every pairing: which TPUSA event, where, when.
* `{SITE_DOCS}Israel_Main_Suspect/` and `{SITE_DOCS}Proof_Intel_Services/` — the motive layer.

## What we already know — the starting facts

These come from `{CK_FILE}` and `{HUB_FILE}`. They are the seed, not the finding. Everything
here must be re-sourced into `{SISTER_INFO}` with its origin before it is published on a page.

* **The counts, and that they disagree.** 73 Erika / ~23 Charlie is the headline (Candace
  Owens's team). Other posts say 72, "70+", or 68. A separate dual-plane tally says the blue and
  yellow jets together overlapped Erika **68 times between 2022 and September 2025**, of which
  **29** also coincided with Charlie's location. **These tallies have never been reconciled.**
* **The geography.** One analysis clusters the U.S. overlaps in five states: **Missouri,
  Delaware, Utah, Nebraska, Kansas.** Cities named: **Omaha, Wichita, Provo.** Unverified.
* **The start of the window.** Overlaps are said to begin around **2022**, which posters note
  aligns with the Kirk marriage timeline. That is 3 years, not 18 months — see the window
  question below.
* **Small and military fields.** SU-BTT's **first-ever trip to America, July 20, 2025, was to an
  Army base in Nebraska.** Trackers say all other flights of that aircraft went to Army bases,
  and Provo may be the only U.S. stop that was not an Army field.
* **May 27, 2025:** SU-BTU flies into Provo; Walid Mahmoud aboard. Departs June 2.
* **Sept 4, 2025:** SU-BTT flies France → Provo, and sits there through Sept 10.
* **Sept 10, 2025, 7:08 MT:** SU-BTT leaves Utah for Wilmington — before the assassination.
  **Sept 11:** it leaves the U.S. for Egypt.
* **SU-BND**, the blue plane, did not take off on Sept 10 — but its **transponder was turned ON**.
* **Sept 10:** N560TW, Scottsdale → Provo → Santa Barbara → Scottsdale.
* Provo airport badge access list updated **9/11/25** — the day after.
* Counter-UAS gear reportedly tested at Provo airport **Sept 4–10**; 4–6 "contractors" with
  claimed "US Department of Defense Liaison" badges dropped off and **not** flown back out.

**THE 18-MONTH-VS-2-YEAR-VS-2022 QUESTION IS AN OPEN RESEARCH QUESTION.** The beat title says 18
months. The filmmaker's framing says 18 months to 2 years. The trackers say 2022 → Sept 2025,
which is closer to three years. **Resolve it with the overlap data in `{SISTER_OVERLAPS}` — find
the earliest overlap we can actually source and let the window follow the evidence.** Do not
silently pick one on a public page; state the range and state who says what.

## Reading order, and what outranks what

* **`{CK_FILE}` — `~/BGit/Bryan_git/charlie-kirk/Charlie_Kirk.txt` — is the most important
  source there is. ALWAYS read it in. It takes PRECEDENCE over everything else, and its content
  is what the output must express. NEVER modify it** — it is read-only to AI under an absolute
  repo rule; new material goes to `{SITE_ROOT}Charlie_Kirk_AI_Inbox.txt` instead.
* Then `{SISTER_CLAUDE}` and everything under `{SISTER_DOCS}` — including `{SISTER_OVERLAPS}`,
  `{SISTER_INFO}`, and every file under `{SISTER_RESEARCH}`. **Hold the sister directory whole,
  not sampled.**
* Then `{HUB_FILE}`, then the tail-number pages under `{SITE_PLANES}`.
* Then `{ASSESS_MANUAL}` for how the page must read and lay out.
* A primary record outranks a relayed account. Where they disagree, the record wins and the
  disagreement gets written down.

## What may be written from here

**Only these.** Everything else in the repo and in the sister repo is read-only source material.

1. Files inside `{THIS_DIR}` — `overview.mdx`, `_category_.json`, and the location pages.
2. The matching rows in `{PAGES_CSV}`.
always learn from the dir ~/BGit/Bryan_git/charlie-kirk/site/docs/Planes/ because it has important info for us to learn to build content for this dir.


## The six data files in this directory

Six CSVs sit beside this file. They are the **structured spine** the location pages are written
from — the same role `{SISTER_OVERLAPS}` plays for the sister directory, but local, and built from
what this repo can actually source today. They are **research data, not published pages**:
Docusaurus does not serve a `.csv` out of `site/docs/`, so nothing in them reaches the web until a
human puts it on a page. Everything in them still has to clear the public-content rules in this
file before it does.

    FLIGHTS_CSV is file {THIS_DIR}flights.csv
    TPUSA_EVENTS_CSV is file {THIS_DIR}tpusa_events.csv
    PLANES_CSV_LOCAL is file {THIS_DIR}planes.csv
    OVERLAPS_CSV_LOCAL is file {THIS_DIR}overlaps.csv
    AIRPORTS_CSV is file {THIS_DIR}airports.csv
    SOURCES_CSV is file {THIS_DIR}sources.csv

They join like this:

    planes.csv ──(tail_number)──▶ flights.csv ◀──(date + city)──▶ tpusa_events.csv
                                       │              │                  │
                    (airport_code) ────┼──────────────┼──────────────────┘
                                       ▼              ▼
                                 airports.csv    overlaps.csv ──(overlap_page)──▶ overlap/*.mdx
                                       │              │
                                       │              └──(source_url)──▶ sources.csv
                                       └──(mdx_page)──▶ the Level 3 location pages in {THIS_DIR}

**`flights.csv`, `tpusa_events.csv` and `planes.csv` are the three ORIGINAL files.** `overlaps.csv`
is the per-claim register. **`airports.csv` (the WHERE spine) and `sources.csv` (the WHO-SAYS spine)
are the two reference tables** every other file joins into. Nothing is ever removed from any of
them — they only grow, and columns are only ever added.

`flights.csv` is where the *foreign* side lives, `tpusa_events.csv` is where the *Kirk / TPUSA*
side lives, and an overlap claim is a row from each that share a date window and a city. Neither
file asserts an overlap on its own. **Building a location page means picking the pairings out of
those two files and writing the gap explicitly** — same day, day before, day after, with both
timestamps.

### `flights.csv` — one row per stay by a following plane

One row = one aircraft on the ground at one location, from arrival to departure.

| Column | Meaning |
|--------|---------|
| `plane_tail_number` | Joins to `planes.csv`. |
| `start_date` | Date the following plane arrived. `UNKNOWN` where no source publishes it. |
| `end_date` | Date it left. `UNKNOWN` is common — trackers post arrivals far more often than departures. |
| `city` / `state` / `country` | Where it sat. Empty for tails with no published leg at all. |
| `notes` | The claim, the dispute, and the counterargument, in that order. Written to be read on its own. |
| `more_info` | The repo file that carries the fullest version of this leg. |
| `mdx_page` | The Level 3 location page in `{THIS_DIR}` this row belongs on. Several rows share one page — that accumulation at a single field is the whole point. |

**21 rows, 7 tails, 5 locations.** The five planned location pages are:

    Provo_KPVU_2025-02-14_to_2025-10-02.mdx        13 rows — the centre of gravity
    Omaha_KOMA_2025-07-20_to_2025-08-23.mdx         2 rows
    Wilmington_KILG_2025-02-14_to_2025-09-11.mdx    3 rows
    Wichita_KICT_2025-10-01_to_2025-12-31.mdx       1 row  — date range approximate
    Minot_KMOT_2025-08-08_to_2025-09-04.mdx         1 row  — transit stop, not a Kirk location

None of those five pages exists yet. The filenames are already fixed IDs — **write the pages under
exactly these names** so the `mdx_page` column stays valid, and never rename one after it ships.

**Deliberate scope decisions in `flights.csv`, so nobody "fixes" them back:**

* **Following planes only.** The column is literally `start_date: date the following plane arrived`.
  Kirk-party and flagged domestic tails — `N102DZ`, `N560TW`, `N888KG`, `N872RA`, `N40JD`,
  `N59906`, `N582MM`, the SAM flights, the casket flight — are **not** in this file. They fix where
  the Kirks were, not who followed them, and they belong to the Sept-10 day-of thread, which is
  `{SITE_PLANES}Sept10-Flight-Timeline.mdx`'s job. **DO NOT MERGE THE THREADS.**
* **Minot ND is in the file but marked as a transit stop.** It is on the route into Provo twice; it
  is not a place anyone claims Charlie or Erika ever was. The note says so in capitals.
* **`T7ELL` and `EJM36` have rows with no location.** They are named in the fleet list and have zero
  published legs. They are carried as empty rows so the tails are not silently dropped — a gap
  named is worth more than a gap hidden.
* **The `2024-04-01` SU-BTT Provo row is a single unverified claim** (@AuntLinda__, Dec 2025) and it
  is pointed at the main Provo page rather than given a 2024 page of its own. It is the only thing
  in the file that would move the window earlier than 2025, which is why it is flagged rather than
  built on. **This row is the live edge of the 18-month-vs-2-year-vs-2022 question.**

### `tpusa_events.csv` — where Charlie and Erika actually were

73 rows, January 2022 through October 2025. Columns: `dates, who, city, state, country, title,
university_or_venue, notes, mdx_page`.

**Its primary source is the podcast archive**, `{SITE_DOCS}TPUSA/apple_podcast/*.csv` — the
Charlie Kirk Show catalogue, which records a live campus stop or TPUSA summit every time one was
published as an episode. That makes it the densest Kirk-location record this repo holds, and it
comes with one caveat that is repeated on nearly every row:

> **THE DATE IS THE PODCAST RELEASE DATE, NOT THE EVENT DATE.** The event is normally 0–7 days
> earlier. Any overlap computed straight off these dates is approximate until the real event date
> is sourced. **Never publish a "same day" claim off a proxy date.**

Rows whose dates *are* real event dates say so in `notes` — AmericaFest 2024 (Dec 19–24, 2024),
SAS 2025 Tampa (Jul 11–13, 2025), UVU (Sept 10, 2025) — sourced from
`{SITE_DOCS}Amfest/amfest-year-timeline.mdx`.

City handling is graded, on purpose:

* Named venue → city stated (a university's city is an ordinary public fact).
* `UNKNOWN` → the venue city is **not stated in any repo source**. Roughly a third of rows, almost
  all of them TPUSA Faith summits, Academy summits and YWLS. **Do not fill these from memory.**
* `AMBIGUOUS` → the source names a system, not a campus ("University of Nevada" — Reno or Las
  Vegas). One row.

**The finding that matters most in this file is a negative one.** Of 73 rows, exactly **one** places
**Erika Kirk** at a TPUSA event before September 10, 2025 — the June 2025 Young Women's Leadership
Summit, sourced only from a later episode description that says "In June of 2025, Charlie and Erika
spoke to a group of young women," with no day of the month. That is the entire documented Erika
location record in this repo for the window the trackers counted **73 overlaps** across.

This is the concrete form of the rule stated earlier in this file — **ERIKA'S SIDE IS THE WEAK
SIDE**. The 73-overlap tally is measured against a set of Erika locations that this repo cannot
reproduce and that no tracker has published as a dated list. Every page carrying an Erika pairing
must say so and must link `{SITE_PLANES}Erika-Flight-Logs-Erased.mdx`. **Do not paper over this by
treating Charlie's itinerary as a stand-in for hers** — the tallies themselves say the two counts
differ by a factor of three.

Three rows are worth knowing before writing the Omaha and Wichita pages, because they cut *against*
the pattern as much as for it:

* **2024-04-11, Omaha NE** — a documented Charlie Kirk appearance in the city SU-BTT flew into on
  2025-07-20 and 2025-08-17. The gap is **15–16 months**. It is not an overlap and the row says so.
* **2024-04-12, University of Kansas, Lawrence KS** — Kansas is a clustering-claim state and
  SU-BTT later landed at Wichita. Gap ~19 months. Same caveat.
* **2024-06-14→23, Detroit MI** — Turning Point Action's People's Convention. SU-BTU flew
  Detroit → Provo on 2025-03-02, nine months later. No source connects the two.

Those three are in the file precisely so a future writer does not "discover" them and publish them
as hits. **A 15-month gap is not a shadowing event.**

### `planes.csv` — tail number and registry

Two columns, `tail_number` and `country_registered`, seven rows. Scope matches `flights.csv`: the
following fleet only.

    SU-BTT, SU-BND, SU-BTU, SU-BTV, SU-BGM   Egypt
    T7ELL                                    San Marino
    EJM36                                    United States

The last two rows carry a correction the site's own fleet list does not yet make, and it should be
made on any page that names them:

* **`T7ELL` is not an Egyptian registration.** `T7-` is the **San Marino** civil prefix. The site
  groups it with the "Egyptian armada" because a fleet-list thread did; the prefix says otherwise.
* **`EJM36` is a callsign, not a registration.** `EJM` is the ICAO operator designator for
  **Executive Jet Management**, a U.S. operator. It may not be a distinct airframe at all — it may
  be a flight number belonging to an aircraft already on the list under another identity.

Both are recorded in `flights.csv` with no legs, no dates and no location, which is the honest state
of the evidence for them.

### `overlaps.csv` — one row per claimed pairing

**85 rows.** The per-claim register. `overlap_id` is a **permanent join key — never renumber it.**

Four ID families, and the family tells you where the claim came from:

* **`OWENS-001` … `OWENS-067`** — the 67 published rows of the Candace Owens spreadsheet, carrying
  the compiler's own `owens_index`.
* **`EXTRA-001` … `EXTRA-007`** — pairings claimed on X outside the sheet.
* **`UNPUB-001` … `UNPUB-005`** — the gap between the sheet's 67 published rows and the claimed
  count of 72. **Carried as empty rows on purpose. A gap named is worth more than a gap hidden.**
* **`SITE-001` … `SITE-006`** — pairings this repo derived itself, each already written up as a
  page under `overlap/` before it had a row here. All six are recorded with the reason they cut
  *against* the pattern as prominently as the reason they support it. `SITE-004` (23 Apr 2024,
  Salt Lake City) and `SITE-006` (10 Sep 2025, Orem) are the only two pairings in this repo's own
  data that survive a same-metro, ±3-day test.

`overlap_page` links every one of the 85 rows to its dedicated page under `overlap/`.

### `airports.csv` — the WHERE spine

**103 rows, one per airport.** Primary key `airport_code` (ICAO). This is the table that answers the
question the whole claim rests on: **how unusual is it for a foreign government jet to be at this
field at all?** The columns that carry the argument:

* `airport_class`, `is_us_customs_port`, `military_colocation`, `runway_longest_ft` — the facility
  facts. A single strip with a windsock is the argument; state it with facts, not adjectives.
* **`mro_on_field`** — the innocent explanation, made a first-class column. Duncan Aviation at
  Provo and at Lincoln (its HQ), Yingling's Part 145 Falcon shop at Wichita. **Read this column
  before writing a word about why an aircraft was somewhere.**
* `how_unusual_foreign_state_jet` and `innocent_explanation` — the assessment and its counter, side
  by side on every researched row. Where a field was never researched the cell says so plainly.
* `role_in_case` — `foreign_plane_stop` / `kirk_tpusa_event_airport` / both /
  `claimed_overlap_only_no_logged_leg` / `referenced_only`.
* The count columns — `following_plane_stays`, `kirk_tpusa_events`, `overlap_claims`,
  `overlap_audited_accurate` / `_partial` / `_inaccurate` / `_untested`, `surviving_pairings`.

**Two rows to read before any other.** **KPHX (Phoenix Sky Harbor)** carries **13** sourced
Charlie/TPUSA events — more than any other field, because TPUSA is headquartered there — and **zero
following-plane legs, ever.** The absence of any Egyptian-registered leg at the fleet's most obvious
target city is a finding that cuts against the shadowing claim, and it is in the table for that
reason. **RKSI (Incheon)** records that Charlie Kirk was on a different continent for four of the
six days SU-BTT sat at Provo.

**KTOP vs KFOE is an identifier conflict, not a typo.** `overlaps.csv` logs the Topeka claim
(`EXTRA-003`) against KTOP (Philip Billard Municipal); the larger Topeka field a bizjet would
actually use is KFOE (Forbes Field). No source states which was meant. Both rows exist; neither is
silently merged.

### `sources.csv` — the WHO-SAYS spine

**202 rows.** Every claim in this directory traces to a row here. `source_id` is the join key:
`X-001`…`X-179` for X posts, then `ADSB-`, `BCAST-`, `VID-`, `PRESS-`, `DOC-`, `REPO-`, `REC-`.

* `role` — `originator_broadcaster` / `auditor` / `rebutter` / `compiler_researcher` /
  `independent_analyst` / `amplifier` / `aggregator` / `ai_relay` / `subject_response` /
  `organisation_account` / `primary_data` / `repo_record`.
* `stance` — `asserts_pattern` / `disputes_counts` / `disputes_pattern` / `corrects_detail` /
  `neutral_restates_official` / `evidence_only`.
* **`count_claimed`** — the published tally, verbatim, per source. 77, 73/~23, 72, 70+, 68/29, 60+,
  65–75, 1, "66% wrong / 60% wrong continent". **These have never been reconciled. Do not average
  them. `corroborated_by` on every asserting row says so in the cell itself.**
* **`evidence_class`** — the honesty column, and the one that ranks everything else:
  `adsb_public_history` > `facility_record` > `broadcast_video_frame` > `subject_denial` >
  `broadcast_claim` > `press_relay` > `social_post_unverified` > `document_quoting_claim`.
  **A primary record outranks a relayed account. A CourtListener PDF that quotes a claim is not a
  finding about the claim.**
* `corroborated_by` / `rebutted_by` — every asserting row carries its rebuttals; every disputing
  row carries what it rests on.
* `citation_count` / `cited_on_pages` — how load-bearing each source is across this directory.
  @KanekoaTheGreat is the single most-cited account here, and he is the principal *auditor*, not a
  claimant.

**`REC-001` and `REC-002` are rows for records that do not exist yet** — the Provo badge access list
and the Duncan Aviation FBO rental-car log. **Together with Erika Kirk's itinerary, those are what
would actually settle this, and nobody on either side has published them.** They are in the table so
the gap is a named row rather than a silence.

### The `attendee_class` column, in flights / tpusa_events / overlaps

The same vocabulary in all three files, so the three tables answer one question the same way:

    CHARLIE_ONLY        Charlie Kirk present; Erika not documented
    CHARLIE_AND_ERIKA   both present or both claimed
    ERIKA_ONLY          Erika claimed; Charlie not
    TPUSA_NO_KIRK       a TPUSA event with neither Kirk documented
    NONE_DOCUMENTED     (flights only) no Kirk or TPUSA presence at that field in that window
    UNKNOWN             not determinable from any source

`charlie_present` and `erika_present` sit beside it so the class is always auditable rather than
asserted, and they distinguish `yes` / `no` / `not_documented` / `claimed` / `no_deceased` /
`no_scheduled_not_held` / `unknown`. **`not_documented` is not `no`. Keep them apart.**

### The two overlap tests, run side by side

`tpusa_events.csv` carries both, because the difference between them *is* the public dispute:

* **`following_plane_at_airport`** — strict: same ICAO code, ±3 days. This is Liz Wheeler's rule.
* **`following_plane_in_metro`** — loose: same metro cluster, ±3 days, via the `metro_area` column
  shared by all three tables. This is closer to the spreadsheet's own ±3 days / 50–100 miles rule.

**Across 139 sourced Charlie/TPUSA events, the strict test returns 1 and the loose test returns 2** —
23 April 2024 (University of Utah / SU-BTT and SU-BND at Provo) and 10 September 2025 (UVU / the
same two aircraft at the same field). **Both are Utah. Both are `CHARLIE_ONLY`.** That is this
repo's own data reproducing the sceptics' result, and it must be reported that way and not softened.

**It is not the same as saying the pattern is false.** 139 is every Kirk/TPUSA location this repo can
source, and it is nowhere near every location the Kirks were at; the Erika side is close to empty.
**A test that returns 1 out of 139 is a statement about what we can currently prove, not about what
happened.** Say both halves of that whenever the number is quoted.

### Keeping the six files current

1. New fact lands in `{SISTER_INFO}` **with its source** first. Research before publication.
2. Add the source row to `sources.csv` — with its `role`, `stance` and `evidence_class` — before
   the fact is used anywhere else.
3. Add or update the row in `flights.csv` / `tpusa_events.csv` / `planes.csv` / `overlaps.csv`. Keep
   `mdx_page` pointing at a filename that follows the naming rule above, whether or not the page
   exists yet. **`overlap_id` and `source_id` are permanent once assigned.**
4. If a new airport appears, add its `airports.csv` row and research
   `how_unusual_foreign_state_jet`, `mro_on_field` and `innocent_explanation` **before** the airport
   is described on a page.
5. Recompute the derived columns — `attendee_class`, the audit counts on `planes.csv`, the two
   overlap tests, the count columns on `airports.csv` — rather than hand-editing them.
6. Only then write or widen the location page. **If the date range at a location grows, widen it
   inside the page and in the CSV — do not rename the shipped file.**
7. Add or fix the matching row in `{PAGES_CSV}`.
8. `cd {SITE_ROOT}site && npm run build` before declaring done.

**Never remove a row or a column from any of these six files, and never reduce a count to make the
pattern look tidier or stronger.** `UNKNOWN`, `AMBIGUOUS`, `not_documented`, the empty `UNPUB-`
rows, the attribution conflicts, the KTOP/KFOE identifier clash and the three-way disputed
departure time are the most valuable content in them — they are what makes the rest credible.

## The `speaking/` yaml layer — airports near every speaking location

Beside every `speaking/*.mdx` sits a `speaking/*.yaml` of the same name. It is **generated,
never hand-edited**, and it answers one question per event:

> Which airports could a private jet have used for this appearance, and was any tracked
> aircraft — above all an Egyptian `SU-` tail — at one of them within ±2 days?

    SPEAKING_YAML pattern is {THIS_DIR}speaking/{YYYYMMDD}_{city}.yaml
    SPEAKING_SUMMARY is file {THIS_DIR}speaking/_airports_near_summary.csv   (the roll-up)
    AIRPORTS_NEAR_PROMPT is file {SITE_ROOT}prompts/p_airports_near.md       (the contract)
    BUILDER is file {THIS_DIR}apis/public_open_source/code/airports_near.py
    FETCHER is file {THIS_DIR}apis/public_open_source/code/fetch_event_windows.py

Regenerate the whole set — it takes about a second off the cached trace index:

    cd {THIS_DIR}apis/public_open_source/code
    ~/.venvs/ck_flight/bin/python airports_near.py --rebuild-traces --report

**A new speaking location needs NO code change.** Add its row to `{TPUSA_EVENTS_CSV}` with
`mdx_page` pointing at the `.mdx`, run `fetch_event_windows.py` for the new window, then
re-run the builder. The `.yaml` appears on its own. `p_airports_near.md` carries the full
stage-by-stage procedure and the yaml block-by-block contract; read it before changing
anything here.

Docusaurus never serves a `.yaml` out of `site/docs`, so these are research data sitting
beside the pages exactly as the six spine CSVs sit beside this file. **Nothing in them
reaches the public web until a human puts it on a page**, and it must clear the
public-content rules above first.

### The three things in these files that a future run will be tempted to break

* **`selection_basis` IS THE WHOLE HONESTY OF `arrival_airport`.** "Probably landed at"
  means *nearest jet-capable field to the venue city*. No published Kirk-side flight
  record exists for the overwhelming majority of these events. Never restate the chosen
  field on a page as a known airport, and where the curated and computed values disagree,
  BOTH are kept in the file — publish the disagreement, never resolve it silently.
* **`estimated_arrival` / `estimated_departure` ARE ARITHMETIC, NOT RECORDS.** Event start
  minus 3 hours, event end plus 4, and where no event time is published 19:00 local is
  assumed *for the arithmetic only* with confidence dropped to low. The one exception is
  `observed_by_adsb`, which holds real ground contacts by a Kirk-side airframe with actual
  first and last times. **Only that block may be described as observed.**
* **`coverage` DECIDES WHETHER AN EMPTY RESULT MEANS ANYTHING.** It splits every
  aircraft-day in the window three ways: a trace is *held*, the archive was *asked and is
  empty*, or nobody has *ever asked*. Only the first two are evidence of anything. An
  empty `tracked_plane_presence` sitting on top of a low `queried_pct` is an UNASKED
  QUESTION, not a negative finding, and `by_side.following.coverage_pct` is the number
  that decides it.

### What the first full run found, and how it must be quoted

An Egyptian `SU-` tail inside 40 miles and ±2 days of **1 of 139** sourced speaking
events — 10 Sep 2025, Orem/UVU, KPVU. Plus **one near miss** in the outer ring: 23 Apr
2024, Salt Lake City, SU-BTT and SU-BND on the ground at Provo, **41.3 and 41.6 miles**
from KSLC, gap 0 days. Both are Utah. Both are `CHARLIE_ONLY`.

That is this repo's own primary ADS-B data reproducing the sceptics' result, and it must
be reported that way and not softened. **It is also not the same as saying the pattern is
false.** 139 rows is every Kirk/TPUSA location this repo can source and it is nowhere near
every location the Kirks were at; exactly one of those rows places Erika Kirk anywhere
before 10 September 2025, against a tally that claims 73 overlaps with her. **A test that
returns 1 out of 139 is a statement about what we can currently prove, not about what
happened. Say both halves of that whenever the number is quoted.**

The 40-mile radius is deliberately **soft**. KSLC to KPVU is 41.6 miles, so a flat cutoff
loses the 23 Apr 2024 pairing by 1.6 miles. The search runs to 60 and reports the outer
ring in `just_outside_the_radius`, which is **not a hit list** and must never be published
as one.


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones this page touches.

**Airports named on this page:**

* [KPVU — Provo Municipal Airport](/Planes/Airports/KPVU), Provo, UT — 135 recorded ground visits, 13 tracked aircraft
* [KSLC — Salt Lake City International Airport](/Planes/Airports/KSLC), Salt Lake City, UT — 33 recorded ground visits, 7 tracked aircraft
* [KPHX — Phoenix Sky Harbor International Airport](/Planes/Airports/KPHX), Phoenix, AZ — 94 recorded ground visits, 6 tracked aircraft

**Aircraft named on this page:**

* [N102DZ](/Planes/N102DZ/overview) — full recovered movement record, every airport and every leg
* [N1098L](/Planes/N1098L/overview) — full recovered movement record, every airport and every leg
* [N40JD](/Planes/N40JD/overview) — full recovered movement record, every airport and every leg
* [N560TW](/Planes/N560TW/overview) — full recovered movement record, every airport and every leg
* [N582MM](/Planes/N582MM/overview) — full recovered movement record, every airport and every leg
* [N59906](/Planes/N59906/overview) — full recovered movement record, every airport and every leg
* [N872RA](/Planes/N872RA/overview) — full recovered movement record, every airport and every leg
* [N888KG](/Planes/N888KG/overview) — full recovered movement record, every airport and every leg
* [SU-BGM](/Planes/SU-BGM/overview) — full recovered movement record, every airport and every leg
* [SU-BND](/Planes/SU-BND/overview) — full recovered movement record, every airport and every leg
* [SU-BTT](/Planes/SU-BTT/overview) — full recovered movement record, every airport and every leg
* [SU-BTU](/Planes/SU-BTU/overview) — full recovered movement record, every airport and every leg
* [SU-BTV](/Planes/SU-BTV/overview) — full recovered movement record, every airport and every leg

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 290 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
