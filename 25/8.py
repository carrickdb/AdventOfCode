import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

input = aoc.getInput("input")
# input = aoc.getInput("test-input")
# input = aoc.getInput("test-input2")

boxes = []
for i,l in enumerate(input):
    boxes.append(list(map(int, l.split(','))))
    # print(i, l)

class Node:
    def __init__(self, n):
        self.size = 1
        self.parent = n
        self.id = n

import math
lb = len(boxes)
forest = []
for i in range(lb):
    forest.append(Node(i))

def find(a):
    while forest[a].parent != a:
        a = forest[a].parent
    return forest[a]

import heapq
h = []
done = set()
for boxID, coords in enumerate(boxes):
    i,j,k = coords
    for otherBox in range(boxID+1, lb):
        otherCoords = boxes[otherBox]
        oi,oj,ok = otherCoords
        currDist = math.sqrt((i-oi)**2 + (j-oj)**2 + (k-ok)**2)
        heapn = (-currDist, boxID, otherBox)
        # if len(h) < 10000:
        heapq.heappush(h, heapn)
        # else:
        #     p = heapq.heappop(h)
        #     if -p[0] < currDist:
        #         heapq.heappush(h, p)
        #     else:
        #         heapq.heappush(h, heapn)

h2 = []
while h:
    a,b,c = heapq.heappop(h)
    heapq.heappush(h2, (-a,b,c))

while h2:
    curr = heapq.heappop(h2)
    _, a,b = curr
    # print(a,b)
    x = find(a)
    y = find(b)
    if x == y:
        continue
    if x.size == y.size:
        x,y = y,x
    y.parent = x.id
    x.size += y.size
    if x.size == len(boxes):
        print(boxes[a][0] * boxes[b][0])


# boxes = []
# for i,l in enumerate(input):
#     boxes.append(list(map(int, l.split(','))))
#     # print(i, l)

# class Node:
#     def __init__(self, n):
#         self.size = 1
#         self.parent = n
#         self.id = n

# import math
# lb = len(boxes)
# forest = []
# for i in range(lb):
#     forest.append(Node(i))

# def find(a):
#     while forest[a].parent != a:
#         a = forest[a].parent
#     return forest[a]

# import heapq
# h = []
# done = set()
# for boxID, coords in enumerate(boxes):
#     i,j,k = coords
#     for otherBox in range(boxID+1, lb):
#         otherCoords = boxes[otherBox]
#         oi,oj,ok = otherCoords
#         currDist = math.sqrt((i-oi)**2 + (j-oj)**2 + (k-ok)**2)
#         heapn = (-currDist, boxID, otherBox)
#         if len(h) < 1000:
#             heapq.heappush(h, heapn)
#         else:
#             p = heapq.heappop(h)
#             if -p[0] < currDist:
#                 heapq.heappush(h, p)
#             else:
#                 heapq.heappush(h, heapn)

# h2 = []
# while h:
#     a,b,c = heapq.heappop(h)
#     heapq.heappush(h2, (-a,b,c))

# while h2:
#     curr = heapq.heappop(h2)
#     _, a,b = curr
#     # print(a,b)
#     x = find(a)
#     y = find(b)
#     if x == y:
#         continue
#     if x.size == y.size:
#         x,y = y,x
#     y.parent = x.id
#     x.size += y.size

# # print()
# # for n in forest:
# #     print(n.id, n.parent, n.size)

# parents = set()
# for n in forest:
#     while n.id!=n.parent:
#         n = forest[n.parent]
#     parents.add(n.id)

# # print(len(parents))
# t = 1
# sizes = []
# for p in parents:
#     sizes.append(forest[p].size)
# sizes.sort()
# print(sizes[-1]*sizes[-2]*sizes[-3])
