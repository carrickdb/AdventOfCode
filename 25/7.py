import sys, os
from functools import cache

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

# input = aoc.getInput("input")
input = aoc.getInput("test-input")
# input = aoc.getInput("test-input2")

beam = input[0].index("S")

@cache
def rec(row, col):
    if row == len(input) - 1:
        return 1
    if input[row][col] == "^":
        return rec(row+1, col-1) + rec(row+1, col+1)
    return rec(row+1, col)

print(rec(0, beam))


# beams = [input[0].index("S")]
# splits = 0
# for line in input[1:]:
#     newbeams = set()
#     for beam in beams:
#         if line[beam] == "^":
#             newbeams.add(beam-1)
#             newbeams.add(beam+1)
#             splits += 1
#         else:
#             newbeams.add(beam)
#     beams = newbeams

# print(splits)