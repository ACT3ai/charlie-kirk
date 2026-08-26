import glob,statistics,yaml,collections
D='/Users/bryanstarbuck/BGit/Bryan_git/charlie-kirk/site/docs/Planes/following/speaking'
off=[];noap=[];basis=collections.Counter()
for f in sorted(glob.glob(D+'/*.yaml')):
    y=yaml.safe_load(open(f)); slug=y['page']['slug']
    aw=y.get('airports_within_radius') or {}
    if not (aw.get('list') or []):
        noap.append((slug,y['event']['location'].get('city'),y['event']['location'].get('country')))
    aa=y.get('arrival_airport') or {}
    d=aa.get('distance_from_event_city_mi')
    basis[aa.get('selection_basis')]+=1
    if d is not None: off.append((d,slug))
off.sort()
ds=[d for d,_ in off]
print("distance ARRIVAL AIRPORT -> event city (mi), n=%d"%len(ds))
print("  min=%.1f p25=%.1f med=%.1f mean=%.1f p75=%.1f p90=%.1f max=%.1f"%(
  ds[0],ds[int(.25*len(ds))],statistics.median(ds),statistics.mean(ds),
  ds[int(.75*len(ds))],ds[int(.90*len(ds))],ds[-1]))
for t in (5,10,15,20,30):
    print("  events where centre is >%d mi from the venue city: %d (%.0f%%)"%(t,sum(1 for x in ds if x>t),100*sum(1 for x in ds if x>t)/len(ds)))
print("\nworst 12 offsets (disc is shifted this far off the venue):")
for d,s in off[-12:]: print("   %6.1f mi  %s"%(d,s))
print("\nEVENTS WITH *NO* AIRPORT SWEEP AT ALL (%d):"%len(noap))
for s,c,co in noap: print("   ",s,"|",c,"|",co)
print("\narrival-airport selection_basis:")
for k,v in basis.most_common(): print("   %3d  %s"%(v,k))
