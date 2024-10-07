graph = {}

def addEdge(graph, a, b):
    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]

with open("input12") as f:
    for line in f:
        a, b = line.strip().split("-")
        if a != "end" and b != "start":
            addEdge(graph, a, b)
        if a != "start" and b != "end":
            addEdge(graph, b, a)

print(graph)

def dfs(graph, curr, visited, path, smallCaveTwice):
    if curr == "end":
        # print("path found:", path)
        return 1
    if curr.islower():
        if curr in visited:
            if smallCaveTwice == True:
                return 0
            smallCaveTwice = True
        visited.add(curr)
    # print("visited:", visited)
    path.append(curr)
    # print("path:", path)
    # print("smallCaveTwice:", smallCaveTwice)
    # input()
    pathsFound = 0
    for node in graph[curr]:
        # print(curr, node, visited, path)
        if (node in visited and not smallCaveTwice) or node not in visited:
            pathsFound += dfs(graph, node, visited.copy(), [x for x in path], smallCaveTwice)
        # else:
        #     print(node, visited)
    return pathsFound

print(dfs(graph, "start", set(), [], False))


# graph = {}
#
# def addEdge(graph, a, b):
#     if a in graph:
#         graph[a].append(b)
#     else:
#         graph[a] = [b]
#
# with open("input12") as f:
#     for line in f:
#         a, b = line.strip().split("-")
#         addEdge(graph, a, b)
#         addEdge(graph, b, a)
#
# print(graph)
#
# def dfs(graph, curr, visited, path):
#     if curr == "end":
#         # print(path)
#         return 1
#     if all(node in visited for node in graph[curr]):
#         return 0
#     path.append(curr)
#     if curr.islower():
#         visited.add(curr)
#     pathsFound = 0
#     for node in graph[curr]:
#         if node not in visited:
#             # print(curr, node, visited, path)
#             pathsFound += dfs(graph, node, visited.copy(), path)
#         # else:
#         #     print(node, visited)
#     return pathsFound
#
#
# print(dfs(graph, "start", set(), []))
