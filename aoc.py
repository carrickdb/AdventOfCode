from typing import List

dirs = [[0,1], [0,-1], [-1, 0], [1,0]]
diagDirs = [[0,1], [0,-1], [-1, 0], [1,0], [-1, -1], [1, 1], [-1, 1], [1, -1]]

def getInput(filename):
    input = []
    with open(filename) as f:
        for l in f:
            input.append(l.strip())
    return input

def printMapGrid(g):
    for i in sorted(g.keys()):
        for j in sorted(g[i].keys()):
            print(g[i][j], end=" ")
        print()

def printGridList(g):
    for row in g:
        print(''.join(row))
    print()

def gridify(input):
    g = {}
    for i in range(len(input)):
        row = input[i]
        for j in range(len(row)):
            if i not in g:
                g[i] = {}
            g[i][j] = row[j]
    return g

def getNextSteps(i,j,g):
    ns = []
    for di,dj in dirs:
        ni,nj = i+di, j+dj
        if ni in g and nj in g[ni]:
            ns.append((ni,nj))
    return ns

def printGraph(g):
    for k,v in g.items():
        print(f"{k}: {v}")

def turnRight(c):
    return c[1], -c[0]

def turnLeft(c):
    return -c[1], c[0]

def transpose(arr):
    newArr = []
    for j in range(len(arr[0])):
        newRow = []
        for i in range(len(arr)):
            newRow.append(arr[i][j])
        newArr.append(''.join(newRow))
    return newArr

def inBounds(c,g):
    i,j = c
    return i>=0 and i<len(g) and j>=0 and j<len(g[0])

def nextStep(i,j,g):
    for di,dj in dirs:
        ni,nj = di+i,dj+j
        if inBounds(ni,nj,g):
            yield ni,nj

def getNext(c, d):
    return c[0]+d[0], c[1]+d[1]

def mapint(l: List[str]):
    return list(map(int, l))

def mapstr(l: List[int]):
    return list(map(str, l))

dirmap = {
    "^": [-1,0],
    ">": [0,1],
    "<": [0,-1],
    "v": [1,0]
}

def iterateThroughGraph(g):
    for i in range(len(g)):
        for j in range(len(g[0])):
            yield i,j

def numRows(g):
    return range(len(g))

def numCols(g):
    return range(len(g[0]))

def getByTwos(l):
    for i in range(0,len(l),2):
        return l[i],l[i+1]