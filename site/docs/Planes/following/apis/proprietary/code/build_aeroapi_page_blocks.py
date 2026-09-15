#!/usr/bin/env python3
"""Put FlightAware's answer on the overlap pages, and a short plain answer on the Erika pages.

Two generated blocks, each between its own markers, each safe to re-run:

  CK_AEROAPI_VERDICT   every overlap page whose row was queried on AeroAPI. Goes directly
                       after the ADS-B verdict block (CK_ADSB_VERDICT), so a reader sees the
                       volunteer-receiver answer and the commercial flight record side by side.
  CK_SHORT_ANSWER      every row whose subject is Erika Kirk (61 pages). Goes directly under
                       the page title: the answer in five plain questions, then FlightAware's
                       timeline for the window. Bryan, 14 Sep 2026: answer first, then the
                       timeline, then the existing detail.

READS ONLY PUBLIC FILES, so anyone can re-run it: following/overlaps.csv (the aeroapi_*
columns from build_aeroapi_columns.py), following/airports.csv, the restated FlightAware
data in ../data/flightaware_restated/, and the overlap graphics' info.yaml. No API key, no
private data.

Nothing here places any person aboard any aircraft, and no block says so.

  python3 build_aeroapi_page_blocks.py            write
  python3 build_aeroapi_page_blocks.py --check    report, write nothing
"""
import csv, datetime as dt, os, re, sys
from zoneinfo import ZoneInfo

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
CHECKOUT = os.path.normpath(os.path.join(HERE, *[".."] * 7))
FOLLOWING = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
PLANES = os.path.dirname(FOLLOWING)
GRAPHICS = os.path.join(CHECKOUT, "site", "internals", "static", "img", "infographics", "overlaps")
GITHUB = "https://github.com/ACT3ai/charlie-kirk/blob/main/"

# pagefacts hard-codes ~/BGit/Bryan_git/charlie-kirk. Point it at THIS checkout so
# airport names and airport-page links resolve wherever the repo is cloned.
sys.path.insert(0, os.path.join(FOLLOWING, "apis", "public_open_source", "code", "lib"))
import pagefacts as pf  # noqa: E402
pf.ROOT, pf.PLANES, pf.FOLLOWING = CHECKOUT, PLANES, FOLLOWING
pf.ANALYSIS = os.path.join(FOLLOWING, "apis/public_open_source/data/analysis")

V_START, V_END = "{/* CK_AEROAPI_VERDICT:START */}", "{/* CK_AEROAPI_VERDICT:END */}"
A_START, A_END = "{/* CK_SHORT_ANSWER:START */}", "{/* CK_SHORT_ANSWER:END */}"
ADSB_END = "{/* CK_ADSB_VERDICT:END */}"

LABEL = {
    "AT_FIELD": "the aircraft was at the claimed airport",
    "SAME_METRO_OTHER_FIELD": "the aircraft was at another airport in the same area",
    "FLEW_ELSEWHERE": "the aircraft flew, but not to the claimed airport",
    "NO_FLIGHT_RECORD": "no flight recorded for the aircraft in the window",
}
MEANING = {
    "AT_FIELD": "FlightAware records this aircraft landing at, or taking off from, the claimed airport inside "
                "the window. **That confirms the aircraft half of the claim, and only that half.**",
    "SAME_METRO_OTHER_FIELD": "FlightAware records this aircraft at another airport in the same metro area inside "
                              "the window, and not at the claimed airport.",
    "FLEW_ELSEWHERE": "FlightAware records flights for this aircraft inside the window, and none of them touches "
                      "the claimed airport. That points away from the claim. FlightAware can miss a leg, so on "
                      "its own it is not proof.",
    "NO_FLIGHT_RECORD": "FlightAware holds no flight for this aircraft in the window. Parked, not tracked, and "
                        "transponder off all look the same from here, so **this is not a finding either way.**",
}


def esc(s):
    return pf.esc(str(s if s is not None else ""))


def utc(s):
    return dt.datetime.fromisoformat(s.replace("Z", "+00:00"))


def when(s, tz):
    """'Sun 28 Apr 2024, 1:42 pm EDT (17:42 UTC)' - the airport's own clock first, UTC after."""
    t = utc(s)
    if not tz:
        return t.strftime("%a %-d %b %Y, %H:%M UTC")
    lt = t.astimezone(ZoneInfo(tz))
    return "%s, %s %s (%s UTC)" % (lt.strftime("%a %-d %b %Y"), lt.strftime("%-I:%M %p").lower(),
                                   lt.strftime("%Z"), t.strftime("%H:%M"))


def best_time(event):
    for basis in ("actual", "estimated", "scheduled"):
        if isinstance(event, dict) and event.get(basis):
            return event[basis]["utc"], basis
    return None, None


def place_label(ap):
    if not ap:
        return "an unrecorded place"
    if ap.get("position_only_point"):
        p = ap["position_only_point"]
        near = ("a point near %s" % ap["city"]) if ap.get("city") else "a point"
        return "%s (%.2f, %.2f)" % (near, p["lat"], p["lon"])
    code = ap.get("icao") or ap.get("code_as_given") or ap.get("iata") or ap.get("faa_lid") or "?"
    return ("%s %s" % (code, ap.get("city") or ap.get("name") or "")).strip()


def codes(ap):
    return {c for c in ((ap or {}).get("icao"), (ap or {}).get("code_as_given")) if c}


def metro_fields():
    out = {}
    for a in csv.DictReader(open(os.path.join(FOLLOWING, "airports.csv"), newline="", encoding="utf-8")):
        if (a.get("metro_area") or "").strip():
            out[a["airport_code"].strip().upper()] = a["metro_area"].strip()
    return out


def load_flights(paths, tail):
    seen, out = set(), []
    for p in paths:
        if f"/{tail}/" not in p:
            continue
        for f in (yaml.safe_load(open(os.path.join(CHECKOUT, p))) or {}).get("flights") or []:
            if f["flightaware_id"] not in seen:
                seen.add(f["flightaware_id"])
                out.append(f)
    return sorted(out, key=lambda f: best_time(f.get("takeoff"))[0] or best_time(f.get("landing"))[0] or "")


def tails_of(row):
    return [t.strip().upper() for t in re.split(r"[;,]| or ", row.get("foreign_tail") or "")
            if t.strip() and t.strip().upper() != "UNKNOWN"]


def verdict_for(row, tail):
    v = (row.get("aeroapi_verdict") or "").strip()
    if ": " not in v:
        return v
    for part in v.split("; "):
        t, _, val = part.partition(": ")
        if t == tail:
            return val
    return ""


def in_window(f, ws, we):
    for ev in ("takeoff", "landing"):
        t = best_time(f.get(ev))[0]
        if t and ws <= utc(t) < we:
            return True
    return False


def field_story(row, tail, flights, ws, we, targets):
    """Landings at / takeoffs from the target fields inside the window, and the stay between them."""
    events = []
    for f in flights:
        lt, _ = best_time(f.get("landing"))
        if lt and codes(f.get("to")) & targets and ws <= utc(lt) < we:
            events.append(("landed at", lt, f, f.get("to"), f.get("from")))
        tt, _ = best_time(f.get("takeoff"))
        if tt and codes(f.get("from")) & targets and ws <= utc(tt) < we:
            events.append(("took off from", tt, f, f.get("from"), f.get("to")))
    events.sort(key=lambda e: e[1])
    stay = None
    for i, (verb, t, f, here, _) in enumerate(events):
        if verb == "landed at":
            later = [e for e in flights if best_time(e.get("takeoff"))[0] and utc(best_time(e.get("takeoff"))[0]) > utc(t)]
            if later and codes(later[0].get("from")) & codes(here):
                stay = (t, best_time(later[0].get("takeoff"))[0], here)
            break
    return events, stay


def hours(a, b):
    h = (utc(b) - utc(a)).total_seconds() / 3600
    if h < 1:
        return "about %d minutes" % round(h * 60)
    if h < 48:
        n = round(h)
        return "about %d hour%s" % (n, "" if n == 1 else "s")
    return "about %.1f days" % (h / 24)


def adsb_sentence(row):
    v = (row.get("adsb_verified_verdict") or "").strip()
    km = (row.get("adsb_closest_approach_km") or "").strip()
    ground = (row.get("adsb_ground_position") or "").strip().lower() == "yes"
    try:
        f = float(km)
        kmt = ("%s km" % format(round(f), ",")) if f >= 10 else "%.1f km" % f
    except ValueError:
        kmt = "an unrecorded distance"
    return {
        "AT_CLAIMED_AIRPORT": "Free ADS-B receivers also heard it there, %s." % ("on the ground" if ground else "in the air %s from the field" % kmt),
        "SAME_METRO_WRONG_FIELD": "Free ADS-B receivers heard it %s from the field." % kmt,
        "ELSEWHERE": "Free ADS-B receivers last heard it %s away that day." % kmt,
        "NOT_HEARD": "The free ADS-B archives did not hear it in the days checked.",
        "NO_ARCHIVE_COVERAGE": "No free ADS-B archive covers this date.",
    }.get(v, "")


def graphic_for(oid):
    path = os.path.join(GRAPHICS, "ledger.csv")
    if not os.path.exists(path):
        return None
    for r in csv.DictReader(open(path, newline="", encoding="utf-8")):
        if r["overlap_id"] == oid and r["dir_name"]:
            info = os.path.join(GRAPHICS, r["dir_name"], "info.yaml")
            return yaml.safe_load(open(info)) if os.path.exists(info) else None
    return None


def short_answer(row):
    oid, date, field = row["overlap_id"], (row.get("date") or "").strip(), (row.get("airport_code") or "").strip().upper()
    name, where = pf.place(field) if field else ("", "")
    city = (name or field) if not where or where == "—" else where.split(",")[0]
    tails = tails_of(row)
    rows = []
    timeline = []

    try:
        day = dt.date.fromisoformat(date)
    except ValueError:
        day = None
    if not day or not tails or (row.get("aeroapi_verdict") or "") == "NOT_QUERIED":
        why = "the row names no date" if not day else "the row names no aircraft" if not tails else "this row has not been checked against FlightAware"
        rows.append(("Was the aircraft there?", "**Cannot be checked:** %s, so there is nothing to look up." % why))
    else:
        ws = dt.datetime.combine(day - dt.timedelta(days=3), dt.time(), dt.timezone.utc)
        we = dt.datetime.combine(day + dt.timedelta(days=4), dt.time(), dt.timezone.utc)
        files = [p for p in (row.get("aeroapi_restated_files") or "").split(";") if p]
        metro = metro_fields()
        for tail in tails:
            v = verdict_for(row, tail)
            flights = load_flights(files, tail)
            win = [f for f in flights if in_window(f, ws, we)]
            targets = {field}
            if v == "SAME_METRO_OTHER_FIELD" and field in metro:
                targets = {c for c, m in metro.items() if m == metro[field]}
            events, stay = field_story(row, tail, flights, ws, we, targets)
            q = "Was %s at %s (%s) around %s?" % (tail, city, field, day.strftime("%-d %B %Y"))
            said = "; ".join("%s %s on %s, %s %s" % (
                verb, place_label(here), when(t, (here or {}).get("timezone")),
                "from" if verb == "landed at" else "to", place_label(other)) for verb, t, f, here, other in events)
            adsb = adsb_sentence(row)
            if v == "AT_FIELD":
                a = "**Yes.** FlightAware records it: %s. %s" % (said, adsb)
                if (row.get("adsb_verified_verdict") or "") == "ELSEWHERE":
                    a += " That is why this row is no longer counted as refuted."
                if (row.get("audit_verdict") or "").strip().lower() == "inaccurate":
                    a += " The tracking-site audit scored this row inaccurate; FlightAware's record says otherwise."
            elif v == "SAME_METRO_OTHER_FIELD":
                a = "**Nearby, not at %s.** FlightAware records it at another airport in the same area: %s. %s" % (field, said, adsb)
            elif v == "FLEW_ELSEWHERE":
                legs = "; ".join("%s to %s" % (place_label(f.get("from")), place_label(f.get("to"))) for f in win)
                a = "**No record of it there.** FlightAware holds %d flight%s for it in the window (%s), and none touches %s. %s" % (
                    len(win), "" if len(win) == 1 else "s", legs, field, adsb)
            elif (row.get("adsb_verified_verdict") or "") == "AT_CLAIMED_AIRPORT":
                a = "**Yes, by free ADS-B only.** %s FlightAware holds no flight for it in the window." % adsb
            else:
                a = "**Unknown.** FlightAware holds no flight for it in the window. %s That is not proof it stayed away." % adsb
            rows.append((q, a.strip()))
            if stay:
                rows.append(("How long was %s there?" % tail, "**%s.** Landed %s; next took off %s." % (
                    hours(stay[0], stay[1]).capitalize(), when(stay[0], stay[2].get("timezone")), when(stay[1], stay[2].get("timezone")))))
            timeline += [(tail, f) for f in win]

    rows.append(("Was Erika Kirk there?", "**No dated source says so.** The claim rests on the overlap sheet's location "
                 "cell. Her itinerary has never been published and her [flight logs are reported erased](/Planes/Erika-Flight-Logs-Erased)."))
    g = graphic_for(oid)
    kp = (g or {}).get("kirk_plane") or {}
    if kp.get("no_aircraft_in_record"):
        rows.append(("Was a Kirk-party aircraft there?", "**None heard.** No Kirk-party aircraft was heard on the ground at "
                     "%s that day. Checked: %s." % (field, kp.get("queried_tails", ""))))
    elif kp.get("tail"):
        rows.append(("Was a Kirk-party aircraft there?", "**%s was heard on the ground there that day.** See the timeline graphic below." % kp["tail"]))
    else:
        rows.append(("Was a Kirk-party aircraft there?", "**Not shown by any record.** The Kirk side of this row is a claimed "
                     "location for a person, not an aircraft. FlightAware hides the tails most often linked to the "
                     "Kirks (N102DZ and N582MM are on its block list)."))
    rows.append(("Does this show anyone was being followed?", "**No.** A flight record places an aircraft, never a person, "
                 "and never a purpose. The counterargument is further down this page."))

    L = [A_START, "", ":::note[The short answer]", "", "| Question | Answer |", "|---|---|"]
    L += ["| **%s** | %s |" % (esc(q), esc(a)) for q, a in rows]
    L += ["", ":::", ""]
    if timeline:
        L += ["### FlightAware timeline, %s to %s" % ((day - dt.timedelta(days=3)).strftime("%-d %b"), (day + dt.timedelta(days=3)).strftime("%-d %b %Y")),
              "", "| # | Aircraft | From | Took off | To | Landed | FlightAware says |", "|---|---|---|---|---|---|---|"]
        for i, (tail, f) in enumerate(timeline, 1):
            tt, tb = best_time(f.get("takeoff"))
            lt, lb = best_time(f.get("landing"))
            note = [f.get("outcome", "")]
            if "position_only" in (f.get("flags") or []):
                note.append("seen by position only")
            if "cancelled" in (f.get("flags") or []):
                note.append("cancelled")
            if tt and lt and tt == lt:
                note.append("no landing observed")
            fmt = lambda t, b, ap: ("%s%s" % (when(t, (ap or {}).get("timezone")), "" if b == "actual" else " (%s)" % b)) if t else "not recorded"
            L.append("| %d | %s | %s | %s | %s | %s | %s |" % (
                i, tail, esc(place_label(f.get("from"))), esc(fmt(tt, tb, f.get("from"))),
                esc(place_label(f.get("to"))), esc(fmt(lt, lb, f.get("to"))), esc(", ".join(n for n in note if n))))
        L += ["", "*Every flight FlightAware holds for the aircraft from three days before the claimed date to three "
              "days after it, the overlap window this site uses. Local time is the time at that airport. Restated "
              "from FlightAware's data; the files are listed in the FlightAware section below.*", ""]
    L.append(A_END)
    return "\n".join(L)


def verdict_block(row):
    tails = tails_of(row)
    files = [p for p in (row.get("aeroapi_restated_files") or "").split(";") if p]
    L = [V_START, "", "## What FlightAware's flight record says", "",
         "The section above is what free, volunteer ADS-B receivers heard. This section is what **FlightAware**, "
         "a commercial flight-tracking service, recorded for the same aircraft over the same days. It is a "
         "different source with different gaps, checked on 14 September 2026.", ""]
    for tail in tails:
        v = verdict_for(row, tail)
        L += ["### FlightAware, %s: %s" % (tail, LABEL.get(v, v)), "", "| Field | Value |", "|---|---|",
              "| Claim ID | **%s** |" % esc(row["overlap_id"]),
              "| Aircraft | [%s](/Planes/%s/overview) |" % (tail, tail) if os.path.isdir(os.path.join(PLANES, tail)) else "| Aircraft | %s |" % tail,
              "| Days checked | %s |" % esc(row.get("aeroapi_window")),
              "| **FlightAware verdict** | **%s** |" % esc(v)]
        multi = ": " in (row.get("aeroapi_verdict") or "")
        pick = lambda col: next((p.partition(": ")[2] for p in (row.get(col) or "").split("; ") if p.startswith(tail + ": ")), "") if multi else (row.get(col) or "")
        if pick("aeroapi_at_field"):
            L.append("| At the claimed airport | %s |" % esc(pick("aeroapi_at_field")))
        L.append("| Flights FlightAware holds in those days | %s |" % esc(pick("aeroapi_flights_in_window")))
        L.append("| Before and after | %s |" % esc(pick("aeroapi_context")))
        L += ["", "**What that verdict means.** %s" % MEANING.get(v, ""), ""]
    L += ["**Against the other checks on this row.** %s" % esc(row.get("aeroapi_vs_adsb")), ""]
    if files:
        L += ["**The data.** FlightAware does not allow its responses to be republished, so the raw responses are held "
              "privately. What is published is every fact in them, restated in our own layout and checked field by field "
              "against the raw response by `check_restated.py`:", ""]
        L += ["* [`%s`](%s%s)" % (os.path.basename(p), GITHUB, p) for p in files]
        L.append("")
    L += ["**This is about the aircraft only.** No flight record places any person aboard any aircraft, and FlightAware's "
          "does not either.", "", V_END]
    return "\n".join(L)


def splice_after(text, block, start, end, after_marker=None, after_h1=False):
    if start in text and end in text:
        return text.split(start)[0] + block + text.split(end, 1)[1]
    if after_marker and after_marker in text:
        i = text.index(after_marker) + len(after_marker)
        return text[:i] + "\n\n" + block + "\n" + text[i:]
    if after_h1:
        m = re.search(r"^# .*$", text, flags=re.M)
        if m:
            return text[:m.end()] + "\n\n" + block + "\n" + text[m.end():]
    return None


def main():
    check = "--check" in sys.argv
    rows = list(csv.DictReader(open(os.path.join(FOLLOWING, "overlaps.csv"), newline="", encoding="utf-8")))
    if "aeroapi_verdict" not in rows[0]:
        sys.exit("overlaps.csv has no aeroapi_* columns - run build_aeroapi_columns.py first")
    changed, skipped = [], []
    for row in rows:
        page = os.path.join(CHECKOUT, (row.get("overlap_page") or "").strip())
        if not row.get("overlap_page") or not os.path.exists(page):
            continue
        text = open(page, encoding="utf-8").read()
        new = text
        if (row.get("aeroapi_verdict") or "NOT_QUERIED") != "NOT_QUERIED":
            out = splice_after(new, verdict_block(row), V_START, V_END, after_marker=ADSB_END)
            if out is None:
                skipped.append((row["overlap_id"], "no CK_ADSB_VERDICT block to sit after"))
            else:
                new = out
        if (row.get("subject") or "").strip() == "Erika":
            out = splice_after(new, short_answer(row), A_START, A_END, after_h1=True)
            if out is None:
                skipped.append((row["overlap_id"], "no page title to sit under"))
            else:
                new = out
        if new != text:
            changed.append(os.path.relpath(page, CHECKOUT))
            if not check:
                open(page, "w", encoding="utf-8").write(new)
    print("%s %d pages" % ("would change" if check else "changed", len(changed)))
    for oid, why in skipped:
        print("  SKIP %s: %s" % (oid, why))
    if "--list" in sys.argv:
        print("\n".join(changed))


if __name__ == "__main__":
    main()
