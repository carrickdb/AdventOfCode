dirs = [[0,1], [0,-1], [-1, 0], [1,0]]
diagDirs = [[0,1], [0,-1], [-1, 0], [1,0], [-1, -1], [1, 1], [-1, 1], [1, -1]]

def printMapGrid(g):
    for i in sorted(g.keys(), reverse=True):
    # for i in sorted(g.keys()):
        for j in sorted(g[i].keys()):
            print(g[i][j], end="")
        print()

def printGridList(g):
    for row in g:
        print(''.join(row))
    print()

def getInput(filename):
    input = []
    with open(filename) as f:
        for l in f:
            input.append(l.strip())
    return input

def gridify(input):
    g = {}
    for i in range(len(input)):
        row = input[i]
        for j in range(len(row)):
            if i not in g:
                g[i] = {}
            g[i][j] = row[j]
    return g

def getNextSteps(i,j,g):
    ns = []
    for di,dj in dirs:
        ni,nj = i+di, j+dj
        if ni in g and nj in g[ni]:
            ns.append((ni,nj))
    return ns

def printGraph(g):
    for k,v in g.items():
        print(f"{k}: {v}")

turn_change = {
    'L' : lambda x: [-x[1], x[0]],
    'R': lambda x: [x[1], -x[0]]
}
