import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc
from functools import cache

# input = aoc.getInput("input")
input = aoc.getInput("test-input")

S = (len(input)-2, 1)
E = (1, len(input[0])-2)
currdir = ">"
import heapq

v = set()
inHeap = set()
inHeap.add((0, S, currdir))
h = [(0, S, currdir)]
while True:
    score, curr, d = heapq.heappop(h)
    if (curr, d) not in inHeap:
        continue
    inHeap.remove(curr)
    if curr in v:
        continue
    if curr == E:
        print(score)
        exit()
    v.add(curr)
    ci,cj = curr
    di,dj = aoc.dirmap[currdir]
    ni,nj = ci+di, cj+dj
    def checkNeighbor(scoreIncrease, i,j, d):
        if aoc.inBounds(i,j,input) and ():
            heapq.heappush(h, (score+1, (ni,nj), d))
            inHeap.add()
            character = input[ni][nj]
            if character == "#":
                continue
    checkNeighbor(1, ni,nj)






