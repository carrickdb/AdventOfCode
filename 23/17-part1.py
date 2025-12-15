import heapq

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
    def __init__(self, i,j, dir, stepsleft, parent):
        self.i = i
        self.j = j
        self.dir = dir
        self.stepsleft = stepsleft
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
visited = {}
lowestheat = float("inf")
lowest = None
initsteps = 2
crucibles = {0:[Crucible(0,0,(0,1), initsteps, None), Crucible(0,0,(1,0), initsteps, None)]}
while h:
    heat = heapq.heappop(h)
    c = crucibles[heat].pop()
    t = (c.i, c.j, c.dir, c.stepsleft)
    if t in visited:
        continue
    visited[t]
    if c.i == len(g)-1 and c.j == len(g[0])-1:
        lowestheat = min(lowestheat, heat)
        lowest = c
        continue
    ni, nj = c.i+c.dir[0], c.j+c.dir[1]
    if ni < len(g) and ni >= 0 and nj < len(g[0]) and nj >=0:
        cparent = (c.i, c.j)
        newc = [Crucible(ni, nj, dirmapping["r"][c.dir], initsteps, cparent), Crucible(ni, nj, dirmapping["l"][c.dir], initsteps, cparent)]
        if c.stepsleft > 0:
            newc.append(Crucible(ni, nj, c.dir, c.stepsleft-1, cparent))
        newheat = g[ni][nj]+heat
        for nc in newc:
            if newheat not in crucibles:
                crucibles[newheat] = []
            heapq.heappush(h, newheat)
            crucibles[newheat].append(nc)

# symbols = {
#     (0,1) : ">",
#     (0,-1): "<",
#     (1,0): "^",
#     (-1,0): "v"
# }

# def printgrid(g, c):
#     while c:
#         g[c.i][c.j] = symbols[c.dir]
#         c = crucibles[c.parent]
#     for i in range(len(g)):
#         print(''.join([g[i][j] for j in range(len(g[0]))]))
#     print()

print(lowestheat)
# printgrid(g, lowest)