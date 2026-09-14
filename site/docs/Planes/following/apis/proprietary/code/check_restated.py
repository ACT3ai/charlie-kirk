#!/usr/bin/env python3
"""Prove that every restated FlightAware file carries EVERY fact of its raw response - and nothing else.

WHY. This repo is public and FlightAware's terms do not allow republishing an AeroAPI
response. The raw responses are checked in to the private `all` repo (private_store.py).
What we publish is a RESTATED file per response: the same facts, laid out in our own
structure and words, written by an AI running
    ~/BGit/all/politics/charlie_kirk/flights/p_restate_flight_data.md
An AI can drop a digit, swap two times, get a time zone wrong, or add something that was
never in the response. This script is the reason we can still say "every fact on this
page came from FlightAware". It rebuilds the expected content from the raw response
itself and compares it to what the AI wrote, field by field.

  python3 check_restated.py              check every raw file; exit 0 only if all pass
  python3 check_restated.py --todo       list only raw files whose restated file is missing or wrong
  python3 check_restated.py --file SU-BTT/2022-10-02_to_2022-10-09_history_p0.json

WHAT "PASS" MEANS
  * the restated file exists, parses as YAML, and matches the expected content exactly
  * except the free-text keys (FREE_TEXT below), which must be present and non-empty but
    are the AI's own words
  * no extra keys: a fact that is not in the raw response is an error, not a bonus
  * a raw field this script does not know stops the check - a new FlightAware field means
    the prompt and this script get updated together, never that the field is silently lost

There is deliberately no --write mode. The restated files are the prompt's output; this
script only judges them.
"""
import datetime as dt, json, os, re, sys
from zoneinfo import ZoneInfo

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from private_store import private_vendor_dir  # noqa: E402

RAW = private_vendor_dir("flightaware")
OUT = os.path.normpath(os.path.join(HERE, "..", "data", "flightaware_restated"))

HISTORY = re.compile(r"^(\d{4}-\d{2}-\d{2})_to_(\d{4}-\d{2}-\d{2})_history_p(\d+)\.json(\.pulled-[\w-]+)?$")
PROBE = re.compile(r"^probe_(blocked|owner)\.json(\.pulled-[\w-]+)?$")
POSITION = re.compile(r"^L\s+(-?\d+(?:\.\d+)?)\s+(-?\d+(?:\.\d+)?)$")

# Raw keys that are not facts about the flight: a vendor product switch and a link into
# the vendor's own website. Named here so leaving them out is a decision, not a loss.
NOT_FACTS = {"foresight_predictions_available"}
AIRPORT_NOT_FACTS = {"airport_info_url"}

FLIGHT_KEYS = {
    "ident", "ident_icao", "ident_iata", "atc_ident", "fa_flight_id", "inbound_fa_flight_id",
    "operator", "operator_icao", "operator_iata", "flight_number", "registration", "aircraft_type", "type",
    "codeshares", "codeshares_iata", "blocked", "diverted", "cancelled", "position_only",
    "origin", "destination", "departure_delay", "arrival_delay", "filed_ete", "filed_airspeed",
    "filed_altitude", "route", "route_distance", "progress_percent", "status",
    "actual_runway_off", "actual_runway_on", "baggage_claim", "gate_origin", "gate_destination",
    "terminal_origin", "terminal_destination", "seats_cabin_first", "seats_cabin_business", "seats_cabin_coach",
    *[f"{b}_{e}" for b in ("scheduled", "estimated", "actual") for e in ("out", "off", "on", "in")],
} | NOT_FACTS
AIRPORT_KEYS = {"code", "code_icao", "code_iata", "code_lid", "name", "city", "timezone"} | AIRPORT_NOT_FACTS
PAGE_KEYS = {"flights", "links", "num_pages"}
OWNER_KEYS = {"name", "location", "location2", "website"}

# Free text the AI writes in its own words. Must exist and be non-empty; not compared.
FREE_TEXT = {("about", "source"), ("about", "question_asked"), ("reading",)}
WITHHELD_PERSON = "withheld - private individual"

EVENTS = (("out", "left_gate"), ("off", "takeoff"), ("on", "landing"), ("in", "reached_gate"))
BASES = ("scheduled", "estimated", "actual")


class UnknownField(Exception):
    pass


def out_rel(rel):
    tail, base = rel.split("/", 1)
    m = HISTORY.match(base)
    if m:
        return f"{tail}/{m[1]}_to_{m[2]}_flights_page{int(m[3]) + 1}{m[4] or ''}.yaml"
    m = PROBE.match(base)
    if m:
        stem = "tracking_block_status" if m[1] == "blocked" else "registered_owner"
        return f"{tail}/{stem}{m[2] or ''}.yaml"
    return None


def raw_files():
    for tail in sorted(os.listdir(RAW)):
        d = os.path.join(RAW, tail)
        if tail.startswith("_") or not os.path.isdir(d):
            continue
        for name in sorted(os.listdir(d)):
            if not name.endswith(".meta.json") and out_rel(f"{tail}/{name}"):
                yield f"{tail}/{name}"


def z(s):
    return dt.datetime.fromisoformat(s.replace("Z", "+00:00"))


def hms(seconds):
    s = int(round(seconds))
    return f"{s // 3600}:{s % 3600 // 60:02d}:{s % 60:02d}"


def signed(seconds):
    return ("-" if seconds < 0 else "+") + hms(abs(seconds))


# FlightAware fills the delay of a flight with no actual time (a cancelled flight, say)
# with a number near minus the Unix epoch - about -55 years. Restated as h:mm:ss that reads
# "-488178:48:01", which a reader would take for a real delay. The number is still kept.
DELAY_PLACEHOLDER_S = 7 * 86400


def delay(seconds):
    if abs(seconds) > DELAY_PLACEHOLDER_S:
        return f"not meaningful (FlightAware gave {seconds} seconds; no actual time recorded)"
    return signed(seconds)


def local(utc, tz):
    t = z(utc).astimezone(ZoneInfo(tz)).isoformat(sep=" ")
    return t


def present(v):
    return v not in (None, "", [], {})


def airport(a):
    a = a or {}
    unknown = set(a) - AIRPORT_KEYS
    if unknown:
        raise UnknownField(f"airport fields {sorted(unknown)}")
    o = {}
    code = a.get("code")
    m = POSITION.match(code or "")
    if m:
        o["position_only_point"] = {"lat": float(m[1]), "lon": float(m[2])}
    for k, name in (("code_icao", "icao"), ("code_iata", "iata"), ("code_lid", "faa_lid")):
        if present(a.get(k)):
            o[name] = a[k]
    if present(code) and not m and code not in (a.get("code_icao"), a.get("code_iata"), a.get("code_lid")):
        o["code_as_given"] = code
    for k in ("name", "city", "timezone"):
        if present(a.get(k)):
            o[k] = a[k]
    return o


def sort_key(f):
    for k in ("actual_off", "estimated_off", "scheduled_off", "actual_out", "estimated_out",
              "scheduled_out", "actual_on", "estimated_on", "scheduled_on"):
        if f.get(k):
            return (z(f[k]), f.get("fa_flight_id") or "")
    return (dt.datetime.max.replace(tzinfo=dt.timezone.utc), f.get("fa_flight_id") or "")


def flight(f, n):
    unknown = set(f) - FLIGHT_KEYS
    if unknown:
        raise UnknownField(f"flight fields {sorted(unknown)}")
    o = {"number": n, "flightaware_id": f["fa_flight_id"]}
    for k, name in (("ident", "callsign"), ("ident_icao", "callsign_icao"), ("ident_iata", "callsign_iata"),
                    ("atc_ident", "atc_callsign"), ("registration", "registration"),
                    ("aircraft_type", "aircraft_type_code")):
        if present(f.get(k)):
            o[name] = f[k]
    if present(f.get("type")):
        o["flight_category"] = f["type"].replace("_", " ").lower()
    if present(f.get("status")):
        o["outcome"] = f["status"]
    if f.get("progress_percent") is not None:
        o["progress_percent"] = f["progress_percent"]
    o["flags"] = [k for k in ("blocked", "cancelled", "diverted", "position_only") if f.get(k)]
    for side, key in (("from", "origin"), ("to", "destination")):
        ap = airport(f.get(key))
        if ap:
            o[side] = ap
    for suffix, event in EVENTS:
        tz = ((f.get("origin") if suffix in ("out", "off") else f.get("destination")) or {}).get("timezone")
        ev = {}
        for b in BASES:
            v = f.get(f"{b}_{suffix}")
            if present(v):
                ev[b] = {"utc": v, **({"local": local(v, tz)} if tz else {})}
        runway = {"off": f.get("actual_runway_off"), "on": f.get("actual_runway_on")}.get(suffix)
        if present(runway):
            ev["runway"] = runway
        if ev:
            o[event] = ev
    if f.get("departure_delay") is not None:
        o["departure_versus_schedule"] = delay(f["departure_delay"])
    if f.get("arrival_delay") is not None:
        o["arrival_versus_schedule"] = delay(f["arrival_delay"])
    if f.get("actual_off") and f.get("actual_on"):
        o["airborne_duration"] = hms((z(f["actual_on"]) - z(f["actual_off"])).total_seconds())
    plan = {}
    if f.get("filed_ete") is not None:
        plan["planned_time_enroute"] = hms(f["filed_ete"])
    if f.get("filed_altitude") is not None:
        plan["cruise_altitude_ft"] = f["filed_altitude"] * 100
    if f.get("filed_airspeed") is not None:
        plan["cruise_speed_kt"] = f["filed_airspeed"]
    if present(f.get("route")):
        plan["route_text"] = f["route"]
    if f.get("route_distance") is not None:
        plan["route_distance_mi"] = f["route_distance"]
    if plan:
        o["flight_plan"] = plan
    if present(f.get("inbound_fa_flight_id")):
        o["previous_leg_flightaware_id"] = f["inbound_fa_flight_id"]
    op = {k: f[r] for k, r in (("name", "operator"), ("icao", "operator_icao"), ("iata", "operator_iata")) if present(f.get(r))}
    if op:
        o["operator"] = op
    if present(f.get("flight_number")):
        o["flight_number"] = f["flight_number"]
    for k in ("codeshares", "codeshares_iata"):
        if present(f.get(k)):
            o[k] = list(f[k])
    for side, pairs in (("at_departure", (("gate", "gate_origin"), ("terminal", "terminal_origin"))),
                        ("at_arrival", (("gate", "gate_destination"), ("terminal", "terminal_destination"),
                                        ("baggage_claim", "baggage_claim")))):
        g = {k: f[r] for k, r in pairs if present(f.get(r))}
        if g:
            o[side] = g
    seats = {k: f[f"seats_cabin_{k}"] for k in ("first", "business", "coach") if f.get(f"seats_cabin_{k}") is not None}
    if seats:
        o["cabin_seats"] = seats
    return o


def about(rel, meta):
    return {"aircraft": rel.split("/", 1)[0], "retrieved_utc": meta.get("retrieved_utc"),
            "vendor_http_status": meta.get("http_status")}


def vendor_error(raw, status):
    if status == 200 or not isinstance(raw, dict):
        return None
    e = {k: raw[k] for k in ("title", "reason", "detail", "status") if present(raw.get(k))}
    return e or None


def expected(rel):
    path = os.path.join(RAW, rel)
    meta = json.load(open(path + ".meta.json"))
    text = open(path).read()
    raw = json.loads(text) if text.strip() else {}
    base = rel.split("/", 1)[1]
    m = HISTORY.match(base)
    if m:
        unknown = set(raw) - PAGE_KEYS - {"title", "reason", "detail", "status"}
        if unknown:
            raise UnknownField(f"page fields {sorted(unknown)}")
        a = about(rel, meta)
        a.update({"window_utc_from": f"{m[1]}T00:00:00Z", "window_utc_until_exclusive": f"{m[2]}T00:00:00Z",
                  "result_page": int(m[3]) + 1})
        if raw.get("num_pages") is not None:
            a["total_pages_reported"] = raw["num_pages"]
        a["further_pages_held_by_vendor"] = bool((raw.get("links") or {}).get("next"))
        flights = sorted(raw.get("flights") or [], key=sort_key)
        doc = {"about": a, "flights_recorded": len(flights), "flights": [flight(f, i + 1) for i, f in enumerate(flights)]}
    else:
        kind = PROBE.match(base)[1]
        doc = {"about": about(rel, meta)}
        if kind == "blocked":
            if "blocked" in raw:
                doc["on_display_block_list"] = bool(raw["blocked"])
        else:
            own = raw.get("owner") or {}
            unknown = set(own) - OWNER_KEYS
            if unknown:
                raise UnknownField(f"owner fields {sorted(unknown)}")
            o = {k: own[r] for k, r in (("name", "name"), ("address_line", "location2"),
                                         ("city_state", "location"), ("website", "website")) if present(own.get(r))}
            if o:
                doc["registered_owner"] = o
    err = vendor_error(raw, meta.get("http_status"))
    if err:
        doc["vendor_error"] = err
    return doc


def compare(want, got, path=()):
    """Yield one line per difference. FREE_TEXT paths only need to be non-empty strings."""
    if isinstance(want, dict) and isinstance(got, dict):
        for k in want:
            if k not in got:
                yield f"{'.'.join(map(str, path + (k,)))}: MISSING (expected {want[k]!r})"
            else:
                yield from compare(want[k], got[k], path + (k,))
        for k in got:
            if k in want or path + (k,) in FREE_TEXT:
                continue
            yield f"{'.'.join(map(str, path + (k,)))}: NOT IN THE RAW RESPONSE ({got[k]!r})"
        return
    if isinstance(want, list) and isinstance(got, list):
        if len(want) != len(got):
            yield f"{'.'.join(map(str, path))}: {len(got)} items, expected {len(want)}"
        for i, (w, g) in enumerate(zip(want, got)):
            yield from compare(w, g, path + (i,))
        return
    if path[-2:] == ("registered_owner", "name") and got == WITHHELD_PERSON:
        return
    if want != got or type(want) is not type(got):
        yield f"{'.'.join(map(str, path))}: got {got!r}, expected {want!r}"


def check(rel):
    out = os.path.join(OUT, out_rel(rel))
    if not os.path.exists(out):
        return ["restated file missing: " + os.path.relpath(out, OUT)]
    try:
        got = yaml.safe_load(open(out)) or {}
    except yaml.YAMLError as e:
        return [f"not valid YAML: {e}"]
    try:
        want = expected(rel)
    except UnknownField as e:
        return [f"raw response has {e} this checker does not know - update the prompt and this script together"]
    problems = list(compare(want, got))
    for p in FREE_TEXT:
        node = got
        for k in p:
            node = node.get(k) if isinstance(node, dict) else None
        if not (isinstance(node, str) and node.strip()):
            problems.append(f"{'.'.join(p)}: required free-text sentence missing")
    return problems


def main():
    files = [sys.argv[sys.argv.index("--file") + 1]] if "--file" in sys.argv else list(raw_files())
    todo = "--todo" in sys.argv
    bad = 0
    for rel in files:
        problems = check(rel)
        if problems:
            bad += 1
            if todo:
                print(f"{rel}\t->\t{os.path.join(OUT, out_rel(rel))}")
            else:
                print(f"FAIL {rel}")
                for p in problems[:25]:
                    print(f"     {p}")
                if len(problems) > 25:
                    print(f"     ... and {len(problems) - 25} more")
        elif not todo:
            print(f"ok   {rel}")
    if not todo:
        print(f"{len(files) - bad} of {len(files)} restated files carry every fact and nothing else")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
