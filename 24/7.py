import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

input = aoc.getInput("input")
# input = aoc.getInput("test-input")

# Part 2
def compute(nums):
    curr = nums[0]
    if len(nums) == 1:
        return [curr]
    res = []
    for output in compute(nums[1:]):
        res.extend([curr + output, curr * output, int(str(output) + str(curr))])
    return res

total = 0
for line in input:
    res, nums = line.split(": ")
    res = int(res)
    nums = list(map(int, nums.split()))
    for output in compute(nums[::-1]):
        if res == output:
            total += res
            break

print(total)


# Part 1
def compute(nums):
    curr = nums[0]
    if len(nums) == 1:
        return [curr]
    res = []
    for output in compute(nums[1:]):
        res.extend([curr + output, curr * output])
    return res

total = 0
for line in input:
    res, nums = line.split(": ")
    res = int(res)
    nums = list(map(int, nums.split()))
    for output in compute(nums[::-1]):
        if res == output:
            total += res
            break
    # exit()

print(total)
