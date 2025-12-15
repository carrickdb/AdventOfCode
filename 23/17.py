import heapq
from collections import deque

g = {}
with open("input") as f:
    rownum = 0
    for l in f:
        l = l.strip()
        if rownum not in g:
            g[rownum] = {}
        for j in range(len(l)):
            g[rownum][j] = int(l[j])
        rownum += 1

class Crucible:
    def __init__(self, i,j, dir, numsteps, parent):
        self.i = i
        self.j = j
        self.dir = dir
        self.numsteps = numsteps
        self.parent = parent

dirmapping = {
    "r": {
        (1,0):  (0,-1),
        (-1,0): (0,1),
        (0,1):  (1,0),
        (0,-1): (-1,0)
    },
    "l": {
        (1,0):  (0,1),
        (-1,0): (0,-1),
        (0,1):  (-1,0),
        (0,-1): (1,0),
    }
}

h = []
heapq.heappush(h, 0)
heapq.heappush(h, 0)
visited = set()
lowestheat = float("inf")
lowest = None
numsteps = 0
crucibles = {0: deque([Crucible(0,0,(0,1), numsteps, None), Crucible(0,0,(1,0), numsteps, None)])}
"""
Once an ultra crucible starts moving in a direction, it needs to move a minimum of four blocks in that direction before it can turn (or even before it can stop at the end). However, it will eventually start to get wobbly: an ultra crucible can move a maximum of ten consecutive blocks without turning.
"""
parents = {}
turnsteps = 2
straightsteps = 9
while h:
    heat = heapq.heappop(h)
    c = crucibles[heat].popleft()
    # print("c.numsteps", c.numsteps)
    ci, cj = c.i, c.j
    # print("popped", ci, cj, c.dir)
    t = (c.i, c.j, c.dir, c.numsteps)
    if t in visited:
        continue
    visited.add(t)
    if (ci,cj) not in parents:
        parents[(ci, cj)] = []
    parents[(ci,cj)].append(c)
    if c.i == len(g)-1 and c.j == len(g[0])-1 and c.numsteps > turnsteps+1:
        lowestheat = min(lowestheat, heat)
        lowest = c
        break
    ni, nj = c.i+c.dir[0], c.j+c.dir[1]
    if ni in g and nj in g[ni]:
        cparent = (c.i, c.j)
        newc = []
        if c.numsteps > turnsteps:
            newc.extend([Crucible(ni, nj, dirmapping["r"][c.dir], 0, cparent), Crucible(ni, nj, dirmapping["l"][c.dir], 0, cparent)])
            # print("turning")
        if c.numsteps < straightsteps:
            newc.append(Crucible(ni, nj, c.dir, c.numsteps+1, cparent))
            # print("walking straight")
        newheat = g[ni][nj]+heat
        for nc in newc:
            if newheat not in crucibles:
                crucibles[newheat] = deque()
            heapq.heappush(h, newheat)
            crucibles[newheat].append(nc)

symbols = {
    (0,1) : ">",
    (0,-1): "<",
    (1,0): "v",
    (-1,0): "^"
}

def printgrid(g, c):
    while True:
        g[c.i][c.j] = symbols[c.dir]
        if not c.parent:
            break
        if len(parents[c.parent]) > 1:
            print(len(parents[c.parent]))
        c = parents[c.parent][0]
    for i in range(len(g)):
        print(''.join([str(g[i][j]) for j in range(len(g[0]))]))
    print()

print(lowestheat)
# printgrid(g, lowest)

# too high: 1390