import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

input = aoc.getInput("test-input")
# input = aoc.getInput("input")

dirs = {
    "R": (0,1),
    "L": (0, -1),
    "U": (-1, 0),
    "D": (1, 0)
}
for i in range(0, len(input), 2):
    a, b = input[i], input[i+1]
    g = {}
    ci,cj = 0,0
    step = 0
    instructions = a.split(",")
    for inst in instructions:
        d, steps = inst[0], int(inst[1:])
        di, dj = dirs[d]
        for _ in range(steps):
            ci += di
            step += 1
            cj += dj
            if (ci, cj) in g:
                continue
            g[(ci,cj)] = step
    instructions = b.split(",")
    ci,cj = 0,0
    step = 0
    shortest = float("inf")
    for inst in instructions:
        d, steps = inst[0], int(inst[1:])
        di,dj = dirs[d]
        for _ in range(steps):
            ci += di
            cj += dj
            step += 1
            if (ci,cj) in g:
                if g[(ci,cj)] < 0:
                    continue
                shortest = min(shortest, step+g[(ci,cj)])
                g[(ci,cj)] = -g[(ci,cj)]
    print(shortest)



# dirs = {
#     "R": (0,1),
#     "L": (0, -1),
#     "U": (-1, 0),
#     "D": (1, 0)
# }
# for i in range(0, len(input), 2):
#     closest = float("inf")
#     a, b = input[i], input[i+1]
#     g = set()
#     ci,cj = 0,0
#     instructions = a.split(",")
#     for inst in instructions:
#         d, steps = inst[0], int(inst[1:])
#         di, dj = dirs[d]
#         for _ in range(steps):
#             ci += di
#             cj += dj
#             g.add((ci,cj))
#     instructions = b.split(",")
#     ci,cj = 0,0
#     for inst in instructions:
#         d, steps = inst[0], int(inst[1:])
#         di,dj = dirs[d]
#         for _ in range(steps):
#             ci += di
#             cj += dj
#             if (ci,cj) in g:
#                 # print(ci,cj)
#                 closest = min(closest, abs(ci)+abs(cj))
#     print(closest)
