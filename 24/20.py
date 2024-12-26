import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc
inputFilename = os.getenv("HOME") + "/Desktop/input"
# inputFilename = "test-input"

with open(inputFilename) as f:
    stuff = f.read()
    tracklen = stuff.count(".")+2

g = list(map(list, stuff.split()))

for i,j in aoc.iterateThroughGraph(g):
    curr = g[i][j]
    if curr == "S":
        s = (i,j)
    if curr == "E":
        e = (i,j)
c = s
step = 0
path = [c]
# number the path
while c != e:
    ci,cj = c
    g[ci][cj] = step
    for n in aoc.nextStepInBounds(c,g):
        val = aoc.getGVal(n,g)
        if val != "." and val != "E":
            continue
        c = n
        break
    step += 1
    path.append(c)

# print(step, tracklen)
ci,cj = c
g[ci][cj] = step

from collections import defaultdict

cheatResults = defaultdict(set)

def checkCheat(n, prev, steps):
    cheatVal = aoc.getGVal(n,g)
    if type(cheatVal) == int:
        cheatRes = cheatVal-aoc.getGVal(prev,g)-steps
        if cheatRes > 49:
            cheatResults[cheatRes].add((n,prev))

cheatIndex = 0
numSteps = 20
while cheatIndex<tracklen:
    cheat = path[cheatIndex]
    ci,cj = cheat
    for i in range(numSteps+1):
        for j in range(numSteps-i+1):
            for di,dj in [(1,1), (-1,1), (1,-1), (-1,-1)]:
                cheatEnd = (ci+i*di, cj+j*dj)
                if aoc.inBounds(cheatEnd, g):
                    checkCheat(cheatEnd, cheat, i+j)
    cheatIndex += 1

total = 0
for timeSaved, cheats in sorted(cheatResults.items()):
    print(f"{len(cheats)} cheats save {timeSaved} picoseconds")
    if timeSaved >= 100:
        total += len(cheats)

print(total)


# Part 1
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc
inputFilename = os.getenv("HOME") + "/Desktop/input"
# inputFilename = "test-input"

with open(inputFilename) as f:
    stuff = f.read()
    tracklen = stuff.count(".")+2

g = list(map(list, stuff.split()))

for i,j in aoc.iterateThroughGraph(g):
    curr = g[i][j]
    if curr == "S":
        s = (i,j)
    if curr == "E":
        e = (i,j)

c = s
step = 0
path = [c]
# number the path
while c != e:
    ci,cj = c
    g[ci][cj] = step
    for n in aoc.nextStepInBounds(c,g):
        val = aoc.getGVal(n,g)
        if val != "." and val != "E":
            continue
        c = n
        break
    step += 1
    path.append(c)

# print(step, tracklen)
ci,cj = c
g[ci][cj] = step

# for i in range(len(g)):
#     for j in range(len(g[0])):
#         curr = g[i][j]
#         if type(curr) == int:
#             print("O", end="")
#         else:
#             print(curr, end="")
#     print()

from collections import defaultdict

cheatResults = defaultdict(set)

def checkCheat(n, prev):
    cheatVal = aoc.getGVal(n,g)
    if type(cheatVal) == int:
        cheatRes = cheatVal-aoc.getGVal(prev,g)-2
        if cheatRes > 1:
            cheatResults[cheatRes].add((n,cheat))

cheatIndex = 0
while cheatIndex<tracklen:
    cheat = path[cheatIndex]
    for n in aoc.nextStepInBounds(cheat,g):
        if aoc.getGVal(n,g) == "#":
            for m in aoc.nextStepInBounds(n,g):
                if m != n:
                    checkCheat(m, cheat)
    cheatIndex += 1

total = 0
for timeSaved, cheats in sorted(cheatResults.items()):
    # print(f"{len(cheats)} cheats save {timeSaved} picoseconds")
    if timeSaved >= 100:
        total += len(cheats)

print(total)