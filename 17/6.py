import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

input = aoc.getInput("input")
# input = aoc.getInput("test-input")

banks = list(map(int, input[0].split()))
lb = len(banks)
seen = set()
cycles = 0
start = None
while True:
    bank_tup = tuple(banks)
    if start == None and bank_tup in seen:
        start = bank_tup
        cycles = 0
    elif bank_tup == start:
        print(cycles)
        break
    seen.add(bank_tup)
    mi, m = None, float("-inf")
    for i, v in enumerate(banks):
        if v > m:
            mi = i
            m = v
    banks[mi] = 0
    base = m//lb
    for i in range(lb):
        banks[i] += base
    for i in range(m%lb):
        banks[(mi+1+i)%lb] += 1
    cycles += 1


# banks = list(map(int, input[0].split()))
# lb = len(banks)
# seen = set()
# cycles = 0
# while True:
#     bank_tup = tuple(banks)
#     if bank_tup in seen:
#         print(cycles)
#         break
#     seen.add(bank_tup)
#     mi, m = None, float("-inf")
#     for i, v in enumerate(banks):
#         if v > m:
#             mi = i
#             m = v
#     banks[mi] = 0
#     base = m//lb
#     for i in range(lb):
#         banks[i] += base
#     for i in range(m%lb):
#         banks[(mi+1+i)%lb] += 1
#     cycles += 1
