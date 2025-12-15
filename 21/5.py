# Part 2:

from math import inf

lowestx = inf
lowesty = inf
highestx = -inf
highesty = -inf

coordinates = []
with open("input5") as f:
    for line in f:
        start_coordinates, end_coordinates = line.strip().split(" -> ")
        startx, starty = map(int, start_coordinates.split(","))
        endx, endy = map(int, end_coordinates.split(","))
        if startx == endx:
            miny = min(starty, endy)
            endy = max(starty, endy)
            starty = miny
        elif starty == endy:
            minx = min(startx, endx)
            endx = max(startx, endx)
            startx = minx
        else:
            if startx > endx:
                tmpx, tmpy = startx, starty
                startx, starty = endx, endy
                endx, endy = tmpx, tmpy
        coordinates.append(((startx, starty), (endx, endy)))
        lowestx = min(lowestx, startx)
        lowesty = min(lowesty, starty)
        highestx = max(highestx, endx)
        highesty = max(highesty, endy)

grid = [[0 for i in range(highestx - lowestx + 1)] for j in range(highesty - lowesty + 1)]
# print(lowestx, highestx)
# print(lowesty, highesty)
# print(grid)

overlaps = 0
# print("len(coordinates)", len(coordinates))
for start, end in coordinates:
    # print(start, end)
    startx, starty = start
    endx, endy = end
    if startx == endx:
        for i in range(starty-lowesty, endy-lowesty + 1):
            grid[i][startx-lowestx] += 1
            if grid[i][startx-lowestx] == 2:
                overlaps += 1
    elif starty == endy:
        for i in range(startx-lowestx, endx-lowestx + 1):
            grid[starty-lowesty][i] += 1
            if grid[starty-lowesty][i] == 2:
                overlaps += 1
        # for row in grid:
        #     print(row)
        # print()
    else:
        if starty > endy:
            for i in range(endx-startx+1):
                grid[starty-lowesty-i][startx-lowestx+i] += 1
                if grid[starty-lowesty-i][startx-lowestx+i] == 2:
                    overlaps += 1
        else:
            for i in range(endx-startx+1):
                grid[starty-lowesty+i][startx-lowestx+i] += 1
                if grid[starty-lowesty+i][startx-lowestx+i] == 2:
                    overlaps += 1

print(overlaps)


# Part 1:

from math import inf

lowestx = inf
lowesty = inf
highestx = -inf
highesty = -inf

coordinates = []
with open("input5") as f:
    for line in f:
        start_coordinates, end_coordinates = line.strip().split(" -> ")
        startx, starty = map(int, start_coordinates.split(","))
        endx, endy = map(int, end_coordinates.split(","))
        if startx == endx:
            miny = min(starty, endy)
            endy = max(starty, endy)
            starty = miny
        elif starty == endy:
            minx = min(startx, endx)
            endx = max(startx, endx)
            startx = minx
        else:
            continue
        coordinates.append(((startx, starty), (endx, endy)))
        lowestx = min(lowestx, startx)
        lowesty = min(lowesty, starty)
        highestx = max(highestx, endx)
        highesty = max(highesty, endy)

grid = [[0 for i in range(highestx - lowestx + 1)] for j in range(highesty - lowesty + 1)]
# print(lowestx, highestx)
# print(lowesty, highesty)
# print(grid)

overlaps = 0
# print("len(coordinates)", len(coordinates))
for start, end in coordinates:
    # print(start, end)
    startx, starty = start
    endx, endy = end
    if startx == endx:
        for i in range(starty-lowesty, endy-lowesty + 1):
            grid[i][startx-lowestx] += 1
            if grid[i][startx-lowestx] == 2:
                overlaps += 1
    elif starty == endy:
        for i in range(startx-lowestx, endx-lowestx + 1):
            grid[starty-lowesty][i] += 1
            if grid[starty-lowesty][i] == 2:
                overlaps += 1
        # for row in grid:
        #     print(row)
        # print()
    else:
        assert False

print(overlaps)





# def getOverlap(i, start, end, intervalsList, perpendicularIntervals):
#     overlap = 0
#     if i not in intervals:
#         intervalsList[i] = [[start, end]]
#     else:
#         # TODO: replace with binary search
#         collision = None
#         intervals = intervalsList[i]
#         for j in range(len(intervals)):
#             intervalStart, intervalEnd = intervals[j]
#             if end < intervalStart or start > intervalEnd:
#                 continue
#             collision = j
#             overlap += min(intervalEnd, end) - max(intervalStart, start)
#             break
#         intervals[collision][0] = [min(intervalStart, start)]
#         intervals[collision][1] = [max(intervalEnd, end)]
#         collision += 1
#         while collision < len(intervals) and end >= intervals[collision][1]:
#             del intervals[collision]
#
#         # now get the intersections with perpendicular lines
#
#     return overlap
#
# horizIntervals = {}
# vertIntervals = {}
# overlap = 0
# with open("input") as f:
#     for line in f:
#         start_coordinates, end_coordinates = line.strip().split(" -> ")
#         startx, starty = map(int, start_coordinates.split(","))
#         endx, endy = map(int, end_coordinates.split(","))
#         if startx == endx: # vertical
#             overlap += getOverlap(startx, min(starty, endy), max(starty, endy), vertIntervals, horizIntervals)
#         elif starty == endy: # horizontal
#             overlap += getOverlap(starty, min(startx, endx), max(startx, endx), horizIntervals, vertIntervals)
#
# print(overlap)
#         # else: ignore
