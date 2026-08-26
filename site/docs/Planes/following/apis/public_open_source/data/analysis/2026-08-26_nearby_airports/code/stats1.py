import json,collections,statistics,math
SCR='.'
ev=json.load(open('events.json'))
g=[e for e in ev if e['lat'] is not None]
print("=== Q1: what 40 miles actually covers ===")
c=[e['n_airports_40'] for e in g]; j=[e['n_jet_40'] for e in g]; lj=[e['n_lightjet_40'] for e in g]
def d(x,n):
    x=sorted(x); print(f"{n}: n={len(x)} min={x[0]} p10={x[int(.1*len(x))]} med={statistics.median(x)} mean={statistics.mean(x):.1f} p90={x[int(.9*len(x))]} max={x[-1]} total={sum(x)}")
d(c,"airports_within_40mi"); d(j,"jet_capable_40mi"); d(lj,"light_jet_capable_40mi")
print("events with 0 jet-capable field in 40mi:",sum(1 for x in j if x==0))
print("events with 1 jet-capable field in 40mi:",sum(1 for x in j if x==1))
print("events with >=5 jet-capable:",sum(1 for x in j if x>=5))
for r in (40,75,100,150): print(f"  area of r={r}mi disc = {math.pi*r*r:,.0f} sq mi")
# how far to the 2nd/3rd jet field
print("\n=== distance to Nth jet-capable field within 40mi ===")
n2=[]
for e in g:
    js=sorted([a['dist'] for a in e['airports'] if a['jet']=='jet_capable'])
    n2.append((e['slug'],js[:4]))
import collections
k=collections.Counter(len(x[1]) for x in n2); print("count of jet fields:",dict(sorted(k.items())))
