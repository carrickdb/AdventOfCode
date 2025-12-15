import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

# input = aoc.getInput("input")
# input = aoc.getInput("test-input")
input = aoc.getInput("test-input2")

g = {}
m = {}
for i,l in enumerate(input):
    n, children = l.split(': ')
    m[n] = i
    children = children.split()
    g[n] = children

from functools import cache
@cache
def getPaths(curr, dac, fft):
    if curr == "out":
        return dac and fft
    t = 0
    for child in g[curr]:
        t += getPaths(child, dac or curr=="dac", fft or curr=="fft")
    return t

print(getPaths("svr", False, False))


# g = {}
# for l in input:
#     n, children = l.split(': ')
#     children = children.split()
#     g[n] = children

# def getPaths(curr, v):
#     if curr in v:
#         return 0
#     if curr == "out":
#         return 1
#     children = g[curr]
#     t = 0
#     v.add(curr)
#     for child in children:
#         t += getPaths(child, v)
#     v.remove(curr)
#     return t

# print(getPaths("you", set()))