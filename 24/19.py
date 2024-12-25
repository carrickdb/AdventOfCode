import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc
from functools import cache

stuff = aoc.getInput(os.getenv("HOME") + "/Desktop/input")
# stuff = aoc.getInput("test-input")

patterns = stuff[0].split(", ")

total = 0
for design in stuff[2:]:
    # print(design)
    dp = [1]
    for i in range(len(design)-1, -1, -1):
        newTotal = 0
        for pattern in patterns:
            lp = len(pattern)
            if pattern == design[i:i+lp]:
                newTotal += dp[-lp]
        dp.append(newTotal)
    # print(dp)
    # print(dp[-1])
    total += dp[-1]

print(total)


## Part 1
# patterns = stuff[0].split(", ")
# possible = 0
# for design in stuff[2:]:
#     @cache
#     def isPossible(i):
#         if i >= len(design):
#             return True
#         for pattern in patterns:
#             lp = len(pattern)
#             e = i+lp
#             # print(f"{i} {design[i:e]=}, {pattern=}")
#             if design[i:e] == pattern:
#                 if isPossible(e):
#                     return True
#         return False

#     res = isPossible(0)
#     possible += res

# print(possible)