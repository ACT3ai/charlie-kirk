import json,csv,math,datetime as dt,collections,random
POS='/Users/bryanstarbuck/BGit/Bryan_git/charlie-kirk/site/docs/Planes/following/apis/public_open_source'
FOREIGN=['SU-BGM','SU-BND','SU-BTT','SU-BTU','SU-BTV','T7-ELL']
KIRK=['N102DZ','N1098L','N2100L','N40JD','N560TW','N582MM','N59906','N872RA','N888KG']
def hav(a,b,c,d):
    R=3958.7613; p1,p2=math.radians(a),math.radians(c); dp=p2-p1; dl=math.radians(d-b)
    return 2*R*math.asin(math.sqrt(math.sin(dp/2)**2+math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2))
events=[e for e in json.load(open('events.json')) if e['lat'] is not None]
tvi=json.load(open(POS+'/data/recovery/trace_visit_index.json'))
GV=collections.defaultdict(list); HELD=collections.defaultdict(set)
for t,days in tvi.items():
    for day,recs in days.items():
        HELD[t].add(day)
        for r in recs:
            for g in r.get('ground_visits',[]):
                GV[t].append((day,g['airport_code'],g['lat'],g['lon'],r.get('source')))
print("=== inventory of ground visits on disk ===")
for fl,ts in (('FOREIGN',FOREIGN),('KIRK',KIRK)):
    n=sum(len(GV[t]) for t in ts); dys=len({(t,d) for t in ts for d,*_ in GV[t]})
    held=sum(len(HELD[t]) for t in ts)
    print(f"{fl}: trace-days held={held}  distinct (tail,day) with >=1 ground visit={dys}  ground visits={n}")
    ac=collections.Counter(a for t in ts for _,a,*_ in GV[t])
    print("   top airports:",ac.most_common(12))
# US only ground visits
def isus(lat,lon): return 24<lat<50 and -125<lon<-66
for fl,ts in (('FOREIGN',FOREIGN),('KIRK',KIRK)):
    us={(t,d) for t in ts for d,a,la,lo,s in GV[t] if isus(la,lo)}
    print(f"{fl}: distinct (tail,day) with a CONUS ground visit = {len(us)}")

print("\n=== PLACEBO: shift every event date by +/- N days, recompute ground pairs ===")
def pairs(shift,R,W,ts):
    s=set()
    for e in events:
        a=dt.date.fromisoformat(e['first'])+dt.timedelta(days=shift)
        b=dt.date.fromisoformat(e['last'])+dt.timedelta(days=shift)
        dl={(a+dt.timedelta(days=i)).isoformat() for i in range(-W,(b-a).days+W+1)}
        for t in ts:
            for d,ap,la,lo,src in GV[t]:
                if d in dl and hav(e['lat'],e['lon'],la,lo)<=R: s.add((e['slug'],t)); break
    return len(s)
for fl,ts in (('FOREIGN',FOREIGN),('KIRK',KIRK)):
    for R in (40,150):
        real=pairs(0,R,2,ts)
        pl=[pairs(sh,R,2,ts) for sh in (-365,-180,-120,-90,-60,-30,30,60,90,120,180,365)]
        import statistics
        print(f"{fl} R={R} W=2: REAL={real}  placebo shifts mean={statistics.mean(pl):.1f} max={max(pl)} vals={pl}")
