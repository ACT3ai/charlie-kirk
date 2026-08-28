#!/usr/bin/env python3
"""
build_event_aircraft.py

Puts the BLIND SWEEP RESULT on every Charlie / Erika / TPUSA speaking-event page:
on this date, in a 50-mile circle on this city, what was actually on the ground.

The sweep does not know a tail number, so it cannot be steered toward a wanted
answer.  That is the whole reason it is worth publishing per event.

THE LADD TRAP, and why this script exists in this shape.
--------------------------------------------------------
`geo_ground_foreign.csv` calls an aircraft "notable" if it carries ANY of six
flags.  12,889 of its ~16,000 rows carry only `dbflag:LADD` — the FAA's
Limiting Aircraft Data Displayed privacy program.  At Provo that is mostly
flight-school Cessna 172s.  Printing the raw "notable" count next to a Kirk
event would tell a reader that 50 suspicious aircraft were present when 45 of
them are trainers whose owner filed a routine privacy form.

So LADD is broken out, labelled ordinary, and EXCLUDED from the named table.
The named table carries only foreign registration, military, government
operator, and unregistered / non-ICAO address.

Sources (all local):
  analysis/geo_circle_days.csv     per circle-day totals, event and control
  analysis/geo_ground_foreign.csv  the flagged aircraft themselves
  following/tpusa_events.csv       event -> page mapping
"""

import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
import pagefacts as pf  # noqa: E402

START = "{/* CK_EVENT_AIRCRAFT:START */}"
END = "{/* CK_EVENT_AIRCRAFT:END */}"
ANCHOR = "{/* CK_PAGE_FOOTER_START */}"

SPEAKING = os.path.join(pf.FOLLOWING, "speaking")
MAX_NAMED = 60


def categorise(flags):
    """
    Returns (set_of_categories, ladd_only).
    Order matters for display; a row can hold more than one.
    """
    toks = set(t.strip() for t in (flags or "").split("|") if t.strip())
    cats = set()
    for t in toks:
        if t == "non_us_registration":
            cats.add("Foreign registration")
        elif t == "dbflag:military" or t == "us_military_serial":
            cats.add("Military")
        elif t == "government_operator_string":
            cats.add("Government operator")
        elif t in ("no_registration", "non_icao_address"):
            cats.add("Unregistered / non-ICAO address")
        elif t == "dbflag:LADD":
            cats.add("FAA privacy program (LADD)")
        elif t.startswith("dbflag:"):
            cats.add("Other database flag")
        elif t.startswith("tracked_fleet:"):
            cats.add("Already tracked by this investigation")
    ladd_only = cats <= {"FAA privacy program (LADD)",
                         "Already tracked by this investigation"} \
        and "FAA privacy program (LADD)" in cats
    return cats, ladd_only


REAL = ["Foreign registration", "Military", "Government operator",
        "Unregistered / non-ICAO address"]


def load_events():
    """page stem -> event row"""
    out = {}
    for r in pf.read_csv("tpusa_events.csv", base=pf.FOLLOWING):
        p = (r.get("mdx_page") or "").strip()
        if p.endswith(".mdx"):
            out[os.path.basename(p)[:-4]] = r
    return out


def build(stem, ev, circle_rows, ground_rows, control_by_date):
    city = ev["city"].strip()
    state = ev["state"].strip()
    edate = ev["dates"].strip()
    who = ev.get("who", "").strip() or "Charlie"

    L = [START, ""]
    L.append("## What was actually on the ground near this event")
    L.append("")

    if not circle_rows:
        L.append(
            f"**This date was not covered by the geographic sweep.** The sweep "
            f"streams an entire UTC day of the open ADS-B archive and filters it "
            f"to a 50-mile circle on the event city. It has not been run for "
            f"{edate} at {pf.esc(city)}, {pf.esc(state)}, so this page cannot say "
            f"what was or was not parked nearby."
        )
        L.append("")
        L.append(
            "That is a **gap in our coverage, not a finding**. It is not evidence "
            "that nothing was there, and it must never be quoted as though it "
            "were. The sweep reaches 2023 onward and covers none of 2022; see "
            "[Investigating Deleted Flights]"
            "(/Planes/investigating_deleted_flights) for exactly which days are "
            "held."
        )
        L.append("")
        L.append(END)
        return "\n".join(L)

    L.append(
        f"A **blind geographic sweep** streams an entire UTC day of the open "
        f"ADS-B archive — 74,000 to 95,000 aircraft — and keeps only what fell "
        f"inside a 50-mile circle on **{pf.esc(city)}, {pf.esc(state)}**. It is "
        f"not given a tail number, so it cannot be steered toward a wanted "
        f"answer. Here is what it found around this event."
    )
    L.append("")

    # ---- the per-day totals
    L.append("| Sweep day (UTC) | | Aircraft entering the circle | On the ground | Flagged on the ground |")
    L.append("|---|---|---:|---:|---:|")
    for r in sorted(circle_rows, key=lambda x: x["sweep_date"]):
        n = pf.days_between(r["sweep_date"], edate)
        lab = pf.when_label(n)
        L.append(
            f"| {r['sweep_date']} | {lab} | {r.get('entering','—')} "
            f"| {r.get('on_ground','—')} | {r.get('notable_ground_all','—')} |"
        )
    L.append("")

    # ---- what "flagged" is actually made of
    per_cat = defaultdict(lambda: defaultdict(int))
    ladd = defaultdict(int)
    named = []
    for r in ground_rows:
        cats, only = categorise(r.get("flag_reasons"))
        d = r["sweep_date"]
        if only:
            ladd[d] += 1
        for c in cats:
            per_cat[c][d] += 1
        if cats & set(REAL):
            named.append(r)

    dates = sorted({r["sweep_date"] for r in circle_rows})
    L.append("### What \"flagged\" is actually made of")
    L.append("")
    head = "| Category | " + " | ".join(dates) + " | What it means |"
    L.append(head)
    L.append("|---|" + "---:|" * len(dates) + "---|")
    MEANING = {
        "Foreign registration": "**The category this investigation is about.** A non-US civil registration.",
        "Military": "A military serial or a military database flag. Mostly routine — see the note below.",
        "Government operator": "The registered operator string names a government body.",
        "Unregistered / non-ICAO address": "No registration resolved, or a transponder address outside the ICAO block.",
        "FAA privacy program (LADD)": "**Ordinary and not suspicious.** Thousands of US owners file for this; at a training field it is mostly Cessna 172s.",
        "Other database flag": "Another community-database flag.",
        "Already tracked by this investigation": "An aircraft already on this site's list, found here by geography rather than by name.",
    }
    for c in REAL + ["FAA privacy program (LADD)", "Other database flag",
                     "Already tracked by this investigation"]:
        if c not in per_cat:
            continue
        cells = " | ".join(str(per_cat[c].get(d, 0)) for d in dates)
        L.append(f"| {c} | {cells} | {MEANING.get(c,'')} |")
    L.append("")
    total_ladd = sum(ladd.values())
    if total_ladd:
        L.append(
            f"**{total_ladd} of the flagged aircraft here carry nothing but the "
            f"FAA privacy flag.** They are excluded from the named table below. "
            f"Counting them as suspicious is the single easiest way to inflate a "
            f"number on this subject, and this site will not do it."
        )
        L.append("")

    # ---- the named table
    L.append("### The foreign, military, government and unregistered aircraft, named")
    L.append("")
    if not named:
        L.append(
            "**None.** On the swept days around this event, no foreign-registered, "
            "military, government-operated or unregistered aircraft was on the "
            "ground inside the circle."
        )
        L.append("")
    else:
        named.sort(key=lambda r: (r["sweep_date"], r.get("reg") or "zzz"))
        shown = named[:MAX_NAMED]
        L.append("| Date (UTC) | Registration | Type | Operator | Field | Mi from field | Ground window (UTC) | Why flagged |")
        L.append("|---|---|---|---|---|---:|---|---|")
        for r in shown:
            cats, _ = categorise(r.get("flag_reasons"))
            why = ", ".join(sorted(cats & set(REAL)))
            reg = (r.get("reg") or "").strip() or "*(none)*"
            op = (r.get("operator") or "").strip() or "—"
            if len(op) > 40:
                op = op[:37].rstrip() + "…"
            fname, fplace = pf.place(r.get("nearest_field", ""))
            L.append(
                f"| {r['sweep_date']} | **{pf.esc(reg)}** "
                f"| {pf.esc(r.get('type') or '—')} | {pf.esc(op)} "
                f"| **{pf.esc(r.get('nearest_field') or '—')}** {pf.esc(fplace)} "
                f"| {r.get('nearest_field_mi','—')} "
                f"| {pf.window(r.get('first_utc'), r.get('last_utc'))} "
                f"| {pf.esc(why)} |"
            )
        L.append("")
        if len(named) > MAX_NAMED:
            L.append(f"*Showing {MAX_NAMED} of {len(named)} rows.*")
            L.append("")

    # ---- control comparison, the yardstick
    ctl = []
    for d in dates:
        ctl.extend(control_by_date.get(d, []))
    if ctl:
        def avg(key):
            vals = []
            for r in ctl:
                try:
                    vals.append(float(r.get(key) or 0))
                except ValueError:
                    pass
            return sum(vals) / len(vals) if vals else 0.0
        ev_notable = [float(r.get("notable_ground_all") or 0) for r in circle_rows]
        ev_ground = [float(r.get("on_ground") or 0) for r in circle_rows]
        L.append("### The same days, at cities with no event")
        L.append("")
        L.append(
            f"On these same sweep dates the run also covered six control cities "
            f"with no Kirk or TPUSA event. Averaged per circle-day:"
        )
        L.append("")
        L.append("| | On the ground | Flagged on the ground |")
        L.append("|---|---:|---:|")
        L.append(f"| **This event circle** | {sum(ev_ground)/len(ev_ground):.1f} "
                 f"| {sum(ev_notable)/len(ev_notable):.1f} |")
        L.append(f"| Control circles ({len(ctl)} circle-days) | {avg('on_ground'):.1f} "
                 f"| {avg('notable_ground_all'):.1f} |")
        L.append("")
        L.append(
            "**Do not read a bigger number here as a finding.** Event cities are "
            "large metros with large airports; several control cities are not. A "
            "raw per-circle comparison measures airport size, and once it is "
            "normalised for that, event circles hold a *lower* share of flagged "
            "aircraft than the controls. See "
            "[Investigating Deleted Flights]"
            "(/Planes/investigating_deleted_flights) §4.5."
        )
        L.append("")

    L.append(
        "**What this section cannot tell you.** A trace proves presence — never "
        "purpose, and never occupancy. Military aircraft near Salt Lake City are "
        "routine: the Utah Air National Guard's refuelling wing is based at the "
        "airport and the Army Guard flies helicopters from South Valley Regional. "
        "An aircraft being in a circle is not an aircraft being *at* an event."
    )
    L.append("")
    L.append(
        "*Built by `build_event_aircraft.py` from the adsb.lol GitHub Release "
        "backup (ODbL). See [Investigating Deleted Flights]"
        "(/Planes/investigating_deleted_flights) for coverage and limits.*"
    )
    L.append("")
    L.append(END)
    return "\n".join(L)


def main():
    events = load_events()

    circles = defaultdict(list)
    control_by_date = defaultdict(list)
    for r in pf.read_csv("geo_circle_days.csv"):
        if r.get("circle_kind") == "control":
            control_by_date[r["sweep_date"]].append(r)
        else:
            circles[(r["event_date"], r["city"].strip().lower())].append(r)

    ground = defaultdict(list)
    for r in pf.read_csv("geo_ground_foreign.csv"):
        ground[(r["event_date"], r["city"].strip().lower())].append(r)

    changed = swept = unswept = 0
    for name in sorted(os.listdir(SPEAKING)):
        if not name.endswith(".mdx") or name.startswith("_") or name == "overview.mdx":
            continue
        stem = name[:-4]
        ev = events.get(stem)
        if not ev:
            print(f"  NO EVENT ROW  {stem}")
            continue
        key = (ev["dates"].strip(), ev["city"].strip().lower())
        crows = circles.get(key, [])
        block = build(stem, ev, crows, ground.get(key, []), control_by_date)
        if pf.splice(os.path.join(SPEAKING, name), block, START, END, ANCHOR):
            changed += 1
        if crows:
            swept += 1
        else:
            unswept += 1

    print(f"speaking pages: {swept} with sweep data, {unswept} without")
    print(f"Pages changed: {changed}")


if __name__ == "__main__":
    main()
