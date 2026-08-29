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

OURAIRPORTS = os.path.join(
    FOLLOWING, "apis/public_open_source/data/ourairports/airports.csv")

# ISO 3166-1 alpha-2 -> display name, for the countries this record touches.
ISO_COUNTRY = {
    "US": "USA", "CA": "Canada", "MX": "Mexico", "EG": "Egypt", "FR": "France",
    "IT": "Italy", "ES": "Spain", "DE": "Germany", "GB": "United Kingdom",
    "IE": "Ireland", "NL": "Netherlands", "BE": "Belgium", "LU": "Luxembourg",
    "DK": "Denmark", "NO": "Norway", "SE": "Sweden", "FI": "Finland",
    "EE": "Estonia", "LV": "Latvia", "LT": "Lithuania", "PL": "Poland",
    "CZ": "Czechia", "SK": "Slovakia", "HU": "Hungary", "AT": "Austria",
    "CH": "Switzerland", "GR": "Greece", "TR": "Turkey", "CY": "Cyprus",
    "BG": "Bulgaria", "RO": "Romania", "RS": "Serbia", "BA": "Bosnia",
    "HR": "Croatia", "SI": "Slovenia", "MT": "Malta", "AL": "Albania",
    "MK": "North Macedonia", "PT": "Portugal", "IL": "Israel", "MD": "Moldova",
    "MC": "Monaco", "AE": "United Arab Emirates", "SA": "Saudi Arabia",
    "BH": "Bahrain", "KW": "Kuwait", "QA": "Qatar", "JO": "Jordan",
    "LB": "Lebanon", "SY": "Syria", "IR": "Iran", "IQ": "Iraq",
    "DZ": "Algeria", "TN": "Tunisia", "MA": "Morocco", "LY": "Libya",
    "SD": "Sudan", "JP": "Japan", "KR": "South Korea", "HK": "Hong Kong",
    "AR": "Argentina", "BR": "Brazil", "AU": "Australia", "NZ": "New Zealand",
    "UA": "Ukraine", "RU": "Russia", "IS": "Iceland", "SM": "San Marino",
}

_AIRPORTS = None
_OA = None

US_STATE = {}  # filled from iso_region on first load


def ourairports():
    """
    The full OurAirports database (85,945 rows) that this pipeline already
    downloaded.  It is the authority for airport name / municipality / region;
    the case-curated following/airports.csv wins where it has an opinion.
    """
    global _OA
    if _OA is None:
        _OA = {}
        if os.path.exists(OURAIRPORTS):
            with open(OURAIRPORTS, newline="", encoding="utf-8") as fh:
                for r in csv.DictReader(fh):
                    ident = (r.get("ident") or "").strip()
                    if ident:
                        _OA[ident] = r
    return _OA


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

    o = ourairports().get(code)
    if o:
        name = name or (o.get("name") or "").strip()
        city = city or (o.get("municipality") or "").strip()
        region = (o.get("iso_region") or "").strip()
        iso = (o.get("iso_country") or "").strip()
        if not state and iso == "US" and region.startswith("US-"):
            state = region[3:]
        if not country and iso:
            country = "USA" if iso == "US" else ISO_COUNTRY.get(iso, iso)

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
    o = ourairports().get(code)
    if o:
        iso = (o.get("iso_country") or "").strip()
        if iso:
            return "USA" if iso == "US" else ISO_COUNTRY.get(iso, iso)
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


_MONTH = ("January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December")


def pretty_date(iso):
    """'2025-09-10' -> '10 September 2025'.  Returns the input if it will not parse."""
    try:
        d = datetime.date.fromisoformat((iso or "").strip())
    except (TypeError, ValueError):
        return iso or "—"
    return f"{d.day} {_MONTH[d.month - 1]} {d.year}"


_LOC_PAGES = None
_LOC_RE = re.compile(r"^([A-Za-z]+)_([A-Z0-9]{3,4})_(\d{4}-\d{2}-\d{2})_to_(\d{4}-\d{2}-\d{2})$")


def following_location_pages():
    """
    airport code -> list of (url, label) for the page-per-location follow log
    under site/docs/Planes/following/, e.g.

        Provo_KPVU_2024-04-19_to_2025-09-13/overview.mdx
          -> KPVU: /Planes/following/Provo_KPVU_2024-04-19_to_2025-09-13/overview

    Only directories that actually hold an overview.mdx are returned, so a link
    built from this is never a 404.  The directory names are stable IDs and are
    never renamed, which is what makes this join safe.
    """
    global _LOC_PAGES
    if _LOC_PAGES is None:
        _LOC_PAGES = {}
        if os.path.isdir(FOLLOWING):
            for d in sorted(os.listdir(FOLLOWING)):
                m = _LOC_RE.match(d)
                if not m:
                    continue
                if not os.path.exists(os.path.join(FOLLOWING, d, "overview.mdx")):
                    continue
                city, code, a, b = m.groups()
                _LOC_PAGES.setdefault(code, []).append(
                    (f"/Planes/following/{d}/overview",
                     f"{city} ({code}), {a} to {b}"))
    return _LOC_PAGES


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


_KNOWN_AP = None


def known_airports():
    """The airport codes that actually have a page under /Planes/Airports/."""
    global _KNOWN_AP
    if _KNOWN_AP is None:
        d = os.path.join(PLANES, "Airports")
        _KNOWN_AP = set()
        if os.path.isdir(d):
            _KNOWN_AP = {f[:-4] for f in os.listdir(d)
                         if f.endswith(".mdx") and f != "overview.mdx"}
    return _KNOWN_AP


def ap_link(code, bold=False):
    """
    Link an airport code ONLY if the page exists.  A sweep can name a field no
    case aircraft ever touched (Offutt AFB, a private strip); linking those
    would ship a 404, and inventing a page for them would bury the case record.
    """
    code = (code or "").strip()
    if not code:
        return "—"
    label = f"**{code}**" if bold else code
    if code in known_airports():
        return f"[{label}](/Planes/Airports/{code})"
    return label


def read_csv(name, base=None):
    p = os.path.join(base or ANALYSIS, name)
    if not os.path.exists(p):
        return []
    with open(p, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))
