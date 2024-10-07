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

for node, node_list in adjacency_list.items():
    print(node, ":", node_list)


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

# for node, count in incoming_counts.items():
#     print(node, count)

# find nodes without parents
root_nodes = []
for node, count in incoming_counts.items():
    if count == 0:
        root_nodes.append(node)

root_nodes = sorted(root_nodes)
counter = 0
order = []
num_workers = 5
jobs = [None for i in range(num_workers)]
remaining_time = [-1 for i in range(num_workers)]

while len(order) < len(adjacency_list.keys()):
    """
    if workers are available:
        loop through the jobs.
        if any are None:
            assign a job from root_nodes

    loop through the jobs to find the minimum one
    travel forwards through time
    deduct minimum remaining time from every job
    add done job to order
        -> pop node off DAG, put into root_nodes
    set the done job to None

    """
    for i in range(num_workers):
        if not jobs[i] and root_nodes:
            jobs[i] = root_nodes[0]
            remaining_time[i] = 60 + ord(root_nodes[0]) - ord('A') + 1
            if len(root_nodes) >= 1:
                root_nodes = root_nodes[1:]
            else:
                root_nodes = []

    print(jobs)
    print(remaining_time)

    min_time_remaining = float("inf")
    for i in range(num_workers):
        if remaining_time[i] > -1:
            min_time_remaining = min(min_time_remaining, remaining_time[i])

    counter += min_time_remaining
    done_job = None
    for i in range(num_workers):
        if remaining_time[i] > -1:
            remaining_time[i] -= min_time_remaining
            if remaining_time[i] == 0:
                done_job = jobs[i]
                remaining_time[i] = -1
                jobs[i] = None

    print(done_job)
    order.append(done_job)

    # deduct 1 incoming edge from all nodes that the done job has to
    curr_edges = adjacency_list[done_job]
    for to_node in curr_edges:
        incoming_counts[to_node] -= 1
        if incoming_counts[to_node] <= 0:
            root_nodes.append(to_node)
    root_nodes = sorted(root_nodes)
    print()

print(''.join(order))
print(counter)

"""

order = [A, B, C, D, E]

workers: 1 2 3 4 5
         A B C D E
         5 10 15 20 25

for each second:
keep hold of the minimum duration
fast-forward by the minimum duration
if jobs are done, then assign a new job to those workers

optimize?: brute force: literally just try every option


"""


