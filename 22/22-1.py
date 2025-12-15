import re

grid = []

with open("input2") as f:
    for line in f:
        line = line[:-1]
        grid.append(line)

r = r'(\d+|L|R)'
instructions = re.findall(r, grid[-1])
grid = grid[:-2]
for i in range(len(grid)):
    grid[i] = list(grid[i])
x, y = 0,0
while grid[y][x] == " ":
    x += 1
grid[y][x] = "x"
dir = 0
# 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^)
for i in range(len(instructions)):
    currIns = instructions[i]
    if currIns == "L":
        # print(currIns, end='')
        dir = (dir-1) % 4
    elif currIns == "R":
        # print(currIns, end='')
        dir = (dir+1) % 4
    else:
        steps = int(currIns)
        for step in range(steps):
            if dir == 0:
                nx, ny = (x+1) % len(grid[y]), y

            elif dir == 1:
                nx, ny = x, (y+1) % len(grid)

            elif dir == 2:
                nx, ny = (x-1) % len(grid[y]), y
            else:
                nx, ny = x, y-1
            if grid[ny][nx] == "#":
                break
            elif grid[ny][nx] == " ":
                print("wrong cell!")
                exit()
            else:
                x, y = nx, ny
                grid[ny][nx] = "x"
        # print(currIns)
        # for row in grid[:40]:
        #     print(''.join(row))
        # input()

print(1000*(y+1)+4*(x+1)+dir)




# import re
#
# grid = []
#
# with open("input2") as f:
#     for line in f:
#         line = line[:-1]
#         grid.append(line)
#
# r = r'(\d+|L|R)'
# instructions = re.findall(r, grid[-1])
# grid = grid[:-2]
# for i in range(len(grid)):
#     grid[i] = list(grid[i])
# x, y = 0,0
# while grid[y][x] == " ":
#     x += 1
# grid[y][x] = "x"
# dir = 0
# # 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^)
# for i in range(len(instructions)):
#     currIns = instructions[i]
#     if currIns == "L":
#         # print(currIns, end='')
#         dir = (dir-1) % 4
#     elif currIns == "R":
#         # print(currIns, end='')
#         dir = (dir+1) % 4
#     else:
#         steps = int(currIns)
#         for step in range(steps):
#             if dir == 0:
#                 nx, ny = (x+1) % len(grid[y]), y
#                 while grid[ny][nx] == ' ':
#                     nx += 1
#             elif dir == 1:
#                 nx, ny = x, (y+1) % len(grid)
#                 if len(grid[ny]) <= nx:
#                     ny = 0
#                 while grid[ny][nx] == ' ':
#                     ny = (ny+1) % len(grid)
#             elif dir == 2:
#                 nx, ny = (x-1) % len(grid[y]), y
#                 while grid[ny][nx] == ' ':
#                     nx -= 1
#             else:
#                 nx, ny = x, y-1
#                 while ny < 0 or len(grid[ny]) <= x or grid[ny][nx] == ' ':
#                     ny = (ny - 1) % len(grid)
#             if grid[ny][nx] == "#":
#                 break
#             elif grid[ny][nx] == " ":
#                 print("wrong cell!")
#                 exit()
#             else:
#                 x, y = nx, ny
#                 grid[ny][nx] = "x"
#         # print(currIns)
#         # for row in grid[:40]:
#         #     print(''.join(row))
#         # input()
#
# print(1000*(y+1)+4*(x+1)+dir)
#
# """
# guesses:
# 19186 (too low)
# 35010
# 122058
# """
