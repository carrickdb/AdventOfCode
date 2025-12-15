import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

# input = aoc.getInput("test-input")
input = aoc.getInput("input")

total = 0
for l in input:
    l = list(map(int, l.split()))
    done = False
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            li,lj = l[i], l[j]
            q1, q2 = li // lj, lj//li
            if q1*lj == li:
                total += q1
                # print(q1)
                done = True
                break
            if q2 * li == lj:
                total += q2
                # print(q2)
                done = True
                break
        if done: break
print(total)


# total = 0
# for l in input:
#     l = list(map(int, l.split()))
#     total += max(l) - min(l)
# print(total)