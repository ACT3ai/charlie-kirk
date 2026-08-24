#!/usr/bin/env python3
"""THE LAST FREE ROUTE: adsb.lol's own OFF-SITE BACKUP, on GitHub Releases.

For 46 of the 69 alleged overlap dates, BOTH free daily archives returned nothing.
Before that can be written down as "nobody heard it", the one place left has to be
asked: adsb.lol mirrors its entire historical database to public GitHub Releases,
one ~2 GB tar per day, Open Database Licence. The live API and the backup are the
same organisation, so a hit here is not independent corroboration -- but a MISS
here is worth a great deal, because it closes the last free door.

Each date is streamed and filtered WITHOUT being stored: curl pipes the tar into
`tar -x --include '*trace_full_<hex>.json'`, so ~2 GB crosses the wire and only a
matching trace (a few hundred KB) ever touches the disk.

    python3 sweep_github_backup.py                 the 2024-2025 misses
    python3 sweep_github_backup.py --year 2023     the 2023 misses too
    python3 sweep_github_backup.py --date 2024-03-18 --hex 0101d3

Every result, hit or miss, is written to data/recovery/github_backup_sweep.json.
A miss is a finding here, not a failure.
"""
import json, os, subprocess, sys, tempfile, shutil, datetime, glob

CODE   = os.path.dirname(os.path.abspath(__file__))
PLANES = os.path.abspath(os.path.join(CODE, "../../../../"))
RECDIR = os.path.abspath(os.path.join(CODE, "../data/recovery"))
OUT    = os.path.join(RECDIR, "github_backup_sweep.json")
NOW    = datetime.datetime.now(datetime.timezone.utc).isoformat()

argv = sys.argv[1:]
def arg(k, d=None): return argv[argv.index(k) + 1] if k in argv else d
YEAR_FLOOR = arg("--year", "2024")

HEX = {"SU-BTT": "0101d3", "SU-BND": "01003e", "SU-BTU": "0101d0", "SU-BTV": "0101d1",
       "SU-BGM": "010070", "T7-ELL": "50018a", "N102DZ": "a00c85", "N888KG": "ac3c75",
       "N560TW": "a728a8", "N582MM": "a77e75", "N872RA": "abff3c", "N40JD": "a4ab14",
       "N1098L": "a0299e", "N2100L": "a1bbe5", "N59906": "a7c14d", "N55906": "a72351"}

# Which (date -> {tail}) still have nothing after both daily archives were asked.
if arg("--date"):
    work = {arg("--date"): {t for t, h in HEX.items() if h == arg("--hex", "")} or set(HEX)}
else:
    an = json.load(open(os.path.join(RECDIR, "overlap_recovery_analysis.json")))
    work = {}
    for r in an["rows"]:
        if r.get("points"): continue                      # already recovered
        if r["date"][:4] < YEAR_FLOOR: continue           # archives do not reach there
        work.setdefault(r["date"], set()).add(r["tail"])

dates = sorted(work)
print(f"{len(dates)} dates to ask adsb.lol's off-site backup about "
      f"(~2 GB streamed each, nothing stored unless it hits)\n")


def list_assets(repo, tag):
    """Which files does this release actually ship? Returns them in sort order, so
    a split tar (`.tar.aa`, `.tar.ab`, ...) concatenates back into one stream."""
    import urllib.request, urllib.error
    api = f"https://api.github.com/repos/{repo}/releases/tags/{tag}"
    req = urllib.request.Request(api, headers={"Accept": "application/vnd.github+json",
                                               "User-Agent": "ck-recovery"})
    tok = os.environ.get("GITHUB_TOKEN")
    if tok: req.add_header("Authorization", f"Bearer {tok}")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            j = json.load(r)
    except Exception:
        return []
    return sorted(a["name"] for a in j.get("assets", []) if ".tar" in a["name"])


def write_out(results, dates):
    with open(OUT, "w") as f:
        json.dump({"generated_utc": NOW, "year_floor": YEAR_FLOOR,
                   "what_this_is": "adsb.lol's off-site GitHub Release backup, asked about every "
                                   "alleged-overlap date that both free daily archives missed",
                   "reading": "A MISS here means adsb.lol's feeders genuinely recorded nothing for that "
                              "aircraft that day. It is not evidence of removal, and it is not "
                              "independent of the adsb.lol live API -- same organisation, same data.",
                   "note_on_split_releases": "Most days ship the tar SPLIT into .tar.aa/.tar.ab. An "
                                             "earlier run of this script asked for a single .tar, got "
                                             "404, and recorded 16 dates as unavailable that are in "
                                             "fact published. The asset list is now read from the API.",
                   "dates": len(dates), "results": results}, f, indent=2)
        f.write("\n")

results = []
for i, date in enumerate(dates, 1):
    tails = sorted(t for t in work[date] if t in HEX)
    tag = f"v{date.replace('-', '.')}-planes-readsb-prod-0"
    repo = f"adsblol/globe_history_{date[:4]}"
    # THE RELEASE IS OFTEN SPLIT. Most days ship `<tag>.tar.aa` + `<tag>.tar.ab`
    # rather than a single `<tag>.tar`, and asking for the wrong name 404s -- which
    # looks exactly like "the day is not published" and is not. Ask the API which
    # assets exist, then stream them IN ORDER through one tar.
    assets = list_assets(repo, tag)
    urls = [f"https://github.com/{repo}/releases/download/{tag}/{a}" for a in assets]
    inc = []
    for t in tails: inc += ["--include", f"*trace_full_{HEX[t]}.json"]
    tmp = tempfile.mkdtemp(prefix="ckgh_")
    rc, hits = None, []
    if not urls:
        results.append({"date": date, "tails_asked": tails, "release": tag, "url": None,
                        "assets": [], "curl_exit": None, "hits": [],
                        "verdict": "RELEASE_NOT_PUBLISHED"})
        print(f"  [{i:>2}/{len(dates)}] {date}  {','.join(tails):<15} RELEASE_NOT_PUBLISHED")
        write_out(results, dates)
        continue
    try:
        p1 = subprocess.Popen(["curl", "-sL", "--fail"] + urls, stdout=subprocess.PIPE)
        p2 = subprocess.Popen(["tar", "-xf", "-", "--fast-read"] + inc,
                              stdin=p1.stdout, cwd=tmp,
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        p1.stdout.close()
        p2.wait(); rc = p1.wait()
        for f in glob.glob(os.path.join(tmp, "**", "trace_full_*.json"), recursive=True):
            h = os.path.basename(f)[len("trace_full_"):-len(".json")]
            tail = next((t for t, x in HEX.items() if x == h), h)
            dest = os.path.join(PLANES, tail, "data", "recovered")
            os.makedirs(dest, exist_ok=True)
            name = f"{tail}_{date}_adsblol-github-backup_trace_full.json"
            shutil.copy(f, os.path.join(dest, name))
            with open(os.path.join(dest, name + ".meta.json"), "w") as m:
                json.dump({"retrieved_utc": NOW, "source": "adsblol-github-backup",
                           "source_role": "adsb.lol's own off-site backup, one release per day, ODbL",
                           "url": urls, "release_tag": tag, "http_status": 200,
                           "bytes": os.path.getsize(f), "tail": tail, "hex": h,
                           "utc_date": date,
                           "note": "pulled because BOTH free daily archives returned nothing for this "
                                   "aircraft on this alleged-overlap date"}, m, indent=2)
                m.write("\n")
            hits.append(tail)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    rec = {"date": date, "tails_asked": tails, "release": tag, "url": urls,
           "assets": assets, "curl_exit": rc, "hits": hits,
           "verdict": "RECOVERED_FROM_OFFSITE_BACKUP" if hits
                      else ("RELEASE_NOT_AVAILABLE" if rc not in (0, None) else "NOT_IN_THE_BACKUP_EITHER")}
    results.append(rec)
    print(f"  [{i:>2}/{len(dates)}] {date}  {','.join(tails):<15} {rec['verdict']}"
          + (f"  <== {','.join(hits)}" if hits else ""))
    write_out(results, dates)   # as we go, so a stopped run still leaves a record

got = sum(1 for r in results if r["hits"])
print(f"\n{got} of {len(dates)} dates produced a trace from the off-site backup.")
print(f"wrote {OUT}")
