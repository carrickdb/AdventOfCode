import aoc, copy
from collections import deque

input = aoc.getInput("input")

c = {}
m = [float("-inf") for _ in range(3)]
bs = {}
for b in range(len(input)):
    # 1,0,1~1,2,1
    bline = input[b]
    s, e = bline.split('~')
    s = list(map(int, s.split(',')))
    e = list(map(int, e.split(',')))
    bs[b] = [s,e]
    for x in range(s[0], e[0]+1):
        m[0] = max(x, m[0])
        if x not in c:
            c[x] = {}
        for y in range(s[1], e[1]+1):
            m[1] = max(y, m[1])
            if y not in c[x]:
                c[x][y] = {}
            for z in range(s[2], e[2]+1):
                m[2] = max(z, m[2])
                c[x][y][z] = b

visited = set()
for z in range(1, m[2]+1):
    for x in range(m[0]+1):
        for y in range(m[1]+1):
            if x not in c:
                continue
            if y not in c[x]:
                continue
            if z not in c[x][y]:
                continue
            curr = c[x][y][z]
            if curr in visited:
                continue
            visited.add(curr)
            cs, ce = bs[curr]
            for cx in range(cs[0], ce[0]+1):
                for cy in range(cs[1], ce[1]+1):
                    for cz in range(cs[2], ce[2]+1):
                        del c[cx][cy][cz]
            currlevel = z-1
            while currlevel > 0:
                canFall = True
                for cx in range(cs[0], ce[0]+1):
                    for cy in range(cs[1], ce[1]+1):
                        if cx in c and cy in c[cx] and currlevel in c[cx][cy]:
                            canFall = False
                            break
                    if not canFall:
                        break
                if not canFall:
                    break
                currlevel -= 1
            height = ce[2] - cs[2] + 1
            for cx in range(cs[0], ce[0]+1):
                for cy in range(cs[1], ce[1]+1):
                    for cz in range(height):
                        currz = currlevel+1+cz
                        if cx not in c:
                            c[cx] = {}
                        if cy not in c[cx]:
                            c[cx][cy] = {}
                        if currz in c[cx][cy]:
                            print("Something went horribly wrong")
                            exit()
                        c[cx][cy][currz] = curr
visited = set()
dag = {}
index = {}
for z in range(1, m[2]+1):
    for x in range(m[0]+1):
        for y in range(m[1]+1):
            if x not in c:
                continue
            if y not in c[x]:
                continue
            if z not in c[x][y]:
                continue
            curr = c[x][y][z]
            if curr in visited:
                continue
            visited.add(curr)
            cs, ce = bs[curr]
            height = ce[2] - cs[2] + 1
            toCheck = set()
            for cx in range(cs[0], ce[0]+1):
                for cy in range(cs[1], ce[1]+1):
                    if cx in c and cy in c[cx] and z+height in c[cx][cy]:
                        toCheck.add(c[cx][cy][z+height])
            for tc in toCheck:
                if tc not in dag:
                    dag[tc] = set()
                dag[tc].add(curr)
                if curr not in index:
                    index[curr] = []
                index[curr].append(tc)

# print(dag)
# print(index)
total = 0
for i in range(len(bs)):
    dagcopy = copy.deepcopy(dag)
    destroyed = 0
    todestroy = deque([i])
    while todestroy:
        lenq = len(todestroy)
        for _ in range(lenq):
            curr = todestroy.popleft()
            if curr not in index:
                continue
            for supports in index[curr]:
                dagcopy[supports].remove(curr)
                if not dagcopy[supports]:
                    todestroy.append(supports)
                    destroyed += 1
                    # print("for", i, "curr", bs[curr], "destroys", supports)
    total += destroyed

print(total)

# too low: 1296


## Part 1

# import aoc

# input = aoc.getInput("input")

# c = {}
# m = [float("-inf") for _ in range(3)]
# bs = {}
# for b in range(len(input)):
#     # 1,0,1~1,2,1
#     bline = input[b]
#     s, e = bline.split('~')
#     s = list(map(int, s.split(',')))
#     e = list(map(int, e.split(',')))
#     bs[b] = [s,e]
#     for x in range(s[0], e[0]+1):
#         m[0] = max(x, m[0])
#         if x not in c:
#             c[x] = {}
#         for y in range(s[1], e[1]+1):
#             m[1] = max(y, m[1])
#             if y not in c[x]:
#                 c[x][y] = {}
#             for z in range(s[2], e[2]+1):
#                 m[2] = max(z, m[2])
#                 c[x][y][z] = b

# visited = set()
# for z in range(1, m[2]+1):
#     for x in range(m[0]+1):
#         for y in range(m[1]+1):
#             if x not in c:
#                 continue
#             if y not in c[x]:
#                 continue
#             if z not in c[x][y]:
#                 continue
#             curr = c[x][y][z]
#             if curr in visited:
#                 continue
#             visited.add(curr)
#             cs, ce = bs[curr]
#             for cx in range(cs[0], ce[0]+1):
#                 for cy in range(cs[1], ce[1]+1):
#                     for cz in range(cs[2], ce[2]+1):
#                         del c[cx][cy][cz]
#             currlevel = z-1
#             while currlevel > 0:
#                 canFall = True
#                 for cx in range(cs[0], ce[0]+1):
#                     for cy in range(cs[1], ce[1]+1):
#                         if cx in c and cy in c[cx] and currlevel in c[cx][cy]:
#                             canFall = False
#                             break
#                     if not canFall:
#                         break
#                 if not canFall:
#                     break
#                 currlevel -= 1
#             height = ce[2] - cs[2] + 1
#             for cx in range(cs[0], ce[0]+1):
#                 for cy in range(cs[1], ce[1]+1):
#                     for cz in range(height):
#                         currz = currlevel+1+cz
#                         if cx not in c:
#                             c[cx] = {}
#                         if cy not in c[cx]:
#                             c[cx][cy] = {}
#                         if currz in c[cx][cy]:
#                             print("Something went horribly wrong")
#                             exit()
#                         c[cx][cy][currz] = curr

# visited = set()
# canBreak = []
# for z in range(1, m[2]+1):
#     for x in range(m[0]+1):
#         for y in range(m[1]+1):
#             if x not in c:
#                 continue
#             if y not in c[x]:
#                 continue
#             if z not in c[x][y]:
#                 continue
#             curr = c[x][y][z]
#             if curr in visited:
#                 continue
#             visited.add(curr)
#             cs, ce = bs[curr]
#             height = max(cs[2], ce[2]) - min(cs[2], ce[2]) + 1
#             toCheck = set()
#             for cx in range(cs[0], ce[0]+1):
#                 for cy in range(cs[1], ce[1]+1):
#                     if cx in c and cy in c[cx] and z+height in c[cx][cy]:
#                         toCheck.add(c[cx][cy][z+height])
#             numsafe = 0
#             heightToCheck = z+height-1
#             for other in list(toCheck):
#                 os, oe = bs[other]
#                 safe = False
#                 for ox in range(os[0], oe[0]+1):
#                     for oy in range(os[1], oe[1]+1):
#                         if ox in c and oy in c[ox] and heightToCheck in c[ox][oy]:
#                             cell = c[ox][oy][heightToCheck]
#                             if cell != curr:
#                                 safe = True
#                                 break
#                     if safe:
#                         break
#                 numsafe += safe
#             if numsafe == len(toCheck):
#                 canBreak.append(curr)
                
# print(len(canBreak))