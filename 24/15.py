import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc
import re

# with open("test-input-15") as f:
# with open("test-larger-15") as f:
# with open("test-input-part2-15") as f:
with open("input-15") as f:
    input = f.read()

m, directions = input.split("\n\n")

g = []
m = m.split()

for line in m:
    newline = []
    for c in line:
        if c == "@":
            newline.extend(["@", "."])
        elif c == "O":
            newline.extend(["[", "]"])
        else:
            newline.extend([c]*2)
    g.append(newline)
# aoc.printGridList(g)

for i in range(len(g)):
    for j in range(len(g[0])):
        curr = g[i][j]
        if curr == "@":
            si,sj = i,j

dirmap = {
    "^": [-1,0],
    ">": [0,1],
    "<": [0,-1],
    "v": [1,0]
}
from collections import deque
ci,cj = si,sj
for row in directions:
    for d in row.strip():
        di,dj = dirmap[d]
        # print(ci,cj, d)
        boxes = set()
        q = deque([(ci,cj)])
        wall = False
        while q:
            lq = len(q)
            # print(q)
            for _ in range(lq):
                i,j = q.popleft()
                curr = g[i][j]
                # print(i,j,curr)
                if curr == "#":
                    wall = True
                    break
                if curr == "." or (i,j, curr) in boxes:
                    continue
                boxes.add((i,j,curr))
                childi,childj = i+di, j+dj
                child = g[childi][childj]
                # print(f"{child=}")
                q.append((childi, childj))
                if d == "^" or d == "v":
                    if g[childi][childj] == "]":
                        q.append((childi,childj-1))
                    elif g[childi][childj] == "[":
                        q.append((childi,childj+1))
            if wall:
                break
        if wall:
            continue
        g[ci][cj] = "."
        for bi,bj,_ in boxes:
            g[bi][bj] = "."
        for bi,bj,c in boxes:
            g[bi+di][bj+dj] = c
        ni,nj = ci+di, cj+dj
        g[ni][nj] = "@"
        ci,cj = ni,nj
        # aoc.printGridList(g)
        # print()
total = 0
for i in range(len(g)):  # TODO
    j = 0
    while j < len(g[0]):
        curr = g[i][j]
        if curr == "[":
            # closestv = min(len(g)-i-1, i)
            # closesth = min(j, len(g[0])-j-2)
            # total += closestv*100+closesth
            total += i*100+j
            j += 1
        j += 1
print(total)




# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# import aoc
# import re

# # input = aoc.getInput("input")
# # with open("test-input") as f:
# # with open("test-larger") as f:
# with open("input") as f:
#     input = f.read()

# m, directions = input.split("\n\n")

# g = []
# m = m.split()

# for line in m:
#     g.append(list(line))
# # aoc.printGridList(g)

# for i in range(len(g)):
#     for j in range(len(g[0])):
#         curr = g[i][j]
#         if curr == "@":
#             si,sj = i,j

# dirmap = {  # TODO
#     "^": [-1,0],
#     ">": [0,1],
#     "<": [0,-1],
#     "v": [1,0]
# }

# ci,cj = si,sj
# for row in directions:
#     for d in row.strip():
#         di,dj = dirmap[d]
#         ni,nj = ci+di,cj+dj
#         ei,ej = ni,nj
#         boxes = 0
#         while g[ei][ej] == "O":
#             ei,ej = di+ei, ej+dj
#             boxes += 1
#         if g[ei][ej] == "#":
#             continue
#         g[ci][cj] = "."
#         g[ni][nj] = "@"
#         ei,ej = ni,nj
#         for _ in range(boxes):
#             ei,ej = di+ei, dj+ej
#             g[ei][ej] = "O"
#         ci,cj = ni,nj
#         # aoc.printGridList(g)

# total = 0
# for i in range(len(g)):  # TODO
#     for j in range(len(g[0])):
#         if g[i][j] == "O":
#             total += i*100+j
# print(total)

