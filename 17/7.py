import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

from collections import Counter

input = aoc.getInput("input")
root = "vtzay"
# input = aoc.getInput("test-input")
# root = "tknk"

# ktlj (57)
# fwft (72) -> ktlj, cntj, xhth

class Node:
    def __init__(self, weight):
        self.weight = weight
        self.children = []

g = {}
for l in input:
    a = l.split(")")
    n, w = a[0].split(" (")
    w = int(w)
    newNode = Node(w)
    # print(n,w, end=" ")
    if a[1]:
        newNode.children = a[1][len(" -> "):].split(", ")
        # print(newNode.children)
    g[n] = newNode


def get_weights(node):
    curr = g[node]
    if not curr.children:
        return curr.weight, 0
    ws = []
    for c in curr.children:
        ws.append(get_weights(c))
    print(node, ws)
    descendants_weights = [x[0]+x[1] for x in ws]
    descendants_total_weight = sum(descendants_weights)
    if len(set(descendants_weights)) == 1:
        return curr.weight, descendants_total_weight
    count = Counter(descendants_weights)
    for w, c in count.items():
        if c != 1:
            target_weight = w
            break
    for child, descendants in ws:
        if child+descendants != target_weight:
            print(target_weight - descendants)
            exit()


get_weights(root)






# g = {}
# for l in input:
#     a = l.split(") -> ")
#     if len(a) == 1:
#         continue
#     n, edges = a
#     n = l.split(" (")[0]
#     edges = edges.split(", ")
#     for edge in edges:
#         g[edge] = n
# # print(g)
# curr = list(g.keys())[0]
# while curr in g:
#     curr = g[curr]
# print(curr)