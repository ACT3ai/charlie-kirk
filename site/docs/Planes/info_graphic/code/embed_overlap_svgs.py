#!/usr/bin/env python3
"""Put each Plane Overlap SVG on the overlap page a visitor actually reads.

WHERE IT GOES, and why not at the top. The top of an overlap page is where the
page says what was CLAIMED and what the recovered data says back. A picture
placed above that reads as the page's headline, and this picture is not the
headline — on most of these rows it is the thing that WEAKENS the claim, and a
reader has to have read the claim before the weakening means anything. So the
graphic lands about 30% of the way down, at the first section boundary past that
mark, after the verdict and before the detail tables.

IDEMPOTENT. Everything it writes sits between CK_OVERLAP_SVG markers and a
re-run replaces that block in place. It never writes inside another generator's
markers and it never writes inside a table.

  python3 embed_overlap_svgs.py            write
  python3 embed_overlap_svgs.py --check    report what would change, write nothing
"""
from __future__ import annotations

import csv
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
PLANES = os.path.normpath(os.path.join(HERE, "..", ".."))
REPO = os.path.normpath(os.path.join(PLANES, "..", "..", ".."))
OUT_ROOT = os.path.join(REPO, "site", "internals", "static", "img", "infographics", "overlaps")
WINDOWS = os.environ.get("CK_WINDOWS_JSON", "/tmp/ck_windows.json")

START = "{/* CK_OVERLAP_SVG:START */}"
END = "{/* CK_OVERLAP_SVG:END */}"
# Fraction of the page body the graphic sits after. Not at the top: see the
# module docstring. It snaps forward to the next section heading from here.
TARGET_FRACTION = 0.30
# ...and never above this, whatever the section boundaries look like. The one
# instruction about placement is "not at the very top".
FLOOR_FRACTION = 0.18

PERSON_TEXT = {"charlie": "Charlie Kirk", "erika": "Erika Kirk",
               "both": "Charlie and Erika Kirk"}


def load_yaml(path):
    """The handful of keys this script needs, read without a YAML dependency.

    Deliberately narrow: it reads only what it prints, so a change to the yaml
    shape shows up as a missing key here rather than as a wrong sentence on a
    public page.
    """
    txt = open(path, encoding="utf-8").read()
    out = {"segments": [], "kirk_segments": 0, "kirk_absent": False}
    out["tail"] = re.search(r"following_plane:\s*\n\s*tail:\s*(\S+)", txt).group(1)
    out["type"] = re.search(r"following_plane:\s*\n\s*tail:.*\n\s*type:\s*(.+)", txt).group(1).strip()
    out["person"] = re.search(r"^person:\s*(\S+)", txt, re.M).group(1)
    out["airport"] = re.search(r"^\s*code:\s*(\S+)", txt, re.M).group(1)
    out["airport_name"] = re.search(r"^\s*name:\s*(.+)$", txt, re.M).group(1).strip()
    out["date"] = re.search(r"^date:\s*(\S+)", txt, re.M).group(1)
    foll, _, kirk = txt.partition("kirk_plane:")
    out["segments"] = re.findall(r"basis:\s*(\S+)", foll)
    out["kirk_absent"] = "no_aircraft_in_record: true" in kirk
    out["kirk_tail"] = None if out["kirk_absent"] else \
        (re.search(r"tail:\s*(\S+)", kirk).group(1) if re.search(r"tail:\s*(\S+)", kirk) else None)
    out["kirk_segments"] = len(re.findall(r"basis:\s*\S+", kirk))
    m = re.search(r"queried_tails:\s*(.+)", kirk)
    out["queried"] = m.group(1).strip() if m else ""
    return out


def alt_text(y):
    """Long and literal. On an evidence site this is not a place to be brief."""
    ng = sum(1 for b in y["segments"] if b == "ground_contact")
    npass = len(y["segments"]) - ng
    parts = ["A 16:9 timeline chart titled “Following plane overlaps with %s”."
             % PERSON_TEXT[y["person"]],
             "The right-hand block names %s, and the year %s."
             % (y["airport_name"], y["date"][:4]),
             "A shared time axis runs left to right across the lower half, with two bars on it."]
    bar = []
    if ng:
        bar.append("%d solid dark-red block%s marking the window%s %s was heard on the ground at the field"
                   % (ng, "" if ng == 1 else "s", "" if ng == 1 else "s", y["tail"]))
    if npass:
        bar.append("%d hatched block%s marking %s heard airborne within 15 km of the field, which is not a landing"
                   % (npass, "" if npass == 1 else "s", y["tail"] if not ng else "it"))
    parts.append("The upper bar is the following aircraft, %s (%s): %s." % (y["tail"], y["type"], " and ".join(bar)))
    if y["kirk_absent"]:
        parts.append("The lower bar is a hollow dashed band labelled “NO AIRCRAFT IN THE RECORD”, "
                     "spanning the whole axis, because no Kirk-party airframe was heard on the ground at "
                     "this field on this date. The tails queried are printed inside it.")
    else:
        parts.append("The lower bar is the Kirk-party aircraft %s, in bright yellow, with %d ground window%s."
                     % (y["kirk_tail"], y["kirk_segments"], "" if y["kirk_segments"] == 1 else "s"))
    parts.append("A caption states that these are ADS-B positions heard by volunteer receivers and that "
                 "they place no person aboard any aircraft.")
    return " ".join(parts)


def caption(y):
    """The sentence under the picture. It says what the picture does NOT show."""
    ng = sum(1 for b in y["segments"] if b == "ground_contact")
    npass = len(y["segments"]) - ng
    bits = []
    if ng and npass:
        bits.append("%s was heard on the ground at %s %d time%s on this date, and airborne within 15 km of "
                    "the field %d time%s. Solid blocks are ground contacts; hatched blocks are airborne "
                    "passes, and a hatched block is not a landing."
                    % (y["tail"], y["airport"], ng, "" if ng == 1 else "s",
                       npass, "" if npass == 1 else "s"))
    elif ng:
        bits.append("%s was heard on the ground at %s %d time%s on this date. Where there are two blocks the "
                    "gap between them is a flight, not a wait — they are never merged."
                    % (y["tail"], y["airport"], ng, "" if ng == 1 else "s"))
    else:
        bits.append("%s was heard **airborne** within 15 km of %s on this date and was never heard on the "
                    "ground there. The hatched bar is an approach, a departure climb or a low pass. **It is "
                    "not evidence the aircraft landed.**" % (y["tail"], y["airport"]))
    if y["kirk_absent"]:
        bits.append("**There is no second bar because there is no second aircraft.** No Kirk-party or "
                    "TPUSA-linked airframe was heard on the ground at this field on this date — queried: %s. "
                    "The claim on this row is a person in a city, and a claimed itinerary is not an aircraft, "
                    "so the absence is drawn as an absence rather than left out." % y["queried"])
    else:
        bits.append("The lower bar is %s, a Kirk-party airframe with its own measured ground window."
                    % y["kirk_tail"])
    bits.append("Times are local to the airport. **A trace proves presence, never purpose, and never "
                "occupancy — nothing here places any person aboard any aircraft.**")
    return " ".join(bits)


def block(dirn, y):
    url = "/img/infographics/overlaps/%s/%s.svg" % (dirn, dirn)
    return "\n".join([
        START,
        "",
        "## The two aircraft on one timeline",
        "",
        "<img src=\"%s\"" % url,
        "     alt=\"%s\"" % alt_text(y).replace('"', "'"),
        "     style={{width:'100%', height:'auto', display:'block', borderRadius:'4px'}}",
        "     loading=\"lazy\" />",
        "",
        caption(y),
        "",
        "*Plotted from the recovered ADS-B traces by "
        "`site/docs/Planes/info_graphic/code/build_overlap_svg.ts`; every time on it is measured, "
        "not drawn. The data behind it is in "
        "[`info.yaml`](/img/infographics/overlaps/%s/info.yaml).*" % dirn,
        "",
        END,
    ])


# Regions written by other generators. Never insert inside one of these.
GUARDED = re.compile(r"\{/\*\s*CK_[A-Z0-9_]+:START\s*\*/\}.*?\{/\*\s*CK_[A-Z0-9_]+:END\s*\*/\}", re.S)


def insert_at(body, lines):
    """Line index of the section boundary NEAREST to TARGET_FRACTION.

    Snapping to a heading matters: dropping an image between a paragraph and the
    table it introduces, or in the middle of a table, produces a page that reads
    as though the picture belongs to the wrong claim.

    NEAREST, not next. Several of these pages carry one enormous section — the
    embedded X posts run 260 lines on the 10 September Provo page — and always
    snapping forward pushed the graphic to 74% down, past most of the page. The
    nearest boundary lands it at 27% there instead. A floor of FLOOR_FRACTION
    keeps it from ever climbing back up to the top of the page, which is the one
    place it must not be.
    """
    guarded = []
    for m in GUARDED.finditer(body):
        guarded.append((body[:m.start()].count("\n"), body[:m.end()].count("\n")))

    def inside(i):
        return any(a <= i <= b for a, b in guarded)

    target = int(len(lines) * TARGET_FRACTION)
    floor = int(len(lines) * FLOOR_FRACTION)
    cands = [i for i, ln in enumerate(lines)
             if ln.startswith("## ") and not inside(i) and i >= floor]
    if not cands:
        cands = [i for i, ln in enumerate(lines) if ln.startswith("## ") and not inside(i)]
    if not cands:
        return None
    return min(cands, key=lambda i: (abs(i - target), i < target))


def main():
    check = "--check" in sys.argv
    recs = json.load(open(WINDOWS))
    ledger = {r["overlap_id"]: r for r in
              csv.DictReader(open(os.path.join(OUT_ROOT, "ledger.csv"), encoding="utf-8"))}

    # overlap_id -> directory, for the built rows AND for the duplicate rows that
    # describe the same overlap. A duplicate row is a second PAGE about the same
    # event, so it gets the same picture; what it must never get is a second
    # directory of its own.
    import build_info_yaml as B
    pages = {}
    for oid, tail, person, dups in B.pick_build(recs):
        dirn = ledger[oid]["dir_name"]
        for o in [oid] + dups:
            pages[o] = dirn

    wrote = skipped = same = 0
    for oid in sorted(pages, key=lambda k: (recs[k]["date"], k)):
        dirn = pages[oid]
        page = recs[oid]["overlap_page"]
        path = os.path.join(REPO, page) if page else ""
        if not page or not os.path.exists(path):
            print("NO PAGE  %-11s %s" % (oid, page or "(overlap_page column empty)"))
            skipped += 1
            continue
        y = load_yaml(os.path.join(OUT_ROOT, dirn, "info.yaml"))
        new = block(dirn, y)
        body = open(path, encoding="utf-8").read()

        if START in body:
            a = body.index(START)
            b = body.index(END) + len(END)
            out = body[:a] + new + body[b:]
            where = "replaced"
        else:
            lines = body.split("\n")
            i = insert_at(body, lines)
            if i is None:
                print("NO ANCHOR %-11s %s - no '## ' heading outside a generated block" % (oid, page))
                skipped += 1
                continue
            out = "\n".join(lines[:i] + [new, ""] + lines[i:])
            where = "inserted before line %d of %d (%.0f%% down)" % (i + 1, len(lines), 100.0 * i / len(lines))
        if out == body:
            same += 1
            print("UNCHANGED %-11s %s" % (oid, dirn))
            continue
        if not check:
            open(path, "w", encoding="utf-8").write(out)
        wrote += 1
        print("%-9s %-11s %-42s %s" % ("WOULD" if check else "WROTE", oid, dirn, where))
    print("\n%d page%s %s, %d unchanged, %d skipped."
          % (wrote, "" if wrote == 1 else "s", "would change" if check else "written", same, skipped))


if __name__ == "__main__":
    main()
