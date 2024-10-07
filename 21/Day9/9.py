# Part 2

grid = []
with open("input9") as f:
    for line in f:
        grid.append(list(map(int, [x for x in line.strip()])))

def inBasin(i, j):
    return grid[i][j] != 9 and grid[i][j] != -1

sizes = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if inBasin(i, j):
            stack = [(i, j)]
            size = 0
            while stack:
                currI, currJ = stack.pop()
                if inBasin(currI, currJ):
                    size += 1
                    # print(grid[currI][currJ])
                    grid[currI][currJ] = -1
                if currI > 0 and inBasin(currI-1, currJ):
                    stack.append((currI-1, currJ))
                if currJ > 0 and inBasin(currI, currJ-1):
                    stack.append((currI, currJ-1))
                if currJ < len(grid[0])-1 and inBasin(currI, currJ+1):
                    stack.append((currI, currJ+1))
                if currI < len(grid)-1 and inBasin(currI+1, currJ):
                    stack.append((currI+1, currJ))
            sizes.append(size)

print(sizes)

sizes = sorted(sizes)
print(sizes[-1]*sizes[-2]*sizes[-3])













# Part 1
# grid = []
#
# def printGrid(grid):
#     for row in grid:
#         print(row)
#
# with open("input9") as f:
#     for line in f:
#         grid.append(list(map(int, [x for x in line.strip()])))
#     printGrid(grid)
#
# riskLevel = 0
# for i in range(len(grid)):
#     for j in range(len(grid[i])):
#         lowPoint = True
#         curr = grid[i][j]
#         lowPoint &= curr < grid[i-1][j] if i > 0 else True
#         lowPoint &= curr < grid[i][j-1] if j > 0 else True
#         lowPoint &= curr < grid[i][j+1] if j < len(grid[0])-1 else True
#         lowPoint &= curr < grid[i+1][j] if i < len(grid)-1 else True
#         riskLevel += curr + 1 if lowPoint else 0
#
# print(riskLevel)
