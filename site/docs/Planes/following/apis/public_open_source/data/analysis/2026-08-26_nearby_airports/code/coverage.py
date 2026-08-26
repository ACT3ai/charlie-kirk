import json,glob,yaml,math,csv,pickle
from datetime import date,timedelta
from collections import Counter,defaultdict
ROOT="/Users/bryanstarbuck/BGit/Bryan_git/charlie-kirk"; FOLL=f"{ROOT}/site/docs/Planes/following"; POS=f"{FOLL}/apis/public_open_source"
TVI=json.load(open(f"{POS}/data/recovery/trace_visit_index.json"))
FOR=["SU-BGM","SU-BND","SU-BTT","SU-BTU","SU-BTV","T7-ELL"]
EVD=set()
for y in sorted(glob.glob(f"{FOLL}/speaking/*.yaml")):
    d=yaml.safe_load(open(y)); e=d["event"]
    f0=date.fromisoformat(str(e["dates"]["first_day"])); l0=date.fromisoformat(str(e["dates"].get("last_day") or e["dates"]["first_day"]))
    dd=f0
    while dd<=l0: EVD.add(dd); dd+=timedelta(days=1)
def near_ev(d,n):
    return any(abs((d-e).days)<=n for e in EVD)
print("== foreign fleet: days for which we hold ANY trace, and whether they sit in an event window ==")
allsrc=Counter(); inw=Counter(); tot=Counter()
daysets=defaultdict(set)
for t in FOR:
    for day,recs in TVI.get(t,{}).items():
        dd=date.fromisoformat(day); daysets[t].add(dd)
        for r in recs: allsrc[r.get("source")]+=1
        tot[dd.year]+=1
        if near_ev(dd,2): inw[dd.year]+=1
alld=set().union(*daysets.values())
print("source counts:",dict(allsrc))
print("distinct foreign-fleet trace-days:",len(alld))
print("within +-2d of an event:",sum(1 for d in alld if near_ev(d,2)),"/",len(alld))
print("is 1st of month:",sum(1 for d in alld if d.day==1))
print("neither:",sum(1 for d in alld if not near_ev(d,2) and d.day!=1))
print("by year (trace-days):",dict(sorted(tot.items())))
print()
rows=pickle.load(open('_inv_rows.pkl','rb'))
print("== presence-day source provenance ==")
c=Counter()
for r in rows: c[tuple(r["sources"])]+=1
for k,v in c.most_common(): print(" ",k,v)
print()
print("== presence-days: is the day inside an event +-2 window? ==")
pin=Counter()
for r in rows:
    dd=date.fromisoformat(r["day"]); pin[(dd.year, near_ev(dd,2))]+=1
for k in sorted(pin): print(" ",k,pin[k])
