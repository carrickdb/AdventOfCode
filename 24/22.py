import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc
from collections import defaultdict

stuff = aoc.getInput(os.getenv("HOME") + "/Desktop/input")
# stuff = aoc.getInput("test-input")
stuff = aoc.mapint(stuff)

PRUNE = 16777216  # 2^24 keep last 24 digits
def getNextSecretNumber(num):
    num = (num ^ (num * 64)) % PRUNE  # << 6
    num = (num ^ (num//32)) % PRUNE   # >> 5
    num = (num ^ (num*2048)) % PRUNE  # << 11
    return num

m = defaultdict(int)
total = 0
for num in stuff:
    seed = num
    seen = set()
    changes = []
    for _ in range(2000):
        prev = num
        num = getNextSecretNumber(num)
        currLastDigit = num%10
        c = currLastDigit - (prev%10)
        if len(changes) < 4:
            changes.append(c)
        else:
            changes = changes[1:]+[c]
        if len(changes) == 4:
            tchanges = tuple(changes)
            if tchanges in seen:
                continue
            seen.add(tchanges)
            m[tchanges] += currLastDigit

    total += num

maxPattern = None
maxTotal = 0
for k,v in m.items():
    if v > maxTotal:
        maxPattern = k
        maxTotal = v

print(maxPattern, maxTotal)