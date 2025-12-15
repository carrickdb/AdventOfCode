import aoc

"""
1 2 3
4 5 6
7 8 9
"""

g_orig = """- - 1 - -
- 2 3 4 -
5 6 7 8 9
- A B C -
- - D - -"""
g = [l.strip().split(" ") for l in g_orig.split("\n")]
# print(g)

m = {
    "U": [-1,0],
    "L": [0,-1],
    "R": [0,1],
    "D": [1,0]
}

# input = aoc.getInput("input")
input = aoc.getInput("test-input")
ci,cj = 2,0
code = []
for line in input:
    for c in line:
        ni,nj = (max(0, min(4, ci+m[c][0])),
                 max(0, min(4, cj+m[c][1])))
        if g[ni][nj] == "-":

    code.append(g[ci][cj])

print(''.join(code))



# import aoc

# """
# 1 2 3
# 4 5 6
# 7 8 9
# """

# g = aoc.gridify([[str(i+j) for i in range(3)] for j in range(1, 10, 3)])
# print(g)

# m = {
#     "U": [-1,0],
#     "L": [0,-1],
#     "R": [0,1],
#     "D": [1,0]
# }

# input = aoc.getInput("input")
# ci,cj = 1,1
# code = []
# for line in input:
#     for c in line:
#         di, dj = m[c]
#         ni, nj = di+ci, dj+cj
#         if ni not in g:
#             ni = ci
#         if nj not in g[ni]:
#             nj = cj
#         ci, cj = ni, nj
#     code.append(g[ci][cj])

# print(''.join(code))
