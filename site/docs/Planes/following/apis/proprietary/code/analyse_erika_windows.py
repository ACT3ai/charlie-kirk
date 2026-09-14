#!/usr/bin/env python3
"""Turn the AeroAPI history pulls into one verdict per Erika-claimed row.

Reads <private>/flightaware/_erika_plan.json and every <TAIL>/*_history_p*.json beside it.
Writes <private>/flightaware/_erika_verdicts.json and prints a table. <private> is the
private `all` repo (private_store.py): the raw commercial responses are never in this repo.

VERDICTS - about the AIRCRAFT only. Nothing here places any person anywhere.
  AT_FIELD          FlightAware records the tail arriving at or departing the claimed field
                    inside the row's window (claimed date -3 .. +3 days).
  SAME_METRO_OTHER_FIELD  as above, but at another field in the same metro_area (airports.csv).
  FLEW_ELSEWHERE    FlightAware records flights in the window, none touching the claimed field.
  NO_FLIGHT_RECORD  FlightAware records no flight for the tail in the window. Parked, not
                    tracked, or transponder off all look the same. NOT a finding.
A flight "in the window" has its off or on time (else scheduled_out) inside it.

LAST KNOWN / NEXT KNOWN come from every flight pulled for that tail, including other rows'
blocks. They are context, not coverage: a gap between two pulled weeks was never asked about.
"""
import csv, datetime as dt, glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from private_store import private_vendor_dir  # noqa: E402

DATA = private_vendor_dir("flightaware")
FOLLOWING = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(FOLLOWING, "apis", "public_open_source", "code", "lib"))
from geo import nearest_airport, haversine_km  # noqa: E402

# metro_area from the case's own airports table, so KSTL / KSUS / KCPS read as one St Louis.
METRO = {}
for a in csv.DictReader(open(os.path.join(FOLLOWING, "airports.csv"), newline="", encoding="utf-8")):
    if (a.get("metro_area") or "").strip():
        METRO[a["airport_code"].strip().upper()] = a["metro_area"].strip()

COUNTRY = {"HE": "Egypt", "LF": "France", "OJ": "Jordan", "LL": "Israel", "OE": "Saudi Arabia", "LG": "Greece",
           "LI": "Italy", "LE": "Spain", "EG": "UK", "LT": "Turkey", "LC": "Cyprus", "OM": "UAE", "K": "USA", "C": "Canada"}

ISO = {"EG": "Egypt", "US": "USA", "FR": "France", "JO": "Jordan", "IL": "Israel", "SA": "Saudi Arabia"}

def country(ident):
    if not ident:
        return "?"
    # OurAirports local idents ("EG-0058") lead with the ISO COUNTRY code, where "EG" is Egypt.
    # Only real ICAO codes use the ICAO prefix, where "EG" is the UK.
    if "-" in ident:
        return ISO.get(ident.split("-")[0], ident.split("-")[0])
    return COUNTRY.get(ident[:2]) or COUNTRY.get(ident[:1]) or ident[:2]

def resolve(ap):
    """(ident, readable label). Position-only endpoints ("L lat lon") get the nearest field and distance."""
    ap = ap or {}
    c = ap.get("code_icao") or ap.get("code")
    m = re.match(r"^L\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)$", c or "")
    if m:
        lat, lon = float(m.group(1)), float(m.group(2))
        try:
            n = nearest_airport(lat, lon)
            ident = n.get("icao") or n.get("ident")
            km = haversine_km(lat, lon, float(n["lat"]), float(n["lon"]))
            return ident, f"position {lat:.2f},{lon:.2f} ~{km:.0f} km from {ident} {n.get('name')} [{country(ident)}]"
        except Exception:
            return None, f"position {lat:.2f},{lon:.2f}"
    return c, (f"{c} ({ap['name']})" if ap.get("name") else (c or "?")) + (f" [{country(c)}]" if c else "")

def ts(s):
    return dt.datetime.fromisoformat(s.replace("Z", "+00:00")) if s else None

def code(ap):
    ap = ap or {}
    return ap.get("code_icao") or ap.get("code") or None

def label(ap):
    ap = ap or {}
    c = code(ap) or "?"
    return c if not ap.get("name") else f"{c} ({ap['name']})"

PLAN = sys.argv[sys.argv.index("--plan") + 1] if "--plan" in sys.argv else "_erika_plan.json"
OUT_NAME = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else "_erika_verdicts.json"
plan = json.load(open(os.path.join(DATA, PLAN)))
flights = {}
for tail in {t for r in plan["rows"] for t in r["tails"]}:
    seen, out = set(), []
    for f in sorted(glob.glob(os.path.join(DATA, tail, "*_history_p*.json"))):
        if f.endswith(".meta.json"):
            continue
        for x in (json.load(open(f)).get("flights") or []):
            if x.get("fa_flight_id") in seen:
                continue
            seen.add(x.get("fa_flight_id"))
            t_off = ts(x.get("actual_off")) or ts(x.get("scheduled_off")) or ts(x.get("scheduled_out"))
            t_on = ts(x.get("actual_on")) or ts(x.get("scheduled_on")) or ts(x.get("scheduled_in"))
            (o_id, o_lab), (d_id, d_lab) = resolve(x.get("origin")), resolve(x.get("destination"))
            out.append(dict(id=x.get("fa_flight_id"), off=t_off, on=t_on,
                            origin=code(x.get("origin")), dest=code(x.get("destination")),
                            origin_near=o_id, dest_near=d_id,
                            origin_label=o_lab, dest_label=d_lab,
                            status=x.get("status"), position_only=x.get("position_only")))
    flights[tail] = sorted(out, key=lambda r: r["off"] or r["on"] or dt.datetime.min.replace(tzinfo=dt.timezone.utc))

def iso(t):
    return t.strftime("%Y-%m-%d %H:%MZ") if t else "—"

verdicts = []
for r in plan["rows"]:
    ws = dt.datetime.fromisoformat(r["window_start"] + "T00:00:00+00:00")
    we = dt.datetime.fromisoformat(r["window_end"] + "T00:00:00+00:00")
    claim_day = dt.date.fromisoformat(r["date"])
    fields = set(filter(None, re.split(r"[/;, ]+", r["airport_code"])))
    for tail in r["tails"]:
        fl = flights.get(tail, [])
        inwin = [f for f in fl if any(t and ws <= t < we for t in (f["off"], f["on"]))]
        touches = []
        for f in inwin:
            if f["dest"] in fields and f["on"] and ws <= f["on"] < we:
                touches.append(("arrived", f["on"], f))
            if f["origin"] in fields and f["off"] and ws <= f["off"] < we:
                touches.append(("departed", f["off"], f))
        claimed_metros = {METRO[f] for f in fields if f in METRO}
        metro_hits = []
        for f in inwin:
            if f["dest"] in METRO and METRO[f["dest"]] in claimed_metros and f["on"] and ws <= f["on"] < we:
                metro_hits.append(("arrived", f["on"], f))
            if f["origin"] in METRO and METRO[f["origin"]] in claimed_metros and f["off"] and ws <= f["off"] < we:
                metro_hits.append(("departed", f["off"], f))
        if touches:
            verdict = "AT_FIELD"
        elif metro_hits:
            verdict = "SAME_METRO_OTHER_FIELD"
            touches = metro_hits
        elif inwin:
            verdict = "FLEW_ELSEWHERE"
        else:
            verdict = "NO_FLIGHT_RECORD"
        before = [f for f in fl if (f["on"] or f["off"]) and (f["on"] or f["off"]) < ws]
        after = [f for f in fl if (f["off"] or f["on"]) and (f["off"] or f["on"]) >= we]
        lastb, nexta = (before[-1] if before else None), (after[0] if after else None)
        verdicts.append(dict(
            overlap_id=r["overlap_id"], date=r["date"], claimed_field=r["airport_code"], city=r["city"],
            state=r["state"], tail=tail, adsb_verified_verdict=r["adsb_verified_verdict"],
            window=f'{r["window_start"]}..{r["window_end"]} (end exclusive)', aeroapi_verdict=verdict,
            at_field=[dict(event=e, utc=iso(t), day_offset=(t.date() - claim_day).days, fa_flight_id=f["id"],
                           leg=f'{f["origin_label"]} -> {f["dest_label"]}', status=f["status"],
                           position_only=f["position_only"]) for e, t, f in touches],
            flights_in_window=[dict(off=iso(f["off"]), on=iso(f["on"]), leg=f'{f["origin_label"]} -> {f["dest_label"]}',
                                    status=f["status"], position_only=f["position_only"], fa_flight_id=f["id"]) for f in inwin],
            last_known_before=None if not lastb else dict(on=iso(lastb["on"]), at=lastb["dest_label"]),
            next_known_after=None if not nexta else dict(off=iso(nexta["off"]), at=nexta["origin_label"])))

out = dict(built_utc=dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), source="AeroAPI /history/flights, pulled 2026-09-14",
           note="Aircraft only. No verdict here places any person aboard any aircraft or at any place.",
           counts={k: sum(1 for v in verdicts if v["aeroapi_verdict"] == k) for k in ("AT_FIELD", "SAME_METRO_OTHER_FIELD", "FLEW_ELSEWHERE", "NO_FLIGHT_RECORD")},
           verdicts=verdicts)
out["plan"] = PLAN
json.dump(out, open(os.path.join(DATA, OUT_NAME), "w"), indent=1, default=str)
print("counts:", out["counts"], "| rows x tails:", len(verdicts))
for v in verdicts:
    extra = ""
    if v["at_field"]:
        extra = "; ".join(f'{a["event"]} {a["utc"]} (day {a["day_offset"]:+d}) {a["leg"]} [{a["status"]}{", position-only" if a["position_only"] else ""}]' for a in v["at_field"])
    elif v["flights_in_window"]:
        extra = "; ".join(f'{f["off"]} {f["leg"]}' for f in v["flights_in_window"])
    else:
        lb, na = v["last_known_before"], v["next_known_after"]
        extra = f'last known {lb["at"]} {lb["on"]}' if lb else "no earlier pulled flight"
        extra += f' | next known {na["at"]} {na["off"]}' if na else " | no later pulled flight"
    print(f'{v["overlap_id"]:10} {v["date"]} {v["claimed_field"]:15} {v["tail"]:6} {v["aeroapi_verdict"]:17} {extra}')
