# import collections as c, itertools, functools, re
#
# r = r'Valve (\w+) .*=(\d*); .* valves? (.*)'
#
# V, F, D = set(), dict(), c.defaultdict(lambda: 1000)
#
# for v, f, us in re.findall(r, open('input2').read()):
#     V.add(v)                                  # store node
#     if f != '0': F[v] = int(f)                # store flow
#     for u in us.split(', '): D[u,v] = 1       # store dist
#
# for k, i, j in itertools.product(V, V, V):    # floyd-warshall
#     D[i,j] = min(D[i,j], D[i,k] + D[k,j])

# for nodes, distance in D.items():
#     print(nodes, distance)
#
# @functools.cache
# def search(t, u='AA', vs=frozenset(F), e=False):
#     return max([F[v] * (t-D[u,v]-1) + search(t-D[u,v]-1, v, vs-{v}, e)
#            for v in vs if D[u,v]<t] + [search(26, vs=vs) if e else 0])
#
# print(search(30), search(26, e=True))

import functools, re, collections, itertools
from itertools import chain, combinations

# Valve UX has flow rate=0; tunnels lead to valves AA, QE
r = r'Valve (\w+) .*=(\d+);.* valves? (.*)'

valves, flows, distances = set(), {}, collections.defaultdict(lambda: 1000)

matches = re.findall(r, open("input2").read())

for valve, flow, otherValves in matches:
    valves.add(valve)
    if flow != '0':
        flows[valve] = int(flow)
    for otherValve in otherValves.split(', '):
        distances[valve, otherValve] = 1

for i, j, k in itertools.product(valves, valves, valves):
    distances[j,k] = min(distances[j,k], distances[j,i]+distances[i,k])

minutes = 30

nonZeroValves = list(flows.keys())
vset = set(nonZeroValves)

@functools.lru_cache(maxsize=None)
def explore(curr, min, opened):
    if min >= minutes:
        return 0
    maxTotal = float("-inf")
    unopened = vset - set(opened)
    if curr in flows and curr not in opened:
        newOpened = tuple(sorted(opened + (curr,)))
        nextDistance = distances[curr,e]
        newTotal = explore(curr, min+nextDistance, newOpened)
        maxTotal = max(maxTotal, newTotal+flows[curr]*(minutes-min-nextDistance))
    return maxTotal

print(explore("AA", 1, ()))
