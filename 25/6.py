import sys, os
from functools import cache

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

input = aoc.getInput("input")
# input = aoc.getInput("test-input")
# input = aoc.getInput("test-input2")
print(input)
import operator
operations = {
    '*': operator.mul,
    '+': operator.add
}
max_len = max(len(l) for l in input)
stuff = []
for l in input:
    llist = list(l)
    if len(l) < max_len:
        llist.extend([' '] * (max_len - len(l)))
    stuff.append(llist)

class Problem:
    def __init__(self):
        self.op = None
        self.nums = []

t = 0
problems = list(zip(*stuff))
print(problems)
problem_list = []
next_problem = Problem()
for col in problems:
    if ''.join(col).isspace():
        problem_list.append(next_problem)
        next_problem = Problem()
        continue
    if col[-1] in operations:
        next_problem.op = operations[col[-1]]
        next_problem.nums.append(int(''.join(col[:-1]).strip()))
    else:
        next_problem.nums.append(int(''.join(col).strip()))
problem_list.append(next_problem)

from functools import reduce
for p in problem_list:
    st = reduce(p.op, p.nums)
    print(st)
    t += st

print(t)



# problems = []
# for line in input[:-1]:
#     problems.append(list(map(int, line.split())))
# problems.append(input[-1].split())

# import operator
# operations = {
#     '*': operator.mul,
#     '+': operator.add
# }

# problems = list(zip(*problems))
# t = 0
# for p in problems:
#     st = 1
#     if p[-1] == '+':
#         st = 0
#     op = operations[p[-1]]
#     for n in p[:-1]:
#         st = op(st, n)
#     t += st
# print(t)