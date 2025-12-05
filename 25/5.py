import sys, os
from functools import cache

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc


with open("test-input") as f:
# with open("input") as f:
    input = f.read()

ints, queries = input.split('\n\n')
intervals = []
for i in ints.split('\n'):
    intervals.append(list(map(int, i.split('-'))))

intervals.sort()
mi = []
curr = 0
li = len(intervals)
# [7,8] [2,9]  6
# [2,9] [3,4]
while curr < li:
    s,e = intervals[curr]
    new = [s,e]
    next = curr + 1
    while next < li:
        s2,e2 = intervals[next]
        if s2 <= new[1]:
            new[1] = max(new[1],e2)
        else:
            break
        next += 1
    mi.append(new)
    curr = next

t = 0
for s,e in mi:
    t += e - s + 1
print(t)


# # with open("test-input") as f:
# with open("input") as f:
#     input = f.read()

# ints, queries = input.split('\n\n')
# intervals = []
# for i in ints.split('\n'):
#     intervals.append(list(map(int, i.split('-'))))

# intervals.sort()
# merged_intervals = []
# curr = 0
# li = len(intervals)
# # [7,8] [2,9]  6
# # [2,9] [3,4]
# while curr < li:
#     s,e = intervals[curr]
#     new = [s,e]
#     next = curr + 1
#     while next < li:
#         s2,e2 = intervals[next]
#         if s2 <= new[1]:
#             new[1] = max(new[1],e2)
#         else:
#             break
#         next += 1
#     merged_intervals.append(new)
#     curr = next

# t = 0
# import bisect
# # [2,3] [2,6]
# print(merged_intervals)
# for q in queries.split():
#     q = int(q)
#     i = bisect.bisect(merged_intervals, q, key=lambda x: x[0])
#     index = max(0,i-1)
#     t += merged_intervals[index][0] <= q <= merged_intervals[index][1]

# print(t)
