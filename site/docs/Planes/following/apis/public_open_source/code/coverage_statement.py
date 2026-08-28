#!/usr/bin/env python3
"""THE HONEST COVERAGE STATEMENT — what did we ASK, and what do we HOLD?

Reads ONLY what is already on disk. Makes no network request of any kind.

Three states, and merging any two of them is how an investigation destroys its
own credibility:

  HELD        an archive returned a payload for that (tail, UTC day).
  ASKED_NONE  an archive was queried and had nothing. A COVERAGE FACT. It is
              NOT evidence the aircraft was elsewhere -- transponder off, out of
              receiver range, and a wrong claimed date all look identical here.
  NEVER_ASKED nobody queried it. An open question, not a finding.

Inputs, all under site/docs/Planes:
  <TAIL>/data/recovered/*.meta.json                  every per-tail ask ever made
  following/tpusa_events.csv                         the sourced event calendar
  following/overlaps.csv                             the claimed overlaps
  following/apis/.../data/geo_sweep/<DATE>/_sweep.meta.json   the sweep audit
  following/apis/.../data/analysis/recovery_ledger.csv

Usage:
  python3 coverage_statement.py            full report to stdout
  python3 coverage_statement.py --json     machine-readable summary
"""
import collections, csv, datetime, glob, gzip, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PLANES = os.path.normpath(os.path.join(HERE, "..", "..", "..", ".."))
FOLL = os.path.join(PLANES, "following")
POS = os.path.join(FOLL, "apis", "public_open_source")
GS = os.path.join(POS, "data", "geo_sweep")
AN = os.path.join(POS, "data", "analysis")

CORE = ["N102DZ", "N40JD", "N560TW", "N582MM", "N872RA", "N888KG",
        "SU-BGM", "SU-BND", "SU-BTT", "SU-BTU", "SU-BTV", "T7-ELL"]
ALL_TAILS = CORE + ["N1098L", "N2100L", "N59906", "N55906"]


def load_asks():
    """Every per-tail ask on disk. A payload beside the .meta.json means HELD."""
    recs, corrupt = [], []
    for f in glob.glob(os.path.join(PLANES, "*", "data", "recovered", "*.meta.json")):
        txt = open(f).read()
        try:
            m = json.loads(txt)
        except Exception:
            try:                                    # a double-written file
                m = json.JSONDecoder().raw_decode(txt)[0]
                corrupt.append(f)
            except Exception:
                corrupt.append(f)
                continue
        recs.append(dict(
            tail=(m.get("tail") or os.path.basename(f).split("_")[0]).upper(),
            date=m.get("utc_date") or m.get("date_utc") or "",
            src=m.get("source") or m.get("source_key") or "",
            held=os.path.exists(f[: -len(".meta.json")]),
            status=m.get("http_status") or m.get("status") or "",
            path=f))
    return recs, corrupt


def sweep_status():
    out = {}
    for d in sorted(glob.glob(os.path.join(GS, "20*"))):
        p = os.path.join(d, "_sweep.meta.json")
        if os.path.exists(p):
            out[os.path.basename(d)] = json.load(open(p))
    return out


def main():
    recs, corrupt = load_asks()
    sw = sweep_status()
    asked = collections.defaultdict(lambda: {"a": set(), "h": set()})
    for r in recs:
        if not r["date"]:
            continue
        asked[(r["tail"], r["date"])]["a"].add(r["src"])
        if r["held"]:
            asked[(r["tail"], r["date"])]["h"].add(r["src"])

    rep = {}

    # ---- 1. per archive -------------------------------------------------
    per = collections.defaultdict(lambda: [0, 0])
    for r in recs:
        per[r["src"]][0] += 1
        per[r["src"]][1] += 1 if r["held"] else 0
    rep["per_archive"] = {k: {"asked": v[0], "held": v[1], "asked_none": v[0] - v[1]}
                          for k, v in sorted(per.items())}

    # ---- 2. per year ----------------------------------------------------
    yr = collections.defaultdict(lambda: [0, 0])
    for (t, d), v in asked.items():
        yr[d[:4]][0] += 1
        yr[d[:4]][1] += 1 if v["h"] else 0
    rep["pairs_by_year"] = {k: {"asked": v[0], "any_held": v[1]} for k, v in sorted(yr.items())}

    # ---- 3. per tail ----------------------------------------------------
    tl = collections.defaultdict(lambda: [0, 0])
    for (t, d), v in asked.items():
        tl[t][0] += 1
        tl[t][1] += 1 if v["h"] else 0
    rep["pairs_by_tail"] = {k: {"asked": v[0], "any_held": v[1]} for k, v in sorted(tl.items())}

    # ---- 4. miss HTTP status --------------------------------------------
    st = collections.Counter((r["src"], str(r["status"])) for r in recs if not r["held"])
    rep["miss_http_status"] = {f"{a}|{b}": c for (a, b), c in sorted(st.items())}

    # ---- 5. event-window coverage ---------------------------------------
    ev = list(csv.DictReader(open(os.path.join(FOLL, "tpusa_events.csv"))))
    def d0(s):
        try:
            return datetime.date.fromisoformat(s[:10])
        except Exception:
            return None
    cells = collections.Counter()
    per_year = collections.defaultdict(collections.Counter)
    windates = set()
    for r in ev:
        d = d0(r["dates"])
        if not d:
            continue
        for o in (-1, 0, 1):
            windates.add((d + datetime.timedelta(days=o)).isoformat())
    for x in sorted(windates):
        for t in CORE:
            k = (t, x)
            s = "NEVER_ASKED" if k not in asked else ("HELD" if asked[k]["h"] else "ASKED_NONE")
            cells[s] += 1
            per_year[x[:4]][s] += 1
    rep["event_window_cells"] = dict(cells)
    rep["event_window_cells_by_year"] = {k: dict(v) for k, v in sorted(per_year.items())}

    dark = []
    for r in ev:
        d = d0(r["dates"])
        if not d:
            continue
        ds = [(d + datetime.timedelta(days=o)).isoformat() for o in (-1, 0, 1)]
        if not any(asked.get((t, x), {}).get("h") for t in CORE for x in ds):
            dark.append(dict(date=r["dates"][:10], city=r["city"], state=r["state"], who=r["who"]))
    rep["event_days_with_no_per_tail_data"] = dark

    # ---- 6. sweep audit --------------------------------------------------
    stat = collections.Counter(m["status"] for m in sw.values())
    rep["sweep_status"] = dict(stat)
    bad = {d: m for d, m in sw.items() if m["status"] != "SWEPT"}
    rep["sweep_failures"] = {
        d: dict(status=m["status"], curl_exit=m.get("curl_exit"),
                expected=m.get("archive_bytes_expected"),
                got=m.get("archive_bytes_read_from_wire"),
                events=[f"{c['city']},{c['state']} {c['event_date']}"
                        for c in m["circles"] if c["kind"] == "event"])
        for d, m in sorted(bad.items())}
    # the last-digit signature: sweep order is sorted on the REVERSED date
    # string (lib/targets.py rank(), `d[::-1]`), so days whose day-of-month ends
    # in 8 or 9 are processed LAST. The failures are positional, not date-specific.
    dig_all = collections.Counter(int(d[-1]) for d in sw)
    dig_bad = collections.Counter(int(d[-1]) for d, m in sw.items()
                                  if m["status"] in ("TRUNCATED", "PROBE_UNRESOLVED"))
    rep["sweep_failure_by_last_digit_of_day"] = {
        str(k): {"dates": dig_all[k], "failed": dig_bad[k]} for k in range(10)}

    # event-days a sweep failure cost us entirely
    circ = collections.defaultdict(dict)
    for d, m in sw.items():
        for c in m["circles"]:
            if c["kind"] == "event":
                circ[(c["event_date"], c["city"], c["state"])][d] = m["status"]
    lost = {f"{k[0]} {k[1]},{k[2]}": v for k, v in circ.items()
            if not any(s == "SWEPT" for s in v.values())}
    rep["event_circles_with_no_clean_sweep_day"] = lost

    # ---- 7. claimed overlaps --------------------------------------------
    ov = list(csv.DictReader(open(os.path.join(FOLL, "overlaps.csv"))))
    rep["overlap_verdicts"] = dict(collections.Counter(r["adsb_verified_verdict"] for r in ov))

    # ---- 8. live-API-vs-own-backup cross check ---------------------------
    led = list(csv.DictReader(open(os.path.join(AN, "recovery_ledger.csv"))))
    oal = [r for r in led if r["verdict"] == "ONLY_ON_AIRPLANES_LIVE"]
    insw = [r for r in oal if sw.get(r["date"], {}).get("status") == "SWEPT"]
    need = collections.defaultdict(set)
    for r in insw:
        need[r["date"]].add(r["tail"].upper())
    found = set()
    for d, tails in need.items():
        p = os.path.join(GS, d, "hits.csv.gz")
        if not os.path.exists(p):
            continue
        with gzip.open(p, "rt", newline="") as fh:
            for row in csv.DictReader(fh):
                if (row["reg"] or "").upper() in tails:
                    found.add(((row["reg"] or "").upper(), d))
    band = collections.Counter()
    for r in insw:
        band[(r["adsb_lol_403_band"], (r["tail"].upper(), r["date"]) in found)] += 1
    rep["live_vs_own_backup"] = {
        "only_on_airplanes_live_rows": len(oal),
        "of_those_on_a_fully_swept_day": len(insw),
        "in_403_band_and_backup_HAS_it": band[("yes", True)],
        "in_403_band_and_backup_lacks_it": band[("yes", False)],
        "outside_band_and_backup_HAS_it": band[("no", True)],
        "outside_band_and_backup_lacks_it": band[("no", False)],
        "recovered_pairs": sorted(found)}

    rep["corrupt_meta_files"] = corrupt

    if "--json" in sys.argv:
        json.dump(rep, sys.stdout, indent=1, default=str)
        print()
        return

    def h(t):
        print("\n" + "=" * 78 + f"\n{t}\n" + "=" * 78)
    h("1. WHAT EACH ARCHIVE WAS ASKED, AND WHAT IT RETURNED")
    print(f"  {'archive':28s} {'ASKED':>7s} {'HELD':>7s} {'ASKED_NONE':>11s}")
    for k, v in rep["per_archive"].items():
        print(f"  {k:28s} {v['asked']:7d} {v['held']:7d} {v['asked_none']:11d}")
    print(f"  {'TOTAL ask records':28s} {sum(v['asked'] for v in rep['per_archive'].values()):7d}")
    print("  NOTE: adsbexchange-samples / wayback / flightaware-activity-log record only HITS.")
    print("        Their 'asked' count is unknowable from disk. Do not read 100% as coverage.")
    h("2. (TAIL, UTC DAY) PAIRS BY YEAR")
    for k, v in rep["pairs_by_year"].items():
        print(f"  {k or '(no date)':10s} asked={v['asked']:6d} any_held={v['any_held']:6d}")
    h("3. EVENT-WINDOW CELLS (12 core tails x every event day +/-1)")
    print(" ", rep["event_window_cells"])
    for k, v in rep["event_window_cells_by_year"].items():
        print(f"  {k}: {dict(v)}")
    print(f"\n  Sourced event-days with ZERO data on ANY core tail across the whole window: "
          f"{len(rep['event_days_with_no_per_tail_data'])}")
    for x in rep["event_days_with_no_per_tail_data"]:
        print("    ", x["date"], x["city"], x["state"], x["who"])
    h("4. GEOGRAPHIC SWEEP AUDIT")
    print(" ", rep["sweep_status"])
    print("\n  failures by last digit of day-of-month (sweep order sorts the REVERSED")
    print("  date string in lib/targets.py rank(), so *8 and *9 run last):")
    for k, v in rep["sweep_failure_by_last_digit_of_day"].items():
        print(f"    ...{k}  dates={v['dates']:4d} failed={v['failed']:4d}")
    print("\n  event circles with no clean sweep day:", len(rep["event_circles_with_no_clean_sweep_day"]))
    for k, v in rep["event_circles_with_no_clean_sweep_day"].items():
        print("    ", k, v)
    h("5. CLAIMED OVERLAPS")
    for k, v in sorted(rep["overlap_verdicts"].items(), key=lambda x: -x[1]):
        print(f"  {k or '(blank)':26s} {v}")
    h("6. adsb.lol LIVE API vs adsb.lol's OWN OFF-SITE BACKUP")
    for k, v in rep["live_vs_own_backup"].items():
        if k != "recovered_pairs":
            print(f"  {k:38s} {v}")
    for p in rep["live_vs_own_backup"]["recovered_pairs"]:
        print("    ", p)
    if corrupt:
        h("7. UNREADABLE ASK RECORDS")
        for c in corrupt:
            print("  ", c)


if __name__ == "__main__":
    main()
