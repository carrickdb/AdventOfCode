import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc
import re

input = aoc.getInput("input")
# input = aoc.getInput("test-input")
correction = 10000000000000
aMultiple = 3
import math

total = 0
for i in range(0,len(input), 4):
    a,b,p,_ = input[i:i+4]
    ax,ay = list(map(int, re.findall(r"[XY]\+(\d+)", a)))
    bx,by = list(map(int, re.findall(r"[XY]\+(\d+)", b)))  # TODO
    px,py = list(map(int, re.findall(r"[XY]=(\d+)",p)))
    px,py = px+correction, py+correction
    # https://openstax.org/books/intermediate-algebra-2e/pages/4-6-solve-systems-of-equations-using-determinants
    # https://www.reddit.com/r/adventofcode/comments/1hd4wda/comment/m1temc7
    det = ax*by-ay*bx
    a = (px*by-py*bx) / det
    b = (ax*py-ay*px) / det
    if a == int(a) and b == int(b):
        total += 3*int(a) + int(b)
print(total)


# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# import aoc
# import re

# input = aoc.getInput("input")
# # input = aoc.getInput("test-input")

# """
# Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400
# """
# aMultiple = 3
# import math
# total = 0
# for i in range(0,len(input), 4):
#     a,b,p,_ = input[i:i+4]
#     ax,ay = list(map(int, re.findall(r"[XY]\+(\d+)", a)))
#     bx,by = list(map(int, re.findall(r"[XY]\+(\d+)", b)))  # TODO
#     px,py = list(map(int, re.findall(r"[XY]=(\d+)",p)))

#     minTokens = math.inf
#     for i in range(101):
#         for j in range(101):
#             if ax*i+bx*j==px and ay*i+by*j==py:
#                 print(i,j)
#                 minTokens = min(minTokens, aMultiple*i + j)
#     print(minTokens)
#     if minTokens == math.inf:
#         continue
#     total += minTokens
# print(total)


# # No: 41184


