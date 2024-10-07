def printGrid(g):
    for l in g:
        print(l)

galaxies = []

emptyRows = []
emptyCols = []
g = []
with open("input") as f:
    i = 0
    for l in f:
        l = l.strip()
        g.append(list(l))
        if all([x=="." for x in l]):
            emptyRows.append(i)
        else:
            galaxies.extend([(i, j) for j in range(len(l)) if l[j]=="#"])
        i += 1

newg = []
for j in range(len(g[0])):
    newRow = []
    for i in range(len(g)):
        newRow.append(g[i][j])
    newg.append(newRow)

i = 0
for l in newg:
    if all([x=="." for x in l]):
        emptyCols.append(i)
    i += 1

total = 0
totals = {}
for first in range(len(galaxies)):
    for other in range(first+1, len(galaxies)):
        n, m = galaxies[other]
        i, j = galaxies[first]
        temptotal = abs(i-n) + abs(j-m)
        minx = min(j,m)
        maxx = max(j,m)
        miny = min(i,n)
        maxy = max(i,n)
        for curr in emptyRows:
            if curr > miny and curr < maxy:
                temptotal += 1000000-1
        for curr in emptyCols:
            if curr > minx and curr < maxx:
                temptotal += 1000000-1
        total += temptotal
        totals[(first+1, other+1)] = temptotal

print(total)
print(len(galaxies))
