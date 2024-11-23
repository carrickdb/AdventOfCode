input = 277678

g = {0: {0: 1}}
ci, cj = 0, 1
l = 2
dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
neighbors = [(-1,-1), (1,1), (-1, 1), (1, -1), (-1, 0), (0, -1), (1, 0), (0, 1)]
while True:
    for i in range(len(dirs)):
        di, dj = dirs[i]
        if i > 0:
            ci += di
            cj += dj
        for step in range(l):
            if ci not in g:
                g[ci] = {}
            total = 0
            for looki, lookj in neighbors:
                neighbori, neighborj = ci+looki, cj+lookj
                if neighbori not in g or neighborj not in g[neighbori]:
                    continue
                total += g[neighbori][neighborj]
            g[ci][cj] = total
            if total > input:
                # aoc.printMapGrid(g)
                # print()
                print(total)
                exit()
            if step < l-1:
                ci, cj = ci+di, cj+dj
    cj += 1
    l += 2



# import math

# for i in input:
#     sr = int(math.sqrt(i))
#     if sr%2 == 0:
#         sr += 1
#     elif sr*sr != i:
#         sr += 2
#     position = i - pow(sr-2, 2) - 1
#     part = position//(sr-1)
#     order = position%(sr-1)
#     ring = sr//2-1
#     print(sr//2 + abs(order - ring))
