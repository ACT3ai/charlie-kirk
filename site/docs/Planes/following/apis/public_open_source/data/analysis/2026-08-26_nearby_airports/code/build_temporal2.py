import json, os, re, csv, math, glob
from collections import defaultdict
from datetime import date
import yaml

ROOT='/Users/bryanstarbuck/BGit/Bryan_git/charlie-kirk'
PL=os.path.join(ROOT,'site/docs/Planes'); FOL=os.path.join(PL,'following')
SCR='/private/tmp/claude-501/-Users-bryanstarbuck-BGit-Bryan-git-charlie-kirk-site-docs-Planes/9300dd48-3a6d-45a1-960c-5f5606096c22/scratchpad'
FOREIGN=['SU-BGM','SU-BND','SU-BTT','SU-BTU','SU-BTV','T7-ELL']
KIRK=['N102DZ','N1098L','N2100L','N40JD','N560TW','N582MM','N59906','N872RA','N888KG']

def hav(a,b,c,d):
    R=6371.0088; p1,p2=math.radians(a),math.radians(c)
    dp=math.radians(c-a); dl=math.radians(d-b)
    x=math.sin(dp/2)**2+math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*R*math.asin(math.sqrt(x))
MI=0.621371
def dd(s):
    y,m,d_=[int(x) for x in str(s).split('-')]; return date(y,m,d_)

# events
events=[]
for yf in sorted(glob.glob(os.path.join(FOL,'speaking','*.yaml'))):
    y=yaml.safe_load(open(yf)); ev=y['event']; loc=ev.get('location') or {}
    g=loc.get('geocode') or {}
    aa=(y.get('arrival_airport') or {}).get('chosen_airport') or {}
    awr=(y.get('airports_within_radius') or {}).get('list') or []
    events.append(dict(slug=y['page']['slug'], first=str(ev['dates']['first_day']), last=str(ev['dates']['last_day']),
        certainty=ev['dates'].get('certainty'), who=ev.get('who'), cls=ev.get('attendee_class'),
        charlie=str(ev.get('charlie_present')), erika=str(ev.get('erika_present')),
        city=loc.get('city'), state=loc.get('state'), country=loc.get('country'),
        lat=g.get('lat'), lon=g.get('lon'), arr=aa.get('airport_code'),
        radius_codes={a.get('airport_code') for a in awr}))
NA_COUNTRIES={'USA','US','United States','Canada','Mexico'}
for e in events: e['is_na']= (e['country'] in NA_COUNTRIES)

# coverage (asked / held tail-days, from filenames)
pat=re.compile(r'^(?P<tail>[A-Z0-9\-]+)_(?P<date>\d{4}-\d{2}-\d{2})_(?P<src>[a-z0-9\-]+)_trace_full(?P<miss>\.miss)?\.json(\.gz)?\.meta\.json$')
asked=defaultdict(set); held=defaultdict(set)
for t in FOREIGN+KIRK:
    d=os.path.join(PL,t,'data','recovered')
    if not os.path.isdir(d): continue
    for fn in os.listdir(d):
        m=pat.match(fn)
        if not m: continue
        asked[t].add(m.group('date'))
        if not m.group('miss'): held[t].add(m.group('date'))

tvi=json.load(open(os.path.join(FOL,'apis/public_open_source/data/recovery/trace_visit_index.json')))
NA=lambda la,lo: la is not None and lo is not None and 14.0<=la<=75.0 and -170.0<=lo<=-50.0

def visits(tails):
    rows=[]
    for t in tails:
        for day,recs in sorted(tvi.get(t,{}).items()):
            seen={}
            for r in recs:
                for gv in r.get('ground_visits',[]):
                    if not NA(gv.get('lat'),gv.get('lon')): continue
                    key=(gv.get('airport_code'),(gv.get('first_seen_utc') or '')[:16])
                    if key not in seen: seen[key]=dict(gv,sources=set())
                    seen[key]['sources'].add(r.get('source'))
            for k,gv in sorted(seen.items(), key=lambda kv: kv[1].get('first_seen_utc') or ''):
                rows.append(dict(tail=t,day=day,airport=gv.get('airport_code'),airport_name=gv.get('airport_name'),
                    lat=gv['lat'],lon=gv['lon'],first=gv.get('first_seen_utc'),last=gv.get('last_seen_utc'),
                    gpts=gv.get('ground_points'),sources=','.join(sorted(x for x in gv['sources'] if x))))
    return rows

frows=visits(FOREIGN)

WINS=[0,1,2,3,7]
out=[]
for r in frows:
    vd=dd(r['day']); o=dict(r); o['year']=r['day'][:4]
    o['era']='POST_DEATH' if r['day']>'2025-09-10' else ('DAY_OF' if r['day']=='2025-09-10' else 'BEFORE_DEATH')
    o['is_kilg']= 'yes' if r['airport']=='KILG' else 'no'
    for w in WINS:
        cands=[]
        for e in events:
            if not e['is_na'] or e['lat'] is None: continue
            ef,el=dd(e['first']),dd(e['last'])
            gap=0 if ef<=vd<=el else ((ef-vd).days if vd<ef else (vd-el).days)
            if gap<=w:
                cands.append((hav(r['lat'],r['lon'],e['lat'],e['lon'])*MI,gap,e))
        o[f'na_events_within_{w}d']=len(cands)
        if cands:
            mi,gap,e=min(cands,key=lambda c:(c[0],c[1]))
            o[f'w{w}_mi']=round(mi,1); o[f'w{w}_gap']=gap; o[f'w{w}_event']=e['slug']
            if w==2:
                o.update(w2_arr=e['arr'],w2_city=e['city'],w2_state=e['state'],w2_class=e['cls'],
                         w2_charlie=e['charlie'],w2_erika=e['erika'],w2_certainty=e['certainty'],
                         w2_in_radius='yes' if r['airport'] in e['radius_codes'] else 'no')
                if r['airport'] in e['radius_codes'] or mi<=40:
                    o['match_class']='SAME_AIRPORT' if (e['arr'] and e['arr']==r['airport']) else 'NEARBY_AIRPORT'
                elif mi<=100: o['match_class']='SAME_REGION_40_100MI'
                elif mi<=250: o['match_class']='REGION_100_250MI'
                else: o['match_class']='FAR_GT250MI'
        else:
            o[f'w{w}_mi']=''; o[f'w{w}_gap']=''; o[f'w{w}_event']=''
            if w==2:
                o.update(w2_arr='',w2_city='',w2_state='',w2_class='',w2_charlie='',w2_erika='',
                         w2_certainty='',w2_in_radius='',match_class='NO_NA_EVENT_WITHIN_2D')
    out.append(o)

cols=['tail','day','year','era','airport','airport_name','is_kilg','lat','lon','first','last','gpts','sources',
      'match_class','w2_in_radius','w2_mi','w2_gap','w2_event','w2_arr','w2_city','w2_state','w2_class',
      'w2_charlie','w2_erika','w2_certainty']
for w in WINS: cols += [f'na_events_within_{w}d',f'w{w}_mi',f'w{w}_gap',f'w{w}_event']
with open(os.path.join(SCR,'temporal_series.csv'),'w',newline='') as f:
    wtr=csv.DictWriter(f,fieldnames=cols); wtr.writeheader()
    for o in sorted(out,key=lambda x:(x['day'],x['tail'],x['first'] or '')): wtr.writerow({k:o.get(k,'') for k in cols})

# ---------- aggregate by year ----------
import statistics as st
def agg(rows,label):
    print('\n==== '+label+' ====')
    byy=defaultdict(list)
    for o in rows: byy[o['year']].append(o)
    print(f"{'yr':5} {'visitdays':>9} {'visitrec':>8} {'held':>5} {'asked':>6} {'cov%':>6} {'rate/100held':>12} {'SAME':>5} {'NEAR':>5} {'FAR':>4} {'NOEV':>5} {'medMi':>8} {'meanMi':>8}")
    for y in sorted(byy):
        rs=byy[y]
        vdays=len({(o['tail'],o['day']) for o in rs})
        h=sum(1 for t in FOREIGN for dt in held[t] if dt[:4]==y)
        a=sum(1 for t in FOREIGN for dt in asked[t] if dt[:4]==y)
        cov=100.0*h/a if a else 0
        mis=[float(o['w2_mi']) for o in rs if o['w2_mi']!='']
        cnt=defaultdict(int)
        for o in rs: cnt[o['match_class']]+=1
        near=cnt['NEARBY_AIRPORT']
        far=cnt['SAME_REGION_40_100MI']+cnt['REGION_100_250MI']+cnt['FAR_GT250MI']
        rate=100.0*vdays/h if h else float('nan')
        print(f"{y:5} {vdays:9d} {len(rs):8d} {h:5d} {a:6d} {cov:6.1f} {rate:12.1f} {cnt['SAME_AIRPORT']:5d} {near:5d} {far:4d} {cnt['NO_NA_EVENT_WITHIN_2D']:5d} "
              f"{(st.median(mis) if mis else float('nan')):8.1f} {(st.mean(mis) if mis else float('nan')):8.1f}")
agg(out,'ALL foreign-fleet NA ground-visit records')
agg([o for o in out if o['is_kilg']=='no'],'EXCLUDING KILG (documented customs/fuel stop)')

json.dump({'held':{t:sorted(held[t]) for t in FOREIGN},'asked':{t:sorted(asked[t]) for t in FOREIGN}},
          open(os.path.join(SCR,'_coverage_days.json'),'w'))
print('\nrows',len(out))
