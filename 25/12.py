import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

with open("input") as f:
    input = f.read().split('\n\n')

shapes = input[:-1]
regions = input[-1]

shape_counts = []
for shape in shapes:
    shape_counts.append(shape.count("#"))

print(shape_counts)
ok = 0
for region in regions.split('\n'):
    dims, counts = region.split(": ")
    x,y = list(map(int, dims.split("x")))
    counts = list(map(int, counts.split(" ")))
    needed_space = sum(counts[i]*shape_counts[i] for i in range(len(counts)))
    if x*y >= needed_space:
        print(dims, counts, x*y, needed_space)
        ok += 1

print(ok)