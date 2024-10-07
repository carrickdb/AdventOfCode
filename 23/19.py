import aoc, re

input = aoc.getInput("input-19")

inst = True
mapping = {"A":True, "R": False}
for l in input:
    if l == "":
        break
    if inst:
        name, rest = l.split("{")
        rest = rest[:-1].split(",")
        assessment = []
        for comp in rest[:-1]:
            pattern = re.compile("([xmas])([<>])([0-9]+):(.+)")
            assessment.append(list(re.findall(pattern, comp)[0]))
        assessment.append([rest[-1]])
        mapping[name] = assessment

def getIntervals(interval, fun):
    currfun = mapping[fun]
    if len(currfun) == 1:
        return interval, currfun[0]
    newintervals = []
    for i in currfun:
        letter, comp, num, res = i
        if comp == "<":
            currinst = res if attributeMapping[letter] < int(num) else None
        else:
            currinst = res if attributeMapping[letter] > int(num) else None
    return newintervals



print(getIntervals([0,4000], "in"))



# import aoc, re

# input = aoc.getInput("input-19")

# inst = True
# mapping = {"A":True, "R": False}
# total = 0
# for l in input:
#     if l == "":
#         inst = False
#         continue
#     if inst:
#         # px{a<2006:qkq,m>2090:A,rfg}
#         name, rest = l.split("{")
#         rest = rest[:-1].split(",")
#         assessment = []
#         for comp in rest[:-1]:
#             pattern = re.compile("([xmas])([<>])([0-9]+):(.+)")
#             assessment.append(list(re.findall(pattern, comp)[0]))
#         assessment.append([rest[-1]])
#         mapping[name] = assessment
#     else:
#         # {x=787,m=2655,a=1222,s=2876}
#         pattern = re.compile("(x)=([0-9]+),(m)=([0-9]+),(a)=([0-9]+),(s)=([0-9]+)")
#         m = re.findall(pattern, l)[0]
#         def chonker(x):
#             for i in range(0,len(x),2):
#                 yield x[i:i+2]
#         attributeMapping = {}
#         for chonk in chonker(m):
#             attributeMapping[chonk[0]] = int(chonk[1])
#         currinst = "in"
#         while currinst != "A" and currinst != "R":
#             # print(currinst)
#             currdec = mapping[currinst]
#             currinst = None
#             for i in range(len(currdec)):
#                 currfun = currdec[i]
#                 if len(currfun) == 1:
#                     currinst = currfun[0]
#                 else:
#                     letter, comp, num, res = currfun
#                     if comp == "<":
#                         currinst = res if attributeMapping[letter] < int(num) else None
#                     else:
#                         currinst = res if attributeMapping[letter] > int(num) else None
#                 if currinst:
#                     break
#         res = mapping[currinst]
#         # print(currinst)
#         if res:
#             # print(m)
#             total += sum(attributeMapping.values())

# print(total)
