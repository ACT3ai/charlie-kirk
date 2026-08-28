#!/usr/bin/env python3
"""
build_interesting_dates.py

Builds the "Interesting dates" tables that go on every aircraft page under
site/docs/Planes/, on the Charlie/Erika aircraft page, and on every Erika page.

ONE ROW PER INCIDENT.  An incident is one aircraft, on the ground, on one UTC
day, at one airport, inside 50 miles of one sourced Charlie / Erika / TPUSA
event.  Every row carries the date, the ground time window exactly as the
archives recorded it, who the event was for, the airport, and the city + state.

Sources, all local, none of this makes a network call:
  analysis/master_proximity.csv      the 4,214 ground visits joined to events
  analysis/definitive_proximity.csv  the archive-verdict enrichment
  analysis/su_presence_union.csv     the two-route union for the foreign fleet
  following/airports.csv             airport -> city, state
  following/tpusa_events.csv         event titles and venues

Writes nothing outside the CK_INTERESTING_DATES markers, so it is idempotent
and can be re-run after any new recovery pass.
"""

import csv
import datetime
import json
import os
import re
import sys
from collections import defaultdict

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
import pagefacts as _pf  # noqa: E402

ROOT = os.path.expanduser("~/BGit/Bryan_git/charlie-kirk")
PLANES = os.path.join(ROOT, "site/docs/Planes")
FOLLOWING = os.path.join(PLANES, "following")
ANALYSIS = os.path.join(FOLLOWING, "apis/public_open_source/data/analysis")

START = "{/* CK_INTERESTING_DATES:START */}"
END = "{/* CK_INTERESTING_DATES:END */}"

# Airports that carry no state in airports.csv.  Filled in by hand rather than
# guessed at run time, so a wrong one is a visible edit and not a silent default.
AIRPORT_FALLBACK = {
    "KAGC": ("West Mifflin", "PA", "Allegheny County Airport"),
    "KAPA": ("Englewood", "CO", "Centennial Airport"),
    "KCRQ": ("Carlsbad", "CA", "McClellan-Palomar Airport"),
    "KDVT": ("Phoenix", "AZ", "Phoenix Deer Valley Airport"),
    "KEUG": ("Eugene", "OR", "Eugene Airport"),
    "KHHR": ("Hawthorne", "CA", "Hawthorne Municipal Airport"),
    "KLAL": ("Lakeland", "FL", "Lakeland Linder International Airport"),
    "KLGB": ("Long Beach", "CA", "Long Beach Airport"),
    "KLZU": ("Lawrenceville", "GA", "Gwinnett County Briscoe Field"),
    "KSDL": ("Scottsdale", "AZ", "Scottsdale Airport"),
    "KSNA": ("Santa Ana", "CA", "John Wayne Airport"),
    "KVNY": ("Los Angeles", "CA", "Van Nuys Airport"),
}

# Where each tail's page lives.  A tail with no page is reported, never dropped.
TAIL_DIR = {
    "N102DZ": "N102DZ", "N1098L": "N1098L", "N2100L": "N2100L",
    "N40JD": "N40JD", "N560TW": "N560TW", "N582MM": "N582MM",
    "N59906": "N59906", "N708JH": "N708JH", "N872RA": "N872RA",
    "N888KG": "N888KG",
    "SU-BGM": "SU-BGM", "SU-BND": "SU-BND", "SU-BTT": "SU-BTT",
    "SU-BTU": "SU-BTU", "SU-BTV": "SU-BTV", "T7-ELL": "T7-ELL",
    "CONTROL-LUFTHANSA": "CONTROL-LUFTHANSA",
    "CONTROL-RYANAIR": "CONTROL-RYANAIR",
}

# One line per tail saying what the aircraft is, so a reader landing on a table
# knows whether proximity is expected or notable.
TAIL_KIND = {
    "N582MM": ("TPUSA-associated Learjet", "expected"),
    "N560TW": ("Kirk-side jet, Scottsdale home base", "expected"),
    "N872RA": ("Kirk-side jet", "expected"),
    "N102DZ": ("Kirk-side jet", "expected"),
    "N888KG": ("Kirk-side jet", "expected"),
    "N40JD": ("Kirk-side jet", "expected"),
    "N1098L": ("LASAI Aviation II Global 6500, callsign AXEL10", "notable"),
    "N2100L": ("LASAI Aviation II Global 6500, callsign AXEL21", "notable"),
    "N59906": ("Piper Navajo aerial-survey aircraft", "notable"),
    "N708JH": ("US Government / Department of Justice Gulfstream G550", "notable"),
    "SU-BTT": ("Egyptian-registered Dassault Falcon 7X", "notable"),
    "SU-BND": ("Egyptian-registered Gulfstream", "notable"),
    "SU-BTU": ("Egyptian-registered Dassault Falcon 7X", "notable"),
    "SU-BTV": ("Egyptian-registered Dassault Falcon 7X", "notable"),
    "SU-BGM": ("Egyptian-registered Gulfstream IV", "notable"),
    "T7-ELL": ("San Marino-registered aircraft", "notable"),
    "CONTROL-LUFTHANSA": ("European control airliner", "control"),
    "CONTROL-RYANAIR": ("European control airliner", "control"),
}

FOREIGN = {"SU-BTT", "SU-BND", "SU-BTU", "SU-BTV", "SU-BGM", "T7-ELL"}

# A bare proximity row is misleading for some of these airframes.  The caveat
# ships with the table, never separately from it.
TAIL_CAVEAT = {
    "N59906": (
        "**The two 10 September contacts are the same survey flight, and the gap "
        "between them is a flight, not a wait.** This aircraft was on the ground at "
        "Provo at 15:08 UTC (09:08 MDT), flew a standard aerial-mapping grid at a "
        "constant 19,000 ft over the Utah Valley, and was back on the ground at "
        "18:08 UTC (12:08 MDT) — roughly fifteen minutes before the shooting. It "
        "passed near UVU because UVU sits inside the survey block. Publishing the "
        "distance without the altitude, the grid, and the landing time would be a "
        "serious misrepresentation."
    ),
    "N708JH": (
        "**The ordinary explanation fits this completely.** A federal aircraft "
        "arriving at the scene of a federal investigation the day after, and at a "
        "national memorial service, is what this aircraft is for. The same sweep "
        "also puts it on the ground at Albuquerque — a control city — so it goes "
        "everywhere. That is the correct frame for these rows."
    ),
    "N1098L": (
        "**Base rate first.** These rows are 1.6% of this aircraft's observed "
        "ground days. That is at or below the ordinary Kirk-side jets and is what a "
        "busy government-contract aircraft flying into major metros produces by "
        "chance."
    ),
    "N2100L": (
        "**Base rate first.** These rows are 3.4% of this aircraft's observed "
        "ground days — at or below the ordinary Kirk-side jets, and consistent with "
        "chance for an aircraft whose dominant field is Biggs Army Airfield."
    ),
    "SU-BTT": (
        "**Two events on nineteen observed days is not a rate.** With a denominator "
        "that small this is an anecdote with a percent sign on it and must not be "
        "quoted as a frequency. Both of this aircraft's events are the same airport "
        "as SU-BND's, on the same two dates."
    ),
    "SU-BND": (
        "**Two events on twenty-two observed days is not a rate.** The aircraft did "
        "not shuttle between these dates — it sat at Provo continuously from 5 to 12 "
        "September 2025 at an unchanging 1.29 km from the field reference point. It "
        "was parked there before Charlie Kirk arrived and still parked two days "
        "after he was killed."
    ),
    "N582MM": (
        "**This is the positive control.** An aircraft that genuinely does travel "
        "with the organisation produces a clear, high, sustained rate — 19.2% across "
        "276 observed days. That is the shape a following pattern makes in this data, "
        "and it is the yardstick every other table on this site should be read "
        "against."
    ),
}


def load_events():
    """(event_date, city) -> (title, page).  The blind sweep records only a city
    and a date, so the human-readable event name is joined back on here."""
    out = {}
    path = os.path.join(FOLLOWING, "tpusa_events.csv")
    if not os.path.exists(path):
        return out
    with open(path, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            d = (r.get("dates") or "").strip()
            city = (r.get("city") or "").strip()
            if not d or not city:
                continue
            key = (d, city.lower())
            if key not in out:
                out[key] = ((r.get("title") or "").strip(),
                            (r.get("mdx_page") or "").strip())
    return out


def load_airports():
    out = {}
    path = os.path.join(FOLLOWING, "airports.csv")
    with open(path, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            out[r["airport_code"]] = (
                r.get("city", "").strip(),
                r.get("state", "").strip(),
                r.get("airport_name", "").strip(),
            )
    return out


def airport_place(code, name_hint, city_hint, airports):
    """City, State for an airport code.  Never guesses a state it does not hold."""
    city = state = name = ""
    if code in airports:
        city, state, name = airports[code]
    if code in AIRPORT_FALLBACK:
        fc, fs, fn = AIRPORT_FALLBACK[code]
        city = city or fc
        state = state or fs
        name = name or fn
    city = city or (city_hint or "").strip()
    name = name or (name_hint or "").strip()
    if city and state:
        place = f"{city}, {state}"
    elif city:
        place = city
    else:
        place = "—"
    return place, name


def hhmm(ts):
    """2025-09-10T13:07:53.123Z -> 13:07"""
    if not ts:
        return ""
    m = re.search(r"T(\d{2}):(\d{2})", ts)
    return f"{m.group(1)}:{m.group(2)}" if m else ""


def window(first, last):
    a, b = hhmm(first), hhmm(last)
    if not a:
        return "—"
    if not b or a == b:
        return f"{a} only"
    return f"{a}–{b}"


def days_after_event(visit_date, event_date):
    """
    THE two source CSVs disagree on the sign of their offset column.
    master_proximity.csv stores (event_date - visit_date); geo_ground_foreign.csv
    stores (sweep_date - event_date).  Reading either one as the other silently
    turns "the day before the assassination" into "the day after".  So neither
    column is ever used: the offset is recomputed here from the two dates.

    Returns visit_date - event_date.  Negative = aircraft was there BEFORE.
    """
    try:
        a = datetime.date.fromisoformat(visit_date)
        b = datetime.date.fromisoformat(event_date)
    except (TypeError, ValueError):
        return None
    return (a - b).days


def offset_label(n):
    if n is None:
        return "—"
    if n == 0:
        return "**Same day**"
    if n == -1:
        return "Day before"
    if n == 1:
        return "Day after"
    if n < 0:
        return f"{abs(n)} days before"
    return f"{n} days after"


def _incident(tail, date, airport, apname_hint, apcity_hint, first, last,
              who, ev_city, ev_state, ev_date, ev_title, miles, km, points,
              archives, sources, event_page, found_by, airports):
    place, apname = airport_place(airport, apname_hint, apcity_hint, airports)
    off = days_after_event(date, ev_date)
    return {
        "tail": tail, "date": date, "airport": airport, "airport_name": apname,
        "win": window(first, last), "first": first or "",
        "who": who or "—", "place": place,
        "event_city": ev_city or "", "event_state": ev_state or "",
        "event_date": ev_date or "", "event_title": (ev_title or "").strip(),
        "offset": off, "miles": miles, "km": km, "points": points,
        "archives": archives, "sources": sources,
        "same_day": off == 0, "event_page": event_page or "",
        "found_by": found_by,
    }


def load_incidents(airports, events=None):
    """
    One row per ground contact inside 50 miles of a sourced event, from BOTH
    recovery lanes:

      per-tail  master_proximity.csv    - asks "where was this tail on this day"
      sweep     geo_ground_foreign.csv  - asks "what was on the ground near this
                                          event", and so can find an aircraft
                                          nobody named

    Neither lane is complete alone.  A contact both lanes hold is marked "both";
    that agreement is itself part of the evidence.
    """
    events = events or {}
    rows = {}

    per_tail = os.path.join(ANALYSIS, "master_proximity.csv")
    with open(per_tail, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            if r.get("within_50mi") != "yes":
                continue
            inc = _incident(
                r["tail"], r["date"], r["airport_code"], r.get("airport_name"),
                r.get("airport_city"), r.get("first_seen_utc"), r.get("last_seen_utc"),
                r.get("nearest_event_who"), r.get("nearest_event_city"),
                r.get("nearest_event_state"), r.get("nearest_event_date"),
                r.get("nearest_event_title"), r.get("miles_to_event_city"),
                r.get("median_km_from_field"), r.get("ground_points"),
                r.get("archives_agreeing"), r.get("sources"), r.get("event_page"),
                "per-tail", airports,
            )
            rows[(inc["tail"], inc["date"], inc["airport"], inc["win"])] = inc

    sweep = os.path.join(ANALYSIS, "geo_ground_foreign.csv")
    if os.path.exists(sweep):
        with open(sweep, newline="", encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                tail = (r.get("reg") or "").strip().upper()
                if tail not in TAIL_DIR:
                    continue
                title, page = events.get(
                    ((r.get("event_date") or "").strip(),
                     (r.get("city") or "").strip().lower()), ("", ""))
                inc = _incident(
                    tail, r["sweep_date"], r.get("nearest_field", ""), "",
                    r.get("city"), r.get("first_utc"), r.get("last_utc"),
                    r.get("who"), r.get("city"), r.get("state"), r.get("event_date"),
                    title, r.get("closest_mi_to_city"), "", r.get("points_in_circle"),
                    "", "adsblol-github-backup (geographic sweep)", page,
                    "sweep", airports,
                )
                key = (inc["tail"], inc["date"], inc["airport"], inc["win"])
                if key in rows:
                    rows[key]["found_by"] = "both"
                else:
                    # A near-match on tail+date+airport is the same contact seen
                    # through a slightly different window; mark it rather than
                    # double-count it.
                    near = [k for k in rows
                            if k[0] == inc["tail"] and k[1] == inc["date"]
                            and k[2] == inc["airport"]]
                    if near:
                        for k in near:
                            rows[k]["found_by"] = "both"
                    else:
                        rows[key] = inc

    out = list(rows.values())
    out.sort(key=lambda x: (x["tail"], x["date"], x["airport"], x["win"]))
    return out


def load_definitive():
    """tail|date|airport -> archive verdict, for the confidence column."""
    path = os.path.join(ANALYSIS, "definitive_proximity.csv")
    out = {}
    if not os.path.exists(path):
        return out
    with open(path, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            out[(r["tail"], r["date"], r["airport"])] = r
    return out


def event_link(page):
    """site/docs/Planes/following/speaking/X.mdx -> /Planes/following/speaking/X"""
    if not page:
        return ""
    p = page.strip()
    if not p.startswith("site/docs/"):
        return ""
    p = p[len("site/docs/"):]
    p = re.sub(r"/(overview)?\.?mdx?$", "", p)
    p = re.sub(r"\.mdx?$", "", p)
    p = re.sub(r"/overview$", "", p)
    return "/" + p


def esc(s):
    """Make a cell safe inside a markdown table and inside MDX."""
    s = (s or "").replace("|", "\\|")
    s = s.replace("{", "&#123;").replace("}", "&#125;")
    s = s.replace("<", "&lt;").replace(">", "&gt;")
    return s


def incident_table(rows, defs, show_tail=False):
    head = ["Date (UTC)", "Ground window (UTC)"]
    if show_tail:
        head.insert(0, "Aircraft")
    head += ["Who", "Airport", "City, State", "Event", "Event city", "Mi", "When", "Found by"]
    out = ["| " + " | ".join(head) + " |"]
    align = ["---"] * len(head)
    align[head.index("Mi")] = "---:"
    out.append("| " + " | ".join(align) + " |")
    for r in rows:
        d = defs.get((r["tail"], r["date"], r["airport"]))
        link = event_link(r["event_page"])
        title = r["event_title"]
        if len(title) > 58:
            title = title[:55].rstrip() + "…"
        ev = esc(title) if title else "—"
        if link and ev != "—":
            ev = f"[{ev}]({link})"
        ecity = f"{r['event_city']}, {r['event_state']}".strip(", ") or "—"
        try:
            mi = f"{float(r['miles']):.1f}"
        except (TypeError, ValueError):
            mi = "—"
        inc_url = f"/Planes/Incidents/{r['tail']}-{r['date']}-{r['airport']}"
        cells = [f"[{r['date']}]({inc_url})", r["win"]]
        if show_tail:
            cells.insert(0, f"**{r['tail']}**")
        cells += [
            esc(r["who"]),
            _pf.ap_link(r["airport"], bold=True),
            esc(r["place"]),
            ev,
            esc(ecity),
            mi,
            offset_label(r["offset"]),
            {"both": "**both routes**", "sweep": "blind sweep",
             "per-tail": "per-tail"}.get(r["found_by"], r["found_by"]),
        ]
        out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out)


def provo_table(rows):
    """Foreign-fleet ground presence at Provo, event or not."""
    out = ["| Date (UTC) | Aircraft | Ground window (UTC) | km from field | "
           "Ground fixes | Field |",
           "|---|---|---|---:|---:|---|"]
    for r in rows:
        out.append(
            f"| {r['date']} | **{r['tail']}** | {r['win']} | {r['km']} | "
            f"{r['points']} | [KPVU](/Planes/Airports/KPVU) |"
        )
    return "\n".join(out)


def build_block_for_tail(tail, rows, defs, all_ground):
    kind, expect = TAIL_KIND.get(tail, ("aircraft in this investigation", "notable"))
    L = []
    L.append(START)
    L.append("")
    L.append("## Interesting dates for this aircraft")
    L.append("")
    L.append(
        "Every date on which the recovered ADS-B traces put this aircraft **on the "
        "ground** within 50 miles of a sourced Charlie Kirk, Erika Kirk, or TPUSA "
        "event. One row per ground contact. The ground window is the first and last "
        "on-ground position the archives recorded that day, in UTC, not a filed "
        "departure or arrival time."
    )
    L.append("")
    L.append(f"**What this aircraft is:** {kind}.")
    L.append("")

    if rows:
        ndates = len({r["date"] for r in rows})
        naps = len({r["airport"] for r in rows})
        L.append(
            f"**{len(rows)} ground contact{'s' if len(rows) != 1 else ''} "
            f"across {ndates} date{'s' if ndates != 1 else ''}, "
            f"at {naps} airport{'s' if naps != 1 else ''}. "
            f"{sum(1 for r in rows if r['same_day'])} "
            f"{'lands' if sum(1 for r in rows if r['same_day']) == 1 else 'land'} "
            f"on the event date itself.**"
        )
        L.append("")
        L.append(
            "One row is one continuous run of on-ground positions. Two rows on the "
            "same date at the same field mean the aircraft took off and came back, "
            "not that it waited."
        )
        L.append("")
        L.append(incident_table(rows, defs))
        L.append("")
        if tail in TAIL_CAVEAT:
            L.append(TAIL_CAVEAT[tail])
            L.append("")
        if expect == "expected":
            L.append(
                "**Read this table the right way.** This is a Kirk- or "
                "TPUSA-associated aircraft. An aircraft that carries the man showing "
                "up where the man is, is not surveillance — these rows are a "
                "data-quality check on the method, not evidence of anything."
            )
        elif expect == "control":
            L.append(
                "**This is a control airframe.** It has no connection to this case "
                "and is queried on the same dates through the same endpoints so that "
                "an archive failure can be told apart from a removal."
            )
        else:
            L.append(
                "**What these rows do and do not establish.** A trace proves "
                "presence. It never proves purpose and it never proves occupancy — "
                "no ADS-B record places any person aboard any aircraft."
            )
        L.append("")
    else:
        L.append(
            "**No incidents. Not one.** Across every day of recovered trace this "
            "investigation holds for this aircraft, it never comes within 50 miles of "
            "a sourced Charlie Kirk, Erika Kirk, or TPUSA event on the event date or "
            "either adjacent day."
        )
        L.append("")
        L.append(
            "That is a published result rather than an empty section. It is also not "
            "proof the aircraft was elsewhere: coverage is thin, and a jet parked with "
            "its transponder off is invisible to a volunteer receiver network."
        )
        L.append("")

    if tail in FOREIGN and all_ground:
        L.append("### Every recorded ground presence at Provo Municipal (KPVU)")
        L.append("")
        L.append(
            "Provo is the field the public argument is built on, so this aircraft's "
            "Provo record is listed in full — including the days that pair with no "
            "event at all."
        )
        L.append("")
        L.append(provo_table(all_ground))
        L.append("")

    L.append(
        "Each date above opens its own page with the full record for that "
        "contact — the exact ground window, the archives that hold it, the "
        "other aircraft at the same field, and what it does and does not "
        "establish. Each airport code opens that field's complete recovered "
        "record. See also "
        "[every interesting date across all aircraft](/Planes/Incidents/overview) "
        "and [every airport in this investigation](/Planes/Airports/overview)."
    )
    L.append("")
    L.append(
        "*Built by `build_interesting_dates.py` from the recovered traces. "
        "See [Investigating Deleted Flights](/Planes/investigating_deleted_flights) "
        "for how the underlying data was recovered and what its limits are.*"
    )
    L.append("")
    L.append(END)
    return "\n".join(L)


def splice(path, block):
    """Replace the marked block, or append it before the first trailing nav section."""
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    if START in text and END in text:
        pre = text.split(START)[0]
        post = text.split(END, 1)[1]
        new = pre + block + post
    else:
        new = text.rstrip("\n") + "\n\n---\n\n" + block + "\n"
    if new != text:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(new)
        return True
    return False


def main():
    airports = load_airports()
    events = load_events()
    incidents = load_incidents(airports, events)
    defs = load_definitive()

    by_tail = defaultdict(list)
    for r in incidents:
        by_tail[r["tail"]].append(r)

    # Provo ground presence for the foreign fleet, from every ground visit not
    # just the event-proximate ones.
    provo = defaultdict(list)
    with open(os.path.join(ANALYSIS, "master_proximity.csv"), newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            if r["airport_code"] == "KPVU" and r["tail"] in FOREIGN:
                provo[r["tail"]].append({
                    "tail": r["tail"], "date": r["date"],
                    "win": window(r.get("first_seen_utc"), r.get("last_seen_utc")),
                    "km": r.get("median_km_from_field", ""),
                    "points": r.get("ground_points", ""),
                })
    for k in provo:
        provo[k].sort(key=lambda x: x["date"])

    changed, report = [], []
    for tail, dirname in sorted(TAIL_DIR.items()):
        page = os.path.join(PLANES, dirname, "overview.mdx")
        if not os.path.exists(page):
            report.append(f"  MISSING PAGE  {tail}  {page}")
            continue
        block = build_block_for_tail(tail, by_tail.get(tail, []), defs, provo.get(tail, []))
        if splice(page, block):
            changed.append(page)
        report.append(f"  {tail:20s} {len(by_tail.get(tail, [])):3d} incidents  -> {dirname}/overview.mdx")

    print(f"Incidents loaded: {len(incidents)} across {len(by_tail)} tails")
    print("\n".join(report))
    print(f"\nPages changed: {len(changed)}")

    # Hand the aggregated rows to the caller for the Charlie / Erika pages.
    out = os.path.join(ANALYSIS, "interesting_dates.json")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(incidents, fh, indent=1)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
