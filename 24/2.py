import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

input = aoc.getInput("input")
# input = aoc.getInput("test-input")
safe = 0
for line in input:
    for j in range(len(line)+1):
        l = list(map(int, line.split()))
        if j < len(l):
            del l[j]
        ok = True
        inc = None
        problem = None
        for i in range(len(l)-1):
            diff = abs(l[i]-l[i+1])
            if inc == None:
                inc = l[i] < l[i+1]
            elif inc != (l[i] < l[i+1]):
                ok = False
                problem = i
                break
            ok &= (diff >= 1) and (diff <=3)
        if ok:
            break
    safe += ok

print(safe)