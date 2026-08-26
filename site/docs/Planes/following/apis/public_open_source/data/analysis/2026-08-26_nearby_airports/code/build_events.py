import yaml, glob, json, os, sys, math
SPK='/Users/bryanstarbuck/BGit/Bryan_git/charlie-kirk/site/docs/Planes/following/speaking'
out=[]
for p in sorted(glob.glob(SPK+'/*.yaml')):
    d=yaml.safe_load(open(p))
    ev=d['event']; awr=d.get('airports_within_radius') or {}
    lst=awr.get('list') or []
    g=ev['location']['geocode']
    out.append(dict(
        slug=d['page']['slug'],
        first=str(ev['dates']['first_day']), last=str(ev['dates']['last_day']),
        certainty=ev['dates'].get('certainty'),
        who=ev.get('who'), attendee_class=ev.get('attendee_class'),
        charlie_present=str(ev.get('charlie_present')), erika_present=str(ev.get('erika_present')),
        city=ev['location']['city'], state=ev['location']['state'],
        lat=g['lat'], lon=g['lon'],
        arrival_airport=(d.get('arrival_airport') or {}).get('chosen_airport',{}).get('airport_code'),
        n_airports_40=awr.get('count'), n_jet_40=awr.get('jet_capable_count'),
        n_lightjet_40=awr.get('light_jet_capable_count'),
        n_nosched_40=awr.get('no_scheduled_service_count'),
        airports=[dict(code=a['airport_code'],lat=a['lat'],lon=a['lon'],
                       jet=a.get('jet_capability'),dist=a.get('distance_mi'),
                       rw=a.get('longest_runway_ft')) for a in lst],
    ))
json.dump(out, open(sys.argv[1],'w'))
print("events",len(out))
