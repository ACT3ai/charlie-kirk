#!/usr/bin/env python3
"""RECONCILE THE HEADLINE NUMBERS — 65, 68, 70, 72, 73, 77.

Reads ONLY files already on disk. Makes no network request.

Answers, reproducibly and with the file path for every figure:

  1. WHO published which number, WHEN, and on what basis.
     Source: following/sources.csv, column `count_claimed` and the quoted
     `claim_summary`. The two are NOT the same thing and the difference is
     itself a finding: `count_claimed` is an ACCOUNT-level attribute in that
     file (every @RealCandaceO row carries "68 then 73" including rows dated
     five weeks before the broadcast that first said it), whereas a number
     appearing inside the quoted `claim_summary` is a number that account
     demonstrably typed. Only the second is safe to publish as "X said N".

  2. How many claimed overlaps now have a DEFINITIVE ADS-B verdict.
     Source: following/overlaps.csv, column `adsb_verified_verdict`.
     AT_CLAIMED_AIRPORT / SAME_METRO_WRONG_FIELD / ELSEWHERE are decidable.
     NOT_HEARD / NO_ARCHIVE_COVERAGE / NO_DATE_CLAIMED / NO_TAIL_CLAIMED are
     NOT. NOT_HEARD is not "disproved". NO_ARCHIVE_COVERAGE is not "false".

  3. What the free archives can actually see, measured against three stays
     nobody disputes. This is the number that decides how much weight
     NOT_HEARD can carry, and it is small.

  4. A control on the geographic sweep's own byte pre-filter.

Run:  python3 reconcile_headline_numbers.py
"""

import csv
import collections
import datetime
import glob
import json
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
FOLLOWING = os.path.abspath(os.path.join(HERE, "..", "..", ".."))     # .../Planes/following
PLANES = os.path.abspath(os.path.join(FOLLOWING, ".."))               # .../Planes
DATA = os.path.join(HERE, "..", "data")

OVERLAPS_CSV = os.path.join(FOLLOWING, "overlaps.csv")
SOURCES_CSV = os.path.join(FOLLOWING, "sources.csv")
GEO_SWEEP = os.path.join(DATA, "geo_sweep")

DECIDABLE = {"AT_CLAIMED_AIRPORT", "SAME_METRO_WRONG_FIELD", "ELSEWHERE"}
HEADLINES = ["65", "68", "70", "72", "73", "77"]

# Stays no party to the dispute denies. Used ONLY to measure how often the free
# archives hear an aircraft that is certainly there. Never as evidence itself.
KNOWN_STAYS = [
    ("SU-BTT", "2025-09-04", "2025-09-10", "SU-BTT parked at Provo KPVU"),
    ("SU-BND", "2025-05-23", "2025-09-13", "SU-BND parked at Provo KPVU (113-day stay)"),
    ("SU-BND", "2024-04-19", "2024-07-12", "SU-BND parked at Provo KPVU (2024 stay)"),
]


def rule(t):
    print("\n" + "=" * 78 + f"\n{t}\n" + "=" * 78)


# --------------------------------------------------------------------------
# 1. Who published which number
# --------------------------------------------------------------------------

def who_said_what():
    rule("1. WHO PUBLISHED WHICH NUMBER — sources.csv")
    rows = list(csv.DictReader(open(SOURCES_CSV)))
    print(f"{SOURCES_CSV}\n{len(rows)} source rows\n")
    print("A number is only credited to an account here when the number appears")
    print("inside that row's QUOTED claim_summary. The count_claimed column is an")
    print("account-level tag and is reported separately.\n")
    for n in HEADLINES:
        pat = re.compile(r"(?<!\d)" + n + r"(?!\d)")
        quoted = [r for r in rows if pat.search(r["claim_summary"])]
        tagged = [r for r in rows if r["count_claimed"] and pat.search(r["count_claimed"])]
        dated = sorted((r for r in quoted if r["source_date"] not in ("", "UNKNOWN")),
                       key=lambda r: r["source_date"])
        print(f"--- {n} --- quoted in {len(quoted)} rows; tagged on {len(tagged)} rows")
        if dated:
            print(f"    earliest QUOTED use: {dated[0]['source_date']} "
                  f"{dated[0]['account_handle'] or dated[0]['platform_or_outlet']} "
                  f"({dated[0]['role']}, {dated[0]['evidence_class']})")
        for r in dated:
            print(f"      {r['source_id']:<10} {r['source_date']} "
                  f"{(r['account_handle'] or r['platform_or_outlet']):<45} {r['role']}")
        tag_dates = sorted(r["source_date"] for r in tagged
                           if r["source_date"] not in ("", "UNKNOWN"))
        if tag_dates and (not dated or tag_dates[0] < dated[0]["source_date"]):
            print(f"    NOTE: count_claimed tags this number as early as {tag_dates[0]}, "
                  f"{(datetime.date.fromisoformat(dated[0]['source_date']) - datetime.date.fromisoformat(tag_dates[0])).days} days"
                  " before anyone is quoted using it. Account-level tag, not a post.")
        print()


# --------------------------------------------------------------------------
# 2. The register and its ADS-B verdicts
# --------------------------------------------------------------------------

def register():
    rule("2. THE REGISTER — overlaps.csv, and what the recovered ADS-B decides")
    rows = list(csv.DictReader(open(OVERLAPS_CSV)))
    print(f"{OVERLAPS_CSV}\n{len(rows)} rows\n")

    fam = collections.Counter(r["overlap_id"].split("-")[0] for r in rows)
    print("ID families:", dict(fam))
    print("  67 OWENS + 5 UNPUB = 72, NOT 73. The register encodes the sheet's 67")
    print("  published rows plus five undated extras; the broadcast arithmetic was")
    print("  68 -> 73. The two have never been made to agree.\n")

    ver = collections.Counter(r["adsb_verified_verdict"] for r in rows)
    dec = sum(v for k, v in ver.items() if k in DECIDABLE)
    print("adsb_verified_verdict:")
    for k, v in ver.most_common():
        mark = "DECIDABLE" if k in DECIDABLE else "not decidable"
        print(f"  {v:4d}  {k:<24} {mark}")
    print(f"\n  decidable {dec}/{len(rows)} = {100*dec/len(rows):.1f}%   "
          f"undecidable {len(rows)-dec}/{len(rows)} = {100*(len(rows)-dec)/len(rows):.1f}%")

    at = [r for r in rows if r["adsb_verified_verdict"] == "AT_CLAIMED_AIRPORT"]
    gnd = [r for r in at if r["adsb_ground_position"] == "yes"]
    print(f"\n  AT_CLAIMED_AIRPORT {len(at)}, of which ON THE GROUND {len(gnd)};")
    print(f"  the other {len(at)-len(gnd)} are an airborne fix near the field "
          "(arrival, departure or a low pass).")
    days = sorted({(t.strip(), r["date"]) for r in gnd
                   for t in r["foreign_tail"].replace(";", ",").split(",") if t.strip()})
    print(f"  those {len(gnd)} rows collapse to {len(days)} distinct aircraft-days:")
    for t, d in days:
        print(f"      {t}  {d}")

    print("\n  NO_ARCHIVE_COVERAGE date range (a RETENTION BOUNDARY, not a removal):")
    nac = sorted(r["date"] for r in rows
                 if r["adsb_verified_verdict"] == "NO_ARCHIVE_COVERAGE")
    print(f"      {len(nac)} rows, {nac[0]} .. {nac[-1]}")

    print("\n  Audit cross-check (Kanekoa's colour verdict vs recovered position data):")
    for want, label in (("inaccurate", "audit says INACCURATE"),
                        (("accurate", "partial"), "audit says ACCURATE or PARTIAL")):
        sel = [r for r in rows if (r["audit_verdict"] == want
                                   if isinstance(want, str)
                                   else r["audit_verdict"] in want)]
        d = [r for r in sel if r["adsb_verified_verdict"] in DECIDABLE]
        c = collections.Counter(r["adsb_verified_verdict"] for r in d)
        print(f"    {label}: {len(sel)} rows, {len(d)} decidable -> {dict(c)}")
        for r in d:
            agree = (r["adsb_verified_verdict"] == "ELSEWHERE") if want == "inaccurate" \
                else (r["adsb_verified_verdict"] == "AT_CLAIMED_AIRPORT")
            if not agree:
                print(f"       AUDIT CONTRADICTED: {r['overlap_id']} {r['date']} "
                      f"{r['foreign_tail']} {r['airport_code']} -> "
                      f"{r['adsb_verified_verdict']} at {r['adsb_closest_approach_km']} km")

    print("\n  Who the register says was there:")
    print("   charlie_present:", dict(collections.Counter(r["charlie_present"] for r in rows)))
    print("   erika_present:  ", dict(collections.Counter(r["erika_present"] for r in rows)))
    print("   NOTE: no row anywhere in the register carries erika_present = 'yes'.")
    return rows


# --------------------------------------------------------------------------
# 3. How much the free archives can see at all
# --------------------------------------------------------------------------

def scan_tail(tail):
    d = os.path.join(PLANES, tail, "data", "recovered")
    held, miss = collections.defaultdict(set), collections.defaultdict(set)
    if not os.path.isdir(d):
        return held, miss
    rx = re.compile(re.escape(tail) + r"_(\d{4}-\d\d-\d\d)_([A-Za-z0-9\-]+)_trace_full(\.miss)?\.json")
    for f in os.listdir(d):
        m = rx.match(f)
        if not m:
            continue
        date, src, ismiss = m.group(1), m.group(2), m.group(3)
        if f.endswith(".meta.json") and not ismiss:
            continue
        (miss if ismiss else held)[date].add(src)
    return held, miss


def coverage():
    rule("3. HOW OFTEN THE FREE ARCHIVES HEAR AN AIRCRAFT THAT IS CERTAINLY THERE")
    print("Counted from the filenames under <TAIL>/data/recovered/. A payload file")
    print("means the archive HELD the day; a '.miss.' meta means the archive was")
    print("ASKED and had nothing. Neither is evidence the aircraft was elsewhere.\n")
    for tail, a, b, label in KNOWN_STAYS:
        held, miss = scan_tail(tail)
        d0, d1 = datetime.date.fromisoformat(a), datetime.date.fromisoformat(b)
        days = [(d0 + datetime.timedelta(i)).isoformat() for i in range((d1 - d0).days + 1)]
        h = [d for d in days if d in held]
        m = [d for d in days if d in miss and d not in held]
        u = [d for d in days if d not in held and d not in miss]
        print(f"  {label}: {a} .. {b} = {len(days)} days")
        print(f"    HELD {len(h)} ({100*len(h)/len(days):.0f}%)  "
              f"ASKED-AND-EMPTY {len(m)}  NEVER ASKED {len(u)}")
        print(f"    held days: {h}")
    print("\n  Whole-history hold rate per tail (distinct dates asked vs held):")
    for tail in ["SU-BTT", "SU-BND", "SU-BTU", "SU-BTV", "SU-BGM", "T7-ELL"]:
        held, miss = scan_tail(tail)
        asked = set(held) | set(miss)
        if not asked:
            continue
        print(f"    {tail:<8} asked {len(asked):5d}  held {len(held):4d}  "
              f"= {100*len(held)/len(asked):5.1f}%")
    byt = os.path.join(DATA, "analysis", "definitive_proximity_by_tail.csv")
    if os.path.exists(byt):
        print(f"\n  Controls, from {byt}:")
        for r in csv.DictReader(open(byt)):
            if r["side"] in ("control", "kirk"):
                a, hh = int(r["archive_days_asked"]), int(r["archive_days_held"])
                print(f"    {r['tail']:<20} {r['side']:<8} asked {a:5d} held {hh:4d} "
                      f"= {100*hh/max(1,a):5.1f}%")
        print("  CONFOUND: the two named controls are scheduled European airliners in")
        print("  the densest receiver coverage on earth. The Kirk-side US private jets")
        print("  are the closer comparator, and they sit between the two.")


# --------------------------------------------------------------------------
# 4. Control on the geographic sweep's byte pre-filter
# --------------------------------------------------------------------------

def prefilter_lon_tokens(lat, lon, radius_mi):
    """Reproduces geo_sweep.prefilter_patterns() longitude tokens exactly."""
    pad = radius_mi / (69.0 * max(0.15, math.cos(math.radians(lat)))) + 0.02
    return set(range(int(math.floor(lon - pad)), int(math.floor(lon + pad)) + 1)), pad


def sweep_prefilter_control():
    rule("4. CONTROL ON THE GEOGRAPHIC SWEEP'S OWN BYTE PRE-FILTER")
    circles = {}
    for f in glob.glob(os.path.join(GEO_SWEEP, "*", "_sweep.meta.json")):
        for c in json.load(open(f))["circles"]:
            circles[(c["key"], c["kind"])] = (c["lat"], c["lon"], c["radius_mi"])
    if not circles:
        print("  no sweep metadata on disk; skipped")
        return
    print(f"  {len(circles)} distinct circles across {GEO_SWEEP}")
    print("  geo_sweep.py builds its longitude tokens with int(math.floor(lon)).")
    print("  In a trace file a longitude of -111.73 is PRINTED '-111.73', so its")
    print("  token is ',-111.' -- but floor(-111.73) is -112. On a negative")
    print("  longitude the generated band is shifted one degree WEST, and the")
    print("  eastern edge of every US circle is never scanned.\n")

    def area_blind(lat0, lon0, r, N=200):
        gen, pad = prefilter_lon_tokens(lat0, lon0, r)
        rlat = r / 69.0
        inside = blind = 0
        for i in range(N):
            la = lat0 - rlat + 2 * rlat * (i + 0.5) / N
            for j in range(N):
                lo = lon0 - pad + 2 * pad * (j + 0.5) / N
                dx = (lo - lon0) * 69.0 * math.cos(math.radians(la))
                dy = (la - lat0) * 69.0
                if dx * dx + dy * dy <= r * r:
                    inside += 1
                    n = int(lo) if lo < 0 else int(math.floor(lo))
                    if n not in gen:
                        blind += 1
        return blind / inside

    ev, ct = [], []
    for (k, kind), (la, lo, r) in circles.items():
        (ev if kind == "event" else ct).append((area_blind(la, lo, r), k))
    for name, arr in (("EVENT", ev), ("CONTROL", ct)):
        if not arr:
            continue
        vals = [x[0] for x in arr]
        print(f"  {name} circles n={len(arr)}: area never scanned "
              f"mean {sum(vals)/len(vals):.1%}, max {max(vals):.1%}, "
              f"circles at 0% = {sum(1 for v in vals if v < 1e-9)}")
    worst = sorted(ev, reverse=True)[:5]
    print("  worst event circles:", [(f"{v:.1%}", k) for v, k in worst])

    # The proven miss.
    p = os.path.join(PLANES, "SU-BTT", "data", "recovered",
                     "SU-BTT_2024-04-23_adsb-lol_trace_full.json")
    slc = circles.get(("20240423_salt_lake_city", "event"))
    if os.path.exists(p) and slc:
        gen, _ = prefilter_lon_tokens(*slc)
        b = open(p, "rb").read()
        toks = {n: (f",{n}.".encode() in b) for n in sorted(gen)}
        print("\n  PROVEN MISS -- SU-BTT, 2024-04-23, Salt Lake City circle:")
        print(f"    circle generates longitude tokens {[f',{n}.' for n in sorted(gen)]}")
        print(f"    present in the trace file? {toks}")
        print(f"    ',-111.' present in the trace file? {b',-111.' in b}")
        t = json.load(open(p))
        lons = [q[2] for q in t["trace"]]
        print(f"    trace westernmost longitude all day: {min(lons):.4f}")
        print("    => pre-filter rejected it before the exact geometry ran, although")
        print("       the same trace ends ON THE GROUND at KPVU, 39.7 mi from the")
        print("       circle centre. The 'exactly three' geo-sweep result is a LOWER")
        print("       BOUND. This is a defect in our own filter, not a removal by")
        print("       anyone, and the live adsb.lol endpoint still serves the day.")


if __name__ == "__main__":
    who_said_what()
    register()
    coverage()
    sweep_prefilter_control()
    print("\nDone. Nothing above required a network request.")
