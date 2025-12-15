import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

inputFile = os.getenv("HOME") + "/Desktop/input"
# inputFile = "test-input"

with open(inputFile) as f:
    stuff = f.read().split("\n\n")

keys = []
locks = []
pin = "#"

for schematic in stuff:
    isLock = schematic[:5] == pin*5
    lk = aoc.transpose(schematic.split("\n"))
    heights = [lk[i].count(pin) for i in range(len(lk))]
    if isLock:
        locks.append(heights)
    else:
        keys.append(heights)

# print(locks)
# print(keys)

pairs = 0
for key in keys:
    for lock in locks:
        pairs += all([key[i]+lock[i] <= 7 for i in range(len(key))])

print(pairs)



