#!/usr/bin/env python3
"""
build_airport_incident_pages.py

Creates the two NEW page types that the tables elsewhere on this site link into,
so that every row in every flight table is a click into the underlying facts
rather than a dead cell:

  /Planes/Airports/<CODE>          one page per airport a case aircraft was
                                   ever on the ground at, or flew a recovered
                                   leg into or out of.  289 fields.

  /Planes/Incidents/<TAIL>-<DATE>-<FIELD>
                                   one page per ground contact inside 50 miles
                                   of a sourced Charlie / Erika / TPUSA event.

Control-airliner-only airports are deliberately NOT given pages: the controls
exist to test the archives, and a page for every European field Ryanair touched
would bury the case record.  They stay in the CSVs and in the control tables.

Every fact on these pages comes from a file in this repository.  Nothing is
written that is not in the data.
"""

import json
import os
import re
import sys
from collections import defaultdict

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
import pagefacts as pf  # noqa: E402

AIRPORTS_DIR = os.path.join(pf.PLANES, "Airports")
INCIDENTS_DIR = os.path.join(pf.PLANES, "Incidents")

CONTROL = {"CONTROL-LUFTHANSA", "CONTROL-RYANAIR"}
FOREIGN = {"SU-BTT", "SU-BND", "SU-BTU", "SU-BTV", "SU-BGM", "T7-ELL"}
KIRK = {"N582MM", "N560TW", "N872RA", "N102DZ", "N888KG", "N40JD"}

TAIL_PAGE = {
    "N102DZ": "/Planes/N102DZ/overview", "N1098L": "/Planes/N1098L/overview",
    "N2100L": "/Planes/N2100L/overview", "N40JD": "/Planes/N40JD/overview",
    "N560TW": "/Planes/N560TW/overview", "N582MM": "/Planes/N582MM/overview",
    "N59906": "/Planes/N59906/overview", "N708JH": "/Planes/N708JH/overview",
    "N872RA": "/Planes/N872RA/overview", "N888KG": "/Planes/N888KG/overview",
    "SU-BGM": "/Planes/SU-BGM/overview", "SU-BND": "/Planes/SU-BND/overview",
    "SU-BTT": "/Planes/SU-BTT/overview", "SU-BTU": "/Planes/SU-BTU/overview",
    "SU-BTV": "/Planes/SU-BTV/overview", "T7-ELL": "/Planes/T7-ELL/overview",
}

TAIL_KIND = {
    "N582MM": "TPUSA-associated Learjet 60",
    "N560TW": "Kirk-side Cessna Citation Excel, Scottsdale base",
    "N872RA": "Kirk-side Hawker 800",
    "N102DZ": "Kirk-side Gulfstream V",
    "N888KG": "Kirk-side Challenger 300",
    "N40JD": "Kirk-side Premier 1",
    "N1098L": "LASAI Aviation II Global 6500, callsign AXEL10",
    "N2100L": "LASAI Aviation II Global 6500, callsign AXEL21",
    "N59906": "Piper Navajo aerial-survey aircraft",
    "N708JH": "US Government / Department of Justice Gulfstream G550",
    "SU-BTT": "Egyptian-registered Dassault Falcon 7X",
    "SU-BND": "Egyptian-registered Gulfstream",
    "SU-BTU": "Egyptian-registered Dassault Falcon 7X",
    "SU-BTV": "Egyptian-registered Dassault Falcon 7X",
    "SU-BGM": "Egyptian-registered Gulfstream IV",
    "T7-ELL": "San Marino-registered aircraft",
    "CONTROL-LUFTHANSA": "European control airliner",
    "CONTROL-RYANAIR": "European control airliner",
}


def airport_url(code):
    return f"/Planes/Airports/{code}"


def airport_link(code, label=None):
    """Link only when the field actually has a page."""
    if not code:
        return "—"
    if code in pf.known_airports():
        return f"[{label or code}]({airport_url(code)})"
    return label or code


def incident_key(tail, date, field):
    return f"{tail}-{date}-{field}"


def incident_url(tail, date, field):
    return f"/Planes/Incidents/{incident_key(tail, date, field)}"


# Every (tail, date, field) that WILL have a contact page this run.  Filled in
# main() before a single page is written, so an airport page can link down into
# a contact page that does not exist on disk yet.  Same discipline as
# pf.ap_link(): a link is emitted only when its target is guaranteed.
INCIDENT_KEYS = set()


def incident_link(tail, date, field, label=None):
    """Link a ground contact ONLY if that contact has a page."""
    k = incident_key(tail, date, field)
    lab = label or date
    return f"[{lab}](/Planes/Incidents/{k})" if k in INCIDENT_KEYS else lab


def tail_link(tail):
    u = TAIL_PAGE.get(tail)
    return f"[{tail}]({u})" if u else tail


def notability(tail):
    """
    0 = foreign-registered, 1 = government / survey / contractor, 2 = Kirk or
    TPUSA fleet.  Used only to ORDER a table, never to characterise an aircraft:
    a Kirk-side jet at a Kirk event is the expected thing and says so on its own
    page.
    """
    if tail in FOREIGN:
        return 0
    if tail in KIRK or tail in CONTROL:
        return 2
    return 1


def when_phrase(off):
    """Prose form of a visit-minus-event day offset.  Negative = before."""
    if off is None:
        return "near in time to"
    if off == 0:
        return "the **same day** as"
    if off == -1:
        return "the **day before**"
    if off == 1:
        return "the **day after**"
    return f"**{abs(off)} days {'before' if off < 0 else 'after'}**"


def miles_cell(v):
    try:
        return f"{float(v):.1f}"
    except (TypeError, ValueError):
        return "—"


def event_adjacent(visits):
    """
    The recovered ground visits at one field that fall on the day of, the day
    before, or the day after a sourced event.

    THE OFFSET IS RECOMPUTED FROM THE TWO DATES AND THE CSV'S OWN OFFSET COLUMN
    IS NEVER READ.  master_proximity.csv stores (event_date - visit_date) and
    geo_ground_foreign.csv stores (sweep_date - event_date); reading one as the
    other turns the day BEFORE the assassination into the day AFTER.

    Each row is one continuous run of on-ground positions and stays its own row.
    Two runs in a day at one field mean the aircraft flew in between — merging
    them would hide a flight.
    """
    out = []
    for v in visits:
        if (v.get("within_50mi") or "").strip() != "yes":
            continue
        off = pf.days_between(v.get("date"), v.get("nearest_event_date"))
        out.append((v, off))
    out.sort(key=lambda x: (
        notability(x[0]["tail"]),
        abs(x[1]) if x[1] is not None else 99,
        float(x[0]["miles_to_event_city"]) if _num(x[0].get("miles_to_event_city")) else 9e9,
        x[0]["date"], x[0]["tail"]))
    return out


def _num(s):
    try:
        float(s)
        return True
    except (TypeError, ValueError):
        return False


def fm(title, sidebar, desc, keywords):
    kw = "\n".join(f"  - {k}" for k in keywords)
    return (
        "---\n"
        f'title: "{title}"\n'
        f'sidebar_label: "{sidebar}"\n'
        f'description: "{desc}"\n'
        "keywords:\n" + kw + "\n"
        'image: "/img/docusaurus-social-card.jpg"\n'
        "---\n\n"
    )


# --------------------------------------------------------------------------
# airport pages
# --------------------------------------------------------------------------

def build_airport_page(code, visits, legs, prox, oa):
    name, where = pf.place(code)
    tails = sorted({v["tail"] for v in visits} | {l["tail"] for l in legs})
    case_tails = [t for t in tails if t not in CONTROL]
    foreign_here = [t for t in tails if t in FOREIGN]

    title = f"{code} — {name}"
    desc = (f"Every recovered ADS-B ground visit and flight leg at {name} "
            f"({code}), {where}, by aircraft tracked in the Charlie Kirk "
            f"investigation.")
    L = [fm(title, code, desc,
            [code, name, where, "ADS-B", "flight records", "Charlie Kirk"])]

    L.append(f"# {code} — {name}\n")

    # ------------------------------------------------------------------
    # THE FINDING FIRST.  What was here, how much of it lands on a sourced
    # event, and the single most striking visit — before any field identity.
    # ------------------------------------------------------------------
    adj = event_adjacent(visits)
    L.append(
        f"**{len(case_tails)} aircraft** this investigation tracks were recorded "
        f"on the ground at **{pf.esc(name)}**, {where}, across **{len(visits)} "
        f"recovered ground visits**. **{len(adj)} of those visits** fall on the "
        f"day of, the day before, or the day after a sourced Charlie Kirk, Erika "
        f"Kirk, or TPUSA event.\n"
    )

    if adj:
        hv, hoff = adj[0]
        band = notability(hv["tail"])
        # Every tail in the same notability band, on the same date, at the same
        # offset — so a field where two foreign jets sat together on the day of
        # an event names both rather than picking one.
        hts = sorted({a[0]["tail"] for a in adj
                      if a[0]["date"] == hv["date"] and a[1] == hoff
                      and notability(a[0]["tail"]) == band})
        # The FURTHEST of the tied rows, not the closest.  Where several tails
        # share the headline, the conservative number is the one that is true of
        # all of them; picking the smallest would quietly overstate proximity.
        hmiles = max((float(a[0]["miles_to_event_city"]) for a in adj
                      if a[0]["tail"] in hts and a[0]["date"] == hv["date"]
                      and _num(a[0].get("miles_to_event_city"))), default=None)
        verb = "were" if len(hts) > 1 else "was"
        links = [tail_link(t) for t in hts]
        if len(links) == 1:
            tls = links[0]
        elif len(links) == 2:
            tls = " and ".join(links)
        else:
            tls = ", ".join(links[:-1]) + " and " + links[-1]
        dist = (f", about **{hmiles:.1f} miles** from the event city"
                if hmiles is not None else "")
        ev_city = f"{hv.get('nearest_event_city','')}, {hv.get('nearest_event_state','')}".strip(", ")
        eu = pf.page_url(hv.get("event_page"))
        ev_txt = f"[{pf.esc(ev_city)}]({eu})" if eu else f"**{pf.esc(ev_city)}**"
        L.append(
            f"{tls} {verb} on the ground here on "
            f"**{pf.pretty_date(hv['date'])}** — {when_phrase(hoff)} a sourced "
            f"**{pf.esc(hv.get('nearest_event_who') or '—')}** event at "
            f"{ev_txt}{dist}.\n"
        )
    else:
        L.append(
            "**No recovered ground visit at this field falls inside the window "
            "of a sourced Charlie Kirk, Erika Kirk, or TPUSA event.** That is a "
            "statement about the sourced event list and the recovered archive "
            "coverage, not a statement that nothing happened here.\n"
        )

    if foreign_here:
        L.append(f"**Foreign-fleet aircraft recorded on the ground here: "
                 f"{', '.join(tail_link(t) for t in foreign_here)}.**\n")

    # the short table: only the event-adjacent visits, most notable first
    if adj:
        L.append("## The visits that land on a sourced event\n")
        L.append(
            "Foreign-registered aircraft first, then government, survey and "
            "contractor aircraft, then the Kirk and TPUSA fleet; within each "
            "band, closest in time to the event first. **Every one of these "
            "rows also appears, in date order, in the full table below** — "
            "nothing here is a second sighting.\n"
        )
        L.append("| Date (UTC) | Aircraft | What it is | When, against the event "
                 "| Sourced event | Miles to event city | Ground window (UTC) | "
                 "Contact page |")
        L.append("|---|---|---|---|---|---:|---|---|")
        for v, off in adj:
            ec = f"{v.get('nearest_event_city','')}, {v.get('nearest_event_state','')}".strip(", ")
            eu = pf.page_url(v.get("event_page"))
            ev = f"[{pf.esc(ec)}]({eu})" if eu else pf.esc(ec) or "—"
            who = pf.esc(v.get("nearest_event_who") or "")
            L.append(
                f"| {v['date']} | {tail_link(v['tail'])} "
                f"| {pf.esc(TAIL_KIND.get(v['tail'], '—'))} "
                f"| {pf.when_label(off)} "
                f"| {ev}{(' — ' + who) if who else ''} "
                f"| {miles_cell(v.get('miles_to_event_city'))} "
                f"| {pf.window(v.get('first_seen_utc'), v.get('last_seen_utc'))} "
                f"| {incident_link(v['tail'], v['date'], code, 'open')} |"
            )
        L.append("")
        L.append(
            "**A row here is an airframe, not a person, and not a purpose.** "
            "Where the same aircraft has two rows on one date, those are two "
            "separate runs of on-ground positions with a flight between them — "
            "not one long wait on the ramp.\n"
        )

    # ground visits
    if visits:
        L.append("## Every recovered ground visit at this field\n")
        L.append("One row is one continuous run of on-ground positions. Times "
                 "are UTC, exactly as the archives recorded them.\n")
        L.append("| Date (UTC) | Aircraft | What it is | Ground window (UTC) | "
                 "km from field | Ground fixes | Near a sourced event? |")
        L.append("|---|---|---|---|---:|---:|---|")
        for v in sorted(visits, key=lambda x: (x["date"], x["tail"])):
            near = "—"
            if v.get("within_50mi") == "yes":
                lab = (f"{v.get('nearest_event_city','')}, "
                       f"{v.get('nearest_event_state','')}").strip(", ")
                near = ("**Yes** — "
                        + incident_link(v["tail"], v["date"], code, lab))
            L.append(
                f"| {v['date']} | {tail_link(v['tail'])} "
                f"| {pf.esc(TAIL_KIND.get(v['tail'], '—'))} "
                f"| {pf.window(v.get('first_seen_utc'), v.get('last_seen_utc'))} "
                f"| {v.get('median_km_from_field','—')} "
                f"| {v.get('ground_points','—')} | {near} |"
            )
        L.append("")

    # legs
    if legs:
        L.append("## Flight legs into and out of this field\n")
        L.append("| Leg date (UTC) | Aircraft | Direction | Other end | "
                 "Left after | Arrived by | How well observed |")
        L.append("|---|---|---|---|---|---|---|")
        for l in sorted(legs, key=lambda x: (x["utc_date"], x["tail"])):
            if l["origin"] == code:
                direction, other = "departed", l["dest"]
            else:
                direction, other = "arrived", l["origin"]
            oname, oplace = pf.place(other)
            un = (l.get("unobserved_days_inside_leg") or "0")
            conf = (l.get("confidence") or "")
            if conf.startswith("direct"):
                cf = "**direct**"
            elif conf.startswith("overnight"):
                cf = "overnight"
            else:
                cf = f"**gap — unobserved {un} day(s)**"
            L.append(
                f"| {l['utc_date']} | {tail_link(l['tail'])} | {direction} "
                f"| {airport_link(other)} — {pf.esc(oplace)} "
                f"| {pf.hhmm(l.get('depart_after_utc','')) or '—'} "
                f"| {pf.hhmm(l.get('arrive_by_utc','')) or '—'} | {cf} |"
            )
        L.append("")

    # event proximity
    if prox:
        L.append("## Sourced Charlie / Erika / TPUSA events near this field\n")
        L.append("| Date (UTC) | Aircraft | Whose event | Event | "
                 "Event city, state | Mi | When | Detail |")
        L.append("|---|---|---|---|---|---:|---|---|")
        for r in sorted(prox, key=lambda x: (x["date"], x["tail"])):
            try:
                mi = f"{float(r['miles']):.1f}"
            except (TypeError, ValueError):
                mi = "—"
            t = r["event_title"] or "—"
            if len(t) > 44:
                t = t[:41].rstrip() + "…"
            u = pf.page_url(r["event_page"])
            ev = f"[{pf.esc(t)}]({u})" if (u and t != "—") else pf.esc(t)
            L.append(
                f"| {r['date']} | {tail_link(r['tail'])} | {pf.esc(r['who'])} "
                f"| {ev} | {pf.esc(r['event_city'])}, {pf.esc(r['event_state'])} "
                f"| {mi} | {pf.when_label(r['offset'])} "
                f"| {incident_link(r['tail'], r['date'], code, 'open')} |"
            )
        L.append("")

    # ------------------------------------------------------------------
    # The field's own identity, below the findings rather than above them.
    # ------------------------------------------------------------------
    L.append("## The field\n")
    L.append(f"**{where}.** This page is the complete recovered record for this "
             f"field: every ground visit and every flight leg by an aircraft "
             f"this investigation tracks.\n")
    L.append("| Field | Value |")
    L.append("|---|---|")
    L.append(f"| ICAO / ident | **{code}** |")
    L.append(f"| Name | {pf.esc(name)} |")
    L.append(f"| Where | {pf.esc(where)} |")
    if oa:
        if oa.get("iata_code"):
            L.append(f"| IATA | {pf.esc(oa['iata_code'])} |")
        if oa.get("type"):
            L.append(f"| Type | {pf.esc(oa['type'].replace('_', ' '))} |")
        if oa.get("elevation_ft"):
            L.append(f"| Elevation | {pf.esc(oa['elevation_ft'])} ft |")
        if oa.get("latitude_deg") and oa.get("longitude_deg"):
            L.append(f"| Coordinates | {oa['latitude_deg']}, {oa['longitude_deg']} |")
        if oa.get("scheduled_service"):
            L.append(f"| Scheduled airline service | "
                     f"{'yes' if oa['scheduled_service'] == 'yes' else 'no'} |")
    L.append(f"| Aircraft tracked here | {len(case_tails)} |")
    L.append(f"| Recovered ground visits | {len(visits)} |")
    L.append(f"| Visits landing on a sourced event | {len(adj)} |")
    L.append(f"| Recovered flight legs | {len(legs)} |")
    L.append("")

    L.append("## What this page cannot tell you\n")
    L.append("* **Presence is not purpose, and it is not occupancy.** No ADS-B "
             "record places any person aboard any aircraft.")
    L.append("* **An absent day is not an absent aircraft.** Volunteer receiver "
             "coverage is uneven, and a jet parked with its transponder off is "
             "invisible. Absence here is a coverage fact.")
    L.append("* **Every count on this page is a count of the aircraft this "
             "investigation tracks**, not of everything that used the field. "
             "Most aircraft at a general-aviation airport are flight-school and "
             "charter traffic, and many carry the FAA's ordinary Limiting "
             "Aircraft Data Displayed privacy flag, which is a routine owner "
             "filing and not a sign of anything.")
    L.append("* **2022 is effectively blank** — no free archive covers it.\n")

    # ------------------------------------------------------------------
    # Drill-down, both directions.  Every link is gated on its target
    # actually existing.
    # ------------------------------------------------------------------
    contacts = sorted({(r["tail"], r["date"]) for r in prox})
    contacts = [c for c in contacts
                if incident_key(c[0], c[1], code) in INCIDENT_KEYS]
    if contacts:
        L.append("## Every recorded ground contact at this field, one page each\n")
        L.append("One page per aircraft-day this field was within 50 miles of a "
                 "sourced event, with the ground window and the archives that "
                 "hold it.\n")
        for tl, dt in contacts:
            L.append(f"* [{tl} at {code} on {dt}](/Planes/Incidents/"
                     f"{incident_key(tl, dt, code)}) — "
                     f"{TAIL_KIND.get(tl, 'aircraft in this investigation')}")
        L.append("")

    L.append("## Related\n")
    for t in case_tails:
        u = TAIL_PAGE.get(t)
        if u:
            L.append(f"* [{t}]({u}) — {TAIL_KIND.get(t, 'aircraft in this investigation')}")
    for url, label in pf.following_location_pages().get(code, []):
        L.append(f"* [The follow log for this location: {label}]({url}) — every "
                 f"claimed pairing at this field, with its counterargument")
    L.append("* [All airports in this investigation](/Planes/Airports/overview)")
    L.append("* [Every interesting date, all aircraft](/Planes/Incidents/overview)")
    L.append("* [Investigating Deleted Flights](/Planes/investigating_deleted_flights)")
    L.append("* [Planes that followed Charlie and Erika](/Planes/following/overview)\n")
    return "\n".join(L)


# --------------------------------------------------------------------------
# incident pages
# --------------------------------------------------------------------------

def build_incident_page(group, siblings, same_field):
    """
    group: every ground segment for one (tail, UTC date, field).

    A tail can be on the ground at one field twice in a day with a flight in
    between — N59906 on 10 September 2025 is exactly that.  Those are ONE page
    with both segments listed, never two pages fighting over one filename.
    """
    r = group[0]
    tail, date, code = r["tail"], r["date"], r["airport"]
    name, where = pf.place(code)
    ecity = f"{r['event_city']}, {r['event_state']}".strip(", ")
    # The offset carried in interesting_dates.json is recomputed from the two
    # dates by build_interesting_dates.py; the source CSVs' own offset columns
    # hold OPPOSITE signs and are never read.  Negative = the aircraft was here
    # BEFORE the event.
    off = r["offset"]
    when = pf.when_label(off)
    wp = when_phrase(off)
    when_txt = re.sub(r"\*\*", "", wp)
    try:
        miles_txt = f"{float(r['miles']):.1f}"
    except (TypeError, ValueError):
        miles_txt = ""

    title = f"{tail} at {code} on {date}"
    desc = (f"{tail} on the ground at {name} ({code}), {where}, on {date} — "
            f"{when_txt} a sourced {r['who']} Kirk / TPUSA event at {ecity}.")
    L = [fm(title, f"{tail} · {date}", desc,
            [tail, code, date, ecity, "ADS-B", "Charlie Kirk"])]

    L.append(f"# {tail} at {code} on {date}\n")
    kind = TAIL_KIND.get(tail, "an aircraft tracked in this investigation")
    dist = f", **{miles_txt} miles** from the event city" if miles_txt else ""
    L.append(
        f"**{tail}** — {kind} — was on the ground at **{name}** "
        f"({airport_link(code)}), {where}, on **{pf.pretty_date(date)}** — "
        f"{wp} a sourced **{pf.esc(r['who'])}** event at **{pf.esc(ecity)}**"
        f"{dist}.\n"
    )

    L.append("## The contact, as the archives recorded it\n")
    L.append("| Field | Value |")
    L.append("|---|---|")
    L.append(f"| Aircraft | {tail_link(tail)} — {pf.esc(TAIL_KIND.get(tail, '—'))} |")
    L.append(f"| UTC date | {date} |")
    if len(group) == 1:
        L.append(f"| Ground window (UTC) | **{r['win']}** |")
    else:
        L.append(f"| Ground segments this day | **{len(group)}** — "
                 f"{', '.join(g['win'] for g in group)} |")
    L.append(f"| Airport | {airport_link(code)} — {pf.esc(name)} |")
    L.append(f"| Where | {pf.esc(where)} |")
    if r.get("km"):
        L.append(f"| Median distance from the field reference point | {r['km']} km |")
    pts = sum(int(g["points"]) for g in group if str(g.get("points", "")).isdigit())
    if pts:
        L.append(f"| On-ground position fixes | {pts} |")
    L.append(f"| Whose event | {pf.esc(r['who'])} |")
    if r.get("event_title"):
        u = pf.page_url(r["event_page"])
        t = pf.esc(r["event_title"])
        L.append(f"| Event | {'[' + t + '](' + u + ')' if u else t} |")
    L.append(f"| Event city | {pf.esc(ecity)} |")
    L.append(f"| Event date | {r['event_date']} |")
    L.append(f"| Timing | {when} |")
    try:
        L.append(f"| Straight-line distance to the event city | {float(r['miles']):.1f} miles |")
    except (TypeError, ValueError):
        pass
    fb = {"both": "**Both recovery routes** — the per-tail pull and the blind "
                  "geographic sweep independently hold this contact",
          "sweep": "The blind geographic sweep, which was not given a tail number",
          "per-tail": "The per-tail archive pull"}
    L.append(f"| Found by | {fb.get(r['found_by'], r['found_by'])} |")
    if r.get("sources"):
        L.append(f"| Archive source | {pf.esc(r['sources'])} |")
    L.append("")

    if len(group) > 1:
        L.append(f"## The {len(group)} ground segments on this day\n")
        L.append(
            "**The aircraft did not sit still between these.** A break between "
            "two runs of on-ground positions at the same field means it took "
            "off and came back — not that it waited on the ramp.\n"
        )
        L.append("| # | Ground window (UTC) | km from field | On-ground fixes |")
        L.append("|---:|---|---:|---:|")
        for i, g in enumerate(sorted(group, key=lambda x: x["win"]), 1):
            L.append(f"| {i} | **{g['win']}** | {g.get('km','—')} "
                     f"| {g.get('points','—')} |")
        L.append("")

    if r["found_by"] == "both":
        L.append(
            "**Two independent routes hold this contact.** One asked *where was "
            "this tail on this day*; the other streamed a whole day of the open "
            "archive and filtered it by geography without being told what to "
            "look for. They agree.\n"
        )

    # The limits section stays in full, word for word — it just sits BELOW the
    # contact and the sibling tables rather than between them.
    limits = ["## What this establishes, and what it does not\n"]
    limits.append(
        "**It establishes that the airframe was there.** The positions are "
        "on-ground reports from a volunteer receiver network, held in a public "
        "archive, and recorded here with the exact window they cover.\n"
    )
    limits.append(
        "**It does not establish purpose, and it does not establish "
        "occupancy.** No ADS-B record anywhere places any person aboard any "
        "aircraft. An aircraft near an event is an airframe near an event.\n"
    )
    if tail in KIRK:
        limits.append(
            "**And for this aircraft, proximity is the expected thing.** This is "
            "a Kirk- or TPUSA-associated airframe. An aircraft that carries the "
            "man showing up where the man is is not surveillance — this row is a "
            "check that the method works, not evidence of anything.\n"
        )
    elif tail in FOREIGN:
        limits.append(
            "**Read it against the denominator.** This aircraft is observed on a "
            "small number of days in total, so one contact is an anecdote rather "
            "than a rate. The full per-aircraft base rates are on "
            "[Investigating Deleted Flights](/Planes/investigating_deleted_flights).\n"
        )

    if siblings:
        L.append(f"## The same aircraft's other event contacts\n")
        L.append("| Date | Airport | Where | Event city | When |")
        L.append("|---|---|---|---|---|")
        for s in siblings:
            n2, w2 = pf.place(s["airport"])
            L.append(
                f"| {incident_link(s['tail'], s['date'], s['airport'])} "
                f"| {airport_link(s['airport'])} | {pf.esc(w2)} "
                f"| {pf.esc(s['event_city'])}, {pf.esc(s['event_state'])} "
                f"| {pf.when_label(s['offset'])} |"
            )
        L.append("")

    if same_field:
        L.append(f"## Other aircraft at {code} around the same event\n")
        L.append("| Date | Aircraft | What it is | When |")
        L.append("|---|---|---|---|")
        for s in same_field:
            L.append(
                f"| {incident_link(s['tail'], s['date'], s['airport'])} "
                f"| {tail_link(s['tail'])} | {pf.esc(TAIL_KIND.get(s['tail'],'—'))} "
                f"| {pf.when_label(s['offset'])} |"
            )
        L.append("")

    L.extend(limits)

    L.append("## Related\n")
    L.append(f"* [{tail} — the aircraft's full record]({TAIL_PAGE.get(tail, '/Planes/overview')})")
    L.append(f"* [{code} — {name} — every recovered visit and leg at this field]"
             f"({airport_url(code)})")
    u = pf.page_url(r["event_page"])
    if u:
        L.append(f"* [The event this is measured against]({u})")
    for url, label in pf.following_location_pages().get(code, []):
        L.append(f"* [The follow log for this location: {label}]({url}) — every "
                 f"claimed pairing at this field, with its counterargument")
    L.append("* [Planes that followed Charlie and Erika](/Planes/following/overview)")
    L.append("* [Every interesting date, all aircraft](/Planes/Incidents/overview)")
    L.append("* [Airports in this investigation](/Planes/Airports/overview)")
    L.append("* [Investigating Deleted Flights](/Planes/investigating_deleted_flights)\n")
    return "\n".join(L)


def write(path, text):
    old = None
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            old = fh.read()
    if old == text:
        return False
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    return True


# --------------------------------------------------------------------------
# indexes and driver
# --------------------------------------------------------------------------

def build_airport_index(rows):
    """rows: list of (code, name, where, n_visits, n_legs, tails)"""
    L = [fm("Airports In This Investigation",
            "Airports",
            "Every airport a tracked aircraft in the Charlie Kirk investigation "
            "was recorded on the ground at, or flew a recovered leg into or out "
            "of, with the visit and leg counts for each.",
            ["airports", "ADS-B", "flight records", "Charlie Kirk", "Provo",
             "Wilmington"])]
    L.append("# Airports In This Investigation\n")
    L.append(f"**{len(rows)} fields.** Every airport at which an aircraft this "
             f"investigation tracks was recorded on the ground, or which a "
             f"recovered flight leg started or ended at.\n")
    L.append("Control-airliner-only fields are not listed: the two European "
             "control airframes exist to test whether an archive is failing, "
             "and their route networks are not part of the case record.\n")
    fr = [r for r in rows if r[5] & FOREIGN]
    if fr:
        L.append("## Fields the foreign fleet was on the ground at\n")
        L.append("| Airport | Name | Where | Foreign-fleet aircraft | Ground visits |")
        L.append("|---|---|---|---|---:|")
        for code, name, where, nv, nl, tails in sorted(
                fr, key=lambda x: (-x[3], x[0])):
            L.append(f"| {airport_link(code)} | {pf.esc(name)} | {pf.esc(where)} "
                     f"| {', '.join(tail_link(t) for t in sorted(tails & FOREIGN))} "
                     f"| {nv} |")
        L.append("")
    L.append("## Every field\n")
    L.append("| Airport | Name | Where | Ground visits | Legs | Aircraft |")
    L.append("|---|---|---|---:|---:|---|")
    for code, name, where, nv, nl, tails in sorted(rows, key=lambda x: (-x[3], x[0])):
        ts = sorted(t for t in tails if t not in CONTROL)
        shown = ", ".join(tail_link(t) for t in ts[:6])
        if len(ts) > 6:
            shown += f", +{len(ts) - 6} more"
        L.append(f"| {airport_link(code)} | {pf.esc(name)} | {pf.esc(where)} "
                 f"| {nv} | {nl} | {shown or '—'} |")
    L.append("")
    L.append("## Related\n")
    L.append("* [Every interesting date, all aircraft](/Planes/Incidents/overview)")
    L.append("* [Investigating Deleted Flights](/Planes/investigating_deleted_flights)")
    L.append("* [Planes that followed Charlie and Erika](/Planes/following/overview)\n")
    return "\n".join(L)


def build_incident_index(rows):
    L = [fm("Every Interesting Date, All Aircraft",
            "Interesting Dates",
            "Every date on which a tracked aircraft was on the ground within 50 "
            "miles of a sourced Charlie Kirk, Erika Kirk, or TPUSA event — one "
            "page per contact, with the ground window, airport, and city.",
            ["interesting dates", "overlaps", "ADS-B", "Charlie Kirk",
             "Erika Kirk", "TPUSA"])]
    L.append("# Every Interesting Date, All Aircraft\n")
    ndays = len({(r["tail"], r["date"], r["airport"]) for r in rows})
    L.append(f"**{len(rows)} ground contacts across {ndays} aircraft-day-field "
             f"pages.** Each row is one aircraft, on the ground, on one UTC day, "
             f"at one airport, within 50 miles of a sourced Charlie Kirk, Erika "
             f"Kirk, or TPUSA event on the event date or either adjacent day. "
             f"Each opens its own page.\n")
    L.append("Where an aircraft was on the ground at one field twice in a day "
             "with a flight in between, that is **one** page carrying both "
             "segments — not two contacts.\n")

    out = [r for r in rows if r["tail"] not in KIRK]
    L.append("## Aircraft outside the Kirk and TPUSA fleet\n")
    L.append("This is the table the following claim is actually about.\n")
    L.append(_idx_table(out) if out else "*(none)*\n")
    L.append("")
    L.append("## The Kirk and TPUSA fleet\n")
    L.append("**An aircraft that carries the man showing up where the man is is "
             "not surveillance.** These rows are the yardstick the table above "
             "is read against.\n")
    L.append(_idx_table([r for r in rows if r["tail"] in KIRK]))
    L.append("")
    L.append("## Related\n")
    L.append("* [Airports in this investigation](/Planes/Airports/overview)")
    L.append("* [Investigating Deleted Flights](/Planes/investigating_deleted_flights)")
    L.append("* [Which planes Charlie flew, which Erika flew](/Planes/Charlie-Erika-Aircraft/overview)\n")
    return "\n".join(L)


def _idx_table(rows):
    L = ["| Date (UTC) | Aircraft | What it is | Airport | City, State | "
         "Whose event | Event city | When |",
         "|---|---|---|---|---|---|---|---|"]
    seen = set()
    uniq = []
    for r in sorted(rows, key=lambda x: (x["date"], x["tail"], x["airport"])):
        k = (r["tail"], r["date"], r["airport"])
        if k in seen:
            continue
        seen.add(k)
        uniq.append(r)
    for r in uniq:
        name, where = pf.place(r["airport"])
        L.append(
            f"| [{r['date']}]({incident_url(r['tail'], r['date'], r['airport'])}) "
            f"| {tail_link(r['tail'])} | {pf.esc(TAIL_KIND.get(r['tail'], '—'))} "
            f"| {airport_link(r['airport'])} | {pf.esc(where)} "
            f"| {pf.esc(r['who'])} "
            f"| {pf.esc(r['event_city'])}, {pf.esc(r['event_state'])} "
            f"| {pf.when_label(r['offset'])} |"
        )
    return "\n".join(L)


def main():
    os.makedirs(AIRPORTS_DIR, exist_ok=True)
    os.makedirs(INCIDENTS_DIR, exist_ok=True)

    visits = defaultdict(list)
    prox = defaultdict(list)
    for r in pf.read_csv("master_proximity.csv"):
        visits[r["airport_code"]].append(r)

    legs_by_ap = defaultdict(list)
    for r in pf.read_csv("flight_legs.csv"):
        for c in (r["origin"], r["dest"]):
            if c:
                legs_by_ap[c].append(r)

    incidents = json.load(
        open(os.path.join(pf.ANALYSIS, "interesting_dates.json"), encoding="utf-8"))
    for r in incidents:
        prox[r["airport"]].append(r)

    # a field earns a page if a NON-control aircraft touched it
    codes = set()
    for c, vs in visits.items():
        if any(v["tail"] not in CONTROL for v in vs):
            codes.add(c)
    for c, ls in legs_by_ap.items():
        if any(l["tail"] not in CONTROL for l in ls):
            codes.add(c)
    # the blind sweep names fields the per-tail lane never saw; a contact page
    # links to its field, so that field must have a page too.
    for r in incidents:
        if r["airport"]:
            codes.add(r["airport"])

    # ONE PAGE PER (tail, UTC date, field).  Several ground segments on the
    # same day at the same field are segments of one contact, not separate
    # contacts, and must not collide on a filename.
    groups = defaultdict(list)
    for r in incidents:
        groups[(r["tail"], r["date"], r["airport"])].append(r)

    # Both link gates are primed BEFORE anything is written, so a page written
    # early in the run can still link to a page written later in the same run.
    # Nothing is added here that this run does not go on to create.
    INCIDENT_KEYS.update(incident_key(*k) for k in groups)
    pf.known_airports().update(codes)

    oa = pf.ourairports()
    written = 0
    index_rows = []
    for c in sorted(codes):
        vs = [v for v in visits.get(c, []) if v["tail"] not in CONTROL]
        ls = [l for l in legs_by_ap.get(c, []) if l["tail"] not in CONTROL]
        name, where = pf.place(c)
        tails = {v["tail"] for v in vs} | {l["tail"] for l in ls}
        index_rows.append((c, name, where, len(vs), len(ls), tails))
        page = build_airport_page(c, vs, ls, prox.get(c, []), oa.get(c))
        written += write(os.path.join(AIRPORTS_DIR, f"{c}.mdx"), page)

    by_tail = defaultdict(list)
    by_field_event = defaultdict(list)
    for k, g in groups.items():
        by_tail[k[0]].append(g[0])
        by_field_event[(k[2], g[0]["event_date"])].append(g[0])

    iw = 0
    for (tl, dt, ap), g in sorted(groups.items()):
        sib = sorted((s for s in by_tail[tl]
                      if not (s["date"] == dt and s["airport"] == ap)),
                     key=lambda x: x["date"])
        same = sorted((s for s in by_field_event[(ap, g[0]["event_date"])]
                       if s["tail"] != tl),
                      key=lambda x: (x["date"], x["tail"]))
        seen = set()
        same = [s for s in same if not (s["tail"] in seen or seen.add(s["tail"]))]
        page = build_incident_page(sorted(g, key=lambda x: x["win"]),
                                   sib[:25], same[:25])
        iw += write(os.path.join(INCIDENTS_DIR, incident_key(tl, dt, ap) + ".mdx"),
                    page)
    print(f"  ({len(incidents)} contacts -> {len(groups)} contact-day pages)")

    write(os.path.join(AIRPORTS_DIR, "overview.mdx"), build_airport_index(index_rows))
    write(os.path.join(INCIDENTS_DIR, "overview.mdx"), build_incident_index(incidents))
    for d, label, pos in ((AIRPORTS_DIR, "Airports", 45),
                          (INCIDENTS_DIR, "Interesting Dates", 46)):
        write(os.path.join(d, "_category_.json"), json.dumps(
            {"label": label, "position": pos,
             "link": {"type": "doc", "id": "Planes/" + os.path.basename(d) + "/overview"}},
            indent=2) + "\n")

    print(f"airport pages: {len(codes)} ({written} written/changed)")
    print(f"incident pages: {len(groups)} ({iw} written/changed)")


if __name__ == "__main__":
    main()
