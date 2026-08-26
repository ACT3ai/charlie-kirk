import glob,os,statistics,json,collections
import yaml
D='/Users/bryanstarbuck/BGit/Bryan_git/charlie-kirk/site/docs/Planes/following/speaking'
files=sorted(glob.glob(D+'/*.yaml'))
rows=[]
for f in files:
    y=yaml.safe_load(open(f))
    slug=y['page']['slug']
    aw=y.get('airports_within_radius') or {}
    lst=aw.get('list') or []
    geo=(y['event']['location'].get('geocode') or {})
    lat=geo.get('lat')
    caps=collections.Counter(a.get('jet_capability') for a in lst)
    rows.append(dict(slug=slug,f=f,lat=lat,
        count=aw.get('count'),n_list=len(lst),
        jet=aw.get('jet_capable_count'),
        lightjet=aw.get('light_jet_capable_count'),
        jet_recount=caps.get('jet_capable',0),
        centre=aw.get('centre_airport'),
        radius=aw.get('radius_miles'),
        caps=dict(caps)))
print("total yaml files:",len(rows))
print("with geocode lat:",sum(1 for r in rows if r['lat'] is not None))
print("with NO geocode lat:",sum(1 for r in rows if r['lat'] is None))
print("airports_within_radius missing/empty:",sum(1 for r in rows if not r['n_list']))
def d(x,n):
    x=sorted(x)
    print(f"{n}: n={len(x)} min={x[0]} p10={x[int(.1*len(x))]} med={statistics.median(x)} mean={statistics.mean(x):.1f} p90={x[int(.9*len(x))]} max={x[-1]} total={sum(x)}")
g=[r for r in rows if r['lat'] is not None]
print("\n-- restricted to geocoded (n=%d) --"%len(g))
d([r['n_list'] for r in g],"airports_within_40mi(list len)")
d([r['jet_recount'] for r in g],"jet_capable_40mi(recount)")
d([r['jet'] or 0 for r in g],"jet_capable_40mi(field)")
j=[r['jet_recount'] for r in g]
print("zero jet:",sum(1 for x in j if x==0),"one jet:",sum(1 for x in j if x==1),">=5:",sum(1 for x in j if x>=5),">=4:",sum(1 for x in j if x>=4))
print("\nALL 139 (incl. non-geocoded):")
d([r['n_list'] for r in rows],"airports_within_40mi ALL")
d([r['jet_recount'] for r in rows],"jet_capable ALL")
print("\nradii used:",collections.Counter(r['radius'] for r in rows))
json.dump(rows,open('/private/tmp/claude-501/-Users-bryanstarbuck-BGit-Bryan-git-charlie-kirk-site-docs-Planes/9300dd48-3a6d-45a1-960c-5f5606096c22/scratchpad/vrows.json','w'))
