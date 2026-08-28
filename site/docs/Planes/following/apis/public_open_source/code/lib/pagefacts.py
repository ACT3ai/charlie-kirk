#!/usr/bin/env python3
"""
pagefacts.py — shared fact resolution for the page generators.

Airport identity, date maths, and MDX-safe cells.  Everything here is derived
from files already in the repository; nothing makes a network call.
"""

import csv
import datetime
import os
import re

ROOT = os.path.expanduser("~/BGit/Bryan_git/charlie-kirk")
PLANES = os.path.join(ROOT, "site/docs/Planes")
FOLLOWING = os.path.join(PLANES, "following")
ANALYSIS = os.path.join(FOLLOWING, "apis/public_open_source/data/analysis")

# ICAO first-two-letter block -> country.  Only the blocks that actually occur
# in this investigation's recovered legs are listed; an unknown block renders as
# the raw code rather than a guess.
ICAO_COUNTRY = {
    "K": "USA", "PA": "USA", "PH": "USA (Hawaii)", "PG": "USA (Guam)",
    "CY": "Canada", "CL": "Canada", "CE": "Canada",
    "MM": "Mexico",
    "HE": "Egypt", "HL": "Libya", "HS": "Sudan",
    "LF": "France", "LI": "Italy", "LE": "Spain", "GC": "Spain (Canaries)",
    "ED": "Germany", "ET": "Germany", "DE": "Germany",
    "EG": "United Kingdom", "EI": "Ireland", "EH": "Netherlands",
    "EB": "Belgium", "EL": "Luxembourg", "EK": "Denmark", "EN": "Norway",
    "ES": "Sweden", "EF": "Finland", "EE": "Estonia", "EV": "Latvia",
    "EY": "Lithuania", "EP": "Poland", "LK": "Czechia", "LZ": "Slovakia",
    "LH": "Hungary", "LO": "Austria", "LS": "Switzerland",
    "LG": "Greece", "LT": "Turkey", "LC": "Cyprus", "LB": "Bulgaria",
    "LR": "Romania", "LY": "Serbia", "LQ": "Bosnia", "LD": "Croatia",
    "LJ": "Slovenia", "LM": "Malta", "LA": "Albania", "LW": "North Macedonia",
    "LP": "Portugal", "LL": "Israel", "LU": "Moldova", "LN": "Monaco",
    "OM": "United Arab Emirates", "OE": "Saudi Arabia", "OB": "Bahrain",
    "OK": "Kuwait", "OT": "Qatar", "OJ": "Jordan", "OL": "Lebanon",
    "OS": "Syria", "OI": "Iran", "OR": "Iraq",
    "DA": "Algeria", "DT": "Tunisia", "GM": "Morocco",
    "RJ": "Japan", "RK": "South Korea", "VH": "Hong Kong",
    "SA": "Argentina", "SB": "Brazil", "SW": "Brazil",
    "YM": "Australia", "NZ": "New Zealand",
    "UK": "Ukraine", "UU": "Russia",
}

# US airports carrying no state in airports.csv.  Written out by hand so a wrong
# one is a visible edit rather than a silent default.
US_FALLBACK = {
    "KAGC": ("West Mifflin", "PA"), "KAPA": ("Englewood", "CO"),
    "KCRQ": ("Carlsbad", "CA"), "KDVT": ("Phoenix", "AZ"),
    "KEUG": ("Eugene", "OR"), "KHHR": ("Hawthorne", "CA"),
    "KLAL": ("Lakeland", "FL"), "KLGB": ("Long Beach", "CA"),
    "KLZU": ("Lawrenceville", "GA"), "KSDL": ("Scottsdale", "AZ"),
    "KSNA": ("Santa Ana", "CA"), "KVNY": ("Los Angeles", "CA"),
    "KBIF": ("El Paso", "TX"), "KGPI": ("Kalispell", "MT"),
    "KHII": ("Lake Havasu City", "AZ"), "KSNS": ("Salinas", "CA"),
    "KPVU": ("Provo", "UT"), "KILG": ("Wilmington", "DE"),
    "KMOT": ("Minot", "ND"), "KSLC": ("Salt Lake City", "UT"),
    "KLNK": ("Lincoln", "NE"), "KICT": ("Wichita", "KS"),
    "KOMA": ("Omaha", "NE"), "KXWA": ("Williston", "ND"),
    "KSTL": ("St. Louis", "MO"), "KCPS": ("Cahokia", "IL"),
    "KDTW": ("Detroit", "MI"), "KJFK": ("New York", "NY"),
    "KIAD": ("Washington", "DC"), "KSJC": ("San Jose", "CA"),
    "KABQ": ("Albuquerque", "NM"), "KDAL": ("Dallas", "TX"),
    "KDFW": ("Dallas-Fort Worth", "TX"), "KPHX": ("Phoenix", "AZ"),
    "KMSN": ("Madison", "WI"), "KSAN": ("San Diego", "CA"),
}

_AIRPORTS = None


def airports():
    global _AIRPORTS
    if _AIRPORTS is None:
        _AIRPORTS = {}
        p = os.path.join(FOLLOWING, "airports.csv")
        if os.path.exists(p):
            with open(p, newline="", encoding="utf-8") as fh:
                for r in csv.DictReader(fh):
                    _AIRPORTS[r["airport_code"]] = r
    return _AIRPORTS


def place(code, name_hint=""):
    """
    (display_name, 'City, ST' or 'City, Country') for an airport code.
    Never invents a state it does not hold; falls back to the country block,
    then to the bare code.
    """
    code = (code or "").strip()
    if not code:
        return ("—", "—")
    a = airports().get(code)
    name = (a or {}).get("airport_name", "") or (name_hint or "")
    city = (a or {}).get("city", "")
    state = (a or {}).get("state", "")
    country = (a or {}).get("country", "")

    if code in US_FALLBACK:
        fc, fs = US_FALLBACK[code]
        city = city or fc
        state = state or fs
        country = country or "USA"

    if not country:
        for n in (2, 1):
            if code[:n] in ICAO_COUNTRY:
                country = ICAO_COUNTRY[code[:n]]
                break

    if city and state:
        where = f"{city}, {state}"
    elif city and country and country != "USA":
        where = f"{city}, {country}"
    elif city:
        where = city
    elif country:
        where = country
    else:
        where = "—"
    return (name or code, where)


def country(code):
    """Country for an airport code, from airports.csv then the ICAO block."""
    code = (code or "").strip()
    if not code:
        return ""
    a = airports().get(code) or {}
    c = (a.get("country") or "").strip()
    if c:
        return c
    if code in US_FALLBACK:
        return "USA"
    for n in (2, 1):
        if code[:n] in ICAO_COUNTRY:
            return ICAO_COUNTRY[code[:n]]
    return ""


def hhmm(ts):
    m = re.search(r"T(\d{2}):(\d{2})", ts or "")
    return f"{m.group(1)}:{m.group(2)}" if m else ""


def window(first, last):
    a, b = hhmm(first), hhmm(last)
    if not a:
        return "—"
    if not b or a == b:
        return f"{a} only"
    return f"{a}–{b}"


def days_between(a, b):
    """a - b, in days, from ISO date strings.  None if either will not parse."""
    try:
        return (datetime.date.fromisoformat(a) - datetime.date.fromisoformat(b)).days
    except (TypeError, ValueError):
        return None


def when_label(n):
    if n is None:
        return "—"
    if n == 0:
        return "**Same day**"
    if n == -1:
        return "Day before"
    if n == 1:
        return "Day after"
    return f"{abs(n)} days {'before' if n < 0 else 'after'}"


def esc(s):
    """Safe inside a markdown table cell and inside MDX."""
    s = (s or "").replace("|", "\\|")
    s = s.replace("{", "&#123;").replace("}", "&#125;")
    s = s.replace("<", "&lt;").replace(">", "&gt;")
    return s


def page_url(page_path):
    """site/docs/X/Y.mdx -> /X/Y ; .../overview.mdx -> /X"""
    p = (page_path or "").strip()
    if not p.startswith("site/docs/"):
        return ""
    p = p[len("site/docs/"):]
    p = re.sub(r"\.mdx?$", "", p)
    p = re.sub(r"/overview$", "", p)
    return "/" + p


def splice(path, block, start, end, anchor=None):
    """
    Replace the marked block if present, else insert.  When `anchor` is given
    and found, the block goes immediately BEFORE that line so it lands above
    the boilerplate nav footers rather than after them.
    """
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    if start in text and end in text:
        new = text.split(start)[0] + block + text.split(end, 1)[1]
    else:
        body = "\n---\n\n" + block + "\n"
        idx = text.find(anchor) if anchor else -1
        if idx > 0:
            new = text[:idx].rstrip("\n") + "\n\n" + body + "\n" + text[idx:]
        else:
            new = text.rstrip("\n") + "\n\n" + body
    if new != text:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(new)
        return True
    return False


def read_csv(name, base=None):
    p = os.path.join(base or ANALYSIS, name)
    if not os.path.exists(p):
        return []
    with open(p, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))
