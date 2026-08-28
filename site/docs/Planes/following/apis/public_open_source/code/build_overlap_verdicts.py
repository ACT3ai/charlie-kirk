#!/usr/bin/env python3
"""
build_overlap_verdicts.py

Puts the ADS-B VERDICT on each of the 85 per-claim overlap pages under
/Planes/following/overlap/.

Those pages describe what somebody CLAIMED.  overlaps.csv has, for every one of
them, what the recovered public ADS-B actually says — and not one of the pages
was publishing it.  This closes that gap.

The seven verdicts, and what each is allowed to mean:

  AT_CLAIMED_AIRPORT      a recovered trace puts the airframe at that field on
                          that date.  With adsb_ground_position=yes it was
                          wheels-down; without, it is an airborne fix near the
                          field - an arrival, a departure, or a low pass.  That
                          distinction is on every row and must never be dropped.
  ELSEWHERE               a recovered trace puts it somewhere else.  The only
                          verdict that refutes a row.
  SAME_METRO_WRONG_FIELD  right metro, wrong airport.
  NOT_HEARD               the archives were asked and hold nothing.  THIS IS NOT
                          A REFUTATION.  The free archives hear a Provo-parked
                          jet on 9 of 114 undisputed days.
  NO_ARCHIVE_COVERAGE     no free archive holds that date for anything.
  NO_DATE_CLAIMED /
  NO_TAIL_CLAIMED         the claim is not specific enough to test.
"""

import os
import sys
from collections import Counter

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
import pagefacts as pf  # noqa: E402

START = "{/* CK_ADSB_VERDICT:START */}"
END = "{/* CK_ADSB_VERDICT:END */}"
ANCHOR = "{/* CK_PAGE_FOOTER_START */}"

ROOT = os.path.expanduser("~/BGit/Bryan_git/charlie-kirk")

VERDICT = {
    "AT_CLAIMED_AIRPORT": (
        "Aircraft was at the claimed field",
        "A recovered trace puts this airframe at the claimed airport on the "
        "claimed date. **This corroborates the aircraft half of the claim, and "
        "only the aircraft half.**"),
    "ELSEWHERE": (
        "Aircraft was somewhere else",
        "A recovered trace puts this airframe somewhere other than the claimed "
        "location on the claimed date. **This is the only verdict that refutes "
        "a row**, and it is applied sparingly."),
    "SAME_METRO_WRONG_FIELD": (
        "Right metro, wrong airport",
        "The airframe was in the claimed metropolitan area but at a different "
        "field from the one claimed."),
    "NOT_HEARD": (
        "Archives were asked and hold nothing",
        "**This is not a refutation and must never be quoted as one.** The free "
        "archives hear a Provo-parked jet on 9 of the 114 days it undisputedly "
        "sat there. A `NOT_HEARD` is a statement about volunteer receiver "
        "coverage, not about whether the aircraft was present."),
    "NO_ARCHIVE_COVERAGE": (
        "No free archive covers this date",
        "Neither free archive holds this date for any airframe we probed — "
        "including the control aircraft. This is an **archive limit**, not "
        "suppression, and it says nothing either way about the claim."),
    "NO_DATE_CLAIMED": (
        "The claim names no testable date",
        "Without a date there is nothing to query an archive for. Untestable as "
        "published."),
    "NO_TAIL_CLAIMED": (
        "The claim names no tail number",
        "Without a registration there is nothing to query an archive for. "
        "Untestable as published."),
}


def build(r):
    v = (r.get("adsb_verified_verdict") or "").strip()
    label, meaning = VERDICT.get(
        v, ("Not yet tested against recovered ADS-B",
            "No verdict has been recorded for this row."))
    ground = (r.get("adsb_ground_position") or "").strip().lower() == "yes"
    km = (r.get("adsb_closest_approach_km") or "").strip()
    note = (r.get("adsb_verified_note") or "").strip()

    L = [START, ""]
    L.append("## What the recovered flight data says about this claim")
    L.append("")
    L.append(
        "This page records what somebody **claimed**. This section records what "
        "the recovered public ADS-B actually shows, tested independently of the "
        "claim."
    )
    L.append("")
    L.append(f"### Verdict: {label}")
    L.append("")
    L.append("| Field | Value |")
    L.append("|---|---|")
    L.append(f"| Claim ID | **{pf.esc(r.get('overlap_id',''))}** |")
    L.append(f"| Claimed date | {pf.esc(r.get('date') or '*none claimed*')} |")
    # "UNKNOWN" is a real value in this column, not a missing one, and it must
    # never become /Planes/UNKNOWN/overview.
    tail = (r.get("foreign_tail") or "").strip()
    if not tail or tail.upper() == "UNKNOWN":
        L.append("| Claimed aircraft | *no tail number claimed* |")
    elif os.path.isdir(os.path.join(pf.PLANES, tail)):
        L.append(f"| Claimed aircraft | [{pf.esc(tail)}](/Planes/{tail}/overview) |")
    else:
        L.append(f"| Claimed aircraft | {pf.esc(tail)} "
                 f"*(no page on this site for this tail)* |")
    ap = (r.get("airport_code") or "").strip()
    if ap:
        L.append(f"| Claimed airport | {pf.ap_link(ap, bold=True)} "
                 f"{pf.esc(pf.place(ap)[1])} |")
    L.append(f"| Claimed location | {pf.esc(r.get('city',''))}, "
             f"{pf.esc(r.get('state',''))} |")
    L.append(f"| Claimed subject | {pf.esc(r.get('subject','') or '—')} |")
    L.append(f"| **ADS-B verdict** | **{pf.esc(v or 'UNTESTED')}** |")
    if km:
        L.append(f"| Closest recovered approach | {pf.esc(km)} km |")
    if v == "AT_CLAIMED_AIRPORT":
        L.append(f"| Wheels on the ground? | "
                 f"{'**Yes** — on-ground positions recorded' if ground else '**No** — airborne fix near the field only (an arrival, a departure, or a low pass)'} |")
    ad = (r.get("audit_verdict") or "").strip()
    if ad:
        L.append(f"| Independent audit's verdict | {pf.esc(ad)} |")
    L.append("")
    L.append(f"**What that verdict means.** {meaning}")
    L.append("")
    if note:
        L.append(f"**On this specific row:** {pf.esc(note)}")
        L.append("")

    if v == "AT_CLAIMED_AIRPORT" and not ground:
        L.append(
            "**Read the wheels-down row carefully.** An airborne fix near a "
            "field is not the same as an aircraft parked at it. Fifteen of the "
            "rows scored `AT_CLAIMED_AIRPORT` across this investigation are "
            "airborne fixes rather than ground presences, and that distinction "
            "travels with the number everywhere it is quoted."
        )
        L.append("")

    ep = (r.get("erika_present") or "").strip()
    if ep and ep != "no":
        L.append(
            "**And the person half of this claim is not confirmed by anything "
            "here.** No ADS-B record anywhere places any person aboard any "
            "aircraft. Across all 85 claimed overlaps the `erika_present` column "
            "is `claimed` on 70 rows and `not_claimed` on 15 — **it is never "
            "`yes` on any row.** Erika Kirk's flight logs are reported erased and "
            "no backup anywhere produces her itinerary. See "
            "[Erika Flight Logs Erased](/Planes/Erika-Flight-Logs-Erased)."
        )
        L.append("")

    L.append(
        "*Verdicts come from `overlaps.csv`, derived from the recovered traces. "
        "See [Investigating Deleted Flights]"
        "(/Planes/investigating_deleted_flights) §4.13 for how the 85 claims "
        "break down as a whole, and "
        "[the overlap window definition](/Planes/following/Overlap_Window_Definition) "
        "for what counts as an overlap at all.*"
    )
    L.append("")
    L.append(END)
    return "\n".join(L)


def main():
    rows = pf.read_csv("overlaps.csv", base=pf.FOLLOWING)
    changed = missing = 0
    counts = Counter()
    for r in rows:
        page = (r.get("overlap_page") or "").strip()
        if not page:
            continue
        full = os.path.join(ROOT, page)
        if not os.path.exists(full):
            missing += 1
            continue
        counts[(r.get("adsb_verified_verdict") or "UNTESTED")] += 1
        if pf.splice(full, build(r), START, END, ANCHOR):
            changed += 1
    print(f"overlap claims: {len(rows)}   pages changed: {changed}   "
          f"missing pages: {missing}")
    for k, n in counts.most_common():
        print(f"  {k:24s} {n}")


if __name__ == "__main__":
    main()
