"""WHAT IS ACTUALLY INSIDE THE RECOVERED TRACES.

Reads every `*_trace_full.json[.gz]` payload under
    site/docs/Planes/<TAIL>/data/recovered/
and characterises it. NOTHING here touches the network. Nothing here writes to
an evidence file; it only reads and reports.

WHAT THE OUTPUT MEANS, AND WHAT IT DOES NOT
-------------------------------------------
* A trace point is a position a volunteer receiver heard. It proves the airframe
  was there. It proves NOTHING about who was aboard or why.
* A day with no payload is a day an archive was asked and had nothing, or a day
  nobody asked. Neither is evidence the aircraft was elsewhere.
* "Anomaly" below means "worth a human look", never "tampering". Every one of
  the classes flagged here has a boring explanation available first: a receiver
  gap, an aircraft climbing out of coverage, a UTC-midnight file boundary.

TRACE FORMAT (readsb / tar1090 `trace_full`), confirmed against the payloads:
  top level dict:
    icao       lowercase hex, e.g. "01003e"
    r          registration as the archive's database had it, e.g. "SU-BND"
    t          ICAO type code, e.g. "GLF4"
    dbFlags    bitfield: 1 military, 2 interesting, 4 PIA, 8 LADD
    desc       plain-language type, e.g. "GULFSTREAM 4"
    version    the readsb build that wrote it
    timestamp  UNIX seconds for 00:00:00Z of the trace's UTC day
    trace      list of points
  each point is a 14-slot list:
    [0]  seconds after `timestamp`
    [1]  latitude
    [2]  longitude
    [3]  barometric altitude in feet, OR the STRING "ground", OR null
    [4]  ground speed, knots
    [5]  track, degrees
    [6]  flags bitfield (bit0 stale position, bit1 new leg)
    [7]  vertical rate, ft/min
    [8]  aircraft detail object, or null. Present only when something changed.
         keys seen: type, flight, squawk, emergency, category, nic, rc,
         version, nac_p, nac_v, sil, sil_type, sda, alert, spi
    [9]  position source, e.g. "adsb_icao", "mlat", "tisb_trackfile"
    [10] geometric altitude, ft
    [11] geometric vertical rate, ft/min
    [12] indicated airspeed, kt
    [13] roll angle, degrees

Run:
    python3 characterise_traces.py            # summary table + anomalies
    python3 characterise_traces.py --json OUT # machine-readable dump
"""
from __future__ import annotations

import collections
import glob
import gzip
import json
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "lib"))
PLANES_DIR = os.path.normpath(os.path.join(HERE, "..", "..", "..", ".."))

TRACE_RE = re.compile(
    r"^(?P<tail>[A-Z0-9-]+)_(?P<date>\d{4}-\d{2}-\d{2})_(?P<source>[a-z0-9-]+)"
    r"_trace_full\.json(?P<gz>\.gz)?$")

# --- anomaly thresholds. Deliberately loose: a flag is a prompt to look. ---
GAP_AIRBORNE_SEC = 900      # 15 min with no position while airborne
JUMP_KT = 900               # implied ground speed a jet cannot make
EDGE_SEC = 900              # within 15 min of a UTC day boundary = file edge
NOWHERE_ALT_FT = 5000       # first/last point this high, mid-day = dropout
EARTH_KM = 6371.0088

INTERESTING_SQUAWK = {
    "7500": "hijack", "7600": "radio failure", "7700": "general emergency",
    "0000": "non-discrete / unassigned", "7777": "military interceptor (US)",
    "7776": "FAA flight-check", "7777": "military interceptor (US)",
}
DBFLAG = {1: "military", 2: "interesting", 4: "PIA", 8: "LADD"}


def hav_km(a, b, c, d):
    p = math.pi / 180
    x = (math.sin((c - a) * p / 2) ** 2
         + math.cos(a * p) * math.cos(c * p) * math.sin((d - b) * p / 2) ** 2)
    return 2 * EARTH_KM * math.asin(math.sqrt(x))


def payloads():
    paths = (glob.glob(os.path.join(PLANES_DIR, "*", "data", "recovered", "*_trace_full.json"))
             + glob.glob(os.path.join(PLANES_DIR, "*", "data", "recovered", "*_trace_full.json.gz")))
    for path in sorted(paths):
        m = TRACE_RE.match(os.path.basename(path))
        if m:
            yield m.group("tail").upper(), m.group("date"), m.group("source"), path


def load(path):
    opener = gzip.open if path.endswith(".gz") else open
    with opener(path, "rt", encoding="utf-8") as fh:
        return json.load(fh)


def hhmm(sec):
    sec = int(sec)
    return f"{sec // 3600:02d}:{sec % 3600 // 60:02d}:{sec % 60:02d}"


def characterise(tail, day, source, path):
    doc = load(path)
    pts = doc.get("trace") or []
    rec = {
        "tail": tail, "date": day, "source": source,
        "file": os.path.relpath(path, PLANES_DIR),
        "icao": doc.get("icao"), "r": doc.get("r"), "t": doc.get("t"),
        "desc": doc.get("desc"), "dbFlags": doc.get("dbFlags"),
        "version": doc.get("version"), "points": len(pts),
        "ground_points": 0, "air_points": 0, "null_alt_points": 0,
        "squawks": collections.Counter(), "callsigns": collections.Counter(),
        "pos_sources": collections.Counter(), "emergency": collections.Counter(),
        "max_alt": None, "max_gs": None,
        "anomalies": [],
    }
    prev = None          # (t, lat, lon, alt)
    first = last = None
    for p in pts:
        if len(p) < 4:
            continue
        t, lat, lon, alt = p[0], p[1], p[2], p[3]
        src = p[9] if len(p) > 9 else None
        if src:
            rec["pos_sources"][src] += 1
        det = p[8] if len(p) > 8 else None
        if isinstance(det, dict):
            if det.get("squawk"):
                rec["squawks"][det["squawk"]] += 1
            if det.get("flight"):
                rec["callsigns"][det["flight"].strip()] += 1
            if det.get("emergency"):
                rec["emergency"][det["emergency"]] += 1
        if alt == "ground":
            rec["ground_points"] += 1
            a = 0.0
        elif isinstance(alt, (int, float)):
            rec["air_points"] += 1
            a = float(alt)
            rec["max_alt"] = a if rec["max_alt"] is None else max(rec["max_alt"], a)
        else:
            rec["null_alt_points"] += 1
            a = None
        if len(p) > 4 and isinstance(p[4], (int, float)):
            rec["max_gs"] = p[4] if rec["max_gs"] is None else max(rec["max_gs"], p[4])
        if lat is None or lon is None:
            continue
        if first is None:
            first = (t, lat, lon, alt)
        last = (t, lat, lon, alt)
        if prev is not None:
            dt_ = t - prev[0]
            dkm = hav_km(prev[1], prev[2], lat, lon)
            airborne_both = (prev[3] != "ground" and alt != "ground")
            if dt_ > GAP_AIRBORNE_SEC and airborne_both:
                rec["anomalies"].append({
                    "kind": "airborne_gap",
                    "detail": (f"{int(dt_)}s ({dt_/60:.0f} min) with no position while airborne, "
                               f"{hhmm(prev[0])}Z -> {hhmm(t)}Z, aircraft moved {dkm:.0f} km "
                               f"({prev[1]:.3f},{prev[2]:.3f} -> {lat:.3f},{lon:.3f})"),
                    "gap_sec": int(dt_), "km": round(dkm, 1),
                    "from_utc": hhmm(prev[0]), "to_utc": hhmm(t)})
            if 0 < dt_ <= 300:
                kt = (dkm * 0.539957) / (dt_ / 3600.0)
                if kt > JUMP_KT:
                    rec["anomalies"].append({
                        "kind": "position_jump",
                        "detail": (f"{dkm:.1f} km in {dt_:.1f}s = {kt:.0f} kt implied at "
                                   f"{hhmm(prev[0])}Z"),
                        "kt": round(kt), "km": round(dkm, 1), "gap_sec": round(dt_, 1)})
        prev = (t, lat, lon, alt)

    if first:
        rec["first_utc"] = hhmm(first[0])
        rec["last_utc"] = hhmm(last[0])
        rec["first_alt"] = first[3]
        rec["last_alt"] = last[3]
        rec["first_pos"] = [round(first[1], 5), round(first[2], 5)]
        rec["last_pos"] = [round(last[1], 5), round(last[2], 5)]
        # A trace that BEGINS airborne well after midnight, or ENDS airborne well
        # before it, is a receiver-coverage edge, not a file boundary.
        if isinstance(first[3], (int, float)) and first[3] >= NOWHERE_ALT_FT and first[0] > EDGE_SEC:
            rec["anomalies"].append({
                "kind": "starts_airborne_mid_day",
                "detail": (f"first position of the UTC day is at {first[3]:.0f} ft, "
                           f"{hhmm(first[0])}Z, at {first[1]:.3f},{first[2]:.3f} - "
                           f"the aircraft was already flying when it was first heard")})
        if isinstance(last[3], (int, float)) and last[3] >= NOWHERE_ALT_FT and last[0] < 86400 - EDGE_SEC:
            rec["anomalies"].append({
                "kind": "ends_airborne_mid_day",
                "detail": (f"last position of the UTC day is at {last[3]:.0f} ft, "
                           f"{hhmm(last[0])}Z, at {last[1]:.3f},{last[2]:.3f} - "
                           f"the aircraft flew out of receiver coverage")})
    for sq in rec["squawks"]:
        if sq in INTERESTING_SQUAWK:
            rec["anomalies"].append({"kind": "squawk", "detail":
                                     f"squawk {sq} ({INTERESTING_SQUAWK[sq]}) on "
                                     f"{rec['squawks'][sq]} points"})
    for em in rec["emergency"]:
        if em not in ("none", None):
            rec["anomalies"].append({"kind": "emergency_field",
                                     "detail": f"emergency={em} on {rec['emergency'][em]} points"})
    if doc.get("dbFlags"):
        flags = [v for k, v in DBFLAG.items() if doc["dbFlags"] & k]
        rec["anomalies"].append({"kind": "dbflags",
                                 "detail": f"dbFlags={doc['dbFlags']} ({', '.join(flags)})"})
    if rec["r"] and rec["r"].upper().replace("-", "") != tail.replace("-", ""):
        rec["anomalies"].append({"kind": "registration_mismatch",
                                 "detail": f"trace says r={rec['r']!r}, directory says {tail}"})
    rec["squawks"] = dict(rec["squawks"])
    rec["callsigns"] = dict(rec["callsigns"])
    rec["pos_sources"] = dict(rec["pos_sources"])
    rec["emergency"] = dict(rec["emergency"])
    return rec


def main():
    out = []
    for tail, day, source, path in payloads():
        try:
            out.append(characterise(tail, day, source, path))
        except Exception as exc:                      # noqa: BLE001
            out.append({"tail": tail, "date": day, "source": source,
                        "file": os.path.relpath(path, PLANES_DIR),
                        "error": str(exc), "anomalies": [
                            {"kind": "unreadable", "detail": str(exc)}]})
    if "--json" in sys.argv:
        dest = sys.argv[sys.argv.index("--json") + 1]
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w", encoding="utf-8") as fh:
            json.dump(out, fh, indent=1)
        print(f"wrote {len(out)} records -> {dest}")
        return
    by_tail = collections.defaultdict(list)
    for r in out:
        by_tail[r["tail"]].append(r)
    print(f"{'TAIL':18} {'files':>5} {'days':>5}  {'date range':23} "
          f"{'points':>9} {'grnd':>7} {'anom':>5}")
    for tail in sorted(by_tail):
        rs = by_tail[tail]
        days = sorted({r["date"] for r in rs})
        print(f"{tail:18} {len(rs):5} {len(days):5}  "
              f"{days[0]} .. {days[-1]}  "
              f"{sum(r.get('points', 0) for r in rs):9} "
              f"{sum(r.get('ground_points', 0) for r in rs):7} "
              f"{sum(len(r.get('anomalies', [])) for r in rs):5}")


if __name__ == "__main__":
    main()
