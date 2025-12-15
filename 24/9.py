import itertools
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

input = aoc.getInput("input")[0]
# input = aoc.getInput("test-input")[0]

disk = []
id = 0
for i in range(len(input)):
    num = int(input[i])
    if i%2!=0:
        disk.extend(["."]*num)
    else:
        disk.extend([id]*num)
        id += 1
id -= 1

e = len(disk)-1
while id >= 0:
    while disk[e] != id:
        e -= 1
    ee = e
    while disk[e] == id:
        e -= 1
    s = 0
    while s <= e:
        while disk[s] != '.' and s <= e:
            s += 1
        ss = s
        while disk[s] == "."  and s <= e:
            s += 1
        fileblocklen = ee-e
        if s-ss >= fileblocklen:
            for x in range(fileblocklen):
                disk[ss+x] = id
            for x in range(e+1,ee+1):
                disk[x] = '.'
            break
    id -= 1
cs = 0
for i in range(len(disk)):
    if disk[i] != ".":
        cs += i * disk[i]
print(cs)

# Part 1
disk = []
id = 0
for i in range(len(input)):
    num = int(input[i])
    if i%2!=0:
        disk.extend(["."]*num)
    else:
        disk.extend([id]*num)
        id += 1
s,e = 0,len(disk)-1
while s < e:
    if disk[s] == ".":
        while disk[e] == ".":
            e -= 1
        disk[s], disk[e] = disk[e], "."
        s += 1
    else:
        s += 1

cs = 0
for i in range(len(disk)):
    if disk[i] != ".":
        cs += i * disk[i]
print(cs)