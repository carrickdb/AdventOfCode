import aoc

## Part 2

def getLoad(gridmap):
    total = 0
    i = len(gridmap)
    while i > 0:
        total += i*sum([1 if x=="O" else 0 for _, x in gridmap[i].items()])
        i -= 1
    return total

def doSpinCycle(gridmap):
    for _ in range(4):
        # north, then west, then south, then east
        for j in range(len(gridmap[1])):
            newCol = []
            dots = 0
            i = len(gridmap)
            while i > 0:
                curr = gridmap[i][j]
                if curr == "#":
                    for _ in range(dots):
                        newCol.append(".")
                    dots = 0
                    newCol.append("#")
                elif curr == "O":
                    newCol.append("O")
                else:
                    dots += 1
                i -= 1
            for _ in range(dots):
                newCol.append(".")
            for i in range(len(newCol)):
                gridmap[len(gridmap)-i][j] = newCol[i]
        newGridmap = {}
        for i in range(len(gridmap)):
            for j in range(len(gridmap[1])):
                newRowI = len(gridmap[1])-j
                if newRowI not in newGridmap:
                    newGridmap[newRowI] = {}
                newGridmap[newRowI][i] = gridmap[i+1][j]

        gridmap = newGridmap
    return gridmap


grid = []
with open("input") as f:
    for l in f:
        grid.append(list(l.strip()))

gridmap = {}
rownum = len(grid)
for row in grid:
    rowmap = {}
    for j in range(len(row)):
        rowmap[j] = row[j]
    gridmap[rownum] = rowmap
    rownum -= 1

prev = {}
prevrev = {}
it = 0
cycles = 1000000000
skipped = False
while it < cycles:
    key = []
    for i in sorted(gridmap.keys()):
        row = []
        for j in sorted(gridmap[i].keys()):
            row.append(gridmap[i][j])
        key.append(''.join(row))
    key = ''.join(key)
    if key in prev and not skipped:
        seen = prev[key]
        mod = it-seen
        cyclesleft = (cycles - seen) % (mod)
        it = cycles-cyclesleft+1
        skipped = True
    else:
        prev[key] = it
        prev[it] = key
        it += 1
    gridmap = doSpinCycle(gridmap)
aoc.printMapGrid(gridmap)
print(getLoad(gridmap))


## Part 1

grid = []
with open("input") as f:
    for l in f:
        grid.append(l.strip())

gridmap = {}
rownum = len(grid)
for row in grid:
    gridmap[rownum] = row
    rownum -= 1

def getSubtotal(rock, numFound):
    gausstotal = (rock*(rock-1))//2
    minigausstotal = ((rock-numFound)*(rock-numFound-1))//2
    subtotal = gausstotal - minigausstotal
    return subtotal

total = 0
for j in range(len(gridmap[1])):
    rock = len(gridmap)+1
    numFound = 0
    i = len(gridmap)
    while i > 0:
        curr = gridmap[i][j]
        if curr == "#":
            total += getSubtotal(rock, numFound)
            numFound = 0
            rock = i
        elif curr == "O":
            numFound += 1
        i -= 1
    total += getSubtotal(rock, numFound)

print(total)