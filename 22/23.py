elves = set()

with open("input") as f:
    i = 0
    for line in f:
        line = line.strip()
        for j in range(len(line)):
            curr = line[j]
            if curr == "#":
                elves.add((i,j))
        i += 1

dirs = [
    [(-1, 0), (-1, 1), (-1, -1)],
    [(1,0), (1,1), (1,-1)],
    [(0,-1), (1,-1), (-1,-1)],
    [(0,1), (-1,1), (1,1)]
]

dirConsidered = 0
someElfMoves = True
round = 0
while someElfMoves:
    someElfMoves = False
    proposals = {}
    for i,j in elves:
        atLeastOne = False
        for di, dj in [(1,0), (0,1), (-1,0), (0, -1), (1,1), (-1,-1), (-1,1), (1,-1)]:
            if (di+i, dj+j) in elves:
                atLeastOne = True
                break
        if not atLeastOne:
            continue
        for x in range(4):
            curr = dirs[(dirConsidered+x)%4]
            move = True
            for di, dj in curr:
                ni, nj = i+di, dj+j
                if (ni, nj) in elves:
                    move = False
                    break
            if move:
                moveDir = (i+curr[0][0], j+curr[0][1])
                if moveDir in proposals:
                    proposals[moveDir].append((i,j))
                else:
                    proposals[moveDir] = [(i,j)]
                break
    newSpaces = set()
    for newSpace, proposers in proposals.items():
        if len(proposers) == 1:
            someElfMoves = True
            newSpaces.add(newSpace)
            elves.remove(proposers[0])
    elves |= newSpaces
    dirConsidered = (dirConsidered + 1) % 4
    round += 1

print(round)




# elves = set()
#
# with open("input") as f:
#     i = 0
#     for line in f:
#         line = line.strip()
#         for j in range(len(line)):
#             curr = line[j]
#             if curr == "#":
#                 elves.add((i,j))
#         i += 1
#
#
# """
# If there is no Elf in the N, NE, or NW adjacent positions, the Elf proposes moving north one step.
# If there is no Elf in the S, SE, or SW adjacent positions, the Elf proposes moving south one step.
# If there is no Elf in the W, NW, or SW adjacent positions, the Elf proposes moving west one step.
# If there is no Elf in the E, NE, or SE adjacent positions, the Elf proposes moving east one step.
# """
#
# dirs = [
#     [(-1, 0), (-1, 1), (-1, -1)],
#     [(1,0), (1,1), (1,-1)],
#     [(0,-1), (1,-1), (-1,-1)],
#     [(0,1), (-1,1), (1,1)]
# ]
#
# dirConsidered = 0
# for _ in range(10):
#     proposals = {}
#     for i,j in elves:
#         atLeastOne = False
#         for di, dj in [(1,0), (0,1), (-1,0), (0, -1), (1,1), (-1,-1), (-1,1), (1,-1)]:
#             if (di+i, dj+j) in elves:
#                 atLeastOne = True
#                 break
#         if not atLeastOne:
#             # print(i,j, "has no neighbors")
#             continue
#         for x in range(4):
#             curr = dirs[(dirConsidered+x)%4]
#             move = True
#             for di, dj in curr:
#                 ni, nj = i+di, dj+j
#                 if (ni, nj) in elves:
#                     move = False
#                     break
#             if move:
#                 moveDir = (i+curr[0][0], j+curr[0][1])
#                 if moveDir in proposals:
#                     proposals[moveDir].append((i,j))
#                     print(i,j, "proposes to move to", moveDir)
#                 else:
#                     proposals[moveDir] = [(i,j)]
#                 break
#     newSpaces = set()
#     for newSpace, proposers in proposals.items():
#         if len(proposers) == 1:
#             newSpaces.add(newSpace)
#             elves.remove(proposers[0])
#     elves |= newSpaces
#     dirConsidered = (dirConsidered + 1) % 4
#
# mini = min([i for i, _ in elves])
# maxi = max([i for i, _ in elves])
# minj = min([j for _, j in elves])
# maxj = max([j for _, j in elves])
# # grid = [["." for _ in range(maxj+1-minj)] for n in range(maxi+1-mini)]
# # # grid = [["." for _ in range(10)] for blah in range(10)]
# # for i,j in elves:
# #     grid[i-mini][j-minj] = "#"
# # for row in grid:
# #     print(''.join(row))
# # input()
#
#
# empty = (maxi+1-mini)*(maxj+1-minj)
# empty -= len(elves)
#
# print(empty)
#
# """
# guesses:
# 4360 (too high)
# """
