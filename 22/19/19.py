from collections import deque
import re

blueprints = []

# Blueprint 3: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 4 ore and 18 clay. Each geode robot costs 4 ore and 11 obsidian.
r = r'Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.'

for bp, orer, cr, obro, obrc, gro, grob in re.findall(r, open("input2").read()):
    blueprints.append(list(map(int, [bp, orer, cr, obro, obrc, gro, grob])))

qualityLevels = 0
for bp, orer, cr, obro, obrc, gro, grob in blueprints:
    print(bp, orer, cr, obro, obrc, gro, grob)
    # ore robot, clay robot, obsidian robot, geode robot, ore, clay, obsidian, geode
    oreRobot, clayRobot, obsRobot, geodeRobot, ore, clay, obs, geodes = [i for i in range(8)]
    curr = [1,0,0,0,0,0,0,0]
    q = deque([curr])
    minute = 1
    visited = set()
    totalGeodes = 0
    while minute < 25:
        lenq = len(q)
        for i in range(lenq):
            curr = q.popleft()
            if tuple(curr) in visited:
                continue
            visited.add(tuple(curr))
            if minute == 24:
                totalGeodes = max(totalGeodes, curr[geodeRobot] + curr[geodes])
            else:
                skipminutes = 0
                for robotType in range(4):
                    newNode = curr.copy()
                    if robotType == 0:
                        if curr[ore] >= orer:
                            newNode[ore] -= orer
                            newNode[oreRobot] += 1
                    elif robotType == 1:
                        if curr[ore] >= cr:
                            newNode[ore] -= cr
                            newNode[clayRobot] += 1
                    elif robotType == 2:
                        if curr[ore] >= obro and curr[clay] >= obrc:
                            newNode[ore] -= obro
                            newNode[clay] -= obrc
                            newNode[obsRobot] += 1
                    else:
                        if curr[ore] >= gro and curr[obs] >= grob:
                            newNode[ore] -= gro
                            newNode[obs] -= grob
                            newNode[geodeRobot] += 1
                    for i in range(4):
                        newNode[4+i] += curr[i]
                    if tuple(newNode) not in visited:
                        q.append(newNode)
        # print(q)
        # input()
    print(totalGeodes)
    qualityLevels += totalGeodes

print(qualityLevels)





# from collections import deque
# import re
#
# blueprints = []
#
# # Blueprint 3: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 4 ore and 18 clay. Each geode robot costs 4 ore and 11 obsidian.
# r = r'Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.'
#
# for bp, orer, cr, obro, obrc, gro, grob in re.findall(r, open("input2").read()):
#     blueprints.append(list(map(int, [bp, orer, cr, obro, obrc, gro, grob])))
#
# qualityLevels = 0
# for bp, orer, cr, obro, obrc, gro, grob in blueprints:
#     print(bp, orer, cr, obro, obrc, gro, grob)
#     # ore robot, clay robot, obsidian robot, geode robot, ore, clay, obsidian, geode
#     oreRobot, clayRobot, obsRobot, geodeRobot, ore, clay, obs, geodes = [i for i in range(8)]
#     curr = [1,0,0,0,0,0,0,0]
#     q = deque([curr])
#     minute = 1
#     visited = set()
#     totalGeodes = 0
#     while minute < 25:
#         lenq = len(q)
#         for i in range(lenq):
#             curr = q.popleft()
#             if tuple(curr) in visited:
#                 continue
#             visited.add(tuple(curr))
#             if minute == 24:
#                 totalGeodes = max(totalGeodes, curr[geodeRobot] + curr[geodes])
#             else:
#                 for robotType in range(4):
#                     newNode = curr.copy()
#                     addNewNode = False
#                     if robotType == 0:
#                         if curr[ore] >= orer:
#                             addNewNode = True
#                             newNode[ore] -= orer
#                             newNode[oreRobot] += 1
#                     elif robotType == 1:
#                         if curr[ore] >= cr:
#                             addNewNode = True
#                             newNode[ore] -= cr
#                             newNode[clayRobot] += 1
#                     elif robotType == 2:
#                         if curr[ore] >= obro and curr[clay] >= obrc:
#                             addNewNode = True
#                             newNode[ore] -= obro
#                             newNode[clay] -= obrc
#                             newNode[obsRobot] += 1
#                     else:
#                         if curr[ore] >= gro and curr[obs] >= grob:
#                             addNewNode = True
#                             newNode[ore] -= gro
#                             newNode[obs] -= grob
#                             newNode[geodeRobot] += 1
#                     if addNewNode:
#                         for i in range(4):
#                             newNode[4+i] += curr[i]
#                         if tuple(newNode) not in visited:
#                             q.append(newNode)
#                 newNode = curr.copy()
#                 for i in range(4):
#                     newNode[4+i] += curr[i]
#                 if tuple(newNode) not in visited:
#                     q.append(newNode)
#         # print(q)
#         # input()
#         minute += 1
#     print(totalGeodes)
#     qualityLevels += totalGeodes
#
# print(qualityLevels)
