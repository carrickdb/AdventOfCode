import sys, os
from functools import cache

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

input = aoc.getInput("input")
# input = aoc.getInput("test-input")
# input = aoc.getInput("test-input2")

@cache
def dfs(s, i, bs):
    if i >= len(s):
        return None
    if bs == 0:
        return int(max(s[i:]))
    option1 = dfs(s, i+1, bs)
    option2 = dfs(s, i+1, bs - 1)
    if option2 != None:
        option2 += int(s[i])*10**bs
        if option1 == None:
            return option2
        return max(option1, option2)
    return option1


# def dfs(s, i, bs):
#     if i >= len(s):
#         return None
#     if bs == 0:
#         return int(max(s[i:]))
#     o1 = dfs(s, i+1, bs)
#     o2 = dfs(s, i+1, bs - 1)
#     if o2:
#         o2 += int(s[i])*(10**bs)





t = 0
for bank in input:
    subtotal = dfs(bank.strip(), 0, 11)
    print(subtotal)
    t += subtotal

print(t)


# wrong: 170520923035030



# t = 0
# for bank in input:
#     lb = len(bank)
#     joltage = 0
#     for i in range(lb):
#         for j in range(i+1, lb):
#             joltage = max(joltage, int(bank[i]+bank[j]))
#     t += joltage

# print(t)
