import aoc

## Part 2

numcards = 0
winningNumbers = {}
scratchcards = []
numcopies = {}
with open("input") as f:
    for l in f:
        id, nums = l.strip().split(": ")
        id = id.split()[1]
        winning, mine = nums.split(" | ")
        winning = set(map(int, winning.split()))
        mine = list(map(int, mine.split()))

        winningNumbers[int(id)] = winning
        scratchcards.append(mine)
    for i in range(len(scratchcards)):
        stack = []
        j = 1
        for num in scratchcards[i]:
            if num in winningNumbers[i+1]:
                stack.append(i+j)
                j += 1
        numcards += 1
        if i+1 not in numcopies:
            numcopies[i+1] = 0
        numcopies[i+1] += 1
        while stack:
            curr = stack.pop()
            j = 1
            for num in scratchcards[curr]:
                if num in winningNumbers[curr+1]:
                    stack.append(curr+j)
                    j += 1
            numcards += 1
            if curr+1 not in numcopies:
                numcopies[curr+1] = 0
            numcopies[curr+1] += 1

print(numcopies)
total = 0
for k in numcopies.values():
    total += k
print(total)
print(numcards)


## Part 1

points = 0
with open("input") as f:
    for l in f:
        _, nums = l.strip().split(": ")
        winning, mine = nums.split(" | ")
        winning = set(map(int, winning.split()))
        mine = list(map(int, mine.split()))
        curr = 0
        for m in mine:
            if m in winning:
                if curr == 0:
                    curr = 1
                else:
                    curr *= 2

        points += curr

print(points)