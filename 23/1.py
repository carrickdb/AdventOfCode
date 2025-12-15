import aoc

with open("input") as f:
    input = f.read()

## Part 2

numlist = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
total = 0
for l in input.split():
    nums = []
    for i in range(len(l)):
        x = l[i]
        if x.isdigit():
            nums.append(x)
            continue
        for j in range(len(numlist)):
            numStr = numlist[j]
            currstr = l[i:i+len(numStr)]
            if currstr == numStr:
                nums.append(str(j))
                break
    newnum = int(nums[0]+nums[-1])
    total += newnum

print(total)



## Part 1

total = 0
for l in input.split():
    nums = [x for x in l.strip() if x.isdigit()]
    total += int(nums[0]+nums[-1])
print(total)
