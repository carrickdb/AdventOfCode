
def print_grid(grid):
    for row in grid:
        for col in row:
            print('{0:>3}'.format(col), end='')
        print()
    print()

grid = []
with open("input11") as f:
    for line in f:
        grid.append([int(x) for x in line.strip()])

# print_grid(grid)
def inBounds(grid, i, j):
    return not (i < 0 or j < 0 or j >= len(grid[0]) or i >= len(grid))

flashes = 0
day = 1
while True:
    stack = []
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] += 1
            if grid[i][j] > 9:
                stack.append((i, j))
                visited.add((i, j))
                flashes += 1
    # print_grid(grid)
    # print(stack)
    while stack:
        flashi, flashj = stack.pop()
        for deltai, deltaj in [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
            neighbori = flashi+deltai
            neighborj = flashj+deltaj
            if not inBounds(grid, neighbori, neighborj):
                continue
            grid[neighbori][neighborj] += 1
            if grid[neighbori][neighborj] > 9 and (neighbori, neighborj) not in visited:
                stack.append((neighbori, neighborj))
                visited.add((neighbori, neighborj))
                flashes += 1
        # print_grid(grid)
        # print(stack)
    allFlashed = True
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] > 9:
                grid[i][j] = 0
            else:
                allFlashed = False
    if allFlashed:
        print(day)
        assert False
    day += 1
    # print_grid(grid)


print(flashes)
