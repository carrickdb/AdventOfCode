import re, queue, math

## Part 2

edges = {}

with open("input") as f:
    dirs = f.readline().strip()
    f.readline()
    for l in f:
        pattern = re.compile("([0-9A-Z][0-9A-Z][0-9A-Z]) = \(([0-9A-Z][0-9A-Z][0-9A-Z]), ([0-9A-Z][0-9A-Z][0-9A-Z])\)")
        matches = pattern.findall(l.strip())[0]
        edges[matches[0]] = [matches[1], matches[2]]

mapping = {
    "L": 0,
    "R": 1
}
steps = 0
q = queue.Queue()
for edge in edges.keys():
    if edge[2] == "A":
        q.put(edge)
patterns = [-1 for i in range(q.qsize())]
while not q.empty():
    lenq = q.qsize()
    found = False
    for i in range(lenq):
        curr = q.get()
        if curr[2] == "Z" and patterns[i] == -1:
            patterns[i] = steps
            print(patterns)
            if all([True if x>0 else False for x in patterns]):
                found = True
                break
        currDir = dirs[steps % len(dirs)]
        q.put(edges[curr][mapping[currDir]])
    if found:
        break
    steps += 1

print(math.lcm(*patterns))



## Part 1

edges = {}

with open("input") as f:
    dirs = f.readline().strip()
    f.readline()
    for l in f:
        pattern = re.compile("([A-Z][A-Z][A-Z]) = \(([A-Z][A-Z][A-Z]), ([A-Z][A-Z][A-Z])\)")
        matches = pattern.findall(l.strip())[0]
        edges[matches[0]] = [matches[1], matches[2]]

print(edges)

curr = "AAA"
steps = 0
mapping = {
    "L": 0,
    "R": 1
}
while curr != "ZZZ":
    curr = edges[curr][mapping[dirs[steps % len(dirs)]]]
    steps += 1

print(steps)
