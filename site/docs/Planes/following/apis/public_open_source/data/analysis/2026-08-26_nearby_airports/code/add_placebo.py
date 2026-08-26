import json,csv,math,datetime as dt,collections
POS='/Users/bryanstarbuck/BGit/Bryan_git/charlie-kirk/site/docs/Planes/following/apis/public_open_source'
FOREIGN=['SU-BGM','SU-BND','SU-BTT','SU-BTU','SU-BTV','T7-ELL']
KIRK=['N102DZ','N1098L','N2100L','N40JD','N560TW','N582MM','N59906','N872RA','N888KG']
SHIFTS=(-365,-180,-120,-90,-60,-30,30,60,90,120,180,365)
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
                GV[t][day].append((g['lat'],g['lon']))
def run(shift,R,W,ts):
    pairs=set(); cov=0; hit=0
    for e in events:
        a=dt.date.fromisoformat(e['first'])+dt.timedelta(days=shift)
        b=dt.date.fromisoformat(e['last'])+dt.timedelta(days=shift)
        dl={(a+dt.timedelta(days=i)).isoformat() for i in range(-W,(b-a).days+W+1)}
        for t in ts:
            for d in dl & HELD[t]:
                cov+=1
                if any(hav(e['lat'],e['lon'],la,lo)<=R for la,lo in GV[t][d]):
                    hit+=1; pairs.add((e['slug'],t))
    return len(pairs),hit,cov
rows=list(csv.DictReader(open('radius_window_matrix.csv')))
for r in rows:
    ts=FOREIGN if r['fleet']=='FOREIGN' else KIRK
    R=int(r['radius_mi']); W=int(r['window_days'])
    _,h,c=run(0,R,W,ts)
    ph=pc=pp=0
    for s in SHIFTS:
        p,hh,cc=run(s,R,W,ts); pp+=p; ph+=hh; pc+=cc
    r['real_hit_aircraft_days']=h
    r['real_hit_rate_pct']=round(100*h/c,3) if c else 0
    r['placebo_pairs_mean']=round(pp/len(SHIFTS),1)
    r['placebo_hit_rate_pct']=round(100*ph/pc,3) if pc else 0
    r['lift_over_placebo']=(round((h/c)/(ph/pc),2) if pc and ph and c else 'INF' if h else 0)
with open('radius_window_matrix.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print('ok')
