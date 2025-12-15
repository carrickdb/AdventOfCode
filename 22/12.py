from collections import deque

grid = []

with open("input") as f:
    for line in f:
        grid.append(line.strip())

starts = []
# 456
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "a":
            starts.append((i, j))

steps = {}

for start in starts:
    queue = deque()
    queue.append(start)
    numSteps = 0
    visited = set()
    done = False
    while queue and not done:
        # print(queue)
        currLen = len(queue)
        for i in range(currLen):
            curr = queue.popleft()
            if curr in visited or curr in steps:
                continue
            curri, currj = curr
            visited.add((curri, currj))
            currChar = grid[curri][currj]
            if currChar == "E":
                steps[start] = numSteps
                done = True
                break
            for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                ni, nj = curri+di, currj+dj
                if ni >= 0 and nj >= 0 and ni < len(grid) and nj < len(grid[0]) and (ni, nj) not in visited:
                    newChar = grid[ni][nj]
                    if newChar == "S":
                        newChar = 'a'
                    elif newChar == "E":
                        newChar = 'z'
                    height = ord(newChar)
                    if currChar == "S":
                        currChar = 'a'
                    elif currChar == "E":
                        currChar = 'z'
                    currHeight = ord(currChar)
                    if height <= currHeight + 1:
                        queue.append((ni, nj))
        numSteps += 1

print(min(steps.values()))



# from collections import deque
#
# grid = []
#
# with open("input") as f:
#     for line in f:
#         grid.append(line.strip())
#
# pos = None
# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         if grid[i][j] == "S":
#             pos = (i, j)
#
# queue = deque()
# queue.append(pos)
# numSteps = 0
# visited = set()
# while queue:
#     # print(queue)
#     currLen = len(queue)
#     for i in range(currLen):
#         curr = queue.popleft()
#         if curr in visited:
#             continue
#         curri, currj = curr
#         visited.add((curri, currj))
#         currChar = grid[curri][currj]
#         if currChar == "E":
#             print(numSteps)
#             exit()
#         for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
#             ni, nj = curri+di, currj+dj
#             if ni >= 0 and nj >= 0 and ni < len(grid) and nj < len(grid[0]) and (ni, nj) not in visited:
#                 newChar = grid[ni][nj]
#                 if newChar == "S":
#                     newChar = 'a'
#                 elif newChar == "E":
#                     newChar = 'z'
#                 height = ord(newChar)
#                 if currChar == "S":
#                     currChar = 'a'
#                 elif currChar == "E":
#                     currChar = 'z'
#                 currHeight = ord(currChar)
#                 if height <= currHeight + 1:
#                     queue.append((ni, nj))
#     numSteps += 1
#     # if numSteps > 1:
#     #     exit()
