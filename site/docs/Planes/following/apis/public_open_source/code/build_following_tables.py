#!/usr/bin/env python3
"""
build_following_tables.py

Puts the "which aircraft were near this person, and when" tables on the pages
that are ABOUT A PERSON rather than about an airframe:

  Planes/Charlie-Erika-Aircraft/overview.mdx    Charlie's side
  Planes/Erika-Flight-Logs-Erased.mdx           Erika's side
  Planes/following/Erika_*.mdx                  every Erika page

Each table is one row per incident: date, ground time window, which aircraft,
who the event was for, the airport, and the city + state.

The split that runs through all of it: an aircraft that carries the man showing
up where the man is is NOT following him.  So the Kirk/TPUSA fleet and everything
else are always in separate tables, never summed into one number.

Reads the incident set built by build_interesting_dates.py.  Run that first.
"""

import datetime
import importlib.util
import json
import os
import re
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "bid", os.path.join(HERE, "build_interesting_dates.py"))
bid = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bid)

PLANES = bid.PLANES
FOLLOWING = bid.FOLLOWING

START = "{/* CK_FOLLOWING_TABLE:START */}"
END = "{/* CK_FOLLOWING_TABLE:END */}"

# The Kirk / TPUSA side.  Proximity here is the expected thing, and it is the
# yardstick every other row is read against.
KIRK_FLEET = {"N582MM", "N560TW", "N872RA", "N102DZ", "N888KG", "N40JD"}

TAIL_NOTE = {
    "N582MM": "TPUSA-associated Learjet",
    "N560TW": "Kirk-side jet, Scottsdale base",
    "N872RA": "Kirk-side jet",
    "N102DZ": "Kirk-side jet",
    "N888KG": "Kirk-side jet",
    "N40JD": "Kirk-side jet",
    "N1098L": "LASAI Aviation II Global 6500 (AXEL10)",
    "N2100L": "LASAI Aviation II Global 6500 (AXEL21)",
    "N59906": "Piper Navajo aerial-survey aircraft",
    "N708JH": "US Government / DOJ Gulfstream G550",
    "SU-BTT": "Egypt — Dassault Falcon 7X",
    "SU-BND": "Egypt — Gulfstream",
    "SU-BTU": "Egypt — Dassault Falcon 7X",
    "SU-BTV": "Egypt — Dassault Falcon 7X",
    "SU-BGM": "Egypt — Gulfstream IV",
    "T7-ELL": "San Marino registration",
}


def table(rows, show_event=True):
    head = ["Date (UTC)", "Ground window (UTC)", "Aircraft", "What it is",
            "Airport", "City, State", "Whose event"]
    if show_event:
        head += ["Event", "Event city, state"]
    head += ["Mi", "When", "Found by"]
    out = ["| " + " | ".join(head) + " |"]
    align = ["---"] * len(head)
    align[head.index("Mi")] = "---:"
    out.append("| " + " | ".join(align) + " |")
    for r in rows:
        try:
            mi = f"{float(r['miles']):.1f}"
        except (TypeError, ValueError):
            mi = "—"
        title = r["event_title"]
        if len(title) > 46:
            title = title[:43].rstrip() + "…"
        ev = bid.esc(title) if title else "—"
        link = bid.event_link(r["event_page"])
        if link and ev != "—":
            ev = f"[{ev}]({link})"
        ecity = f"{r['event_city']}, {r['event_state']}".strip(", ") or "—"
        cells = [
            r["date"], r["win"], f"**{r['tail']}**",
            bid.esc(TAIL_NOTE.get(r["tail"], "—")),
            f"**{r['airport']}**", bid.esc(r["place"]), bid.esc(r["who"]),
        ]
        if show_event:
            cells += [ev, bid.esc(ecity)]
        cells += [
            mi,
            bid.offset_label(r["offset"]),
            {"both": "**both routes**", "sweep": "blind sweep",
             "per-tail": "per-tail"}.get(r["found_by"], r["found_by"]),
        ]
        out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out)


def summary_by_tail(rows, label):
    """A compact per-aircraft roll-up above the long table."""
    by = defaultdict(list)
    for r in rows:
        by[r["tail"]].append(r)
    out = [f"| Aircraft | What it is | Contacts | Dates | Airports | First | Last |",
           "|---|---|---:|---:|---|---|---|"]
    for tail in sorted(by, key=lambda t: (-len(by[t]), t)):
        rs = sorted(by[tail], key=lambda x: x["date"])
        aps = sorted({x["airport"] for x in rs})
        out.append(
            f"| **{tail}** | {bid.esc(TAIL_NOTE.get(tail, '—'))} | {len(rs)} | "
            f"{len({x['date'] for x in rs})} | {', '.join(aps)} | "
            f"{rs[0]['date']} | {rs[-1]['date']} |"
        )
    return "\n".join(out)


def build_block(person, rows_all, self_page=""):
    """person is 'Charlie' or 'Erika'.  self_page suppresses a self-link."""
    if person == "Charlie":
        want = {"Charlie", "Both"}
        other = "Erika"
    else:
        want = {"Erika", "Both"}
        other = "Charlie"

    rows = [r for r in rows_all if r["who"] in want]
    rows.sort(key=lambda x: (x["date"], x["tail"], x["win"]))
    kirk = [r for r in rows if r["tail"] in KIRK_FLEET]
    outside = [r for r in rows if r["tail"] not in KIRK_FLEET]

    L = [START, ""]
    L.append(f"## Which aircraft were near {person} Kirk, and exactly when")
    L.append("")
    L.append(
        f"One row per ground contact: an aircraft **on the ground**, on one UTC "
        f"day, at one airport, within 50 miles of a sourced **{person} Kirk** "
        f"event on the event date or either adjacent day. The ground window is "
        f"the first and last on-ground position the archives actually recorded — "
        f"not a filed departure or arrival time."
    )
    L.append("")
    L.append(
        f"**{len(rows)} contact{'s' if len(rows) != 1 else ''} in total: "
        f"{len(kirk)} by the Kirk/TPUSA fleet, {len(outside)} by everything else.**"
    )
    L.append("")

    # ---- the table that answers the following question
    L.append("### Aircraft outside the Kirk and TPUSA fleet")
    L.append("")
    if outside:
        L.append(
            "This is the table the following claim is actually about — aircraft "
            "with no established role carrying the Kirks or the organisation."
        )
        L.append("")
        L.append(summary_by_tail(outside, person))
        L.append("")
        L.append(table(outside))
        L.append("")
    else:
        L.append(
            f"**Empty. Not one row.** Across every day of recovered trace this "
            f"investigation holds, no Egyptian-registered aircraft — and no other "
            f"aircraft outside the Kirk/TPUSA fleet — is on the ground within 50 "
            f"miles of a sourced **{person} Kirk** event on the event date or "
            f"either adjacent day."
        )
        L.append("")
        L.append(
            "That is a published result and it points away from the claim, so it "
            "is stated here as plainly as a hit would be. It is **not** proof "
            "nothing happened: see the limits below."
        )
        L.append("")

    # ---- the yardstick
    L.append("### The Kirk and TPUSA fleet, for comparison")
    L.append("")
    if kirk:
        L.append(
            "**An aircraft that carries the man showing up where the man is, is "
            "not surveillance.** These rows are the yardstick: they are what a "
            "genuine travels-with-them pattern looks like in this data, and every "
            "row in the table above should be read against them."
        )
        L.append("")
        L.append(summary_by_tail(kirk, person))
        L.append("")
        L.append(table(kirk))
        L.append("")
    else:
        L.append(
            f"No Kirk or TPUSA aircraft appears near a sourced **{person} Kirk** "
            f"event in the recovered traces either. With both tables empty, the "
            f"limiting factor is coverage, not the aircraft."
        )
        L.append("")

    # ---- limits, which for Erika are the whole story
    L.append("### What these tables cannot tell you")
    L.append("")
    L.append(
        "* **A trace proves presence. It never proves purpose, and it never "
        "proves occupancy.** No ADS-B record anywhere places any person aboard "
        "any aircraft. An aircraft near an event is an airframe near an event."
    )
    if person == "Erika":
        L.append(
            "* **Erika Kirk's flight logs are reported erased, and no archive "
            "anywhere produces her itinerary.** Every row above is anchored to a "
            "sourced *event* she is recorded as attending, not to a document "
            "saying where she was. This is the single largest hole in the whole "
            "overlap claim."
            + ("" if self_page == "Erika-Flight-Logs-Erased" else
               " See [Erika Flight Logs Erased]"
               "(/Planes/Erika-Flight-Logs-Erased).")
        )
        L.append(
            "* **The sourced Erika event calendar is short.** These tables can "
            "only test the events this repository can source. That is nowhere "
            "near every place she went, so an empty row is a statement about our "
            "calendar as much as about any aircraft."
        )
    else:
        L.append(
            "* **139 sourced events is nowhere near every place Charlie Kirk "
            "went.** An aircraft that is absent from these tables was not "
            "necessarily absent from his travel."
        )
    L.append(
        "* **An absence is not a finding.** A day with no row may be a day a "
        "volunteer receiver network heard nothing. Transponder off, outside "
        "coverage, and genuinely elsewhere all look identical from here."
    )
    L.append(
        "* **2022 is effectively blank.** No free archive covers it, so no row "
        "above and no gap above can speak to that year."
    )
    L.append("")
    L.append(
        "*Built by `build_following_tables.py` from the recovered ADS-B traces, "
        "through both recovery routes. See "
        "[Investigating Deleted Flights](/Planes/investigating_deleted_flights) "
        "for how the data was recovered, what percentage of it we hold, and where "
        "it is missing.*"
    )
    L.append("")
    L.append(END)
    return "\n".join(L)


def splice(path, block):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    if START in text and END in text:
        new = text.split(START)[0] + block + text.split(END, 1)[1]
    else:
        new = text.rstrip("\n") + "\n\n---\n\n" + block + "\n"
    if new != text:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(new)
        return True
    return False


def main():
    data = os.path.join(bid.ANALYSIS, "interesting_dates.json")
    if not os.path.exists(data):
        sys.exit("Run build_interesting_dates.py first.")
    rows = json.load(open(data, encoding="utf-8"))

    targets = [("Charlie", os.path.join(PLANES, "Charlie-Erika-Aircraft/overview.mdx"))]
    targets.append(("Erika", os.path.join(PLANES, "Erika-Flight-Logs-Erased.mdx")))
    for name in sorted(os.listdir(FOLLOWING)):
        if name.startswith("Erika_") and name.endswith(".mdx"):
            targets.append(("Erika", os.path.join(FOLLOWING, name)))

    changed = 0
    for person, path in targets:
        if not os.path.exists(path):
            print(f"  MISSING  {path}")
            continue
        stem = os.path.splitext(os.path.basename(path))[0]
        block = build_block(person, rows, self_page=stem)
        if splice(path, block):
            changed += 1
            mark = "updated"
        else:
            mark = "unchanged"
        print(f"  {person:8s} {mark:10s} {os.path.relpath(path, PLANES)}")
    print(f"\nPages changed: {changed}")


if __name__ == "__main__":
    main()
