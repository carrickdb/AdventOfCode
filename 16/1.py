import aoc

input = aoc.getInput("test-input4")
input = aoc.getInput("input")
d = input[0].split(', ')
loc = [0, 0]
curr_dir = [-1, 0]
turn_change = {
    'L' : lambda x: [-x[1], x[0]],
    'R': lambda x: [x[1], -x[0]]
}
visits = set([tuple(loc)])
for inst in d:
    turn = inst[0]
    steps = int(inst[1:])
    curr_dir = turn_change[turn](curr_dir)
    prev = loc[:]
    for s in range(steps):
        loc = [x+y for x, y in zip(loc, curr_dir)]
        if tuple(loc) in visits:
            print(sum(list(map(abs, loc))))
            exit()
        visits.add(tuple(loc))


# # input = aoc.getInput("test-input3")
# input = aoc.getInput("input")
# d = input[0].split(', ')
# loc = [0, 0]
# curr_dir = [-1, 0]
# turn_change = {
#     'L' : lambda x: [-x[1], x[0]],
#     'R': lambda x: [x[1], -x[0]]
# }
# for inst in d:
#     turn = inst[0]
#     steps = int(inst[1:])
#     curr_dir = turn_change[turn](curr_dir)
#     loc = [x+y*steps for x,y in zip(loc, curr_dir)]

# print(sum(list(map(abs, loc))))