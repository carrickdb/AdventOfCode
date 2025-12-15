import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

input = aoc.getInput("input")
# input = aoc.getInput("test-input")





# maxRect = 0
# for a,acoord in enumerate(input):
#     ai,aj = list(map(int, acoord.split(",")))
#     for bcoord in input[a+1:]:
#         bi,bj = list(map(int, bcoord.split(",")))
#         currArea = (abs(ai-bi)+1) * (abs(aj-bj)+1)
#         # print(ai,aj,bi,bj, currArea)
#         maxRect = max(maxRect, currArea)

# print(maxRect)

