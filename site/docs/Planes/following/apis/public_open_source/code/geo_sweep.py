#!/usr/bin/env python3
"""THE GEOGRAPHIC SWEEP: stop asking about tails, start asking about places.

Everything this repo has pulled from the open archives until now was a PER-TAIL
question -- "was SU-BTT at Provo on 10 September" -- and a per-tail question can
only ever confirm or fail to confirm an aircraft somebody had already named. It
holds about 9% of the aircraft-days the speaking-event windows need, and it is
structurally incapable of finding the aircraft nobody thought to look for.

adsb.lol mirrors its ENTIRE global database to public GitHub Releases, one tar
per UTC day, Open Database Licence, no account and no key. That archive holds
every aircraft its volunteer receivers heard that day -- roughly 90,000 of them
-- not just the sixteen in this repo's fleet file. Streaming one day and
filtering it by GEOGRAPHY instead of by hex turns the question inside out:

    WHAT WAS WITHIN 50 MILES OF THIS CITY ON THIS DAY?

That is the question the following-planes claim actually needs answered, and
this is the only free way to answer it.

    python3 geo_sweep.py --plan                  what it would sweep, in order
    python3 geo_sweep.py --run                   sweep, priority order, resumable
    python3 geo_sweep.py --run --date 2025-09-10
    python3 geo_sweep.py --run --max-dates 20    bounded run
    python3 geo_sweep.py --run --radius 50 --window 1
    python3 geo_sweep.py --report                what is on disk now

HOW IT WORKS, AND WHY IT IS AFFORDABLE
--------------------------------------
Each day is ~2-5 GB. It is STREAMED and never stored: curl pipes the tar into
Python, each member is gunzipped in memory, and a cheap byte pre-filter throws
out the ~92% of aircraft that were never in the right degree square before any
JSON is parsed. Measured cost is about one minute of CPU per day; the wire is
the only real budget.

WHAT LANDS ON DISK
------------------
A CSV row for EVERY aircraft that entered any circle -- that is the coverage
record, and it is the part that makes an absence meaningful. The full trace is
kept only for aircraft that are FLAGGED (foreign-registered, unregistered,
military/PIA/LADD, or in this repo's fleet file), because keeping 90,000 traces
a day in a git repo an automated job pushes every few minutes is not an option.
Unflagged aircraft are counted, described in the CSV, and not stored.

THE FOUR RULES THIS SCRIPT EXISTS TO KEEP
-----------------------------------------
1. THE CONTROL CITIES ARE SWEPT ON THE SAME DAYS, in the same run, by the same
   code. "Foreign jets were within 50 miles of the event" means nothing until
   you know how many were within 50 miles of Des Moines that day. This
   investigation has already had to retract one finding for skipping a control.

2. A CIRCLE IS NOT AN AIRPORT AND A POSITION IS NOT A LANDING. Every row
   carries the distance in miles to the nearest field and whether the aircraft
   ever reported itself ON GROUND. Never drop those two columns.

3. AN EMPTY DAY IS A COVERAGE FACT, NOT AN ABSENCE. A swept day with no hits
   is written down as swept, with the aircraft count the archive held, so
   "asked and nothing was there" can never be confused with "never asked".

4. NOTHING IS OVERWRITTEN. A re-sweep of a date already on disk lands beside
   the first with a timestamp suffix. The diff between two sweeps of one day is
   how this repo proves something stopped being retrievable.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import gzip
import io
import json
import math
import os
import subprocess
import sys
import tarfile
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))

from geo import airports_within, haversine_mi          # noqa: E402
from targets import build_targets, priority            # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_ROOT = os.path.normpath(os.path.join(HERE, "..", "data", "geo_sweep"))
FLEET_JS = os.path.join(HERE, "lib", "fleet.js")

REPO = "adsblol/globe_history_{year}"
TAG = "v{y}.{m}.{d}-planes-readsb-prod-0"
DL = "https://github.com/{repo}/releases/download/{tag}/{asset}"

# readsb dbFlags bitfield, as published by the tar1090 database.
DB_FLAGS = {1: "military", 2: "interesting", 4: "PIA", 8: "LADD"}


def utcnow():
    return dt.datetime.now(dt.timezone.utc).isoformat()


# --------------------------------------------------------------------------
# Which aircraft are worth keeping the whole trace for
# --------------------------------------------------------------------------

def load_fleet_hexes():
    """The hexes this repo already tracks, read out of lib/fleet.js so the two
    never drift. A miss here is not fatal -- it only means a known tail gets
    kept for being foreign rather than for being known."""
    out = {}
    if not os.path.exists(FLEET_JS):
        return out
    import re
    for m in re.finditer(r'reg:\s*"([^"]+)",\s*hex:\s*"([0-9a-fA-F]+)"', open(FLEET_JS).read()):
        out[m.group(2).lower()] = m.group(1)
    return out


FLEET_HEX = load_fleet_hexes()

# US military aircraft carry a fiscal-year serial ("07-7189", "94-7315"), not an
# N-number. Treating those as "foreign registration" is exactly the kind of
# quiet mislabel that turns a routine C-17 at Peterson SFB into a finding.
US_MIL_SERIAL = __import__("re").compile(r"^\d{2}-\d{3,5}$")

GOV_WORDS = ("AIR FORCE", "ARMY", "NAVY", "MARINE CORPS", "COAST GUARD",
             "DEPARTMENT OF", "UNITED STATES OF AMERICA", "GOVERNMENT",
             "STATE OF", "FEDERAL", "CUSTOMS", "BORDER PROTECTION",
             "EXECUTIVE", "ROYAL", "REPUBLIC OF", "MINISTRY")


def flag_aircraft(d):
    """Everything notable about this aircraft, as a list of reason strings.

    This is a DESCRIPTION, not a verdict. The reasons are published verbatim in
    the CSV so a reader can see exactly what the filter noticed and disagree
    with any of it. `dbflag:LADD` in particular is very common and means only
    that the owner has asked the FAA to keep the tail off the commercial
    displays -- which is a finding about the tracking industry, not about the
    aircraft.
    """
    reasons = []
    hexid = (d.get("icao") or "").lower().lstrip("~")
    reg = (d.get("r") or "").strip()
    own = (d.get("ownOp") or "").upper()
    flags = int(d.get("dbFlags") or 0)

    if hexid in FLEET_HEX:
        reasons.append(f"tracked_fleet:{FLEET_HEX[hexid]}")
    if (d.get("icao") or "").startswith("~"):
        reasons.append("non_icao_address")       # TIS-B / ADS-R, not a real airframe address
    if not reg:
        reasons.append("no_registration")
    elif US_MIL_SERIAL.match(reg):
        reasons.append("us_military_serial")
    elif not reg.upper().startswith("N"):
        reasons.append("non_us_registration")
    for bit, name in DB_FLAGS.items():
        if flags & bit:
            reasons.append(f"dbflag:{name}")
    if any(w in own for w in GOV_WORDS):
        reasons.append("government_operator_string")
    return reasons


# Storing a trace and noticing an aircraft are two different decisions. A day
# holds ~1,400 notable aircraft across all circles; keeping every one of their
# traces would add gigabytes to a repo an automated job pushes every few
# minutes. So the CSV records ALL of them -- that is the coverage evidence --
# and only these get the full track kept:
STORE_REASONS = ("tracked_fleet:", "non_us_registration", "no_registration",
                 "non_icao_address", "dbflag:military", "dbflag:PIA")


def store_worthy(reasons, hits):
    """Keep the whole trace only for a foreign, unregistered, military or PIA
    aircraft that was ON THE GROUND inside an EVENT circle -- plus any tail
    this repo already tracks, wherever it turns up.

    THE GROUND TEST IS THE POINT. Most foreign registrations inside a 50-mile
    circle are airliners at 35,000 ft on a great-circle route; a Westjet 737
    over Utah is not "at" Orem in any sense the following-planes claim means.
    An aircraft that reported itself on the ground was on somebody's ramp.
    """
    if any(r.startswith("tracked_fleet:") for r in reasons):
        return True
    if not any(r.startswith(p) for r in reasons for p in STORE_REASONS):
        return False
    return any(h["circle"]["kind"] == "event" and h["ground"] for h in hits)


# --------------------------------------------------------------------------
# The byte pre-filter
# --------------------------------------------------------------------------

def prefilter_patterns(circles):
    """Degree-square tokens for one day's circles.

    A trace point is `[seconds, lat, lon, ...]`, so every latitude and every
    longitude in the file is preceded by a comma. Requiring one in-range
    latitude token AND one in-range longitude token rejects the great majority
    of the world's aircraft for the cost of a substring search.

    It is a PRE-filter and only a pre-filter: it can pass an aircraft that was
    at the right latitude over one ocean and the right longitude over another,
    which the exact check below then rejects. It cannot reject an aircraft that
    was genuinely inside a circle, because that aircraft necessarily carries
    both tokens. Run with --no-prefilter to confirm that on any given day.
    """
    lats, lons = set(), set()
    for c in circles:
        pad_lat = c["radius_mi"] / 69.0 + 0.02
        pad_lon = c["radius_mi"] / (69.0 * max(0.15, math.cos(math.radians(c["lat"])))) + 0.02
        for v in (c["lat"] - pad_lat, c["lat"] + pad_lat):
            lats.add(int(math.floor(v)))
        for v in (c["lon"] - pad_lon, c["lon"] + pad_lon):
            lons.add(int(math.floor(v)))
        lats.update(range(int(math.floor(c["lat"] - pad_lat)), int(math.floor(c["lat"] + pad_lat)) + 1))
        lons.update(range(int(math.floor(c["lon"] - pad_lon)), int(math.floor(c["lon"] + pad_lon)) + 1))
    pats_lat = [p for n in sorted(lats) for p in (f",{n}.".encode(), f",{n},".encode())]
    pats_lon = [p for n in sorted(lons) for p in (f",{n}.".encode(), f",{n},".encode())]
    return pats_lat, pats_lon


# --------------------------------------------------------------------------
# The exact check
# --------------------------------------------------------------------------

def check_trace(d, circles):
    """Every circle this aircraft entered, with the closest approach in each.

    Returns a list of hit dicts. `ground` is True only if the aircraft reported
    itself ON GROUND while inside the circle -- readsb writes the literal
    string "ground" in the altitude slot for that, and it is the single most
    useful bit in the whole record.
    """
    ts = float(d.get("timestamp") or 0)
    per = {}
    for p in d.get("trace") or ():
        try:
            lat, lon = p[1], p[2]
        except (IndexError, TypeError):
            continue
        if lat is None or lon is None:
            continue
        for c in circles:
            dist = haversine_mi(c["lat"], c["lon"], lat, lon)
            if dist > c["radius_mi"]:
                continue
            h = per.setdefault(c["key"], {
                "circle": c, "n": 0, "first": None, "last": None,
                "min_dist": 1e9, "min_lat": None, "min_lon": None,
                "ground": False, "ground_lat": None, "ground_lon": None,
                "min_alt": None,
            })
            h["n"] += 1
            t = ts + (p[0] or 0)
            h["first"] = t if h["first"] is None else min(h["first"], t)
            h["last"] = t if h["last"] is None else max(h["last"], t)
            alt = p[3] if len(p) > 3 else None
            if alt == "ground":
                if not h["ground"]:
                    h["ground"], h["ground_lat"], h["ground_lon"] = True, lat, lon
            elif isinstance(alt, (int, float)):
                h["min_alt"] = alt if h["min_alt"] is None else min(h["min_alt"], alt)
            if dist < h["min_dist"]:
                h["min_dist"], h["min_lat"], h["min_lon"] = dist, lat, lon
    return list(per.values())


def resolve_field(lat, lon):
    """Nearest usable field to a position, WITH THE DISTANCE. The distance is
    not decoration: a nearest-field label read as a destination is the exact
    mistake that produced the Provo-versus-Dugway correction on this site."""
    if lat is None:
        return None, None
    near = airports_within(lat, lon, 25)
    if not near:
        return None, None
    return near[0]["ident"], near[0]["distance_mi"]


# --------------------------------------------------------------------------
# The archive
# --------------------------------------------------------------------------

class _Counting:
    """Counts bytes actually read off the pipe.

    The completeness test compares this against the assets' total Content-Length.
    It must NOT be computed from tar member sizes: a tar pads every member to a
    512-byte boundary and prefixes a 512-byte header, and members that are not
    traces are skipped entirely, so member payload always undershoots the wire
    figure and every day looks truncated. That mistake fired on the first
    attempt at this check and is why the counter lives here instead."""

    def __init__(self, fh):
        self._fh = fh
        self.count = 0

    def read(self, n=-1):
        b = self._fh.read(n)
        self.count += len(b)
        return b

    def close(self):
        return self._fh.close()


def _probe(url, timeout=45, tries=4):
    """PRESENT / ABSENT / UNKNOWN — and the three are never merged.

    THIS FUNCTION EXISTS BECAUSE IT GOT THIS WRONG ONCE. The first version
    treated any non-200 as "the archive does not have this day", ran eight
    concurrent multi-gigabyte streams alongside it, and wrote
    NO_RELEASE_FOR_THIS_DATE onto 230 of 278 dates. Every one of those days was
    checked by hand afterwards and the release was there. A timeout under load
    had been recorded as an archive fact.

    So: only an HTTP 404 means ABSENT. A timeout, a reset, a 429 or a 5xx means
    UNKNOWN, is retried with backoff, and if it still will not resolve the day
    is left UNSWEPT rather than written down as empty. An unasked question and
    an answered one are different things and this repo does not merge them.
    """
    last = None
    for i in range(tries):
        r = subprocess.run(["curl", "-sS", "-L", "-r", "0-1", "--max-time", str(timeout),
                            "-o", os.devnull, "-w", "%{http_code}", url],
                           capture_output=True, text=True)
        code = r.stdout.strip()
        last = code
        if code in ("200", "206"):
            return "PRESENT", code
        if code == "404":
            return "ABSENT", code
        time.sleep(2 ** i)                    # 1s, 2s, 4s, 8s
    return "UNKNOWN", last


def content_length(url, timeout=45):
    """Total asset size, read out of the Content-Range of a 2-byte GET.
    Used to prove a stream ran to the end rather than dying quietly."""
    r = subprocess.run(["curl", "-sS", "-L", "-r", "0-1", "-D", "-", "--max-time", str(timeout),
                        "-o", os.devnull, url], capture_output=True, text=True)
    for line in r.stdout.splitlines():
        if line.lower().startswith("content-range:") and "/" in line:
            tail = line.split("/")[-1].strip()
            if tail.isdigit():
                return int(tail)
    return None


def asset_urls(date_iso, timeout=45):
    """Locate one UTC day in the GitHub backup WITHOUT touching the GitHub API.

    The API allows 60 unauthenticated requests an hour and a full sweep needs
    hundreds, so the release URL is constructed and probed directly on the CDN,
    which is not rate limited. Tags use dots in the date. A day is either one
    `.tar` or a `split` of one into `.tar.aa`, `.tar.ab`, ... which concatenate
    back into a single stream in sort order.

    Releases sit in the repo for the year, except at the year boundary where
    adsb.lol has filed the first days of January under the previous year's
    repo -- so the adjacent years are tried too.
    """
    y, m, d = date_iso.split("-")
    tag = TAG.format(y=y, m=m, d=d)
    unknown = False
    for yr in (int(y), int(y) - 1, int(y) + 1):
        repo = REPO.format(year=yr)
        base = DL.format(repo=repo, tag=tag, asset="")
        st, _ = _probe(base + tag + ".tar", timeout)
        if st == "PRESENT":
            return [base + tag + ".tar"], repo, tag, "OK"
        if st == "UNKNOWN":
            unknown = True
        parts, suf = [], 0
        while suf <= 25:
            url = base + f"{tag}.tar.a{chr(ord('a') + suf)}"
            st, _ = _probe(url, timeout)
            if st == "PRESENT":
                parts.append(url)
                suf += 1
                continue
            if st == "UNKNOWN":
                unknown = True
            break
        if parts:
            return parts, repo, tag, "OK"
    # Nothing found. Say WHICH kind of nothing.
    return [], None, tag, ("PROBE_UNRESOLVED" if unknown else "ABSENT")


def sweep_date(date_iso, circles, outdir, prefilter=True, timeout=30, verbose=True):
    """Stream one UTC day and return the hits. Nothing but hits touches disk."""
    urls, repo, tag, probe_verdict = asset_urls(date_iso, timeout)
    meta = {
        "sweep_date": date_iso, "retrieved_utc": utcnow(), "source": "adsblol-github-backup",
        "github_repo": repo, "release_tag": tag, "asset_urls": urls,
        "licence": "Open Database Licence (ODbL), adsb.lol",
        "radius_mi": circles[0]["radius_mi"] if circles else None,
        "circles": [{"key": c["key"], "kind": c["kind"], "city": c.get("city"),
                     "state": c.get("state"), "lat": c["lat"], "lon": c["lon"],
                     "radius_mi": c["radius_mi"], "offset_days": c.get("offset_days"),
                     "center_basis": c.get("center_basis"),
                     "event_date": c.get("date"), "who": c.get("who")}
                    for c in circles],
        "prefilter": prefilter,
    }
    if not urls:
        if probe_verdict == "ABSENT":
            meta.update(status="NO_RELEASE_FOR_THIS_DATE", aircraft_in_archive=0, hits=0,
                        note="Every candidate asset URL returned HTTP 404. The backup has "
                             "no prod release for this UTC day. That is an ARCHIVE fact, "
                             "not an aircraft fact, and it is not evidence that anything "
                             "was or was not here.")
        else:
            meta.update(status="PROBE_UNRESOLVED", aircraft_in_archive=0, hits=0,
                        note="The probe never got a clean answer — timeouts or transient "
                             "errors, not a 404. THIS DAY IS UNSWEPT AND UNKNOWN. It must "
                             "never be counted as an empty day; re-run it. Recording a "
                             "timeout as an archive fact is the exact mistake that put a "
                             "false NO_RELEASE on 230 dates on 26 Aug 2026.")
        return [], meta

    # What SHOULD cross the wire, so a stream that dies halfway cannot be
    # written down as a completed sweep.
    expected = 0
    for u in urls:
        n = content_length(u, timeout)
        if n is None:
            expected = None
            break
        expected += n

    pl, po = prefilter_patterns(circles) if prefilter else ([], [])
    t0 = time.time()
    n_files = n_deep = n_bytes = 0
    hits = []
    keep = {}

    truncated = None
    proc = subprocess.Popen(["curl", "-sS", "-L", "--retry", "3", "--retry-delay", "3",
                             "--retry-all-errors", "--speed-time", "120", "--speed-limit", "1024",
                             "--max-time", "10800"] + urls,
                            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                            bufsize=1024 * 1024)
    wire = _Counting(proc.stdout)
    try:
        tf = tarfile.open(fileobj=wire, mode="r|")
        for m in tf:
            if not m.isfile() or "trace_full_" not in m.name:
                continue
            n_files += 1
            n_bytes += m.size
            try:
                raw = tf.extractfile(m).read()
            except Exception as ex:
                truncated = f"{type(ex).__name__}: {ex}"
                break
            try:
                b = gzip.decompress(raw)
            except Exception:
                b = raw
            if prefilter and not (any(p in b for p in pl) and any(p in b for p in po)):
                continue
            n_deep += 1
            try:
                d = json.loads(b)
            except Exception:
                continue
            got = check_trace(d, circles)
            if not got:
                continue
            reasons = flag_aircraft(d)
            for h in got:
                lat = h["ground_lat"] if h["ground"] else h["min_lat"]
                lon = h["ground_lon"] if h["ground"] else h["min_lon"]
                field, fdist = resolve_field(lat, lon)
                hits.append({
                    "sweep_date": date_iso,
                    "circle_key": h["circle"]["key"],
                    "circle_kind": h["circle"]["kind"],
                    "city": h["circle"].get("city"),
                    "state": h["circle"].get("state"),
                    "event_date": h["circle"].get("date"),
                    "offset_days": h["circle"].get("offset_days"),
                    "who": h["circle"].get("who"),
                    "hex": d.get("icao"),
                    "reg": d.get("r") or "",
                    "type": d.get("t") or "",
                    "own_op": d.get("ownOp") or "",
                    "year": d.get("year") or "",
                    "db_flags": int(d.get("dbFlags") or 0),
                    "flag_reasons": "|".join(reasons),
                    "flagged": bool(reasons),
                    "points_in_circle": h["n"],
                    "first_utc": dt.datetime.fromtimestamp(h["first"], dt.timezone.utc).isoformat()
                                  if h["first"] else "",
                    "last_utc": dt.datetime.fromtimestamp(h["last"], dt.timezone.utc).isoformat()
                                 if h["last"] else "",
                    "closest_mi_to_city": round(h["min_dist"], 2),
                    "closest_lat": round(h["min_lat"], 5) if h["min_lat"] is not None else "",
                    "closest_lon": round(h["min_lon"], 5) if h["min_lon"] is not None else "",
                    "on_ground_in_circle": h["ground"],
                    "min_alt_ft": h["min_alt"] if h["min_alt"] is not None else "",
                    "nearest_field": field or "",
                    "nearest_field_mi": fdist if fdist is not None else "",
                })
            if store_worthy(reasons, got):
                keep[d.get("icao")] = b
        tf.close()
    except Exception as ex:
        truncated = truncated or f"{type(ex).__name__}: {ex}"
    finally:
        try:
            proc.stdout.close()
        except Exception:
            pass
        proc.wait()

    if keep:
        tdir = os.path.join(outdir, "traces")
        os.makedirs(tdir, exist_ok=True)
        for hexid, b in keep.items():
            path = os.path.join(tdir, f"{hexid}.json.gz")
            if os.path.exists(path):        # never overwrite a previous pull
                path = os.path.join(tdir, f"{hexid}.{utcnow()[:19].replace(':', '')}.json.gz")
            with gzip.open(path, "wb") as fh:
                fh.write(b)

    # A short stream is NOT a sweep. Recording one as complete would silently
    # publish a fraction of the sky as if it were all of it -- the 26 Aug 2026
    # run read 39,076 aircraft for 10 September against 74,405 on a clean pull
    # and called both SWEPT.
    short = expected is not None and wire.count < expected * 0.999
    status = "TRUNCATED" if (truncated or short) else "SWEPT"

    meta.update(status=status, curl_exit=proc.returncode,
                archive_bytes_expected=expected,
                archive_bytes_read_from_wire=wire.count,
                truncation_error=truncated,
                aircraft_in_archive=n_files, deep_parsed=n_deep,
                archive_bytes_streamed=n_bytes, hits=len(hits),
                distinct_aircraft_in_circles=len({h["hex"] for h in hits}),
                flagged_aircraft_stored=len(keep),
                seconds=round(time.time() - t0, 1),
                note=("THIS DAY IS INCOMPLETE. The stream ended early, so the counts below "
                      "are a FRACTION of the day and mean nothing on their own. Re-sweep it; "
                      "do not quote it, and do not treat a missing aircraft here as absent."
                      if status == "TRUNCATED" else
                      "A swept day with no hits means the archive was ASKED and held "
                     "nothing inside these circles. It is not evidence that no "
                     "aircraft was there: a volunteer network heard nothing, and "
                      "transponder-off, out-of-coverage and a wrong claimed date all "
                      "look identical from here."))
    return hits, meta


def _worker(job):
    """One UTC day, in its own process.

    Processes rather than threads on purpose: the work is gzip and JSON over
    ~20 GB of decompressed trace per day, and Python threads serialise the JSON
    half on the GIL -- five threads measured no faster than one. Separate
    processes use the cores AND overlap the five downloads.
    """
    i, total, d, circles, prefilter = job
    ev = ", ".join(f"{c['city']},{c['state']}" for c in circles if c["kind"] == "event")
    head = f"[{i}/{total}] {d}  {ev or '(controls only)'}"
    try:
        hits, m = sweep_date(d, circles, os.path.join(OUT_ROOT, d), prefilter=prefilter)
    except Exception as e:
        return f"{head}\n    ERROR {type(e).__name__}: {e}"
    write_day(d, hits, m)
    if m["status"] != "SWEPT":
        return f"{head}\n    {m['status']}"
    gnd = sorted({h["reg"] or h["hex"] for h in hits
                  if h["flagged"] and h["circle_kind"] == "event" and h["on_ground_in_circle"]})
    out = (f"{head}\n    {m['aircraft_in_archive']} aircraft in archive, "
           f"{m['distinct_aircraft_in_circles']} in circles, "
           f"{m['flagged_aircraft_stored']} traces kept, {m['seconds']}s")
    if gnd:
        out += ("\n    notable, on the ground in an event circle: "
                + ", ".join(gnd[:20]) + (f" ... +{len(gnd) - 20}" if len(gnd) > 20 else ""))
    return out


HITS_FIELDS = ["sweep_date", "circle_key", "circle_kind", "city", "state", "event_date",
               "offset_days", "who", "hex", "reg", "type", "own_op", "year", "db_flags",
               "flag_reasons", "flagged", "points_in_circle", "first_utc", "last_utc",
               "closest_mi_to_city", "closest_lat", "closest_lon", "on_ground_in_circle",
               "min_alt_ft", "nearest_field", "nearest_field_mi"]


def write_day(date_iso, hits, meta):
    outdir = os.path.join(OUT_ROOT, date_iso)
    os.makedirs(outdir, exist_ok=True)
    mp = os.path.join(outdir, "_sweep.meta.json")
    if os.path.exists(mp):
        mp = os.path.join(outdir, f"_sweep.{utcnow()[:19].replace(':', '')}.meta.json")
    with open(mp, "w") as fh:
        json.dump(meta, fh, indent=2)
    # gzipped: ~7,800 rows a day across 278 days is 400 MB raw and 40 MB
    # compressed, in a repo an automated job pushes constantly. gzip is
    # lossless -- `gunzip -c hits.csv.gz` returns the exact bytes -- and every
    # reader in this directory opens either form transparently.
    hp = os.path.join(outdir, "hits.csv.gz")
    if os.path.exists(hp):
        hp = os.path.join(outdir, f"hits.{utcnow()[:19].replace(':', '')}.csv.gz")
    with gzip.open(hp, "wt", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=HITS_FIELDS)
        w.writeheader()
        for h in sorted(hits, key=lambda x: (not x["flagged"], x["circle_key"], x["hex"])):
            w.writerow(h)
    return outdir


def already_swept(date_iso):
    """Only a CLEAN result counts as done. A TRUNCATED or PROBE_UNRESOLVED day is
    an open question, so a resumed run picks it up again instead of inheriting a
    partial answer forever."""
    mp = os.path.join(OUT_ROOT, date_iso, "_sweep.meta.json")
    if not os.path.exists(mp):
        return False
    try:
        return json.load(open(mp)).get("status") in ("SWEPT", "NO_RELEASE_FOR_THIS_DATE")
    except Exception:
        return False


def open_hits(date_iso):
    """`hits.csv` and `hits.csv.gz` are the SAME EVIDENCE in two containers.
    Sweeps before 26 Aug 2026 wrote the plain form and are left exactly as they
    are -- nothing that is already evidence gets rewritten to save space."""
    d = os.path.join(OUT_ROOT, date_iso)
    for name in ("hits.csv.gz", "hits.csv"):
        p = os.path.join(d, name)
        if os.path.exists(p):
            return gzip.open(p, "rt", newline="") if p.endswith(".gz") else open(p, newline="")
    return None


# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--date", action="append", help="sweep only this UTC date (repeatable)")
    ap.add_argument("--radius", type=float, default=50.0, help="circle radius in miles")
    ap.add_argument("--window", type=int, default=1, help="+/- days around each event date")
    ap.add_argument("--max-dates", type=int, default=0)
    ap.add_argument("--no-controls", action="store_true")
    ap.add_argument("--no-prefilter", action="store_true",
                    help="parse every aircraft; slow, used to verify the pre-filter")
    ap.add_argument("--repull", action="store_true", help="re-sweep dates already on disk")
    ap.add_argument("--jobs", type=int, default=1,
                    help="sweep this many UTC dates at once. The work is roughly "
                         "half wire and half CPU, so 3-6 is the useful range on a "
                         "laptop; more than that just starves the download.")
    args = ap.parse_args()

    by_date, meta = build_targets(args.radius, args.window, controls=not args.no_controls)
    order = priority(by_date, meta)
    if args.date:
        order = [d for d in order if d in set(args.date)]
        for d in args.date:                      # allow a date with no event circle
            if d not in by_date:
                print(f"  {d}: no event circle on this date; controls only")
                by_date[d] = [dict(c, sweep_date=d) for c in
                              next(iter(by_date.values())) if c["kind"] == "control"]
                order.append(d)
    if not args.repull:
        order = [d for d in order if not already_swept(d)]
    if args.max_dates:
        order = order[:args.max_dates]

    os.makedirs(OUT_ROOT, exist_ok=True)
    with open(os.path.join(OUT_ROOT, "targets.json"), "w") as fh:
        json.dump({"built_utc": utcnow(),
                   "radius_mi": args.radius, "window_days": args.window,
                   "event_days_on_map": len(meta["events"]),
                   "utc_dates": len(by_date),
                   "controls": meta["controls"],
                   "archive_floor": meta["archive_floor"],
                   "not_swept_no_exact_date": [
                       {"dates": r["dates"], "city": r["city"], "state": r["state"],
                        "title": r.get("title")} for r in meta["undated"]],
                   "not_swept_not_geocodable": [
                       {"dates": r["dates"], "city": r["city"], "state": r["state"]}
                       for r in meta["ungeocoded"]],
                   "dates": {d: [{"key": c["key"], "kind": c["kind"], "city": c.get("city"),
                                  "state": c.get("state"), "lat": c["lat"], "lon": c["lon"],
                                  "offset_days": c.get("offset_days")}
                                 for c in cs] for d, cs in by_date.items()}}, fh, indent=2)

    if args.report:
        return report()

    if args.plan or not args.run:
        print(f"{len(meta['events'])} US event-days on the map "
              f"({len(meta['undated'])} rows name no exact date, "
              f"{len(meta['ungeocoded'])} cannot be geocoded)")
        print(f"{len(by_date)} UTC dates in the target set at radius {args.radius} mi, "
              f"window +/-{args.window} d, {len(meta['controls'])} control cities per date")
        print(f"{len(order)} dates still to sweep\n")
        for d in order[:40]:
            ev = [c for c in by_date[d] if c["kind"] == "event"]
            print(f"  {d}  " + (", ".join(f"{c['city']},{c['state']}" for c in ev) or "(controls only)"))
        if len(order) > 40:
            print(f"  ... and {len(order) - 40} more")
        return

    jobs = [(i, len(order), d, by_date[d], not args.no_prefilter)
            for i, d in enumerate(order, 1)]
    if args.jobs > 1:
        from concurrent.futures import ProcessPoolExecutor, as_completed
        with ProcessPoolExecutor(max_workers=args.jobs) as ex:
            futs = [ex.submit(_worker, j) for j in jobs]
            for f in as_completed(futs):        # report as they land, not in order
                print(f.result(), flush=True)
    else:
        for j in jobs:
            print(_worker(j), flush=True)


def report():
    days = sorted(d for d in os.listdir(OUT_ROOT)
                  if os.path.isdir(os.path.join(OUT_ROOT, d)))
    tot = flagged = 0
    ev_f = ct_f = 0
    for d in days:
        fh = open_hits(d)
        if fh is None:
            continue
        for r in csv.DictReader(fh):
            tot += 1
            if r["flagged"] == "True":
                flagged += 1
                if r["circle_kind"] == "event":
                    ev_f += 1
                else:
                    ct_f += 1
    print(f"{len(days)} UTC days swept")
    print(f"{tot} circle entries, {flagged} by flagged aircraft")
    print(f"  flagged inside EVENT circles:   {ev_f}")
    print(f"  flagged inside CONTROL circles: {ct_f}   <- the comparison that makes the "
          f"first number mean anything")


if __name__ == "__main__":
    main()
