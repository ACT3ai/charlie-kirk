import json,csv,glob,math,yaml,pickle
from datetime import date
from collections import defaultdict,Counter
ROOT="/Users/bryanstarbuck/BGit/Bryan_git/charlie-kirk"; FOLL=f"{ROOT}/site/docs/Planes/following"; POS=f"{FOLL}/apis/public_open_source"
def hav(a,b,c,d):
    R=3958.7613; p1,p2=math.radians(a),math.radians(c)
    dp=math.radians(c-a); dl=math.radians(d-b)
    h=math.sin(dp/2)**2+math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*R*math.asin(min(1,math.sqrt(h)))
EV=[]
for y in sorted(glob.glob(f"{FOLL}/speaking/*.yaml")):
    d=yaml.safe_load(open(y)); e=d["event"]; loc=e["location"]; g=loc.get("geocode") or {}
    ch=d.get("arrival_airport",{}).get("chosen_airport") or {}
    if not g.get("lat"): continue
    fd=e["dates"]["first_day"]; ld=e["dates"].get("last_day") or fd
    EV.append(dict(slug=d["page"]["slug"],who=e["who"],ac=e.get("attendee_class",""),
        ch=e.get("charlie_present",""),ek=e.get("erika_present",""),
        first=date.fromisoformat(str(fd)),last=date.fromisoformat(str(ld)),
        city=loc["city"],state=loc.get("state",""),metro=loc.get("metro_area","") or "",
        lat=g["lat"],lon=g["lon"],apt=ch.get("airport_code"),apt_lat=ch.get("lat"),apt_lon=ch.get("lon"),
        title=e["title"]))
rows=pickle.load(open('_inv_rows.pkl','rb'))
KNOWN=set()
for r in csv.DictReader(open(f"{FOLL}/overlaps.csv")):
    t=(r.get("foreign_tail") or "").strip(); dt=(r.get("date") or "").strip()
    for tt in [x.strip() for x in t.replace(' or ',';').split(';')]:
        if tt and dt: KNOWN.add((dt,tt))
def sg(vd,e):
    if e["first"]<=vd<=e["last"]: return 0
    if vd<e["first"]: return -(e["first"]-vd).days
    return (vd-e["last"]).days
pairs=[]
for r in rows:
    vd=date.fromisoformat(r["day"])
    for e in EV:
        dc=hav(r["lat"],r["lon"],e["lat"],e["lon"])
        da=hav(r["lat"],r["lon"],e["apt_lat"],e["apt_lon"]) if e["apt_lat"] else None
        g=sg(vd,e)
        if dc<=150 and abs(g)<=7:
            pairs.append(dict(day=r["day"],tail=r["tail"],code=r["code"],dc=dc,da=da,gap=g,
                slug=e["slug"],edate=str(e["first"]),city=f"{e['city']}, {e['state']}",who=e["who"],
                ac=e["ac"],apt=e["apt"],title=e["title"],
                known=(r["day"],r["tail"]) in KNOWN, same=(r["code"]==e["apt"]),
                bucket=r["bucket"],src=";".join(r["sources"])))
pairs.sort(key=lambda p:(p["dc"]/100+abs(p["gap"])/3))
w=csv.writer(open("inversion_pairs_wide.csv","w",newline=""))
w.writerow("visit_date tail ground_airport event_slug event_date event_city event_who attendee_class event_airport same_airport dist_to_event_city_mi dist_to_event_airport_mi gap_days score bucket_pm3 tail_date_in_overlaps_csv source".split())
for p in pairs:
    w.writerow([p["day"],p["tail"],p["code"],p["slug"],p["edate"],p["city"],p["who"],p["ac"],p["apt"],
        "yes" if p["same"] else "no",round(p["dc"],1),round(p["da"],1) if p["da"] else "",f"{p['gap']:+d}",
        round(p["dc"]/100+abs(p["gap"])/3,3),p["bucket"],"yes" if p["known"] else "no",p["src"]])
print("wide pairs (<=150mi, +-7d):",len(pairs))
print()
for p in pairs:
    print(f"{p['day']} {p['tail']:7s} {p['code']:5s} -> {p['slug']:32s} {p['edate']} {p['city']:22s} who={p['who']:8s} ac={p['ac']:22s} evapt={p['apt']} same={'Y' if p['same'] else 'N'} dc={p['dc']:6.1f}mi da={(p['da'] or 0):6.1f}mi gap={p['gap']:+d} known={'Y' if p['known'] else 'N'}")
