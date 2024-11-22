import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc


# input = aoc.getInput("test-input")
input = aoc.getInput("input")

m = {
    1: lambda x, y: x+y,
    2: lambda x,y: x*y,
}
for l in input:
    l = list(map(int, l.split(",")))
    l[1] = 12
    l[2] = 2
    for i in range(0, len(l), 4):
        op = l[i]
        if op == 99:
            break
        fun = m[l[i]]
        l[l[i+3]] = fun(l[l[i+1]], l[l[i+2]])
    print(l[0])