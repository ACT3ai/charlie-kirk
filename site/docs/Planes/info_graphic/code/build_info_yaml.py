#!/usr/bin/env python3
"""Write one info.yaml per Plane Overlap graphic, straight from the raw traces.

WHY THIS EXISTS. p_create_svgs.md says every number in an info.yaml is traceable
to a file in this repo. Hand-typing a dozen of them from a terminal dump is how a
digit gets transposed and never noticed, so the timestamps are MEASURED here and
written out mechanically. Re-running this after a new archive pull re-measures
everything; nothing is remembered between runs.

WHAT IT MEASURES, per (claimed following tail, claimed date, claimed field):
  * ground windows  runs of positions with the ADS-B on-ground flag set within
                    8 km of the field. A real stay.
  * pass windows    runs of AIRBORNE positions within 15 km of the field. Real,
                    measured, and NOT a landing - emitted with
                    basis: near_field_pass so the generator hatches them.
  * the Kirk side   every Kirk-party / TPUSA-linked tail is queried at the same
                    field on the same date. If none was heard ON THE GROUND, the
                    yaml declares no_aircraft_in_record: true and names what was
                    queried, so a reader can tell an unanswered question from an
                    answered one that came back empty.

Runs shorter than MIN_WINDOW_SEC are dropped rather than drawn: below that the
generator has to widen them to a visible minimum and the width stops being
proportional, which is a bar that lies about its own duration.

  python3 build_info_yaml.py            write every graphic in BUILD
  python3 build_info_yaml.py --check    report, write nothing
"""
import datetime as dt, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PLANES = os.path.normpath(os.path.join(HERE, "..", ".."))
OUT_ROOT = os.path.normpath(os.path.join(
    PLANES, "..", "..", "internals", "static", "img", "infographics", "overlaps"))
WINDOWS = os.environ.get("CK_WINDOWS_JSON", "/tmp/ck_windows.json")

# A near-field PASS shorter than this is two or three position reports, not a
# window, and drawing it forces the generator to widen it past its true width.
MIN_PASS_SEC = 60
# A GROUND CONTACT is never dropped for being short. SU-BTT was on the ground at
# Wilmington for 23 seconds on 20 April 2023 — that is the single genuine ground
# contact in the whole Erika set at that field, and an earlier version of this
# script silently discarded it under a blanket 60-second floor. The generator
# widens a too-short bar to a visible minimum and WARNS that it did; that warning
# is the honest outcome and dropping the evidence is not.
AS_OF = "2026-08-29"

# Kirk-party and TPUSA-linked airframes. planes.csv category "Private / Kirk
# party" is N102DZ alone; the rest are queried too so the absence is a wide one.
KIRK_TAILS = ["N102DZ", "N582MM", "N872RA", "N40JD", "N560TW", "N888KG"]
# ...but only these two may ever BE the lower bar. The lower bar is "the Kirk
# aircraft", and planes.csv puts only N102DZ in "Private / Kirk party", with
# N582MM as the TPUSA-linked airframe. N888KG is "Private / Transponder anomaly"
# and lib/fleet.js says of it, in capitals, SEPARATE CLAIM - DO NOT MERGE;
# N872RA, N40JD and N560TW are "Provo arrival" and "donor-linked" tails. Drawing
# any of those as the Kirk bar would silently answer the question the graphic is
# supposed to ask. They are still QUERIED, and still named in the yaml, so the
# absence on the lower band is a wide and auditable one.
BAR_TAILS = ["N102DZ", "N582MM"]

AIRPORTS = {
    "KILG": dict(name="Wilmington Airport / New Castle Airport", city="Wilmington",
                 state="DE", state_name="Delaware", timezone="America/New_York",
                 town_population=70898, town_population_source="US Census 2020"),
    "KPVU": dict(name="Provo Municipal Airport", city="Provo",
                 state="UT", state_name="Utah", timezone="America/Denver",
                 town_population=115162, town_population_source="US Census 2020"),
    "KOMA": dict(name="Eppley Airfield", city="Omaha",
                 state="NE", state_name="Nebraska", timezone="America/Chicago",
                 town_population=486051, town_population_source="US Census 2020"),
}
PLANE = {
    "SU-BTT": dict(type="Dassault Falcon 7X", operator="Egyptian / foreign VIP"),
    "SU-BND": dict(type="Gulfstream G550", operator="Egyptian / foreign VIP"),
    "N102DZ": dict(type="Gulfstream V", operator="Private / Kirk party"),
}
PERSON_DIR = {"charlie": "Charlie", "erika": "Erika", "both": "Both"}

# (overlap_id, following tail, person). One row is one graphic. Duplicate rows in
# overlaps.csv that describe the SAME (date, field, person, tail) are named in
# `duplicates` rather than given a second directory of their own.
BUILD = [
    ("OWENS-011", "SU-BTT", "erika",   []),
    ("OWENS-013", "SU-BTT", "erika",   []),
    ("OWENS-021", "SU-BTT", "erika",   []),
    ("OWENS-027", "SU-BTT", "erika",   []),
    ("OWENS-025", "SU-BND", "erika",   []),
    ("SITE-004",  "SU-BTT", "charlie", ["OWENS-026"]),
    ("OWENS-035", "SU-BND", "charlie", ["OWENS-065"]),
    ("OWENS-038", "SU-BTT", "erika",   []),
    ("OWENS-039", "SU-BTT", "erika",   []),
    ("OWENS-042", "SU-BND", "erika",   []),
]


def secs(a, b):
    f = lambda s: dt.datetime.fromisoformat(s.replace("Z", "+00:00"))
    return (f(b) - f(a)).total_seconds()


def trim(iso):
    """Whole seconds, Z. The sub-second digits are receiver jitter, not precision."""
    return iso.split(".")[0] + ("Z" if not iso.split(".")[0].endswith("Z") else "")


def windows_for(per_tail, tail):
    out = []
    for r in per_tail[tail]["ground"]:
        out.append(dict(kind="ground_contact", **r))
    for r in per_tail[tail]["near"]:
        if secs(r["first"], r["last"]) >= MIN_PASS_SEC:
            out.append(dict(kind="near_field_pass", **r))
    return sorted(out, key=lambda r: r["first"])


def yaml_for(oid, tail, person, dups, rec):
    code = rec["airport"]
    ap = AIRPORTS[code]
    date = rec["date"]
    # The city and state come from the curated AIRPORTS table, NOT from the
    # overlaps.csv cell: that cell is free text and holds things like
    # "Salt Lake City (event) / Provo (aircraft)", which is not a directory name.
    dirn = "%s_%s_%s_%s_%s" % (date.replace("-", "_"), code, PERSON_DIR[person],
                               ap["state"], ap["city"].lower().replace(" ", "_"))
    wins = windows_for(rec["per_tail"], tail)
    if not wins:
        return None, dirn, "no measured window for %s at %s on %s" % (tail, code, date)

    # THE KIRK SIDE. Ground contact only - an airborne pass by a Kirk aircraft is
    # not an aircraft "at the field" for the purpose of the lower bar.
    kirk_hits = [(t, rec["per_tail"][t]["ground"]) for t in BAR_TAILS
                 if rec["per_tail"].get(t, {}).get("ground")]
    other_hits = [t for t in KIRK_TAILS if t not in BAR_TAILS
                  and rec["per_tail"].get(t, {}).get("ground")]
    queried = [t for t in KIRK_TAILS if rec["per_tail"].get(t, {}).get("queried")]
    not_held = [t for t in KIRK_TAILS if not rec["per_tail"].get(t, {}).get("queried")]

    L = []
    a = L.append
    a("overlap_id: %s" % oid)
    a("date: %s" % date)
    a("person: %s" % person)
    a("dir_name: %s" % dirn)
    a("evidence_basis: adsb_ground_contact")
    a("airport:")
    a("  code: %s" % code)
    a("  name: %s" % ap["name"])
    a("  city: %s" % ap["city"])
    a("  state: %s" % ap["state"])
    a("  state_name: %s" % ap["state_name"])
    a("  timezone: %s" % ap["timezone"])
    a("  town_population: %d" % ap["town_population"])
    a("  town_population_source: %s" % ap["town_population_source"])
    a("following_plane:")
    a("  tail: %s" % tail)
    a("  type: %s" % PLANE[tail]["type"])
    a("  operator: %s" % PLANE[tail]["operator"])
    a("  segments:")
    for w in wins:
        a("    - from: {utc: %s, source_zone: UTC}" % trim(w["first"]))
        a("      to:   {utc: %s, source_zone: UTC}" % trim(w["last"]))
        a("      basis: %s" % w["kind"])
        a("      ground_points: %d" % w["n"])
        a("      min_km: %s" % w["min_km"])
        if w["kind"] == "near_field_pass" and w.get("min_alt_ft") is not None:
            a("      min_alt_ft: %d" % w["min_alt_ft"])
        a("      sources: %s" % "|".join(w["srcs"]))
    a("kirk_plane:")
    if kirk_hits:
        t, runs = kirk_hits[0]
        a("  tail: %s" % t)
        a("  type: %s" % PLANE.get(t, {}).get("type", "type not published"))
        a("  operator: %s" % PLANE.get(t, {}).get("operator", "Private"))
        a("  segments:")
        for r in runs:
            a("    - from: {utc: %s, source_zone: UTC}" % trim(r["first"]))
            a("      to:   {utc: %s, source_zone: UTC}" % trim(r["last"]))
            a("      basis: ground_contact")
            a("      ground_points: %d" % r["n"])
            a("      sources: %s" % "|".join(r["srcs"]))
    else:
        a("  no_aircraft_in_record: true")
        a("  claim: \"%s claimed present at this field on this date · no Kirk-party airframe heard\""
          % {"charlie": "Charlie Kirk", "erika": "Erika Kirk", "both": "Charlie and Erika Kirk"}[person])
        # Name EVERY tail that was asked for, not only the ones an archive
        # happened to hold. "we queried one" and "we queried six and five came
        # back empty" are different facts and the second is the true one.
        a("  queried_tails: %s" % ", ".join(KIRK_TAILS))
    a("times_status: complete")
    a("as_of: %s" % AS_OF)
    a("source_line: \"Source: recovered ADS-B traces, adsb.lol and airplanes.live. "
      "Ground contacts and near-field passes measured point by point. As of %s.\"" % AS_OF)
    a("sources:")
    a("  - site/docs/Planes/following/overlaps.csv")
    a("  - site/docs/Planes/following/airports.csv")
    for s in sorted({s for w in wins for s in w["srcs"]}):
        a("  - site/docs/Planes/%s/data/recovered/%s_%s_%s_trace_full.json" % (tail, tail, date, s))
    for t, runs in kirk_hits:
        for s in sorted({s for r in runs for s in r["srcs"]}):
            a("  - site/docs/Planes/%s/data/recovered/%s_%s_%s_trace_full.json" % (t, t, date, s))
    a("  - site/docs/Planes/info_graphic/code/build_info_yaml.py")
    note = []
    ng = sum(1 for w in wins if w["kind"] == "ground_contact")
    npass = len(wins) - ng
    note.append("%s was heard %s at %s on this date." % (
        tail,
        " and ".join(filter(None, [
            "on the ground %d time%s" % (ng, "" if ng == 1 else "s") if ng else "",
            "airborne within 15 km %d time%s" % (npass, "" if npass == 1 else "s") if npass else ""])),
        code))
    if not kirk_hits:
        note.append("NO Kirk-party or TPUSA-linked airframe was heard on the ground at this field "
                    "on this date. Queried: %s. Held by neither archive for this date: %s. "
                    "The lower band is drawn hollow because the claim on this row is a PERSON IN A "
                    "CITY, and a claimed itinerary is not an aircraft."
                    % (", ".join(queried) or "none", ", ".join(not_held) or "none"))
    if not kirk_hits and other_hits:
        note.append("Other tracked private aircraft WERE on the ground at this field on this date "
                    "(%s), but none of them is a Kirk aircraft - they belong to separate claims in "
                    "this investigation and are not drawn as the Kirk bar." % ", ".join(other_hits))
    if npass:
        note.append("A hatched window is an AIRBORNE pass near the field - an approach, a departure "
                    "climb or an overflight. It is not evidence the aircraft landed.")
    if dups:
        note.append("overlaps.csv holds this same claim more than once: %s. One graphic, not several."
                    % ", ".join([oid] + dups))
    note.append("A trace proves presence, never purpose, and never occupancy. Nothing here places "
                "any person aboard any aircraft.")
    a("notes: >-")
    for line in note:
        a("  " + line)
    return "\n".join(L) + "\n", dirn, None


def write_ledger(recs, built):
    """Every candidate row on the qualifying field-years, drawn or not.

    A SKIP IS A COVERAGE FACT AND IT IS PUBLISHED, not hidden. The three reasons
    are different claims and are never collapsed into one:
      * archive held nothing for the claimed tail on the claimed date
      * archive held the tail, but it was nowhere near the claimed field
      * the row names no following tail at all
    """
    import csv as _csv
    path = os.path.join(OUT_ROOT, "ledger.csv")
    cols = ["overlap_id", "dir_name", "person", "following_tail", "kirk_tail",
            "airport_code", "date", "times_status", "drawable", "built_date", "skip_reason"]
    rows = []
    for oid in sorted(recs, key=lambda k: (recs[k]["date"], k)):
        r = recs[oid]
        hit = built.get(oid)
        tails = [t.strip() for t in r["foreign_tail"].split(";") if t.strip() and t.strip() != "UNKNOWN"]
        if hit:
            rows.append(dict(zip(cols, [oid, hit["dir"], PERSON_DIR[hit["person"]], hit["tail"],
                                        hit["kirk"] or "", r["airport"], r["date"], "complete",
                                        "yes", AS_OF, ""])))
            continue
        if not tails:
            why = "no following tail named on this row"
        else:
            windows = {t: windows_for(r["per_tail"], t) for t in tails if t in r["per_tail"]}
            if any(windows.values()):
                why = "duplicate of another row already built for this date, field and person"
            else:
                held = [t for t in tails if r["per_tail"].get(t, {}).get("queried")]
                if held:
                    near = [(t, r["per_tail"][t]["closest"]["km"]) for t in held
                            if r["per_tail"][t].get("closest")]
                    why = ("archives hold this tail for this date but it was not at the claimed field ("
                           + ", ".join("%s closest %s km" % (t, k) for t, k in near) + ")") if near else                           "archives hold this tail for this date but no usable position"
                else:
                    why = "neither free archive holds a trace for %s on this date - a coverage fact, not an absence" % "/".join(tails)
        rows.append(dict(zip(cols, [oid, "", "", ";".join(tails), "", r["airport"], r["date"],
                                    "none", "no", "", why])))
    with open(path, "w", newline="") as fh:
        w = _csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    drawn = sum(1 for r in rows if r["drawable"] == "yes")
    print("\nledger.csv: %d candidate rows, %d drawable, %d skipped" % (len(rows), drawn, len(rows) - drawn))


def main():
    check = "--check" in sys.argv
    recs = json.load(open(WINDOWS))
    made = skipped = 0
    built = {}
    for oid, tail, person, dups in BUILD:
        rec = recs.get(oid)
        if rec is None:
            print("MISSING  %s not in %s" % (oid, WINDOWS)); skipped += 1; continue
        body, dirn, why = yaml_for(oid, tail, person, dups, rec)
        if body is None:
            print("SKIP     %-11s %s" % (oid, why)); skipped += 1; continue
        d = os.path.join(OUT_ROOT, dirn)
        if not check:
            os.makedirs(d, exist_ok=True)
            open(os.path.join(d, "info.yaml"), "w").write(body)
        hollow = "no_aircraft_in_record: true" in body
        kirk = "" if hollow else next((t for t in BAR_TAILS
                                       if rec["per_tail"].get(t, {}).get("ground")), "")
        built[oid] = dict(dir=dirn, person=person, tail=tail, kirk=kirk)
        for dup in dups:
            built.setdefault(dup, dict(dir=dirn, person=person, tail=tail, kirk=kirk))
        print("%-8s %-11s %-42s %s" % ("OK" if check else "WROTE", oid, dirn,
                                       "HOLLOW Kirk band" if hollow else "two real bars"))
        made += 1
    # The two 10 September 2025 Provo graphics are written by hand rather than by
    # this script - they are the only rows with a real Kirk-party aircraft bar -
    # so they are named here so the ledger is the whole run and not part of it.
    for oid, dirn, person, tail in (("EXTRA-006", "2025_09_10_KPVU_Charlie_UT_provo", "charlie", "SU-BND"),
                                    ("OWENS-041", "2025_09_10_KPVU_Both_UT_provo", "both", "SU-BTT"),
                                    ("SITE-006", "2025_09_10_KPVU_Charlie_UT_provo", "charlie", "SU-BND")):
        built.setdefault(oid, dict(dir=dirn, person=person, tail=tail, kirk="N102DZ"))
    print("\n%d written, %d skipped." % (made, skipped))
    if not check:
        write_ledger(recs, built)


if __name__ == "__main__":
    main()
