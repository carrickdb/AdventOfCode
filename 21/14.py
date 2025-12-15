
replacements = {}
with open("input14") as f:
    template = f.readline().strip()
    f.readline()
    for line in f:
        pair, insertion = line.strip().split(' -> ')
        replacements[pair] = insertion

counts = {}
for char in template:
    if char in counts:
        counts[char] += 1
    else:
        counts[char] = 1

pairs = {}
for i in range(len(template)-1):
    if template[i:i+2] in pairs:
        pairs[template[i:i+2]] += 1
    else:
        pairs[template[i:i+2]] = 1

# print(pairs)
# print(counts)

for i in range(40):
    newPairs = {}
    for pair, pairCount in [(k, v) for k, v in pairs.items()]:
        # print("pair, pairCount:", pair, pairCount)
        newChar = replacements[pair]
        # print("newChar", newChar)
        if newChar in counts:
            counts[newChar] += pairCount
        else:
            counts[newChar] = pairCount
        newPair1 = pair[0]+newChar
        newPair2 = newChar+pair[1]
        # print("new pairs:", newPair1, newPair2)
        if newPair1 in newPairs:
            newPairs[newPair1] += pairCount
        else:
            newPairs[newPair1] = pairCount
        if newPair2 in newPairs:
            newPairs[newPair2] += pairCount
        else:
            newPairs[newPair2] = pairCount
    pairs = newPairs

# print(pairs)
# print(counts)

maxNum = 0
minNum = float("inf")
for _, num in counts.items():
    maxNum = max(maxNum, num)
    minNum = min(minNum, num)

print(maxNum - minNum)
