import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

input = aoc.getInput("input")
# input = aoc.getInput("test-input")

import re

# Part 1
total = 0
for line in input:
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line)
    for m1,m2 in matches:
        total += int(m1) * int(m2)
print(total)


# Part 2
total = 0
do = True
for line in input:
    matches = re.findall(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", line)
    # print(matches)

    for match in matches:
        if match == "don't()":
            do = False
        elif match == "do()":
            do = True
        elif do:
            n = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", match)[0]
            print(n)
            total += int(n[0])*int(n[1])

print(total)

