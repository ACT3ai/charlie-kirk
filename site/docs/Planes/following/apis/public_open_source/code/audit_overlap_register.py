#!/usr/bin/env python3
"""Prove that every claimed overlap is still there, end to end.

WHY THIS EXISTS
---------------
The overlap register is the spine of the following-planes investigation, and its
headline is a COUNT. That makes it uniquely easy to damage without noticing: a
row that quietly stops being published looks exactly like a row that was never
claimed, and the only visible symptom is a number that got smaller. This site
spent a page-load arguing that a compilation's count was unreliable; it cannot
afford the same charge.

So this walks the whole chain for every row and fails loudly if any link breaks:

    overlaps.csv  ->  a page on disk  ->  a row in pages.csv  ->  HTML in build/
                  ->  tracked in git (the live site builds from the REPO, so an
                      untracked page renders locally and 404s for every visitor)
                  ->  a verdict from the recovered traces
                  ->  a bar or a ghost block in the infographic

It also checks the register against ITSELF: no duplicate ids, no gaps in any id
series, and the attendee and tail breakdowns each summing to the row total.

NOTHING HERE DELETES OR REPAIRS ANYTHING. It reports. A row that has gone
missing is a fact to investigate, never something to tidy away by adjusting the
expected total.

    python3 audit_overlap_register.py            exit 0 clean, 1 findings
    python3 audit_overlap_register.py --verbose  print the per-row chain
"""
from __future__ import annotations

import argparse
import collections
import csv
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
FOLLOWING = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
ROOT = os.path.normpath(os.path.join(FOLLOWING, "..", "..", "..", ".."))
OVERLAPS_CSV = os.path.join(FOLLOWING, "overlaps.csv")
PAGES_CSV = os.path.join(ROOT, "pages.csv")
BUILD = os.path.join(ROOT, "site", "build")
SVG = os.path.join(ROOT, "site/internals/static/img/infographics/Overlap_Timeline.svg")
INDEX_MDX = os.path.join(FOLLOWING, "overlap", "overview.mdx")

# Verdict -> fill class, kept in step with generate_overlap_timeline.py.
FILL = {"AT_CLAIMED_AIRPORT": "C", "SAME_METRO_WRONG_FIELD": "M", "ELSEWHERE": "R",
        "NOT_HEARD": "U", "NO_ARCHIVE_COVERAGE": "U", "NOT_QUERIED": "U",
        "NO_TAIL_CLAIMED": "N"}

findings = []


def fail(msg):
    findings.append(msg)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    rows = list(csv.DictReader(open(OVERLAPS_CSV, newline="", encoding="utf-8")))
    n = len(rows)
    print(f"register: {n} rows in overlaps.csv")

    # ── the register against itself ─────────────────────────────────────────
    dups = [k for k, v in collections.Counter(r["overlap_id"] for r in rows).items() if v > 1]
    if dups:
        fail(f"duplicate overlap_id values: {dups}")
    series = collections.defaultdict(list)
    for r in rows:
        pre, _, num = r["overlap_id"].partition("-")
        if num.isdigit():
            series[pre].append(int(num))
    for pre, nums in sorted(series.items()):
        gaps = [i for i in range(1, max(nums) + 1) if i not in nums]
        print(f"  {pre}-001..{max(nums):03d}  {len(nums):3} rows  gaps={gaps or 'none'}")
        if gaps:
            fail(f"{pre} id series has gaps: {gaps} - a claimed overlap may have been dropped")

    ac = collections.Counter(r["attendee_class"] for r in rows)
    if sum(ac.values()) != n:
        fail(f"attendee_class breakdown sums to {sum(ac.values())}, not {n}")

    def tail_class(r):
        t = r["foreign_tail"]
        if t in ("SU-BTT", "SU-BND"):
            return t
        if ";" in t:
            return "both"
        if " or " in t:
            return "or"
        return "none"
    tc = collections.Counter(tail_class(r) for r in rows)
    if sum(tc.values()) != n:
        fail(f"tail breakdown sums to {sum(tc.values())}, not {n}")

    # ── the publication chain, per row ──────────────────────────────────────
    by_file = {r["file_path"]: r for r in csv.DictReader(open(PAGES_CSV, newline="", encoding="utf-8"))}
    tracked = set(subprocess.run(["git", "-C", ROOT, "ls-files",
                                 "site/docs/Planes/following/overlap/"],
                                capture_output=True, text=True).stdout.split("\n"))
    index_txt = open(INDEX_MDX, encoding="utf-8").read() if os.path.exists(INDEX_MDX) else ""

    for r in rows:
        rid, fp = r["overlap_id"], r["overlap_page"]
        if not fp:
            fail(f"{rid}: no overlap_page recorded")
            continue
        abs_fp = os.path.join(ROOT, fp)
        chain = []
        chain.append("disk" if os.path.exists(abs_fp) else fail(f"{rid}: page missing on disk - {fp}") or "DISK!")
        chain.append("pages.csv" if fp in by_file else fail(f"{rid}: not in pages.csv - {fp}") or "CSV!")
        chain.append("git" if fp in tracked else fail(f"{rid}: NOT TRACKED IN GIT - renders locally, 404s for visitors - {fp}") or "GIT!")
        built = os.path.join(BUILD, fp.replace("site/docs/", "").replace("/overview.mdx", "/overview.html"))
        if os.path.exists(BUILD):
            chain.append("build" if os.path.exists(built) else fail(f"{rid}: not in build/ - {built}") or "BUILD!")
        slug = fp.rstrip("/").split("/")[-2] if "/" in fp else fp
        chain.append("index" if (slug in index_txt or rid in index_txt) else fail(f"{rid}: not linked from overlap/overview.mdx") or "INDEX!")
        if not r["adsb_verified_verdict"].strip():
            fail(f"{rid}: no adsb_verified_verdict - never tested against the recovered traces")
        if args.verbose:
            print(f"    {rid:12} {' -> '.join(chain)}")

    if not os.path.exists(BUILD):
        print("  (build/ absent - skipped the built-HTML check; run `npm run build` first)")

    # ── pages with no row ───────────────────────────────────────────────────
    import glob
    have = {r["overlap_page"] for r in rows}
    for p in glob.glob(os.path.join(FOLLOWING, "overlap", "*", "overview.mdx")):
        rel = os.path.relpath(p, ROOT)
        if rel not in have:
            fail(f"orphan page with no register row: {rel}")

    # ── the infographic accounts for every row ──────────────────────────────
    plotted = collections.Counter()
    undated = 0
    for r in rows:
        d = r["date"].strip()
        if len(d) < 7 or d == "UNKNOWN":
            undated += 1
        else:
            plotted[FILL.get(r["adsb_verified_verdict"], "U")] += 1
    total_plotted = sum(plotted.values())
    print(f"\ninfographic: {total_plotted} plotted as bars + {undated} ghosted = "
          f"{total_plotted + undated}")
    if total_plotted + undated != n:
        fail(f"infographic accounts for {total_plotted + undated} rows, register holds {n}")

    if os.path.exists(SVG):
        svg = open(SVG, encoding="utf-8").read()
        drawn = {
            "C": len(re.findall(r'<rect x="[\d.]+" y="[\d.]+" width="17" height="40" fill="#[0-9a-f]{6}"/>', svg)),
            "M": len(re.findall(r'width="17" height="40" fill="url\(#hatch', svg)),
            "R": len(re.findall(r'width="15.4" height="38.4" fill="none" stroke="#(?:e0a33e|6ea8d8)" stroke-width="1.6"', svg)),
        }
        dotted = len(re.findall(r'width="15.4" height="38.4" fill="none" stroke="#(?:e0a33e|6ea8d8)" stroke-width="1.4" stroke-dasharray="3 3"', svg))
        ghost = len(re.findall(r'width="17" height="88" fill="none" stroke="#6e6e77"', svg))
        for k in ("C", "M", "R"):
            if drawn[k] != plotted[k]:
                fail(f"SVG draws {drawn[k]} '{k}' blocks, register has {plotted[k]}")
        if dotted != plotted["U"] + plotted["N"]:
            fail(f"SVG draws {dotted} dotted blocks, register has {plotted['U'] + plotted['N']}")
        if ghost != undated:
            fail(f"SVG draws {ghost} ghost blocks, register has {undated} undated rows")
        print(f"  SVG blocks: solid={drawn['C']} hatch={drawn['M']} outline={drawn['R']} "
              f"dotted={dotted} ghost={ghost}")

    # ── result ──────────────────────────────────────────────────────────────
    print()
    if findings:
        print(f"{len(findings)} FINDING(S) - a claimed overlap is not fully published:")
        for f in findings:
            print(f"  * {f}")
        print("\nDo NOT resolve these by lowering an expected total. Find the row.")
        return 1
    print(f"CLEAN: all {n} claimed overlaps are present, published, tracked, tested and charted.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
