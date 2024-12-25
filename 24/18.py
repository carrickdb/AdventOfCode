import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

stuff = aoc.getInput(os.getenv("HOME") + "/Desktop/input")
s = 71
sim = 1024

# sim = 12
# stuff = aoc.getInput("test-input")
# s = 7

bytes = []
for line in stuff:
    bytes.append(aoc.mapint(line.split(",")))

def bfs(g):
    start = (0,0)
    e = (s-1, s-1)
    from collections import deque
    q = deque()
    q.append(start)
    steps = 0
    v = set()
    while q:
        lq = len(q)
        for _ in range(lq):
            curr = q.popleft()
            if curr in v:
                continue
            v.add(curr)
            if curr == e:
                return True
            for ni,nj in aoc.nextStep(curr):
                if (ni,nj) not in v and ni >= 0 and ni < s and nj >= 0 and nj < s and (ni,nj) not in g:
                    q.append((ni,nj))
        steps += 1
    return False


for byte in [2905, 2906, 2907, 2908]:
    g = {}
    for line in bytes[:byte]:
        i,j = line
        g[j,i] = "#"
    print(bfs(g))

print(bytes[2907])
l,r = sim, len(bytes)
while l < r:
    g = {}
    m = l + (r-l)//2

    canExit = bfs(g)
    # print(f"{canExit=}, {m=}")
    if canExit:
        l = m+1
    else:
        r = m
    prev = canExit

print(bytes[m-1], m-1)


# Part 1
stuff = aoc.getInput(os.getenv("HOME") + "/Desktop/input")
s = 71
sim = 1024
# sim = 12
# stuff = aoc.getInput("test-input")
# s = 7

g = {}

for l in stuff[:sim]:
    i,j = aoc.mapint(l.split(","))
    g[j,i] = "#"

# for i in range(s):
#     for j in range(s):
#         if (i,j) in g:
#             print("#", end="")
#         else:
#             print(".", end="")
#     print()

start = (0,0)
e = (s-1, s-1)
from collections import deque
q = deque()
q.append(start)
steps = 0
v = set()
while q:
    lq = len(q)
    for _ in range(lq):
        curr = q.popleft()
        if curr in v:
            continue
        v.add(curr)
        if curr == e:
            print(steps)
            exit()
        for ni,nj in aoc.nextStep(curr):
            if (ni,nj) not in v and ni >= 0 and ni < s and nj >= 0 and nj < s and (ni,nj) not in g:
                q.append((ni,nj))
    steps += 1


