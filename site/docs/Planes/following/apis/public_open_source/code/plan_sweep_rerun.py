#!/usr/bin/env python3
"""WHAT STILL NEEDS RE-SWEEPING, AND WHY — a runnable manifest, not a caveat.

Three separate populations of UTC days are incomplete, for three different
reasons, and they need different amounts of network to fix. Leaving that as a
sentence in a page is how it gets forgotten; this writes it down as a list a
person or a cron job can execute.

  1. LOST_TO_OUR_PREFILTER_BUG
     Dates where we can PROVE the shipped sweep dropped a tracked aircraft it
     should have kept, because we hold that aircraft's trace from another
     archive and replaying both filter versions against its real positions
     shows the fixed filter surfaces it and the old one does not. Highest
     value per gigabyte: we know exactly what is there.

  2. TRUNCATED / PROBE_UNRESOLVED
     Dates whose download died partway or never got a clean answer. The server
     reported a full Content-Length on every one, so the data exists on the CDN
     and we simply failed to finish reading it. NOT deletions.

  3. ALL SWEPT DATES (the full re-run)
     Every date swept before 2026-08-28 was swept with the broken filter, which
     blinded an average 28.7% of each event circle's AREA. Population 1 only
     catches the loss among the SIXTEEN TRACKED TAILS — the aircraft we already
     knew to look for. The sweep's whole purpose is finding aircraft nobody
     named, and for those the loss is unmeasurable without redoing the day.

     THIS IS WHY EVERY SWEEP-ONLY COUNT REMAINS A FLOOR.

    python3 plan_sweep_rerun.py             # the plan, and the commands
    python3 plan_sweep_rerun.py --json      # machine-readable manifest
"""
import collections, glob, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PLANES = os.path.normpath(os.path.join(HERE, "..", "..", "..", ".."))
SWEEP = os.path.normpath(os.path.join(HERE, "..", "data", "geo_sweep"))
OUT = os.path.normpath(os.path.join(HERE, "..", "data", "analysis"))


def main():
    lost = collections.defaultdict(list)
    for f in glob.glob(os.path.join(PLANES, "*", "data", "recovered",
                                    "*_adsblol-github-backup_trace_full.miss.json.meta.json")):
        try:
            m = json.load(open(f))
        except Exception:
            continue
        if m.get("verdict") == "LOST_TO_OUR_PREFILTER_BUG":
            lost[m["date_utc"]].append(m["tail"])

    status = {}
    for f in glob.glob(os.path.join(SWEEP, "*", "_sweep.meta.json")):
        try:
            m = json.load(open(f))
        except Exception:
            continue
        status[m["sweep_date"]] = m.get("status")

    failed = sorted(d for d, s in status.items() if s in ("TRUNCATED", "PROBE_UNRESOLVED"))
    swept = sorted(d for d, s in status.items() if s == "SWEPT")
    no_release = sorted(d for d, s in status.items() if s == "NO_RELEASE_FOR_THIS_DATE")

    manifest = {
        "generated_for": "the 2026-08-28 pre-filter fix",
        "priority_1_lost_to_prefilter_bug": {
            "dates": sorted(lost),
            "aircraft_days": sum(len(v) for v in lost.values()),
            "detail": {d: sorted(v) for d, v in sorted(lost.items())},
            "why": "Provably dropped by the old filter; we know what is there.",
        },
        "priority_2_download_failed": {
            "dates": failed,
            "why": ("Download died partway or never resolved. The CDN reported a full "
                    "Content-Length on every one — the asset exists. NOT a deletion."),
        },
        "priority_3_full_resweep": {
            "dates": swept,
            "why": ("Swept with the broken filter. Priority 1 only measures the loss among "
                    "the 16 tracked tails; for UNNAMED aircraft — the sweep's entire "
                    "purpose — the loss cannot be measured without redoing the day. "
                    "UNTIL THIS RUNS, EVERY SWEEP-ONLY COUNT IS A FLOOR."),
        },
        "not_recoverable_by_re_running": {
            "dates": no_release,
            "why": "adsb.lol published no release for these UTC days. A hole in its archive, not ours.",
        },
    }

    p1, p2, p3 = (manifest["priority_1_lost_to_prefilter_bug"],
                  manifest["priority_2_download_failed"],
                  manifest["priority_3_full_resweep"])
    print("=" * 78)
    print("SWEEP RE-RUN MANIFEST")
    print("=" * 78)
    print(f"\nPRIORITY 1 — provably lost to our own pre-filter bug")
    print(f"  {p1['aircraft_days']} aircraft-days across {len(p1['dates'])} UTC dates")
    for d in p1["dates"]:
        print(f"    {d}  {', '.join(p1['detail'][d])}")
    print(f"\n  python3 geo_sweep.py --run " + " ".join(f"--date {d}" for d in p1["dates"][:3]) + " ...")
    print(f"  (or loop: for d in {' '.join(p1['dates'])}; do python3 geo_sweep.py --run --date $d; done)")
    print(f"\nPRIORITY 2 — download failed, asset exists on the CDN: {len(p2['dates'])} dates")
    print("    " + " ".join(p2["dates"][:12]) + (" ..." if len(p2["dates"]) > 12 else ""))
    print(f"\nPRIORITY 3 — full re-sweep with the fixed filter: {len(p3['dates'])} dates")
    print("  This is the one that turns every sweep-only FLOOR into a TOTAL.")
    print("  Cost: roughly 2-5 GB streamed per date, never stored.")
    print(f"\nNOT RECOVERABLE — no release published: {len(manifest['not_recoverable_by_re_running']['dates'])} dates")

    path = os.path.join(OUT, "sweep_rerun_manifest.json")
    json.dump(manifest, open(path, "w"), indent=1)
    print(f"\nwrote {path}")
    if "--json" in sys.argv:
        print(json.dumps(manifest, indent=1))


if __name__ == "__main__":
    main()
