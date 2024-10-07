def getRating(numbers, index, mostCommon=True):
    if len(numbers) == 1:
        return numbers[0]
    start = 0
    end = len(numbers) - 1
    while start < end:
        while start < end and numbers[start][index] == "1":
            start += 1
        while start < end and numbers[end][index] == "0":
            end -= 1
        if start < end:
            tmp = numbers[start]
            numbers[start] = numbers[end]
            numbers[end] = tmp
    split = 0
    while numbers[split][index] == "1":
        split += 1
    threshold = len(numbers) // 2 + (len(numbers) % 2 != 0)
    if start >= threshold:
        if mostCommon:
            return getRating(numbers[:split], index+1)
        return getRating(numbers[split:], index+1, mostCommon)
    else:
        if mostCommon:
            return getRating(numbers[split:], index+1)
        return getRating(numbers[:split], index+1, mostCommon)
"""
11001
11110
10110
10111
10101
10000
11100
> > 00111
01111
00100
00010
01010
"""

numbers = []
with open("input3") as f:
    for line in f:
        numbers.append(line.strip())

oxygenGeneratorRating = getRating(numbers, 0)
print("oxygenGeneratorRating", oxygenGeneratorRating)
CO2ScrubberRating = getRating(numbers, 0, False)
print("CO2ScrubberRating", CO2ScrubberRating)
print(int(oxygenGeneratorRating, 2) * int(CO2ScrubberRating, 2))



with open("input3", 'r') as f:
    numLines = 1
    line = f.readline().strip()
    counts = list(map(int, list(line.strip())))
    strlen = len(counts)
    for line in f:
        numLines += 1
        currCounts = list(map(int, list(line.strip())))
        for i in range(strlen):
            counts[i] += currCounts[i]

threshold = numLines // 2 + (numLines % 2 != 0)

gamma = ["1" if count >= threshold else "0" for count in counts]
gamma = int("".join(gamma), 2)
mask = ~(-1 << strlen)
print("solution:", gamma * (~gamma & mask))
