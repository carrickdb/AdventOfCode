import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

input = aoc.getInput(os.getenv("HOME") + "/input")
# input = aoc.getInput("test-input")
# input = aoc.getInput("second-example")

S = (len(input)-2, 1)
E = (1, len(input[0])-2)
currdir = (0,1)
import heapq, math
prev = {}
dist = {}
v = set()
bestscore = math.inf
h = [(0, S, currdir)]
while h:
    score, coords, d = heapq.heappop(h)
    node = (coords, d)
    if coords == E:
        bestscore = min(bestscore, score)
    if node in v:
        continue
    v.add(node)
    for direction, scoreincrease in [(d,1), (aoc.turnLeft(d), 1001), (aoc.turnRight(d), 1001)]:
        n = aoc.getNext(coords, direction)
        if aoc.inBounds(n,input) and input[n[0]][n[1]] != "#":
            newNode = (n, direction)
            newScore = score+scoreincrease
            heapq.heappush(h, (newScore, n, direction))
            if n==E and newNode in dist:
                print(f"{dist[newNode]==newScore=}")
            if newNode not in dist or dist[newNode] > newScore:
                prev[newNode] = set([node])
                dist[newNode] = newScore
            elif dist[newNode]==newScore:
                prev[newNode].add(node)

ends = [node for node in prev if node[0]==E and dist[node]==bestscore]

bestpaths = set()

def getpath(curr):
    while True:
        bestpaths.add(curr[0])
        if curr not in prev:
            return # found the start
        parents = list(prev[curr])
        if len(parents) == 1:
            curr = parents[0]
        else:
            break
    for parent in parents:
        getpath(parent)


for end in ends:
    getpath(end)

print(len(bestpaths))



# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# import aoc

# input = aoc.getInput("input")
# # input = aoc.getInput("test-input")
# # input = aoc.getInput("second-example")

# S = (len(input)-2, 1)
# E = (1, len(input[0])-2)
# currdir = (0,1)
# import heapq
# v = set()
# h = [(0, S, currdir, [S])]
# bestpaths = set()
# bestscore = None
# dist = {}
# while h:
#     x = heapq.heappop(h)
#     score, curr, d, path = x
#     if curr == E:
#         if bestscore == None:
#             bestscore = score
#             bestpaths |= set(path+[curr])
#         elif bestscore == score:
#             bestpaths |= set(path+[curr])
#         print(score)
#     if (curr,d) in dist and dist[curr,d] < score:
#         continue
#     dist[curr,d] = score

#     def checkNeighbor(scoreIncrease, neighbor, d, path):
#         ni,nj = neighbor
#         if aoc.inBounds(ni,nj,input) and input[ni][nj]!="#":
#             y = (score+scoreIncrease, neighbor, d, path)
#             heapq.heappush(h, y)

#     checkNeighbor(1, aoc.getNext(curr, d), d, path+[curr])
#     rightd = aoc.turnRight(d)
#     checkNeighbor(1001, aoc.getNext(curr, rightd), rightd, path+[curr])
#     leftd = aoc.turnLeft(d)
#     checkNeighbor(1001, aoc.getNext(curr, leftd), leftd, path+[curr])

# print(len(bestpaths))

# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# import aoc

# # input = aoc.getInput("input")
# # input = aoc.getInput("test-input")
# # input = aoc.getInput("second-example")

# S = (len(input)-2, 1)
# E = (1, len(input[0])-2)
# startdir = (0,1)
# import heapq
# v = set()
# inHeap = set()
# inHeap.add((0, S, startdir))
# h = [(0, S, startdir)]
# bestscore = None
# prev = {}
# while h:
#     x = heapq.heappop(h)
#     score, curr, d = x
#     if x not in inHeap:
#         continue
#     if curr == E and bestscore == None:
#         bestscore = score
#     inHeap.remove(x)
#     if (curr, d) in v:
#         continue
#     v.add((curr, d))

#     def checkNeighbor(scoreIncrease, neighbor, d):
#         ni,nj = neighbor
#         if aoc.inBounds(ni,nj,input) and input[ni][nj]!="#":
#             y = (score+scoreIncrease, neighbor, d)
#             heapq.heappush(h, y)
#             inHeap.add(y)

#     checkNeighbor(1, aoc.getNext(curr, d), d)
#     rightd = aoc.turnRight(d)
#     checkNeighbor(1001, aoc.getNext(curr, rightd), rightd)
#     leftd = aoc.turnLeft(d)
#     checkNeighbor(1001, aoc.getNext(curr, leftd), leftd)

# bestpaths = set()

# def findpath(coord, d, v, score):
#     v.add(coord)
#     if coord==E:
#         # print(f"{score=}")
#         if score == bestscore:
#             global bestpaths
#             bestpaths |=v
#         return
#     nextcoord = aoc.getNext(coord, d)
#     def validspace(nextcoord):
#         ni,nj = nextcoord
#         return aoc.inBounds(ni,nj,input) and input[ni][nj]!="#" and nextcoord not in v
#     if validspace(nextcoord):
#         findpath(nextcoord, d, v.copy(), score+1)
#     rightd = aoc.turnRight(d)
#     nextcoord = aoc.getNext(coord, rightd)
#     if validspace(nextcoord):
#         findpath(nextcoord, rightd, v.copy(), score+1001)
#     leftd = aoc.turnLeft(d)
#     nextcoord = aoc.getNext(coord, leftd)
#     if validspace(nextcoord):
#         findpath(nextcoord, leftd, v.copy(), score+1001)

# findpath(S, startdir, set(), 0)


# for i in range(len(input)):
#     for j in range(len(input[0])):
#         if (i,j) in bestpaths:
#             print("O", end='')
#         else:
#             print(input[i][j], end='')
#     print()

# print(len(bestpaths))


# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# import aoc

# # g = aoc.getInput("input")
# g = aoc.getInput("test-input")
# # g = aoc.getInput("second-example")
# # g = aoc.getInput("mini")

# S = (len(g)-2, 1)
# E = (1, len(g[0])-2)
# print(f"{S=}")
# print(f"{E=}")
# currdir = (0,1)
# import heapq
# dist = {}
# prev = {}
# h = [(0, S, currdir)]
# bestscore = None
# while h:
#     x = heapq.heappop(h)
#     score, curr, d = x
#     if curr == E and bestscore == None:
#         bestscore = score
#     currNode = (curr, d)
#     if currNode in dist and score > dist[currNode]:
#         continue

#     def checkNeighbor(scoreIncrease, neighbor, d, parent):
#         ni,nj = neighbor
#         currScore = score+scoreIncrease
#         if aoc.inBounds(ni,nj,g) and g[ni][nj]!="#":
#             y = (currScore, neighbor, d)
#             heapq.heappush(h, y)
#             join = (1,2)
#             if neighbor == join:
#                 print("parent of join", parent, currScore)
#                 if join in prev:
#                     print(f"initial prev: {prev[join]=}, {dist[join]}")
#             if neighbor not in dist or dist[neighbor] > currScore:
#                 dist[neighbor] = currScore
#                 prev[neighbor] = set([curr])
#             elif dist[neighbor] == currScore:
#                 print("adding parent to existing set with score", currScore)
#                 prev[neighbor].add(parent)
#             if neighbor == join:
#                 if join in prev:
#                     print(f"prev after modification: {prev[join]=}, {dist[join]}")

#     checkNeighbor(1, aoc.getNext(curr, d), d, curr)
#     rightd = aoc.turnRight(d)
#     checkNeighbor(1001, aoc.getNext(curr, rightd), rightd, curr)
#     leftd = aoc.turnLeft(d)
#     checkNeighbor(1001, aoc.getNext(curr, leftd), leftd, curr)

# bestpaths = set()
# for curr, parents in prev.items():
#     print(curr, parents)
#     if len(parents) > 1:
#         print("more than 1 parent:", parents)

# def traceback(curr):
#     while True:
#         bestpaths.add(curr)
#         if curr==S:
#         # if curr in testparents:
#             return
#         parents = prev[curr]
#         if len(parents) > 1:
#             break
#         curr = list(parents)[0]
#     for parent in prev[curr]:
#         traceback(parent)

# traceback(E)
# print(len(bestpaths))

# for i in range(len(g)):
#     for j in range(len(g[0])):
#         if (i,j) in bestpaths:
#             print("O", end='')
#         else:
#             print(g[i][j], end='')
#     print()


# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# import aoc

# input = aoc.getInput("input")
# # input = aoc.getInput("test-input")
# # input = aoc.getInput("second-example")

# S = (len(input)-2, 1)
# E = (1, len(input[0])-2)
# currdir = (0,1)
# import heapq
# v = set()
# inHeap = set()
# inHeap.add((0, S, currdir))
# h = [(0, S, currdir)]
# while True:
#     x = heapq.heappop(h)
#     score, curr, d = x
#     if x not in inHeap:
#         continue
#     if curr == E:
#         print(score)
#         exit()
#     inHeap.remove(x)
#     if (curr, d) in v:
#         continue
#     v.add((curr, d))

#     def checkNeighbor(scoreIncrease, neighbor, d):
#         ni,nj = neighbor
#         if aoc.inBounds(ni,nj,input) and input[ni][nj]!="#":
#             y = (score+scoreIncrease, neighbor, d)
#             heapq.heappush(h, y)
#             inHeap.add(y)

#     checkNeighbor(1, aoc.getNext(curr, d), d)
#     rightd = aoc.turnRight(d)
#     checkNeighbor(1001, aoc.getNext(curr, rightd), rightd)
#     leftd = aoc.turnLeft(d)
#     checkNeighbor(1001, aoc.getNext(curr, leftd), leftd)
