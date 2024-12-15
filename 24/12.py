import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

input = aoc.getInput("input")
# input = aoc.getInput("test-input")
# input = aoc.getInput("test-input-small")

counts = {}
v = set()
for i in range(len(input)):
    for j in range(len(input[0])):
        curr = input[i][j]
        if (i,j) in v:
            continue
        s = [(i,j)]
        perim = {}
        area = 0
        currv = set()
        while s:
            c = s.pop()
            if c in currv:
                continue
            currv.add(c)
            ci,cj = c
            area += 1
            for di,dj in aoc.dirs:
                ni,nj = di+ci,dj+cj
                if aoc.inBounds(ni,nj,input) and input[ni][nj] == curr and (ni,nj) not in currv:
                    s.append((ni,nj))
                elif (ni,nj) not in currv:
                    if (di,dj) not in perim:
                        perim[(di,dj)] = set()
                    perim[(di,dj)].add((ni,nj))
        sides = 0
        # print(perim)
        for direction, segments in perim.items():
            perimeterVisited = set()
            for segment in segments:
                if segment in perimeterVisited:
                    continue
                stack = [segment]
                while stack:
                    curr = stack.pop()
                    if curr in perimeterVisited:
                        continue
                    perimeterVisited.add(curr)
                    for di,dj in aoc.dirs:
                        ni,nj = di+curr[0],dj+curr[1]
                        if (ni,nj) not in segments:
                            continue
                        stack.append((ni,nj))
                sides += 1
        counts[(i,j)] = (area, sides)
        # exit()
        v |= currv

print(sum(x[0]*x[1] for _,x in counts.items()))

# for k,v in counts.items():
#     i,j = k
#     print(input[i][j], v)






# print(input)
# counts = {}
# v = set()
# for i in range(len(input)):
#     for j in range(len(input[0])):
#         curr = input[i][j]
#         if (i,j) in v:
#             continue
#         s = [(i,j)]
#         perim = 0
#         area = 0
#         currv = set()
#         while s:
#             # print(s)
#             c = s.pop()
#             if c in currv:
#                 continue
#             currv.add(c)
#             ci,cj = c
#             area += 1
#             # print(ci,cj)
#             for di,dj in aoc.dirs:
#                 ni,nj = di+ci,dj+cj
#                 if aoc.inBounds(ni,nj,input) and input[ni][nj] == curr and (ni,nj) not in currv:
#                     s.append((ni,nj))
#                 elif (ni,nj) not in currv:
#                     perim += 1
#         counts[(i,j)] = (area, perim)
#         v |= currv
#         # print(area)
#         # exit()

# print(sum(x[0]*x[1] for _,x in counts.items()))

# for k,v in counts.items():
#     i,j = k
#     print(input[i][j], v)

# counts = {}
# v = set()
# for i in range(len(input)):
#     for j in range(len(input[0])):
#         curr = input[i][j]
#         if (i,j) in v:
#             continue
#         s = [(i,j)]
#         perim = {}
#         area = 0
#         currv = set()
#         while s:
#             c = s.pop()
#             if c in currv:
#                 continue
#             currv.add(c)
#             ci,cj = c
#             area += 1
#             for di,dj in aoc.dirs:
#                 ni,nj = di+ci,dj+cj
#                 if aoc.inBounds(ni,nj,input) and input[ni][nj] == curr and (ni,nj) not in currv:
#                     s.append((ni,nj))
#                 elif (ni,nj) not in currv:
#                     perim[(ni,nj)] = '#'
#         pi,pj = list(perim.keys())[0]
#         print(pi,pj)
        # sides = 0
        # diri,dirj = None, None
        # print(perim)
        # for di,dj in aoc.dirs:
        #     if (pi+di, pj+dj) in perim:
        #         diri,dirj = di,dj
        # print(diri,dirj)
        # ci,cj = pi,pj
        # while True:
        #     ni,nj = ci+diri, cj+dirj
        #     if (ni,nj) not in perim:
        #         ti,tj = aoc.turn_change('L')(diri,dirj)
        #         ni,nj = ti+ci,tj+cj
        #         if (ni,nj) not in perim:
        #             ni,nj = ti+ci, tj+cj
        #             if (ni,nj) not in perim:
        #                 print("This will never happen")
        #                 exit()
        #         sides += 1
        #     ci,cj = ni,nj
        #     if ci==pi and cj==pj:
        #         break
#         counts[(i,j)] = (area, sides)
#         v |= currv
#         # print(area)
#         # exit()

# print(sum(x[0]*x[1] for _,x in counts.items()))

# for k,v in counts.items():
#     i,j = k
#     print(input[i][j], v)



# print(input)
# counts = {}
# v = set()
# for i in range(len(input)):
#     for j in range(len(input[0])):
#         curr = input[i][j]
#         if (i,j) in v:
#             continue
#         s = [(i,j)]
#         perim = 0
#         area = 0
#         currv = set()
#         while s:
#             # print(s)
#             c = s.pop()
#             if c in currv:
#                 continue
#             currv.add(c)
#             ci,cj = c
#             area += 1
#             # print(ci,cj)
#             for di,dj in aoc.dirs:
#                 ni,nj = di+ci,dj+cj
#                 if aoc.inBounds(ni,nj,input) and input[ni][nj] == curr and (ni,nj) not in currv:
#                     s.append((ni,nj))
#                 elif (ni,nj) not in currv:
#                     perim += 1
#         counts[(i,j)] = (area, perim)
#         v |= currv
#         # print(area)
#         # exit()

# print(sum(x[0]*x[1] for _,x in counts.items()))

# # for k,v in counts.items():
# #     i,j = k
# #     print(input[i][j], v)





