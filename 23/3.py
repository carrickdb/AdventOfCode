import aoc

total = 0
grid = []
with open("input") as f:
    for l in f:
        grid.append(list(l.strip()))

for i in range(len(grid)):
    row = grid[i]
    for j in range(len(row)):
        c = row[j]
        if c == "*":
            nums = []
            newGrid = grid[max(0, i-1):min(len(grid), i+2)].copy()
            ni = 1
            if i-1 < 0:
                ni = 0
            for di, dj in aoc.diagDirs:
                ip = ni+di
                if ip < 0 or ip >= len(newGrid):
                    continue
                jp = j+dj
                if jp < 0 or jp >= len(newGrid[0]):
                    continue
                newSpace = newGrid[ip][jp]
                if newSpace.isdigit():
                    beginning = jp
                    end = jp
                    while beginning >= 0 and newGrid[ip][beginning].isdigit():
                        beginning -= 1
                    while end < len(grid[0]) and newGrid[ip][end].isdigit():
                        end += 1
                    nums.append(int(''.join(newGrid[ip][beginning+1:min(len(grid[0]), end)])))
                    for k in range(beginning+1, end):
                        newGrid[ip][k] = '.'
            if len(nums) == 2:
                total += nums[0] * nums[1]
                
print(total)


## Part 1

total = 0
grid = []
with open("input") as f:
    for l in f:
        grid.append(l.strip())

for i in range(len(grid)):
    row = grid[i]
    currNum = ""
    partNumber = False
    for j in range(len(row)):
        c = row[j]
        if c.isdigit():
            currNum += c
            if partNumber == False:
                for di, dj in aoc.diagDirs:
                    ip = i+di
                    jp = j+dj
                    if ip < 0 or ip >= len(grid):
                        continue
                    if jp < 0 or jp >= len(grid[0]):
                        continue
                    newSpace = grid[ip][jp]
                    if not newSpace.isdigit() and newSpace != ".":
                        partNumber = True
                        break
        elif currNum != "":
            if partNumber:
                total += int(currNum)
                partNumber = False
            currNum = ""
    if partNumber:
        total += int(currNum)


print(total)