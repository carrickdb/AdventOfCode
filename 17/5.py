import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

input = aoc.getInput("input")
# input = aoc.getInput("test-input")
i = list(map(int, input))
pos = 0
steps = 0
while pos >= 0 and pos < len(i):
    jump = i[pos]
    if jump >= 3:
        i[pos] -= 1
    else:
        i[pos] += 1
    pos += jump
    steps += 1

print(steps)