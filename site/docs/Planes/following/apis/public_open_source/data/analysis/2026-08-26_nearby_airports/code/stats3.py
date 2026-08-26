import json,math,datetime as dt,collections,statistics
POS='/Users/bryanstarbuck/BGit/Bryan_git/charlie-kirk/site/docs/Planes/following/apis/public_open_source'
FOREIGN=['SU-BGM','SU-BND','SU-BTT','SU-BTU','SU-BTV','T7-ELL']
KIRK=['N102DZ','N1098L','N2100L','N40JD','N560TW','N582MM','N59906','N872RA','N888KG']
def hav(a,b,c,d):
    R=3958.7613; p1,p2=math.radians(a),math.radians(c); dp=p2-p1; dl=math.radians(d-b)
    return 2*R*math.asin(math.sqrt(math.sin(dp/2)**2+math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2))
events=[e for e in json.load(open('events.json')) if e['lat'] is not None]
tvi=json.load(open(POS+'/data/recovery/trace_visit_index.json'))
GV=collections.defaultdict(lambda: collections.defaultdict(list)); HELD=collections.defaultdict(set)
for t,days in tvi.items():
    for day,recs in days.items():
        HELD[t].add(day)
        for r in recs:
            for g in r.get('ground_visits',[]):
                GV[t][day].append((g['airport_code'],g['lat'],g['lon'],r.get('source'),g.get('ground_points')))

print("=== BASELINE foreign pairs at R=40 W=2 ===")
for e in events:
    a=dt.date.fromisoformat(e['first']); b=dt.date.fromisoformat(e['last'])
    dl={(a+dt.timedelta(days=i)).isoformat() for i in range(-2,(b-a).days+3)}
    for t in FOREIGN:
        for d in dl & set(GV[t]):
            for ap,la,lo,src,pts in GV[t][d]:
                dd=hav(e['lat'],e['lon'],la,lo)
                if dd<=40:
                    print(f"  {e['slug']} {e['city']},{e['state']} {e['attendee_class']} charlie={e['charlie_present']} | {t} {d} {ap} {dd:.1f}mi pts={pts} src={src}")

print("\n=== COVERAGE-NORMALISED HIT RATE (hits per covered aircraft-day) ===")
def rate(shift,R,W,ts):
    cov=0; hit=0
    for e in events:
        a=dt.date.fromisoformat(e['first'])+dt.timedelta(days=shift)
        b=dt.date.fromisoformat(e['last'])+dt.timedelta(days=shift)
        dl={(a+dt.timedelta(days=i)).isoformat() for i in range(-W,(b-a).days+W+1)}
        for t in ts:
            for d in dl & HELD[t]:
                cov+=1
                if any(hav(e['lat'],e['lon'],la,lo)<=R for ap,la,lo,src,pts in GV[t][d]): hit+=1
    return hit,cov
for fl,ts in (('FOREIGN',FOREIGN),('KIRK',KIRK)):
    print(fl)
    for R in (40,75,100,150):
        h,c=rate(0,R,2,ts)
        pls=[rate(sh,R,2,ts) for sh in (-365,-180,-120,-90,-60,-30,30,60,90,120,180,365)]
        ph=sum(x[0] for x in pls); pc=sum(x[1] for x in pls)
        print(f"  R={R:3d}: REAL {h}/{c} = {100*h/c:.2f}%   PLACEBO {ph}/{pc} = {100*ph/pc if pc else 0:.2f}%   lift x{(h/c)/(ph/pc) if pc and ph else float('inf'):.1f}" if ph else
              f"  R={R:3d}: REAL {h}/{c} = {100*h/c:.2f}%   PLACEBO {ph}/{pc} = 0.00%   lift infinite")
