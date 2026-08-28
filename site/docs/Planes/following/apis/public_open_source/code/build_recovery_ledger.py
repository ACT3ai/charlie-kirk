#!/usr/bin/env python3
"""THE RECOVERY LEDGER -- for every (tail, UTC day) this investigation ASKED
about, what each archive answered.

Three states, and merging any two of them is how an investigation destroys its
own credibility:

  HELD        the archive returned a trace. Presence, at a time, to a position.
  ASKED_NONE  the archive was queried and had nothing. A COVERAGE FACT. It is
              NOT evidence the aircraft was elsewhere -- transponder off, out of
              receiver range, and a wrong claimed date all look identical here.
  NOT_ASKED   nobody has queried it. An open question, not a finding.

The column that matters is `verdict`:

  BOTH_HAVE_IT              two independent archives agree the day exists.
  ONLY_ON_AIRPLANES_LIVE    adsb.lol had nothing, the other network did.
  ONLY_ON_ADSB_LOL          the reverse.
  NEITHER_HAS_IT            both were asked, neither holds it.

ONLY_ON_AIRPLANES_LIVE IS NOT A DELETION. `adsb_lol_403_band` marks the dates
adsb.lol refuses for EVERY aircraft including the two control airliners -- a
retention/serving boundary. Rows inside that band can never be published as
suppression. Rows OUTSIDE it are the ones worth arguing about, and even those
carry a background rate the controls make visible.
"""
import collections, csv, glob, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PLANES = os.path.normpath(os.path.join(HERE, "..", "..", "..", ".."))
OUT = os.path.normpath(os.path.join(HERE, "..", "data", "analysis"))
os.makedirs(OUT, exist_ok=True)

# adsb.lol serves HTTP 403 for every date from here on, for the case aircraft
# AND for both control airliners. Verified 2026-08-24. Archive fact.
BAND_START = "2025-10-12"


def main():
    rows = collections.defaultdict(lambda: {"held": {}, "none": set()})
    for f in glob.glob(os.path.join(PLANES, "*", "data", "recovered", "*.meta.json")):
        try: m = json.load(open(f))
        except Exception: continue
        base = os.path.basename(f)
        tail = (m.get("tail") or base.split("_")[0]).upper()
        date = m.get("utc_date") or m.get("date_utc")
        src = m.get("source") or m.get("source_key")
        if not date or not src: continue
        payload = f[: -len(".meta.json")]
        k = (tail, date)
        if os.path.exists(payload):
            s = m.get("summary") or {}
            rows[k]["held"][src] = dict(
                bytes=m.get("bytes"), points=s.get("points"),
                first=s.get("first_seen_utc"), last=s.get("last_seen_utc"),
                url=m.get("url"), file=os.path.relpath(payload, PLANES),
                retrieved=m.get("retrieved_utc"))
        else:
            rows[k]["none"].add(src)

    out = []
    for (tail, date), v in sorted(rows.items()):
        held, none = v["held"], v["none"]
        h = set(held)
        if "adsb-lol" in h and "airplanes-live" in h: verdict = "BOTH_HAVE_IT"
        elif "airplanes-live" in h and "adsb-lol" in none: verdict = "ONLY_ON_AIRPLANES_LIVE"
        elif "adsb-lol" in h and "airplanes-live" in none: verdict = "ONLY_ON_ADSB_LOL"
        elif not h: verdict = "NEITHER_HAS_IT"
        else: verdict = "HELD_BY_" + "+".join(sorted(h)).upper()
        best = max(held.values(), key=lambda x: x.get("points") or 0, default={})
        out.append(dict(
            tail=tail, date=date, verdict=verdict,
            archives_held="|".join(sorted(h)), archives_asked_none="|".join(sorted(none)),
            adsb_lol_403_band="yes" if date >= BAND_START else "no",
            is_control="yes" if tail.startswith("CONTROL-") else "no",
            trace_points=best.get("points", ""), first_seen_utc=best.get("first", ""),
            last_seen_utc=best.get("last", ""), bytes=best.get("bytes", ""),
            stored_file=best.get("file", ""), source_url=best.get("url", ""),
            retrieved_utc=best.get("retrieved", "")))

    path = os.path.join(OUT, "recovery_ledger.csv")
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)

    c = collections.Counter(r["verdict"] for r in out)
    band = collections.Counter((r["verdict"], r["adsb_lol_403_band"], r["is_control"]) for r in out)
    summary = dict(rows=len(out), verdicts=dict(c),
                   only_airplanes_live_in_band=band[("ONLY_ON_AIRPLANES_LIVE", "yes", "no")],
                   only_airplanes_live_outside_band=band[("ONLY_ON_AIRPLANES_LIVE", "no", "no")],
                   control_only_airplanes_live_outside_band=band[("ONLY_ON_AIRPLANES_LIVE", "no", "yes")])
    json.dump(summary, open(os.path.join(OUT, "recovery_ledger_summary.json"), "w"), indent=1)
    print(json.dumps(summary, indent=1), file=sys.stderr)
    print("wrote " + path, file=sys.stderr)


if __name__ == "__main__":
    main()
