#!/usr/bin/env python
"""INVERSION: start from every foreign-fleet ground-visit day we hold a trace for,
and ask which TPUSA/Kirk event is nearest in time and space. Read-only."""
import json, csv, glob, math, os, sys, yaml
from datetime import date, datetime, timedelta
from collections import defaultdict, Counter

ROOT = "/Users/bryanstarbuck/BGit/Bryan_git/charlie-kirk"
FOLL = f"{ROOT}/site/docs/Planes/following"
POS  = f"{FOLL}/apis/public_open_source"
OUT  = "/private/tmp/claude-501/-Users-bryanstarbuck-BGit-Bryan-git-charlie-kirk-site-docs-Planes/9300dd48-3a6d-45a1-960c-5f5606096c22/scratchpad"

FOREIGN = ["SU-BGM","SU-BND","SU-BTT","SU-BTU","SU-BTV","T7-ELL"]

def hav(a,b,c,d):
    R=3958.7613
    p1,p2=math.radians(a),math.radians(c)
    dp=math.radians(c-a); dl=math.radians(d-b)
    h=math.sin(dp/2)**2+math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*R*math.asin(min(1,math.sqrt(h)))

# ---------- ourairports ----------
AP={}
with open(f"{POS}/data/ourairports/airports.csv") as f:
    for r in csv.DictReader(f):
        try: la=float(r["latitude_deg"]); lo=float(r["longitude_deg"])
        except: continue
        rec=dict(lat=la,lon=lo,name=r["name"],city=r["municipality"],
                 region=r["iso_region"],country=r["iso_country"],type=r["type"])
        for k in (r["ident"],r["icao_code"],r["gps_code"],r["local_code"]):
            if k and k not in AP: AP[k]=rec

# ---------- following/airports.csv (customs ports, metro) ----------
CUSTOMS=set(); APT_METRO={}
with open(f"{FOLL}/airports.csv") as f:
    for r in csv.DictReader(f):
        c=r["airport_code"].strip()
        if r.get("is_us_customs_port","").strip().lower().startswith("yes"): CUSTOMS.add(c)
        if r.get("metro_area","").strip(): APT_METRO[c]=r["metro_area"].strip()

# ---------- events ----------
EV=[]
for y in sorted(glob.glob(f"{FOLL}/speaking/*.yaml")):
    d=yaml.safe_load(open(y))
    e=d["event"]; loc=e["location"]; g=loc.get("geocode") or {}
    ch=d.get("arrival_airport",{}).get("chosen_airport") or {}
    fd=e["dates"]["first_day"]; ld=e["dates"].get("last_day") or fd
    EV.append(dict(
        slug=d["page"]["slug"],
        title=e["title"], who=e["who"], attendee_class=e.get("attendee_class",""),
        charlie=e.get("charlie_present",""), erika=e.get("erika_present",""),
        first=date.fromisoformat(str(fd)), last=date.fromisoformat(str(ld)),
        city=loc["city"], state=loc.get("state",""), metro=loc.get("metro_area","") or "",
        lat=g.get("lat"), lon=g.get("lon"),
        apt=ch.get("airport_code"), apt_lat=ch.get("lat"), apt_lon=ch.get("lon"),
        apt_name=ch.get("name",""),
        radius_list=set(a.get("airport_code") for a in
            (d.get("airports_within_radius",{}) or {}).get("list",[]) if isinstance(a,dict)),
    ))
sys.stderr.write(f"events={len(EV)} geocoded={sum(1 for e in EV if e['lat'])}\n")

# ---------- overlaps.csv (date+tail already-known pairs) ----------
KNOWN=set(); KNOWN_ROWS=defaultdict(list)
with open(f"{FOLL}/overlaps.csv") as f:
    for r in csv.DictReader(f):
        t=(r.get("foreign_tail") or "").strip()
        dt=(r.get("date") or "").strip()
        if t and dt:
            KNOWN.add((dt,t)); KNOWN_ROWS[(dt,t)].append(r.get("overlap_id",""))

# ---------- presence days from trace_visit_index ----------
TVI=json.load(open(f"{POS}/data/recovery/trace_visit_index.json"))
visits=[]
for tail in FOREIGN:
    for day,recs in TVI.get(tail,{}).items():
        for rec in recs:
            for gv in rec.get("ground_visits") or []:
                la,lo=gv.get("lat"),gv.get("lon")
                if la is None: continue
                visits.append(dict(tail=tail,day=day,code=gv.get("airport_code"),
                    aname=gv.get("airport_name"),acity=gv.get("airport_city"),
                    lat=la,lon=lo,med_km=gv.get("median_distance_km"),
                    resolved=gv.get("resolved"),first=gv.get("first_seen_utc"),
                    last=gv.get("last_seen_utc"),pts=gv.get("ground_points"),
                    source=rec.get("source"),file=rec.get("file")))

def is_na(v):
    return -170 <= v["lon"] <= -50 and 10 <= v["lat"] <= 75

na=[v for v in visits if is_na(v)]
sys.stderr.write(f"ground_visits total={len(visits)} north_america={len(na)}\n")

# collapse duplicates: same tail+day+airport from multiple sources
agg={}
for v in na:
    k=(v["tail"],v["day"],v["code"] or f"UNRESOLVED_{v['lat']:.3f}_{v['lon']:.3f}")
    if k not in agg:
        agg[k]=dict(v); agg[k]["sources"]={v["source"]}; agg[k]["files"]=[v["file"]]
        agg[k]["pts"]=v["pts"] or 0
    else:
        a=agg[k]; a["sources"].add(v["source"]); a["files"].append(v["file"])
        a["pts"]=(a["pts"] or 0)+(v["pts"] or 0)
        if v["first"] and (not a["first"] or v["first"]<a["first"]): a["first"]=v["first"]
        if v["last"] and (not a["last"] or v["last"]>a["last"]): a["last"]=v["last"]
rows=sorted(agg.values(), key=lambda r:(r["day"],r["tail"],r["code"] or ""))
sys.stderr.write(f"unique tail-day-airport presence records = {len(rows)}\n")
sys.stderr.write(f"unique tail-days = {len(set((r['tail'],r['day']) for r in rows))}\n")

# ---------- scoring ----------
def gapdays(evd, vd):
    return (evd - vd).days

def ev_dist(v, e):
    """miles from the airport the plane was ON THE GROUND at, to event city + event airport"""
    dc = hav(v["lat"],v["lon"],e["lat"],e["lon"]) if e["lat"] is not None else None
    da = hav(v["lat"],v["lon"],e["apt_lat"],e["apt_lon"]) if e["apt_lat"] is not None else None
    return dc,da

def signed_gap(v_date, e):
    """0 if the visit falls inside the event's own date span; else signed days to nearest edge.
       negative = plane was there BEFORE the event, positive = AFTER."""
    if e["first"] <= v_date <= e["last"]: return 0
    if v_date < e["first"]: return (e["first"]-v_date).days * -1   # plane before event
    return (v_date-e["last"]).days                                  # plane after event

MAXMI=100.0; MAXGAP=3.0
out=[]
for r in rows:
    vd=date.fromisoformat(r["day"])
    cands=[]
    for e in EV:
        dc,da=ev_dist(r,e)
        g=signed_gap(vd,e)
        d_eff = dc if dc is not None else da
        if d_eff is None: continue
        comb = d_eff/MAXMI + abs(g)/MAXGAP
        cands.append((comb,d_eff,g,dc,da,e))
    cands.sort(key=lambda x:x[0])
    # nearest in time (min |gap|, ties -> nearer)
    nt=min(cands,key=lambda x:(abs(x[2]),x[1]))
    # nearest in space
    ns=min(cands,key=lambda x:(x[1],abs(x[2])))
    best=cands[0]
    top5=cands[:5]
    r["_cands"]=cands; r["_nt"]=nt; r["_ns"]=ns; r["_best"]=best; r["_top5"]=top5

    # bucket: evaluated over ALL events within +-3 days
    near=[c for c in cands if abs(c[2])<=MAXGAP]
    code=r["code"]
    bucket=None; bev=None; bdist=None; bgap=None
    same=[c for c in near if code and (c[5]["apt"]==code)]
    if same:
        c=min(same,key=lambda x:(abs(x[2]),x[1])); bucket="SAME_AIRPORT"; bev=c
    else:
        metro=APT_METRO.get(code)
        sm=[c for c in near if (metro and c[5]["metro"]==metro) or (code and code in c[5]["radius_list"])]
        if sm:
            c=min(sm,key=lambda x:(x[1],abs(x[2]))); bucket="SAME_METRO"; bev=c
        else:
            nb=[c for c in near if c[1]<=MAXMI]
            if nb:
                c=min(nb,key=lambda x:(x[1],abs(x[2]))); bucket="NEARBY_AIRPORT"; bev=c
            else:
                bucket = "KNOWN_TRANSIT" if code in CUSTOMS else "DISTANT"
                bev=None
    r["_bucket"]=bucket; r["_bev"]=bev
    out.append(r)

# ---------- write matrix ----------
hdr=["visit_date","tail","ground_airport","ground_airport_name","ground_airport_city",
     "lat","lon","median_dist_km","ground_points","first_seen_utc","last_seen_utc",
     "sources","n_source_files",
     "bucket",
     "bucket_event_slug","bucket_event_date","bucket_event_city","bucket_event_who",
     "bucket_event_airport","bucket_dist_to_event_city_mi","bucket_dist_to_event_airport_mi","bucket_gap_days",
     "nearest_in_time_slug","nearest_in_time_date","nearest_in_time_city","nearest_in_time_gap_days","nearest_in_time_dist_mi",
     "nearest_in_space_slug","nearest_in_space_date","nearest_in_space_city","nearest_in_space_dist_mi","nearest_in_space_gap_days",
     "best_combined_slug","best_combined_date","best_combined_city","best_combined_who","best_combined_attendee_class",
     "best_combined_dist_city_mi","best_combined_dist_airport_mi","best_combined_gap_days","best_combined_score",
     "best_combined_event_airport","same_airport_as_event",
     "in_overlaps_csv","overlaps_csv_ids","status",
     "top5"]
def evs(c):
    comb,d,g,dc,da,e=c
    return f"{e['slug']}|{e['first']}|{e['city']},{e['state']}|{e['who']}|dist_city={dc if dc is None else round(dc,1)}mi|dist_apt={da if da is None else round(da,1)}mi|gap={g:+d}d|score={comb:.2f}"

with open(f"{OUT}/inversion_matrix.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(hdr)
    for r in out:
        nt=r["_nt"]; ns=r["_ns"]; b=r["_best"]; bev=r["_bev"]
        key=(r["day"],r["tail"])
        known = key in KNOWN
        be=b[5]
        w.writerow([
            r["day"],r["tail"],r["code"],r["aname"],r["acity"],
            round(r["lat"],5),round(r["lon"],5),r["med_km"],r["pts"],r["first"],r["last"],
            ";".join(sorted(r["sources"])),len(r["files"]),
            r["_bucket"],
            bev[5]["slug"] if bev else "", bev[5]["first"] if bev else "",
            f"{bev[5]['city']}, {bev[5]['state']}" if bev else "",
            bev[5]["who"] if bev else "",
            bev[5]["apt"] if bev else "",
            round(bev[3],1) if bev and bev[3] is not None else "",
            round(bev[4],1) if bev and bev[4] is not None else "",
            f"{bev[2]:+d}" if bev else "",
            nt[5]["slug"],nt[5]["first"],f"{nt[5]['city']}, {nt[5]['state']}",f"{nt[2]:+d}",round(nt[1],1),
            ns[5]["slug"],ns[5]["first"],f"{ns[5]['city']}, {ns[5]['state']}",round(ns[1],1),f"{ns[2]:+d}",
            be["slug"],be["first"],f"{be['city']}, {be['state']}",be["who"],be["attendee_class"],
            round(b[3],1) if b[3] is not None else "", round(b[4],1) if b[4] is not None else "",
            f"{b[2]:+d}", round(b[0],3),
            be["apt"], "yes" if r["code"]==be["apt"] else "no",
            "yes" if known else "no", ";".join(KNOWN_ROWS.get(key,[])),
            ("KNOWN" if known else "NEW"),
            " || ".join(evs(c) for c in r["_top5"]),
        ])

json.dump({"n_rows":len(out)}, open(f"{OUT}/_inv_meta.json","w"))
# stash for crosstab
import pickle
pickle.dump([{k:v for k,v in r.items() if not k.startswith("_")} | {
    "bucket":r["_bucket"],
    "bev":( {"slug":r["_bev"][5]["slug"],"date":str(r["_bev"][5]["first"]),
             "city":r["_bev"][5]["city"]+", "+r["_bev"][5]["state"],
             "who":r["_bev"][5]["who"],"ac":r["_bev"][5]["attendee_class"],
             "apt":r["_bev"][5]["apt"],
             "dist_city":r["_bev"][3],"dist_apt":r["_bev"][4],"gap":r["_bev"][2]} if r["_bev"] else None),
    "best":{"slug":r["_best"][5]["slug"],"date":str(r["_best"][5]["first"]),
            "city":r["_best"][5]["city"]+", "+r["_best"][5]["state"],
            "who":r["_best"][5]["who"],"ac":r["_best"][5]["attendee_class"],
            "dist_city":r["_best"][3],"dist_apt":r["_best"][4],"gap":r["_best"][2],
            "score":r["_best"][0],"apt":r["_best"][5]["apt"]},
    "known": (r["day"],r["tail"]) in KNOWN,
    "ovids": ";".join(KNOWN_ROWS.get((r["day"],r["tail"]),[])),
    "sources":sorted(r["sources"]),
} for r in out], open(f"{OUT}/_inv_rows.pkl","wb"))
print("rows written:",len(out))
