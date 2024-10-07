# Part 2
trees = []
with open("input3") as f:
    for line in f:
        trees.append(line.strip())

treeProduct = 1
for right, down in [[1,1], [3,1],[5,1],[7,1],[1,2]]:
    numTrees = 0
    x = 0
    for i in range(down, len(trees), down):
        x += right
        x %= len(trees[0])
        numTrees += trees[i][x] == "#"
    treeProduct *= numTrees

print(treeProduct)


# # Part 1
# trees = []
# with open("input3") as f:
#     for line in f:
#         trees.append(line.strip())
#
# x = 0
# numTrees = 0
# for i in range(1, len(trees)):
#     x += 3
#     x %= len(trees[0])
#     numTrees += trees[i][x] == "#"
#
# print(numTrees)
