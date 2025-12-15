import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

# input = aoc.getInput("input")
input = aoc.getInput("test-input")

suffix = [17, 31, 73, 47, 23]
for i in input:
    a = []
    for c in i:
        a.append(ord(c))
    a.extend(suffix)

    l = [i for i in range(256)]

    skip = 0
    curr = 0
    lenl = len(l)
    for r in range(64):
        for length in a:
            end = curr+length
            if end <= lenl:
                l = l[:curr] + l[curr:end][::-1] + l[end:]
            else:
                d = l+l
                d = d[:curr] + d[curr:end][::-1] + d[end:]
                l = d[lenl:end] + d[end-lenl:lenl]
            curr = (curr+length+skip) % lenl
            skip += 1
    print()





# numElements = 256
# l = [i for i in range(numElements)]

# skip = 0
# curr = 0
# lenl = len(l)
# for length in input:
#     end = curr+length
#     if end <= lenl:
#         l = l[:curr] + l[curr:end][::-1] + l[end:]
#     else:
#         d = l+l
#         d = d[:curr] + d[curr:end][::-1] + d[end:]
#         l = d[lenl:end] + d[end-lenl:lenl]
#     curr = (curr+length+skip) % lenl
#     skip += 1
# print(l[0]*l[1])