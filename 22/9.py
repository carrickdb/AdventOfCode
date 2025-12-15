positions = set()

knots = [[0, 0] for _ in range(10)]
dirs = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1)
}
positions.add((0, 0))
with open("input") as f:
    for line in f:
        dir, num = line.strip().split()
        num = int(num)
        dx, dy = dirs[dir]
        for _ in range(num):
            knots[0][0] += dx
            knots[0][1] += dy
            for i in range(1, len(knots)):
                curr = knots[i]
                hx = knots[i-1][0]
                hy = knots[i-1][1]
                if hx > curr[0] + 1:
                    curr[0] += 1
                    if hy < curr[1]:
                        curr[1] -= 1
                    elif hy > curr[1]:
                        curr[1] += 1
                elif hx < curr[0] - 1:
                    curr[0] -= 1
                    if hy < curr[1]:
                        curr[1] -= 1
                    elif hy > curr[1]:
                        curr[1] += 1
                elif hy > curr[1] + 1:
                    curr[1] += 1
                    if hx < curr[0]:
                        curr[0] -= 1
                    elif hx > curr[0]:
                        curr[0] += 1
                elif hy < curr[1] - 1:
                    curr[1] -= 1
                    if hx < curr[0]:
                        curr[0] -= 1
                    elif hx > curr[0]:
                        curr[0] += 1
                # print("h:", hx, hy)
                # print("t:", curr)
                # print()
                # exit()
            positions.add((knots[9][0], knots[9][1]))

print(len(positions))





# positions = set()
#
# hx, hy = 0, 0
# tx, ty = 0, 0
# dirs = {
#     "R": (1, 0),
#     "L": (-1, 0),
#     "U": (0, 1),
#     "D": (0, -1)
# }
# positions.add((tx, ty))
# with open("input") as f:
#     for line in f:
#         dir, num = line.strip().split()
#         num = int(num)
#         dx, dy = dirs[dir]
#         # print("dx, dy:", dx, dy)
#         for _ in range(num):
#             hx += dx
#             hy += dy
#             if hx > tx + 1:
#                 tx += 1
#                 if hy < ty:
#                     ty -= 1
#                 elif hy > ty:
#                     ty += 1
#                 # print("tx changed to", tx)
#             elif hx < tx - 1:
#                 tx -= 1
#                 if hy < ty:
#                     ty -= 1
#                 elif hy > ty:
#                     ty += 1
#                 # print("tx changed to", tx)
#             elif hy > ty + 1:
#                 print("hy", hy, "is greater than ty", ty, "plus 1")
#                 ty += 1
#                 if hx < tx:
#                     tx -= 1
#                 elif hx > tx:
#                     tx += 1
#                 # print("ty changed to", ty)
#             elif hy < ty - 1:
#                 ty -= 1
#                 if hx < tx:
#                     tx -= 1
#                 elif hx > tx:
#                     tx += 1
#                 # print("ty changed to", ty)
#             print("h:", hx, hy)
#             print("t:", tx, ty)
#             print()
#             # exit()
#             positions.add((tx, ty))
#
# print(len(positions))
