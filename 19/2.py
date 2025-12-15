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
input = list(map(int, input[0].split(",")))
for noun in range(100):
    for verb in range(100):
        l = input[:]
        l[1] = noun
        l[2] = verb
        for i in range(0, len(l), 4):
            op = l[i]
            if op == 99:
                break
            fun = m[l[i]]
            l[l[i+3]] = fun(l[l[i+1]], l[l[i+2]])
        if l[0] == 19690720:
            print(100*noun+verb)