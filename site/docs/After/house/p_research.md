# p_research — Research the Orem Staging House and Grow Its Public Pages

**DO NOT RUN THIS PROMPT YET.** This file is the instruction set for a later run.

When executed later, the agent researches everything findable about the house at
**691 W 925 S St, Orem, UT 84058**, then writes and grows public `.mdx` pages in
this directory so that visitors to the site can understand the house, who owns
it, who rented it, where it was listed for rent, and why it matters to the
Charlie Kirk assassination investigation.

This prompt is **re-runnable**. Every run should ADD new information and new
topic pages. Never delete or shrink existing content — pages only grow and get
better organized.

---

## Absolute paths and variables

| Symbol | Path |
|--------|------|
| `ROOT_DIR` | `~/BGit/Bryan_git/charlie-kirk` |
| `HOUSE_DIR` | `{ROOT_DIR}/site/docs/After/house/` — **all output pages go here** |
| `CK_FILE` | `{ROOT_DIR}/Charlie_Kirk.txt` — master investigation file. **READ-ONLY. NEVER WRITE.** |
| `CK_INBOX` | `{ROOT_DIR}/Charlie_Kirk_AI_Inbox.txt` — append-only inbox for new raw findings |
| `PAGES_CSV` | `{ROOT_DIR}/pages.csv` — master page index; keep in sync |
| `ASSESS_MANUAL` | `{ROOT_DIR}/prompts/Assess_Manual.md` — read FIRST; governs page writing and layout |
| `RESEARCH_TOPICS` | `{ROOT_DIR}/Research/Topics/` — private topic files; search for house material |
| `RESEARCH_RAW` | `{ROOT_DIR}/Research/raw/` — raw source posts; search for house material |
| `KNOWLEDGE` | `{ROOT_DIR}/knowledge/` — synthesized write-ups; search for house material |

## The house

**691 W 925 S St, Orem, UT 84058.**

The big investigative possibility: the attackers used this house to stage the
assassination of Charlie Kirk (September 10, 2025, Utah Valley University).
Maybe they rented it. Orem is the city where UVU sits, so proximity, sight
lines, travel time to campus, and short-term occupancy around September 10 all
matter.

---

## Page hierarchy (must match)

- Parent directory `After/` is **LEVEL 2**.
- `{HOUSE_DIR}/overview.mdx` is the **LEVEL 3** page — "House".
- Every other `{HOUSE_DIR}/*.mdx` topic file is a **LEVEL 4** page.

**Linking rule for overview.mdx:** the overview prose must contain phrase links
into **every** Level 4 page in this directory. A phrase link means a natural
sentence where the meaningful phrase itself is the link — e.g.
"county records show [who owns the house](./ownership) and when it last sold" —
NOT a bare "see here" link and NOT only a link list at the bottom. Every time a
new Level 4 page is created, the overview must be updated in the same run to
weave in a phrase link to it.

---

## Steps

### Step 1 — Load context

1. Read `{ASSESS_MANUAL}` fully. All pages must conform to it.
2. Read `{HOUSE_DIR}/CLAUDE.md` and every existing `.mdx` already in
   `{HOUSE_DIR}` so re-runs grow pages instead of duplicating them.
3. Search the private layer for anything already known about the house:
   - `grep -ri "925 S" {ROOT_DIR}/Research/ {ROOT_DIR}/knowledge/ {CK_FILE}`
   - Also grep for: `691 W`, `Orem`, `staging`, `rental`, `airbnb`, `vrbo`,
     and any owner/renter names found along the way.
   - `{CK_FILE}` is read-only but reading it is encouraged — it is the richest
     source.

### Step 2 — Research the house (web)

Use web search extensively. Research each of these angles and record source
URLs for everything:

1. **Ownership** — current owner, prior owners, purchase dates and prices.
   Utah County assessor / recorder parcel records, property tax records.
2. **Rental history & listings** — was it listed on Zillow, Redfin,
   Apartments.com, KSL Classifieds, Furnished Finder, Airbnb, VRBO? Listing
   dates, asking rent, listing photos, property manager or host name. Who was
   renting it around September 10, 2025?
3. **The property itself** — build year, size, layout, lot, garage/parking,
   sight lines, what listing photos reveal about interior and exterior.
4. **Location & proximity to UVU** — distance and drive/walk time to Utah
   Valley University and to the Losee Center / courtyard where Charlie Kirk
   was shot; nearby routes in and out; nearby cameras.
5. **Neighborhood & witnesses** — anything neighbors reported; unusual
   activity, vehicles, or occupants around September 10, 2025.
6. **Investigation attention** — X/Twitter posts, citizen-investigator
   threads, videos, or articles that name this address or this house; what
   law enforcement said or did about it (searches, canvassing, silence).
7. **Connected people** — anyone tied to the house (owner, landlord, tenants,
   property manager, host) and any connection to other names already in the
   investigation.

**Always run explicit Google/web searches on the address and log them.** Every
run must fire a batch of web searches on the literal address (and its
variants — `691 W 925 S`, `691 West 925 South`, with and without `Orem UT
84058`) plus the owner/seller names as they surface, and write the results into
a dedicated Level 4 page, `web-search-log.mdx`. That page is the public,
citable record of *what was searched, what was found, and what came up empty* —
so the next run does not repeat dead ends and a reader can retrace the trail.
Record each search's query, the useful hits (with URLs), and a one-line
verdict. Mirror those same notes into **Appendix B** of this prompt file.

### Step 3 — Deed chain & Utah County Recorder documents

The ownership page currently rests on a parcel record whose **serial life ended
in 1993** (serial 36:214:0001). Utah County re-serializes parcels; the current
title chain is NOT yet established. Fix that:

1. Use the Utah County parcel serial-history / conversion tools to find the
   **successor serial(s)** for this address and pull the **current** parcel
   record (owner, acreage, last document).
2. Search the **Utah County Recorder grantor/grantee index** for the owner-of-
   record surname and for the address. List every recorded instrument found:
   warranty deeds, quitclaim deeds, trust deeds (mortgages), reconveyances,
   liens, lis pendens, easements, and boundary/subdivision actions.
3. Flag any **transfer, refinance, trust/LLC conveyance, or new trust deed in
   2024–2026**, especially in the months surrounding September 10, 2025. A
   quiet title transfer or refinance near the event date is a lead; the
   absence of one also matters — record it either way.
4. Record entry numbers, book/page or document numbers, and dates for every
   instrument so anyone can re-pull them.

### Step 4 — Assessor, property tax & the residential-exemption signal

Utah taxes owner-occupied primary residences on **55% of market value** (the
45% primary residential exemption). Landlord-owned and second homes lose the
exemption. This makes the tax record a **rental detector**:

1. Pull the Utah County Assessor's current valuation and tax history for the
   parcel.
2. Determine whether the parcel carried the **primary residential exemption**
   in tax years 2024, 2025, and 2026. An exemption **removed or absent** is a
   documentary signal the house was NOT owner-occupied — directly relevant to
   the rented-staging-house theory. An exemption present cuts the other way.
   Report whichever is found.
3. Compare the **tax-notice mailing address** to the property address. A
   mismatch signals an absentee owner.
4. Note any tax delinquency, appeal, or Greenbelt/other special status.

### Step 5 — City of Orem records: rental license, permits, code enforcement

1. **Orem rental dwelling license.** Orem requires a city license to operate a
   rental dwelling. Search whether 691 W 925 S ever held (or applied for) a
   rental dwelling license or a short-term-rental/business license. A license
   on file would confirm landlord use; none on file constrains the "rented it"
   theory to unlicensed or short-term arrangements.
2. **Building permits.** Remodels, basement-apartment conversions, accessory
   apartment approvals — anything showing the house was configured for
   multiple occupants or income use.
3. **Code enforcement.** Complaints at the address (vehicles, occupancy,
   noise) — especially any complaint dated August–October 2025.
4. Record what exists publicly online vs what requires a records request
   (feeds Step 6).

### Step 6 — Draft GRAMA public-records requests

Utah's **GRAMA** (Government Records Access and Management Act) is the tool
that turns the open questions into compellable documents. Draft ready-to-send
GRAMA request letters (and note the correct records officer for each agency):

1. **Orem City Police** — CAD/dispatch call logs and incident reports
   referencing 691 W 925 S (and the surrounding block), August 1 – October 31,
   2025.
2. **Orem City** — rental dwelling license file, business license file, code
   enforcement file, and building permit file for the address.
3. **UVU Police Department** — any report or CAD entry referencing the
   address.
4. **Utah County Sheriff / Utah DPS** — any record referencing the address in
   connection with the September 10, 2025 investigation.

Publish the drafts (or a "how to file this yourself" walkthrough) on a public
page so citizen investigators can send them — this matches the site's
Your_Actions_Fix_It ethos. Record any responses in later runs.

### Step 7 — Courts, business entities & financial trails

1. **Utah state courts** (Xchange / MyCase): evictions, unlawful detainer,
   probate, divorce, civil suits, or protective orders touching the address or
   the owner-of-record name. An eviction case would prove tenancy; a probate
   case would explain a stale title.
2. **Federal PACER**: any filing referencing the address.
3. **Utah Division of Corporations**: business entities registered AT the
   address, or connected to names surfaced in Steps 3–6. Note registered
   agents, officers, and especially **entities formed or revived in 2025**.
4. **UCC filings and recorded liens** for financing trails on the property or
   its occupants.

### Step 8 — Occupancy & people verification (who actually lived there)

1. Establish who occupied the house around September 10, 2025: people-search
   aggregators, voter-registration listings, published obituaries, LinkedIn /
   Facebook location data, county marriage/divorce indexes.
2. The owner of record surfaced so far dates to a 1983–1993 serial window —
   determine whether that person is **alive or deceased** (obituaries, probate
   in Step 7). If deceased, identify the estate/heirs holding title now.
3. Every person surfaced here gets the defamation treatment in the defamation
   step: `Status: Alive / Deceased (YYYY) / Unknown`, attribution, and the
   explicit statement that occupancy/ownership implies no wrongdoing.
4. Cross-check every name against `{CK_FILE}`, `{ROOT_DIR}/Details/`, and the
   site's People pages for any pre-existing connection to the case.

### Step 9 — Confirm the campus proximity and sightline (updated)

**Correction from the current run:** an earlier draft claimed 691 W 925 S sits
"roughly three miles" from UVU in "south Orem." That is **wrong**. By the Orem
street grid and by geocoding, the house is only about **a quarter-mile from the
north edge of the UVU campus** — walking distance. The grid anchor: UVU's
north-campus building (Utah County Academy of Sciences) is at **940 W 800 S**,
and the house is **691 W 925 S**, ~0.2 mi away; geocoding puts the house near
**40.2801, −111.7106** and the campus point near **40.2778, −111.7139**
(~0.25 mi straight-line). This means the @DiligentDenizen "command center"
video's placement — **directly across from the Losee Center, overlooking UVU** —
is **broadly consistent** with the real geography, not in conflict with it.
So the remaining work is confirmation, not conflict-resolution:

1. **Pin the exact building in the video.** Match rooflines, landscaping, curb
   cuts, dumpster position, signage, and terrain against Street View and county
   GIS to confirm the videoed structure IS 691 W 925 S (or identify the precise
   neighbor if it is not). Produce a candidate address either way.
2. **Test the sightline claim** ("clear view of the Losee building and ALL UVU
   roofs south of the Computer Science building") with a viewshed/elevation
   analysis — the house is close enough that a rooftop line of sight is
   plausible, but plausibility is not proof. State the result plainly.
3. If the videoed building turns out to be a **different** parcel than the
   tax-mailing house, create a `second-location.mdx` Level 4 page and run the
   full records chain (Steps 3–8) against it, making clear which claims attach
   to which building.

### Step 10 — Imagery, sightlines & physical verification

1. Pull **Google Street View history** and **historical aerial imagery**
   (Google Earth, Utah County GIS orthophotos) for the address — compare
   frames before and after September 10, 2025 for vehicles, the alleged
   barricade, dumpsters, or physical changes.
2. Run a **viewshed / elevation check** of the "you can see all of the roofs
   of UVU" claim from the videoed location: does the terrain actually support
   the sightline? State the result plainly either way.
3. Screenshot and archive every piece of imagery used (Step 12) — Street View
   and listing photos get replaced without notice.

### Step 11 — Vehicles, the barricade & neighborhood canvass (open-source)

1. From video frames: identify the **box truck and delivery truck** (company
   logos, USDOT/MC numbers, fleet numbers, plates) and the **dumpster** rental
   company branding. A company name yields pickup/delivery records an
   investigator or GRAMA/subpoena could reach.
2. Chase the **grey Dodge Challenger Ring-camera claim** to its original
   footage or post — who posted it, when, and does the footage actually show
   this address?
3. Sweep **Nextdoor, Ring Neighbors, and local Facebook groups** (Sunset
   Heights / south Orem / UVU-area) for resident posts about unusual
   activity, vehicles, or occupants August–October 2025.
4. Log every claim with its author and date; neighbor reports are "reported,"
   never "confirmed."

### Step 12 — Preservation & cross-referencing

1. **Archive every source** the pages cite — archive.org / archive.today
   snapshots for listings, county record pages, X posts, and news items — and
   put the archive link next to the live link on each page. Listing pages and
   X posts about this case have a history of disappearing.
2. Pin decisive media (video, key screenshots) to **IPFS** per the repo's
   IPFS workflow (public gateway URLs only, never 127.0.0.1), respecting the
   banned-media CSVs.
3. Cross-reference all new names, entities, and addresses against `{CK_FILE}`
   sections, `Details/`, and existing site pages; add "Related Areas" links
   both directions where a real connection exists.

### Step 13 — Write / grow the Level 4 topic pages

One `.mdx` file per topic in `{HOUSE_DIR}`. Create what the evidence supports —
suggested set (rename or extend as findings dictate):

| File | Topic |
|------|-------|
| `ownership.mdx` | Who owns the house; ownership history; parcel records |
| `rental-listings.mdx` | Where it was listed for rent; dates, prices, hosts |
| `renters.mdx` | Who rented / occupied it, especially around Sept 10, 2025 |
| `property-details.mdx` | The house itself: build, layout, photos, lot |
| `location-proximity.mdx` | Map context; distance and routes to UVU |
| `staging-theory.mdx` | The case for and against the house as a staging site |
| `neighborhood-reports.mdx` | Neighbor and witness reports |
| `investigation-coverage.mdx` | X posts, articles, and law-enforcement handling |
| `deed-chain.mdx` | Recorder instruments: deeds, trust deeds, transfers, dates |
| `tax-and-exemption.mdx` | Assessor value, tax history, residential-exemption signal |
| `city-records.mdx` | Orem rental license, permits, code-enforcement file |
| `records-requests.mdx` | Ready-to-file GRAMA requests and how to send them |
| `second-location.mdx` | The "command center" building near Losee; geolocation |
| `vehicles-barricade.mdx` | Box/delivery trucks, dumpster, grey Challenger, IDs |
| `web-search-log.mdx` | Public log of every Google/web search on the address, with results |

Page rules:

- Written for the general public learning about the assassination — plain
  language, explain context, no insider shorthand.
- Frontmatter with `title` and a short `description`; sensible `sidebar_label`.
- Every factual claim carries its source (link the source in prose).
- Distinguish clearly: **confirmed record** (deeds, listings, official docs) vs
  **reported** (media, X posts) vs **theory/question** (staging possibility).
- If a run finds little on a topic, still write the page with what is known and
  an explicit "Open Questions" section — later runs fill it in.
- MDX gotcha: keep `<div>`/`</div>` tags at column 0 (indented closing tags
  break the build and only `npm run build` catches it).

### Step 14 — Write / grow overview.mdx (Level 3)

- Title the page "The Orem House" (or similar) with the full address up top.
- Summarize: what the house is, why investigators care (possible staging
  site — maybe rented by the attackers), and the strongest findings so far.
- Weave in a **phrase link to every Level 4 page** per the linking rule above.
- Keep the staging idea framed as an investigative possibility under active
  citizen investigation, not a proven fact.

### Step 15 — Defamation pass (mandatory before finishing)

All pages here are PUBLIC. For every living person named (owner, landlord,
tenant, property manager, neighbor):

- Never state as fact that they committed a crime or knowingly aided one.
- Use attribution: "county records list…", "according to the listing…",
  "investigators on X have asked whether…".
- Frame suspicion as questions, include denials/counter-explanations found.
- Determine alive/dead status before profiling anyone; include
  `Status: Alive / Deceased (YYYY) / Unknown` where a person is profiled.
- An innocent explanation exists for most facts (a normal family may simply
  own or rent this house) — say so where honest.

### Step 16 — Bookkeeping

1. **pages.csv** — add/update a row for every page touched. `overview.mdx` is
   level 3 with `parent_key` = the After section's Level 2 key; each topic page
   is level 4 with `parent_key` = the house overview's key. Fill every column.
2. **CK_INBOX** — append significant NEW raw findings (records found, names,
   dates, listing URLs) to `{CK_INBOX}` in the equal-sign section format with a
   line naming the `{CK_FILE}` section they belong under. Never write to
   `{CK_FILE}` itself.
3. **Build check** — run `cd {ROOT_DIR}/site && npm run build` and fix any MDX
   errors introduced.
4. Report to Bryan: pages created/grown, key new findings, what was appended to
   the inbox, and the biggest open questions for the next run.

---

## MORE STAGES — additional ways to find information (run these too)

These extend the research sequence above. Each run should pull from this menu,
add findings to the matching Level 4 page, and **append new avenues here** as
they are discovered — this section is meant to keep growing.

### Step 17 — Utility, occupancy & mail signals

1. **Utility hookups.** Orem City power/water and any private gas provider bill
   the occupant. A GRAMA request for account start/stop dates at the address
   (redacting the customer's private data) shows **when occupancy changed** —
   a move-in near September 2025 is a lead; a decades-stable account is the
   innocent explanation. Add to the Step 6 GRAMA drafts.
2. **USPS / NCOA.** Change-of-address and mail-forwarding signals (via
   people-search aggregators that ingest NCOA) can show recent move-ins/outs.
3. **Voter file.** Utah's public voter registration list shows registrants at
   the address and registration dates — another occupancy timestamp.
4. **Garbage/recycling & short-term-rental occupancy** patterns if any city
   dataset exposes them.

### Step 18 — Short-term-rental history (deep)

1. **AirDNA / STR analytics.** These services retain historical Airbnb/Vrbo
   listing IDs, pricing, and booking calendars even after a listing is deleted.
   Search Orem STR data for a 6-bed/7,486-sqft house matching this one.
2. **Airbnb/Vrbo listing-ID archaeology.** Wayback Machine and Google cache of
   listing URLs; reverse-search distinctive interior features.
3. **Orem short-term-rental registry / business license** (ties to Step 5) —
   whether any STR permit was ever issued for the parcel.
4. **Furnished Finder / corporate-housing** history — traveling-nurse and
   corporate-stay boards that a short operational rental might use.

### Step 19 — Listing-photo ↔ video cross-match (high value)

1. Retrieve **every archived listing photo** ever published for 691 W 925 S
   (Zillow/Redfin/Trulia/MLS via Wayback). Retrieve **frames from the
   @DiligentDenizen walkthrough video**.
2. **Compare interiors and exteriors** — floor plan, fixtures, railings, view
   out the windows. If the video's building matches a past *listing* of this
   house, that is a strong link between "it was rented/listed" and "it was the
   command center." If they do **not** match, that is evidence the video shows
   a **different** building (feeds Step 9).
3. Document the comparison honestly, including a "no match / inconclusive"
   result.

### Step 20 — Air & signal correlation

1. The video narrator invokes the **[planes](/Planes/overview) "dipping down
   low."** Pull ADS-B/flight-track data (ADSBExchange history, the site's own
   Planes evidence) for aircraft over this coordinate on the morning of
   September 10, 2025, and state whether any track actually passes over the
   house.
2. Note this is correlation only — a plane near a campus during a large event
   is not itself evidence — but a documented low pass over this exact address
   would be worth recording.

### Step 21 — Social-media geolocation sweep

1. Search **Instagram, TikTok, Snapchat Map, X, and Facebook** for posts
   **geotagged** at or near the address around September 10, 2025.
2. Reverse-search any images that surface; log author, timestamp, and platform.
3. Treat all of it as "reported," never "confirmed," and apply defamation rules
   to any person who appears.

### Step 22 — Owner & associate mapping (defamation-bounded)

1. For each name in the recorded chain of title (currently **Kostas Markidas**;
   historically **Howell** and **Broderick** of the College Heights
   subdivision), determine **alive/deceased status** and whether any is already
   named anywhere in `{CK_FILE}`, `Details/`, or the site's People pages.
2. Map business entities, trusts, and co-owners tied to those names (via Step 7
   corporations data) — but **only publish a connection that is documented**,
   and always with the explicit statement that ownership implies no wrongdoing.
3. If nothing connects an owner to the case (the expected outcome), **say so
   plainly** — a clean result protects a private person and is itself a finding.

### Step 23 — Title, escrow & lender trail

1. Identify the **title company / escrow** and **lender** on the most recent
   transfer and any refinance (names appear on recorded trust deeds — Step 3).
2. A trust deed or reconveyance dated near September 2025 is a lead; note it or
   its absence.
3. Identify the **MLS listing agent / brokerage** of record for any past sale —
   a human who can be interviewed about who bought or rented.

### Step 24 — HOA, plat & neighborhood infrastructure

1. Pull the **College Heights subdivision plat(s)** (Plat F 1982, Plat J 1993 —
   already in the recorder index) and any **HOA/CC&Rs** governing the parcel;
   an HOA keeps records of owners and complaints.
2. Map **nearby cameras** (Ring/doorbell, business CCTV, city/UDOT traffic
   cams, UVU cameras) with a line of sight to the house or its street — the
   grey-Challenger Ring claim (Step 11) implies at least one exists.
3. Note ingress/egress routes from the house to the campus and to I-15.

### Step 25 — Regenerate this appendix and the file inventory

At the end of every run, refresh **Appendix A** (files in the directory) and
prune any stage whose findings are now fully captured on a page, so the prompt
reflects the current state instead of drifting.

---

## Hard rules (repeat)

- `{CK_FILE}` is **read-only to AI**. No exceptions. New material → `{CK_INBOX}`.
- Public pages never link into private directories (`Details/`, `Research/`,
  `knowledge/`).
- Pages only grow across runs — never delete findings; reorganize additively.
- Every Level 4 page must be phrase-linked from `overview.mdx`.

---

## APPENDIX A — Files currently in this directory

Pages and files present in `{HOUSE_DIR}` at the time this appendix was written.
Regenerate this list on each run so it stays current.

* `overview.mdx`: Level 3 hub — what the house is, the staging lead, the "command center" video, links to every Level 4 page.
* `location-and-property.mdx`: Physical facts — size, beds/baths, year built, lot, neighborhood, ~0.25 mi from UVU (walking distance).
* `ownership.mdx`: Ownership record — UVU bought the house in 2019 ($900k, from the Theobalds, "contiguous to campus"); older Markidas county serial and College Heights deed chain; no one accused.
* `rental-listings.mdx`: Whether it appeared as a rental/for-sale listing; nothing active found; why "was it rented" is testable.
* `staging-allegation.mdx`: The verbatim unverified claim it was a planning/staging site, and what would confirm or kill it.
* `neighborhood-reports.mdx`: Reported neighborhood evidence — ATF/police door-to-door camera canvass, the Ring-camera homeowner, the grey Challenger; no resident accused.
* `records-requests.mdx`: Ready-to-file GRAMA request templates (Orem PD, UVU, city, UVU Police) to test the lead, plus the open records to pull directly.
* `web-search-log.mdx`: Public log of every Google/web search run on the address, the useful hits, and the dead ends.
* `p_research.md`: This re-runnable research prompt — stages, page hierarchy, defamation and bookkeeping rules, this appendix.
* `CLAUDE.md`: Directory instructions — the address, the staging hypothesis, the Level 2/3/4 page structure for this dir.
* `_category_.json`: Docusaurus sidebar config for the "House" category (label and position).

---

## APPENDIX B — Search log across runs (what was tried, what worked)

A running, append-only record of the web/Google searches used to research this
address, so future runs skip dead ends and build on what worked. **Append a new
dated block each run. Never delete a prior block.** Also mirror the useful hits
into the public `web-search-log.mdx` page.

### Run 2026-08-09 (second run)

**What worked well — reuse these:**

* `691 W 925 S Orem UT 84058 property` — surfaced the property specs and the
  primary aggregator/record set: Trulia, Movoto, and the **Utah County land
  record**. Best single starting query.
* **WebFetch of the Utah County land record** (`utahcounty.gov/landrecords/...
  Property.asp?av_serial=362140001002`) — returned owner name (Markidas,
  Kostas), parcel serial, acreage, last document. The county ASP "mobile view"
  page fetches cleanly; use it directly.
* `"691 W 925 S" Orem sold history owner Markidas` — **the breakthrough.** It
  surfaced a USHE Board of Regents agenda PDF revealing that **Utah Valley
  University purchased this house in 2019 for $900,000.** Adding "sold history"
  + owner surname to the address is what cracked it open.
* Follow-ups on the UVU purchase (`"Utah Valley University" 925 South ...
  board trustees 2019 appraised campus`) — confirmed the **Theobald family**
  seller, **1.239 acres / 7,486 sqft**, "**contiguous to campus**," and the
  June 18 2019 trustee meeting. Board-minutes searches are gold for
  institution-owned property.
* `UVU Losee Center ... Computer Science building 925 South Orem campus map` —
  gave the **CS Building address 601 W 1000 South**, the grid fact that proves
  the house is one block off campus (kills the "3 miles away" error).
* `Charlie Kirk shooting house across from UVU ... grey Challenger Ring camera`
  — surfaced the **Fox 13 ATF/police door-to-door canvass**, the **ABC4
  Ring-camera homeowner**, and the **grey Challenger 8:29 a.m. campus arrival**
  — the backbone of `neighborhood-reports.mdx`.

**What did NOT work — don't waste a call on these again:**

* **WebFetch of Trulia, Movoto, Homes.com** → **403 Forbidden.** Real-estate
  aggregators block WebFetch. Read their content from the WebSearch result
  snippets instead of fetching the page.
* **WebFetch of large PDFs** → the **UVU trustee agenda (>10 MB)** exceeds the
  fetch size limit and the **USHE Regents PDF (3.7 MB)** is a **scanned image
  with no extractable text.** Rely on the WebSearch engine's extracted snippet
  of these PDFs, or pull the smaller `utah.gov/pmn/files/*.pdf` meeting records.
* **Direct Airbnb/Vrbo search for the exact address** → nothing (expected; STR
  platforms hide addresses). Defer to the AirDNA / listing-ID archaeology in
  Step 18 rather than plain address search.

**Best-yield lesson:** the decisive fact (UVU ownership) came not from property
sites but from **government board minutes** found by pairing the address with
"sold history" and the owner surname. For any institution-adjacent property,
search the owning body's **trustee/regents/council agendas** early.

### Run <YYYY-MM-DD> (template — copy for the next run)

**What worked well:**
* `<query>` — `<what it found + URL>`

**What did NOT work:**
* `<query>` — `<why it failed>`

**Best-yield lesson:** `<one line>`
