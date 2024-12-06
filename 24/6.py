import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

input = aoc.getInput("input")
# input = aoc.getInput("test-input")


# Part 2

g = aoc.gridify(input)

gi,gj = None, None
for i in g:
    for j in g[i]:
        if g[i][j] == "^":
            gi,gj = i,j
            break
        if gi:
            break

dirs = {
    "up": [-1,0],
    "down": [1,0],
    "left": [0,-1],
    "right": [0,1]
}
dirChange = {
    "up": "right",
    "right": "down",
    "down": "left",
    "left": "up",
}
dir = "up"
obs = 0

origgi, origgj = gi,gj
print("start:", origgi, origgj) # 6,4
origDir = dir
for i in g:
    for j in g[i]:
        if g[i][j] == "#" or (i == origgi and j==origgj):
            continue
        g[i][j] = "#"
        gi,gj = origgi, origgj
        dir = origDir
        ri,rj = gi,gj
        rdir = "up"
        done = set()
        while True:
            g[gi][gj] = "X"
            if (gi,gj,dir) in done:
                print("cycle detected", i,j)
                obs += 1
                break
            done.add((gi,gj,dir))
            ci,cj = dirs[dir]
            ni,nj = ci+gi, gj+cj
            if not aoc.inBounds(ni,nj,g):
                break
            if g[ni][nj] == "#":
                dir = dirChange[dir]
            else:
                gi,gj = ni,nj
        g[i][j] = "."
print(obs)


# Part 1
g = aoc.gridify(input)

gi,gj = None, None
for i in g:
    for j in g[i]:
        if g[i][j] == "^":
            gi,gj = i,j
            break
        if gi:
            break

dirs = {
    "up": [-1,0],
    "down": [1,0],
    "left": [0,-1],
    "right": [0,1]
}
dirChange = {
    "up": "right",
    "right": "down",
    "down": "left",
    "left": "up",
}
dir = "up"
while True:
    g[gi][gj] = "X"
    ci,cj = dirs[dir]
    ni,nj = ci+gi, gj+cj
    if not aoc.inBounds(ni,nj,g):
        break
    if g[ni][nj] == "#":
        dir = dirChange[dir]
    else:
        gi,gj = ni,nj

total = 0
aoc.printMapGrid(g)
for i in g:
    for j in g[i]:
        if g[i][j]=='X':
            total += 1
print(total)