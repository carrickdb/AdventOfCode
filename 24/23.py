import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc
from collections import defaultdict

stuff = aoc.getInput(os.getenv("HOME") + "/Desktop/input")
# stuff = aoc.getInput("test-input")

g = defaultdict(set)
for line in stuff:
    u,v = line.split("-")
    g[u].add(v)
    g[v].add(u)

from functools import cache
@cache
def getClique(node, currClique):
    edges = g[node]
    for edge in edges:
        if edge in currClique:
            continue
        inClique = True
        for friend in currClique:
            if friend not in g[edge]:
                inClique = False
                break
        if inClique:
            currClique = currClique + (edge,)
            currClique = getClique(edge, currClique)
    return currClique

friends = []
for n in g:
    currFriends = getClique(n, (n,))
    if len(currFriends) > len(friends):
        friends = currFriends

password = sorted(friends)
print(','.join(password))


# components = 0
# v = set()
# for n, e in g.items():
#     if n in v:
#         continue
#     components += 1
#     stack = [n]
#     size = 0
#     while stack:
#         curr = stack.pop()
#         if curr in v:
#             continue
#         size += 1
#         v.add(curr)
#         for edge in g[curr]:
#             if edge in v:
#                 continue
#             stack.append(edge)
#     print(size)

# print(components)

## Part 1
# g = defaultdict(list)
# for line in stuff:
#     u,v = line.split("-")
#     g[u].append(v)
#     g[v].append(u)

# cliques = set()
# for node in g:
#     if node[0] == "t":
#         for secondNode in g[node]:
#             for thirdNode in g[secondNode]:
#                 if node in g[thirdNode]:
#                     cliques.add(tuple(sorted([node,secondNode,thirdNode])))


# print(len(cliques))