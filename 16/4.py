import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

from collections import Counter
from functools import cmp_to_key

input = aoc.getInput("input")
# input = aoc.getInput("test-input")

for l in input:
    # aaaaa-bbb-z-y-x-123[abxyz]
    a,b = l.split("[")
    cs = b[:-1]
    a = a.split("-")
    ct, id = a[:-1], int(a[-1])
    c = Counter()
    for s in ct:
        c.update(s)

    def cmp(x, y):
        if x[1] == y[1]:
            return ord(x[0]) - ord(y[0])
        return y[1] - x[1]
    c = sorted([(i,j) for i,j in c.items()], key=cmp_to_key(cmp))
    if cs == ''.join([x[0] for x in c[:5]]):
    # ct, id = ["qzmt", "zixmtkozy", "ivhz"], 343
        for w in ct:
            curr = list(w)
            for i in range(len(curr)):
                curr[i] = chr(ord('a') + (((ord(curr[i]) - ord('a')) + id ) % 26))
            if ''.join(curr) == "northpole":
                print(id)


# from collections import Counter
# from functools import cmp_to_key

# input = aoc.getInput("input")
# # input = aoc.getInput("test-input")

# total = 0
# for l in input:
#     # aaaaa-bbb-z-y-x-123[abxyz]
#     a,b = l.split("[")
#     cs = b[:-1]
#     a = a.split("-")
#     ct, id = a[:-1], int(a[-1])
#     c = Counter()
#     for s in ct:
#         c.update(s)

#     def cmp(x, y):
#         if x[1] == y[1]:
#             return ord(x[0]) - ord(y[0])
#         return y[1] - x[1]
#     c = sorted([(i,j) for i,j in c.items()], key=cmp_to_key(cmp))
#     if cs == ''.join([x[0] for x in c[:5]]):
#         total += id

# print(total)
