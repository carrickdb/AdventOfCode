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

shortest = math.inf
from functools import cache
@cache
def getShortestLen(seq, id):
    if id == 0:
        prevSeq = "A" + seq
        newSequences = []
        for a,b in pairwise(prevSeq):
            ac = keypadCoords[a]
            bc = keypadCoords[b]
            seqs = [x+"A" for x in getShortestSequences((ac,bc), keypad, set())]
            for s in seqs:
                getShortestLen(s, id + 1)
    else:
        newSequences = []
        seq = "A" + seq
        y = []
        for a,b in pairwise(seq):
            currSeqs = [x+"A" for x in controllerSequences[(a,b)]]
            y = getProducts(y, currSeqs)
        newSequences.extend(y)
        if id==2:
            minlen = min([len(x) for x in newSequences])
            global shortest
            shortest = min(shortest, minlen)
            return shortest
        else:
            for ns in newSequences:
                getShortestLen(ns, id+1)

total = 0
for code in codes.split():
    shortest = math.inf
    getShortestLen(code, 0)
    numeric = int(code[:-1])
    total += numeric * shortest

print(total)


# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# import aoc
# import math
# codes = """869A
# 180A
# 596A
# 965A
# 973A"""

# # codes = """029A
# # 980A
# # 179A
# # 456A
# # 379A"""

# keypad = """789
# 456
# 123
#  0A""".split('\n')

# controller = """ ^A
# <v>""".split('\n')


# from itertools import pairwise, product

# keypadCoords = {}
# for i in range(len(keypad)):
#     for j in range(len(keypad[0])):
#         keypadCoords[keypad[i][j]] = (i,j)
# controllerCoords = {}
# for i,j in aoc.iterateThroughGraph(controller):
#     controllerCoords[controller[i][j]] = (i,j)

# for i,j in aoc.iterateThroughGraph(keypad):
#     keypadCoords[keypad[i][j]] = (i,j)

# def getShortestSequences(pair, device, v):
#     a,b = pair
#     if a == b:
#         return [""]
#     if a in v:
#         return []
#     v.add(a)
#     seqs = []
#     minlen = math.inf
#     for dirchar, d in aoc.dirmap.items():
#         n = aoc.getNext(a,d)
#         if not aoc.inBounds(n,device):
#             continue
#         val = aoc.getGVal(n, device)
#         if val == " ":
#             continue
#         prevSequences = getShortestSequences((n,b), device, v.copy())
#         for s in prevSequences:
#             newseq = dirchar + s
#             minlen = min(minlen, len(newseq))
#             seqs.append(newseq)
#     return [x for x in seqs if len(x)==minlen]

# controllerSequences = {}
# for a,b in product("A><v^", repeat=2):
#     ac = controllerCoords[a]
#     bc = controllerCoords[b]
#     controllerSequences[(a,b)] = getShortestSequences((ac,bc), controller, set())

# def getProducts(newSequences, seqs):
#     if not newSequences:
#         newSequences = seqs
#     else:
#         newSequences = list(product(newSequences, seqs))
#         for i in range(len(newSequences)):
#             n,m = newSequences[i]
#             newSequences[i] = n+m
#     return newSequences

# def getSequences(prevSeq, id):
#     if id == 0:
#         prevSeq = "A" + prevSeq
#         newSequences = []
#         for a,b in pairwise(prevSeq):
#             ac = keypadCoords[a]
#             bc = keypadCoords[b]
#             seqs = [x+"A" for x in getShortestSequences((ac,bc), keypad, set())]
#             newSequences = getProducts(newSequences, seqs)
#         return newSequences
#     seqs = getSequences(prevSeq, id-1)
#     newSequences = []
#     for seq in seqs:
#         seq = "A" + seq
#         y = []
#         for a,b in pairwise(seq):
#             currSeqs = [x+"A" for x in controllerSequences[(a,b)]]
#             y = getProducts(y, currSeqs)
#         newSequences.extend(y)
#     minlen = min([len(x) for x in newSequences])
#     ret = [x for x in newSequences if len(x) == minlen]
#     return ret

# shortest = math.inf
# from functools import cache
# @cache
# def getShortestLen(seq, id):
#     if id == 0:
#         prevSeq = "A" + seq
#         newSequences = []
#         for a,b in pairwise(prevSeq):
#             ac = keypadCoords[a]
#             bc = keypadCoords[b]
#             seqs = [x+"A" for x in getShortestSequences((ac,bc), keypad, set())]
#             newSequences = getProducts(newSequences, seqs)
#         for ns in newSequences:
#             getShortestLen(ns, id + 1)
#     else:
#         newSequences = []
#         seq = "A" + seq
#         y = []
#         for a,b in pairwise(seq):
#             currSeqs = [x+"A" for x in controllerSequences[(a,b)]]
#             y = getProducts(y, currSeqs)
#         newSequences.extend(y)
#         if id==25:
#             minlen = min([len(x) for x in newSequences])
#             global shortest
#             shortest = min(shortest, minlen)
#             return shortest
#         else:
#             for ns in newSequences:
#                 getShortestLen(ns, id+1)


# total = 0
# for code in codes.split():
#     shortest = math.inf
#     getShortestLen(code, 0)
#     numeric = int(code[:-1])
#     total += numeric * shortest

# print(total)



# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# import aoc
# import math
# codes = """869A
# 180A
# 596A
# 965A
# 973A"""

# codes = """029A
# 980A
# 179A
# 456A
# 379A"""

# keypad = """789
# 456
# 123
#  0A""".split('\n')

# controller = """ ^A
# <v>""".split('\n')


# from itertools import pairwise, product

# keypadCoords = {}
# for i in range(len(keypad)):
#     for j in range(len(keypad[0])):
#         keypadCoords[keypad[i][j]] = (i,j)
# controllerCoords = {}
# for i,j in aoc.iterateThroughGraph(controller):
#     controllerCoords[controller[i][j]] = (i,j)

# for i,j in aoc.iterateThroughGraph(keypad):
#     keypadCoords[keypad[i][j]] = (i,j)

# def getShortestSequences(pair, device, v):
#     a,b = pair
#     if a == b:
#         return [""]
#     if a in v:
#         return []
#     v.add(a)
#     seqs = []
#     minlen = math.inf
#     for dirchar, d in aoc.dirmap.items():
#         n = aoc.getNext(a,d)
#         if not aoc.inBounds(n,device):
#             continue
#         val = aoc.getGVal(n, device)
#         if val == " ":
#             continue
#         prevSequences = getShortestSequences((n,b), device, v.copy())
#         for s in prevSequences:
#             newseq = dirchar + s
#             minlen = min(minlen, len(newseq))
#             seqs.append(newseq)
#     return [x for x in seqs if len(x)==minlen]

# controllerSequences = {}
# for a,b in product("A><v^", repeat=2):
#     ac = controllerCoords[a]
#     bc = controllerCoords[b]
#     controllerSequences[(a,b)] = getShortestSequences((ac,bc), controller, set())

# def getProducts(newSequences, seqs):
#     if not newSequences:
#         newSequences = seqs
#     else:
#         newSequences = list(product(newSequences, seqs))
#         for i in range(len(newSequences)):
#             n,m = newSequences[i]
#             newSequences[i] = n+m
#     return newSequences

# def getSequences(prevSeq, id):
#     if id == 0:
#         prevSeq = "A" + prevSeq
#         newSequences = []
#         for a,b in pairwise(prevSeq):
#             ac = keypadCoords[a]
#             bc = keypadCoords[b]
#             seqs = [x+"A" for x in getShortestSequences((ac,bc), keypad, set())]
#             newSequences = getProducts(newSequences, seqs)
#         return newSequences
#     seqs = getSequences(prevSeq, id-1)
#     newSequences = []
#     for seq in seqs:
#         seq = "A" + seq
#         y = []
#         for a,b in pairwise(seq):
#             currSeqs = [x+"A" for x in controllerSequences[(a,b)]]
#             y = getProducts(y, currSeqs)
#         newSequences.extend(y)
#     minlen = min([len(x) for x in newSequences])
#     ret = [x for x in newSequences if len(x) == minlen]
#     return ret

# total = 0
# for code in codes.split():
#     lenShortest = len(getSequences(code, 2)[0])
#     numeric = int(code[:-1])
#     # print(lenShortest, numeric)
#     total += numeric * lenShortest

# print(total)
