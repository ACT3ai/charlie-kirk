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

SCOPE, CHANGED 2026-08-29. This used to carry a hand-written BUILD list of ten
overlap_ids. It now walks EVERY row of overlaps.csv and builds a graphic for
every row that has a measured window, so "100% of the overlap rows" is a fact
about the code rather than about who remembered to add a line. Which rows those
are is decided by the DATA, in pick_build(), and every row that does not make it
is written into ledger.csv with the reason kept separate from the other reasons.

The windows themselves are measured by measure_windows.py, which writes
CK_WINDOWS_JSON. Run that first; this script never measures and never guesses.

  python3 measure_windows.py            measure every row of overlaps.csv
  python3 build_info_yaml.py            write every graphic that has a window
  python3 build_info_yaml.py --check    report, write nothing
"""
import csv, datetime as dt, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(
    HERE, "..", "..", "following", "apis", "public_open_source", "code", "lib")))
from geo import airport_by_code  # noqa: E402
PLANES = os.path.normpath(os.path.join(HERE, "..", ".."))
OUT_ROOT = os.path.normpath(os.path.join(
    PLANES, "..", "..", "internals", "static", "img", "infographics", "overlaps"))
WINDOWS = os.environ.get("CK_WINDOWS_JSON", "/tmp/ck_windows.json")

# A near-field PASS shorter than this is two or three position reports, not a
# window, and drawing it forces the generator to widen it past its true width.
MIN_PASS_SEC = 60
# A near-field window whose lowest altitude is more than this above the field is
# an aircraft crossing the circle, not one visiting the field. See field_ceiling.
NEAR_FIELD_AGL = 6000
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

# Field identity. The three fields the first run covered carry a CURATED entry,
# because a hand-checked name and a sourced US Census population are better than
# anything derivable. Every other field is resolved from the OurAirports
# database the flight pipeline already downloaded, and its population comes back
# `unknown` — the generator then omits the population line rather than printing
# a figure nobody sourced. NEVER fill one of those in from memory.
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

# The IANA zone for every other field this investigation touches, stated rather
# than inferred. geo.timezone_at() falls back to a per-STATE table when
# timezonefinder is not installed, and several states straddle two zones — an
# approximate zone would silently shift every clock time on the picture by an
# hour. Each line below is a claim about one named field, not about a state.
FIELD_TZ = {
    "KICT": "America/Chicago",     "KLNK": "America/Chicago",
    "KSTL": "America/Chicago",     "KSUS": "America/Chicago",
    "KCPS": "America/Chicago",     "KTOP": "America/Chicago",
    "KORD": "America/Chicago",     "KJFK": "America/New_York",
    "KBOS": "America/New_York",    "KBGR": "America/New_York",
    "KATL": "America/New_York",    "KSMF": "America/Los_Angeles",
    "CYYR": "America/Goose_Bay",
}
STATE_NAME = {
    "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas",
    "CA": "California", "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware",
    "DC": "District of Columbia", "FL": "Florida", "GA": "Georgia", "HI": "Hawaii",
    "ID": "Idaho", "IL": "Illinois", "IN": "Indiana", "IA": "Iowa", "KS": "Kansas",
    "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine", "MD": "Maryland",
    "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi",
    "MO": "Missouri", "MT": "Montana", "NE": "Nebraska", "NV": "Nevada",
    "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico", "NY": "New York",
    "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma",
    "OR": "Oregon", "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina",
    "SD": "South Dakota", "TN": "Tennessee", "TX": "Texas", "UT": "Utah",
    "VT": "Vermont", "VA": "Virginia", "WA": "Washington", "WV": "West Virginia",
    "WI": "Wisconsin", "WY": "Wyoming",
    "NL": "Newfoundland and Labrador",
}


def airport_facts(code):
    """Curated entry if there is one, otherwise resolved from OurAirports.

    Returns None when the field cannot be resolved at all — the caller then
    skips the row and says so, rather than drawing a picture headed UNKNOWN.
    """
    if code in AIRPORTS:
        return AIRPORTS[code]
    ap = airport_by_code(code)
    if not ap:
        return None
    st = (ap.get("iso_region") or "").split("-")[-1].upper()
    tz = FIELD_TZ.get(code)
    if not tz:                       # never guess a zone; the clock times depend on it
        return None
    city = (ap.get("municipality") or "").split("/")[0].strip()
    return dict(name=ap["name"], city=city, state=st,
                state_name=STATE_NAME.get(st, st), timezone=tz,
                town_population="unknown",
                town_population_source="no sourced figure held for this place")


# Aircraft type and operator. The three that carry the argument are curated; any
# other tail is looked up in planes.csv rather than typed from memory.
PLANE = {
    "SU-BTT": dict(type="Dassault Falcon 7X", operator="Egyptian / foreign VIP"),
    "SU-BND": dict(type="Gulfstream G550", operator="Egyptian / foreign VIP"),
    "N102DZ": dict(type="Gulfstream V", operator="Private / Kirk party"),
}
PLANES_CSV = os.path.normpath(os.path.join(PLANES, "..", "..", "..", "planes.csv"))


def plane_facts(tail):
    if tail in PLANE:
        return PLANE[tail]
    try:
        with open(PLANES_CSV, newline="", encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                if (r.get("tail") or r.get("plane_key") or "").strip().upper() == tail:
                    return dict(type=(r.get("aircraft_type") or "type not published").strip(),
                                operator=(r.get("operator") or r.get("category") or "operator not published").strip())
    except OSError:
        pass
    return dict(type="type not published", operator="operator not published")


PERSON_DIR = {"charlie": "Charlie", "erika": "Erika", "both": "Both"}

# WHICH ROWS BECOME GRAPHICS is decided by pick_build() out of the measured
# windows, not by a hand-written list. See the SCOPE note in the docstring.
#
# One graphic is ONE following aircraft, at ONE instance of overlap, against ONE
# Kirk side. Duplicate rows in overlaps.csv that describe the SAME
# (date, field, person, tail) are named in `duplicates` rather than given a
# second directory of their own.


def person_for(rec):
    """Charlie / Erika / Both, or None when this row is not a Kirk overlap.

    A TPUSA event with neither Kirk claimed present is not a Charlie-or-Erika
    overlap and this template does not cover it. That is a scope fact and it is
    recorded, not silently dropped.
    """
    subj = (rec.get("subject") or "").strip().lower()
    if subj in ("charlie", "erika", "both"):
        return subj
    ch = (rec.get("charlie") or "").strip().lower() in ("yes", "claimed", "true")
    er = (rec.get("erika") or "").strip().lower() in ("yes", "claimed", "true")
    if ch and er:
        return "both"
    if ch:
        return "charlie"
    if er:
        return "erika"
    return None


def row_tails(rec):
    """Every following tail a row names. "SU-BTT or SU-BND" names two."""
    raw = (rec.get("foreign_tail") or "").strip()
    if not raw or raw.upper() == "UNKNOWN":
        return []
    return [t.strip().upper() for t in re.split(r"[;,]| or ", raw) if t.strip()]


def pick_build(recs):
    """(overlap_id, tail, person, duplicates) for every row with a real window.

    A row earns a graphic when, and only when, the archives hold a MEASURED
    window for the tail it names at the field it names on the date it names.
    Nothing here widens a date into a time and nothing here promotes a row that
    came back empty; those rows go to the ledger with their reason.

    WHEN ONE ROW NAMES TWO TAILS and both were heard, the graphic goes to the
    one with real GROUND contact — a stay at the field is the claim being made,
    and an airborne pass is not the same event. The other tail is named in the
    notes so the choice is visible rather than quiet.
    """
    chosen, dups = {}, {}
    for oid in sorted(recs, key=lambda k: (recs[k].get("date") or "", k)):
        rec = recs[oid]
        if rec.get("unmeasurable"):
            continue
        person = person_for(rec)
        if person is None:
            continue
        best = None
        for tail in row_tails(rec):
            wins = windows_for(rec, tail)
            if not wins:
                continue
            rank = (sum(1 for w in wins if w["kind"] == "ground_contact"),
                    sum(w["n"] for w in wins))
            if best is None or rank > best[0]:
                best = (rank, tail, wins)
        if best is None:
            continue
        tail = best[1]
        key = (rec["date"], rec["airport"], person)
        if key in chosen:
            # Same date, same field, same Kirk side: one graphic, not several.
            dups.setdefault(chosen[key][0], []).append(oid)
            continue
        chosen[key] = (oid, tail, person)
    return [(oid, tail, person, dups.get(oid, []))
            for oid, tail, person in chosen.values()]


def secs(a, b):
    f = lambda s: dt.datetime.fromisoformat(s.replace("Z", "+00:00"))
    return (f(b) - f(a)).total_seconds()


def trim(iso):
    """Whole seconds, Z. The sub-second digits are receiver jitter, not precision."""
    return iso.split(".")[0] + ("Z" if not iso.split(".")[0].endswith("Z") else "")


def field_ceiling(code):
    """Barometric altitude above which a window near the field is a TRANSIT.

    measure_windows.py deliberately applies no altitude limit — it measures, it
    does not judge. The judgement is here, and it matters: within 15 km of a
    field is a circle roughly 30 km across, and an airliner at cruise crosses
    one of those every few minutes. Drawing that as a hatched "near-field pass"
    beside a claim that an aircraft was following somebody would manufacture a
    bar out of an aircraft that never came near the ground. NEAR_FIELD_AGL above
    the field's own elevation is an approach, a departure climb or a low
    overflight — something that happened AT the field.
    """
    ap = airport_by_code(code)
    elev = 0.0
    try:
        elev = float(ap.get("elevation_ft") or 0)
    except (AttributeError, TypeError, ValueError):
        elev = 0.0
    return elev + NEAR_FIELD_AGL


def windows_for(rec, tail):
    per_tail = rec["per_tail"]
    if tail not in per_tail:
        return []
    out = []
    for r in per_tail[tail]["ground"]:
        out.append(dict(kind="ground_contact", **r))
    ceiling = field_ceiling(rec["airport"])
    for r in per_tail[tail]["near"]:
        if secs(r["first"], r["last"]) < MIN_PASS_SEC:
            continue
        alt = r.get("min_alt_ft")
        if alt is None or alt > ceiling:
            continue                    # a transit over the circle, not a pass at the field
        out.append(dict(kind="near_field_pass", **r))
    return sorted(out, key=lambda r: r["first"])


def yaml_for(oid, tail, person, dups, rec):
    code = rec["airport"]
    ap = airport_facts(code)
    if ap is None:
        return None, code, "field %s could not be resolved to a name and an IANA time zone" % code
    date = rec["date"]
    # The city and state come from the curated AIRPORTS table, NOT from the
    # overlaps.csv cell: that cell is free text and holds things like
    # "Salt Lake City (event) / Provo (aircraft)", which is not a directory name.
    dirn = "%s_%s_%s_%s_%s" % (date.replace("-", "_"), code, PERSON_DIR[person],
                               ap["state"], ap["city"].lower().replace(" ", "_"))
    wins = windows_for(rec, tail)
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
    a("  town_population: %s" % ap["town_population"])
    a("  town_population_source: %s" % ap["town_population_source"])
    a("following_plane:")
    a("  tail: %s" % tail)
    a("  type: %s" % plane_facts(tail)["type"])
    a("  operator: %s" % plane_facts(tail)["operator"])
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
        a("  type: %s" % plane_facts(t)["type"])
        a("  operator: %s" % plane_facts(t)["operator"])
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
        # THE DISTANCE IS THE NUMBER THAT MATTERS on a pass and the bar label
        # only carries the altitude, so it is stated here. Within 15 km is a
        # circle 30 km across, and "0.2 km at 4,325 ft" and "7.2 km at 2,100 ft"
        # are not the same event even though both are drawn the same way.
        note.append("A hatched window is an AIRBORNE pass near the field - an approach, a departure "
                    "climb or an overflight. It is not evidence the aircraft landed. Closest "
                    "approach and lowest altitude heard, per pass: "
                    + "; ".join("%s km at %s ft" % (w["min_km"], w.get("min_alt_ft"))
                                for w in wins if w["kind"] == "near_field_pass") + ".")
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

    A SKIP IS A COVERAGE FACT AND IT IS PUBLISHED, not hidden. The reasons are
    different claims and are never collapsed into one:
      * the row was never measurable — no date, or a metro area and not a field
      * the row names no following tail at all
      * archive held nothing for the claimed tail on the claimed date
      * archive held the tail, but it was nowhere near the claimed field
      * archive held it near the field, but only airborne above the pass ceiling
      * a duplicate of a row already built for that date, field and Kirk side
    """
    import csv as _csv
    path = os.path.join(OUT_ROOT, "ledger.csv")
    cols = ["overlap_id", "dir_name", "person", "following_tail", "kirk_tail",
            "airport_code", "date", "times_status", "drawable", "built_date", "skip_reason"]
    rows = []
    for oid in sorted(recs, key=lambda k: (recs[k].get("date") or "", k)):
        r = recs[oid]
        hit = built.get(oid)
        tails = [t.strip() for t in r["foreign_tail"].split(";") if t.strip() and t.strip() != "UNKNOWN"]
        if hit:
            rows.append(dict(zip(cols, [oid, hit["dir"], PERSON_DIR[hit["person"]], hit["tail"],
                                        hit["kirk"] or "", r["airport"], r["date"], "complete",
                                        "yes", AS_OF, ""])))
            continue
        if r.get("unmeasurable"):
            # NOT an archive result. A row with no date, or naming a metro area
            # rather than a field, was never a measurable question in the first
            # place, and calling it "the archive holds nothing" would turn a
            # bookkeeping gap into a negative finding about an aircraft.
            why = r["unmeasurable"]
        elif not tails:
            why = "no following tail named on this row"
        else:
            windows = {t: windows_for(r, t) for t in tails if t in r["per_tail"]}
            if person_for(r) is None:
                # OUT OF SCOPE, NOT A DUPLICATE AND NOT AN EMPTY ARCHIVE. A TPUSA
                # event with neither Kirk claimed present is not a Charlie-or-
                # Erika overlap, so this template has nothing to draw for it even
                # when the archives held the aircraft. Two of these rows DO have
                # a measured near-field window, and calling them duplicates would
                # bury a real measurement under a bookkeeping word.
                why = ("TPUSA event with neither Kirk claimed present - outside this template, "
                       "which draws one following aircraft against one Kirk side"
                       + (" (a measured window for %s DOES exist at this field on this date)"
                          % "/".join(t for t, w in windows.items() if w) if any(windows.values()) else ""))
            elif any(windows.values()):
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
    build = pick_build(recs)
    print("%d overlap rows measured, %d of them become a graphic.\n" % (
        sum(1 for r in recs.values() if not r.get("unmeasurable")), len(build)))
    for oid, tail, person, dups in sorted(build, key=lambda b: (recs[b[0]]["date"], b[0])):
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
    print("\n%d written, %d skipped." % (made, skipped))
    if not check:
        write_ledger(recs, built)


if __name__ == "__main__":
    main()
