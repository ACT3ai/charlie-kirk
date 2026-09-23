#!/usr/bin/env python3
"""The Kirk-side jets' whole recovered record: every stop, what it lined up with, and what
was parked beside it.

Built for three questions Bryan Starbuck set on the 16 September 2026 call:

  1. HIS PLANE AND HER PLANE. On days Charlie Kirk and Erika Kirk were publicly in different
     cities, which aircraft was at each city? Repeated across dates, that is how a tail gets
     tied to a person without a manifest.
  2. TRIPS WITHOUT THEM. Which stops line up with a sourced public event (a Kirk was
     probably aboard), and which do not - especially short stops in the middle of the night
     at small fields.
  3. THE CLAIMED ADELSON "MEET-UPS". Posts on X (Ana Escobar, Stew Peters, July-August 2026)
     say a TPUSA plane repeatedly sat beside Miriam Adelson's aircraft (N804MS, N108MS and
     other Las Vegas Sands jets) before those flew on to Israel. This lists every time a
     Kirk-side jet and an Adelson jet were heard on the ground at the same field, and where
     the Adelson jet went next.

    python3 analyse_kirk_side_record.py [--erika-events PATH]

WHAT A STOP IS. A run of on-ground positions from free volunteer ADS-B receivers, resolved
to the nearest field within 8 km (lib/traces.py). "First heard" and "last heard" are when
receivers heard it on the ground - NOT a landing or take-off time. Receivers often lose an
aircraft on the ramp, so a heard duration is a floor, never the real time on the ground.

WHAT NONE OF THIS SHOWS. Who was aboard, what was carried, or why. Two jets heard at the
same field at the same time were at the same airport; the record cannot say they met.

WRITES data/analysis/kirk_side/:
  stops.csv                 every stop by every Kirk-side and Adelson jet
  kirk_stop_class.csv       each Kirk-side stop against the sourced events, with the night /
                            short / small-field flags
  kirk_adelson_colocated.csv  every Kirk-side stop that shares a field and time with an
                            Adelson jet, and the Adelson jet's next stops
  different_cities_days.csv days two Kirk-side jets sat at two different event cities
  coverage.csv              per tail: days held / asked-empty / never asked
"""
import collections, csv, datetime as dt, json, os, re, sys
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "lib"))
from traces import trace_files, open_trace, build_miss_index, GROUND_MAX_KM, VISIT_GAP_SEC, _iso  # noqa: E402
from geo import airport_by_code, haversine_km, haversine_mi, nearest_airport, timezone_at  # noqa: E402
import build_master_proximity as bmp  # noqa: E402

OUT = os.path.normpath(os.path.join(HERE, "..", "data", "analysis", "kirk_side"))
KIRK = ["N102DZ", "N582MM", "N79SC", "N560TW", "N40JD", "N872RA", "N888KG"]
ADELSON = ["N804MS", "N108MS", "N885LS", "N889LS", "N336LS", "N337LS", "N338LS", "N339LS"]
# Listed in stops.csv only (privacy-period record), not classified against Kirk events.
OTHER = ["T7-ELL"]
MERGE_GAP_MIN = 180          # two ground runs at one field this close are one stop
EVENT_RADIUS_MI = 50
NIGHT = (22, 5)              # local hour window, [22:00, 05:00)
SHORT_MIN = 90
COLOCATE_GAP_MIN = 180       # "same field, near in time" tier


def ts(s):
    return dt.datetime.fromisoformat(s.replace("Z", "+00:00"))


def local(when, ap):
    st = (ap.get("iso_region") or "")[3:] if ap else ""
    tz, method = (timezone_at(ap["lat"], ap["lon"], st) if ap else (None, "unresolved"))
    if not tz:
        return None, None, method
    return when.astimezone(ZoneInfo(tz)), tz, method


# A rebuildable cache, kept OUT of the repo on purpose.
CACHE = os.environ.get("CK_GROUND_CACHE", "/tmp/ck_kirk_side_ground_runs_cache.json")


def ground_visits(path, day):
    """The on-ground half of traces.visits_from_trace, same rules (8 km, 45-min split),
    without the per-point low-pass search this analysis does not use."""
    try:
        with open_trace(path) as fh:
            pts = json.load(fh).get("trace") or []
    except (OSError, ValueError, EOFError):
        return None
    ground = [(p[0], p[1], p[2]) for p in pts if len(p) >= 4 and p[1] is not None and p[3] == "ground"]
    runs, run = [], []
    for pt in ground:
        if run and pt[0] - run[-1][0] > VISIT_GAP_SEC:
            runs.append(run)
            run = []
        run.append(pt)
    if run:
        runs.append(run)
    out = []
    for run in runs:
        mid = run[len(run) // 2]
        ap = nearest_airport(mid[1], mid[2], radius_mi=GROUND_MAX_KM * 0.621371 + 1)
        out.append(dict(airport_code=ap["ident"] if ap else None,
                        median_distance_km=round(haversine_km(mid[1], mid[2], ap["lat"], ap["lon"]), 2) if ap else None,
                        first_seen_utc=_iso(day, run[0][0]), last_seen_utc=_iso(day, run[-1][0]),
                        ground_points=len(run)))
    return out


def load_stops(tails):
    cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
    runs = collections.defaultdict(list)
    for tail, day, source, path in trace_files(set(tails)):
        key = f"{os.path.basename(path)}:{os.path.getsize(path)}"
        if key not in cache:
            cache[key] = ground_visits(path, day)
        for v in cache[key] or []:
            if not v["airport_code"]:
                continue
            runs[tail].append(dict(code=v["airport_code"], first=ts(v["first_seen_utc"]),
                                   last=ts(v["last_seen_utc"]), km=v["median_distance_km"],
                                   src={source}, pts=v["ground_points"]))
    json.dump(cache, open(CACHE, "w"))
    stops = []
    for tail, rs in runs.items():
        rs.sort(key=lambda r: r["first"])
        cur = None
        for r in rs:
            if cur and r["code"] == cur["code"] and (r["first"] - cur["last"]).total_seconds() <= MERGE_GAP_MIN * 60:
                cur["last"] = max(cur["last"], r["last"])
                cur["src"] |= r["src"]
                cur["pts"] += r["pts"]
                continue
            if cur:
                stops.append(cur)
            cur = dict(r, tail=tail)
        if cur:
            stops.append(cur)
    stops.sort(key=lambda s: (s["tail"], s["first"]))
    return stops


def load_erika_events(path):
    """Erika-only appearance rows: date_from,date_to,date_certainty,city,state,..."""
    if not path or not os.path.exists(path):
        return []
    gaz = bmp.load_gazetteer()
    out = []
    for r in csv.DictReader(open(path, encoding="utf-8")):
        if r.get("date_certainty") != "EVENT_DATE" or (r.get("country") or "USA") not in ("USA", "US", "United States"):
            continue
        city, st = (r.get("city") or "").strip(), (r.get("state") or "").strip()
        ll = gaz.get((city.lower(), st)) or bmp.MANUAL.get((city, st))
        if not ll:
            continue
        a = dt.date.fromisoformat(r["date_from"])
        b = dt.date.fromisoformat(r.get("date_to") or r["date_from"])
        for i in range((b - a).days + 1):
            out.append(dict(date=(a + dt.timedelta(i)).isoformat(), city=city, state=st, lat=ll[0], lon=ll[1],
                            who="Erika", title=r.get("event_title", ""), charlie=r.get("charlie_present", ""),
                            erika="yes", source=r.get("source_url", "")))
    return out


def main():
    a = sys.argv[1:]
    erika_path = a[a.index("--erika-events") + 1] if "--erika-events" in a else os.path.join(
        HERE, "..", "..", "..", "erika_events.csv")
    os.makedirs(OUT, exist_ok=True)
    stops = load_stops(KIRK + ADELSON + OTHER)
    gaz = bmp.load_gazetteer()
    events = bmp.load_events(gaz)
    for e in events:
        e["source"] = e.get("page", "")
    erika = load_erika_events(erika_path)
    by_date = collections.defaultdict(list)
    for e in events + erika:
        by_date[e["date"]].append(e)

    # ---- stops.csv --------------------------------------------------------------------
    rows = []
    for s in stops:
        ap = airport_by_code(s["code"])
        lf, tz, method = local(s["first"], ap)
        ll, _, _ = local(s["last"], ap)
        s.update(ap=ap, lfirst=lf, llast=ll, tz=tz, tz_method=method,
                 minutes=round((s["last"] - s["first"]).total_seconds() / 60))
        rows.append(dict(tail=s["tail"], side="adelson" if s["tail"] in ADELSON else ("other" if s["tail"] in OTHER else "kirk"),
                         airport=s["code"], airport_name=ap["name"] if ap else "",
                         municipality=(ap or {}).get("municipality") or "", region=(ap or {}).get("iso_region") or "",
                         country=(ap or {}).get("iso_country") or "", field_type=(ap or {}).get("type") or "",
                         first_heard_utc=s["first"].isoformat(), last_heard_utc=s["last"].isoformat(),
                         first_heard_local=lf.strftime("%Y-%m-%d %H:%M") if lf else "",
                         last_heard_local=ll.strftime("%Y-%m-%d %H:%M") if ll else "",
                         timezone=tz or "", timezone_method=method, heard_minutes=s["minutes"],
                         ground_points=s["pts"], sources=";".join(sorted(s["src"]))))
    write(os.path.join(OUT, "stops.csv"), rows)

    # ---- kirk_stop_class.csv ----------------------------------------------------------
    cls = []
    # HOME FIELDS: a jet arriving home late at night is a return, not the claimed pattern.
    # A field is a home field for a tail if it holds at least 15% of that tail's stops.
    per_tail = collections.defaultdict(collections.Counter)
    seq_by_tail = collections.defaultdict(list)
    for s in stops:
        per_tail[s["tail"]][s["code"]] += 1
        seq_by_tail[s["tail"]].append(s)
    home = {t: {c for c, n in cnt.items() if n >= 0.15 * sum(cnt.values())} for t, cnt in per_tail.items()}
    for s in stops:
        if s["tail"] not in KIRK or not s["ap"]:
            continue
        seq = seq_by_tail[s["tail"]]
        i = seq.index(s)
        nxt = seq[i + 1] if i + 1 < len(seq) else None
        # QUICK TURN: next heard at a DIFFERENT field within 4 h of arriving here. Heard ground
        # time alone cannot show this - receivers lose parked aircraft - so the next stop does.
        turn_h = round((nxt["first"] - s["first"]).total_seconds() / 3600, 1) if nxt and nxt["code"] != s["code"] else None
        quick = turn_h is not None and turn_h <= 4
        lf = s["lfirst"]
        day = (lf or s["first"]).date()
        near = []
        for off in (-1, 0, 1):
            for e in by_date.get((day + dt.timedelta(off)).isoformat(), []):
                d = haversine_mi(s["ap"]["lat"], s["ap"]["lon"], e["lat"], e["lon"])
                if d <= EVENT_RADIUS_MI:
                    near.append((abs(off), d, off, e))
        near.sort(key=lambda x: (x[0], x[1]))
        night = bool(lf) and (lf.hour >= NIGHT[0] or lf.hour < NIGHT[1])
        short = s["minutes"] <= SHORT_MIN
        small = s["ap"]["type"] == "small_airport"
        at_home = s["code"] in home.get(s["tail"], set())
        if near:
            e = near[0][3]
            label = f"EVENT_{e['who'].upper()}" + ("_SAME_DAY" if near[0][2] == 0 else "_ADJACENT_DAY")
        elif at_home:
            label = "HOME_FIELD"
        elif night and quick:
            label = "NO_EVENT_NIGHT_QUICK_TURN"
        elif quick:
            label = "NO_EVENT_DAY_QUICK_TURN"
        else:
            label = "NO_EVENT"
        cls.append(dict(tail=s["tail"], airport=s["code"], airport_name=s["ap"]["name"],
                        municipality=s["ap"].get("municipality") or "", region=s["ap"].get("iso_region") or "",
                        field_type=s["ap"]["type"], first_heard_local=lf.strftime("%Y-%m-%d %H:%M") if lf else "",
                        heard_minutes=s["minutes"], night_local=night, short=short, small_field=small,
                        home_field=at_home, hours_to_next_stop_elsewhere=turn_h if turn_h is not None else "",
                        next_stop=(f"{nxt['code']} {nxt['lfirst'].strftime('%Y-%m-%d %H:%M')}" if nxt and nxt.get("lfirst") else ""),
                        class_=label,
                        event_who=near[0][3]["who"] if near else "", event_title=near[0][3]["title"] if near else "",
                        event_city=f"{near[0][3]['city']}, {near[0][3]['state']}" if near else "",
                        event_date=near[0][3]["date"] if near else "",
                        event_distance_mi=round(near[0][1], 1) if near else "",
                        event_source=near[0][3].get("source", "") if near else "",
                        timezone_method=s["tz_method"]))
    write(os.path.join(OUT, "kirk_stop_class.csv"), cls)

    # ---- kirk_adelson_colocated.csv ---------------------------------------------------
    ad_by_code = collections.defaultdict(list)
    ad_by_tail = collections.defaultdict(list)
    for s in stops:
        if s["tail"] in ADELSON:
            ad_by_code[s["code"]].append(s)
            ad_by_tail[s["tail"]].append(s)
    col = []
    for k in stops:
        if k["tail"] not in KIRK:
            continue
        for d in ad_by_code.get(k["code"], []):
            overlap = (min(k["last"], d["last"]) - max(k["first"], d["first"])).total_seconds() / 60
            gap = -overlap if overlap < 0 else 0
            if overlap < 0 and gap > COLOCATE_GAP_MIN:
                continue
            seq = ad_by_tail[d["tail"]]
            i = seq.index(d)
            nxt = [f"{x['code']} ({(x['ap'] or {}).get('iso_country','')}) {x['first'].strftime('%Y-%m-%d %H:%MZ')}"
                   for x in seq[i + 1:i + 4]]
            abroad = next((x for x in seq[i + 1:i + 4] if x["ap"] and x["ap"].get("iso_country") != "US"), None)
            prev_k = [x for x in stops if x["tail"] == k["tail"] and x["last"] < k["first"]][-1:]
            col.append(dict(kirk_tail=k["tail"], adelson_tail=d["tail"], airport=k["code"],
                            airport_name=(k["ap"] or {}).get("name", ""), field_type=(k["ap"] or {}).get("type", ""),
                            municipality=(k["ap"] or {}).get("municipality") or "", region=(k["ap"] or {}).get("iso_region") or "",
                            kirk_first_local=k["lfirst"].strftime("%Y-%m-%d %H:%M") if k["lfirst"] else "",
                            kirk_last_local=k["llast"].strftime("%Y-%m-%d %H:%M") if k["llast"] else "",
                            adelson_first_local=d["lfirst"].strftime("%Y-%m-%d %H:%M") if d["lfirst"] else "",
                            adelson_last_local=d["llast"].strftime("%Y-%m-%d %H:%M") if d["llast"] else "",
                            tier="HEARD_TOGETHER" if overlap >= 0 else "SAME_FIELD_WITHIN_3H",
                            minutes_heard_together=round(overlap) if overlap >= 0 else 0,
                            minutes_apart=round(gap),
                            kirk_previous_stop=(f"{prev_k[0]['code']} {prev_k[0]['lfirst'].strftime('%Y-%m-%d %H:%M') if prev_k[0]['lfirst'] else ''} "
                                                f"({prev_k[0]['minutes']} min heard)") if prev_k else "",
                            adelson_next_stops=" | ".join(nxt),
                            adelson_next_abroad=(f"{abroad['code']} {abroad['ap'].get('iso_country')}" if abroad else ""),
                            timezone_method=k["tz_method"]))
    col.sort(key=lambda r: r["kirk_first_local"])
    write(os.path.join(OUT, "kirk_adelson_colocated.csv"), col)


    # ---- adelson_to_israel_departures.csv -----------------------------------------------
    # The claim as stated on air (Stew Peters, The Jimmy Dore Show, 1 Aug 2026): the Adelson
    # jet sits 2-4 h beside a Kirk-side jet, "then immediately ... goes straight to Tel Aviv".
    # So start from every Tel Aviv arrival, take the last field heard before it, and ask
    # whether any Kirk-side jet was heard there in the 6 hours before that jet left.
    isr = []
    for t in ADELSON:
        seq = ad_by_tail[t]
        for i, s in enumerate(seq):
            if s["code"] != "LLBG" or i == 0:
                continue
            dep = seq[i - 1]
            us = bool(dep["ap"]) and dep["ap"].get("iso_country") == "US"
            near = []
            if us:
                lo = dep["first"] - dt.timedelta(hours=6)
                near = [k for k in stops if k["tail"] in KIRK and k["code"] == dep["code"]
                        and k["last"] >= lo and k["first"] <= dep["last"]]
            isr.append(dict(adelson_tail=t, tel_aviv_first_heard_utc=s["first"].isoformat(),
                            previous_field=dep["code"], previous_country=(dep["ap"] or {}).get("iso_country", ""),
                            previous_last_heard_utc=dep["last"].isoformat(),
                            hours_previous_to_tel_aviv=round((s["first"] - dep["last"]).total_seconds() / 3600, 1),
                            kirk_side_jets_at_previous_field_6h=";".join(
                                f"{k['tail']} {k['first'].isoformat()}" for k in near)))
    write(os.path.join(OUT, "adelson_to_israel_departures.csv"), isr)
    print("tel aviv arrivals:", len(isr), "| previous field in US:", sum(1 for r in isr if r["previous_country"] == "US"),
          "| with a Kirk-side jet there:", sum(1 for r in isr if r["kirk_side_jets_at_previous_field_6h"]))

    # ---- private_period_stops.csv -------------------------------------------------------
    # Every stop recovered after the earliest date each tail is known hidden from the public.
    # The dates come from privacy_flag_timeline.csv and the FlightAware block checks; the basis
    # travels with every row so a reader can see how strong it is.
    private = {
        "N102DZ": ("2025-12-02", "FAA LADD flag appears between 2025-12-01 and 2026-04-01 (ADS-B Exchange DB); FlightAware block visible 2026-01-14 (Wayback)"),
        "N888KG": ("2022-07-02", "FAA LADD flag appears between 2022-07-01 and 2022-12-01 (ADS-B Exchange DB); FlightAware block visible 2025-09-11 (Wayback)"),
        "N582MM": ("2023-02-06", "Never LADD; FlightAware blocked=true (AeroAPI, Sep 2026) with no known start date, so the whole recovered record is listed"),
        "T7-ELL": ("2026-02-02", "LADD flag appears between 2026-02-01 and 2026-05-01 (ADS-B Exchange DB); FlightAware and Flightradar24 hide it (15 Sep 2026)"),
        "N79SC": ("2026-05-02", "LADD flag appears between 2026-05-01 and 2026-06-01 (airplanes.live DB)"),
    }
    prv = []
    for s in stops:
        if s["tail"] in private and s["first"].date().isoformat() >= private[s["tail"]][0]:
            prv.append(dict(tail=s["tail"], private_from=private[s["tail"]][0], private_basis=private[s["tail"]][1],
                            date_utc=s["first"].date().isoformat(), airport=s["code"],
                            airport_name=(s["ap"] or {}).get("name", ""), city=(s["ap"] or {}).get("municipality") or "",
                            region=(s["ap"] or {}).get("iso_region") or "", country=(s["ap"] or {}).get("iso_country") or "",
                            first_heard_utc=s["first"].isoformat(), last_heard_utc=s["last"].isoformat(),
                            first_heard_local=s["lfirst"].strftime("%Y-%m-%d %H:%M") if s["lfirst"] else "",
                            sources=";".join(sorted(s["src"]))))
    write(os.path.join(OUT, "private_period_stops.csv"), prv)

    # ---- different_cities_days.csv ----------------------------------------------------
    at_event = collections.defaultdict(list)
    for c in cls:
        if c["class_"].startswith("EVENT_") and c["class_"].endswith("SAME_DAY"):
            at_event[c["event_date"]].append(c)
    diff = []
    for day, cs in sorted(at_event.items()):
        cities = {c["event_city"] for c in cs}
        if len(cities) < 2:
            continue
        for c in cs:
            diff.append(dict(date=day, tail=c["tail"], airport=c["airport"], event_city=c["event_city"],
                             event_who=c["event_who"], event_title=c["event_title"],
                             first_heard_local=c["first_heard_local"], heard_minutes=c["heard_minutes"]))
    write(os.path.join(OUT, "different_cities_days.csv"), diff)

    # ---- coverage.csv -----------------------------------------------------------------
    held = collections.defaultdict(set)
    for tail, day, source, path in trace_files(set(KIRK + ADELSON)):
        held[tail].add(day)
    miss = build_miss_index()
    d0, d1 = dt.date(2023, 2, 6), dt.date(2026, 9, 16)
    span = {(d0 + dt.timedelta(i)).isoformat() for i in range((d1 - d0).days + 1)}
    cov = []
    for t in KIRK + ADELSON:
        h = held[t] & span
        m = set((miss.get(t) or {}).keys()) & span - h
        cov.append(dict(tail=t, days_in_span=len(span), held=len(h), asked_empty=len(m),
                        never_asked=len(span) - len(h) - len(m),
                        stops=sum(1 for s in stops if s["tail"] == t)))
    write(os.path.join(OUT, "coverage.csv"), cov)

    counts = collections.Counter(c["class_"] for c in cls)
    print("stops:", len(stops), "| kirk-side classes:", dict(counts))
    print("kirk/adelson co-located:", collections.Counter(r["tier"] for r in col))
    print("different-city event days:", len({r['date'] for r in diff}))
    print("erika event-days loaded:", len(erika))


def write(path, rows):
    if not rows:
        open(path, "w").write("")
        return
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


if __name__ == "__main__":
    main()
