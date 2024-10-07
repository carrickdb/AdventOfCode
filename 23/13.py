import aoc

counts = [(1, 7), (0, 5), (1, 12), (1, 8), (1, 1), (0, 13), (0, 1), (1, 4), (1, 3), (0, 12), (1, 16), (1, 2), (0, 4), (0, 5), (0, 1), (1, 1), (0, 2), (1, 3), (0, 3), (1, 1), (0, 1), (0, 1), (0, 7), (0, 6), (0, 6), (1, 7), (0, 14), (0, 16), (1, 4), (1, 13), (1, 9), (1, 10), (0, 2), (1, 16), (0, 15), (0, 8), (1, 1), (0, 1), (1, 14), (0, 12), (1, 3), (1, 12), (0, 11), (0, 12), (1, 10), (0, 12), (0, 3), (0, 14), (1, 8), (1, 1), (0, 14), (1, 12), (0, 4), (1, 14), (1, 12), (1, 11), (0, 1), (1, 10), (0, 16), (1, 10), (0, 1), (0, 12), (1, 12), (1, 1), (1, 4), (1, 3), (0, 7), (0, 12), (1, 10), (1, 3), (1, 3), (0, 1), (1, 1), (0, 1), (1, 6), (0, 16), (1, 1), (0, 5), (1, 5), (1, 1), (0, 2), (1, 4), (1, 1), (0, 1), (0, 13), (1, 3), (0, 7), (1, 12), (0, 12), (0, 1), (1, 1), (1, 10), (1, 2), (1, 9), (1, 5), (0, 6), (1, 3), (1, 16), (1, 1), (0, 2)]
# counts = [(0, 5), (1, 4)]

def getCount(grid, prev):
    w = len(grid[0])
    for l in range(1,w):
        found = True
        r = min(l, w-l)
        for row in grid:
            mirror = list(reversed(row[l:r+l]))
            if row[l-r:l] != mirror:
                found = False
                break
        if found and (prev==None or l != prev):
            return l
    return None

total = 0
mapnum = 0
with open("input") as f:
    currmap = []
    for l in f:
        if l == "\n":
            count = None
            for n in range(len(currmap)):
                for m in range(len(currmap[0])):
                    before = currmap[n][m]
                    if before == "#":
                        currmap[n][m] = "."
                    else:
                        currmap[n][m] = "#"
                    prev = None if counts[mapnum][0] == 1 else counts[mapnum][1]
                    count = getCount(currmap, prev)
                    if not count:
                        newmap = []
                        for j in range(len(currmap[0])):
                            newmap.append([currmap[i][j] for i in range(len(currmap))])
                        prev = None if counts[mapnum][0] == 0 else counts[mapnum][1]
                        count = getCount(newmap, prev)
                        if count:
                            count *= 100
                    currmap[n][m] = before
                    if count:
                        break
                if count:
                    break
            if not count:
                print("something went wrong")
                exit()
            total += count
            currmap = []
            mapnum += 1
        else:
            currmap.append(list(l.strip()))

print(total)


def getCount(grid):
    w = len(grid[0])
    # print(w)
    for l in range(1,w):
        found = True
        r = min(l, w-l)
        for row in grid:
            mirror = ''.join(reversed(row[l:r+l]))
            if row[l-r:l] != mirror:
                found = False
                break
        if found:
            return l
    return None

total = 0
counts = []
with open("input2") as f:
    currmap = []
    for l in f:
        if l == "\n":
            count = getCount(currmap)
            # print("count", count)
            if not count:
                newmap = []
                for j in range(len(currmap[0])):
                    newmap.append(''.join([currmap[i][j] for i in range(len(currmap))]))
                count = getCount(newmap)
                if not count:
                    print("something went wrong")
                    exit()
                counts.append((1,count))
                count *= 100
            else:
                counts.append((0, count))
            total += count
            currmap = []
        else:
            currmap.append(l.strip())

print(total)
print(counts)
