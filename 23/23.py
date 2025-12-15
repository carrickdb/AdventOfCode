import aoc
from collections import deque

input = aoc.getInput("input")
g = aoc.gridify(input)

mapping = {
    "^": (-1,0),
    "v": (1,0),
    "<": (0,-1),
    ">": (0, 1)
}

def isend(ci,cj):
    return ci==len(g)-1 and cj == len(g[0])-2

def backwards(ij):
    i,j = ij
    if i==0:
        return 0,j*-1
    return (i*-1,0)

class Path:
    def __init__(self, start, parent, dir):
        self.start = start
        self.parent = parent
        self.dir = dir

graph = {}
v = set()
q = deque([Path((0,1), (0,1), (1,0))])
while q:
    for _ in range(len(q)):
        curr = q.popleft()
        pathstart = curr.start
        pathstarti, pathstartj = pathstart
        p = curr.parent
        if (pathstart, p) in v:
            continue
        v.add((pathstart, p))
        s = 1
        dir = curr.dir
        pathi,pathj = pathstarti, pathstartj
        while True:
            nextsteps = []
            for di,dj in aoc.dirs:
                newdirs = (di,dj)
                if newdirs == backwards(dir):
                    continue
                n = pathi+di, pathj+dj
                ni,nj = n
                if ni not in g or nj not in g[ni]:
                    continue
                if g[ni][nj] == "#":
                    continue
                nextsteps.append((n, newdirs))
            if len(nextsteps) == 0:
                break
            if len(nextsteps) == 1:
                nextstep, nextdir = nextsteps[0]
                ni,nj = nextstep
                if ni == len(g)-1 and nj == len(g[0])-2:
                    # found the end
                    if p not in graph:
                        graph[p] = set()
                    graph[p].add((nextstep, s))
                    break
                dir = nextdir
                pathi,pathj = nextstep
                s += 1
                continue
            # found a node
            newnode = (pathi, pathj)
            if (newnode, p) in v:
                break
            if p not in graph:
                graph[p] = set()
            graph[p].add((newnode,s))
            for nextstep, nextdir in nextsteps:
                q.append(Path(nextstep, newnode, nextdir))
            break

# for k, v in graph.items():
#     print(f"{k}: {v}")

stack = [(0,1,0,set())]
longest = float("-inf")
while stack:
    ci, cj, pathlen, v = stack.pop()
    curr = (ci,cj)
    if isend(ci,cj):
        longest = max(longest, pathlen)
        continue
    if curr in v:
        continue
    v.add(curr)
    if curr not in graph:
        continue
    edges = graph[curr]
    for e, w in list(edges):
        if e in v:
            continue
        ei, ej = e
        stack.append((ei,ej,pathlen+w,v.copy()))

print(longest)

# 5,3

# import aoc

# input = aoc.getInput("input")
# g = aoc.gridify(input)

# mapping = {
#     "^": (-1,0),
#     "v": (1,0),
#     "<": (0,-1),
#     ">": (0, 1)
# }

# stack = [(0,1,0,set())]
# longest = float("-inf")
# while stack:
#     ci,cj,steps, v = stack.pop()
#     if ci==len(g)-1 and cj == len(g[0])-2:
#         longest = max(longest, steps)
#         continue
#     if (ci,cj) in v:
#         continue
#     v.add((ci,cj))
#     if g[ci][cj] in mapping:
#         di,dj = mapping[g[ci][cj]]
#         ni,nj = ci+di, cj+dj
#         if (ni,nj) in v:
#             continue
#         stack.append((ci+di,cj+dj,steps+1,v))
#     toappend = []
#     for di, dj in aoc.dirs:
#         ni,nj = ci+di, cj+dj
#         if ni in g and nj in g[nj]:
#             n = g[ni][nj]
#             if n == "#":
#                 continue
#             if (ni,nj) in v:
#                 continue
#             # stack.append((ni,nj,steps+1, v.copy()))
#             toappend.append((ni,nj))
#     if len(toappend) == 1:
#         ni,nj = toappend[0]
#         stack.append((ni,nj,steps+1,v))
#     else:
#         for curr in toappend:
#             ni,nj = curr
#             stack.append((ni,nj,steps+1, v.copy()))

# print(longest)