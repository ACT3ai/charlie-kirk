# p_timeline_create — Site-wide likelihood timeline SVGs

**DO NOT RUN THIS PROMPT YET.** This file is the instruction set for a later run.

When executed later, the agent walks the public Docusaurus tree, decides for each page whether a **likelihood-of-when** timeline belongs on that page, reuses a pre-built SVG when one already measures the same event, or creates a new SVG + registry row.

---

## Absolute paths and roots

| Symbol | Path |
|--------|------|
| `ROOT_DIR` | `~/BGit/Bryan_git/charlie-kirk` |
| `SITE_DOCS` | `{ROOT_DIR}/site/docs/` — **start walking here** |
| `TIMELINES_CSV` | `{ROOT_DIR}/timeslines.csv` — registry (create if missing). Filename is exactly **`timeslines.csv`** at repo root (not under `site/`). |
| `STATIC_IMG` | `{ROOT_DIR}/site/internals/static/img/` — **only** static root Docusaurus serves |
| `TIMELINE_SVG_DIR` | `{ROOT_DIR}/site/internals/static/img/km-timelines/` — established location for kill-me claim timelines; use this pattern for new event families |

### Critical static-asset rule (hard lesson already learned)

Docusaurus for this site is configured as:

```ts
// site/docusaurus.config.ts
staticDirectories: ["internals/static"],
```

**Never** put timeline SVGs under `site/static/`. Files there are **not** published — Docusaurus does not read that directory at all.

**One canonical copy only.** Write each SVG to `internals/static` and **nowhere else**. Do **not** also drop a copy in `site/static/` "to be safe": a second copy is worse than none, because a later editor can edit the `site/static/` copy, see the live site never change, and conclude SVGs are broken when the real asset was never touched.

> **Known stale duplicates:** 13 byte-identical copies of the KM charts are currently tracked under `site/static/img/km-timelines/`. They are dead weight and serve no purpose. Do not add to them, do not edit them, and never treat them as the source of truth. `site/internals/static/img/km-timelines/` is the only real location.

Public URL path is always:

```text
/img/<subdir>/<filename>.svg
```

which maps on disk to:

```text
{ROOT_DIR}/site/internals/static/img/<subdir>/<filename>.svg
```

Example already live:

- Disk: `site/internals/static/img/km-timelines/km-02-timeline.svg`
- MDX: `<img src="/img/km-timelines/km-02-timeline.svg" … />`
- Public: `https://whoassassinatedcharliekirk.com/img/km-timelines/km-02-timeline.svg`

SVG is supported. Prefer SVG. Convert to PNG/JPEG only if a real rendering failure is proven after assets are in `internals/static`.

---

## What these timelines are (and are not)

They are **not** government-certified times.  
They are **relative-likelihood charts** of when a claimed event most likely occurred, built from:

- Investigation indexes and master notes (`Charlie_Kirk.txt` — **read-only**)
- Named witnesses, interviews, recaps
- **Any X/Twitter claim or implication** about “when,” “day before,” “weeks before,” “Aug 13,” “night of,” “24 hours,” minutes/hours, etc.
- Web packaging when it dates the same claim

Bar **height** = relative likelihood that the event fell in that time bin.  
X-axis = earliest plausible → latest plausible, **trimmed** so near-zero tails do not waste width.

On every page that gets a chart, include prose **above** the image:

> **Best understanding of when [this happened / he said this]**  
> …working date range, peak, sources of uncertainty…

And **below** (or at page bottom, before Related Areas / author credit), a section of **exact X/Twitter (and other) quotes** about timing — not summaries only; keep the wording people used.

Hard rules from the investigation:

- **Never remove** pre-existing page claims or data.
- **Do not soften** for defamation legal risk on public pages beyond what the page already does; still do not invent court findings.
- Prefer growing information over shrinking.

---

## Registry: `{ROOT_DIR}/timeslines.csv`

### Create if missing

If `{ROOT_DIR}/timeslines.csv` does not exist, create it with this header row:

```csv
event_key,event,path_to_cvg,description
```

**Note on column name `path_to_cvg`:** this is the registry column name (path to the chart asset). Values are paths to **SVG** files (or PNG if conversion was required), including filename. Prefer absolute-from-repo paths or site-relative static paths that are unambiguous — recommended form:

```text
site/internals/static/img/<family>/<filename>.svg
```

### Columns (required)

| Column | Meaning |
|--------|---------|
| **event_key** | Primary key. Few words, `snake_case` underscores, **unique per row**. Used to refer to this row from other descriptions. Examples: `km_02_harrison_smith_relay`, `uvu_shot_moment_2025_09_10`, `robinson_surrender_chain`. |
| **event** | Human name of the event **and sub-event**. Be specific: not just “kill me texts” but e.g. `KM-02 Harrison Smith relay — when Charlie’s underlying remark (if any) was made`. The name measures **one** time window, not a whole meta-topic. |
| **path_to_cvg** | Path on disk under the Docusaurus-served tree to the chart file, **including filename**. Must match where the public site will host it. |
| **description** | Full description of what is being timed. Call out **which aspect** of a larger meta-event this measures. If similar to another row, say how it differs and **cite the other `event_key`**. |

### When to reuse vs create

1. Open `{ROOT_DIR}/timeslines.csv` (create if needed).
2. Search by meaning: same claim, same person-said-X, same physical event, same minute window.
3. If a row already measures **the same time question**, **reuse** `path_to_cvg` (same SVG URL on the page). Do **not** duplicate SVG files for identical events.
4. If the page needs a **different sub-event** (different wording, different recipient, different day cluster), create a **new** `event_key`, new SVG, new CSV row — even if related. Cross-link in `description` to the sibling `event_key`.
5. After creating a new SVG, **append** a row to `timeslines.csv` immediately.

### Seed from existing work (kill-me claims)

These already exist under `site/internals/static/img/km-timelines/` and should be registered in `timeslines.csv` on first run if missing:

| event_key (suggested) | file | measures |
|----------------------|------|----------|
| `km_01_wiped_out_premonition` | `km-01-timeline.svg` | When the “wiped out at any time” premonition text was said (multi-year) |
| `km_02_harrison_smith_relay` | `km-02-timeline.svg` | When Charlie’s underlying Israel-kill fear was expressed (on/before AUG 13 Smith post) |
| `km_03_break_away_pro_israel` | `km-03-timeline.svg` | “They will kill me if I break away…” (AUG 13 index window) |
| `km_04_go_against_israel` | `km-04-timeline.svg` | “If I go against Israel I think they will kill me” (AUG 13 / AUG 16 bimodal) |
| `km_05_turek_want_me_dead` | `km-05-timeline.svg` | Turek “want me dead / under the gun” weeks-before vs day-before vs months-apart |
| `km_06_worried_israel_kill_me` | `km-06-timeline.svg` | “I’m worried Israel is going to kill me” (~one day before) |
| `km_07_sept9_all_caps` | `km-07-timeline.svg` | “THEY ARE GOING TO KILL ME” SEPT 9 meeting |
| `km_08_kolvet_they_will_kill_me` | `km-08-timeline.svg` | Kolvet-bound night-before kill-me |
| `km_09_three_people_warned` | `km-09-timeline.svg` | “I think they’re going to kill me” to ~three people SEPT 9 |
| `km_10_flood_executed_tomorrow` | `km-10-timeline.svg` | Flood “executed tomorrow” night SEPT 9 |
| `km_11_the_left_will_kill_me` | `km-11-timeline.svg` | Competing Flood wording (same night as `km_10_…`) |
| `km_12_security_exchange` | `km-12-timeline.svg` | Security exchange “I know they want me dead” |
| `km_13_donor_executed_tomorrow` | `km-13-timeline.svg` | Donor lane of execute/kill tomorrow multi-recipient claim |

MDX pages that already embed these:  
`site/docs/Charlie/Text_Messages/kill-me-01-*.mdx` … `kill-me-13-*.mdx`.

---

## Orchestration model: one agent per directory under `site/docs/`

### Start

```text
{ROOT_DIR}/site/docs/
```

### Fan-out

1. List **top-level** directories and root-level `.md` / `.mdx` files under `site/docs/`.
2. **Assign one agent (or sequential workstream) per top-level directory** (e.g. `Charlie/`, `FBI/`, `After/`, `Timeline/`, `People/`, …). Root-level files can be a small “root” workstream.
3. Each directory agent recursively walks **all** pages under its tree (including nested `_category_.json` siblings’ `.md`/`.mdx`).
4. Agents share **one** registry file `{ROOT_DIR}/timeslines.csv` — treat it as the single source of truth; avoid duplicate `event_key`s. Coordinate by reading the CSV before creating, and writing new rows atomically when possible.
5. Parallel agents must **not** invent conflicting paths for the same event; reuse by `event_key` / description match first.

### Per-page assessment (every page)

For each `.md` / `.mdx` page, decide **exactly one** of:

| Decision | Action |
|----------|--------|
| **A. Already has a correct timeline** | Verify SVG exists under `internals/static`, URL works, and a matching `timeslines.csv` row exists (add row if chart exists but CSV missing). Do not remove content. |
| **B. Needs a timeline — reuse** | Search `timeslines.csv` for the same event/sub-event. If found, embed that chart’s public path on the page (prose + img + timing quotes if missing). Do not rebuild the SVG unless it is wrong for this page’s question. |
| **C. Needs a timeline — create** | Research timing claims → compute likelihood window → write SVG to correct static path → append CSV row → embed on page. |
| **D. No timeline** | Leave page alone (or only note internally). Most pure index, law-text, or non-temporal analysis pages fall here. |

### When a page “should” have a timeline

Add or reuse when the page is substantially about **when something happened or was said**, including:

- A dated claim, warning, text, call, flight, sighting, resignation, paving, surrender, hearing, leak, or meeting
- “Day before,” “48 hours,” “weeks before,” “night of SEPT 9,” etc.
- Competing date theories that a likelihood curve can display
- Especially **SEPT 8–12, 2025** activity (Charlie, Tyler Robinson, security, campus, FBI, medical, flights)

Skip when:

- The page is pure navigation, glossary, or undated opinion with no event locus
- Timing is not a real open question and no public claims date the event
- A parent overview already hosts the only needed chart **and** the child does not re-argue timing (optional: still link to parent; do not force duplicates)

---

## How to build a likelihood timeline SVG (procedure used for KM charts)

### 1. Research the time question

For the **specific sub-event** only:

- Read the page and linked pages.
- Pull master-file sections (read-only) for date language.
- Run X/web searches for **any** claim or implication of when: “August 13,” “day before,” “night before,” “24 hours,” “weeks before,” “hours before,” “minutes after,” etc.
- Keep **exact quotes** with handles and status IDs when available.
- Note **competing** datings (e.g. AUG 13 vs AUG 16; weeks-before vs months-apart edit claim).

### 2. Choose resolution

| Context | Axis resolution |
|---------|-----------------|
| Default multi-week or multi-month story | Days or day-clusters; labels like `AUG 13`, `SEPT 9` (year **2025** assumed for assassination arc unless multi-year) |
| Multi-year premonition / long-running state | Years on the axis (see `km-01`) |
| **Critical window: SEPT 8–12, 2025** (day of, two days before, two days after) — especially **Tyler Robinson**, security, UVU, medical, surrender, flights, anything operational | Prefer **hour** (and **minute** when claims support it). Rare outside this window; use when appropriate. |

**SEPT 8–12 priority:** Anything in the three days up to the event, **SEPT 10, 2025**, and the two days after is **super important**. Within that band, time-of-day (hour/minute) often matters more than calendar day alone.

### 3. Build a likelihood curve

- Define bins along the chosen axis.
- Assign relative likelihood from public claims (not a false precision number from “the government”).
- Shape can be a **bell curve**, **bimodal** (two peaks), **wide flat** (high uncertainty), or **spike** (tight consensus).
- **Trim width:** if likelihood is near zero on the left or right tail, **do not force a wide empty chart**. Crop the axis so the visible mass is focused. Do not pad with huge zero-probability regions.
- Peak annotation: mark best working peak label (e.g. `AUG 13`, `SEPT 9 night`, `12:23 PM`).

### 4. Axis labeling (one or two rows of text)

- Month abbreviations: **`AUG`**, **`SEPT`** (not long month names unless multi-year needs full words).
- Day-level: e.g. `AUG 13`, `SEPT 9`, `SEPT 10`.
- When hour/minute is needed, use **two rows** under the tick so width does not explode:
  - Row 1: date (`SEPT 10`)
  - Row 2: time (`12:23 PM` or `~11:00 PM`)
- You may use forms like `12-AUG` if compact; stay consistent within a chart family.

### 5. Visual design (match existing quality)

Reference existing SVGs in `site/internals/static/img/km-timelines/`.

Recommended pattern:

- Wide-but-not-tall viewBox (e.g. ~920×220), but **width follows content** if the trimmed window is short — do not leave a large empty right/left pad when chance ≈ 0.
- Rounded card background, subtle gradient.
- Vertical bars with height = likelihood; color scales with height (cool → warm).
- Smooth stroke/curve over the bar envelope (optional but used on KM charts).
- Peak marker (dot + label).
- Title of event on the chart; subtitle that bar height = relative likelihood.
- Footer line with working range summary.
- Accessible: `role="img"`, `aria-label`, good contrast.

### 6. Write file to the correct static location

Family directories under `site/internals/static/img/`:

| Family | Suggested subdir | Notes |
|--------|------------------|-------|
| Kill-me / KM claims | `km-timelines/` | **Already established** — keep using |
| New families | `timelines/<topic>/` or topic-specific folder under `img/` | e.g. `timelines/robinson/`, `timelines/flights/`, `timelines/uvu/` |

Filename: descriptive, stable, lowercase-hyphen, ends in `.svg`.  
After write, set `path_to_cvg` in CSV to that repo-relative path.

### 7. Embed on the MDX page

Insert **after** the page’s early orientation / “At a glance” (or equivalent), **without deleting** existing sections:

```mdx
## Best understanding of when [this happened]

[Prose: peak, range, uncertainty, what the curve is measuring. Not a court finding.]

**Date range (working model):** …

The chart below is **not** a government finding. Bar height is **relative likelihood** from public claims …

<div className="ck-km-timeline" style={{margin:'1rem 0 1.5rem', maxWidth:'100%', overflowX:'auto'}}>
  <img
    src="/img/km-timelines/km-02-timeline.svg"
    alt="… likelihood timeline …"
    width="920"
    height="220"
    style={{width:'100%', height:'auto', display:'block'}}
  />
</div>
```

Use the real public path for the reused or new SVG (`/img/...` not a filesystem path).

#### MDX embed rules — these are JSX, not HTML

`.mdx` files compile as JSX. HTML that looks fine in a plain `.md` file will **fail the build** or silently drop the image. The embed block above is already correct; keep every one of these properties when you copy it:

| Rule | Correct | Wrong — breaks build or image |
|------|---------|-------------------------------|
| Style must be a JS object, not a string | `style={{width:'100%'}}` | `style="width:100%"` |
| CSS class attribute | `className="ck-km-timeline"` | `class="ck-km-timeline"` |
| `<img>` must be explicitly self-closed | `<img src="…" />` | `<img src="…">` |
| Comments | `{/* note */}` | `<!-- note -->` |
| Object keys are camelCase | `overflowX`, `maxWidth` | `overflow-x`, `max-width` |

**`<!-- -->` comments are the single most common build-killer in this repo.** An HTML comment anywhere in an `.mdx` file fails MDX compilation, the GitHub Pages build goes red, and the whole site silently keeps serving the previous deploy — which looks exactly like "my new SVG did not render." Never introduce one.

Leave a blank line before and after the `<div>…</div>` block so MDX parses it as a JSX block rather than folding it into surrounding prose.

**Path is absolute from the site root.** Always `/img/km-timelines/foo.svg`. Never a relative path (`./img/…`, `../../static/…`) and never a filesystem path — relative paths resolve against the page URL and 404 on nested pages.

Near the bottom (before Defamation note / author credit / Related Areas), add:

```mdx
## X / Twitter posts on when this was likely said

Exact public claims and implications about **timing**:

- **[@handle](https://x.com/handle/status/ID)**: "exact quote…"
- **Source name**: "exact quote…"
```

Never strip prior claims to “make room” for the chart.

### 8. Update `timeslines.csv`

Append one row per **new** event_key. Never reuse an `event_key` for a different time question. Never delete other agents’ rows.

---

## Example: research → curve decisions (from KM work)

Use as a template for judgment, not as the only events:

- **Tight post date, uncertain prior conversation** (KM-02): peak on/before carrier post day (AUG 13); left tail early AUG; little mass after death day.
- **Index vs public reel collision** (KM-04): **bimodal** AUG 13 and AUG 16.
- **“Weeks before” + counter-claim** (KM-05): wide hump mid–late AUG + secondary SEPT 9 + low early-AUG mass for months-apart theory.
- **Night-before consensus** (KM-07–10, 13): sharp SEPT 9 peak; trim empty AUG if near-zero.
- **Multi-year premonition** (KM-01): year axis, peak ~2018 claim, not SEPT 2025.

For **Robinson / day-of** pages later: if claims argue 11:00 vs 12:23 vs evening, switch to hour/minute bins on SEPT 10 (and SEPT 9–11 as needed), two-line tick labels.

---

## Parallel agent checklist (per directory agent)

```text
[ ] Load timeslines.csv (create with header if missing)
[ ] Register any existing km-timelines SVGs missing from CSV
[ ] Enumerate all .md/.mdx under assigned directory
[ ] For each page: A / B / C / D decision
[ ] If C: research dates → trim window → SVG in internals/static → CSV row → MDX embed + quotes
[ ] If B: embed existing path_to_cvg via /img/... URL; add prose/quotes if missing
[ ] If A: verify asset + CSV row
[ ] Write each SVG to internals/static ONLY — never a second copy in site/static/
[ ] MDX embed uses style={{}} / className / self-closed <img /> — no <!-- --> comments
[ ] Gate 1: every embed src resolves to a real, non-empty file on disk
[ ] Gate 2: `npm run build` exits clean AND chart appears in site/build/img/…
[ ] Gate 3: after deploy completes, svg=200 (image/svg+xml, non-zero) and page_refs >= 1
[ ] Before calling any chart broken: `gh run list` — in_progress means WAIT, not fix
[ ] Never write to Charlie_Kirk.txt
[ ] Never remove pre-existing page content
[ ] Do not run site-wide deploy unless operator asks
```

---

## Operator / later-run notes

- **Do not execute this prompt until Bryan asks to run it.**
- First run may seed `timeslines.csv` from the 13 KM charts, then walk the rest of `site/docs/`.
- Prefer many **specific** event_keys over one vague mega-chart.
- Prefer **reuse** when two pages ask the same timing question.
- Prefer **trim** over wide empty axes when probability ≈ 0 at the ends.
- Prefer **day/month** labels normally; **hour/minute** (two-line ticks) when the SEPT 8–12 operational window or a same-day dispute requires it.

---

## Verification — prove the SVG is actually visible

Writing the file and the embed is **not** done. An agent that stops there will report success on charts nobody can see. Run these three gates in order.

### Gate 1 — Every embed points at a file that exists (instant, run always)

For each page you touched, resolve the `src` against `site/internals/static` and confirm the file is on disk. A typo like `km-3-timeline.svg` vs `km-03-timeline.svg` costs a full deploy cycle to discover otherwise:

```bash
cd {ROOT_DIR}/site/docs/Charlie/Text_Messages
for f in kill-me-*.mdx; do
  ref=$(grep -o '/img/km-timelines/[^"]*\.svg' "$f" | head -1)
  [ -z "$ref" ] && { echo "NO-IMG: $f"; continue; }
  [ -f "{ROOT_DIR}/site/internals/static$ref" ] \
    && echo "OK   $f -> $ref" || echo "MISS $f -> $ref"
done
```

Every line must read `OK`. Also confirm each SVG is non-empty and starts with `<svg` or `<?xml` — a zero-byte or truncated file returns HTTP 200 and renders as nothing, which is the most deceptive failure of all.

### Gate 2 — The site actually builds

MDX errors do not fail loudly; they fail the *deploy*, and the old site keeps serving. Confirm before pushing:

```bash
cd {ROOT_DIR}/site && npm run build
```

A clean exit means the MDX compiled and the assets were copied. Then verify the SVGs really landed in the output — this is what proves the `internals/static` path is right:

```bash
ls {ROOT_DIR}/site/build/img/km-timelines/
```

If a chart is missing here, it is in the wrong static directory. Fix the location, not the page.

### Gate 3 — Confirm on the live site, and do not confuse "stale" with "broken"

**This is the step that has already cost real debugging time.** The site is GitHub Pages, not localhost. After a push, a build+deploy runs for roughly **4 minutes**. During that window the live site serves the **previous** deploy: the SVG returns 404 *and the page HTML does not even contain the `<img>` tag*. That is indistinguishable from a genuine rendering bug unless you check the deploy first.

**Always check the deploy state before diagnosing anything:**

```bash
cd {ROOT_DIR} && gh run list --limit 5
```

- `in_progress` → **nothing is wrong.** Wait for it to finish, then re-test. Do not "fix" anything.
- `completed failure` → the build broke. Open the log (`gh run view <id> --log-failed`); suspect an `<!-- -->` comment or a `style="…"` string in an `.mdx`.
- `completed success` → only now is a 404 a real bug.

Once the run for **your** commit shows success, verify each chart end-to-end:

```bash
for n in 01 02 03 04 05 06 07 08 09 10 11 12 13; do
  printf "km-%s: " "$n"
  curl -s -o /dev/null -w "svg=%{http_code}/%{size_download}b " \
    "https://whoassassinatedcharliekirk.com/img/km-timelines/km-$n-timeline.svg"
  page=$(basename $(ls {ROOT_DIR}/site/docs/Charlie/Text_Messages/kill-me-$n-*.mdx | head -1) .mdx)
  echo "page_refs=$(curl -s "https://whoassassinatedcharliekirk.com/Charlie/Text_Messages/$page" | grep -c "km-$n-timeline.svg")"
done
```

Pass condition for every row: `svg=200` with a **non-zero byte count**, and `page_refs` ≥ 1. Content type must be `image/svg+xml` — if it is `text/html`, you got the 404 page with a 200-ish wrapper.

A `page_refs=0` on a successful, completed deploy means the embed never made it into the built page — re-check Gate 1 and the MDX embed rules.

### Deploy gotcha: concurrent pushes cancel each other

`.github/workflows/pages.yml` sets `concurrency: cancel-in-progress: true` on the `pages` group. Two pushes in quick succession **kill the first deploy mid-flight**, so a correct commit can silently never publish. If a change seems to have vanished, check `gh run list` for a `cancelled` run and push again (an empty commit is enough) rather than editing working files.

---

## Acceptance criteria (when this is eventually run)

1. `{ROOT_DIR}/timeslines.csv` exists with columns `event_key,event,path_to_cvg,description`.
2. Every new chart file lives under `site/internals/static/img/…` — one copy, no `site/static/` duplicate — and is reachable as `/img/…` on the built site.
2a. **Verified visible, not merely written.** All three gates in "Verification" pass: file resolves on disk, `npm run build` exits clean with the chart present in `site/build/img/…`, and after the deploy completes the live URL returns `200` `image/svg+xml` with non-zero bytes while the live page HTML contains the `<img>` reference. A chart that was never confirmed on the live site does not count as done.
3. Every page that needs a timeline either embeds a registry SVG or has a documented **D** skip reason (internal log ok).
4. No duplicate `event_key`s; similar events cross-reference each other in `description`.
5. No existing investigative claims deleted from pages.
6. Charts focused (trimmed tails); SEPT 8–12 operational pages use finer time when appropriate.
7. Pages with charts include “best understanding” prose above and timing-quote sources below.

---

## Related prior art in this repo

- Prompt: this file — `prompts/p_timeline_create.md`
- Example MDX embeds: `site/docs/Charlie/Text_Messages/kill-me-*.mdx`
- Example SVGs: `site/internals/static/img/km-timelines/*.svg`
- Research dumps from first pass: `tmp/kill_me_research/` (private; not required on public site)
- Site config: `site/docusaurus.config.ts` → `staticDirectories: ["internals/static"]`

END OF PROMPT — do not run until instructed.
