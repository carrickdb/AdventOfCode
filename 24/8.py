import itertools
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

input = aoc.getInput("input")
# input = aoc.getInput("test-input")

# Part 2
antinodes = set()
antennas = {}
for i in range(len(input)):
    for j in range(len(input[0])):
        curr = input[i][j]
        if curr == ".":
            continue
        if curr not in antennas:
            antennas[curr] = []
        antennas[curr].append((i,j))

for aType, coords in antennas.items():
    for coord1, coord2 in itertools.combinations(coords, 2):
        i,j = coord1
        antinodes.add((i,j))
        x,y = coord2
        antinodes.add((x,y))
        di,dj = i - x, j - y
        ni,nj = x-di, y - dj
        while aoc.inBounds(ni,nj,input):
            antinodes.add((ni,nj))
            ni,nj = ni-di, nj - dj
        ni,nj = i+di, j+dj
        while aoc.inBounds(ni,nj, input):
            antinodes.add((ni,nj))
            ni,nj = ni+di, nj+dj

print(len(antinodes))


# Part 1
antinodes = set()
antennas = {}
for i in range(len(input)):
    for j in range(len(input[0])):
        curr = input[i][j]
        if curr == ".":
            continue
        if curr not in antennas:
            antennas[curr] = []
        antennas[curr].append((i,j))

for aType, coords in antennas.items():
    for coord1, coord2 in itertools.combinations(coords, 2):
        i,j = coord1
        x,y = coord2
        di,dj = i - x, j - y
        ni,nj = x-di, y - dj
        if aoc.inBounds(ni,nj,input):
            antinodes.add((ni,nj))
        ni,nj = i+di, j+dj
        if aoc.inBounds(ni,nj, input):
            antinodes.add((ni,nj))
print(len(antinodes))