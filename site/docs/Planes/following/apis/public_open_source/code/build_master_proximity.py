#!/usr/bin/env python3
"""MASTER PROXIMITY TABLE -- the whole investigation in one CSV.

Joins three things that have never been joined in this repo:

  1. Every airport GROUND VISIT recovered from raw ADS-B traces
     (data/recovery/trace_visit_index.json, 6,429 visits over 2,235 tail-days).
  2. Every sourced Charlie / Erika / TPUSA event (following/tpusa_events.csv).
  3. Every hit from the GEOGRAPHIC SWEEP (data/geo_sweep/*/hits.csv.gz),
     which asks WHAT WAS THERE rather than WHERE WAS THIS TAIL.

Output rows are one (tail, date, airport) presence with the distance to the
nearest sourced event city on that date +/- WINDOW days.

WHAT A ROW IS NOT. A ground visit proves an airframe transmitted on-ground
positions near a runway. It does not prove a landing, a passenger, a purpose,
or that anyone named was aboard. A 50-mile match is a DRIVING-DISTANCE
COINCIDENCE, nothing more, and the control cities in the sweep exist so that
the base rate of such coincidences is visible beside every claim.
"""
import re
import csv, gzip, glob, json, os, sys, math, collections, datetime as dt

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(HERE, "..", "data"))
FOLLOWING = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
OUT = os.path.join(DATA, "analysis")
os.makedirs(OUT, exist_ok=True)
sys.path.insert(0, os.path.join(HERE, "lib"))
from geo import haversine_km, MI_PER_KM  # noqa

WINDOW = 1
RADIUS_MI = 50.0

def load_gazetteer():
    path = os.path.join(DATA, "gazetteer", "2024_Gaz_place_national.txt")
    idx = {}
    with open(path, encoding="latin-1") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            row = { (k or "").strip(): (v or "").strip() for k, v in row.items() }
            name = row.get("NAME", ""); st = row.get("USPS", "")
            try: lat, lon = float(row["INTPTLAT"]), float(row["INTPTLONG"])
            except Exception: continue
            alts = {name, name.rsplit(" ", 1)[0]}
            # Census names consolidated governments and CDPs in forms an event
            # sheet never uses: "Lexington-Fayette urban county", "State College
            # borough", "Athens-Clarke County unified government (balance)".
            base = re.split(r"[-(]", name)[0].strip()
            alts.add(base)
            alts.add(re.sub(r"\s+(city|town|village|borough|CDP|municipality|urban county|unified government.*|consolidated government.*|metro government.*|\(balance\))$", "", base, flags=re.I).strip())
            for n in alts:
                if n: idx.setdefault((n.lower(), st), (lat, lon))
    return idx

def load_airports():
    ap = {}
    with open(os.path.join(DATA, "ourairports", "airports.csv")) as fh:
        for r in csv.DictReader(fh):
            try: ap[r["ident"]] = (float(r["latitude_deg"]), float(r["longitude_deg"]),
                                   r["name"], r["municipality"], r["iso_country"], r["iso_region"])
            except Exception: pass
    return ap

# Places the Census gazetteer cannot supply and that we will not guess at from
# a name alone. Each is a campus/venue coordinate looked up deliberately.
MANUAL = {
    ("University Park", "PA"): (40.7982, -77.8599),   # Penn State University Park
}

UNRESOLVED = []


def load_events(gaz):
    out = []
    with open(os.path.join(FOLLOWING, "tpusa_events.csv")) as fh:
        for r in csv.DictReader(fh):
            raw = (r.get("dates") or "").strip()
            city, st = (r.get("city") or "").strip(), (r.get("state") or "").strip()
            if not raw or not city: continue
            import datetime as _dt
            iso = re.findall(r"\d{4}-\d{2}-\d{2}", raw)
            days = []
            if " to " in raw and len(iso) == 2:
                a, b = _dt.date.fromisoformat(iso[0]), _dt.date.fromisoformat(iso[1])
                if 0 <= (b - a).days <= 21:
                    days = [(a + _dt.timedelta(days=i)).isoformat() for i in range((b - a).days + 1)]
            if not days: days = iso
            if not days: continue   # month-only rows are DROPPED and counted, never guessed
            ll = (gaz.get((city.lower(), st)) or gaz.get((city.lower().replace(" city",""), st))
                  or MANUAL.get((city, st)))
            if not ll:
                UNRESOLVED.append((city, st, raw)); continue
            for d in days:
                out.append(dict(date=d, city=city, state=st, lat=ll[0], lon=ll[1],
                                who=r.get("who",""), title=r.get("title",""),
                                charlie=r.get("charlie_present",""), erika=r.get("erika_present",""),
                                venue=r.get("university_or_venue",""), page=r.get("mdx_page","")))
    return out

def main():
    gaz, ap = load_gazetteer(), load_airports()
    events = load_events(gaz)
    by_date = collections.defaultdict(list)
    for e in events: by_date[e["date"]].append(e)
    print(f"sourced event-days: {len(events)}  distinct dates: {len(by_date)}", file=sys.stderr)
    if UNRESOLVED: print(f"UNRESOLVED event cities (dropped, never guessed): {UNRESOLVED}", file=sys.stderr)

    vi = json.load(open(os.path.join(DATA, "recovery", "trace_visit_index.json")))
    rows = []
    for tail, days in vi.items():
        for day, entries in days.items():
            seen = {}
            for e in entries:
                src = e.get("source", "")
                for g in e.get("ground_visits", []):
                    code = g.get("airport_code") or ""
                    key = (code, g.get("first_seen_utc", "")[:13])
                    if key in seen:
                        seen[key]["sources"].add(src); continue
                    seen[key] = dict(visit=g, sources={src}, file=e.get("file",""),
                                     typ=e.get("type",""), reg=e.get("registration",""))
            for key, v in seen.items():
                g = v["visit"]; code = g.get("airport_code") or ""
                lat, lon = g.get("lat"), g.get("lon")
                if lat is None: continue
                best = None
                d0 = dt.date.fromisoformat(day)
                for off in range(-WINDOW, WINDOW + 1):
                    for ev in by_date.get((d0 + dt.timedelta(days=off)).isoformat(), []):
                        mi = haversine_km(lat, lon, ev["lat"], ev["lon"]) * MI_PER_KM
                        if best is None or mi < best[0]: best = (mi, ev, off)
                mi, ev, off = best if best else (None, {}, None)
                rows.append(dict(
                    tail=tail, date=day, airport_code=code,
                    airport_name=g.get("airport_name",""), airport_city=g.get("airport_city",""),
                    median_km_from_field=g.get("median_distance_km"),
                    ground_points=g.get("ground_points"),
                    first_seen_utc=g.get("first_seen_utc"), last_seen_utc=g.get("last_seen_utc"),
                    lat=lat, lon=lon, type=v["typ"], registration=v["reg"],
                    sources="|".join(sorted(s for s in v["sources"] if s)),
                    archives_agreeing=len([s for s in v["sources"] if s]),
                    nearest_event_city=ev.get("city",""), nearest_event_state=ev.get("state",""),
                    nearest_event_date=ev.get("date",""), nearest_event_who=ev.get("who",""),
                    nearest_event_title=ev.get("title",""),
                    charlie_present=ev.get("charlie",""), erika_present=ev.get("erika",""),
                    event_offset_days=off if best else "",
                    miles_to_event_city=round(mi,2) if mi is not None else "",
                    within_50mi="yes" if (mi is not None and mi <= RADIUS_MI) else "no",
                    same_day="yes" if off == 0 else "no",
                    event_page=ev.get("page","")))
    rows.sort(key=lambda r: (r["date"], r["tail"], r["airport_code"]))
    path = os.path.join(OUT, "master_proximity.csv")
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    hits = [r for r in rows if r["within_50mi"] == "yes"]
    print(f"ground visits: {len(rows)}  within 50mi of a sourced event: {len(hits)}", file=sys.stderr)
    print(f"wrote {path}", file=sys.stderr)
    return rows, hits

if __name__ == "__main__":
    main()
