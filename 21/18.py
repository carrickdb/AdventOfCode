# Part 2:

import json

def getMagnitude(result):
    if type(result) is int:
        return result
    return 3*getMagnitude(result[0]) + 2*getMagnitude(result[1])

def reduceNums(numStr):
    numList = [x for x in numStr]
    # print(''.join(numList))
    done = False
    while not done:
        done = True
        i = 0
        nests = 0
        while i < len(numList):
            curr = numList[i]
            if curr == "[":
                nests += 1
                i += 1
                continue
            if curr == "]":
                i += 1
                nests -= 1
                continue
            if curr.isdigit() and nests > 4 and i+2 < len(numList) and numList[i+2].isdigit():
                # print(''.join(numList))
                for j in range(i-1, -1, -1):
                    if numList[j].isdigit():
                        numList[j] = str(int(numList[j]) + int(curr))
                        break
                for j in range(i+3, len(numList)):
                    if numList[j].isdigit():
                        numList[j] = str(int(numList[j]) + int(numList[i+2]))
                        break
                numList[i-1] = "0"
                numList = numList[:i] + numList[i+4:]
                done = False
                i = 0
                break
            i += 1
        i = 0
        while done and i < len(numList):
            if numList[i].isdigit():
                currNum = int(numList[i])
                if currNum > 9:
                    L = currNum//2
                    R = currNum//2 + (currNum % 2)
                    numList = numList[:i] + ["["] + [str(L)] + [","] + [str(R)] + ["]"] + numList[i+1:]
                    done = False
                    i += 4
                    # print(''.join(numList))
                    break
            i += 1

    return ''.join(numList)


def addNums(a, b):
    total = "[" + a + "," + b + "]"
    result = reduceNums(total)
    magnitude = getMagnitude(json.loads(result))
    return magnitude

snailfishNums = []
with open("input18") as f:
    for line in f:
        snailfishNums.append(line.strip())

maxMagnitude = float("-inf")
for i in range(len(snailfishNums)):
    for j in range(i+1, len(snailfishNums)):
        maxMagnitude = max(maxMagnitude, addNums(snailfishNums[i], snailfishNums[j]))
        maxMagnitude = max(maxMagnitude, addNums(snailfishNums[j], snailfishNums[i]))

print(maxMagnitude)



## Part 1:
# import json
#
# def getMagnitude(result):
#     if type(result) is int:
#         return result
#     return 3*getMagnitude(result[0]) + 2*getMagnitude(result[1])
#
# def reduceNums(numStr):
#     numList = [x for x in numStr]
#     # print(''.join(numList))
#     done = False
#     while not done:
#         done = True
#         i = 0
#         nests = 0
#         while i < len(numList):
#             curr = numList[i]
#             if curr == "[":
#                 nests += 1
#                 i += 1
#                 continue
#             if curr == "]":
#                 i += 1
#                 nests -= 1
#                 continue
#             if curr.isdigit() and nests > 4 and i+2 < len(numList) and numList[i+2].isdigit():
#                 # print(''.join(numList))
#                 for j in range(i-1, -1, -1):
#                     if numList[j].isdigit():
#                         numList[j] = str(int(numList[j]) + int(curr))
#                         break
#                 for j in range(i+3, len(numList)):
#                     if numList[j].isdigit():
#                         numList[j] = str(int(numList[j]) + int(numList[i+2]))
#                         break
#                 numList[i-1] = "0"
#                 numList = numList[:i] + numList[i+4:]
#                 done = False
#                 i = 0
#                 break
#             i += 1
#         i = 0
#         while done and i < len(numList):
#             if numList[i].isdigit():
#                 currNum = int(numList[i])
#                 if currNum > 9:
#                     L = currNum//2
#                     R = currNum//2 + (currNum % 2)
#                     numList = numList[:i] + ["["] + [str(L)] + [","] + [str(R)] + ["]"] + numList[i+1:]
#                     done = False
#                     i += 4
#                     # print(''.join(numList))
#                     break
#             i += 1
#
#     return ''.join(numList)
#
# total = None
# with open("input18") as f:
#     for line in f:
#         if not total:
#             total = line.strip()
#             continue
#         total = "[" + total + "," + line.strip() + "]"
#         total = reduceNums(total)
#
# print(total)
#
# print(getMagnitude(json.loads(total)))
