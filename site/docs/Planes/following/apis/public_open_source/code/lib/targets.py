"""The target set for the geographic sweep: WHICH CIRCLE, ON WHICH UTC DAY.

The per-tail archive probing this repo has done until now can only answer
"was THIS aircraft here" for a tail somebody already suspected. It holds ~9%
of the aircraft-days the speaking-event windows need, and it can never find an
aircraft nobody thought to name.

This module builds the input to the other question -- "WHAT WAS HERE" -- by
turning each sourced speaking event into a circle on the map and a set of UTC
dates. Everything inside the circle, on those days, gets looked at, whoever it
turns out to be.

THE THREE HONESTY RULES BAKED INTO THE OUTPUT, none of which may be edited out:

  * THE CIRCLE IS A CIRCLE, NOT AN AIRPORT. A 50-mile radius around a city
    centroid contains every field within 50 miles of that city, which is the
    point -- but a hit inside it is a position, not a landing and not a
    destination. `nearest airport` is resolved later, WITH the distance
    attached, by lib/traces.py.

  * THE CITY CENTROID IS THE US CENSUS INTERNAL POINT, not the venue. Most of
    these events have no published venue address, and where one exists it is
    still miles from any runway. The centroid is a defensible, reproducible
    anchor and is labelled as one in `center_basis`.

  * A CONTROL CIRCLE IS PART OF THE SET, NOT AN AFTERTHOUGHT. Every sweep also
    covers cities with NO connection to this case on the SAME days. Without
    that, "six foreign-registered jets were within 50 miles" is a number with
    nothing to compare it to, and this investigation has already had to retract
    one finding for exactly that reason.
"""
from __future__ import annotations

import csv
import datetime as dt
import os
import re

from geo import geocode_place

HERE = os.path.dirname(os.path.abspath(__file__))
FOLLOWING = os.path.normpath(os.path.join(HERE, "..", "..", "..", ".."))
EVENTS_CSV = os.path.join(FOLLOWING, "tpusa_events.csv")

# The free daily archive on GitHub starts here. 2022 has NO daily archive at
# all -- the only free route into 2022 is the ADS-B Exchange monthly sample,
# which is one day in thirty and cannot be swept geographically.
ARCHIVE_FLOOR = dt.date(2023, 1, 1)

ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
# "2022-06-02 to 2022-06-04" -- the multi-day conferences (AmericaFest, Student
# Action Summit, SAS). Every day in the range is a real, named day and all of
# them get swept. A range is NOT an undated row.
ISO_RANGE = re.compile(r"^(\d{4}-\d{2}-\d{2})\s*(?:to|-|–|through)\s*(\d{4}-\d{2}-\d{2})$", re.I)

# Control cities: no TPUSA/Kirk event on any date in this study, spread across
# the country and across airport sizes. They are NOT traffic-matched to the
# event cities and the output says so -- a control that is merely "somewhere
# else" still answers the question that matters most here, which is whether a
# foreign-registered jet inside a 50-mile circle is unusual at all.
CONTROL_CITIES = [
    ("Des Moines", "IA"),
    ("Chattanooga", "TN"),
    ("Spokane", "WA"),
    ("Albuquerque", "NM"),
    ("Syracuse", "NY"),
    ("Shreveport", "LA"),
]


def _parse_date(s):
    s = (s or "").strip()
    return dt.date.fromisoformat(s) if ISO_DATE.match(s) else None


def _parse_dates(s):
    """Every exact day a row names. One for a plain date, N for a range, none
    for a row that names only a month. Returns (days, basis)."""
    s = (s or "").strip()
    if ISO_DATE.match(s):
        return [dt.date.fromisoformat(s)], "exact_date"
    m = ISO_RANGE.match(s)
    if m:
        a, b = dt.date.fromisoformat(m.group(1)), dt.date.fromisoformat(m.group(2))
        if a <= b and (b - a).days <= 14:
            return [a + dt.timedelta(days=i) for i in range((b - a).days + 1)], "date_range"
    return [], "no_exact_date"


def load_events(radius_mi=50.0):
    """Every US speaking event we can put on the map, as a circle.

    Rows whose date is a month ("2023-05 (month)") or otherwise not an exact
    ISO date are RETURNED SEPARATELY as `undated`, never silently dropped and
    never guessed at. A sweep cannot ask about a day nobody has named.
    """
    events, undated, ungeocoded = [], [], []
    with open(EVENTS_CSV, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            if (r.get("country") or "").strip().upper() not in ("USA", "US", "UNITED STATES"):
                continue
            days, basis = _parse_dates(r.get("dates"))
            if not days:
                undated.append(r)
                continue
            g = geocode_place(r.get("city"), r.get("state"), r.get("country"))
            if not g:
                ungeocoded.append(r)
                continue
            for d in days:
                events.append({
                "key": f"{d:%Y%m%d}_{re.sub(r'[^a-z0-9]+', '_', (r.get('city') or '').lower()).strip('_')}",
                "date": d.isoformat(),
                "date_basis": basis,
                "date_as_published": (r.get("dates") or "").strip(),
                "city": r.get("city"),
                "state": r.get("state"),
                "who": r.get("who"),
                "title": r.get("title"),
                "venue": r.get("university_or_venue"),
                "nearest_airport_code": r.get("nearest_airport_code"),
                "mdx_page": r.get("mdx_page"),
                "lat": g["lat"],
                "lon": g["lon"],
                "radius_mi": radius_mi,
                "center_basis": g["method"],
                "center_matched": g["matched"],
                "kind": "event",
                })
    return events, undated, ungeocoded


def build_targets(radius_mi=50.0, window_days=1, controls=True):
    """UTC date -> list of circles to look inside on that date.

    `window_days` widens each event to date-N .. date+N. An aircraft that
    arrived the evening before or left the morning after is the whole shape of
    the claim being tested, and a UTC day boundary sits in the middle of the
    US evening, so a window of at least 1 is not optional.
    """
    events, undated, ungeocoded = load_events(radius_mi)
    by_date = {}
    for e in events:
        d0 = dt.date.fromisoformat(e["date"])
        for k in range(-window_days, window_days + 1):
            d = d0 + dt.timedelta(days=k)
            if d < ARCHIVE_FLOOR:
                continue
            c = dict(e, offset_days=k, sweep_date=d.isoformat())
            by_date.setdefault(d.isoformat(), []).append(c)

    if controls:
        ctrl = []
        for city, st in CONTROL_CITIES:
            g = geocode_place(city, st, "USA")
            if g:
                ctrl.append({"key": f"control_{city.lower().replace(' ', '_')}",
                             "city": city, "state": st, "lat": g["lat"], "lon": g["lon"],
                             "radius_mi": radius_mi, "center_basis": g["method"],
                             "center_matched": g["matched"], "kind": "control",
                             "who": "CONTROL — no known Kirk/TPUSA event",
                             "offset_days": 0})
        for d in list(by_date):
            for c in ctrl:
                by_date[d].append(dict(c, sweep_date=d))

    return by_date, {"events": events, "undated": undated, "ungeocoded": ungeocoded,
                     "radius_mi": radius_mi, "window_days": window_days,
                     "controls": CONTROL_CITIES if controls else [],
                     "archive_floor": ARCHIVE_FLOOR.isoformat()}


def priority(by_date, meta):
    """Sweep order. Bandwidth is the only real cost here, so spend it on the
    days that decide something first: the assassination window, then the days
    an overlap was actually CLAIMED, then everything else newest-first."""
    claimed = set()
    ov = os.path.join(FOLLOWING, "overlaps.csv")
    if os.path.exists(ov):
        with open(ov, newline="", encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                for k in ("date", "dates", "overlap_date"):
                    d = _parse_date(r.get(k))
                    if d:
                        claimed.add(d.isoformat())

    def rank(d):
        if "2025-09-08" <= d <= "2025-09-12":
            return (0, d)
        if d in claimed:
            return (1, d)
        return (2, "9999" if d is None else d[::-1])

    return sorted(by_date, key=rank)


if __name__ == "__main__":
    import json
    by_date, meta = build_targets()
    print(f"{len(meta['events'])} US events on the map, "
          f"{len(meta['undated'])} with no exact date, "
          f"{len(meta['ungeocoded'])} not geocodable")
    print(f"{len(by_date)} UTC dates to sweep at radius {meta['radius_mi']} mi, "
          f"window +/-{meta['window_days']} d")
    for d in priority(by_date, meta)[:12]:
        ev = [c for c in by_date[d] if c["kind"] == "event"]
        print(f"  {d}  {len(ev)} event circle(s): "
              + ", ".join(f"{c['city']},{c['state']}" for c in ev))
    for r in meta["undated"]:
        print(f"  NO EXACT DATE, not swept: {r['dates']!r} {r['city']}, {r['state']}")
    for r in meta["ungeocoded"]:
        print(f"  NOT GEOCODABLE, not swept: {r['city']!r}, {r['state']}")
