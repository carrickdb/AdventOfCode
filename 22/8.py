grid = []
with open("input") as f:
    for line in f:
        grid.append(list(map(int, line.strip())))

maxScore = float("-inf")
for i in range(len(grid)):
    for j in range(len(grid[0])):
        # i = 1
        # j = 2
        dirScores = []
        for dx, dy in [[0, -1], [-1, 0], [1, 0], [0, 1]]:
            y = i
            x = j
            dirScore = 0
            while True:
                x += dx
                y += dy
                if x >= len(grid[0]) or x < 0:
                    break
                if y >= len(grid) or y < 0:
                    break
                if grid[y][x] < grid[i][j]:
                    dirScore += 1
                else:
                    dirScore += 1
                    break
            dirScores.append(dirScore)
        curr = 1
        for num in dirScores:
            curr *= num
        maxScore = max(maxScore, curr)
        # print(maxScore)
        # print(dirScores)
        # assert False

print(maxScore)




# grid = []
# with open("input") as f:
#     for line in f:
#         grid.append(list(map(int, line.strip())))
# seen = set()
# for i in range(len(grid)):
#     tallest = None
#     for j in range(len(grid[0])):
#         curr = grid[i][j]
#         if tallest == None:
#             seen.add((i, j))
#             tallest = curr
#         elif tallest < curr:
#             seen.add((i, j))
#             tallest = curr
#
# for j in range(len(grid[0])):
#     tallest = None
#     for i in range(len(grid)):
#         curr = grid[i][j]
#         if tallest == None:
#             seen.add((i, j))
#             tallest = curr
#         elif tallest < curr:
#             seen.add((i, j))
#             tallest = curr
#
# for i in range(len(grid)):
#     tallest = None
#     for j in range(len(grid[0])-1, -1, -1):
#         curr = grid[i][j]
#         if tallest == None:
#             seen.add((i, j))
#             tallest =curr
#         elif tallest < curr:
#             seen.add((i, j))
#             tallest = curr
#
#
# for j in range(len(grid[0])):
#     tallest = None
#     for i in range(len(grid)-1, -1, -1):
#         curr = grid[i][j]
#         if tallest == None:
#             seen.add((i, j))
#             tallest = curr
#         elif tallest < curr:
#             seen.add((i, j))
#             tallest = curr
#
# print(len(seen))
