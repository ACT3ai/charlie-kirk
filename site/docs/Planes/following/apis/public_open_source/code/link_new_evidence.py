#!/usr/bin/env python3
"""
link_new_evidence.py

Adds inbound links, on every customer-visible page under /Planes/, to the
per-airport and per-contact evidence pages.

It does NOT link everything to everything.  For each page it reads the page's
own text and links only what that page ACTUALLY TALKS ABOUT:

  * a tail number the page mentions        -> that aircraft's event contacts
  * an ICAO code the page mentions         -> that airport's page
  * a date the page mentions that is also
    a recorded contact                     -> that contact's page

A page that mentions nothing linkable gets the two hub links and nothing else,
rather than a padded list.  The block is written between markers so re-running
is idempotent.
"""

import json
import os
import re
import sys
from collections import defaultdict

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
import pagefacts as pf  # noqa: E402

START = "{/* CK_NEW_EVIDENCE_LINKS:START */}"
END = "{/* CK_NEW_EVIDENCE_LINKS:END */}"

SKIP_DIRS = {"Airports", "Incidents"}
SKIP_PARTS = ("/data/", "/code/", "/node_modules/", "/build/")

MAX_AIRPORTS = 500
MAX_CONTACTS = 500

def _datekey(d):
    """YYYY-MM-DD -> sortable int; unparseable dates rank oldest."""
    try:
        return int(d.replace("-", ""))
    except Exception:
        return 0


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
FOREIGN = {"SU-BTT", "SU-BND", "SU-BTU", "SU-BTV", "SU-BGM", "T7-ELL"}


def visible_pages():
    out = []
    for root, dirs, files in os.walk(pf.PLANES):
        # apis/ holds real customer-visible knowledge pages; only its data/
        # and code/ subtrees are machinery.
        dirs[:] = [d for d in dirs
                   if d not in SKIP_DIRS and d not in ("data", "code",
                                                       "node_modules", "backup",
                                                       "backups", "__pycache__")]
        rel = root[len(pf.PLANES):]
        if any(p in rel + "/" for p in SKIP_PARTS):
            continue
        for f in files:
            if not f.endswith((".md", ".mdx")):
                continue
            if f.startswith("_") or f == "CLAUDE.md":
                continue
            out.append(os.path.join(root, f))
    return sorted(out)


def build_block(tails, airports, contacts, airport_meta, counts,
                window=None, untracked=None, contacts_total=None):
    L = [START, ""]
    L.append("## Flight-record pages for what is on this page")
    L.append("")
    if window:
        L.append(
            f"This investigation keeps one page per airport and one page per "
            f"recorded ground contact, built directly from the recovered ADS-B "
            f"traces. These are the ones that fall inside **{window[0]} to "
            f"{window[1]}**, the range this page covers."
        )
    else:
        L.append(
            "This investigation keeps one page per airport and one page per "
            "recorded ground contact, built directly from the recovered ADS-B "
            "traces. These are the ones this page touches."
        )
    L.append("")
    if untracked:
        L.append(
            f"**There is no recovered ADS-B record for {untracked} on this "
            f"site.** This airframe is not in the tracked fleet that the "
            f"archive pulls were run against, so nothing below is a statement "
            f"about where it was — only about the aircraft that were queried. "
            f"Absence here is a scope fact, not a finding."
        )
        L.append("")
    if window and not contacts:
        L.append(
            f"**No tracked aircraft was on the ground near a sourced event in "
            f"this window.** Across {window[0]} to {window[1]} the recovered "
            f"traces record no contact. That is a coverage statement as much as "
            f"anything — see the limits on the linked pages."
        )
        L.append("")

    # one row per (tail, date, field): several ground segments on one day at
    # one field are one contact page, so they must not render as repeat rows.
    seen = set()
    uniq = []
    for c in contacts:
        k = (c["tail"], c["date"], c["airport"])
        if k in seen:
            continue
        seen.add(k)
        uniq.append(c)
    contacts = uniq

    if contacts:
        if contacts_total and contacts_total > len(contacts):
            L.append(
                f"**Ground contacts near a sourced Charlie / Erika / TPUSA "
                f"event** — the **{len(contacts)}** most significant of "
                f"**{contacts_total}** this page touches, foreign-fleet and "
                f"same-day first, then most recent. The full set is on "
                f"[the contacts index](/Planes/Incidents/overview) and on each "
                f"aircraft's own page."
            )
        else:
            L.append("**Ground contacts near a sourced Charlie / Erika / TPUSA event:**")
        L.append("")
        L.append("| Date (UTC) | Aircraft | Airport | City, State | Whose event | When |")
        L.append("|---|---|---|---|---|---|")
        for c in contacts:
            name, where = pf.place(c["airport"])
            L.append(
                f"| [{c['date']}](/Planes/Incidents/{c['tail']}-{c['date']}-{c['airport']}) "
                f"| [{c['tail']}]({TAIL_PAGE.get(c['tail'], '/Planes/overview')}) "
                f"| [{c['airport']}](/Planes/Airports/{c['airport']}) "
                f"| {pf.esc(where)} | {pf.esc(c['who'])} "
                f"| {pf.when_label(c['offset'])} |"
            )
        L.append("")

    if airports:
        L.append("**Airports named on this page:**")
        L.append("")
        for code in airports:
            name, where = pf.place(code)
            meta = airport_meta.get(code, {})
            bits = []
            if meta.get("visits"):
                bits.append(f"{meta['visits']} recorded ground visit"
                            f"{'s' if meta['visits'] != 1 else ''}")
            if meta.get("tails"):
                bits.append(f"{len(meta['tails'])} tracked aircraft")
            tail = f" — {', '.join(bits)}" if bits else ""
            L.append(f"* [{code} — {pf.esc(name)}](/Planes/Airports/{code}), "
                     f"{pf.esc(where)}{tail}")
        L.append("")

    if tails:
        L.append("**Aircraft named on this page:**")
        L.append("")
        for t in tails:
            L.append(f"* [{t}]({TAIL_PAGE[t]}) — full recovered movement record, "
                     f"every airport and every leg")
        L.append("")

    L.append("**The two indexes:**")
    L.append("")
    L.append(f"* [Every airport in this investigation](/Planes/Airports/overview) "
             f"— {counts['airports']} fields, each with its complete recovered "
             f"ground-visit and flight-leg record")
    L.append(f"* [Every interesting date, all aircraft](/Planes/Incidents/overview) "
             f"— {counts['contacts']} ground contacts near a sourced event, "
             f"across {counts['contact_pages']} pages")
    L.append("* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) "
             "— how the data was recovered, how much of it we hold, and where it "
             "is still missing")
    L.append("")
    L.append(END)
    return "\n".join(L)


def main():
    incidents = json.load(
        open(os.path.join(pf.ANALYSIS, "interesting_dates.json"), encoding="utf-8"))
    by_tail = defaultdict(list)
    for r in incidents:
        by_tail[r["tail"]].append(r)

    real_airports = {f[:-4] for f in os.listdir(os.path.join(pf.PLANES, "Airports"))
                     if f.endswith(".mdx") and f != "overview.mdx"}
    airport_meta = defaultdict(lambda: {"visits": 0, "tails": set()})
    for r in pf.read_csv("master_proximity.csv"):
        if r["airport_code"] in real_airports:
            airport_meta[r["airport_code"]]["visits"] += 1
            airport_meta[r["airport_code"]]["tails"].add(r["tail"])

    contact_keys = {(r["tail"], r["date"], r["airport"]): r for r in incidents}
    counts = {
        "airports": len(real_airports),
        "contacts": len(incidents),
        "contact_pages": len({(r["tail"], r["date"], r["airport"])
                              for r in incidents}),
    }

    tail_re = re.compile(r"\b(N\d{2,5}[A-Z]{0,2}|SU-B[A-Z]{2}|T7-ELL)\b")
    icao_re = re.compile(r"\b([KC][A-Z0-9]{3}|[EHLOMRSVWY][A-Z]{3})\b")
    date_re = re.compile(r"\b(20\d{2}-\d{2}-\d{2})\b")

    changed = skipped = 0
    for path in visible_pages():
        rel = os.path.relpath(path, pf.PLANES)
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        body = text.split(START)[0] + (text.split(END, 1)[1] if END in text else "")

        found_t = sorted({t for t in tail_re.findall(body) if t in TAIL_PAGE})
        found_a = sorted({c for c in icao_re.findall(body) if c in real_airports})
        found_d = set(date_re.findall(body))

        contacts = []
        for (tl, dt, ap), r in contact_keys.items():
            if dt in found_d and (tl in found_t or ap in found_a):
                contacts.append(r)
        # a page about one aircraft gets that aircraft's contacts even with no dates
        if not contacts and len(found_t) == 1:
            contacts = list(by_tail.get(found_t[0], []))
        contacts.sort(key=lambda x: (x["date"], x["tail"]))

        # a page that declares a date range (the weekly research pages) gets
        # every contact inside that range
        window = None
        m = re.search(r"Date range:\s*(20\d{2}-\d{2}-\d{2})\s*to\s*"
                      r"(20\d{2}-\d{2}-\d{2})", body)
        if m:
            window = (m.group(1), m.group(2))
            contacts = sorted(
                (r for r in incidents if window[0] <= r["date"] <= window[1]),
                key=lambda x: (x["date"], x["tail"]))

        # an aircraft page for an airframe we hold no traces for says so
        untracked = None
        parts = rel.split(os.sep)
        if len(parts) == 2 and parts[1] in ("overview.mdx", "overview.md"):
            d = parts[0]
            if re.fullmatch(r"(N\d{2,5}[A-Z]{0,2}|SU-B[A-Z]{2}|T7-ELL|SAM-.*|"
                            r"99-\d{4}.*|Pilatus-PC-12)", d) and d not in TAIL_PAGE:
                untracked = d

        # rank airports: foreign-fleet fields first, then by visit count
        def arank(c):
            m = airport_meta.get(c, {})
            return (0 if (m.get("tails", set()) & FOREIGN) else 1, -m.get("visits", 0), c)
        found_a = sorted(found_a, key=arank)[:MAX_AIRPORTS]

        if not (found_t or found_a or contacts or untracked):
            skipped += 1

        # Rank BEFORE truncating.  A plain date sort keeps the OLDEST rows, so
        # as a page gained tail mentions the cap silently discarded the newest
        # ones -- which is how the 10 September 2025 Provo contacts fell off
        # this block.  Significance survives the cap; the table is re-sorted
        # into date order afterwards so the reader still gets a timeline.
        def crank(c):
            return (0 if c.get("tail") in FOREIGN else 1,      # foreign fleet first
                    abs(int(c.get("offset") or 0)),            # same day, then +/-1
                    -_datekey(c.get("date") or ""))            # most recent first
        shown = sorted(contacts, key=crank)[:MAX_CONTACTS]
        shown.sort(key=lambda x: (x["date"], x["tail"]))

        block = build_block(found_t, found_a, shown,
                            airport_meta, counts, window, untracked,
                            contacts_total=len(contacts))
        anchor = "{/* CK_PAGE_FOOTER_START */}"
        if pf.splice(path, block, START, END, anchor):
            changed += 1

    print(f"pages scanned: {len(visible_pages())}")
    print(f"pages changed: {changed}   (with nothing specific to link: {skipped})")


if __name__ == "__main__":
    main()
