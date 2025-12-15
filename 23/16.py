import copy

## Part 2

class Tile:
    def __init__(self, symbol):
        self.symbol = symbol
        self.visited = set()

class Beam:
    def __init__(self, i, j, dir):
        self.i = i
        self.j = j
        self.dir = dir

def printGrid(g):
    for i in range(len(g)):
        for j in range(len(g[0])):
            print(len(g[i][j].visited), end='')
        print()

g = {}
with open("input") as f:
    rownum = 0
    for l in f:
        if rownum not in g:
            g[rownum] = {}
        for i in range(len(l.strip())):
            c = l[i]
            g[rownum][i] = Tile(c)
        rownum += 1

dirmapping = {
    "/": {
        (1,0):  (0,-1), # down then left
        (-1,0): (0,1), # up then right
        (0,1):  (-1,0), # right then up
        (0,-1): (1,0) # left then down
    },
    ".":{
        (1,0): (1,0),
        (-1,0): (-1,0),
        (0,1): (0,1),
        (0,-1): (0,-1),
    },
    "\\": {
        (1,0):  (0,1),
        (-1,0): (0,-1),
        (0,1):  (1,0),
        (0,-1): (-1,0),
    }
}

def getNewBeam(b, symbol):
    newdir = dirmapping[symbol][b.dir]
    ni, nj = b.i+newdir[0], b.j+newdir[1]
    if ni not in g:
        return None
    if nj not in g[0]:
        return None
    return Beam(ni,nj,newdir)

def energize(s, g):
    stack = [s]
    while stack:
        b = stack.pop()
        t = g[b.i][b.j]
        currvisited = t.visited
        if b.dir in currvisited:
            continue
        currvisited.add(b.dir)
        toAdd = []
        if t.symbol in dirmapping:
            newb = getNewBeam(b, t.symbol)
            toAdd.append(newb)
        elif (t.symbol == '-' and b.dir[1] != 0) or (t.symbol == "|" and b.dir[0] != 0):
            newb = getNewBeam(b, ".")
            toAdd.append(newb)
        else:
            newb = getNewBeam(b, "\\")
            toAdd.append(newb)
            newb = getNewBeam(b, "/")
            toAdd.append(newb)
        for a in toAdd:
            if a:
                stack.append(a)

    energized = 0
    for i in range(len(g)):
        for j in range(len(g[0])):
            if len(g[i][j].visited) > 0:
                energized += 1
    return energized

maxenergized = float("-inf")
for i in range(len(g)):
    dir = (0,1)
    currenergized = energize(Beam(i,0,dir), copy.deepcopy(g))
    maxenergized = max(maxenergized, currenergized)
    dir = (0,-1)
    currenergized = energize(Beam(i,len(g[0])-1,dir), copy.deepcopy(g))
    maxenergized = max(maxenergized, currenergized)

for j in range(len(g)):
    dir = (1,0)
    currenergized = energize(Beam(0,j,dir), copy.deepcopy(g))
    maxenergized = max(maxenergized, currenergized)
    dir = (-1,0)
    currenergized = energize(Beam(len(g)-1, j, dir), copy.deepcopy(g))
    maxenergized = max(maxenergized, currenergized)

print(maxenergized)
    


## Part 1

class Tile:
    def __init__(self, symbol):
        self.symbol = symbol
        self.visited = set()

class Beam:
    def __init__(self, i, j, dir):
        self.i = i
        self.j = j
        self.dir = dir

def printGrid(g):
    for i in range(len(g)):
        for j in range(len(g[0])):
            print(len(g[i][j].visited), end='')
        print()

g = {}
with open("input") as f:
    rownum = 0
    for l in f:
        if rownum not in g:
            g[rownum] = {}
        for i in range(len(l.strip())):
            c = l[i]
            g[rownum][i] = Tile(c)
        rownum += 1

# printGrid(g)

dirmapping = {
    "/": {
        (1,0):  (0,-1), # down then left
        (-1,0): (0,1), # up then right
        (0,1):  (-1,0), # right then up
        (0,-1): (1,0) # left then down
    },
    ".":{
        (1,0): (1,0),
        (-1,0): (-1,0),
        (0,1): (0,1),
        (0,-1): (0,-1),
    },
    "\\": {
        (1,0):  (0,1),
        (-1,0): (0,-1),
        (0,1):  (1,0),
        (0,-1): (-1,0),
    }
}

def getNewBeam(b, symbol):
    newdir = dirmapping[symbol][b.dir]
    ni, nj = b.i+newdir[0], b.j+newdir[1]
    if ni not in g:
        return None
    if nj not in g[0]:
        return None
    return Beam(ni,nj,newdir)

s = Beam(0,0,(0,1))
stack = [s]
while stack:
    b = stack.pop()
    t = g[b.i][b.j]
    currvisited = t.visited
    if b.dir in currvisited:
        continue
    currvisited.add(b.dir)
    toAdd = []
    if t.symbol in dirmapping:
        newb = getNewBeam(b, t.symbol)
        toAdd.append(newb)
    elif (t.symbol == '-' and b.dir[1] != 0) or (t.symbol == "|" and b.dir[0] != 0):
        newb = getNewBeam(b, ".")
        toAdd.append(newb)
    else:
        newb = getNewBeam(b, "\\")
        toAdd.append(newb)
        newb = getNewBeam(b, "/")
        toAdd.append(newb)
    for a in toAdd:
        if a:
            stack.append(a)

energized = 0
for i in range(len(g)):
    for j in range(len(g[0])):
        if len(g[i][j].visited) > 0:
            energized += 1


print(energized)