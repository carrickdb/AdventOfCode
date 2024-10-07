droplets = set()

with open("input") as f:
    for line in f:
        droplets.add(tuple(map(int, line.strip().split(','))))

maxx = max([i for i, j, k in list(droplets)])
maxy = max([j for i, j, k in list(droplets)])
maxz = max([k for i, j, k in list(droplets)])
minx = min([i for i, j, k in list(droplets)])
miny = min([j for i, j, k in list(droplets)])
minz = min([k for i, j, k in list(droplets)])

def DFS(start):
    numsides = 0
    stack = [start]
    while stack:
        curr = stack.pop()
        if curr in visited:
            continue
        visited.add(curr)
        for axis in range(3):
            for diff in [-1, 1]:
                next = list(curr)
                next[axis] += diff
                nextT = tuple(next)
                if nextT in droplets:
                    numsides += 1
                else:
                    if next[axis] >= mins[axis] and next[axis] <= maxes[axis] and nextT not in visited:
                        stack.append(nextT)
    return numsides

numsides = 0
visited = set()
mins = [minx, miny, minz]
maxes = [maxx, maxy, maxz]
for i in range(minx-1, maxx+2):
    for j in range(miny-1, maxy+2):
        for k in [minz-1, maxz+1]:
            if (i,j,k) not in droplets and (i,j,k) not in visited:
                numsides += DFS((i,j,k))

for i in range(minx-1, maxx+2):
    for j in [miny-1, maxy+1]:
        for k in range(minz-1, maxz+2):
            if (i,j,k) not in droplets and (i,j,k) not in visited:
                numsides += DFS((i,j,k))

for i in [minx-1, maxx+1]:
    for j in range(miny-1, maxy+2):
         for k in range(minz-1, maxz+2):
             if (i,j,k) not in droplets and (i,j,k) not in visited:
                 numsides += DFS((i,j,k))

print(numsides)




# numsides = 0
# dCopy = droplets.copy()
# while dCopy:
#     stack = [list(dCopy)[0]]
#     visited = set()
#     while stack:
#         curr = stack.pop()
#         if curr in visited:
#             continue
#         visited.add(curr)
#         for i in range(3):
#             for j in [-1, 1]:
#                 next = list(curr)
#                 next[i] += j
#                 nextT = tuple(next)
#                 if nextT in dCopy:
#                     if nextT not in visited:
#                         stack.append(nextT)
#                 else:
#                     numsides += 1
#     dCopy = dCopy - visited
#
# print(numsides)
#
# maxx = max([i for i, j, k in list(droplets)])
# maxy = max([j for i, j, k in list(droplets)])
# maxz = max([k for i, j, k in list(droplets)])
# minx = min([i for i, j, k in list(droplets)])
# miny = min([j for i, j, k in list(droplets)])
# minz = min([k for i, j, k in list(droplets)])
#
# mins = [minx, miny, minz]
# maxes = [maxx, maxy, maxz]
#
# visited = set()
# airPocketSurfaceArea = 0
# for i in range(minx, maxx+1):
#     for j in range(miny, maxy+1):
#         for k in range(minz, maxz+1):
#             curr = (i, j, k)
#             if curr in droplets or curr in visited:
#                 continue
#             isAirPocket = True
#             surfaceArea = 0
#             stack = [curr]
#             while stack:
#                 c = stack.pop()
#                 if c in visited:
#                     continue
#                 visited.add(c)
#                 for n in range(3):
#                     for m in [-1, 1]:
#                         next = list(c)
#                         next[n] += m
#                         if next[n] < mins[n] or next[n] > maxes[n]:
#                             isAirPocket = False
#                             surfaceArea = 0
#                             break
#                         nextT = tuple(next)
#                         if nextT not in droplets:
#                             if nextT not in visited:
#                                 stack.append(nextT)
#                         else:
#                             surfaceArea += 1
#                     if not isAirPocket:
#                         break
#             airPocketSurfaceArea += surfaceArea
#
# print(numsides - airPocketSurfaceArea)

"""
guessed: 2087

"""


# droplets = set()
#
# with open("input") as f:
#     for line in f:
#         droplets.add(tuple(map(int, line.strip().split(','))))
#
# # print(len(droplets))
#
# numsides = 0
# while droplets:
#     stack = [list(droplets)[0]]
#     visited = set()
#     while stack:
#         curr = stack.pop()
#         if curr in visited:
#             continue
#         # print(curr)
#         visited.add(curr)
#         for i in range(3):
#             for j in [-1, 1]:
#                 next = list(curr)
#                 next[i] += j
#                 nextT = tuple(next)
#                 if nextT in droplets:
#                     if nextT not in visited:
#                         stack.append(nextT)
#                 else:
#                     numsides += 1
#     droplets = droplets - visited
#
# print(numsides)
