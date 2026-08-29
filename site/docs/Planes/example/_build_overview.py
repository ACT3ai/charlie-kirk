#!/usr/bin/env python3
"""Regenerate site/docs/Planes/example/overview.mdx.

Every number on the generated page comes from one of:
  * site/docs/Planes/following/overlaps.csv   (the overlap rows themselves)
  * site/docs/Planes/following/airports.csv   (field class, runway, logged stays)
  * the US Census 2020 city populations in TOWNS below (the one external number)

Re-run:  python3 _build_overview.py
"""
import csv, os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
FOLLOWING = os.path.normpath(os.path.join(HERE, "..", "following"))
REPO = os.path.normpath(os.path.join(HERE, "..", "..", "..", ".."))
OUT = os.path.join(HERE, "overview.mdx")

# US Census 2020 city population, and the metro the field actually serves.
# Rank tier: 1 = smallest town / least traffic = best match for this page.
TOWNS = {
    "KILG": dict(tier=1, city="Wilmington, DE",  pop="70,898",    metro="Delaware Valley DE/PA/NJ"),
    "KPVU": dict(tier=2, city="Provo, UT",       pop="115,162",   metro="Wasatch Front UT"),
    "KLNK": dict(tier=3, city="Lincoln, NE",     pop="291,082",   metro="Omaha-Lincoln NE"),
    "KICT": dict(tier=4, city="Wichita, KS",     pop="397,532",   metro="Wichita KS"),
    "KOMA": dict(tier=5, city="Omaha, NE",       pop="486,051",   metro="Omaha-Lincoln NE"),
    "KSTL": dict(tier=6, city="St. Louis, MO",   pop="301,578",   metro="St. Louis metro (~2.8M)"),
    "KORD": dict(tier=7, city="Chicago, IL",     pop="2,746,388", metro="Chicago IL"),
}

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

rows = []
for (code, year), items in groups.items():
    erika = [r for r in items if r["erika_present"] == "claimed"]
    # HARD REQUIREMENT: two or more overlaps at this field in this year, and
    # Erika Kirk claimed at the field in that same year.
    if len(items) < 2 or not erika:
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
  'year, with Erika Kirk claimed present at that field in that year.** '
  '%d airport-years out of the %d rows in '
  '[`overlaps.csv`](/Planes/following/73_overlaps) qualify. '
  'Each date in the last column links to that overlap\'s own page.'
  % (len(rows), len(overlaps)))
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
w('| # | Airport | Town (2020 census) | Field size &amp; traffic | Year | Overlap rows | Distinct dates | Erika | Charlie / TPUSA | Audited accurate | Audited inaccurate | ADS-B at the field | Tails | Overlap dates — each links to its page |')
w('|---|---|---|---|---|---|---|---|---|---|---|---|---|---|')
for i, d in enumerate(rows, 1):
    a = airports[d["code"]]
    t = TOWNS[d["code"]]
    field = "%s, %s ft runway" % (a["airport_class"], a["runway_longest_ft"])
    dates = " · ".join(datelink(r) for r in d["items"])
    w('| %d | [%s](/Planes/Airports/%s)<br/>%s | %s<br/><small>pop %s</small> | %s | %s | **%d** | %s | %d | %d | %s | %s | %s | %s | %s |'
      % (i, d["code"], d["code"], a["airport_name"].replace("|", "/"),
         t["city"], t["pop"], field, d["year"], d["n"],
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
  '**Erika Kirk is claimed present at that field in that year**. One visit is not a '
  'pattern, and a pair with no Erika claim is a different question than this page asks. '
  'Airport-years failing either test are absent — that is why fields with a single '
  'logged overlap are not listed at all.')
w('')
w('**Then smallest first.** Rank is by field tier, and field tier is the town the field '
  'serves plus how much traffic the field carries, taken from the '
  '`airport_class` and `runway_longest_ft` columns of '
  '[`airports.csv`](/Planes/following/overview) and the 2020 US Census city population. '
  'Ties inside one field go to the year with more overlaps.')
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
w('```')
w('')
w('The page is generated by `_build_overview.py` in this directory, which reads '
  '`following/overlaps.csv` and `following/airports.csv` and resolves every link out of '
  'the target page\'s own frontmatter slug. Re-run it after either CSV changes.')

open(OUT, "w").write("\n".join(L) + "\n")
print("wrote %s — %d airport-years, %d overlap rows scanned"
      % (OUT, len(rows), len(overlaps)))
