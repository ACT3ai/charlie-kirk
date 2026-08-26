import glob,collections,statistics,yaml
D='/Users/bryanstarbuck/BGit/Bryan_git/charlie-kirk/site/docs/Planes/following/speaking'
files=sorted(glob.glob(D+'/*.yaml'))
IN=OUT=0
ev_in=ev_out=0
out_ap=collections.Counter(); in_ap=collections.Counter()
out_su=0; in_su=0
ev_out_su=[]
dists=[]
rows=[]
for f in files:
    y=yaml.safe_load(open(f))
    slug=y['page']['slug']
    tp=y.get('tracked_plane_presence') or {}
    inside=tp.get('from_adsb_traces') or []
    jo=tp.get('just_outside_the_radius') or {}
    outside=jo.get('adsb_ground_contacts') or []
    IN+=len(inside); OUT+=len(outside)
    if inside: ev_in+=1
    if outside: ev_out+=1
    for r in inside:
        in_ap[r.get('airport_code')]+=1
        if r.get('is_egyptian_su'): in_su+=1
    su_here=0
    for r in outside:
        out_ap[r.get('airport_code')]+=1
        dists.append(r.get('distance_from_arrival_airport_mi'))
        if r.get('is_egyptian_su'): out_su+=1; su_here+=1
    if su_here: ev_out_su.append((slug,su_here))
    rows.append((slug,len(inside),len(outside)))
print("ADS-B ground contacts INSIDE 40mi radius :",IN,"  across",ev_in,"events")
print("ADS-B ground contacts OUTSIDE (40-60mi)  :",OUT,"  across",ev_out,"events")
print("share of observed contacts that the 40mi disc MISSED: %.1f%%"%(100*OUT/(IN+OUT)))
print()
print("EGYPTIAN SU- contacts inside 40mi :",in_su)
print("EGYPTIAN SU- contacts OUTSIDE 40mi:",out_su)
if in_su+out_su:
    print("share of EGYPTIAN contacts missed by the 40mi disc: %.1f%%"%(100*out_su/(in_su+out_su)))
print()
print("events where an EGYPTIAN SU- contact fell OUTSIDE the disc:",len(ev_out_su))
for s,n in ev_out_su: print("   ",s,n)
print()
print("top airports OUTSIDE the disc:",out_ap.most_common(10))
print("top airports INSIDE  the disc:",in_ap.most_common(10))
if dists:
    ds=sorted(x for x in dists if x is not None)
    print("\ndistance of missed contacts from centre (mi): min=%.1f med=%.1f max=%.1f"%(ds[0],statistics.median(ds),ds[-1]))
    print("missed contacts within 41-45mi of centre:",sum(1 for x in ds if x<=45),"of",len(ds))
