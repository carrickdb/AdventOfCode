import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

g = aoc.getInput("input")
# g = aoc.getInput("test-input-small")
# g = aoc.getInput("test-input")
# g = aoc.getInput("test-input-dots")
# g = aoc.getInput("wrap")

count = 0
for i in range(1, len(g)-1):
    for j in range(1, len(g[0])-1):
        x1 = ''.join([g[i-1][j-1], g[i][j], g[i+1][j+1]])
        if not (x1 == "MAS" or x1[::-1] == "MAS"):
            continue
        x2 = ''.join([g[i-1][j+1], g[i][j], g[i+1][j-1]])
        count += x2 == "MAS" or x2[::-1]=="MAS"

print(count)

arrT = aoc.transpose(g)
count = 0
XMAS = 'XMAS'
for i in range(len(g)):
    for j in range(len(g[0])):
        count += g[i][j:j+4] == XMAS
        if j-3 >= 0:
            count += g[i][j-3:j+1][::-1] == XMAS
        count += arrT[j][i:i+4] == XMAS
        if i-3 >= 0:
            count += arrT[j][i-3:i+1][::-1] == XMAS
        f = [
            lambda x,y,z: (x+z, y+z),
            lambda x,y,z: (x-z, y+z),
            lambda x,y,z: (x-z, y-z),
            lambda x,y,z: (x+z, y-z),
        ]
        for fi in range(len(f)):
            fun = f[fi]
            diag = []
            for k in range(4):
                ni,nj = fun(i,j,k)
                if ni < 0 or nj < 0 or ni >= len(g) or nj >= len(g[0]):
                    continue
                diag.append(g[ni][nj])
            count += ''.join(diag) == XMAS
            if ''.join(diag) == XMAS:
                print(i,j, "diag", fi)

print(count)
