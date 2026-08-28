#!/usr/bin/env python3
"""
build_flight_record.py

Puts the HARD MOVEMENT RECORD on every aircraft page: every flight leg the
recovered traces support, and every airport the aircraft was ever on the ground
at, with dates and times.

This is the section that answers the reader's actual question — where did this
plane go, and when — instead of describing that a question exists.

Sources (all local):
  analysis/flight_legs.csv     2,349 legs, each labelled direct / overnight / gap
  analysis/master_proximity.csv  ground visits with times and distances

THE GAP LABEL IS NOT DECORATION.  Most legs are "we saw it at A, and later we
saw it at B".  An unobserved gap of 300 days is not a 300-day flight, and the
table says so on every row rather than in a footnote.
"""

import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
import pagefacts as pf  # noqa: E402

START = "{/* CK_FLIGHT_RECORD:START */}"
END = "{/* CK_FLIGHT_RECORD:END */}"
ANCHOR = "{/* CK_PAGE_FOOTER_START */}"

TAIL_DIR = {
    "N102DZ": "N102DZ", "N1098L": "N1098L", "N2100L": "N2100L",
    "N40JD": "N40JD", "N560TW": "N560TW", "N582MM": "N582MM",
    "N59906": "N59906", "N708JH": "N708JH", "N872RA": "N872RA",
    "N888KG": "N888KG", "SU-BGM": "SU-BGM", "SU-BND": "SU-BND",
    "SU-BTT": "SU-BTT", "SU-BTU": "SU-BTU", "SU-BTV": "SU-BTV",
    "T7-ELL": "T7-ELL",
}

MAX_LEG_ROWS = 120   # long fleets get the most recent legs plus a stated total


def conf_cell(r):
    c = (r.get("confidence") or "").strip()
    if c.startswith("direct"):
        return "**direct** — continuous"
    if c.startswith("overnight"):
        return "overnight — crossed a UTC midnight"
    un = (r.get("unobserved_days_inside_leg") or "0").strip()
    try:
        n = int(un)
    except ValueError:
        n = 0
    if n <= 0:
        return "gap — not continuously observed"
    return f"**gap — unobserved {n} day{'s' if n != 1 else ''}**"


def leg_table(legs):
    out = ["| Leg date (UTC) | From | To | Left after (UTC) | Arrived by (UTC) | How well observed |",
           "|---|---|---|---|---|---|"]
    for r in legs:
        oname, oplace = pf.place(r["origin"], r.get("origin_name"))
        dname, dplace = pf.place(r["dest"], r.get("dest_name"))
        arr_date = r.get("arrive_utc_date", "")
        arr = pf.hhmm(r.get("arrive_by_utc", "")) or "—"
        if arr_date and arr_date != r["utc_date"]:
            arr = f"{arr_date} {arr}"
        out.append(
            f"| {r['utc_date']} "
            f"| {pf.ap_link(r['origin'], bold=True)} {pf.esc(oplace)} "
            f"| {pf.ap_link(r['dest'], bold=True)} {pf.esc(dplace)} "
            f"| {pf.hhmm(r.get('depart_after_utc','')) or '—'} "
            f"| {arr} "
            f"| {conf_cell(r)} |"
        )
    return "\n".join(out)


def airport_table(visits):
    """visits: airport_code -> list of visit dicts"""
    out = ["| Airport | Name | Where | Ground visits | First seen | Last seen |",
           "|---|---|---|---:|---|---|"]
    def key(code):
        return (-len(visits[code]), code)
    for code in sorted(visits, key=key):
        vs = sorted(visits[code], key=lambda x: x["date"])
        name, where = pf.place(code, vs[0].get("name", ""))
        out.append(
            f"| {pf.ap_link(code, bold=True)} | {pf.esc(name)} "
            f"| {pf.esc(where)} | {len(vs)} "
            f"| {vs[0]['date']} | {vs[-1]['date']} |"
        )
    return "\n".join(out)


def build(tail, legs, visits):
    L = [START, ""]
    L.append("## Where this aircraft actually went, and when")
    L.append("")

    if not legs and not visits:
        L.append(
            "**No recovered flight legs and no recorded ground visits for this "
            "aircraft.** Nothing in the free ADS-B archives places this airframe "
            "anywhere. That is a coverage statement, not a statement that it did "
            "not fly."
        )
        L.append("")
        L.append(END)
        return "\n".join(L)

    countries = {pf.country(c) for c in visits if pf.country(c)}
    if legs:
        first, last = legs[0]["utc_date"], legs[-1]["utc_date"]
        direct = sum(1 for r in legs if (r.get("confidence") or "").startswith("direct"))
        L.append(
            f"**{len(legs)} flight legs recovered, {first} to {last}, touching "
            f"{len(visits)} airport{'s' if len(visits) != 1 else ''} in "
            f"{len(countries)} countr{'ies' if len(countries) != 1 else 'y'}. "
            f"{direct} of the {len(legs)} are continuously observed end to end.**"
        )
        L.append("")

    L.append(
        "**Read the last column before you read anything else.** A leg marked "
        "*gap* means the archives saw this aircraft at one field and then, some "
        "number of days later, at another. It is not a claim that the aircraft "
        "flew directly between them, and intermediate stops are **not** ruled "
        "out. A leg marked *direct* is one the traces actually follow from "
        "wheels-up to wheels-down."
    )
    L.append("")

    if visits:
        L.append("### Every airport this aircraft was on the ground at")
        L.append("")
        L.append(airport_table(visits))
        L.append("")

    if legs:
        shown = legs
        note = ""
        if len(legs) > MAX_LEG_ROWS:
            shown = legs[-MAX_LEG_ROWS:]
            note = (f"\n*Showing the most recent {MAX_LEG_ROWS} of {len(legs)} "
                    f"recovered legs. The full set is in "
                    f"`analysis/flight_legs.csv`.*\n")
        L.append("### Every recovered flight leg")
        L.append("")
        L.append(leg_table(shown))
        L.append("")
        if note:
            L.append(note)

    L.append(
        "Every airport code above opens that field's own page — every recovered "
        "ground visit and flight leg there, by every aircraft this "
        "investigation tracks. See also "
        "[every airport in this investigation](/Planes/Airports/overview)."
    )
    L.append("")
    L.append(
        "*Times are UTC as the archives recorded them — the last on-ground "
        "position before departure and the first on-ground position after "
        "arrival — not filed or scheduled times. Built by "
        "`build_flight_record.py`; see "
        "[Investigating Deleted Flights](/Planes/investigating_deleted_flights) "
        "for how much of the record is missing and why.*"
    )
    L.append("")
    L.append(END)
    return "\n".join(L)


def main():
    legs = defaultdict(list)
    for r in pf.read_csv("flight_legs.csv"):
        legs[r["tail"]].append(r)
    for t in legs:
        legs[t].sort(key=lambda r: (r["utc_date"], r.get("depart_after_utc", "")))

    visits = defaultdict(lambda: defaultdict(list))
    for r in pf.read_csv("master_proximity.csv"):
        visits[r["tail"]][r["airport_code"]].append({
            "date": r["date"], "name": r.get("airport_name", ""),
        })

    changed = 0
    for tail, d in sorted(TAIL_DIR.items()):
        page = os.path.join(pf.PLANES, d, "overview.mdx")
        if not os.path.exists(page):
            print(f"  MISSING PAGE  {tail}")
            continue
        block = build(tail, legs.get(tail, []), visits.get(tail, {}))
        hit = pf.splice(page, block, START, END, ANCHOR)
        changed += bool(hit)
        print(f"  {tail:10s} {len(legs.get(tail, [])):4d} legs  "
              f"{len(visits.get(tail, {})):3d} airports  "
              f"{'updated' if hit else 'unchanged'}")
    print(f"\nPages changed: {changed}")


if __name__ == "__main__":
    main()
