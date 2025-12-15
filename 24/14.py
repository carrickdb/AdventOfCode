import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc
import re
from statistics import variance
input = aoc.getInput("input-14")
w,h = 101, 103
# input = aoc.getInput("test-input")

robots = []
for l in input:
    p = re.findall(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", l)
    pj,pi,vj, vi = aoc.mapint(p[0])
    robots.append((pi,pj,vi,vj))

image_id=7093
i_s = [(pi+image_id*vi) % h for pi,_,vi,_ in robots]
j_s = [(pj+image_id*vj) % w for _,pj,_,vj in robots]


image = [[" " for _ in range(w)] for _ in range(h)]
for i in range(len(i_s)):
    image[i_s[i]][j_s[i]] = "X"

for row in image:
    print(''.join(row))

# 10404 (the first time it repeats an image)
# low variance: 23 (vertical), 89 (horizontal)


# quadrants = {
#     (0,h//2-1,0,w//2-1): 0,
#     (h//2+1, h, 0,w//2-1): 0,
#     (0,h//2-1,w//2+1,w): 0,
#     (h//2+1,h,w//2+1,w): 0
# }
# for robot in robots:
#     i,j,_,_ = robot
#     for quadrant in quadrants.keys():
#         a,b,c,d = quadrant
#         if i>=a and i<=b and j>=c and j<=d:
#             quadrants[quadrant] += 1
# print(functools.reduce(operator.mul, quadrants.values()))



# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# import aoc
# import re
# import operator, functools
# input = aoc.getInput("input")
# w,h = 101, 103
# # input = aoc.getInput("test-input")
# w,h = 11,7

# totalSeconds = 100
# # totalSeconds = 5
# # p=10,3 v=-1,2
# g = {}
# for l in input:
#     p = re.findall(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", l)
#     pj,pi,vj, vi = aoc.mapint(p[0])
#     # pi,pj,vj,vi= 2,4,2,-3
#     ni,nj = (pi + totalSeconds*vi) % h, (pj + totalSeconds*vj) % w
#     if (ni,nj) not in g:
#         g[(ni,nj)] = 0
#     g[(ni,nj)] += 1
#     # print(g)
#     # break

# # printg = [['.' for _ in range(w)] for _ in range(h)]
# # for coords, count in g.items():
# #     i,j = coords
# #     try:
# #         printg[i][j] = str(count)
# #     except:
# #         print(i,j,len(printg), len(printg[0]))
# #         exit()

# # for row in printg:
# #     print(''.join(row))


# quadrants = {
#     (0,h//2-1,0,w//2-1): 0,
#     (h//2+1, h, 0,w//2-1): 0,
#     (0,h//2-1,w//2+1,w): 0,
#     (h//2+1,h,w//2+1,w): 0
# }
# # print(g)

# for coords, count in g.items():
#     i,j = coords
#     for quadrant in quadrants.keys():
#         a,b,c,d = quadrant
#         # print(f"{quadrant=}")
#         if i>=a and i<=b and j>=c and j<=d:
#             # print(f"adding {count} at {i,j}")
#             quadrants[quadrant] += count
# # print(quadrants)
# print(functools.reduce(operator.mul, quadrants.values()))

