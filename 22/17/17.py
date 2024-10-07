import copy


with open("input") as f:
    gas = f.read().strip()

grid = [["#" for i in range(7)]]

def printGrid(grid, falling=None):
    g = copy.deepcopy(grid)
    if falling:
        for cx,cy in falling:
            while cy > len(g)-1:
                g.append(["." for _ in range(7)])
            g[cy][cx] = "@"
    for row in g[::-1]:
        print(''.join(row))
    input()

top = 0
height = 0
currJet = 0
i = 0
patterns = {}
patternLength = 0
while i < 1000000000000:
    if i % 5 == 0:
        curr = [(j, top+4) for j in range(2, 6)]
    elif i % 5 == 1:
        curr = [(j, top+5) for j in range(2, 5)]
        curr.append((3, top+4))
        curr.append((3, top+6))
    elif i % 5 == 2:
        curr = [(j, top+4) for j in range(2, 5)]
        curr.append((4, top+5))
        curr.append((4, top+6))
    elif i % 5 == 3:
        curr = [(2, top+j) for j in range(4, 8)]
    elif i % 5 == 4:
        curr = [(2, top+4), (3, top+4), (2, top+5), (3, top+5)]
    # printGrid(grid)
    canMoveDown = True
    while canMoveDown:
        dir = gas[currJet]
        currJet = (currJet + 1) % len(gas)
        if dir == "<":
            diff = -1
        else:
            diff = 1
        canMoveSideways = True
        newcoords = [(x+diff, y) for x, y in curr]
        for nx, ny in newcoords:
            if nx < 0 or nx >= 7 or (ny < len(grid) and grid[ny][nx] == "#"):
                canMoveSideways = False
                break
        if canMoveSideways:
            curr = newcoords
            # printGrid(grid, curr)
        newcoords = [(x, y-1) for x, y in curr]
        for nx, ny in newcoords:
            if nx < 0 or nx >= 7 or (ny < len(grid) and grid[ny][nx] == "#"):
                canMoveDown = False
                break
        if canMoveDown:
            curr = newcoords
            # printGrid(grid, curr)
        else:
            break
    for x, y in curr:
        while y > len(grid)-1:
            grid.append(["." for _ in range(7)])
        grid[y][x] = "#"
    top = len(grid) - 1
    i += 1
    if len(grid) > 10:
        snapshot = [''.join(grid[k]) for k in range(len(grid)-10, len(grid))]
        pattern = (currJet, i%5, tuple(snapshot))
        if pattern in patterns and patternLength == 0:
            print("pattern acquired")
            patternLength = top - patterns[pattern]
            # print(patternLength)
            # exit()
            height = 
        else:
            patterns[pattern] = top

print(height+top)





# """
# ####  0
#
# .#.   1
# ###
# .#.
#
# ..#   2
# ..#
# ###
#
# #     3
# #
# #
# #
#
# ##    4
# ##
# """
#
# with open("input2") as f:
#     gas = f.read().strip()
#
# grid = [["#" for i in range(7)]]
#
# def printRocks(grid):
#     for row in grid[::-1]:
#         print(''.join(row))
#
# top = 0
# currJet = 0
# for i in range(2022):
#     if i % 5 == 0:
#         curr = [(i, top+4) for i in range(2, 6)]
#     elif i % 5 == 1:
#         curr = [(i, top+5) for i in range(2, 5)]
#         curr.append((3, top+4))
#         curr.append((3, top+6))
#     elif i % 5 == 2:
#         curr = [(i, top+4) for i in range(2, 5)]
#         curr.append((4, top+5))
#         curr.append((4, top+6))
#     elif i % 5 == 3:
#         curr = [(2, top+i) for i in range(4, 8)]
#     elif i % 5 == 4:
#         curr = [(2, top+4), (3, top+4), (2, top+5), (3, top+5)]
#     canMoveDown = True
#     while canMoveDown:
#         dir = gas[currJet%len(gas)]
#         currJet += 1
#         if dir == "<":
#             diff = -1
#         else:
#             diff = 1
#         canMoveSideways = True
#         newcoords = [(x+diff, y) for x, y in curr]
#         for nx, ny in newcoords:
#             if nx < 0 or nx >= 7 or (ny < len(grid) and grid[ny][nx] == "#"):
#                 canMoveSideways = False
#                 break
#         if canMoveSideways:
#             curr = newcoords
#         newcoords = [(x, y-1) for x, y in curr]
#         for nx, ny in newcoords:
#             if nx < 0 or nx >= 7 or (ny < len(grid) and grid[ny][nx] == "#"):
#                 canMoveDown = False
#                 break
#         if canMoveDown:
#             curr = newcoords
#         else:
#             break
#     for x, y in curr:
#         while y > len(grid)-1:
#             grid.append(["." for _ in range(7)])
#         grid[y][x] = "#"
#     top = len(grid) - 1
#
# print(top)
