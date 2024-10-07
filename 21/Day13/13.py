# Part 2

dots = set()
folds = []

with open("input13") as f:
    for line in f:
        if line == "\n":
            continue
        if line[0] == "f":
            fold = line.strip().split()[2].split("=")
            folds.append([fold[0], int(fold[1])])
        else:
            dots.add(tuple(map(int, line.strip().split(","))))

# print(folds)
# print(len(dots))
for direction, line in folds:
    for dotj, doti in [dot for dot in dots]:
        if direction == "y":
            if doti > line and doti <= line*2:
                newi = line - (doti-line)
                dots.discard((dotj, doti))
                dots.add((dotj, newi))
        if direction == "x":
            if dotj > line and dotj <= line*2:
                newj = line - (dotj-line)
                dots.discard((dotj, doti))
                dots.add((newj, doti))
                # print((dotj, doti))

maxX = 0
maxY = 0
for x, y in dots:
    maxX = max(maxX, x)
    maxY = max(maxY, y)

grid = [[" " for j in range(maxX+1)] for i in range(maxY+1)]

for j, i in dots:
    grid[i][j] = "█"

for row in grid:
    print(''.join(row))


# # Part 1
#
# dots = set()
# folds = []
#
# with open("input") as f:
#     for line in f:
#         if line == "\n":
#             continue
#         if line[0] == "f":
#             fold = line.strip().split()[2].split("=")
#             folds.append([fold[0], int(fold[1])])
#         else:
#             dots.add(tuple(map(int, line.strip().split(","))))
#
# # print(folds)
# print(len(dots))
# direction, line = folds[0]
# for dotj, doti in [dot for dot in dots]:
#     if direction == "y":
#         if doti > line and doti <= line*2:
#             newi = line - (doti-line)
#             if (dotj, newi) in dots:
#                 dots.discard((dotj, doti))
#                 # print((dotj, doti))
#     if direction == "x":
#         if dotj > line and dotj <= line*2:
#             newj = line - (dotj-line)
#             if (newj, doti) in dots:
#                 dots.discard((dotj, doti))
#                 # print((dotj, doti))
#
# print(len(dots))
