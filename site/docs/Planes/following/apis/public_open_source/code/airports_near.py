#!/usr/bin/env python3
"""Build one `.yaml` beside every speaking-event page: the airports within 40
miles of the field Charlie Kirk probably landed at, and every tracked aircraft
that was at any of them inside a +/- 2 day window.

    python3 airports_near.py                     # every speaking page
    python3 airports_near.py --only 20250910_orem
    python3 airports_near.py --radius 40 --window 2
    python3 airports_near.py --rebuild-traces    # re-read the ADS-B traces first
    python3 airports_near.py --report            # print the cross-event summary

WHAT THIS PRODUCES, IN ONE SENTENCE
-----------------------------------
For each sourced Charlie Kirk / Erika Kirk / TPUSA speaking appearance, a
machine-readable record of: where the event was, which airport a private jet
would most plausibly have used, every other field within 40 miles that a
private jet could also have used, and whether any Egyptian `SU-` registered
aircraft or other tracked tail shows up at any of them within two days.

WHAT IT DOES NOT PRODUCE
------------------------
An overlap claim. Three separate honesty rules are enforced in the output and
must never be edited out of it:

  * THE ARRIVAL AIRPORT IS AN INFERENCE. No Kirk-side flight record has been
    published for the overwhelming majority of these events. "Probably landed
    at" means "this is the nearest jet-capable field to the venue city", and
    the YAML says so in `selection_basis` on every row.

  * THE ARRIVAL AND DEPARTURE TIMES ARE ESTIMATES unless an actual ADS-B
    ground contact by a Kirk-side tail is on disk, in which case the observed
    times appear in a SEPARATE block and are labelled as observed.

  * AN EMPTY RESULT IS NOT A FINDING EITHER WAY. `coverage` records how many
    of the window's aircraft-days this repo actually holds a trace for. Most
    are zero. Zero traces means the volunteer receiver networks were not asked
    or did not hear, NOT that no aircraft was there.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))

import geo            # noqa: E402
import traces         # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
FOLLOWING = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
SPEAKING = os.path.join(FOLLOWING, "speaking")
REPO = os.path.normpath(os.path.join(FOLLOWING, "..", "..", "..", ".."))
CACHE = os.path.join(HERE, "..", "data", "recovery", "trace_visit_index.json")

EVENTS_CSV = os.path.join(FOLLOWING, "tpusa_events.csv")
FLIGHTS_CSV = os.path.join(FOLLOWING, "flights.csv")
OVERLAPS_CSV = os.path.join(FOLLOWING, "overlaps.csv")
PLANES_CSV = os.path.join(FOLLOWING, "planes.csv")

DEFAULT_RADIUS_MI = 40
DEFAULT_WINDOW_DAYS = 2

# Hours before an event a private jet would plausibly land, and after it would
# plausibly leave. PLANNING ASSUMPTIONS, not observations - they exist so the
# estimate is reproducible, and every YAML states them next to the number.
ARRIVE_BEFORE_H = 3
DEPART_AFTER_H = 2
EVENT_DEFAULT_LOCAL = "19:00"      # used only when the event time is unpublished
EVENT_DEFAULT_NOTE = "no event time published; 19:00 local assumed for arithmetic only"


# --------------------------------------------------------------------------
# small helpers
# --------------------------------------------------------------------------

def read_csv(path):
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def parse_dates(raw):
    """'2025-09-10' / '2022-06-02 to 2022-06-04' / '2023-05 (month)'."""
    raw = (raw or "").strip()
    days = re.findall(r"\d{4}-\d{2}-\d{2}", raw)
    if days:
        return days[0], days[-1], "DAY"
    m = re.match(r"(\d{4})-(\d{2})", raw)
    if m:
        y, mo = int(m.group(1)), int(m.group(2))
        last = (dt.date(y + (mo == 12), (mo % 12) + 1, 1) - dt.timedelta(days=1))
        return f"{y:04d}-{mo:02d}-01", last.isoformat(), "MONTH_ONLY"
    return None, None, "UNPARSEABLE"


def d(s):
    return dt.date.fromisoformat(s)


def parse_local_time(raw):
    """First HH:MM in the free-text time cell, or a coarse part-of-day word."""
    raw = (raw or "").strip()
    if not raw:
        return None, "no_time_published"
    m = re.search(r"\b([0-2]?\d):([0-5]\d)\b", raw)
    if m:
        return f"{int(m.group(1)):02d}:{m.group(2)}", "parsed_from_event_time_cell"
    low = raw.lower()
    for word, hhmm in (("morning", "10:00"), ("noon", "12:00"),
                       ("afternoon", "14:00"), ("evening", "19:00")):
        if word in low:
            return hhmm, f"coarse_word_'{word}'_mapped_to_{hhmm}"
    return None, "time_cell_present_but_unparseable"


def to_utc(day, hhmm, tzname):
    if not (day and hhmm and tzname):
        return None
    try:
        from zoneinfo import ZoneInfo
        naive = dt.datetime.strptime(f"{day} {hhmm}", "%Y-%m-%d %H:%M")
        return naive.replace(tzinfo=ZoneInfo(tzname)).astimezone(
            dt.timezone.utc).isoformat().replace("+00:00", "Z")
    except Exception:
        return None


def utc_to_local(iso_utc, tzname):
    if not (iso_utc and tzname):
        return None
    try:
        from zoneinfo import ZoneInfo
        t = dt.datetime.fromisoformat(iso_utc.replace("Z", "+00:00"))
        return t.astimezone(ZoneInfo(tzname)).strftime("%Y-%m-%d %H:%M:%S %Z")
    except Exception:
        return None


def shift(day, hours):
    t = dt.datetime.strptime(day, "%Y-%m-%d") + dt.timedelta(hours=hours)
    return t.strftime("%Y-%m-%d"), t.strftime("%H:%M")


# --------------------------------------------------------------------------
# YAML emitter - deliberately hand-rolled so the file is diff-stable and
# comment-carrying. pyyaml reorders and strips comments; this does neither.
# --------------------------------------------------------------------------

def q(v):
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return repr(v)
    s = str(v)
    if s == "":
        return '""'
    if re.fullmatch(r"[A-Za-z0-9_./+@-]+", s) and not re.fullmatch(r"(true|false|null|yes|no|on|off|~)", s, re.I):
        return s
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ") + '"'


def emit(node, indent=0, out=None):
    out = out if out is not None else []
    pad = "  " * indent
    if isinstance(node, dict):
        for k, v in node.items():
            if isinstance(k, str) and k.startswith("#"):
                for line in str(v).split("\n"):
                    out.append(f"{pad}# {line}" if line else f"{pad}#")
                continue
            if isinstance(v, dict) and v:
                out.append(f"{pad}{k}:")
                emit(v, indent + 1, out)
            elif isinstance(v, list) and v:
                out.append(f"{pad}{k}:")
                emit(v, indent + 1, out)
            elif isinstance(v, (dict, list)):
                out.append(f"{pad}{k}: {'{}' if isinstance(v, dict) else '[]'}")
            else:
                out.append(f"{pad}{k}: {q(v)}")
    elif isinstance(node, list):
        for item in node:
            if isinstance(item, dict):
                keys = list(item.keys())
                first = keys[0]
                out.append(f"{pad}- {first}: {q(item[first])}"
                           if not isinstance(item[first], (dict, list))
                           else f"{pad}- {first}:")
                if isinstance(item[first], (dict, list)):
                    emit(item[first], indent + 2, out)
                rest = {k: item[k] for k in keys[1:]}
                if rest:
                    emit(rest, indent + 1, out)
            else:
                out.append(f"{pad}- {q(item)}")
    return out


# --------------------------------------------------------------------------
# the fleet, and which side of the claim each tail sits on
# --------------------------------------------------------------------------

CONTROL_PROBE = os.path.join(HERE, "..", "data", "recovery", "archive_control_probe.json")


def load_control_by_year():
    """Per-year archive hit rate for aircraft with NO connection to this case."""
    try:
        with open(os.path.normpath(CONTROL_PROBE), encoding="utf-8") as fh:
            return json.load(fh)["by_year"]["control"]
    except (OSError, ValueError, KeyError):
        return {}


CONTROL_BY_YEAR = load_control_by_year()


def load_fleet():
    """tail -> {registry, side, type, is_su}. planes.csv first, lib/fleet.js second."""
    fleet = {}
    for r in read_csv(PLANES_CSV):
        t = r["tail_number"].strip().upper()
        fleet[t] = {"registry": r.get("country_registered") or None,
                    "aircraft_type": r.get("aircraft_type") or None,
                    "nickname": r.get("nickname") or None,
                    "side": "following",
                    "in_73_tally": r.get("in_73_tally") == "yes"}
    js = os.path.join(HERE, "lib", "fleet.js")
    if os.path.exists(js):
        txt = open(js, encoding="utf-8").read()
        for m in re.finditer(r'reg:\s*"([^"]+)".*?side:\s*"([^"]+)".*?type:\s*"([^"]*)".*?registry:\s*"([^"]*)"', txt, re.S):
            reg, side, typ, registry = m.groups()
            t = reg.upper()
            e = fleet.setdefault(t, {})
            e.setdefault("aircraft_type", typ or None)
            e.setdefault("registry", registry or None)
            e["side"] = side
            e.setdefault("nickname", None)
            e.setdefault("in_73_tally", False)
    for t, e in fleet.items():
        e["is_egyptian_su"] = t.startswith("SU-") or t.startswith("SU")
        e["tail"] = t
    # tails in the trace index that neither file names
    return fleet


def norm_tail(t):
    return t.strip().upper().replace(" ", "")


def tail_variants(t):
    t = norm_tail(t)
    return {t, t.replace("-", "")}


# --------------------------------------------------------------------------
# the per-event build
# --------------------------------------------------------------------------

def choose_arrival_airport(lat, lon, curated_code):
    """The centre of the search. Curated value wins; computed value audits it."""
    curated = geo.airport_by_code(curated_code) if curated_code and curated_code != "UNKNOWN" else None
    computed = geo.nearest_airport(
        lat, lon, radius_mi=90,
        predicate=lambda a: a["jet_capability"] in ("jet_capable", "light_jet_capable"))
    if curated and computed and curated["ident"] == computed["ident"]:
        basis = "CURATED_CSV_AND_COMPUTED_NEAREST_JET_FIELD_AGREE"
        chosen = curated
    elif curated:
        basis = "CURATED_tpusa_events.csv_VALUE_KEPT_computed_nearest_jet_field_DIFFERS"
        chosen = curated
    elif computed:
        basis = "COMPUTED_NEAREST_JET_CAPABLE_FIELD_no_curated_value"
        chosen = computed
    else:
        return None, None, None, "NO_AIRPORT_RESOLVED"
    return chosen, curated, computed, basis


def airport_row(a, centre=None):
    row = {
        "airport_code": a["ident"],
        "icao": a.get("icao"),
        "iata": a.get("iata"),
        "name": a["name"],
        "city": a.get("municipality"),
        "region": a.get("iso_region"),
        "country": a.get("iso_country"),
        "type": a["type"],
        "elevation_ft": int(a["elevation_ft"]) if str(a.get("elevation_ft") or "").lstrip("-").isdigit() else None,
        "longest_runway_ft": a.get("longest_runway_ft"),
        "longest_runway_surface": a.get("longest_runway_surface"),
        "runway_count": a.get("runway_count"),
        "runways_lighted": a.get("runways_lighted"),
        "scheduled_service": a.get("scheduled_service"),
        "jet_capability": a.get("jet_capability"),
        "lat": round(a["lat"], 5),
        "lon": round(a["lon"], 5),
    }
    if "distance_mi" in a:
        row["distance_mi"] = a["distance_mi"]
        row["bearing"] = a["bearing"]
    return row


def build_event(row, radius_mi, window_days, tindex, midx, fleet, flights, overlaps):
    mdx = row["mdx_page"]
    slug = os.path.splitext(os.path.basename(mdx))[0]
    first, last, dgran = parse_dates(row["dates"])

    rec = {
        "#0": "GENERATED FILE - regenerate, do not hand-edit.\n"
              "  node/python: apis/public_open_source/code/airports_near.py --only " + slug + "\n"
              "  The prompt that governs this file: prompts/p_airports_near.md",
        "schema": "ck.speaking.airports_near/1",
        "generated_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "generated_by": "site/docs/Planes/following/apis/public_open_source/code/airports_near.py",
    }

    rec["page"] = {
        "slug": slug,
        "mdx": f"site/docs/Planes/following/speaking/{slug}.mdx",
        "yaml": f"site/docs/Planes/following/speaking/{slug}.yaml",
        "url": f"/Planes/following/speaking/{slug}",
    }

    # ---- event ----------------------------------------------------------
    geoc = geo.geocode_place(row["city"], row["state"], row["country"])
    if not geoc:
        # LAST RESORT, and it is labelled as one: the researched
        # nearest_airport_code already in tpusa_events.csv. Used where the US
        # Census has no place by that name (Penn State's "University Park" is a
        # campus, not a Census place). Never used where the city itself is
        # UNKNOWN or AMBIGUOUS - those stay unresolved on purpose.
        cur = geo.airport_by_code(row.get("nearest_airport_code"))
        if cur and (row.get("city") or "").upper() not in ("UNKNOWN", "AMBIGUOUS", ""):
            geoc = {"lat": cur["lat"], "lon": cur["lon"],
                    "method": "curated_nearest_airport_code_in_tpusa_events_csv",
                    "matched": f"{cur['ident']} {cur['name']} - the CITY could not be "
                               f"geocoded, so the search is centred on the curated field itself"}
    tzname, tzmethod = (geo.timezone_at(geoc["lat"], geoc["lon"], row["state"])
                        if geoc else (None, "no_geocode"))
    hhmm, tbasis = parse_local_time(row.get("time"))

    rec["event"] = {
        "title": row["title"],
        "who": row["who"],
        "attendee_class": row.get("attendee_class"),
        "charlie_present": row.get("charlie_present"),
        "erika_present": row.get("erika_present"),
        "attendance_status": row.get("attendance_status"),
        "event_type": row.get("event_type"),
        "dates": {
            "raw": row["dates"],
            "first_day": first,
            "last_day": last,
            "granularity": dgran,
            "certainty": row.get("date_certainty"),
            "#c": "PODCAST_PROXY means the date is a podcast RELEASE date and the event "
                  "was normally 0-7 days earlier. Never publish a same-day claim off one.",
        },
        "local_time": {
            "raw": row.get("time") or None,
            "parsed_hhmm": hhmm,
            "basis": tbasis,
            "timezone": tzname,
            "timezone_method": tzmethod,
        },
        "location": {
            "city": row["city"],
            "state": row["state"] or None,
            "country": row["country"],
            "venue": row.get("university_or_venue") or None,
            "metro_area": row.get("metro_area") or None,
            "geocode": ({"lat": round(geoc["lat"], 5), "lon": round(geoc["lon"], 5),
                         "method": geoc["method"], "matched": geoc["matched"]}
                        if geoc else {"lat": None, "lon": None,
                                      "method": "FAILED",
                                      "matched": "city is UNKNOWN or AMBIGUOUS in tpusa_events.csv - "
                                                 "not filled in from memory, on purpose"}),
        },
        "source": row.get("source") or None,
        "source_url": row.get("source_url") or None,
        "days_before_sept10_2025": int(row["days_before_sept10"]) if (row.get("days_before_sept10") or "").lstrip("-").isdigit() else None,
    }

    if not geoc or not first:
        rec["arrival_airport"] = {
            "resolved": False,
            "reason": "The event has no geocodable city or no parseable date in tpusa_events.csv. "
                      "Nothing downstream can be computed and nothing is guessed.",
        }
        rec["airports_within_radius"] = {"radius_miles": radius_mi, "count": 0, "list": []}
        rec["tracked_plane_presence"] = {"any_found": False,
                                         "reason": "not searched - no coordinates"}
        return slug, rec

    # ---- arrival airport -------------------------------------------------
    chosen, curated, computed, basis = choose_arrival_airport(
        geoc["lat"], geoc["lon"], row.get("nearest_airport_code"))

    if chosen is None:
        rec["arrival_airport"] = {"resolved": False,
                                  "reason": "no airport of any kind within 90 miles"}
        rec["airports_within_radius"] = {"radius_miles": radius_mi, "count": 0, "list": []}
        rec["tracked_plane_presence"] = {"any_found": False, "reason": "no arrival airport"}
        return slug, rec

    venue_mi = round(geo.haversine_mi(geoc["lat"], geoc["lon"], chosen["lat"], chosen["lon"]), 1)

    # arrival / departure estimates
    est_hhmm = hhmm or EVENT_DEFAULT_LOCAL
    arr_day, arr_time = shift(f"{first} {est_hhmm}".split()[0], 0)
    a_dt = dt.datetime.strptime(f"{first} {est_hhmm}", "%Y-%m-%d %H:%M") - dt.timedelta(hours=ARRIVE_BEFORE_H)
    dp_dt = dt.datetime.strptime(f"{last} {est_hhmm}", "%Y-%m-%d %H:%M") + dt.timedelta(hours=DEPART_AFTER_H + 2)

    est_conf = "medium" if hhmm else "low"
    est_basis = (f"event start {est_hhmm} local ({tbasis}) minus {ARRIVE_BEFORE_H}h"
                 if hhmm else
                 f"{EVENT_DEFAULT_NOTE}; minus {ARRIVE_BEFORE_H}h")

    arrival = {
        "#0": "ESTIMATE. No published Kirk-side flight record exists for this event unless\n"
              "the observed_by_adsb block below is non-empty. This is arithmetic on the\n"
              "event time, not a landing record.",
        "chosen_airport": airport_row(dict(chosen, distance_mi=venue_mi,
                                           bearing=geo.compass(geo.bearing_deg(
                                               geoc["lat"], geoc["lon"], chosen["lat"], chosen["lon"])))),
        "distance_from_event_city_mi": venue_mi,
        "selection_basis": basis,
        "curated_value_in_tpusa_events_csv": {
            "airport_code": row.get("nearest_airport_code") or None,
            "airport_name": row.get("nearest_airport_name") or None,
            "distance_mi": row.get("airport_distance_mi") or None,
        },
        "computed_nearest_jet_capable_field": ({
            "airport_code": computed["ident"], "name": computed["name"],
            "distance_mi": round(geo.haversine_mi(geoc["lat"], geoc["lon"], computed["lat"], computed["lon"]), 1),
            "longest_runway_ft": computed.get("longest_runway_ft"),
        } if computed else None),
        "estimated_arrival": {
            "date": a_dt.strftime("%Y-%m-%d"),
            "local_time": a_dt.strftime("%H:%M"),
            "timezone": tzname,
            "utc": to_utc(a_dt.strftime("%Y-%m-%d"), a_dt.strftime("%H:%M"), tzname),
            "basis": est_basis,
            "confidence": est_conf,
        },
        "estimated_departure": {
            "date": dp_dt.strftime("%Y-%m-%d"),
            "local_time": dp_dt.strftime("%H:%M"),
            "timezone": tzname,
            "utc": to_utc(dp_dt.strftime("%Y-%m-%d"), dp_dt.strftime("%H:%M"), tzname),
            "basis": f"event end + {DEPART_AFTER_H + 2}h (speech, exit, wheels-up)",
            "confidence": est_conf,
        },
    }

    # ---- airports within the radius --------------------------------------
    near = geo.airports_within(chosen["lat"], chosen["lon"], radius_mi)
    near_by_code = {a["ident"]: a for a in near}
    # A HARD RADIUS CREATES A CLIFF, and a cliff hides evidence. KSLC to KPVU is
    # 41.6 miles: at a flat 40 the 23 April 2024 Salt Lake City pairing vanishes
    # by 1.6 miles. So the search runs to 1.5x the radius and reports anything
    # found in the outer ring SEPARATELY, labelled as outside the radius. It is
    # never counted as an in-radius hit.
    outer_mi = radius_mi * 1.5
    wide = geo.airports_within(chosen["lat"], chosen["lon"], outer_mi)
    wide_by_code = {a["ident"]: a for a in wide}

    # ---- the search window ------------------------------------------------
    w_from = (d(first) - dt.timedelta(days=window_days)).isoformat()
    w_to = (d(last) + dt.timedelta(days=window_days)).isoformat()
    window_days_list = []
    cur = d(w_from)
    while cur <= d(w_to):
        window_days_list.append(cur.isoformat())
        cur += dt.timedelta(days=1)

    def gap_days(day):
        """Signed distance in days from a single day to the event window.
        Negative = before the event, positive = after, 0 = during."""
        x = d(day)
        if x < d(first):
            return (x - d(first)).days
        if x > d(last):
            return (x - d(last)).days
        return 0

    def gap_days_interval(start, end):
        """Gap between a STAY [start,end] and the event window. 0 when they
        overlap at all - an aircraft parked across the event date is gap 0, not
        the distance from one of its endpoints. Getting this wrong is how an
        84-day maintenance stay reads as an 80-day miss."""
        s0, e0 = d(start), d(end)
        if e0 < d(first):
            return (e0 - d(first)).days
        if s0 > d(last):
            return (s0 - d(last)).days
        return 0

    # ---- the control test, read for THIS event's year --------------------
    # A gap can only be called a removal once an unrelated airframe has failed
    # the same way on the same dates. The 2022 line below is the whole reason
    # this block exists: BOTH free archives return nothing at all for 2022,
    # for the control aircraft as much as for the case aircraft.
    year = first[:4]
    ctl = CONTROL_BY_YEAR.get(year)
    ctl_pct = ctl["hit_pct"] if ctl else None
    if ctl is None:
        ctl_verdict = ("NO CONTROL DATA FOR %s. Do not characterise any gap in this window "
                       "until the control test has been run for it." % year)
    elif ctl["hit_pct"] < 10:
        ctl_verdict = (
            "ARCHIVE RETENTION BOUNDARY. Unrelated control aircraft return %s%% for %s from "
            "these archives - they hold essentially nothing for this year at all. AN EMPTY "
            "RESULT IN THIS WINDOW SAYS NOTHING ABOUT ANY AIRCRAFT AND MUST NEVER BE "
            "PUBLISHED AS A REMOVAL OR AS AN ABSENCE. The ADS-B Exchange monthly sample "
            "(one day per month) is the only free route into this period."
            % (ctl["hit_pct"], year))
    elif ctl["hit_pct"] < 60:
        ctl_verdict = ("PARTIAL ARCHIVE COVERAGE. Control aircraft return %s%% for %s. Treat a "
                       "gap here as inconclusive." % (ctl["hit_pct"], year))
    else:
        ctl_verdict = (
            "ARCHIVE HEALTHY. Unrelated control aircraft return %s%% for %s, so an empty result "
            "here is a fact about the AIRCRAFT rather than about the archive. It is still not "
            "proof the aircraft was elsewhere: transponder off, outside receiver coverage, and a "
            "wrong claimed date all look identical from here." % (ctl["hit_pct"], year))

    # ---- 1. primary: recovered ADS-B ground contacts ---------------------
    adsb_hits, coverage_days, no_coverage = [], 0, {}
    merge = {}
    cov_by_side = {}
    asked_empty = 0
    for tail, days in tindex.items():
        t = norm_tail(tail)
        info = fleet.get(t) or fleet.get(t.replace("-", "")) or {}
        held = [x for x in window_days_list if x in days]
        coverage_days += len(held)
        side = info.get("side", "unknown")
        c = cov_by_side.setdefault(side, {"tails": 0, "held": 0, "needed": 0})
        c["tails"] += 1
        c["held"] += len(held)
        c["needed"] += len(window_days_list)
        mdays = midx.get(t, {})
        c_empty = sum(1 for x in window_days_list if x not in days and x in mdays)
        c["asked_and_empty"] = c.get("asked_and_empty", 0) + c_empty
        c["never_asked"] = c.get("never_asked", 0) + (len(window_days_list) - len(held) - c_empty)
        asked_empty += c_empty
        missing = [x for x in window_days_list if x not in days]
        if missing:
            no_coverage[t] = missing
        for day in held:
            for pull in days[day]:
                for v in pull["ground_visits"]:
                    if not v.get("resolved"):
                        continue
                    dist = geo.haversine_mi(chosen["lat"], chosen["lon"], v["lat"], v["lon"])
                    if dist > outer_mi:
                        continue
                    key = (t, day, v["airport_code"])
                    slot = merge.setdefault(key, {
                        "tail": t,
                        "registry": info.get("registry"),
                        "side": info.get("side", "unknown"),
                        "aircraft_type": info.get("aircraft_type"),
                        "is_egyptian_su": bool(info.get("is_egyptian_su") or t.startswith("SU")),
                        "in_73_tally": bool(info.get("in_73_tally")),
                        "airport_code": v["airport_code"],
                        "airport_name": v["airport_name"],
                        "distance_from_arrival_airport_mi": round(dist, 1),
                        "median_distance_from_that_runway_km": v["median_distance_km"],
                        "date_utc": day,
                        "gap_days_from_event": gap_days(day),
                        "on_ground_first_utc": v["first_seen_utc"],
                        "on_ground_last_utc": v["last_seen_utc"],
                        "on_ground_first_local": utc_to_local(v["first_seen_utc"], tzname),
                        "on_ground_last_local": utc_to_local(v["last_seen_utc"], tzname),
                        "ground_positions": v["ground_points"],
                        "ground_minutes": None,
                        "adsb_sources": [],
                        "source_count": 0,
                        "trace_files": [],
                        "evidence_class": "adsb_public_history",
                        "#c": "PRESENCE ONLY. A trace never establishes purpose and never "
                              "establishes who was aboard.",
                    })
                    slot["adsb_sources"].append(pull["source"])
                    slot["trace_files"].append("site/docs/Planes/" + pull["file"])
                    slot["source_count"] = len(set(slot["adsb_sources"]))
                    # keep the widest observed ground window across sources
                    if v["first_seen_utc"] < slot["on_ground_first_utc"]:
                        slot["on_ground_first_utc"] = v["first_seen_utc"]
                        slot["on_ground_first_local"] = utc_to_local(v["first_seen_utc"], tzname)
                    if v["last_seen_utc"] > slot["on_ground_last_utc"]:
                        slot["on_ground_last_utc"] = v["last_seen_utc"]
                        slot["on_ground_last_local"] = utc_to_local(v["last_seen_utc"], tzname)
                    slot.setdefault("_windows", []).append(
                        (pull["source"], v["first_seen_utc"], v["last_seen_utc"]))

    for slot in merge.values():
        slot["adsb_sources"] = sorted(set(slot["adsb_sources"]))
        slot["trace_files"] = sorted(set(slot["trace_files"]))
        try:
            a = dt.datetime.fromisoformat(slot["on_ground_first_utc"].replace("Z", "+00:00"))
            b = dt.datetime.fromisoformat(slot["on_ground_last_utc"].replace("Z", "+00:00"))
            slot["ground_minutes"] = round((b - a).total_seconds() / 60, 1)
        except Exception:
            pass
        # CROSS-CHECK. Two independent free archives should agree on the same
        # aircraft-day. Where they do not, the disagreement is published, never
        # resolved by picking one.
        wins = slot.pop("_windows", [])
        if len(set(w[0] for w in wins)) > 1:
            spread = max(
                abs((dt.datetime.fromisoformat(x[1].replace("Z", "+00:00"))
                     - dt.datetime.fromisoformat(y[1].replace("Z", "+00:00"))).total_seconds())
                for x in wins for y in wins)
            slot["cross_source_agreement"] = (
                "AGREE (first-contact times within %ds across %d independent archives)" % (round(spread), slot["source_count"])
                if spread <= 120 else
                "DISAGREE by %ds on first contact across %d archives - published as a "
                "disagreement, not reconciled" % (round(spread), slot["source_count"]))
        else:
            slot["cross_source_agreement"] = "SINGLE SOURCE - not independently corroborated"
        adsb_hits.append(slot)

    # Egyptian SU- tails first: they are the subject of the claim.
    adsb_hits.sort(key=lambda h: (not h["is_egyptian_su"], h["date_utc"], h["tail"]))

    # ---- 2. the curated flights.csv register ------------------------------
    csv_hits = []
    for f in flights:
        code = (f.get("airport_code") or "").strip().upper()
        if not code or code not in wide_by_code:
            continue
        s, e = f.get("start_date"), f.get("end_date")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", s or ""):
            continue
        e = e if re.fullmatch(r"\d{4}-\d{2}-\d{2}", e or "") else s
        if d(e) < d(w_from) or d(s) > d(w_to):
            continue
        t = norm_tail(f["plane_tail_number"])
        info = fleet.get(t, {})
        csv_hits.append({
            "tail": t,
            "registry": info.get("registry") or f.get("country"),
            "is_egyptian_su": t.startswith("SU"),
            "in_73_tally": bool(info.get("in_73_tally")),
            "airport_code": code,
            "airport_name": wide_by_code[code]["name"],
            "distance_from_arrival_airport_mi": wide_by_code[code]["distance_mi"],
            "on_ground_start_date": s,
            "on_ground_end_date": e,
            "gap_days_from_event": gap_days_interval(s, e),
            "on_ground_during_event": gap_days_interval(s, e) == 0 and d(s) <= d(last) and d(e) >= d(first),
            "days_on_ground": f.get("days_on_ground") or None,
            "confidence": f.get("confidence"),
            "source": f.get("source"),
            "evidence_class": "curated_register_flights.csv",
        })

    # ---- 3. the claimed-overlap register ---------------------------------
    ov_hits = []
    for o in overlaps:
        code = (o.get("airport_code") or "").strip().upper()
        day = (o.get("date") or "").strip()
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", day):
            continue
        if code not in wide_by_code:
            continue
        if d(day) < d(w_from) or d(day) > d(w_to):
            continue
        ov_hits.append({
            "overlap_id": o["overlap_id"],
            "date": day,
            "gap_days_from_event": gap_days(day),
            "airport_code": code,
            "foreign_tail": o.get("foreign_tail"),
            "kirk_tail": o.get("kirk_tail") or None,
            "subject": o.get("subject"),
            "confidence": o.get("confidence"),
            "audit_verdict": o.get("audit_verdict"),
            "survives_audit": o.get("survives_audit"),
            "source": o.get("source"),
            "evidence_class": "claimed_overlap_register",
            "#c": "A CLAIM, not a record. audit_verdict is this repo's own check of it.",
        })

    def inside(h):
        return h.get("distance_from_arrival_airport_mi", 0) <= radius_mi

    outer_adsb = [h for h in adsb_hits if not inside(h)]
    outer_csv = [h for h in csv_hits if not inside(h)]
    adsb_hits = [h for h in adsb_hits if inside(h)]
    csv_hits = [h for h in csv_hits if inside(h)]
    outer_ov = [h for h in ov_hits
                if wide_by_code.get(h["airport_code"], {}).get("distance_mi", 0) > radius_mi]
    ov_hits = [h for h in ov_hits if h not in outer_ov]
    for h in outer_adsb + outer_csv:
        h["#c"] = ("OUTSIDE THE %g-MILE RADIUS. Reported so a near miss is not hidden by "
                   "the cliff edge. This is NOT an in-radius hit." % radius_mi)

    su_adsb = [h for h in adsb_hits if h["is_egyptian_su"]]
    su_csv = [h for h in csv_hits if h["is_egyptian_su"]]

    # attach per-airport presence to the radius list
    per_ap = {}
    for h in adsb_hits:
        per_ap.setdefault(h["airport_code"], []).append(
            f"{h['tail']} on {h['date_utc']} - ADS-B ground contact, "
            f"{h['ground_minutes']} min, {h['source_count']} archive(s)")
    for h in csv_hits:
        per_ap.setdefault(h["airport_code"], []).append(
            f"{h['tail']} {h['on_ground_start_date']}..{h['on_ground_end_date']} (flights.csv)")

    ap_list = []
    for a in near:
        r = airport_row(a)
        r["tracked_plane_presence_in_window"] = per_ap.get(a["ident"], [])
        ap_list.append(r)

    jetc = sum(1 for a in near if a["jet_capability"] == "jet_capable")
    lightc = sum(1 for a in near if a["jet_capability"] == "light_jet_capable")
    unlisted = sum(1 for a in near if not a["scheduled_service"])

    rec["search"] = {
        "radius_miles": radius_mi,
        "window_days_each_side": window_days,
        "window_from": w_from,
        "window_to": w_to,
        "window_day_count": len(window_days_list),
        "centre": chosen["ident"],
        "tails_searched": sorted(tindex.keys()),
        "sources_searched": [
            "recovered ADS-B traces on disk (site/docs/Planes/<TAIL>/data/recovered/)",
            "site/docs/Planes/following/flights.csv",
            "site/docs/Planes/following/overlaps.csv",
        ],
    }

    rec["arrival_airport"] = arrival
    rec["arrival_airport"]["observed_by_adsb"] = [
        {"tail": h["tail"], "airport_code": h["airport_code"],
         "date_utc": h["date_utc"], "gap_days_from_event": h["gap_days_from_event"],
         "on_ground_first_local": h["on_ground_first_local"],
         "on_ground_last_local": h["on_ground_last_local"],
         "on_ground_first_utc": h["on_ground_first_utc"],
         "on_ground_last_utc": h["on_ground_last_utc"],
         "ground_minutes": h["ground_minutes"],
         "adsb_sources": h["adsb_sources"],
         "#c": "OBSERVED, not estimated. This is a real ground contact by a Kirk-side "
               "airframe. It still does not establish who was aboard."}
        for h in adsb_hits if h["side"] == "kirk"
    ] or []
    if not rec["arrival_airport"]["observed_by_adsb"]:
        rec["arrival_airport"]["observed_by_adsb_note"] = (
            "NO Kirk-side aircraft is on disk on the ground within %d miles of %s in this window. "
            "The arrival and departure above stay estimates." % (radius_mi, chosen["ident"]))

    rec["airports_within_radius"] = {
        "#0": "Every field a private jet could physically use within the radius.\n"
              "Heliports, seaplane bases, balloonports and closed fields are excluded -\n"
              "a business jet cannot use any of them. Everything else is kept, including\n"
              "every small strip with no scheduled service: those are the point of the sweep.",
        "radius_miles": radius_mi,
        "centre_airport": chosen["ident"],
        "count": len(near),
        "jet_capable_count": jetc,
        "light_jet_capable_count": lightc,
        "no_scheduled_service_count": unlisted,
        "source": "OurAirports (CC0) airports.csv + runways.csv",
        "list": ap_list,
    }

    rec["tracked_plane_presence"] = {
        "#0": "Was any tracked aircraft on the ground at any field in the list above,\n"
              "inside the window? Three registers are searched and kept apart, strongest\n"
              "first. NEVER collapse them into one number.",
        "window": {"from": w_from, "to": w_to, "days_each_side": window_days},
        "any_found": bool(adsb_hits or csv_hits or ov_hits),
        "egyptian_su_found": bool(su_adsb or su_csv),
        "counts": {
            "adsb_ground_contacts": len(adsb_hits),
            "adsb_ground_contacts_egyptian_su": len(su_adsb),
            "flights_csv_stays": len(csv_hits),
            "flights_csv_stays_egyptian_su": len(su_csv),
            "claimed_overlaps": len(ov_hits),
        },
        "from_adsb_traces": adsb_hits,
        "from_flights_csv": csv_hits,
        "from_overlaps_csv": ov_hits,
        "just_outside_the_radius": {
            "#0": "A hard radius creates a cliff and a cliff hides evidence. These fields\n"
                  "sit between %g and %g miles from the arrival airport. They are NOT counted\n"
                  "as hits and must never be published as ones - they are here so a near miss\n"
                  "is visible rather than silently dropped." % (radius_mi, outer_mi),
            "outer_radius_miles": outer_mi,
            "adsb_ground_contacts": outer_adsb,
            "flights_csv_stays": outer_csv,
            "claimed_overlaps": outer_ov,
        },
        "coverage": {
            "#0": "AN EMPTY RESULT ABOVE IS NOT A FINDING UNLESS THIS SAYS THE DAYS WERE HELD.\n"
                  "aircraft_days_needed = tails x days in the window.\n"
                  "  aircraft_days_held                     a trace is on disk\n"
                  "  aircraft_days_asked_and_archive_empty  the archive WAS asked and holds\n"
                  "                                         nothing for that aircraft-day\n"
                  "  aircraft_days_never_asked               nobody has queried it yet\n"
                  "Only the FIRST TWO are evidence of anything. The third is an open question,\n"
                  "and closing it is what fetch_event_windows.py is for. Even an asked-and-empty\n"
                  "day is NOT proof the aircraft was elsewhere: a volunteer receiver network\n"
                  "heard nothing, and transponder-off, out-of-coverage, and a wrong claimed date\n"
                  "all look identical from here.",
            "aircraft_days_needed": len(tindex) * len(window_days_list),
            "aircraft_days_held": coverage_days,
            "aircraft_days_asked_and_archive_empty": asked_empty,
            "aircraft_days_never_asked": len(tindex) * len(window_days_list) - coverage_days - asked_empty,
            "coverage_pct": round(100.0 * coverage_days / max(1, len(tindex) * len(window_days_list)), 1),
            "queried_pct": round(100.0 * (coverage_days + asked_empty)
                                 / max(1, len(tindex) * len(window_days_list)), 1),
            "tails_with_no_trace_in_window": sorted(
                t for t, miss in no_coverage.items() if len(miss) == len(window_days_list)),
            "archive_control_test": {
                "#0": "The control test, run 24 Aug 2026 over every 8th window day against two\n"
                      "aircraft with no connection to this case. Full record:\n"
                      "apis/public_open_source/data/recovery/archive_control_probe.json",
                "control_hit_pct_this_year": ctl_pct,
                "verdict": ctl_verdict,
            },
            "by_side": {
                side: {
                    "#0": ("FOLLOWING is the side the claim is about - the Egyptian SU- tails.\n"
                           "This percentage is the one that decides whether an empty result means\n"
                           "anything at all." if side == "following" else
                           "KIRK-side coverage is what turns an ESTIMATED arrival into an\n"
                           "OBSERVED one. Low here means the arrival times above stay estimates."
                           if side == "kirk" else "Other tracked aircraft. A DIFFERENT CLAIM - "
                           "do not merge the threads."),
                    "tails": c["tails"],
                    "aircraft_days_needed": c["needed"],
                    "aircraft_days_held": c["held"],
                    "aircraft_days_asked_and_archive_empty": c.get("asked_and_empty", 0),
                    "aircraft_days_never_asked": c.get("never_asked", 0),
                    "coverage_pct": round(100.0 * c["held"] / max(1, c["needed"]), 1),
                    "queried_pct": round(100.0 * (c["held"] + c.get("asked_and_empty", 0))
                                         / max(1, c["needed"]), 1),
                }
                for side, c in sorted(cov_by_side.items())
            },
        },
    }

    rec["counterargument"] = [
        "ONE PAIRING IS NOT EVIDENCE. The claim under test is a repetition across many "
        "stops, and any single pairing has an innocent explanation a reader will find.",
        "A field inside the radius is a field a jet COULD have used. Nothing here shows "
        "that anyone did use it, or that two aircraft on one ramp had any connection.",
        "Maintenance is the strongest innocent explanation in this record: Duncan Aviation "
        "(Provo and Lincoln) and Yingling (Wichita) are Part 145 Falcon and Gulfstream shops, "
        "and a Falcon 7X sitting for weeks at one reads as a maintenance visit.",
        "Transatlantic customs and fuel stops explain the recurring East Coast fields.",
        "ERIKA'S SIDE IS THE WEAK SIDE. Her flight logs are reported erased, so any Erika "
        "pairing rests on the foreign aircraft's track plus a CLAIMED location for her. "
        "See /Planes/Erika-Flight-Logs-Erased.",
    ]

    rec["what_we_do_not_know"] = [
        "Whether Charlie Kirk, Erika Kirk, or any TPUSA party actually flew to this event, "
        "or which aircraft they used. The arrival airport above is an inference from the "
        "venue city, not a record.",
        "Whether the estimated arrival and departure times are within hours or within days "
        "of the truth, wherever observed_by_adsb is empty.",
        "What the tracked aircraft were doing at any field they appear at. A trace proves "
        "presence, never purpose and never occupancy.",
        "Whether the receiver networks simply did not hear an aircraft that was there. "
        "See the coverage block - an absence is not a finding.",
    ]
    return slug, rec


# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only", action="append", default=[],
                    help="slug of one speaking page, repeatable")
    ap.add_argument("--radius", type=float, default=DEFAULT_RADIUS_MI)
    ap.add_argument("--window", type=int, default=DEFAULT_WINDOW_DAYS)
    ap.add_argument("--rebuild-traces", action="store_true")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    print(f"trace index ... ", end="", flush=True)
    tindex = traces.build_index(cache_path=os.path.normpath(CACHE), rebuild=args.rebuild_traces)
    print(f"{len(tindex)} tails, "
          f"{sum(len(v) for v in tindex.values())} aircraft-days on disk")

    midx = traces.build_miss_index()
    print(f"miss index ... {sum(len(v) for v in midx.values())} aircraft-days asked and empty")

    fleet = load_fleet()
    flights = read_csv(FLIGHTS_CSV)
    overlaps = read_csv(OVERLAPS_CSV)
    events = [r for r in read_csv(EVENTS_CSV) if "/speaking/" in (r.get("mdx_page") or "")]

    written, summary = 0, []
    for row in events:
        slug = os.path.splitext(os.path.basename(row["mdx_page"]))[0]
        if args.only and slug not in args.only:
            continue
        slug, rec = build_event(row, args.radius, args.window, tindex, midx, fleet, flights, overlaps)
        text = "\n".join(emit(rec)) + "\n"
        out = os.path.join(SPEAKING, slug + ".yaml")
        if not args.dry_run:
            with open(out, "w", encoding="utf-8") as fh:
                fh.write(text)
        written += 1
        tp = rec.get("tracked_plane_presence", {})
        outer = tp.get("just_outside_the_radius", {})
        outer_su = [h for h in (outer.get("adsb_ground_contacts") or [])
                    + (outer.get("flights_csv_stays") or []) if h.get("is_egyptian_su")]
        aw = rec.get("airports_within_radius", {})
        arr = rec.get("arrival_airport", {})
        cov = tp.get("coverage", {})
        summary.append({
            "outer_su": outer_su,
            "row": {
                "slug": slug,
                "date_first": rec["event"]["dates"]["first_day"] or "",
                "date_last": rec["event"]["dates"]["last_day"] or "",
                "date_certainty": rec["event"]["dates"]["certainty"] or "",
                "who": rec["event"]["who"],
                "attendee_class": rec["event"]["attendee_class"] or "",
                "city": rec["event"]["location"]["city"],
                "state": rec["event"]["location"]["state"] or "",
                "venue": rec["event"]["location"]["venue"] or "",
                "geocode_method": rec["event"]["location"]["geocode"]["method"],
                "arrival_airport": (arr.get("chosen_airport") or {}).get("airport_code") or "",
                "arrival_airport_name": (arr.get("chosen_airport") or {}).get("name") or "",
                "arrival_selection_basis": arr.get("selection_basis") or "UNRESOLVED",
                "arrival_dist_from_city_mi": arr.get("distance_from_event_city_mi") or "",
                "est_arrival_local": ((arr.get("estimated_arrival") or {}).get("date") or "") +
                                     " " + ((arr.get("estimated_arrival") or {}).get("local_time") or ""),
                "est_departure_local": ((arr.get("estimated_departure") or {}).get("date") or "") +
                                       " " + ((arr.get("estimated_departure") or {}).get("local_time") or ""),
                "est_confidence": (arr.get("estimated_arrival") or {}).get("confidence") or "",
                "kirk_side_observed_on_adsb": len(arr.get("observed_by_adsb") or []),
                "airports_within_radius": aw.get("count", 0),
                "jet_capable": aw.get("jet_capable_count", 0),
                "light_jet_capable": aw.get("light_jet_capable_count", 0),
                "no_scheduled_service": aw.get("no_scheduled_service_count", 0),
                "su_found_in_radius": "yes" if tp.get("egyptian_su_found") else "no",
                "adsb_ground_contacts": tp.get("counts", {}).get("adsb_ground_contacts", 0),
                "adsb_ground_contacts_su": tp.get("counts", {}).get("adsb_ground_contacts_egyptian_su", 0),
                "flights_csv_stays": tp.get("counts", {}).get("flights_csv_stays", 0),
                "flights_csv_stays_su": tp.get("counts", {}).get("flights_csv_stays_egyptian_su", 0),
                "claimed_overlaps": tp.get("counts", {}).get("claimed_overlaps", 0),
                "su_just_outside_radius": len(outer_su),
                "su_just_outside_tails": ";".join(sorted({h["tail"] for h in outer_su})),
                "archive_control_verdict": (cov.get("archive_control_test", {})
                                            .get("verdict", "") or "").split(".")[0],
                "aircraft_days_needed": cov.get("aircraft_days_needed", 0),
                "aircraft_days_held": cov.get("aircraft_days_held", 0),
                "coverage_pct_all_tails": cov.get("coverage_pct", 0),
                "coverage_pct_following_fleet": (cov.get("by_side", {})
                                                 .get("following", {})
                                                 .get("coverage_pct", 0)),
                "queried_pct_following_fleet": (cov.get("by_side", {})
                                                .get("following", {})
                                                .get("queried_pct", 0)),
                "following_days_never_asked": (cov.get("by_side", {})
                                               .get("following", {})
                                               .get("aircraft_days_never_asked", 0)),
                "yaml": f"site/docs/Planes/following/speaking/{slug}.yaml",
            },
            "slug": slug,
            "date": rec["event"]["dates"]["first_day"],
            "city": rec["event"]["location"]["city"],
            "airport": rec.get("arrival_airport", {}).get("chosen_airport", {}).get("airport_code"),
            "n_airports": rec.get("airports_within_radius", {}).get("count", 0),
            "su_found": tp.get("egyptian_su_found", False),
            "counts": tp.get("counts", {}),
        })

    verb = "would write" if args.dry_run else "wrote"
    print(f"{verb} {written} yaml files into {SPEAKING}")

    # The roll-up. Underscore-prefixed so Docusaurus never publishes it, and a
    # CSV so it can be sorted and grepped without opening 139 yaml files.
    if not args.dry_run and not args.only:
        cols = list(summary[0]["row"].keys()) if summary else []
        out = os.path.join(SPEAKING, "_airports_near_summary.csv")
        with open(out, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=cols)
            w.writeheader()
            for s_ in summary:
                w.writerow(s_["row"])
        print(f"wrote the roll-up: {os.path.relpath(out, REPO)}")

    if args.report:
        hits = [s for s in summary if s["su_found"]]
        print(f"\nEVENTS WITH AN EGYPTIAN SU- TAIL INSIDE THE WINDOW: {len(hits)} of {len(summary)}")
        for s in hits:
            c = s["counts"]
            print(f"  {s['date']}  {s['city']:<20} {s['airport']:<6} "
                  f"{s['n_airports']:>3} fields   "
                  f"adsb={c.get('adsb_ground_contacts_egyptian_su', 0)} "
                  f"flights.csv={c.get('flights_csv_stays_egyptian_su', 0)} "
                  f"claims={c.get('claimed_overlaps', 0)}")
        outer_hits = [s for s in summary if s["outer_su"] and not s["su_found"]]
        print(f"\nNEAR MISSES - an Egyptian SU- tail just OUTSIDE the radius: {len(outer_hits)}")
        for s in outer_hits:
            for h in s["outer_su"]:
                print(f"  {s['date']}  {s['city']:<20} {s['airport']:<6} "
                      f"{h['tail']} at {h['airport_code']} "
                      f"{h.get('distance_from_arrival_airport_mi')}mi  "
                      f"gap {h.get('gap_days_from_event')}d")
        print("  (NOT hits. Reported so the 40-mile cliff edge does not hide them.)")

        noap = [s for s in summary if not s["airport"]]
        if noap:
            print(f"\nNO ARRIVAL AIRPORT RESOLVED ({len(noap)}): "
                  + ", ".join(s["slug"] for s in noap))
        tot = sum(s["n_airports"] for s in summary)
        print(f"\nairports within radius, total across all events: {tot}, "
              f"mean {tot / max(1, len(summary)):.1f}")


if __name__ == "__main__":
    main()
