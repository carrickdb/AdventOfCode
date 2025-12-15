import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc
from collections import defaultdict

filename = os.getenv("HOME") + "/Desktop/input"
# with open("test-input") as f:
# with open("part2-example") as f:
with open(filename) as f:
    stuff = f.read()
    initial, gatesStrs = stuff.split("\n\n")

funcMap = {
    "AND": lambda x,y: x&y,
    "OR": lambda x,y: x|y,
    "XOR": lambda x,y: x^y
}

wires = {}
gates = set()

for line in initial.split("\n"):
    wire, val = line.split(": ")
    wires[wire] = int(val)

x = ''.join(aoc.mapstr([v for _,v in sorted(wires.items())[:len(wires)//2]]))
xint = int(x, 2)
print("", x, xint)
y = ''.join(aoc.mapstr([v for _,v in sorted(wires.items())[len(wires)//2:]]))
yint = int(y,2)
print("", y, yint)
correctSum = xint+yint
print(format(correctSum, 'b'))

reversedGates = {}
for gate in gatesStrs.split("\n"): # x00 AND y00 -> z00
    first, func, second, _, output = gate.split()
    gates.add((first, func, second, output))
    reversedGates[output] = [first, func, second]

while gates:
    toDelete = []
    for gate in gates:
        first, func, second, output = gate
        if first in wires and second in wires:
            # print(first, func, second)
            wires[output] = funcMap[func](wires[first],wires[second])
            toDelete.append(gate)
    for g in toDelete:
        gates.remove(g)

total = 0
for wire, val in sorted(wires.items(), reverse=True):
    if wire[0] == "z":
        total <<= 1
        total |= val
print(format(total, "b"), total)

i = 0
from collections import deque
while total != 0:
    # if (total%2 ^ correctSum%2) != 0:
    print(i)
    q = deque(["z"+ format(i, '02')])
    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            print(curr, end=" ")
            if curr not in reversedGates:
                continue
            q.extend(reversedGates[curr])
        print()
    i += 1
    if i > 3:
        exit()
    total >>= 1
    correctSum >>= 1



# # Part 1
# funcMap = {
#     "AND": lambda x,y: x&y,
#     "OR": lambda x,y: x|y,
#     "XOR": lambda x,y: x^y
# }

# wires = {}
# gates = set()

# for line in initial.split("\n"):
#     wire, val = line.split(": ")
#     wires[wire] = int(val)

# for gate in gatesStrs.split("\n"): # x00 AND y00 -> z00
#     first, func, second, _, output = gate.split()
#     gates.add((first, func, second, output))

# while gates:
#     toDelete = []
#     for gate in gates:
#         first, func, second, output = gate
#         if first in wires and second in wires:
#             wires[output] = funcMap[func](wires[first],wires[second])
#             toDelete.append(gate)
#     for g in toDelete:
#         gates.remove(g)

# total = 0
# for wire, val in sorted(wires.items(), reverse=True):
#     if wire[0] == "z":
#         total <<= 1
#         total |= val
# print(total)