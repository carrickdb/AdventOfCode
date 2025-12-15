import aoc

## Part 2

total = 0
with open("input") as f:
    for l in f:
        seq = list(map(int, l.strip().split()))
        newseq = []
        firstNums = []
        while not all([x==0 for x in seq]):
            for i in range(len(seq)-1):
                newseq.append(seq[i+1]-seq[i])
            firstNums.append(seq[0])
            seq = newseq
            newseq = []
        s = 0
        lenf = len(firstNums)
        print(firstNums)
        for i in range(lenf):
            s = firstNums[lenf-1-i] -s
        total += s

print(total)


## Part 1

total = 0
with open("input") as f:
    for l in f:
        seq = list(map(int, l.strip().split()))
        newseq = []
        lastNums = []
        while not all([x==0 for x in seq]):
            for i in range(len(seq)-1):
                newseq.append(seq[i+1]-seq[i])
            lastNums.append(seq[-1])
            seq = newseq
            newseq = []
        total += sum(lastNums)

print(total)
