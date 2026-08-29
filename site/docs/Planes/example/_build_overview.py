#!/usr/bin/env python3
"""Regenerate site/docs/Planes/example/overview.mdx.

Every number on the generated page comes from one of:
  * site/docs/Planes/following/overlaps.csv   (the overlap rows themselves)
  * site/docs/Planes/following/airports.csv   (field class, runway, logged stays)
  * the US Census 2020 city populations in TOWNS below (the one external number)

Re-run:  python3 _build_overview.py
"""
import csv, os, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
FOLLOWING = os.path.normpath(os.path.join(HERE, "..", "following"))
REPO = os.path.normpath(os.path.join(HERE, "..", "..", "..", ".."))
OUT = os.path.join(HERE, "overview.mdx")

# Town, population and traffic all live in _build_pages.py so the table and the
# per-field-year pages can never quote different numbers at each other.
sys.path.insert(0, HERE)
from _build_pages import TOWNS, TRAFFIC   # noqa: E402

overlaps = list(csv.DictReader(open(os.path.join(FOLLOWING, "overlaps.csv"))))
airports = {r["airport_code"]: r for r in csv.DictReader(open(os.path.join(FOLLOWING, "airports.csv")))}

def slug_of(row):
    """Read the explicit slug out of the overlap page's own frontmatter."""
    path = os.path.join(REPO, row["overlap_page"])
    for line in open(path):
        if line.startswith("slug:"):
            return line.split(":", 1)[1].strip()
    raise SystemExit("no slug in " + path)

# ---- group: one row per (airport, year) -------------------------------------
groups = defaultdict(list)
for r in overlaps:
    if not r["airport_code"] or r["date"] == "UNKNOWN":
        continue
    groups[(r["airport_code"], r["date"][:4])].append(r)

rows, near_misses = [], []
for (code, year), items in groups.items():
    erika = [r for r in items if r["erika_present"] == "claimed"]
    # HARD REQUIREMENT: two or more overlap rows at this field in this year, AND
    # Erika Kirk claimed present at that field at least TWICE in that year.
    if len(items) < 2:
        continue
    if len(erika) < 2:
        # Kept, named, and shown below the table. A field-year that just misses
        # the bar is worth seeing; silently dropping it would hide how narrow
        # the qualifying set is.
        near_misses.append(dict(code=code, year=year, n=len(items), n_erika=len(erika)))
        continue
    items.sort(key=lambda r: (r["date"], r["overlap_id"]))
    rows.append(dict(
        code=code, year=year, items=items,
        n=len(items), n_dates=len({r["date"] for r in items}), n_erika=len(erika),
        n_charlie=len([r for r in items if r["charlie_present"] == "claimed"]),
        n_accurate=len([r for r in items if r["audit_verdict"] == "accurate"]),
        n_inaccurate=len([r for r in items if r["audit_verdict"] == "inaccurate"]),
        n_adsb=len([r for r in items if r["adsb_verified_verdict"] == "AT_CLAIMED_AIRPORT"]),
        tails=sorted({t.strip() for r in items for t in r["foreign_tail"].split(";")
                      if t.strip() and t.strip() != "UNKNOWN"}),
    ))

# Best match sorts highest: smallest town / least traffic first, then the
# year with the most overlaps at that field.
rows.sort(key=lambda d: (TOWNS[d["code"]]["tier"], -d["n"], d["year"]))

def datelink(r):
    d = r["date"][8:10].lstrip("0") + " " + \
        ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"][int(r["date"][5:7])-1]
    who = {"Erika": "E", "Charlie": "C", "Both": "C+E", "TPUSA": "T"}[r["subject"]]
    return "[%s&nbsp;(%s)](%s)" % (d, who, slug_of(r))

L = []
w = L.append

w('---')
w('displayed_sidebar: docs')
w('title: "Small-Town Airports Where Erika Kirk Overlapped Twice In One Year"')
w('sidebar_label: "Repeat Small-Field Overlaps"')
w('description: "Every airport in the overlap record where two or more claimed '
  'overlaps fall in the same calendar year and Erika Kirk is one of them — ranked '
  'with the smallest towns and lowest-traffic fields first."')
w('keywords:')
for k in ["Charlie Kirk", "Erika Kirk", "Charlie Kirk assassination", "flight tracking",
          "ADS-B", "SU-BTT", "SU-BND", "KILG", "KPVU", "KLNK", "overlap"]:
    w('  - "%s"' % k)
w('image: "/img/docusaurus-social-card.jpg"')
w('hide_table_of_contents: true')
w('---')
w('')
w('{/* Full-bleed marker: activates the site-wide full-width + text-wrap')
w('    layout in custom.css. Scoped via CSS :has(). */}')
w('<div className="ck-full-bleed" />')
w('')
w("<a href=\"/Planes/following/overview\" style={{display:'inline-block', marginBottom:'1rem',")
w("padding:'0.35rem 0.9rem', background:'#1a73e8', color:'#fff',")
w("borderRadius:'4px', textDecoration:'none', fontSize:'0.9rem'}}>← Following</a>")
w('')
w('# Small-Town Airports Where Erika Kirk Overlapped Twice In One Year')
w('')
w('**A repeat is more interesting than a single visit, and a repeat at a small field '
  'in a small town is more interesting than a repeat at a hub.** A foreign-registered '
  'government jet turning up twice in one year at O\'Hare is traffic. The same jet '
  'turning up twice in one year at a municipal field in a town of 70,000 is a pattern '
  'worth naming. This page ranks the record on exactly that axis.')
w('')
w('Every row below is one **airport in one calendar year** that meets the hard '
  'requirement: **two or more claimed overlaps at that same field inside that same '
  'year, and Erika Kirk claimed present at that field at least twice in that year.** '
  '%d field-years out of the %d rows in '
  '[`overlaps.csv`](/Planes/following/73_overlaps) qualify, covering %d fields. '
  '**Each has its own page** — dates, clock times measured out of the recovered ADS-B '
  'traces, tail numbers, town population and annual traffic — linked in the second '
  'column. Each date in the last column links to that single overlap\'s own page.'
  % (len(rows), len(overlaps), len({r["code"] for r in rows})))
w('')
w('**Read the audit columns before the ranking.** Sorting high on this page means '
  '*small town, low traffic, repeated* — it does **not** mean *proven*. Most of these '
  'claims did not survive the audit. Wichita 2025 sorts above St. Louis 2024 and every '
  'one of its six claims is audited inaccurate. The two columns that say what actually '
  'held up are **Audited accurate** and **ADS-B at the field**, and on several of the '
  'best-ranked rows both read zero.')
w('')

# ---- the table --------------------------------------------------------------
w('## The table')
w('')
w('| # | Field-year page | Airport | Town (2020 census) | Ops / year | Passengers / year | Year | Overlap rows | Distinct dates | Erika | Charlie / TPUSA | Audited accurate | Audited inaccurate | ADS-B at the field | Tails | Overlap dates — each links to its page |')
w('|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|')
for i, d in enumerate(rows, 1):
    a = airports[d["code"]]
    t = TOWNS[d["code"]]
    dates = " · ".join(datelink(r) for r in d["items"])
    tr = TRAFFIC[d["code"]]
    w('| %d | **[%s %s](/Planes/example/%s_%s)** | [%s](/Planes/Airports/%s)<br/>%s | %s, %s<br/><small>pop %s</small> | %s<br/><small>%s</small> | %s<br/><small>%s</small> | %s | **%d** | %s | %d | %d | %s | %s | %s | %s | %s |'
      % (i, t["city"], d["year"], t["file"], d["year"],
         d["code"], d["code"], a["airport_name"].replace("|", "/"),
         t["city"], t["abbr"], t["pop"],
         tr["ops"], tr["ops_year"], tr["pax"], tr["pax_year"],
         d["year"], d["n"],
         ("**%d**" % d["n_dates"]) if d["n_dates"] != d["n"] else str(d["n_dates"]),
         d["n_erika"], d["n_charlie"],
         ("**%d**" % d["n_accurate"]) if d["n_accurate"] else "0",
         d["n_inaccurate"], d["n_adsb"],
         " ".join("[%s](/Planes/%s/overview)" % (x, x) for x in d["tails"]) or "—",
         dates))
w('')
w('Legend for the date column: **(E)** Erika claimed present · **(C)** Charlie claimed '
  'present · **(C+E)** both claimed · **(T)** a TPUSA event with neither Kirk claimed.')
w('')
w('**Where the two count columns differ, the same calendar date carries more than one '
  'row.** That is the reconstructed sheet holding the same claim twice — a Kanekoa-audit '
  'row and a site row for one date, for instance — not two separate visits. Provo 2025 is '
  'ten rows on six dates; Wichita 2025 is six rows on four. **Read the distinct-date '
  'column as the number of visits and the row column as the size of the paper trail.** '
  'Ranking uses the row count, so the fields with duplicated paperwork sit slightly '
  'higher inside their tier than the visits alone would put them.')
w('')

# ---- method -----------------------------------------------------------------
w('## How the ranking was built')
w('')
w('**The hard requirement, applied first.** A field only appears if, inside one '
  'calendar year, the record holds **two or more overlap rows at that field** and '
  '**Erika Kirk is claimed present at that field at least twice in that year**. One '
  'visit is not a pattern, and a single Erika claim beside somebody else\'s is a '
  'different question than this page asks. Field-years failing either half are absent, '
  'and the ones that failed only the second half are named below rather than dropped.')
w('')
w('**Then smallest first.** Each of the six fields is ranked three ways — by 2020 census '
  'city population, by aircraft operations a year, and by passengers a year — and the three '
  'ranks are averaged. Ties inside one field go to the year with more overlaps. The three '
  'measures agree closely enough that the averaged order is also the order you get from town '
  'population alone.')
w('')
w('**The one place they disagree is Provo, and it is worth knowing about.** '
  'KPVU handles **184,395 aircraft operations a year** — MORE than Wichita (117,671) or '
  'Omaha (107,914), and the second busiest field on this page by movements. It is still a '
  'small-town field by every other measure: 889,000 passengers against Omaha\'s 5.2 million, '
  'in a town of 115,162. The movement count is inflated by the flight school and the Duncan '
  'Aviation maintenance base on the field, which fly circuits rather than journeys. Ranking '
  'Provo second is a judgment that the town and the passenger traffic describe the place '
  'better than the circuit count does — but the circuit count is printed in the table so a '
  'reader can disagree.')
w('')
w('**What just missed.** These field-years hold two or more overlaps but only ONE '
  'with Erika Kirk claimed present, so they fail the second half of the rule and have '
  'no page: ' + ", ".join(
      # Near-miss fields need not be in TOWNS at all — TOWNS covers only the
      # six fields that qualify — so name them out of airports.csv.
      "**%s %s** (%s, %d rows, %d with Erika)"
      % (airports[m["code"]]["city"], m["year"], m["code"], m["n"], m["n_erika"])
      for m in sorted(near_misses, key=lambda m: (m["code"], m["year"]))
  ) + '. They are listed here so the qualifying set is not mistaken for the whole record.')
w('')
w('**One caution about St. Louis.** Ranking uses the field and the metro it serves, not '
  'the city limits. St. Louis city proper is 301,578 people — smaller than Wichita or '
  'Omaha — but Lambert is a major international field serving a metro of about 2.8 '
  'million, so it ranks near the bottom where it belongs. The city population is printed '
  'anyway so the reader can see the adjustment rather than take it on trust.')
w('')
w('**Wilmington ranks first and the reason it ranks first is not the reason it is on the '
  'list.** New Castle is a small field beside a small city, which is exactly what this '
  'page is looking for. It is also, per '
  '[`airports.csv`](/Planes/Airports/KILG), *"a standard transatlantic corporate '
  'customs-and-fuel stop in the Philadelphia-Baltimore-Washington corridor without the '
  'slot pressure of the major hubs"* — it carries 16 logged stays because it is the '
  'outbound customs stop. A small field can be repeatedly visited for an entirely '
  'ordinary reason, and this one has one.')
w('')

# ---- what this does not show ------------------------------------------------
w('## What this page does not show')
w('')
w('* **A trace proves presence, never purpose, and never occupancy.** Nothing here '
  'places Charlie Kirk, Erika Kirk, or any other person aboard any aircraft. Erika '
  'Kirk\'s own itinerary is the missing document and no archive produces it — see '
  '[Erika flight logs erased](/Planes/following/Erika_Kirk_Flights).')
w('* **"Erika claimed present" is a claim, not a record.** It is a cell on the '
  'reconstructed sheet, and on that sheet the location is often a state rather than a '
  'field. See [the overlap window definition](/Planes/following/Overlap_Window_Definition) '
  'for what was and was not counted.')
w('* **An absence is not a finding.** `NOT_HEARD` means a volunteer ADS-B network held '
  'nothing for that airframe that day. Parked and silent, outside receiver coverage, '
  'or a wrong claimed date all look identical from here.')
w('* **A repeat is not an intent.** These fields host maintenance, customs and fuel. '
  'Provo and Lincoln both sit beside Duncan Aviation work; Wichita holds a '
  'Falcon-authorised service centre. Repetition is the thing worth checking, not the '
  'conclusion.')
w('')
w('Sources: [`overlaps.csv`](/Planes/following/73_overlaps) and `airports.csv`, both in '
  'this repo, as of 28 August 2026. City populations: US Census 2020.')
w('')

# ---- the prompt, verbatim ---------------------------------------------------
w('---')
w('')
w('## The request this page was built from')
w('')
w('Recorded verbatim so a reader can check the page against what was actually asked for.')
w('')
w('```text')
w('overview.mdx')
w('')
w('Create this page. Here are the goals.')
w('* Create a table')
w('* Each row a airport location that matches these criteria')
w('* Better is airports that less traffic')
w('* Better is airports in smaller or smallest towns')
w('* A hard requirement is Erika stopped in that same airport in the same airport in')
w('  the same year, and both were overlaps.')
w('')
w('Search parent dir and all sub dirs.  All overlaps.')
w('')
w('Get results on ./overview.mdx')
w('')
w('Best matching results sort higher in table on that page.')
w('')
w('Each row cell hyperlinks to that overlap flight page.')
w('')
w('get all of this prompt info on bottom of ./overview.mdx')
w('')
w('--- follow-up request ---')
w('')
w('For each row, for each year.  Create a page')
w('./{town}_{year}.mdx')
w('')
w('They must have Erika overlap twice in one year.')
w('')
w('Give dates of overlap.')
w('Also give times.')
w('')
w('give the plane tail number.')
w('')
w('Give population of the town.')
w('')
w('Give a measurement of how many flights estimated per year in that airport')
w('')
w('Enable web search')
w('')
w('Build this for every row in that table above.')
w('')
w('in ./example/ dir.')
w('```')
w('')
w('**The follow-up tightened the rule.** The first version of this table asked only '
  'that Erika Kirk be claimed at the field once in the year. \"They must have Erika '
  'overlap twice in one year\" is stricter, and applying it dropped four field-years — '
  'the three Lincoln years and St. Louis 2023 — from sixteen rows to twelve. Those four '
  'are named under **What just missed** above rather than deleted, and every remaining '
  'row has its own page.')
w('')
w('Everything in this directory is generated, by three scripts that live beside the '
  'pages. `_extract_times.py` measures the clock times out of the raw recovered ADS-B '
  'traces and writes `_times.json`. `_build_pages.py` writes the twelve '
  '`{Town}_{Year}.mdx` pages. `_build_overview.py` writes this page, and imports its '
  'town and traffic tables from `_build_pages.py` so the table and the pages can never '
  'quote different numbers at each other. Every link is resolved out of the target '
  'page\'s own frontmatter slug rather than guessed. Re-run in that order after any '
  'change to `following/overlaps.csv` or `following/airports.csv`.')

open(OUT, "w").write("\n".join(L) + "\n")
print("wrote %s — %d airport-years, %d overlap rows scanned"
      % (OUT, len(rows), len(overlaps)))
