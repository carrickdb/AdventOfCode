import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

from collections import Counter

input = aoc.getInput("input")
# input = aoc.getInput("test-input")

total = 0
for l in input:
    strs = set()
    for w in l.split():
        w = ''.join(sorted(w))
        if w in strs:
            break
        strs.add(w)
    else:
        print(l)
        total += 1

print(total)

# print(sum([1 if all([x==1 for _, x in Counter(l.split()).items()]) else 0 for l in input]))