import aoc

input = aoc.getInput("input")

m = {}
mapping = {
    "2": (0, -1),
    "0": (0, 1),
    "3": (-1,0),
    "1": (1,0)
}
ci, cj = 0,0
area = 0
b = 0
for l in input:
    # L 4 (#6c82d0)
    _, inst = l.split("(#")
    num = int(inst[:-2], 16)
    di, dj = mapping[inst[-2]]
    ni, nj = ci+di*num, cj+dj*num
    area += ((ni-ci)*(nj+cj))//2
    b += num
    ci, cj = ni, nj
print(area+1+b//2)

# too low: 952408144115

# import aoc

# input = aoc.getInput("input")

# m = {}
# mapping = {
#     "L": (0, -1),
#     "R": (0, 1),
#     "U": (-1,0),
#     "D": (1,0)
# }
# ci, cj = 0,0
# area = 0
# b = 0
# for l in input:
#     # L 4 (#6c82d0)
#     dir, num, _ = l.split()
#     num = int(num)
#     di, dj = mapping[dir]
#     ni, nj = ci+di*num, cj+dj*num
#     area += ((ni-ci)*(nj+cj))/2
#     b += num
#     ci, cj = ni, nj
#     print(ci, cj)
# print(area+1+b/2)
