#!/usr/bin/env python3
"""Write the FlightAware AeroAPI results into following/overlaps.csv.

Reads the verdicts analyse_erika_windows.py built from the raw AeroAPI pulls (held in the
private `all` repo - see private_store.py) and adds these columns to overlaps.csv.
Columns are only ever ADDED, never removed or reordered, and a re-run rewrites only these.

  aeroapi_verdict            AT_FIELD | SAME_METRO_OTHER_FIELD | FLEW_ELSEWHERE | NO_FLIGHT_RECORD,
                             "TAIL: VERDICT; TAIL: VERDICT" when a row names two tails,
                             or NOT_QUERIED for a row never pulled (no date, or no tail)
  aeroapi_window             the UTC window asked about: the claimed date -3 to +3 days
  aeroapi_at_field           each recorded landing at / takeoff from the claimed field (or,
                             for SAME_METRO_OTHER_FIELD, the other field in the same metro)
  aeroapi_flights_in_window  how many flights FlightAware holds for the tail in the window
  aeroapi_context            the last flight before the window and the first one after it
  aeroapi_vs_adsb            what the FlightAware record does to this row's ADS-B verdict
                             and to the tracking-site audit, in plain words
  aeroapi_restated_files     the published restated files the verdict can be checked against

About the AIRCRAFT only. Nothing here places any person aboard any aircraft.

WHERE AEROAPI AND ADS-B DISAGREE, BOTH COLUMNS KEEP THEIR OWN ANSWER. adsb_verified_verdict
is never rewritten here; aeroapi_vs_adsb says what the disagreement is.

  python3 build_aeroapi_columns.py            write
  python3 build_aeroapi_columns.py --check    print what would be written, write nothing
"""
import csv, datetime as dt, glob, io, json, os, re, sys
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from private_store import private_vendor_dir  # noqa: E402

RAW = private_vendor_dir("flightaware")
CHECKOUT = os.path.normpath(os.path.join(HERE, *[".."] * 7))
OVERLAPS = os.path.normpath(os.path.join(HERE, "..", "..", "..", "overlaps.csv"))
RESTATED = os.path.normpath(os.path.join(HERE, "..", "data", "flightaware_restated"))
VERDICT_FILES = ["_erika_verdicts.json", "_erika_verdicts_decided.json"]

COLUMNS = ["aeroapi_verdict", "aeroapi_window", "aeroapi_at_field", "aeroapi_flights_in_window",
           "aeroapi_context", "aeroapi_vs_adsb", "aeroapi_restated_files"]


def raw_flights():
    """fa_flight_id -> raw flight, for the airport time zones the verdict files do not carry."""
    out = {}
    for f in glob.glob(os.path.join(RAW, "*", "*_history_p*.json")):
        if f.endswith(".meta.json"):
            continue
        for x in (json.load(open(f)).get("flights") or []):
            out.setdefault(x.get("fa_flight_id"), x)
    return out


def local(utc_text, tz):
    """'2024-04-28 17:42Z' -> '13:42 EDT'."""
    if not tz:
        return None
    t = dt.datetime.strptime(utc_text, "%Y-%m-%d %H:%MZ").replace(tzinfo=dt.timezone.utc)
    return t.astimezone(ZoneInfo(tz)).strftime("%H:%M %Z")


def restated_files(tail, window):
    """Restated flight files for the tail whose 7-day block overlaps the row's window."""
    ws, we = window.split(" (")[0].split("..")
    ws, we = dt.date.fromisoformat(ws), dt.date.fromisoformat(we)
    out = []
    for f in sorted(glob.glob(os.path.join(RESTATED, tail, "*_flights_page*.yaml"))):
        m = re.match(r"(\d{4}-\d{2}-\d{2})_to_(\d{4}-\d{2}-\d{2})_", os.path.basename(f))
        s, e = dt.date.fromisoformat(m[1]), dt.date.fromisoformat(m[2])
        if s < we and ws < e:
            out.append(os.path.relpath(f, CHECKOUT))
    return out


def event_text(ev, flights):
    x = flights.get(ev["fa_flight_id"]) or {}
    tz = ((x.get("destination") if ev["event"] == "arrived" else x.get("origin")) or {}).get("timezone")
    lt = local(ev["utc"], tz)
    verb = "landed" if ev["event"] == "arrived" else "took off"
    extra = []
    if ev.get("position_only"):
        extra.append("position-only record")
    extra.append("FlightAware status %s" % ev["status"])
    return "%s %s (%s) on the leg %s, day %+d, %s" % (
        verb, ev["utc"].replace("Z", " UTC"), lt or "local time not recorded", ev["leg"], ev["day_offset"], ", ".join(extra))


def vs_adsb(v, row):
    """What the FlightAware verdict does to the ADS-B verdict and the audit, in words."""
    fa, adsb = v["aeroapi_verdict"], (row.get("adsb_verified_verdict") or "").strip()
    audit = (row.get("audit_verdict") or "").strip().lower()
    km = (row.get("adsb_closest_approach_km") or "").strip()
    try:
        km = format(round(float(km)), ",")
    except ValueError:
        km = km or "an unrecorded number of"
    if fa == "AT_FIELD":
        s = {
            "AT_CLAIMED_AIRPORT": "Agrees with ADS-B: both place the aircraft at the claimed field.",
            "SAME_METRO_WRONG_FIELD": "Upgrades the ADS-B verdict: ADS-B heard it %s km away; FlightAware records it at the claimed field itself." % km,
            "ELSEWHERE": "DISAGREES WITH ADS-B, and FlightAware's record is the stronger one here: ADS-B's closest position was %s km away, but FlightAware records the aircraft at the claimed field. The ADS-B 'elsewhere' verdict is withdrawn as a refutation." % km,
            "NOT_HEARD": "Fills an ADS-B gap: the free receivers did not hear it; FlightAware records it at the claimed field.",
            "NO_ARCHIVE_COVERAGE": "Fills an ADS-B gap: no free archive covers this date; FlightAware records it at the claimed field.",
        }.get(adsb, "FlightAware records it at the claimed field.")
        if audit == "inaccurate":
            s += " Also disagrees with the tracking-site audit, which scored this row inaccurate."
    elif fa == "SAME_METRO_OTHER_FIELD":
        s = {
            "ELSEWHERE": "Partly disagrees with ADS-B: ADS-B puts it %s km away on the claimed day, and FlightAware agrees it was not in the area that day, but records it at another field in the same metro area inside the ±3-day window." % km,
        }.get(adsb, "FlightAware records it at another field in the same metro area, not at the claimed field.")
    elif fa == "FLEW_ELSEWHERE":
        s = {
            "ELSEWHERE": "Agrees with ADS-B: FlightAware records its flights in the window and none touches the claimed field.",
            "AT_CLAIMED_AIRPORT": "DISAGREES WITH ADS-B: ADS-B heard it at the field, but no FlightAware flight in the window touches it. FlightAware can miss a leg; both answers stand.",
        }.get(adsb, "FlightAware records flights for it in the window, and none touches the claimed field. That points away from the claim; FlightAware can miss a leg, so it is not proof on its own.")
        if audit == "accurate":
            s += " Disagrees with the tracking-site audit, which scored this row accurate."
    else:
        s = {
            "AT_CLAIMED_AIRPORT": "Does not contradict ADS-B: ADS-B heard it at the field, and FlightAware simply holds no flight for it in the window. A FlightAware coverage gap, not a disagreement about where it was.",
        }.get(adsb, "No finding either way: FlightAware holds no flight for it in the window.")
    return s


def context_text(v):
    lb, na = v.get("last_known_before"), v.get("next_known_after")
    a = ("last flight before the window landed at %s %s" % (lb["at"], lb["on"].replace("Z", " UTC"))) if lb else "no earlier flight pulled"
    b = ("first flight after it took off from %s %s" % (na["at"], na["off"].replace("Z", " UTC"))) if na else "no later flight pulled"
    return "%s; %s. Only the weeks that were pulled are known - a gap between them was never asked about." % (a, b)


def main():
    check = "--check" in sys.argv
    verdicts = {}
    for name in VERDICT_FILES:
        for v in json.load(open(os.path.join(RAW, name)))["verdicts"]:
            verdicts.setdefault(v["overlap_id"], []).append(v)
    flights = raw_flights()

    raw = open(OVERLAPS, "rb").read().decode("utf-8")
    table = list(csv.reader(io.StringIO(raw, newline="")))
    header, rows = table[0], table[1:]
    for c in COLUMNS:
        if c not in header:
            header.append(c)
    idx = {c: i for i, c in enumerate(header)}
    for r in rows:
        r.extend([""] * (len(header) - len(r)))

    counts = {}
    for r in rows:
        row = dict(zip(header, r))
        vs = verdicts.get(row["overlap_id"])
        if not vs:
            values = {"aeroapi_verdict": "NOT_QUERIED"}
        else:
            multi = len(vs) > 1
            tag = (lambda v, s: "%s: %s" % (v["tail"], s)) if multi else (lambda v, s: s)
            values = {
                "aeroapi_verdict": "; ".join(tag(v, v["aeroapi_verdict"]) for v in vs),
                "aeroapi_window": "%s to %s UTC, end exclusive" % tuple(vs[0]["window"].split(" (")[0].split("..")),
                "aeroapi_at_field": "; ".join(tag(v, " | ".join(event_text(e, flights) for e in v["at_field"])) for v in vs if v["at_field"]),
                "aeroapi_flights_in_window": "; ".join(tag(v, str(len(v["flights_in_window"]))) for v in vs),
                "aeroapi_context": "; ".join(tag(v, context_text(v)) for v in vs),
                "aeroapi_vs_adsb": " ".join(tag(v, vs_adsb(v, row)) for v in vs),
                "aeroapi_restated_files": ";".join(sorted({f for v in vs for f in restated_files(v["tail"], v["window"])})),
            }
        for c in COLUMNS:
            r[idx[c]] = values.get(c, "")
        counts[r[idx["aeroapi_verdict"]]] = counts.get(r[idx["aeroapi_verdict"]], 0) + 1
        if check and vs:
            print("%-10s %-40s %s" % (row["overlap_id"], r[idx["aeroapi_verdict"]], r[idx["aeroapi_vs_adsb"]][:110]))

    for k in sorted(counts):
        print("  %4d  %s" % (counts[k], k))
    if check:
        return
    buf = io.StringIO(newline="")
    csv.writer(buf, lineterminator="\r\n").writerows([header] + rows)
    open(OVERLAPS, "wb").write(buf.getvalue().encode("utf-8"))
    print("wrote", os.path.relpath(OVERLAPS, CHECKOUT))


if __name__ == "__main__":
    main()
