#!/usr/bin/env python3
"""Generate one page per qualifying field-year: {Town}_{Year}.mdx.

QUALIFYING RULE (stricter than an earlier draft of overview.mdx):
    two or more overlap rows at one field inside one calendar year, AND
    Erika Kirk claimed present at that field at least TWICE that year.

Inputs, all in this repo except the traffic figures:
  following/overlaps.csv          the overlap rows, dates, tails, verdicts
  following/airports.csv          field class, runway, logged stays
  _times.json                     clock times measured out of the recovered
                                  ADS-B traces by _extract_times.py
  TRAFFIC below                    annual operations / passengers, web-sourced,
                                  each with its own citation URL
  TOWNS below                      US Census 2020 city population

Re-run:  python3 _extract_times.py && python3 _build_pages.py
"""
import csv, json, os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
FOLLOWING = os.path.normpath(os.path.join(HERE, "..", "following"))
REPO = os.path.normpath(os.path.join(HERE, "..", "..", "..", ".."))

MONTHS = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

# US Census 2020 city population. `file` is the page filename stem.
TOWNS = {
    "KILG": dict(abbr="DE", tier=1, file="Wilmington", city="Wilmington", state="Delaware",
                 pop="70,898", metro="Delaware Valley DE/PA/NJ"),
    "KPVU": dict(abbr="UT", tier=2, file="Provo", city="Provo", state="Utah",
                 pop="115,162", metro="Wasatch Front UT"),
    "KICT": dict(abbr="KS", tier=3, file="Wichita", city="Wichita", state="Kansas",
                 pop="397,532", metro="Wichita KS"),
    "KOMA": dict(abbr="NE", tier=4, file="Omaha", city="Omaha", state="Nebraska",
                 pop="486,051", metro="Omaha-Lincoln NE"),
    "KSTL": dict(abbr="MO", tier=5, file="St_Louis", city="St. Louis", state="Missouri",
                 pop="301,578", metro="St. Louis metro, about 2.8 million"),
    "KORD": dict(abbr="IL", tier=6, file="Chicago", city="Chicago", state="Illinois",
                 pop="2,746,388", metro="Chicago IL"),
}

# HOW MANY FLIGHTS A YEAR. An aircraft OPERATION is one takeoff or one landing,
# so a visiting jet that arrives and leaves counts twice. Figures are the public
# annual counts, each with the year it covers and where it came from — they are
# NOT from this repo, which holds no traffic data at all.
TRAFFIC = {
    "KILG": dict(ops="46,057", ops_year="12 months ending 22 December 2022",
                 per_day="126", based="219", pax="331,000", pax_year="2025",
                 src="https://en.wikipedia.org/wiki/Wilmington_Airport_(Delaware)",
                 srcname="Wikipedia, citing FAA Form 5010"),
    "KPVU": dict(ops="184,395", ops_year="2024", per_day="505", based=None,
                 pax="889,000", pax_year="2024",
                 src="https://en.wikipedia.org/wiki/Provo_Municipal_Airport",
                 srcname="Wikipedia, citing FAA"),
    "KICT": dict(ops="117,671", ops_year="2025", per_day="322", based=None,
                 pax="1,867,723", pax_year="2025",
                 src="https://en.wikipedia.org/wiki/Wichita_Dwight_D._Eisenhower_National_Airport",
                 srcname="Wikipedia, citing FAA"),
    "KOMA": dict(ops="107,914", ops_year="2025", per_day="296", based=None,
                 pax="5,225,232", pax_year="2025",
                 src="https://en.wikipedia.org/wiki/Eppley_Airfield",
                 srcname="Wikipedia, citing FAA and the airport authority"),
    "KSTL": dict(ops="161,300", ops_year="2025", per_day="442", based=None,
                 pax="15,303,756", pax_year="2025",
                 src="https://en.wikipedia.org/wiki/St._Louis_Lambert_International_Airport",
                 srcname="Wikipedia, citing FAA"),
    "KORD": dict(ops="857,000", ops_year="2025", per_day="2,340", based=None,
                 pax="84,851,825", pax_year="2025",
                 src="https://en.wikipedia.org/wiki/O%27Hare_International_Airport",
                 srcname="Wikipedia, citing FAA and the Chicago Department of Aviation"),
}

overlaps = list(csv.DictReader(open(os.path.join(FOLLOWING, "overlaps.csv"))))
airports = {r["airport_code"]: r for r in csv.DictReader(open(os.path.join(FOLLOWING, "airports.csv")))}
times = json.load(open(os.path.join(HERE, "_times.json")))

def slug_of(row):
    for line in open(os.path.join(REPO, row["overlap_page"])):
        if line.startswith("slug:"):
            return line.split(":", 1)[1].strip()
    raise SystemExit("no slug in " + row["overlap_page"])

def qualifying():
    g = defaultdict(list)
    for r in overlaps:
        if not r["airport_code"] or r["date"] == "UNKNOWN":
            continue
        g[(r["airport_code"], r["date"][:4])].append(r)
    out = {}
    for k, v in g.items():
        er = [r for r in v if r["erika_present"] == "claimed"]
        if len(v) >= 2 and len(er) >= 2:
            v.sort(key=lambda r: (r["date"], r["overlap_id"]))
            out[k] = v
    return out

def longdate(d):
    return "%d %s %s" % (int(d[8:10]), MONTHS[int(d[5:7]) - 1], d[:4])

WHO = {"Erika": "Erika Kirk", "Charlie": "Charlie Kirk",
       "Both": "Charlie and Erika Kirk", "TPUSA": "TPUSA event, neither Kirk"}

VERDICT_PLAIN = {
    "AT_CLAIMED_AIRPORT": "aircraft recovered at the claimed field",
    "NOT_HEARD": "no archive heard this airframe that day",
    "NO_ARCHIVE_COVERAGE": "no free archive covers this date",
    "ELSEWHERE": "**refuted — the airframe was somewhere else**",
    "SAME_METRO_WRONG_FIELD": "right area, wrong field",
    "NO_TAIL_CLAIMED": "no tail number was claimed, nothing to test",
    "NO_DATE_CLAIMED": "no date was claimed, nothing to test",
}

def time_cell(oid, tails):
    """Ground window and closest approach, as measured, or an honest blank."""
    rec = times.get(oid)
    if not rec:
        return "—", "—"
    ground, closest = [], []
    for tail in tails:
        info = rec["per_tail"].get(tail) or {}
        for g in info.get("ground", []):
            ground.append("%s %s–%s (%s–%s UTC)"
                          % (tail, g["first_local"].split()[0], g["last_local"],
                             g["first"][11:16], g["last"][11:16]))
        c = info.get("closest")
        if c:
            where = ("on the ground" if c["on_ground"]
                     else "airborne %s ft" % c["alt_ft"])
            closest.append("%s **%.2f km** at %s (%s UTC), %s"
                           % (tail, c["km"], c["local"], c["utc"][11:19], where))
    return ("<br/>".join(ground) or "none recovered",
            "<br/>".join(closest) or "nothing recovered")

def build(code, year, items):
    t, a, tr = TOWNS[code], airports[code], TRAFFIC[code]
    erika = [r for r in items if r["erika_present"] == "claimed"]
    charlie = [r for r in items if r["charlie_present"] == "claimed"]
    dates = sorted({r["date"] for r in items})
    tails = sorted({x.strip() for r in items for x in r["foreign_tail"].split(";")
                    if x.strip() and x.strip() != "UNKNOWN"})
    accurate = [r for r in items if r["audit_verdict"] == "accurate"]
    inaccurate = [r for r in items if r["audit_verdict"] == "inaccurate"]
    at_field = [r for r in items if r["adsb_verified_verdict"] == "AT_CLAIMED_AIRPORT"]
    with_time = [r for r in items if r["overlap_id"] in times
                 and any(v.get("closest") for v in times[r["overlap_id"]]["per_tail"].values())]

    L = []
    w = L.append
    title = "%s, %s — %s" % (t["city"], t["state"], year)
    w('---')
    w('displayed_sidebar: docs')
    w('title: "%s"' % title)
    w('sidebar_label: "%s %s"' % (t["city"], year))
    w('description: "%s claimed overlaps at %s (%s) during %s, %d of them with '
      'Erika Kirk claimed present — with the dates, the clock times measured out of '
      'the recovered ADS-B traces, the tail numbers, the town population and how '
      'many aircraft operations the field handles in a year."'
      % (len(items), a["airport_name"], code, year, len(erika)))
    w('keywords:')
    for k in ["Charlie Kirk", "Erika Kirk", "Charlie Kirk assassination",
              t["city"], code, "flight tracking", "ADS-B"] + tails:
        w('  - "%s"' % k)
    w('image: "/img/docusaurus-social-card.jpg"')
    w('hide_table_of_contents: true')
    w('---')
    w('')
    w('{/* Full-bleed marker: activates the site-wide full-width + text-wrap')
    w('    layout in custom.css. Scoped via CSS :has(). */}')
    w('<div className="ck-full-bleed" />')
    w('')
    w("<a href=\"/Planes/example/overview\" style={{display:'inline-block', marginBottom:'1rem',")
    w("padding:'0.35rem 0.9rem', background:'#1a73e8', color:'#fff',")
    w("borderRadius:'4px', textDecoration:'none', fontSize:'0.9rem'}}>← All field-years</a>")
    w('')
    w('# %s' % title)
    w('')
    w('**In %s the overlap record holds %d claimed overlap%s at [%s (%s)](/Planes/Airports/%s), '
      'on %d separate date%s. Erika Kirk is claimed present on %d of them — which is why this '
      'field-year has a page at all.**'
      % (year, len(items), "" if len(items) == 1 else "s", a["airport_name"], code, code,
         len(dates), "" if len(dates) == 1 else "s", len(erika)))
    w('')
    if at_field:
        w('Of those %d rows, **%d were checked against recovered ADS-B position data and put '
          'the airframe at or over this field**, and %d carry a measured clock time below. '
          'The rest were checked and the archives held nothing — which is not the same as the '
          'aircraft being elsewhere.' % (len(items), len(at_field), len(with_time)))
    else:
        w('**No row on this page is corroborated by recovered ADS-B position data.** Every one '
          'was checked; the free archives either held nothing for the airframe that day or do '
          'not cover the date at all. That is an absence of evidence, not evidence of absence — '
          'and it is also not corroboration.')
    w('')
    w('**Nothing here places any person aboard any aircraft.** These are aircraft positions and '
      'claimed locations, and the two are different kinds of thing.')
    w('')

    # ---- the field and the town --------------------------------------------
    w('## The town and the field')
    w('')
    w('| | |')
    w('|---|---|')
    w('| Town | %s, %s |' % (t["city"], t["state"]))
    w('| Population | **%s** (US Census 2020) |' % t["pop"])
    w('| Metro served | %s |' % t["metro"])
    w('| Airport | %s ([%s](/Planes/Airports/%s)) |' % (a["airport_name"], code, code))
    w('| Field class | %s |' % a["airport_class"])
    w('| Longest runway | %s ft |' % a["runway_longest_ft"])
    w('| **Aircraft operations per year** | **%s** (%s) — about %s a day |'
      % (tr["ops"], tr["ops_year"], tr["per_day"]))
    w('| Passengers per year | %s (%s) |' % (tr["pax"], tr["pax_year"]))
    if tr["based"]:
        w('| Based aircraft | %s |' % tr["based"])
    w('| Egyptian-registered stays logged here, all years | %s, over %s days on the ground |'
      % (a["following_plane_stays"], a["following_plane_days_on_ground"]))
    w('')
    w('An **operation** is one takeoff or one landing, so a visiting jet that arrives and '
      'departs counts twice. At %s that works out to roughly **%s operations a day**. '
      'Traffic figures: [%s](%s). They are not from this repo, which holds no traffic data.'
      % (code, tr["per_day"], tr["srcname"], tr["src"]))
    w('')
    if a["how_unusual_foreign_state_jet"]:
        w('**Is a foreign state jet unusual here?** %s' % a["how_unusual_foreign_state_jet"])
        w('')

    # ---- the overlaps -------------------------------------------------------
    w('## The overlaps — dates, times and tail numbers')
    w('')
    w('| Date | Claimed present | Tail | On the ground at this field | Closest recovered position | Sheet audit | ADS-B check | Row |')
    w('|---|---|---|---|---|---|---|---|')
    for r in items:
        rtails = [x.strip() for x in r["foreign_tail"].split(";")
                  if x.strip() and x.strip() != "UNKNOWN"]
        ground, closest = time_cell(r["overlap_id"], rtails)
        taillinks = " ".join("[%s](/Planes/%s/overview)" % (x, x) for x in rtails) or "none claimed"
        w('| **%s** | %s | %s | %s | %s | %s | %s | [%s](%s) |'
          % (longdate(r["date"]), WHO[r["subject"]], taillinks, ground, closest,
             r["audit_verdict"] or "not audited",
             VERDICT_PLAIN.get(r["adsb_verified_verdict"], r["adsb_verified_verdict"] or "—"),
             r["overlap_id"], slug_of(r)))
    w('')
    if len(items) != len(dates):
        w('**%d rows on %d dates.** Where one date carries two rows, the reconstructed sheet '
          'holds the same claim twice — an audit row and a site row, say — not two separate '
          'visits. Count the dates for visits and the rows for paperwork.'
          % (len(items), len(dates)))
        w('')

    # ---- times section ------------------------------------------------------
    w('## Where the clock times come from')
    w('')
    w('**There is no time column anywhere in the source data.** `overlaps.csv` and '
      '`flights.csv` carry dates only. Every time on this page was measured for it, point by '
      'point, out of the raw ADS-B traces held in this repo under `<TAIL>/data/recovered/` — '
      'the same files the ADS-B verdicts were computed from. Local times are the field\'s own '
      'local clock; UTC is given beside each so nothing turns on a timezone.')
    w('')
    if with_time:
        w('**%d of the %d rows produced a measured time.** The other %d did not, because no '
          'archive holds a trace for that airframe on that date.'
          % (len(with_time), len(items), len(items) - len(with_time)))
    else:
        w('**No row here produced a measured time**, because no archive holds a trace for '
          'these airframes on these dates. Every "—" in the table above is that, and only '
          'that.')
    w('')
    w('A blank is not a finding. Parked with the transponder off, outside volunteer receiver '
      'coverage, and a wrong claimed date all look identical from here.')
    w('')

    # ---- what it does and does not show -------------------------------------
    w('## What this page does and does not show')
    w('')
    w('* **A trace proves presence, never purpose, and never occupancy.** No archive anywhere '
      'puts Charlie Kirk, Erika Kirk or anyone else aboard any of these aircraft. Erika Kirk\'s '
      'itinerary is the missing document — see '
      '[Erika Kirk flights](/Planes/following/Erika_Kirk_Flights).')
    w('* **"Claimed present" is a claim, not a record.** It is a cell on the reconstructed '
      'sheet, and on that sheet the location is often a state rather than a field. See '
      '[the overlap window definition](/Planes/following/Overlap_Window_Definition).')
    if inaccurate:
        w('* **%d of these %d rows were audited inaccurate** and are shown anyway. They are '
          'part of the record of what was claimed, and dropping them would misrepresent how '
          'much of the claim survived.' % (len(inaccurate), len(items)))
    if accurate:
        w('* **%d were audited accurate.** That means the claim matched the aircraft record on '
          'checking — not that anybody was aboard.' % len(accurate))
    w('* **Repetition at a field is a reason to look, not a conclusion.** Fields host '
      'maintenance, customs and fuel stops, and a jet can return to one for entirely ordinary '
      'reasons.')
    w('')
    if code == "KPVU" and year == "2025":
        w('### One correction this page makes')
        w('')
        w('Elsewhere on this site, SU-BTT\'s closest recovered position at Provo on '
          '10 September 2025 is given as **1.23 km**. Measured across every point in both '
          'recovered traces, the closest is **0.03 km at 13:14:06 UTC (07:14:06 MDT)**, '
          'airborne at 4,550 ft barometric over a field about 4,497 ft up — roughly 50 ft above '
          'the runway, at the moment of liftoff. **1.23 km is the closest *on-ground* fix, not '
          'the closest fix.** Both archives, adsb.lol and airplanes.live, hold the same point to '
          'the second and to four decimals of position. The correction changes no conclusion: '
          'it still places an airframe and nobody aboard.')
        w('')
    w('Sources: `following/overlaps.csv` and `following/airports.csv` in this repo, as of '
      '28 August 2026; clock times measured from the recovered traces under '
      '`Planes/<TAIL>/data/recovered/`; town population from the US Census 2020; annual '
      'traffic from [%s](%s).' % (tr["srcname"], tr["src"]))
    w('')
    w('Back to [every qualifying field-year](/Planes/example/overview).')

    path = os.path.join(HERE, "%s_%s.mdx" % (t["file"], year))
    open(path, "w").write("\n".join(L) + "\n")
    return path, len(items), len(erika)

if __name__ == "__main__":
  q = qualifying()
  made = []
  for (code, year), items in sorted(q.items(),
                                    key=lambda kv: (TOWNS[kv[0][0]]["tier"], kv[0][1])):
      made.append(build(code, year, items))
  for path, n, e in made:
      print("%-22s %2d rows, %d with Erika claimed" % (os.path.basename(path), n, e))
  print("%d pages" % len(made))
