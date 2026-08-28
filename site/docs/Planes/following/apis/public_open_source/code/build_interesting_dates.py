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
import json
import os
import re
import sys
from collections import defaultdict

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


def offset_label(off):
    try:
        n = int(off)
    except (TypeError, ValueError):
        return "—"
    if n == 0:
        return "**day 0**"
    return f"day {n:+d}"


def load_incidents(airports):
    """One row per (tail, date, airport) ground visit inside 50 mi of an event."""
    path = os.path.join(ANALYSIS, "master_proximity.csv")
    rows = []
    with open(path, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            if r.get("within_50mi") != "yes":
                continue
            place, apname = airport_place(
                r["airport_code"], r.get("airport_name"), r.get("airport_city"), airports
            )
            rows.append({
                "tail": r["tail"],
                "date": r["date"],
                "win": window(r.get("first_seen_utc"), r.get("last_seen_utc")),
                "first": r.get("first_seen_utc", ""),
                "who": r.get("nearest_event_who") or "—",
                "airport": r["airport_code"],
                "airport_name": apname,
                "place": place,
                "event_city": r.get("nearest_event_city", ""),
                "event_state": r.get("nearest_event_state", ""),
                "event_date": r.get("nearest_event_date", ""),
                "event_title": (r.get("nearest_event_title") or "").strip(),
                "offset": r.get("event_offset_days", ""),
                "miles": r.get("miles_to_event_city", ""),
                "km": r.get("median_km_from_field", ""),
                "points": r.get("ground_points", ""),
                "archives": r.get("archives_agreeing", ""),
                "sources": r.get("sources", ""),
                "same_day": r.get("same_day") == "yes",
                "event_page": r.get("event_page", ""),
            })
    rows.sort(key=lambda x: (x["tail"], x["date"], x["airport"]))
    return rows


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
    head += ["Who", "Airport", "City, State", "Event", "Event city", "Mi", "When"]
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
        cells = [r["date"], r["win"]]
        if show_tail:
            cells.insert(0, f"**{r['tail']}**")
        cells += [
            esc(r["who"]),
            f"**{r['airport']}**",
            esc(r["place"]),
            ev,
            esc(ecity),
            mi,
            offset_label(r["offset"]),
        ]
        out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out)


def provo_table(rows):
    """Foreign-fleet ground presence at Provo, event or not."""
    out = ["| Date (UTC) | Aircraft | Ground window (UTC) | km from field | Ground fixes |",
           "|---|---|---|---:|---:|"]
    for r in rows:
        out.append(
            f"| {r['date']} | **{r['tail']}** | {r['win']} | {r['km']} | {r['points']} |"
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
        "event. One row per incident. The ground window is the first and last "
        "on-ground position the archives recorded that day, in UTC, not a filed "
        "departure or arrival time."
    )
    L.append("")
    L.append(f"**What this aircraft is:** {kind}.")
    L.append("")

    if rows:
        L.append(
            f"**{len(rows)} incident{'s' if len(rows) != 1 else ''} "
            f"across {len({r['date'] for r in rows})} date"
            f"{'s' if len({r['date'] for r in rows}) != 1 else ''}, "
            f"at {len({r['airport'] for r in rows})} airport"
            f"{'s' if len({r['airport'] for r in rows}) != 1 else ''}. "
            f"{sum(1 for r in rows if r['same_day'])} of them are same-day.**"
        )
        L.append("")
        L.append(incident_table(rows, defs))
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
    incidents = load_incidents(airports)
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
