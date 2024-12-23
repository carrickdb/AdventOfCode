import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

input = aoc.getInput("input")
# input = aoc.getInput("test-input")
# input = aoc.getInput("second-example")

S = (len(input)-2, 1)
E = (1, len(input[0])-2)
currdir = (0,1)
import heapq
v = set()
h = [(0, S, currdir, [S])]
bestpaths = set()
bestscore = None
dist = {}
while h:
    x = heapq.heappop(h)
    score, curr, d, path = x
    if curr == E:
        if bestscore == None:
            bestscore = score
            bestpaths |= set(path+[curr])
        elif bestscore == score:
            bestpaths |= set(path+[curr])
    if (curr,d) in dist and dist[curr,d] < score:
        continue
    dist[curr,d] = score

    def checkNeighbor(scoreIncrease, neighbor, d, path):
        ni,nj = neighbor
        if aoc.inBounds(ni,nj,input) and input[ni][nj]!="#":
            y = (score+scoreIncrease, neighbor, d, path)
            heapq.heappush(h, y)

    checkNeighbor(1, aoc.getNext(curr, d), d, path+[curr])
    rightd = aoc.turnRight(d)
    checkNeighbor(1001, aoc.getNext(curr, rightd), rightd, path+[curr])
    leftd = aoc.turnLeft(d)
    checkNeighbor(1001, aoc.getNext(curr, leftd), leftd, path+[curr])

print(len(bestpaths))


# Part 1

S = (len(input)-2, 1)
E = (1, len(input[0])-2)
currdir = (0,1)
import heapq
v = set()
inHeap = set()
inHeap.add((0, S, currdir))
h = [(0, S, currdir)]
while True:
    x = heapq.heappop(h)
    score, curr, d = x
    if x not in inHeap:
        continue
    if curr == E:
        print(score)
        exit()
    inHeap.remove(x)
    if (curr, d) in v:
        continue
    v.add((curr, d))

    def checkNeighbor(scoreIncrease, neighbor, d):
        ni,nj = neighbor
        if aoc.inBounds(ni,nj,input) and input[ni][nj]!="#":
            y = (score+scoreIncrease, neighbor, d)
            heapq.heappush(h, y)
            inHeap.add(y)

    checkNeighbor(1, aoc.getNext(curr, d), d)
    rightd = aoc.turnRight(d)
    checkNeighbor(1001, aoc.getNext(curr, rightd), rightd)
    leftd = aoc.turnLeft(d)
    checkNeighbor(1001, aoc.getNext(curr, leftd), leftd)
