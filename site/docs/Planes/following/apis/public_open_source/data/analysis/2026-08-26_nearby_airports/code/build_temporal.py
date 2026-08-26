import json, os, re, csv, math, sys, glob
from collections import defaultdict
import yaml

ROOT='/Users/bryanstarbuck/BGit/Bryan_git/charlie-kirk'
PL=os.path.join(ROOT,'site/docs/Planes')
FOL=os.path.join(PL,'following')
SCR='/private/tmp/claude-501/-Users-bryanstarbuck-BGit-Bryan-git-charlie-kirk-site-docs-Planes/9300dd48-3a6d-45a1-960c-5f5606096c22/scratchpad'
FOREIGN=['SU-BGM','SU-BND','SU-BTT','SU-BTU','SU-BTV','T7-ELL']

def hav(a,b,c,d):
    R=6371.0088
    p1,p2=math.radians(a),math.radians(c)
    dp=math.radians(c-a); dl=math.radians(d-b)
    x=math.sin(dp/2)**2+math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*R*math.asin(math.sqrt(x))

# ---------- 1. coverage: asked vs held (tail,date) from filenames ----------
asked=defaultdict(set); held=defaultdict(set)
pat=re.compile(r'^(?P<tail>[A-Z0-9\-]+)_(?P<date>\d{4}-\d{2}-\d{2})_(?P<src>[a-z0-9\-]+)_trace_full(?P<miss>\.miss)?\.json(\.gz)?\.meta\.json$')
for t in FOREIGN:
    d=os.path.join(PL,t,'data','recovered')
    if not os.path.isdir(d): continue
    for fn in os.listdir(d):
        m=pat.match(fn)
        if not m: continue
        dt=m.group('date')
        asked[t].add(dt)
        if not m.group('miss'):
            held[t].add(dt)

# ---------- 2. events ----------
events=[]
for yf in sorted(glob.glob(os.path.join(FOL,'speaking','*.yaml'))):
    y=yaml.safe_load(open(yf))
    ev=y.get('event',{})
    g=(ev.get('location') or {}).get('geocode') or {}
    aa=(y.get('arrival_airport') or {}).get('chosen_airport') or {}
    events.append(dict(
        slug=y['page']['slug'],
        first=str(ev['dates']['first_day']), last=str(ev['dates']['last_day']),
        certainty=ev['dates'].get('certainty'),
        who=ev.get('who'), cls=ev.get('attendee_class'),
        charlie=str(ev.get('charlie_present')), erika=str(ev.get('erika_present')),
        city=(ev.get('location') or {}).get('city'), state=(ev.get('location') or {}).get('state'),
        country=(ev.get('location') or {}).get('country'),
        lat=g.get('lat'), lon=g.get('lon'),
        arr=aa.get('airport_code'),
    ))
print('events:',len(events), 'with geocode:', sum(1 for e in events if e['lat'] is not None))

from datetime import date, timedelta
def d(s): 
    y,m,dd=[int(x) for x in s.split('-')]; return date(y,m,dd)

# ---------- 3. foreign fleet North American ground-visit days ----------
tvi=json.load(open(os.path.join(FOL,'apis/public_open_source/data/recovery/trace_visit_index.json')))

NA=lambda la,lo: (la is not None and lo is not None and 14.0<=la<=75.0 and -170.0<=lo<=-50.0)

rows=[]
for t in FOREIGN:
    for day,recs in sorted(tvi.get(t,{}).items()):
        # merge ground visits across sources for this tail-day; dedupe by (airport, first_seen minute)
        seen={}
        for r in recs:
            src=r.get('source')
            for gv in r.get('ground_visits',[]):
                if not NA(gv.get('lat'),gv.get('lon')): continue
                key=(gv.get('airport_code'), (gv.get('first_seen_utc') or '')[:16])
                if key not in seen:
                    seen[key]=dict(gv); seen[key]['sources']=set()
                seen[key]['sources'].add(src)
        for (ac,fs),gv in sorted(seen.items(), key=lambda kv: kv[1].get('first_seen_utc') or ''):
            rows.append(dict(tail=t, day=day, airport=ac, airport_name=gv.get('airport_name'),
                             city=gv.get('airport_city'), lat=gv['lat'], lon=gv['lon'],
                             first=gv.get('first_seen_utc'), last=gv.get('last_seen_utc'),
                             gpts=gv.get('ground_points'), sources=','.join(sorted(x for x in gv['sources'] if x))))
print('NA ground-visit records:', len(rows))
print('distinct tail-days:', len({(r['tail'],r['day']) for r in rows}))

# ---------- 4. match each visit to nearest event ----------
WINDOWS=[0,1,2,3,7]
out=[]
for r in rows:
    vd=d(r['day'])
    best=None; best2=None
    for e in events:
        if e['lat'] is None: continue
        ef,el=d(e['first']),d(e['last'])
        # temporal gap in days (0 if visit day falls inside event span)
        if ef<=vd<=el: gap=0
        elif vd<ef: gap=(ef-vd).days
        else: gap=(vd-el).days
        km=hav(r['lat'],r['lon'],e['lat'],e['lon'])
        cand=dict(gap=gap,km=km,e=e)
        # nearest in space among events within +-2 days
        if gap<=2:
            if best is None or km<best['km']: best=cand
        if best2 is None or (gap,km)<(best2['gap'],best2['km']): best2=cand
    o=dict(r)
    for w in WINDOWS:
        near=[c for c in ([] ) ]
    # counts of events within windows and various radii
    for w in WINDOWS:
        cnt=0; cntnear=0
        for e in events:
            if e['lat'] is None: continue
            ef,el=d(e['first']),d(e['last'])
            if ef<=vd<=el: gap=0
            elif vd<ef: gap=(ef-vd).days
            else: gap=(vd-el).days
            if gap<=w:
                cnt+=1
                if hav(r['lat'],r['lon'],e['lat'],e['lon'])<=161: cntnear+=1  # 100 mi
        o[f'events_within_{w}d']=cnt
        o[f'events_within_{w}d_and_100mi']=cntnear
    if best:
        e=best['e']
        o.update(w2_event=e['slug'], w2_gap_days=best['gap'], w2_km=round(best['km'],1),
                 w2_mi=round(best['km']*0.621371,1), w2_arr_airport=e['arr'],
                 w2_city=e['city'], w2_state=e['state'], w2_class=e['cls'],
                 w2_charlie=e['charlie'], w2_erika=e['erika'], w2_certainty=e['certainty'])
    else:
        o.update(w2_event='', w2_gap_days='', w2_km='', w2_mi='', w2_arr_airport='',
                 w2_city='', w2_state='', w2_class='', w2_charlie='', w2_erika='', w2_certainty='')
    e=best2['e']
    o.update(any_event=e['slug'], any_gap_days=best2['gap'], any_km=round(best2['km'],1),
             any_mi=round(best2['km']*0.621371,1), any_arr_airport=e['arr'], any_class=e['cls'])
    # classification, on the ±2d window
    if not best:
        o['match_class']='NO_EVENT_IN_WINDOW'
    else:
        same = (best['e']['arr'] and best['e']['arr']==r['airport'])
        mi=best['km']*0.621371
        if same: o['match_class']='SAME_AIRPORT'
        elif mi<=40: o['match_class']='NEARBY_LE40MI'
        elif mi<=100: o['match_class']='NEARBY_40_100MI'
        elif mi<=250: o['match_class']='REGION_100_250MI'
        else: o['match_class']='FAR_GT250MI'
    o['year']=r['day'][:4]
    o['era']='post_death' if r['day']>'2025-09-10' else ('day_of_or_before')
    out.append(o)

cols=['tail','day','year','era','airport','airport_name','city','lat','lon','first','last','gpts','sources',
      'match_class','w2_event','w2_gap_days','w2_mi','w2_km','w2_arr_airport','w2_city','w2_state','w2_class',
      'w2_charlie','w2_erika','w2_certainty','any_event','any_gap_days','any_mi','any_km','any_arr_airport','any_class']+ \
     [f'events_within_{w}d' for w in WINDOWS]+[f'events_within_{w}d_and_100mi' for w in WINDOWS]
with open(os.path.join(SCR,'temporal_series.csv'),'w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=cols); w.writeheader()
    for o in sorted(out,key=lambda x:(x['day'],x['tail'],x['first'] or '')):
        w.writerow({k:o.get(k,'') for k in cols})

json.dump(dict(asked={t:sorted(asked[t]) for t in FOREIGN}, held={t:sorted(held[t]) for t in FOREIGN}),
          open(os.path.join(SCR,'_coverage_days.json'),'w'))
print('wrote temporal_series.csv rows=',len(out))
