import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

input = aoc.getInput("input")
# input = aoc.getInput("test-input")
# input = aoc.getInput("test-input2")

# Part 2:
ranges = input[0].split(",")
invalid = 0
for r in ranges:
    s,e = list(map(int, r.split("-")))
    for i in range(s,e+1):
        istr = str(i)
        li = len(istr)
        for j in range(li//2):
            newstr = istr[:j+1] * (li//(j+1))
            # print(newstr)
            if istr == newstr:
                # print(j)
                invalid += i
                break

print(invalid)



# # Part 1:
# ranges = input[0].split(",")
# invalid = 0
# for r in ranges:
#     s,e = list(map(int, r.split("-")))
#     for i in range(s,e+1):
#         istr = str(i)
#         li= len(istr)
#         if (li % 2 == 0) and (istr[:li//2] == istr[li//2:]):
#             invalid += i

# print(invalid)