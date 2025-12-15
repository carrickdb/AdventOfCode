import aoc, re

grid = {}
input = aoc.getInput("input")
# input = aoc.getInput("input")
off = '_'
on = '*'
ops = {
    "turn on": lambda x: x+1,
    "toggle": lambda x: x+2,
    "turn off": lambda x: max(0, x-1)
}
size = 2
size = 1000
for i in range(size):
    grid[i] = {}
    for j in range(size):
        grid[i][j] = 0
for line in input:
    # turn on 0,0 through 4,4
    match = re.match(r"(turn on|toggle|turn off) (\d+,\d+) through (\d+,\d+)", line)
    if not match:
        print(line)
        exit()
    op, s, e = match.group(1,2,3)
    si,sj = list(map(int, s.split(',')))
    ei,ej = list(map(int, e.split(',')))
    for i in range(si, ei+1, 1):
        for j in range(sj, ej+1, 1):
            grid[i][j] = ops[op](grid[i][j])
    # aoc.printMapGrid(grid)
    # print()
total = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        total += grid[i][j]
print(total)


# import aoc, re

# grid = {}
# # input = aoc.getInput("test-input")
# input = aoc.getInput("input")
# off = '_'
# on = '*'
# ops = {
#     "turn on": lambda x: on,
#     "toggle": lambda x: on if x==off else off,
#     "turn off": lambda x: off
# }
# # size = 5
# size = 1000
# for i in range(size):
#     grid[i] = {}
#     for j in range(size):
#         grid[i][j] = off
# for line in input:
#     # turn on 0,0 through 4,4
#     match = re.match(r"(turn on|toggle|turn off) (\d+,\d+) through (\d+,\d+)", line)
#     if not match:
#         print(line)
#         exit()
#     op, s, e = match.group(1,2,3)
#     si,sj = list(map(int, s.split(',')))
#     ei,ej = list(map(int, e.split(',')))
#     for i in range(si, ei+1, 1):
#         for j in range(sj, ej+1, 1):
#             grid[i][j] = ops[op](grid[i][j])
# # aoc.printMapGrid(grid)
# num_on = 0
# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         num_on += grid[i][j] == '*'
# print(num_on)