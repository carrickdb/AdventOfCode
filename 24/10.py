import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

input = aoc.getInput("input")
# input = aoc.getInput("test-input-larger")

## Part 2

g = []
for row in input:
    g.append(list(map(int, row)))


def rec(i,j, v):
    if (i,j) in v:
        return 0
    if g[i][j] == 9:
        return 1
    vc = v.copy()
    vc.add((i,j))
    curr = g[i][j]
    currTotal = 0
    for di,dj in aoc.dirs:
        ni,nj = di+i,dj+j
        if aoc.inBounds(ni,nj,g):
            if g[ni][nj] == curr+1:
                currTotal += rec(ni,nj,vc)
    return currTotal

total = 0
for i in range(len(g)):
    for j in range(len(g[0])):
        if g[i][j] == 0:
            total += rec(i,j, set())

print(total)



## Part 1
# g = []
# for row in input:
#     g.append(list(map(int, row)))

# total = 0
# for i in range(len(g)):
#     for j in range(len(g[0])):
#         if g[i][j] == 0:
#             s = [(i,j)]
#             v = set()
#             while s:
#                 ci,cj = s.pop()
#                 if (ci,cj) in v:
#                     continue
#                 v.add((ci,cj))
#                 curr = g[ci][cj]
#                 if curr == 9:
#                     # print(ci,cj, "is 9")
#                     total += 1
#                     continue
#                 for di,dj in aoc.dirs: # TODO: add
#                     ni,nj = di+ci,dj+cj
#                     if aoc.inBounds(ni,nj,g):
#                         if g[ni][nj] == curr+1:
#                             s.append((ni,nj))

# print(total)
