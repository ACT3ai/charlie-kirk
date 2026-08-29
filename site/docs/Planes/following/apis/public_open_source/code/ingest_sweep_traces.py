#!/usr/bin/env python3
"""INGEST THE TRACES THE GEOGRAPHIC SWEEP ALREADY DOWNLOADED.

The sweep keeps the full trace for any TRACKED TAIL it meets, anywhere in a
circle, as a by-product of asking a geographic question. Those files sat under
data/geo_sweep/<date>/traces/<hex>.json.gz and were never filed into the
per-aircraft record, so the per-tail coverage numbers UNDERSTATED what this
investigation actually holds.

This is not new data off the internet. It is data already downloaded, from
adsb.lol's GitHub Release backup, being put where the per-tail lane can see it.
It is copied, never moved -- the sweep directory stays intact as the primary
artifact -- and the source key in the filename is `adsblol-github-backup` so the
provenance is exactly as auditable as every other pull.

    python3 ingest_sweep_traces.py [--dry-run]
"""
import glob, gzip, json, os, re, shutil, sys, collections
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
from atomic import write_json   # atomic: never leave a spliced evidence file

HERE = os.path.dirname(os.path.abspath(__file__))
PLANES = os.path.normpath(os.path.join(HERE, "..", "..", "..", ".."))
SWEEP = os.path.normpath(os.path.join(HERE, "..", "data", "geo_sweep"))
SRC = "adsblol-github-backup"
DRY = "--dry-run" in sys.argv


def fleet():
    js = open(os.path.join(HERE, "lib", "fleet.js")).read()
    return {h: t for t, h in re.findall(r'reg:\s*"([^"]+)",\s*hex:\s*"([0-9a-f]{6})"', js)}


def summarise(trace):
    """Same summary shape the other recovery clients write, so the ledger and
    traces.py read an ingested file exactly like a directly-pulled one."""
    pts = trace.get("trace") or []
    day = f"{trace.get('timestamp')}"
    first = last = wheels_up = wheels_down = None
    prev_ground = None
    import datetime as dt
    base = dt.datetime.fromtimestamp(float(trace["timestamp"]), dt.timezone.utc) if trace.get("timestamp") else None

    def iso(sec):
        if base is None: return None
        return (base + dt.timedelta(seconds=float(sec))).isoformat().replace("+00:00", "Z")

    for p in pts:
        if p[1] is None or p[2] is None: continue
        on_ground = (p[3] == "ground")
        if first is None: first, first_pos = iso(p[0]), [p[1], p[2]]
        last, last_pos = iso(p[0]), [p[1], p[2]]
        if prev_ground is True and not on_ground and wheels_up is None: wheels_up = iso(p[0])
        if prev_ground is False and on_ground and wheels_down is None: wheels_down = iso(p[0])
        prev_ground = on_ground
    return dict(registration=(trace.get("r") or "").strip(), type=(trace.get("t") or "").strip(),
                points=len(pts), first_seen_utc=first, last_seen_utc=last,
                first_pos=locals().get("first_pos"), last_pos=locals().get("last_pos"),
                wheels_up_utc=wheels_up, wheels_down_utc=wheels_down)


def main():
    hx = fleet()
    added = collections.Counter(); skipped = collections.Counter()
    for path in sorted(glob.glob(os.path.join(SWEEP, "*", "traces", "*.json.gz"))):
        date = path.split(os.sep)[-3]
        hexid = os.path.basename(path).split(".")[0].lstrip("~")
        tail = hx.get(hexid)
        if not tail:
            continue
        outdir = os.path.join(PLANES, tail, "data", "recovered")
        stem = f"{tail}_{date}_{SRC}_trace_full.json.gz"
        out = os.path.join(outdir, stem)
        if os.path.exists(out):
            skipped["already_ingested"] += 1
            continue
        # A directly-pulled trace from either live archive is the BETTER artifact
        # (it was fetched for this aircraft, not harvested in passing). Never
        # shadow one -- ingest only where the per-tail lane has nothing.
        if glob.glob(os.path.join(outdir, f"{tail}_{date}_*_trace_full.json*")):
            skipped["per_tail_lane_already_has_this_day"] += 1
            continue
        try:
            with gzip.open(path, "rt") as fh:
                trace = json.load(fh)
        except Exception as e:
            skipped[f"unreadable:{type(e).__name__}"] += 1
            continue
        if DRY:
            added[tail] += 1
            continue
        os.makedirs(outdir, exist_ok=True)
        shutil.copyfile(path, out)
        meta = dict(
            url=f"https://github.com/adsblol/globe_history_{date[:4]}/releases/"
                f"tag/v{date.replace('-', '.')}-planes-readsb-prod-0",
            http_status=200, stored_gzipped=True,
            stored_bytes=os.path.getsize(out),
            retrieved_utc=None, tail=tail, hex=hexid, date_utc=date,
            source=SRC, source_key=SRC,
            source_role="adsb.lol's own off-site mirror of its entire archive, ODbL",
            tool="apis/public_open_source/code/ingest_sweep_traces.py",
            ingested_from=os.path.relpath(path, PLANES),
            note="Downloaded by the GEOGRAPHIC sweep, which streams a whole UTC day "
                 "and keeps the full trace for any tracked tail it meets. Copied here "
                 "so the per-aircraft lane can see it; the sweep copy is untouched. "
                 "Same bytes, same archive, filed under the tail instead of the date.",
            summary=summarise(trace))
        write_json(out + ".meta.json", meta, indent=1)
        added[tail] += 1
    # ---- THE THIRD STATE, AND WHY IT IS NOT "ASKED AND EMPTY" --------------
    # It is tempting to treat "this tail is not in that day's traces/ directory"
    # as an ASK that came back empty. IT IS NOT, and saying so would be exactly
    # the class of false claim this investigation keeps having to retract.
    #
    # geo_sweep.py applies a cheap BYTE PRE-FILTER before an aircraft is ever
    # identified (geo_sweep.py, the `if prefilter and not (...): continue` line
    # in the member loop). A tracked tail whose positions that day fall outside
    # the generated token band is skipped WITHOUT EVER BEING EXAMINED. So an
    # absence from the sweep has two possible causes and we cannot tell them
    # apart from the sweep alone:
    #     (a) the archive genuinely held no trace for that airframe that day
    #     (b) our own filter never looked at it
    # Until 2026-08-28 cause (b) was systematically large: a floor/truncate bug
    # blinded ~28.7% of every event circle's area.
    #
    # So the record written here says NOT_SURFACED_BY_SWEEP, not "asked and
    # empty" -- and where we hold the aircraft's trace for that day from ANOTHER
    # archive, we go further and TEST which cause it was, by replaying that
    # day's token filter against the positions we actually have. That turns an
    # unusable absence into a checkable one.
    from geo_sweep import prefilter_patterns          # noqa: E402
    import traces as _traces                          # noqa: E402

    def _buggy_patterns(circles):
        """The PRE-2026-08-28 token builder, reconstructed exactly.

        It used math.floor() on the coordinate, which is one degree too far west
        on every negative longitude. Kept here ONLY so the cost of that bug can
        be measured against real positions rather than estimated from geometry.
        """
        import math
        lats, lons = set(), set()
        for c in circles:
            pad_lat = c["radius_mi"] / 69.0 + 0.02
            pad_lon = c["radius_mi"] / (69.0 * max(0.15, math.cos(math.radians(c["lat"])))) + 0.02
            lats.update(range(int(math.floor(c["lat"] - pad_lat)), int(math.floor(c["lat"] + pad_lat)) + 1))
            lons.update(range(int(math.floor(c["lon"] - pad_lon)), int(math.floor(c["lon"] + pad_lon)) + 1))
        return ({f",{n}." for n in lats}, {f",{n}." for n in lons})

    def _load_trace(tail, date):
        outdir = os.path.join(PLANES, tail, "data", "recovered")
        cand = [p for p in glob.glob(os.path.join(outdir, f"{tail}_{date}_*_trace_full.json*"))
                if not p.endswith(".meta.json")]
        if not cand:
            return None
        try:
            with _traces.open_trace(sorted(cand)[0]) as fh:
                return json.load(fh)
        except Exception:
            return None

    def _passes(doc, lat_tok, lon_tok):
        for p in doc.get("trace") or ():
            if len(p) < 3 or p[1] is None or p[2] is None:
                continue
            if (f",{p[1]:.6f}".split(".")[0] + ".") in lat_tok and \
               (f",{p[2]:.6f}".split(".")[0] + ".") in lon_tok:
                return True
        return False

    def _would_have_passed(tail, date, circles):
        """(fixed_filter_passes, buggy_filter_passes) or (None, None).

        Comparing the two is the whole point: `fixed and not buggy` is an
        aircraft-day the shipped sweep provably lost to our own bug.
        """
        doc = _load_trace(tail, date)
        if doc is None:
            return None, None
        pl, po = prefilter_patterns(circles)
        fixed = _passes(doc, {t.decode() for t in pl}, {t.decode() for t in po})
        bl, bo = _buggy_patterns(circles)
        buggy = _passes(doc, bl, bo)
        return fixed, buggy

    verdicts = collections.Counter()
    for meta_path in sorted(glob.glob(os.path.join(SWEEP, "*", "_sweep.meta.json"))):
        try:
            sm = json.load(open(meta_path))
        except Exception:
            continue
        if sm.get("status") != "SWEPT":
            continue                      # TRUNCATED / NO_RELEASE / UNRESOLVED is NOT an ask
        date = sm["sweep_date"]
        circles = sm.get("circles") or []
        tdir = os.path.join(os.path.dirname(meta_path), "traces")
        present = {os.path.basename(p).split(".")[0].lstrip("~")
                   for p in glob.glob(os.path.join(tdir, "*.json.gz"))}
        for hexid, tail in hx.items():
            if hexid in present:
                continue
            outdir = os.path.join(PLANES, tail, "data", "recovered")
            out = os.path.join(outdir, f"{tail}_{date}_{SRC}_trace_full.miss.json.meta.json")
            if os.path.exists(out):
                continue
            if glob.glob(os.path.join(outdir, f"{tail}_{date}_{SRC}_trace_full.json*")):
                continue
            passed, buggy = (_would_have_passed(tail, date, circles)
                             if circles else (None, None))
            if passed is True and buggy is False:
                verdict = "LOST_TO_OUR_PREFILTER_BUG"
                note = ("NOT AN ARCHIVE FACT AND NOT AN AIRCRAFT FACT. We hold this airframe's "
                        "trace for this date from another archive. Replayed against those real "
                        "positions, the FIXED byte pre-filter surfaces the file and the "
                        "pre-2026-08-28 filter — which used math.floor() and so shifted every "
                        "negative longitude one degree west — REJECTS it. This aircraft-day was "
                        "inside a swept circle's reach and the shipped sweep lost it to our own "
                        "bug. Re-running this date would recover it.")
            elif passed is True:
                verdict = "ARCHIVE_HELD_NOTHING"
                note = ("The sweep streamed this whole UTC day and this airframe was not in it. "
                        "We hold its trace for this date from another archive, and BOTH the "
                        "fixed and the old pre-filter would have surfaced it. The absence is "
                        "therefore the backup archive's, not our filter's. It still is not "
                        "evidence the aircraft was elsewhere: AN ABSENCE IS NOT A FINDING.")
            elif passed is False:
                verdict = "NOT_NEAR_ANY_SWEPT_CIRCLE"
                note = ("Correct rejection, not a gap. We hold this airframe's trace for this "
                        "date from another archive and none of its positions fall in any circle "
                        "swept that day — the aircraft was simply somewhere else. The sweep was "
                        "right to skip it.")
            else:
                verdict = "NOT_SURFACED_BY_SWEEP"
                note = ("The sweep streamed this whole UTC day and this airframe was not among "
                        "the traces it kept. TWO CAUSES ARE INDISTINGUISHABLE FROM HERE: the "
                        "archive held nothing, or our byte pre-filter skipped the file before "
                        "identifying it. We hold no trace for this aircraft-day from any other "
                        "archive, so the two cannot be separated. This is NOT 'asked and empty' "
                        "and must never be counted as one.")
            verdicts[verdict] += 1
            if DRY:
                continue
            os.makedirs(outdir, exist_ok=True)
            write_json(out, dict(
                url=f"https://github.com/adsblol/globe_history_{date[:4]}/releases/"
                    f"tag/v{date.replace('-', '.')}-planes-readsb-prod-0",
                http_status=200, bytes=0, tail=tail, hex=hexid, date_utc=date,
                source=SRC, source_key=SRC, verdict=verdict,
                retrieved_utc=sm.get("retrieved_utc"),
                tool="apis/public_open_source/code/ingest_sweep_traces.py",
                aircraft_in_archive=sm.get("aircraft_in_archive"),
                prefilter_replayed_fixed=passed, prefilter_replayed_old=buggy,
                note=note), indent=1)
    print(("DRY RUN -- " if DRY else "") + "sweep-absence records: "
          + json.dumps(dict(verdicts)), file=sys.stderr)

    print(("DRY RUN -- " if DRY else "") + f"ingested {sum(added.values())} aircraft-days", file=sys.stderr)
    for t, n in added.most_common(): print(f"  {t:10}{n:>5}", file=sys.stderr)
    print("skipped:", dict(skipped), file=sys.stderr)


if __name__ == "__main__":
    main()
