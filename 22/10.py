cycles = 0
X = 1
with open("input") as f:
    for line in f:
        line = line.strip().split()
        if line[0] == "noop":
            pos = cycles % 40
            if pos > X-2 and pos < X+2:
                print("#", end='')
            else:
                print(".", end='')
            cycles += 1
            if cycles % 40 == 0:
                print()
        else:
            for _ in range(2):
                pos = cycles % 40
                if pos > X-2 and pos < X+2:
                    print("#", end='')
                else:
                    print(".", end='')
                cycles += 1
                if cycles % 40 == 0:
                    print()
            X += int(line[1])


# cycles = 0
# X = 1
# total = 0
# with open("input") as f:
#     for line in f:
#         line = line.strip().split()
#         if line[0] == "noop":
#             cycles += 1
#             if (cycles - 20) % 40 == 0:
#                 total += cycles * X
#                 print("X, cycles, total:", X, cycles, total)
#             # print(X)
#         else:
#             for _ in range(2):
#                 cycles += 1
#                 if (cycles - 20) % 40 == 0:
#                     total += cycles * X
#                     print("X, cycles, total:", X, cycles, total)
#                 # print(X)
#             X += int(line[1])
#             # print(X)
#
# print(total)
