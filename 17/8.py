import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

input = aoc.getInput("input")
# input = aoc.getInput("test-input")

import re
import operator

ops = {
    ">": operator.gt,
    "<": operator.lt,
    ">=": operator.ge,
    "<=": operator.le,
    "==": operator.eq,
    "!=": operator.ne
}

f = {
    "dec": operator.sub,
    "inc": operator.add
}


registers = {}
max_seen = float("-inf")
for l in input:
    r1, operation, operand, _, r2, cmp, num = re.findall(r"[\w>=!<-]+", l)
    num, operand = int(num), int(operand)
    r2val = 0 if r2 not in registers else registers[r2]
    if cmp not in ops:
        print(l)
        exit()
    if ops[cmp](r2val, num):
        r1val = 0 if r1 not in registers else registers[r1]
        curr = f[operation](r1val, operand)
        registers[r1] = curr
        max_seen = max(max_seen, curr)

print(max_seen)


# noj dec -179 if f != 1421
# registers = {}
# for l in input:
#     r1, operation, operand, _, r2, cmp, num = re.findall(r"[\w>=!<-]+", l)
#     num, operand = int(num), int(operand)
#     r2val = 0 if r2 not in registers else registers[r2]
#     if cmp not in ops:
#         print(l)
#         exit()
#     if ops[cmp](r2val, num):
#         r1val = 0 if r1 not in registers else registers[r1]
#         registers[r1] = f[operation](r1val, operand)

# print(max(registers.values()))
