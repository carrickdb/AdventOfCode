import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

input = aoc.getInput("input")
# input = aoc.getInput("test-input")
# input = aoc.getInput("test-input2")
curr = 50
t = 0
for i in input:
    dir, steps = i[0], int(i[1:])
    if dir == "L":
        if curr == 0:
            curr = 100
        curr = curr-steps
        if curr <= 0:
            print(dir, steps, abs(curr) // 100 + 1, curr)
            t += abs(curr) // 100 + 1
    else:
        curr = curr+steps
        if curr >= 100:
            print(dir, steps, curr //100, curr)
            t += curr // 100
    curr %= 100


print(t)