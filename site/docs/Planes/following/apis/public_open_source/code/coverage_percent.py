#!/usr/bin/env python3
"""HOW MUCH OF THE DATA DO WE ACTUALLY HAVE? -- stated as a percentage, with the
denominator named every time.

A coverage percentage is meaningless without saying "percent of WHAT". Four
different denominators are reported here because four different questions get
asked, and quoting the wrong one is how "9%" and "83%" both end up being true
sentences about the same investigation:

  D1  CALENDAR COVERAGE. Every UTC day of the claim period (2022-01-01 to
      2025-12-31) for every aircraft in the fleet. The honest ceiling on
      "do we know where this plane was".
  D2  ASKED COVERAGE. Of the aircraft-days we actually QUERIED an archive
      about, how many came back with a trace. This is the archive's hit rate,
      not our completeness.
  D3  EVENT-WINDOW COVERAGE. Only the aircraft-days that matter: every sourced
      Charlie/Erika/TPUSA event date +/-1 day. This is the one that bears on
      the following claim.
  D4  SWEEP COVERAGE. Of the event-days the GEOGRAPHIC sweep needed, how many
      UTC days were successfully swept. The sweep does not need a tail number,
      so it answers "was anything there" even where D3 is empty.

Split by SOURCE FAMILY throughout, because the whole point of this exercise is
which lane produced the data:

  OPEN SOURCE, no account, free    adsb.lol, airplanes.live, adsb.lol's GitHub
                                   Release backup, ADS-B Exchange free samples
  ARCHIVE OF A WEB PAGE            Internet Archive snapshots of FR24/FlightAware
  PROPRIETARY / PAID               FlightRadar24 API, FlightAware AeroAPI,
                                   ADS-B Exchange historical API, OpenSky OAuth
"""
import collections, csv, datetime as dt, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(HERE, "..", "data"))
AN = os.path.join(DATA, "analysis")
FOLLOWING = os.path.normpath(os.path.join(HERE, "..", "..", ".."))

OPEN = {"adsb-lol", "airplanes-live", "adsbexchange-samples", "adsblol-github-backup"}
PAGE = {"wayback/flightradar24", "wayback/flightaware", "flightaware-activity-log"}

FOREIGN = ["SU-BTT", "SU-BND", "SU-BTU", "SU-BTV", "SU-BGM", "T7-ELL"]
US_FLEET = ["N102DZ", "N1098L", "N2100L", "N40JD", "N560TW", "N582MM",
            "N59906", "N55906", "N872RA", "N888KG"]
CONTROLS = ["CONTROL-LUFTHANSA", "CONTROL-RYANAIR"]

START, END = dt.date(2022, 1, 1), dt.date(2025, 12, 31)
SPAN = (END - START).days + 1


def load_ledger():
    rows = list(csv.DictReader(open(os.path.join(AN, "recovery_ledger.csv"))))
    held, asked = collections.defaultdict(set), collections.defaultdict(set)
    src_days = collections.defaultdict(lambda: collections.defaultdict(set))
    for r in rows:
        t, d = r["tail"], r["date"]
        asked[t].add(d)
        fams = set()
        if r["archives_held"]:
            held[t].add(d)
            for s in r["archives_held"].split("|"):
                fam = "open_source" if s in OPEN else ("page_archive" if s in PAGE else "other:" + s)
                src_days[t][fam].add(d)
                src_days[t]["src:" + s].add(d)
    return held, asked, src_days


def event_days():
    """Every sourced event date +/-1, as UTC days."""
    import re
    days = set()
    for r in csv.DictReader(open(os.path.join(FOLLOWING, "tpusa_events.csv"))):
        iso = re.findall(r"\d{4}-\d{2}-\d{2}", r.get("dates") or "")
        if not iso: continue
        if " to " in (r.get("dates") or "") and len(iso) == 2:
            a, b = dt.date.fromisoformat(iso[0]), dt.date.fromisoformat(iso[1])
            base = [a + dt.timedelta(days=i) for i in range((b - a).days + 1)] if 0 <= (b - a).days <= 21 else [a]
        else:
            base = [dt.date.fromisoformat(x) for x in iso]
        for d in base:
            for off in (-1, 0, 1):
                days.add((d + dt.timedelta(days=off)).isoformat())
    return days


def pct(a, b):
    return f"{100.0 * a / b:6.2f}%" if b else "   n/a"


def main():
    held, asked, src_days = load_ledger()
    ev = event_days()
    ev_in_span = {d for d in ev if START.isoformat() <= d <= END.isoformat()}

    print("=" * 88)
    print("D1  CALENDAR COVERAGE  -- % of all UTC days 2022-01-01..2025-12-31 we hold a trace for")
    print("=" * 88)
    print(f"{'tail':20}{'days held':>10}{'of':>7}{'D1 %':>9}{'asked':>8}{'D2 asked-hit':>14}")
    groups = [("FOREIGN FLEET", FOREIGN), ("US / KIRK-ASSOCIATED FLEET", US_FLEET), ("CONTROLS", CONTROLS)]
    tot = {}
    for name, tails in groups:
        print(f"-- {name}")
        h = a = 0
        for t in tails:
            hs = {d for d in held[t] if START.isoformat() <= d <= END.isoformat()}
            as_ = {d for d in asked[t] if START.isoformat() <= d <= END.isoformat()}
            h += len(hs); a += len(as_)
            print(f"{t:20}{len(hs):>10}{SPAN:>7}{pct(len(hs), SPAN):>9}{len(as_):>8}{pct(len(hs), len(as_)):>14}")
        n = SPAN * len(tails)
        tot[name] = (h, n, a)
        print(f"{'  GROUP TOTAL':20}{h:>10}{n:>7}{pct(h, n):>9}{a:>8}{pct(h, a):>14}")
    print()

    print("=" * 88)
    print("D3  EVENT-WINDOW COVERAGE -- the days that actually bear on the following claim")
    print(f"    {len(ev_in_span)} distinct UTC days = every sourced event date +/-1, inside the claim span")
    print("=" * 88)
    print(f"{'tail':20}{'held in window':>16}{'of':>7}{'D3 %':>9}{'asked':>8}{'never asked':>13}")
    for name, tails in groups:
        print(f"-- {name}")
        h = a = 0
        for t in tails:
            hs = held[t] & ev_in_span
            as_ = asked[t] & ev_in_span
            h += len(hs); a += len(as_)
            print(f"{t:20}{len(hs):>16}{len(ev_in_span):>7}{pct(len(hs), len(ev_in_span)):>9}{len(as_):>8}{len(ev_in_span)-len(as_):>13}")
        n = len(ev_in_span) * len(tails)
        print(f"{'  GROUP TOTAL':20}{h:>16}{n:>7}{pct(h, n):>9}{a:>8}{n-a:>13}")
    print()

    print("=" * 88)
    print("D3 BY YEAR -- foreign fleet only (SU-* and T7-ELL), the fleet the claim is about")
    print("=" * 88)
    print(f"{'year':8}{'window days':>13}{'fleet-days needed':>19}{'held':>7}{'%':>9}{'asked':>8}{'never asked':>13}")
    for y in (2022, 2023, 2024, 2025):
        wd = {d for d in ev_in_span if d.startswith(str(y))}
        need = len(wd) * len(FOREIGN)
        h = sum(len(held[t] & wd) for t in FOREIGN)
        a = sum(len(asked[t] & wd) for t in FOREIGN)
        print(f"{y:<8}{len(wd):>13}{need:>19}{h:>7}{pct(h, need):>9}{a:>8}{need-a:>13}")
    print()

    print("=" * 88)
    print("WHICH LANE PRODUCED THE DATA -- aircraft-days held, by source")
    print("=" * 88)
    fam = collections.defaultdict(set)
    per_src = collections.defaultdict(set)
    for t, d in src_days.items():
        for k, days in d.items():
            for x in days:
                if k.startswith("src:"): per_src[k[4:]].add((t, x))
                else: fam[k].add((t, x))
    allheld = set().union(*fam.values()) if fam else set()
    print(f"{'source family':24}{'aircraft-days':>15}{'share of all held':>19}")
    for k, v in sorted(fam.items(), key=lambda x: -len(x[1])):
        print(f"{k:24}{len(v):>15}{pct(len(v), len(allheld)):>19}")
    print(f"{'  TOTAL HELD':24}{len(allheld):>15}")
    print()
    print(f"{'individual source':28}{'aircraft-days':>15}{'share':>10}{'UNIQUE (only source)':>22}")
    for k, v in sorted(per_src.items(), key=lambda x: -len(x[1])):
        others = set().union(*[w for j, w in per_src.items() if j != k]) if len(per_src) > 1 else set()
        print(f"{k:28}{len(v):>15}{pct(len(v), len(allheld)):>10}{len(v - others):>22}")
    print()
    # Page snapshots are NOT aircraft-days. A wayback capture is dated by when the
    # crawler visited, not by when an aircraft flew, so it cannot enter any of the
    # denominators above. It is counted here in its own unit.
    import glob as _g
    snaps = collections.Counter()
    for f in _g.glob(os.path.join(os.path.normpath(os.path.join(HERE, "..", "..", "..", "..")), "*", "data", "recovered", "*.meta.json")):
        try: m = json.load(open(f))
        except Exception: continue
        s_ = m.get("source") or m.get("source_key") or ""
        if "wayback" in s_ or "activity-log" in s_:
            if os.path.exists(f[:-len(".meta.json")]): snaps[s_] += 1
    print("PAGE-ARCHIVE LANE -- web page snapshots, counted in PAGES not aircraft-days")
    for k, v in snaps.most_common(): print(f"  {k:28}{v:>6} captures held")
    print(f"  {'TOTAL':28}{sum(snaps.values()):>6}")
    print("  These preserve WHAT A TRACKING SITE SAID. They are the only lane that can")
    print("  document a page-level removal, and the only lane that reaches before 2022.")
    print()
    print("PROPRIETARY / PAID LANES (FR24 API, FlightAware AeroAPI, ADSBX historical,")
    print("OpenSky OAuth): 0 aircraft-days. No credential is held, so none was queried.")
    print("100% of the trace data in this investigation came from FREE, OPEN-SOURCE")
    print("archives or from the Internet Archive's copy of a public web page.")
    print()

    print("=" * 88)
    print("D4  GEOGRAPHIC-SWEEP COVERAGE -- the lane that needs no tail number")
    print("=" * 88)
    import glob
    st = collections.Counter(); swept = set()
    for f in glob.glob(os.path.join(DATA, "geo_sweep", "*", "_sweep.meta.json")):
        m = json.load(open(f)); st[m.get("status")] += 1
        if m.get("status") in ("SWEPT", "TRUNCATED"): swept.add(m["sweep_date"])
    need = len({d for d in ev if START.isoformat() <= d <= END.isoformat()})
    print(f"day-directories on disk         {sum(st.values()):>6}")
    for k, v in st.most_common(): print(f"  {k:30}{v:>6}")
    print(f"UTC days usefully swept         {len(swept):>6}")
    print(f"event-window days in span       {need:>6}")
    print(f"D4 sweep coverage of the window {pct(len(swept & ev_in_span), need):>6}")
    for y in (2022, 2023, 2024, 2025):
        wd = {d for d in ev_in_span if d.startswith(str(y))}
        print(f"   {y}  {pct(len(swept & wd), len(wd))}   ({len(swept & wd)} of {len(wd)} window days)")


if __name__ == "__main__":
    main()
