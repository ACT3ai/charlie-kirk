#!/usr/bin/env python3
"""Plan AeroAPI history pulls around the Erika-claimed overlap rows.

WHICH ROWS (--scope). Rows of following/overlaps.csv with erika_present = `claimed`, then:
  undecided  adsb_verified_verdict NOT_HEARD or NO_ARCHIVE_COVERAGE   (default; 42 rows on 2026-09-14)
  decided    adsb_verified_verdict AT_CLAIMED_AIRPORT, SAME_METRO_WRONG_FIELD or ELSEWHERE (22 rows)
  dated      every row with a usable date                               (64 rows)
  none       no rows - only the --extra blocks

WHICH TAILS. The row's own foreign_tail, unless --tails overrides it for every row
(e.g. --tails N102DZ,N582MM asks "was a Kirk-side aircraft at this field in this window?").

WHICH WINDOW. The row's overlap window, claimed date -3 days to +3 days
(Overlap_Window_Definition.mdx): start = date - 3, end = date + 4. AeroAPI's `start` is
inclusive and `end` exclusive, so that is exactly the 7-day maximum one call allows.

FEWER CALLS, NO REPEATS. Per tail, the union of every row's days, MINUS every day already
covered by a history file on disk for that tail, is packed into consecutive 7-day blocks -
one call each. A day is never bought twice.

This script bills nothing and calls nothing. It writes a plan; aeroapi_erika_windows.js runs it.

  python3 plan_erika_windows.py                                    the 42 undecided rows
  python3 plan_erika_windows.py --scope decided --out _erika_plan_decided.json
  python3 plan_erika_windows.py --scope dated --tails N102DZ,N582MM --out _erika_plan_kirk.json
  python3 plan_erika_windows.py --scope none --extra N560TW:2025-09-09:2025-09-12 --out _sept10_plan.json
  add --check to print the plan and write nothing
"""
import csv, datetime as dt, glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from private_store import private_vendor_dir  # noqa: E402

OVERLAPS = os.path.normpath(os.path.join(HERE, "..", "..", "..", "overlaps.csv"))
# Plans and raw pulls live in the private `all` repo - see private_store.py.
DATA = private_vendor_dir("flightaware")
PRICE_HISTORY = 0.020
SCOPES = {
    "undecided": {"NOT_HEARD", "NO_ARCHIVE_COVERAGE"},
    "decided": {"AT_CLAIMED_AIRPORT", "SAME_METRO_WRONG_FIELD", "ELSEWHERE"},
    "dated": None,
    "none": set(),
}


def arg(name, default=None):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default


def tails_of(cell):
    return [t.strip().upper() for t in re.split(r"[;,]| or ", cell or "")
            if t.strip() and t.strip().upper() != "UNKNOWN"]


def covered_days(tail):
    """Every UTC day already inside a history pull on disk for this tail."""
    days = set()
    for f in glob.glob(os.path.join(DATA, tail, "*_to_*_history_p0.json")):
        m = re.match(r"(\d{4}-\d{2}-\d{2})_to_(\d{4}-\d{2}-\d{2})_history_p0\.json$", os.path.basename(f))
        if m:
            s, e = dt.date.fromisoformat(m.group(1)), dt.date.fromisoformat(m.group(2))
            days.update(s + dt.timedelta(days=k) for k in range((e - s).days))
    return days


def main():
    scope = arg("--scope", "undecided")
    if scope not in SCOPES:
        sys.exit(f"--scope must be one of {', '.join(SCOPES)}")
    override = [t.strip().upper() for t in arg("--tails", "").split(",") if t.strip()]
    out_name = arg("--out", "_erika_plan.json")
    extras = [sys.argv[i + 1] for i, a in enumerate(sys.argv) if a == "--extra"]

    rows = list(csv.DictReader(open(OVERLAPS, newline="", encoding="utf-8")))
    picked, skipped = [], []
    for r in rows if scope != "none" else []:
        if r["erika_present"] != "claimed":
            continue
        if SCOPES[scope] is not None and r["adsb_verified_verdict"] not in SCOPES[scope]:
            continue
        try:
            day = dt.date.fromisoformat((r["date"] or "").strip())
        except ValueError:
            skipped.append((r["overlap_id"], "no usable date")); continue
        tails = override or tails_of(r["foreign_tail"])
        if not tails:
            skipped.append((r["overlap_id"], "no tail")); continue
        picked.append(dict(overlap_id=r["overlap_id"], date=day.isoformat(),
                           airport_code=(r["airport_code"] or "").strip().upper(),
                           city=r["city"], state=r["state"], tails=tails,
                           adsb_verified_verdict=r["adsb_verified_verdict"],
                           window_start=(day - dt.timedelta(days=3)).isoformat(),
                           window_end=(day + dt.timedelta(days=4)).isoformat()))

    need = {}
    for p in picked:
        d0 = dt.date.fromisoformat(p["window_start"])
        for t in p["tails"]:
            need.setdefault(t, set()).update(d0 + dt.timedelta(days=k) for k in range(7))
    for spec in extras:
        t, s, e = spec.split(":")
        s, e = dt.date.fromisoformat(s), dt.date.fromisoformat(e)
        need.setdefault(t.upper(), set()).update(s + dt.timedelta(days=k) for k in range((e - s).days))

    blocks, already = [], 0
    for tail in sorted(need):
        have = covered_days(tail)
        already += len(need[tail] & have)
        ds, i = sorted(need[tail] - have), 0
        while i < len(ds):
            s = ds[i]; e = s + dt.timedelta(days=7)
            blocks.append(dict(tail=tail, start=s.isoformat(), end=e.isoformat()))
            while i < len(ds) and ds[i] < e:
                i += 1

    plan = dict(built_utc=dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                source=os.path.relpath(OVERLAPS, HERE), scope=scope, tails_override=override or None,
                extras=extras, rows=picked, skipped=skipped, blocks=blocks,
                days_already_on_disk=already, est_cost_usd=round(len(blocks) * PRICE_HISTORY, 3))
    print(f"scope={scope} tails={override or 'row foreign_tail'}: {len(picked)} rows, {len(skipped)} skipped, "
          f"{already} tail-days already on disk, {len(blocks)} calls, est ${plan['est_cost_usd']:.2f} at one page each")
    for t in sorted({b['tail'] for b in blocks}):
        print(f"  {t}: {sum(1 for b in blocks if b['tail'] == t)} calls")
    if "--check" in sys.argv:
        return
    os.makedirs(DATA, exist_ok=True)
    open(os.path.join(DATA, out_name), "w").write(json.dumps(plan, indent=1) + "\n")
    print("wrote", os.path.join(DATA, out_name))


if __name__ == "__main__":
    main()
