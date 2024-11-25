import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

input = aoc.getInput("input")
# input = aoc.getInput("test-input")

for l in input:
    inGarbage = False
    ignore = False
    garbage = 0
    for c in l:
        if ignore:
            ignore = False
        elif inGarbage:
            if c == ">":
                inGarbage = False
            elif c == "!":
                ignore = True
            else:
                garbage += 1
        elif c == "<":
            inGarbage = True
    print(garbage)






# for l in input:
#     groups = 0
#     inGarbage = False
#     ignore = False
#     score = 0
#     for c in l:
#         if ignore:
#             ignore = False
#         elif inGarbage:
#             if c == ">":
#                 inGarbage = False
#             elif c == "!":
#                 ignore = True
#         elif c == "{":
#             groups += 1
#         elif c == "}":
#             score += groups
#             groups -= 1
#         elif c == "<":
#             inGarbage = True
#     print(score)
