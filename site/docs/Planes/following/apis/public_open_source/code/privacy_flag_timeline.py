#!/usr/bin/env python3
"""When did each aircraft go private? Read it out of the archives' own daily records.

Every readsb trace_full file starts with a small header the archive wrote THAT DAY from its
aircraft database: the registration, the type, the owner/operator string (`ownOp`), and
`dbFlags` - a bit field in which 8 = FAA LADD (Limiting Aircraft Data Displayed) and
4 = PIA (Privacy ICAO Address). Because a header is written per day, the sequence of
headers across a tail's recovered days is a dated history of what the archive's database
said about the aircraft - including the day the privacy flag first appears and the day
the listed owner changes.

This is the free, reproducible route to Bryan Starbuck's question "which planes went
private on which date". It has limits, and they travel with the result:

  * The flag is the ARCHIVE'S copy of the FAA list, refreshed on the archive's schedule.
    A first-flagged day brackets the FAA change; it is not the FAA's effective date.
  * The history is only as dense as the held days. The bracket is
    (last day seen unflagged, first day seen flagged); the real change is somewhere inside.
  * LADD asks commercial trackers (FlightAware, Flightradar24) to stop DISPLAYING an
    aircraft. It deletes nothing, and the volunteer archives read here keep recording it -
    which is exactly why these traces exist for the blocked period.

    python3 privacy_flag_timeline.py [--tails N102DZ,N582MM]

WRITES data/analysis/kirk_side/privacy_flag_timeline.csv (every change, with its bracket)
and privacy_flag_days.csv (one row per tail-day-source header).
"""
import collections, csv, gzip, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "lib"))
from traces import trace_files  # noqa: E402

OUT = os.path.normpath(os.path.join(HERE, "..", "data", "analysis", "kirk_side"))
DEFAULT = ["N102DZ", "N582MM", "N79SC", "N888KG", "T7-ELL", "N560TW", "N40JD", "N872RA",
           "N804MS", "N108MS", "N885LS", "N889LS"]


def flags_text(f):
    if f is None:
        return "not_in_header"
    names = []
    for bit, name in ((1, "military"), (2, "interesting"), (4, "PIA"), (8, "LADD")):
        if f & bit:
            names.append(name)
    return "+".join(names) or "none"


def header(path):
    with open(path, "rb") as fh:
        raw = fh.read()
    if raw[:2] == b"\x1f\x8b":
        raw = gzip.decompress(raw)
    d = json.loads(raw)
    return {k: d.get(k) for k in ("r", "t", "dbFlags", "ownOp", "desc", "year")}


def main():
    a = sys.argv[1:]
    tails = a[a.index("--tails") + 1].split(",") if "--tails" in a else DEFAULT
    days = []
    for tail, day, source, path in trace_files(set(tails)):
        try:
            h = header(path)
        except Exception as e:  # an unreadable payload is reported, never counted as a flag state
            days.append(dict(tail=tail, date=day, source=source, dbFlags="", flags="UNREADABLE:" + type(e).__name__,
                             ownOp="", registration="", file=os.path.basename(path)))
            continue
        days.append(dict(tail=tail, date=day, source=source, dbFlags=h["dbFlags"] if h["dbFlags"] is not None else "",
                         flags=flags_text(h["dbFlags"]), ownOp=h["ownOp"] or "", registration=h["r"] or "",
                         file=os.path.basename(path)))
    days.sort(key=lambda r: (r["tail"], r["date"], r["source"]))
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "privacy_flag_days.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(days[0].keys()))
        w.writeheader()
        w.writerows(days)

    # Changes, per tail and per source (two archives' databases can refresh on different days).
    changes = []
    by = collections.defaultdict(list)
    for r in days:
        if not r["flags"].startswith("UNREADABLE"):
            by[(r["tail"], r["source"])].append(r)
    for (tail, source), rs in sorted(by.items()):
        prev = None
        for r in rs:
            for field in ("flags", "ownOp", "registration"):
                if prev and r[field] != prev[field]:
                    changes.append(dict(tail=tail, source=source, field=field, before=prev[field], after=r[field],
                                        last_day_before=prev["date"], first_day_after=r["date"],
                                        bracket_days=(__import__("datetime").date.fromisoformat(r["date"])
                                                      - __import__("datetime").date.fromisoformat(prev["date"])).days))
            prev = r
        if rs:
            changes.append(dict(tail=tail, source=source, field="summary",
                                before=f"first held {rs[0]['date']} flags={rs[0]['flags']} ownOp={rs[0]['ownOp']}",
                                after=f"last held {rs[-1]['date']} flags={rs[-1]['flags']} ownOp={rs[-1]['ownOp']}",
                                last_day_before="", first_day_after="", bracket_days=len(rs)))
    with open(os.path.join(OUT, "privacy_flag_timeline.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(changes[0].keys()))
        w.writeheader()
        w.writerows(changes)
    for c in changes:
        print(c["tail"], c["source"], c["field"], "|", c["before"], "->", c["after"], "|", c["last_day_before"], c["first_day_after"])


if __name__ == "__main__":
    main()
