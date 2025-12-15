from time import sleep

edges = []

with open("input.txt") as f:
    # Step A must be finished before step I can begin.
    for line in f:
        line_list = line.strip().split()
        edge = (line_list[1], line_list[7])
        edges.append(edge)

adjacency_list = {}
# node: [node, node]
# build the graph
for edge in edges:
    from_node, to_node = edge
    if from_node in adjacency_list:
        adjacency_list[from_node].append(to_node)
    else:
        adjacency_list[from_node] = [to_node]
    if to_node not in adjacency_list:
        adjacency_list[to_node] = []

# for node, node_list in adjacency_list.items():
#     print(node, ":", node_list)


# count incoming edges
incoming_counts = {}
for node, to_nodes in adjacency_list.items():
    if node not in incoming_counts:
        incoming_counts[node] = 0
    for to_node in to_nodes:
        if to_node in incoming_counts:
            incoming_counts[to_node] += 1
        else:
            incoming_counts[to_node] = 1

for node, count in incoming_counts.items():
    print(node, count)

# find nodes without parents
root_nodes = []
for node, count in incoming_counts.items():
    if count == 0:
        root_nodes.append(node)

curr = sorted(root_nodes)[0]
order = [curr]

while len(order) < len(adjacency_list.keys()):
    if len(root_nodes) >= 1:
        root_nodes = root_nodes[1:]
    else:
        root_nodes = []
    curr_edges = adjacency_list[curr]
    for to_node in curr_edges:
        incoming_counts[to_node] -= 1
        if incoming_counts[to_node] <= 0:
            root_nodes.append(to_node)
    root_nodes = sorted(root_nodes)
    curr = root_nodes[0]
    order.append(curr)

print(''.join(order))










