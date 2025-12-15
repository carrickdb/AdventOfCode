import sys, os
from functools import cache

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

input = aoc.getInput("input")
# input = aoc.getInput("test-input")
# input = aoc.getInput("test-input2")

# Part 2
rolls = 0

grid = aoc.gridify(input)
num_rows = len(grid)
num_cols = len(grid[0])

rolls_adj = {}
for i in range(num_rows):
    for j in range(num_cols):
        if grid[i][j] != "@":
            continue
        num_adj = 0
        for di,dj in aoc.diagDirs:
            ci,cj = i+di, j+dj
            if ci not in grid or cj not in grid[ci]:
                continue
            num_adj += grid[ci][cj] == "@"
        rolls_adj[(i,j)] = num_adj

import heapq
h = [(num, coord) for coord, num in rolls_adj.items()]
heapq.heapify(h)
while h[0][0] < 4:
    _, coord = heapq.heappop(h)
    if coord not in rolls_adj:
        continue
    del rolls_adj[coord]
    rolls += 1
    i,j = coord
    for di,dj in aoc.diagDirs:
        ci,cj = i+di, j+dj
        neighbor = (ci,cj)
        if neighbor not in rolls_adj:
            continue
        rolls_adj[neighbor] -= 1
        heapq.heappush(h, (rolls_adj[neighbor], neighbor))

print(rolls)



# Part 1
# rolls = 0

# grid = aoc.gridify(input)
# num_rows = len(grid)
# num_cols = len(grid[0])

# for i in range(num_rows):
#     for j in range(num_cols):
#         if grid[i][j] != "@":
#             continue
#         num_adj = 0
#         for di,dj in aoc.diagDirs:
#             ci,cj = i+di, j+dj
#             if ci not in grid or cj not in grid[ci]:
#                 continue
#             num_adj += grid[ci][cj] == "@"
#         if num_adj < 4:
#             rolls += 1
#             # print(f"{i}, {j} has {num_adj} adjacent")
# print(rolls)