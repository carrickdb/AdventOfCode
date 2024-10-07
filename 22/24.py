from collections import defaultdict, deque
import copy
import aoc

"""
6 x 7
#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#
"""

dirs = {'^': 0, 'v':1, '<':2, '>':3}
dirsRev = {0: '^', 1: 'v', 2: '<', 3: '>'}
grid = open("input").read().strip().split('\n')
width = len(grid)
length = len(grid[0])
# print("width, length", width, length)
blizzards = [set() for _ in range(4)]
for i in range(1, width-1):
    for j in range(1, length-1):
        curr = grid[i][j]
        if curr == ".":
            continue
        curr = dirs[curr]
        blizzards[curr].add((i,j))

def printGrid(bsets, queue=None):
    tmpgrid = [["." for j in range(length)] for i in range(width)]
    for i in range(len(bsets)):
        bset = bsets[i]
        for bi, bj in bset:
            blah = tmpgrid[bi]
            blah2 = blah[bj]
            blizzardStack = tmpgrid[bi][bj]
            if type(blizzardStack) == int:
                tmpgrid[bi][bj] += 1
            elif blizzardStack != ".":
                tmpgrid[bi][bj] = 2
            else:
                tmpgrid[bi][bj] = dirsRev[i]
    if queue:
        q = set(queue)
        for ij, _ in q:
            i, j = ij
            if tmpgrid[i][j] != ".":
                print("uh oh", i, j, tmpgrid[i][j])
                printGrid(bsets)
                exit()
            tmpgrid[i][j] = "E"
    for row in tmpgrid:
        print(''.join([str(x) for x in row]))

minute = 0
starts = [(0,1), (width-1, length-2), (0,1)]
for starti in range(len(starts)):
    done = False
    start = starts[starti]
    q = deque()
    q.append((start, minute))
    visited = set()
    while q:
        for n in range(len(blizzards)):
            bs = blizzards[n]
            newbs = set()
            for bi, bj in bs:
                # dirs = {'^': 0, 'v':1, '<':2, '>':3}
                if n == 0:
                    newbi = bi-1
                    if newbi == 0:
                        newbi = width-2
                    newCoords = (newbi, bj)
                elif n == 1:
                    newbi = bi + 1
                    if newbi > width-2:
                        newbi = 1
                    newCoords = (newbi, bj)
                elif n == 2:
                    newbj = bj-1
                    if newbj == 0:
                        newbj = length-2
                    newCoords = (bi, newbj)
                else:
                    newbj = bj+1
                    if newbj > length-2:
                        newbj = 1
                    newCoords = (bi, newbj)
                newbs.add(newCoords)
            blizzards[n] = newbs
        u = set()
        for bset in blizzards:
            u |= bset
        numInLevel = len(q)
        for _ in range(numInLevel):
            curr = q.popleft()
            if curr in visited:
                continue
            visited.add(curr)
            currCoords, currmin = curr
            ci, cj = currCoords
            for di, dj in aoc.dirs + [[0,0]]:
                ni, nj = ci+di, cj+dj
                if starti == 0 or starti == 2:
                    if ni == width-1 and nj == length-2:
                        done = True
                        print(ni, nj, minute+1)
                        if starti == 2:
                            exit()
                        break
                elif starti == 1:
                    if ni == 0 and nj == 1:
                        done = True
                        print(ni, nj, minute+1)
                if ni == 0 and nj == 1:
                    q.append(((ni, nj), minute+1))
                elif (ni, nj) not in u and ni > 0 and ni < width-1 and nj > 0 and nj < length-1:
                    q.append(((ni, nj), minute+1))
            if done:
                break
        minute += 1
        if done:
            break

"""
guesses:
561 (too low)
"""



# from collections import defaultdict, deque
# import copy
# import aoc
#
# """
# 6 x 7
# #.######
# #>>.<^<#
# #.<..<<#
# #>v.><>#
# #<^v^^>#
# ######.#
# """
#
# dirs = {'^': 0, 'v':1, '<':2, '>':3}
# dirsRev = {0: '^', 1: 'v', 2: '<', 3: '>'}
# grid = open("input").read().strip().split('\n')
# width = len(grid)
# length = len(grid[0])
# # print("width, length", width, length)
# blizzards = [set() for _ in range(4)]
# for i in range(1, width-1):
#     for j in range(1, length-1):
#         curr = grid[i][j]
#         if curr == ".":
#             continue
#         curr = dirs[curr]
#         blizzards[curr].add((i,j))
#
# def printGrid(bsets, queue=None):
#     tmpgrid = [["." for j in range(length)] for i in range(width)]
#     for i in range(len(bsets)):
#         bset = bsets[i]
#         for bi, bj in bset:
#             blah = tmpgrid[bi]
#             blah2 = blah[bj]
#             blizzardStack = tmpgrid[bi][bj]
#             if type(blizzardStack) == int:
#                 tmpgrid[bi][bj] += 1
#             elif blizzardStack != ".":
#                 tmpgrid[bi][bj] = 2
#             else:
#                 tmpgrid[bi][bj] = dirsRev[i]
#     if queue:
#         q = set(queue)
#         for ij, _ in q:
#             i, j = ij
#             if tmpgrid[i][j] != ".":
#                 print("uh oh", i, j, tmpgrid[i][j])
#                 printGrid(bsets)
#                 exit()
#             tmpgrid[i][j] = "E"
#     for row in tmpgrid:
#         print(''.join([str(x) for x in row]))
#
# q = deque()
# q.append(((0,1), 0))
# visited = set()
# minute = 0
# while q:
#     for n in range(len(blizzards)):
#         bs = blizzards[n]
#         newbs = set()
#         for bi, bj in bs:
#             # dirs = {'^': 0, 'v':1, '<':2, '>':3}
#             if n == 0:
#                 newbi = bi-1
#                 if newbi == 0:
#                     newbi = width-2
#                 newCoords = (newbi, bj)
#             elif n == 1:
#                 newbi = bi + 1
#                 if newbi > width-2:
#                     newbi = 1
#                 newCoords = (newbi, bj)
#             elif n == 2:
#                 newbj = bj-1
#                 if newbj == 0:
#                     newbj = length-2
#                 newCoords = (bi, newbj)
#             else:
#                 newbj = bj+1
#                 if newbj > length-2:
#                     newbj = 1
#                 newCoords = (bi, newbj)
#             newbs.add(newCoords)
#         blizzards[n] = newbs
#     u = set()
#     for bset in blizzards:
#         u |= bset
#     numInLevel = len(q)
#     for _ in range(numInLevel):
#         curr = q.popleft()
#         if curr in visited:
#             continue
#         visited.add(curr)
#         currCoords, currmin = curr
#         ci, cj = currCoords
#         for di, dj in aoc.dirs + [[0,0]]:
#             ni, nj = ci+di, cj+dj
#             if ni == width-1 and nj == length-2:
#                 print(ni, nj, minute+1)
#                 exit()
#             if ni == 0 and nj == 1:
#                 q.append(((ni, nj), minute+1))
#             elif (ni, nj) not in u and ni > 0 and ni < width-1 and nj > 0 and nj < length-1:
#                 q.append(((ni, nj), minute+1))
#
#     # print(q)
#     # printGrid(blizzards, q)
#     minute += 1
