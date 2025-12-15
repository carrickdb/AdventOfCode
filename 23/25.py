import aoc, copy
from math import comb, log, ceil
from random import shuffle

input = aoc.getInput("input2")

graph = {}
edges = []
for l in input:
    # jqt: rhn xhk nvd
    n, ms = l.split(": ")
    ms = ms.split(" ")
    if n not in graph:
        graph[n] = [1, set()]
    for m in ms:
        if m not in graph:
            graph[m] = [1, set()]
        graph[m][1].add(n)
        graph[n][1].add(m)
        edges.append((n, m))

# aoc.printGraph(graph)
T = int(ceil(comb(len(input), 2) * log(len(input))))

for _ in range(T):
    shuffle(edges)
    graphcopy = copy.deepcopy(graph)
    edgenum = 0
    while len(graphcopy.keys()) > 2:
        n,m = edges[edgenum]
        if n not in graphcopy:
            print("This should never happen")
            exit()
        graphcopy[n][1].remove(m)
        # print(f"removed {m} from {n}")
        if len(graphcopy[n][1]) == 0:
            # print(f"adding {n}'s edges to {m}")
            graphcopy[m][0] += graphcopy[n][0]
            del graphcopy[n]
        graphcopy[m][1].remove(n)
        # print(f"removed {n} from {m}")
        if len(graphcopy[m][1]) == 0:
            if n in graphcopy:
                # print(f"adding {m}'s edges ({graphcopy[m][0]}) to {n}")
                graphcopy[n][0] += graphcopy[m][0]
            del graphcopy[m]
        edgenum += 1
    # aoc.printGraph(graphcopy)
    # print()
    nums = []
    for n,v in graphcopy.items():
        size, es = v
        nums.append(size)
    if nums[0]+nums[1] == len(graph.keys()):
        print(nums[0]*nums[1])

    # exit()