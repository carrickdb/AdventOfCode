import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc
import math
codes = """869A
180A
596A
965A
973A"""

# codes = """029A
# 980A
# 179A
# 456A
# 379A"""

keypad = """789
456
123
 0A""".split('\n')

controller = """ ^A
<v>""".split('\n')


from itertools import pairwise, product

keypadCoords = {}
for i in range(len(keypad)):
    for j in range(len(keypad[0])):
        keypadCoords[keypad[i][j]] = (i,j)
controllerCoords = {}
for i,j in aoc.iterateThroughGraph(controller):
    controllerCoords[controller[i][j]] = (i,j)

for i,j in aoc.iterateThroughGraph(keypad):
    keypadCoords[keypad[i][j]] = (i,j)

def getShortestSequences(pair, device, v):
    a,b = pair
    if a == b:
        return [""]
    if a in v:
        return []
    v.add(a)
    seqs = []
    minlen = math.inf
    for dirchar, d in aoc.dirmap.items():
        n = aoc.getNext(a,d)
        if not aoc.inBounds(n,device):
            continue
        val = aoc.getGVal(n, device)
        if val == " ":
            continue
        prevSequences = getShortestSequences((n,b), device, v.copy())
        for s in prevSequences:
            newseq = dirchar + s
            minlen = min(minlen, len(newseq))
            seqs.append(newseq)
    return [x for x in seqs if len(x)==minlen]

controllerSequences = {}
for a,b in product("A><v^", repeat=2):
    ac = controllerCoords[a]
    bc = controllerCoords[b]
    controllerSequences[(a,b)] = getShortestSequences((ac,bc), controller, set())

def getProducts(newSequences, seqs):
    if not newSequences:
        newSequences = seqs
    else:
        newSequences = list(product(newSequences, seqs))
        for i in range(len(newSequences)):
            n,m = newSequences[i]
            newSequences[i] = n+m
    return newSequences

def getSequences(prevSeq, id):
    if id == 0:
        prevSeq = "A" + prevSeq
        newSequences = []
        for a,b in pairwise(prevSeq):
            ac = keypadCoords[a]
            bc = keypadCoords[b]
            seqs = [x+"A" for x in getShortestSequences((ac,bc), keypad, set())]
            newSequences = getProducts(newSequences, seqs)
        return newSequences
    seqs = getSequences(prevSeq, id-1)
    newSequences = []
    for seq in seqs:
        seq = "A" + seq
        y = []
        for a,b in pairwise(seq):
            currSeqs = [x+"A" for x in controllerSequences[(a,b)]]
            y = getProducts(y, currSeqs)
        newSequences.extend(y)
    minlen = min([len(x) for x in newSequences])
    ret = [x for x in newSequences if len(x) == minlen]
    return ret

total = 0
for code in codes.split():
    lenShortest = len(getSequences(code, 2)[0])
    numeric = int(code[:-1])
    # print(lenShortest, numeric)
    total += numeric * lenShortest

print(total)






# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# import aoc

# # codes = """869A
# # 180A
# # 596A
# # 965A
# # 973A"""

# codes = """029A
# 980A
# 179A
# 456A
# 379A"""

# keypad = """789
# 456
# 123
#  0A""".split("\n")

# controller = """ ^A
# <v>""".split("\n")

# keypadSequences = {}
# controllerSequences = {}

# from collections import deque

# def bfs(device, start, sequences):
#     q = deque()
#     q.append((start, ""))
#     v = set()
#     while q:
#         lq = len(q)
#         for _ in range(lq):
#             curr, ins = q.popleft()
#             if curr in v:
#                 continue
#             v.add(curr)
#             sequences[(aoc.getGVal(start, device), aoc.getGVal(curr,device))] = ins
#             for dirchar, d in aoc.dirmap.items():
#                 n = aoc.getNext(curr,d)
#                 if not aoc.inBounds(n,device):
#                     continue
#                 ni,nj = n
#                 if n not in v and device[ni][nj]!=" ":
#                     q.append((n, ins+dirchar))

# for c in aoc.iterateThroughGraph(keypad):
#     bfs(keypad, c, keypadSequences)

# for c in aoc.iterateThroughGraph(controller):
#     bfs(controller, c, controllerSequences)

# from itertools import pairwise
# def getNextSequence(seq, sequences):
#     newSequence = []
#     for p in pairwise(seq):
#         newSequence.extend([sequences[p], "A"])
#     return ''.join(newSequence)

# def getButtonPresses(code):
#     currSequence = getNextSequence("A"+code, keypadSequences)
#     for _ in range(3):
#         currSequence = getNextSequence("A"+currSequence, controllerSequences)
#     return len(currSequence)

# codes = codes.split()
# total = 0
# for code in codes:
#     lenShortest = getButtonPresses(code)
#     numeric = int(code[:-1])
#     print(lenShortest, numeric)
#     total += numeric * lenShortest

# print(total)