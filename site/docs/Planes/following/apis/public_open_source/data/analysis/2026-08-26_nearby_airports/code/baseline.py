import json,csv,glob,math,yaml,pickle
from datetime import date
from collections import Counter,defaultdict
ROOT="/Users/bryanstarbuck/BGit/Bryan_git/charlie-kirk"; FOLL=f"{ROOT}/site/docs/Planes/following"; POS=f"{FOLL}/apis/public_open_source"
def hav(a,b,c,d):
    R=3958.7613; p1,p2=math.radians(a),math.radians(c); dp=math.radians(c-a); dl=math.radians(d-b)
    h=math.sin(dp/2)**2+math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*R*math.asin(min(1,math.sqrt(h)))
EV=[]
for y in sorted(glob.glob(f"{FOLL}/speaking/*.yaml")):
    d=yaml.safe_load(open(y)); e=d["event"]; loc=e["location"]; g=loc.get("geocode") or {}
    if not g.get("lat"): continue
    fd=e["dates"]["first_day"]
    EV.append(dict(slug=d["page"]["slug"],lat=g["lat"],lon=g["lon"],d=date.fromisoformat(str(fd)),
        ac=e.get("attendee_class",""),who=e["who"],city=loc["city"],ek=e.get("erika_present","")))
rows=pickle.load(open('_inv_rows.pkl','rb'))
print("=== event composition (134 geocoded of 139) ===")
print(Counter(e["ac"] for e in EV))
print("by year:",Counter(e["d"].year for e in EV))
print()
print("=== BASELINE: for each airport the foreign fleet was on the ground at, how many of the 134 events are within N mi (ANY date) ===")
apts={}
for r in rows: apts.setdefault(r["code"],(r["lat"],r["lon"],[]))[2].append(r["day"])
for code,(la,lo,days) in sorted(apts.items(), key=lambda x:-len(x[1][2])):
    n100=sum(1 for e in EV if hav(la,lo,e["lat"],e["lon"])<=100)
    n40=sum(1 for e in EV if hav(la,lo,e["lat"],e["lon"])<=40)
    n250=sum(1 for e in EV if hav(la,lo,e["lat"],e["lon"])<=250)
    print(f"{code:6s} presence_days={len(days):3d}  events<=40mi={n40:3d}  <=100mi={n100:3d}  <=250mi={n250:3d}")
print()
print("=== Kirk-side fleet ground visits, Sept 2025 and Apr 2024 ===")
TVI=json.load(open(f"{POS}/data/recovery/trace_visit_index.json"))
KIRK=["N102DZ","N1098L","N2100L","N40JD","N560TW","N582MM","N59906","N872RA","N888KG"]
for tail in KIRK:
    for day,recs in sorted(TVI.get(tail,{}).items()):
        if day.startswith("2025-09") or day.startswith("2024-04"):
            gv=[g for r in recs for g in (r.get("ground_visits") or [])]
            if gv: print(tail,day,[ (g["airport_code"],g.get("airport_city")) for g in gv])
print()
print("=== Kirk-side fleet: total NA ground-visit days held ===")
for tail in KIRK:
    dd=set(d for d,recs in TVI.get(tail,{}).items() for r in recs for g in (r.get("ground_visits") or []) if g.get("lon") and -170<=g["lon"]<=-50)
    print(f"{tail}: {len(dd)} days, {min(dd) if dd else '-'} .. {max(dd) if dd else '-'}")
