import functools, re, collections, itertools
from itertools import chain, combinations

# Valve UX has flow rate=0; tunnels lead to valves AA, QE
r = r'Valve (\w+) .*=(\d+);.* valves? (.*)'

valves, flows, distances = set(), {}, collections.defaultdict(lambda: 10000)

matches = re.findall(r, open("input2").read())

for valve, flow, otherValves in matches:
    valves.add(valve)
    if flow != '0':
        flows[valve] = int(flow)
    for otherValve in otherValves.split(', '):
        distances[valve, otherValve] = 1

for i, j, k in itertools.product(valves, valves, valves):
    distances[i,k] = min(distances[i,k], distances[i,j]+distances[j,k])

# for nodes, distance in distances.items():
#     print(nodes, distance)

nonZeroValves = list(flows.keys())
vset = set(nonZeroValves)

@functools.lru_cache(maxsize=None)
def explore(curr, min, opened):
    if min >= 26:
        return 0
    maxTotal = float("-inf")
    unopened = vset - set(opened)
    for e in unopened:
        newTotal = explore(e, min+distances[curr,e], opened)
        maxTotal = max(newTotal, maxTotal)
    if curr in flows and curr not in opened:
        newOpened = tuple(sorted(opened + (curr,)))
        nextDistance = distances[curr,e]
        newTotal = explore(curr, min+nextDistance, newOpened)
        maxTotal = max(maxTotal, newTotal+flows[curr]*(26-min-nextDistance))
    return maxTotal

sets = chain.from_iterable(combinations(nonZeroValves, r) for r in range(len(nonZeroValves)))
maxFlow = float("-inf")
checked = set()
for s in sets:
    if s not in checked:
        me = explore("AA", 1, s)
        elephantSet = vset-set(s)
        elephant = explore("AA", 1, tuple(elephantSet))
        maxFlow = max(maxFlow, me+elephant)
        checked.add(s)
        checked.add(tuple(elephantSet))


print(maxFlow)


# import collections as c, itertools, functools, re
#
# r = r'Valve (\w+) .*=(\d*); .* valves? (.*)'
#
# V, F, D = set(), dict(), c.defaultdict(lambda: 1000)
#
# for v, f, us in re.findall(r, open('in.txt').read()):
#     V.add(v)                                  # store node
#     if f != '0': F[v] = int(f)                # store flow
#     for u in us.split(', '): D[u,v] = 1       # store dist
#
# for k, i, j in itertools.product(V, V, V):    # floyd-warshall
#     D[i,j] = min(D[i,j], D[i,k] + D[k,j])
#
# @functools.cache
# def search(t, u='AA', vs=frozenset(F), e=False):
#     return max([F[v] * (t-D[u,v]-1) + search(t-D[u,v]-1, v, vs-{v}, e)
#            for v in vs if D[u,v]<t] + [search(26, vs=vs) if e else 0])
#
# print(search(30), search(26, e=True))

# v = {}
# flows = {}
# with open("input") as f:
#     for line in f:
#         a, b = line.strip().split("; ")
#         rate = int(a.split("=")[-1])
#         name = a[len("Valve "):len("Valve ")+2]
#         if b[:len("tunnels")] == "tunnels":
#             edges = b.split("valves ")[-1].split(", ")
#         else:
#             edges = [b[-2:]]
#         v[name] = edges
#         flows[name] = rate
#
# @functools.lru_cache(maxsize=None)
# def explore(curr1, curr2, min, opened):
#     # open curr if unopened and > 0
#     # go to a different node
#     maxTotal = 0
#     edges1 = v[curr1]
#     edges2 = v[curr2]
#     if min < 25:
#         # 24: walk to a different place
#         # 25: open that valve
#         # 26: get one minute of that valve's flow
#         for e1 in edges1:
#             for e2 in edges2:
#                 newTotal = explore(e1, e2, min+1, opened)
#                 maxTotal = max(newTotal, maxTotal)
#     if flows[curr1] > 0 and curr1 not in opened:
#         if flows[curr2] > 0 and curr2 not in opened:
#             if min == 25:
#                 newTotal = flows[curr1]+flows[curr2]
#             else:
#                 newOpened = tuple(sorted(opened + (curr2,curr1)))
#                 newTotal = explore(curr1, curr2, min+1, newOpened)+(flows[curr1]+flows[curr2])*(26-min)
#             maxTotal = max(maxTotal, newTotal)
#         else:
#             if min == 25:
#                 newTotal = flows[curr1]
#             else:
#                 newOpened = tuple(sorted(opened + (curr1,)))
#                 newTotal = explore(curr1, curr2, min+1, newOpened)+flows[curr1]*(26-min)
#             maxTotal = max(maxTotal, newTotal)
#     elif flows[curr2] > 0 and curr2 not in opened:
#         if min == 25:
#             newTotal = flows[curr2]
#         else:
#             newOpened = tuple(sorted(opened + (curr2,)))
#             newTotal = explore(curr1, curr2, min+1, newOpened)
#         maxTotal = max(maxTotal, newTotal)
#     return maxTotal
#
# print(explore("AA", "AA", 1, ()))

# v = {}
# flows = {}
# with open("input") as f:
#     for line in f:
#         a, b = line.strip().split("; ")
#         rate = int(a.split("=")[-1])
#         name = a[len("Valve "):len("Valve ")+2]
#         if b[:len("tunnels")] == "tunnels":
#             edges = b.split("valves ")[-1].split(", ")
#         else:
#             edges = [b[-2:]]
#         v[name] = edges
#         flows[name] = rate
#
# @functools.lru_cache(maxsize=None)
# def explore(curr, min, opened):
#     if min == 30:
#         return 0
#     # open curr if unopened and > 0
#     # go to a different node
#     maxTotal = float("-inf")
#     edges = v[curr]
#     for e in edges:
#         newTotal = explore(e,  min+1, opened)
#         maxTotal = max(newTotal, maxTotal)
#     if flows[curr] > 0 and curr not in opened:
#         newOpened = tuple(sorted(opened + (curr,)))
#         newTotal = explore(curr, min+1, newOpened)
#         maxTotal = max(maxTotal, newTotal+flows[curr]*(30-min))
#     return maxTotal
#
# print(explore("AA", 1, ()))

# rev = {}
# for name, n in v.items():
#     for edge in n.edges:
#         if edge not in rev:
#             rev[edge] = Node(v[edge].flow, [])
#         rev[edge].edges.append(name)
#
# # for name, node in rev.items():
# #     print(name, node.flow, ":", node.edges)
#
# dp = [{} for i in range(30)]
# dp[0]["AA"] = {}
# dp[0]["AA"][()] = [0, 0] # dp[min][node][opened] = [flowTotal, fps]
#
# """
# dp[i][node][opened] = max(dp[i-1][node][opened]+node.flow, dp[i-1][prev][opened1], dp[i-1][prev][opened2],...)
# """
#
# print("------------------------------------------------------------------")
# for i in range(1, 30):
#     print("*****", i+1, "*****")
#     for name, n in rev.items():
#         for parent in n.edges:
#             if parent in dp[i-1]:
#                 for openValves, totals in dp[i-1][parent].items():
#                     total, fps = totals
#                     dp[i][name] = {openValves : [total + fps, fps]}
#         if name in dp[i-1] and n.flow > 0:
#             for openValves, totals in dp[i-1][name].items():
#                 total, fps = totals
#                 newValves = set(openValves)
#                 newValves.add(name)
#                 newValvesT = tuple(newValves)
#                 if name in dp[i] and newValvesT in dp[i][name]:
#                     if dp[i][name][newValvesT][0] < total+fps:
#                         dp[i][name][newValvesT] = [total+fps, fps+n.flow]
#                 else:
#                     dp[i][name] = {}
#                     dp[i][name][newValvesT] = [total+fps, fps+n.flow]
#     print(dp[i])
#     if i > 6:
#         exit()
# print(dp[-1].items())
