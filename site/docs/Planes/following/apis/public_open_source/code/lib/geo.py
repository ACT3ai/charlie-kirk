"""Airport geometry for the following-planes investigation.

WHAT THIS IS AND IS NOT
-----------------------
This module answers exactly two geometric questions:

  1. Where is this city / this airport?
  2. Which airports sit within N miles of that point?

It does NOT answer "did an aircraft land here". Distance to a runway is
distance to a runway. The Provo-versus-Dugway mislabel this investigation
already had to correct is what happens when a nearest-field label is read as a
destination, so every function here returns the DISTANCE alongside the name and
no caller may drop it.

DATA SOURCES, all public-domain or open, all cached under ../data/:
  * OurAirports airports.csv + runways.csv (CC0)     ~85,000 fields worldwide
  * US Census 2024 Gazetteer, places national file   ~32,000 US places

Refresh them with:
    node ourairports.js                              (airports + runways)
    see p_airports_near.md STAGE 1 for the gazetteer curl
"""
from __future__ import annotations

import csv
import math
import os
import re
import sys
from functools import lru_cache

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(HERE, "..", "..", "data"))
AIRPORTS_CSV = os.path.join(DATA, "ourairports", "airports.csv")
RUNWAYS_CSV = os.path.join(DATA, "ourairports", "runways.csv")
GAZ_TXT = os.path.join(DATA, "gazetteer", "2024_Gaz_place_national.txt")

# Heliports, seaplane bases, balloonports and closed fields are dropped: a
# private jet cannot use any of them. Everything else is kept, INCLUDING every
# `small_airport` with no scheduled service — those grass-and-windsock fields
# are the whole point of the 40-mile sweep.
SKIP_TYPES = {"closed", "heliport", "seaplane_base", "balloonport"}

MI_PER_KM = 0.621371
EARTH_KM = 6371.0088

# Runway length a business jet realistically needs. These are ROUGH PLANNING
# NUMBERS for classifying a field, not performance data for any specific type.
# A Falcon 7X or G550 at weight wants ~5,000 ft; light jets get in and out of
# 4,000 ft; below 3,000 ft is piston/turboprop country.
JET_RUNWAY_FT = 5000
LIGHT_JET_RUNWAY_FT = 4000
MIN_PAVED_FT = 3000


def haversine_km(lat1, lon1, lat2, lon2):
    p = math.pi / 180
    a = (math.sin((lat2 - lat1) * p / 2) ** 2
         + math.cos(lat1 * p) * math.cos(lat2 * p) * math.sin((lon2 - lon1) * p / 2) ** 2)
    return 2 * EARTH_KM * math.asin(math.sqrt(a))


def haversine_mi(lat1, lon1, lat2, lon2):
    return haversine_km(lat1, lon1, lat2, lon2) * MI_PER_KM


def bearing_deg(lat1, lon1, lat2, lon2):
    p = math.pi / 180
    y = math.sin((lon2 - lon1) * p) * math.cos(lat2 * p)
    x = (math.cos(lat1 * p) * math.sin(lat2 * p)
         - math.sin(lat1 * p) * math.cos(lat2 * p) * math.cos((lon2 - lon1) * p))
    return (math.degrees(math.atan2(y, x)) + 360) % 360


_COMPASS = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
            "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]


def compass(deg):
    return _COMPASS[int((deg + 11.25) % 360 // 22.5)]


# --------------------------------------------------------------------------
# Airports
# --------------------------------------------------------------------------

@lru_cache(maxsize=1)
def _runway_index():
    """airport_ident -> {longest_ft, longest_surface, paved, count, lighted}."""
    idx = {}
    if not os.path.exists(RUNWAYS_CSV):
        return idx
    with open(RUNWAYS_CSV, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            if r.get("closed") == "1":
                continue
            ident = (r.get("airport_ident") or "").strip()
            if not ident:
                continue
            try:
                ln = int(float(r.get("length_ft") or 0))
            except ValueError:
                ln = 0
            surf = (r.get("surface") or "").strip().upper()
            e = idx.setdefault(ident, {"longest_ft": 0, "longest_surface": "",
                                       "runway_count": 0, "lighted": False})
            e["runway_count"] += 1
            if r.get("lighted") == "1":
                e["lighted"] = True
            if ln > e["longest_ft"]:
                e["longest_ft"] = ln
                e["longest_surface"] = surf
    for e in idx.values():
        s = e["longest_surface"]
        e["paved"] = bool(re.search(r"ASP|CON|PEM|BIT|TAR|PAVED", s))
    return idx


def jet_capability(longest_ft, paved):
    """A four-way classification, deliberately coarse and deliberately labelled.

    Returns one of: jet_capable / light_jet_capable / marginal / not_jet_capable
    plus `unknown` when OurAirports publishes no runway row for the field.
    """
    if not longest_ft:
        return "unknown"
    if longest_ft >= JET_RUNWAY_FT and paved:
        return "jet_capable"
    if longest_ft >= LIGHT_JET_RUNWAY_FT and paved:
        return "light_jet_capable"
    if longest_ft >= MIN_PAVED_FT and paved:
        return "marginal"
    return "not_jet_capable"


@lru_cache(maxsize=1)
def load_airports():
    """Every usable field on earth, as a list of dicts sorted by latitude."""
    rw = _runway_index()
    out = []
    with open(AIRPORTS_CSV, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            if r["type"] in SKIP_TYPES:
                continue
            try:
                lat = float(r["latitude_deg"])
                lon = float(r["longitude_deg"])
            except (TypeError, ValueError):
                continue
            ident = r["ident"].strip()
            runway = rw.get(ident, {})
            longest = runway.get("longest_ft", 0)
            paved = runway.get("paved", False)
            out.append({
                "ident": ident,
                "icao": (r.get("icao_code") or "").strip() or None,
                "iata": (r.get("iata_code") or "").strip() or None,
                "local_code": (r.get("local_code") or "").strip() or None,
                "name": r["name"],
                "type": r["type"],
                "lat": lat,
                "lon": lon,
                "elevation_ft": r.get("elevation_ft") or None,
                "municipality": (r.get("municipality") or "").strip() or None,
                "iso_region": r.get("iso_region"),
                "iso_country": r.get("iso_country"),
                "scheduled_service": r.get("scheduled_service") == "yes",
                "longest_runway_ft": longest or None,
                "longest_runway_surface": runway.get("longest_surface") or None,
                "runway_count": runway.get("runway_count", 0),
                "runways_lighted": runway.get("lighted", False),
                "jet_capability": jet_capability(longest, paved),
            })
    out.sort(key=lambda a: a["lat"])
    return out


@lru_cache(maxsize=1)
def _by_code():
    m = {}
    for a in load_airports():
        for k in (a["ident"], a["icao"], a["local_code"]):
            if k:
                m.setdefault(k.upper(), a)
    for a in load_airports():          # IATA last: three-letter codes are reused
        if a["iata"]:
            m.setdefault(a["iata"].upper(), a)
    return m


def airport_by_code(code):
    if not code:
        return None
    return _by_code().get(str(code).strip().upper())


def _lat_window(lat, pad_deg):
    """Binary-search the latitude-sorted list; returns the slice bounds."""
    a = load_airports()
    lo, hi = 0, len(a)
    lo_target = lat - pad_deg
    while lo < hi:
        m = (lo + hi) // 2
        if a[m]["lat"] < lo_target:
            lo = m + 1
        else:
            hi = m
    return a, lo


def airports_within(lat, lon, radius_mi, include_types=None):
    """Every field within radius_mi of a point, nearest first, distance attached."""
    pad = radius_mi / 69.0 + 0.05
    a, start = _lat_window(lat, pad)
    hits = []
    for i in range(start, len(a)):
        ap = a[i]
        if ap["lat"] > lat + pad:
            break
        if include_types and ap["type"] not in include_types:
            continue
        d = haversine_mi(lat, lon, ap["lat"], ap["lon"])
        if d <= radius_mi:
            b = bearing_deg(lat, lon, ap["lat"], ap["lon"])
            hits.append(dict(ap, distance_mi=round(d, 1),
                             bearing_deg=round(b), bearing=compass(b)))
    hits.sort(key=lambda x: x["distance_mi"])
    return hits


def nearest_airport(lat, lon, radius_mi=60, predicate=None):
    for ap in airports_within(lat, lon, radius_mi):
        if predicate is None or predicate(ap):
            return ap
    return None


# --------------------------------------------------------------------------
# Geocoding a city
# --------------------------------------------------------------------------

_SUFFIX = re.compile(
    r"\s+(city|town|village|borough|CDP|municipality|"
    r"consolidated government|metro government|metropolitan government|"
    r"unified government|urban county|corporation|comunidad|zona urbana)"
    r"(\s+\(balance\))?$", re.I)


@lru_cache(maxsize=1)
def _gazetteer():
    """(STATE, normalised place name) -> (lat, lon, official name)."""
    idx = {}
    if not os.path.exists(GAZ_TXT):
        return idx
    with open(GAZ_TXT, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            r = {k.strip(): (v.strip() if isinstance(v, str) else v) for k, v in r.items()}
            try:
                lat, lon = float(r["INTPTLAT"]), float(r["INTPTLONG"])
            except (KeyError, TypeError, ValueError):
                continue
            name = r["NAME"]
            key = (r["USPS"].upper(), _SUFFIX.sub("", name).strip().upper())
            # Prefer the largest-land-area match when a state repeats a name.
            try:
                area = float(r.get("ALAND") or 0)
            except ValueError:
                area = 0
            prev = idx.get(key)
            if prev is None or area > prev[3]:
                idx[key] = (lat, lon, name, area)
    return idx


# Cities this investigation touches that the US Census file cannot answer.
# Each one is a deliberate hand entry, and the source is stated because a
# hand-entered coordinate is a claim like any other.
MANUAL_PLACES = {
    ("SEOUL", "", "SOUTH KOREA"): (37.5665, 126.9780, "Seoul, Republic of Korea (city hall)"),
    ("TOKYO", "", "JAPAN"): (35.6895, 139.6917, "Tokyo, Japan (metropolitan government)"),
}


def geocode_place(city, state, country="USA"):
    """Return {lat, lon, method, matched} or None. NEVER guesses."""
    if not city or city.upper() in ("UNKNOWN", "AMBIGUOUS", ""):
        return None
    c = city.strip().upper()
    st = (state or "").strip().upper()
    ctry = (country or "").strip().upper()

    man = MANUAL_PLACES.get((c, st, ctry))
    if man:
        return {"lat": man[0], "lon": man[1], "method": "manual_table",
                "matched": man[2]}

    if ctry in ("USA", "US", "UNITED STATES") and st:
        hit = _gazetteer().get((st, _SUFFIX.sub("", c).strip()))
        if hit:
            return {"lat": hit[0], "lon": hit[1],
                    "method": "us_census_2024_gazetteer", "matched": hit[2]}

    # Fallback: the centroid of every OurAirports field whose municipality is
    # this city in this region. Weaker, and it says so in `method`.
    cands = [a for a in load_airports()
             if a["municipality"] and a["municipality"].strip().upper() == c
             and (not st or (a["iso_region"] or "").upper().endswith("-" + st))]
    if cands:
        return {"lat": sum(a["lat"] for a in cands) / len(cands),
                "lon": sum(a["lon"] for a in cands) / len(cands),
                "method": "ourairports_municipality_centroid",
                "matched": f"{len(cands)} field(s) whose municipality is {city}"}
    return None


# --------------------------------------------------------------------------
# Time zones
# --------------------------------------------------------------------------

_TF = None
_TF_TRIED = False

# Fallback only, and a lossy one: several of these states straddle two zones.
# Used ONLY when timezonefinder is not installed, and the caller is told so.
_STATE_TZ = {
    "AL": "America/Chicago", "AK": "America/Anchorage", "AZ": "America/Phoenix",
    "AR": "America/Chicago", "CA": "America/Los_Angeles", "CO": "America/Denver",
    "CT": "America/New_York", "DE": "America/New_York", "DC": "America/New_York",
    "FL": "America/New_York", "GA": "America/New_York", "HI": "Pacific/Honolulu",
    "ID": "America/Boise", "IL": "America/Chicago", "IN": "America/Indiana/Indianapolis",
    "IA": "America/Chicago", "KS": "America/Chicago", "KY": "America/New_York",
    "LA": "America/Chicago", "ME": "America/New_York", "MD": "America/New_York",
    "MA": "America/New_York", "MI": "America/Detroit", "MN": "America/Chicago",
    "MS": "America/Chicago", "MO": "America/Chicago", "MT": "America/Denver",
    "NE": "America/Chicago", "NV": "America/Los_Angeles", "NH": "America/New_York",
    "NJ": "America/New_York", "NM": "America/Denver", "NY": "America/New_York",
    "NC": "America/New_York", "ND": "America/Chicago", "OH": "America/New_York",
    "OK": "America/Chicago", "OR": "America/Los_Angeles", "PA": "America/New_York",
    "RI": "America/New_York", "SC": "America/New_York", "SD": "America/Chicago",
    "TN": "America/Chicago", "TX": "America/Chicago", "UT": "America/Denver",
    "VT": "America/New_York", "VA": "America/New_York", "WA": "America/Los_Angeles",
    "WV": "America/New_York", "WI": "America/Chicago", "WY": "America/Denver",
}


def timezone_at(lat, lon, state=None):
    """Return (tz_name, method). Method names the weaker route when it is used."""
    global _TF, _TF_TRIED
    if not _TF_TRIED:
        _TF_TRIED = True
        try:
            from timezonefinder import TimezoneFinder
            _TF = TimezoneFinder()
        except ImportError:
            _TF = None
    if _TF is not None:
        tz = _TF.timezone_at(lat=lat, lng=lon)
        if tz:
            return tz, "timezonefinder"
    if state and state.upper() in _STATE_TZ:
        return _STATE_TZ[state.upper()], "state_table_APPROXIMATE"
    return None, "unresolved"


if __name__ == "__main__":
    lat, lon = 40.2192, -111.7233
    print("airports within 40 mi of Orem UT:")
    for a in airports_within(lat, lon, 40):
        print(f"  {a['ident']:6} {a['distance_mi']:5.1f}mi {a['bearing']:>3} "
              f"{a['type']:14} {str(a['longest_runway_ft']):>6}ft "
              f"{a['jet_capability']:18} {a['name']}")
    print(geocode_place("Orem", "UT"), timezone_at(lat, lon, "UT"), file=sys.stderr)
