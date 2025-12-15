import queue

grid = {}
with open("input-10") as f:
    i = 0
    for l in f:
        grid[i] = {}
        j = 0
        for x in l.strip():
            grid[i][j] = x
            j += 1
        i += 1
    
s = None
for i in range(len(grid.keys())):
    for j in range(len(grid[0].keys())):
        if grid[i][j] == "S":
            s = [i, j]

toMap = {
    (0,1): set(["7", "-", "J"]),
    (0, -1): set(["-", "L", "F"]),
    (1,0): set(["|","J", "L"]),
    (-1,0): set(["|",  "F", "7"]),
}

fromMap = {
    "S": [[0,1], [0,-1], [-1, 0], [1,0]],
    "|": [[-1, 0], [1, 0]],
    "-": [[0,1], [0,-1]],
    "L": [[-1,0], [0,1]],
    "J": [[-1,0], [0,-1]],
    "7": [[1,0], [0,-1]],
    "F": [[1,0], [0,1]],
    ".": []
}

def printGrid(g):
    for i in range(len(g.keys())):
        for j in range(len(g[i].keys())):
            print(g[i][j], end="\t")
        print()

q = queue.Queue()
q.put(s)
step = 0
done = False
area = 0
while not q.empty():
    lenq = q.qsize()
    for i in range(lenq):
        ci, cj = q.get()
        curr = grid[ci][cj]
        if isinstance(curr, int):
            done = True
            break
        dirs = fromMap[curr]
        grid[ci][cj] = step
        for di, dj in dirs:
            ni, nj = ci+di, cj+dj
            if ni in grid and nj in grid[ni]:
                other = grid[ni][nj]
                if isinstance(other, int):
                    if step == 13883 and other == 0:
                        area += (ni-ci)*(cj+nj)/2
                        break
                    continue
                ok = toMap[(di, dj)]
                if other in ok:
                    q.put([ni, nj])
                    area += (ni-ci)*(cj+nj)/2 # Shoelace formula
                    break
    if done:
        break
    step += 1

print("area+1-step//2", abs(area)+1-step//2) # Pick's theorem

## Part 1

grid = {}
with open("input") as f:
    i = 0
    for l in f:
        grid[i] = {}
        j = 0
        for x in l.strip():
            grid[i][j] = x
            j += 1
        i += 1
    
s = None
for i in range(len(grid.keys())):
    for j in range(len(grid[0].keys())):
        if grid[i][j] == "S":
            s = [i, j]

q = queue.Queue()
q.put(s)
step = 0
done = False
while not q.empty():
    lenq = q.qsize()
    for i in range(lenq):
        ci, cj = q.get()
        curr = grid[ci][cj]
        if isinstance(curr, int):
            done = True
            break
        dirs = fromMap[curr]
        grid[ci][cj] = step
        for di, dj in dirs:
            ni, nj = ci+di, cj+dj
            if ni in grid and nj in grid[ni]:
                other = grid[ni][nj]
                if isinstance(other, int):
                    continue
                ok = toMap[(di, dj)]
                if other in ok:
                    q.put([ni, nj])
    if done:
        break
    step += 1

print(step)