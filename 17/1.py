import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc
from functools import reduce

input = aoc.getInput("input")

for l in input:
    doubles = [int(l[i]) if l[i] == l[(i+len(l)//2) % len(l)] else 0 for i in range(len(l))]
    print(sum(doubles))



# for l in input:
#     doubles = [int(l[i]) if l[i] == l[(i+1) % len(l)] else 0 for i in range(len(l))]
#     print(sum(doubles))
