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
        json.dump(meta, open(out + ".meta.json", "w"), indent=1)
        added[tail] += 1
    print(("DRY RUN -- " if DRY else "") + f"ingested {sum(added.values())} aircraft-days", file=sys.stderr)
    for t, n in added.most_common(): print(f"  {t:10}{n:>5}", file=sys.stderr)
    print("skipped:", dict(skipped), file=sys.stderr)


if __name__ == "__main__":
    main()
