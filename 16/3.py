import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

import itertools

from numpy import transpose

input = aoc.getInput("input")

m = transpose([list(map(int, l.split())) for l in input])
count = 0
for r in m:
    for i in range(0, len(r), 3):
        triangle = True
        for a,b,c in itertools.permutations(r[i:i+3]):
            triangle &= a+b > c
        count += triangle
print(count)

# # input = ["5 10 6"]
# poss = 0
# for l in input:
#     l = list(map(int, l.split()))
#     triangle = True
#     for a,b,c in itertools.permutations(l):
#         triangle &= a+b > c
#     poss += triangle
# print(poss)