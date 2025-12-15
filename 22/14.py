paths = []

maxx = float("-inf")
maxy = float("-inf")

with open("input") as f:
    for line in f:
        # 529,71 -> 529,72 -> 539,72 -> 539,71
        curr = line.strip().split(" -> ")
        pairs = []
        for pair in curr:
            intPair = list(map(int, pair.split(",")))
            maxx = max(maxx, intPair[0])
            maxy = max(maxy, intPair[1])
            pairs.append(intPair)
        paths.append(pairs)

width = maxx + 1000
height = maxy + 3

cave = [["." for _ in range(width)] for j in range(height-1)]
cave.append(["#" for _ in range(width)])

def sign(a, b):
    if a-b < 0:
        return -1
    return 1

for path in paths:
    for i in range(1, len(path)):
        startx, starty = path[i-1]
        nextx, nexty = path[i]
        currx = startx
        curry = starty
        if startx == nextx:
            for j in range(abs(starty-nexty)+1):
                cave[curry][currx] = "#"
                curry += 1*sign(nexty, starty)
        else:
            for j in range(abs(startx-nextx)+1):
                cave[curry][currx] = "#"
                currx += 1*sign(nextx, startx)

def printCave(cave):
    for row in cave:
        print(''.join(row))

# printCave(cave)
# exit()

numSand = 1
while True:
    sandx = 500
    sandy = 0
    if cave[sandy][sandx] == 'o':
        print(numSand)
        exit()
    while True:
        if sandy + 1 >= height:
            print(numSand)
            exit()
        if cave[sandy+1][sandx] == ".":
            sandy += 1
        else:
            if sandx-1 < 0:
                print(numSand)
                exit()
            if cave[sandy+1][sandx-1] == '.':
                sandy += 1
                sandx -= 1
            else:
                if sandx+1 >= width:
                    print(numSand)
                    exit()
                if cave[sandy+1][sandx+1] == '.':
                    sandy += 1
                    sandx += 1
                else:
                    cave[sandy][sandx] = 'o'
                    break
    numSand += 1



# paths = []
#
# maxx = float("-inf")
# minx = float("inf")
# maxy = float("-inf")
#
# with open("input") as f:
#     for line in f:
#         # 529,71 -> 529,72 -> 539,72 -> 539,71
#         curr = line.strip().split(" -> ")
#         pairs = []
#         for pair in curr:
#             intPair = list(map(int, pair.split(",")))
#             maxx = max(maxx, intPair[0])
#             minx = min(minx, intPair[0])
#             maxy = max(maxy, intPair[1])
#             pairs.append(intPair)
#         paths.append(pairs)
#
# cave = [["." for _ in range(maxx-minx+1)] for j in range(maxy+1)]
#
# def sign(a, b):
#     if a-b < 0:
#         return -1
#     return 1
#
# for path in paths:
#     for i in range(1, len(path)):
#         startx, starty = path[i-1]
#         startx -= minx
#         nextx, nexty = path[i]
#         nextx -= minx
#         currx = startx
#         curry = starty
#         if startx == nextx:
#             for j in range(abs(starty-nexty)+1):
#                 cave[curry][currx] = "#"
#                 curry += 1*sign(nexty, starty)
#         else:
#             for j in range(abs(startx-nextx)+1):
#                 cave[curry][currx] = "#"
#                 currx += 1*sign(nextx, startx)
#
# def printCave(cave):
#     for row in cave:
#         print(''.join(row))
#
# # printCave(cave)
# # exit()
#
# width = maxx - minx + 1
# height = maxy + 1
# numSand = 1
# while True:
#     sandx = 500-minx
#     sandy = 0
#     while True:
#         if sandy + 1 >= height:
#             print(numSand)
#             exit()
#         if cave[sandy+1][sandx] == ".":
#             sandy += 1
#         else:
#             if sandx-1 < 0:
#                 print(numSand)
#                 exit()
#             if cave[sandy+1][sandx-1] == '.':
#                 sandy += 1
#                 sandx -= 1
#             else:
#                 if sandx+1 >= width:
#                     print(numSand)
#                     exit()
#                 if cave[sandy+1][sandx+1] == '.':
#                     sandy += 1
#                     sandx += 1
#                 else:
#                     cave[sandy][sandx] = 'o'
#                     break
#     numSand += 1
#     # if numSand == 23:
#     #     printCave(cave)
#     #     print()
#     #     exit()
