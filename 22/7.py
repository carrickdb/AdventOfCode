class Node:

    def __init__(self, name, parent, isDir, size):
        self.name = name
        self.parent = parent
        self.isDir = isDir
        self.size = size
        self.children = {}

root = Node("/", None, True, 0)
root.parent = root
curr = root
with open("input") as f:
    for line in f:
        line = line.strip().split()
        if line[0] == "$":
            if line[1] == "cd":
                dir = line[2]
                if dir == "..":
                    curr = curr.parent
                elif dir == "/":
                    curr = root
                else:
                    curr = curr.children[dir]
        else:
            metadata, name = line
            if metadata == "dir":
                curr.children[name] = Node(name, curr, True, 0)
            else:
                curr.children[name] = Node(name, curr, False, int(metadata))
    # print(curr.name)
    # for child in curr.children.values():
    #     print(child.name, child.size, end=' ')
    # print()

def getTotals(node):
    if not node.isDir:
        return node.size
    total = 0
    for child in node.children.values():
        total += getTotals(child)
    print(total)
    return total

getTotals(root)

class Node:

    def __init__(self, val, size, parent, isDir):
        self.val = val
        self.size = size
        self.children = {}
        self.parent = parent
        self.isDir = isDir

root = Node("/", 0, None, True)
root.parent = root
with open("input") as f:
    curr = root
    for line in f:
        line = line.strip().split()
        if line[0] == "$":
            if line[1] == "cd":
                # print("hello")
                dir = line[2]
                if dir == "..":
                    curr = curr.parent
                elif dir == "/":
                    curr = root
                elif dir not in curr.children:
                    curr.children[dir] = Node(dir, 0, curr, True)
                    curr = curr.children[dir]
                else:
                    curr = curr.children[dir]
        else:
            info = line[0]
            name = line[1]
            if info == "dir":
                curr.children[name] = Node(name, 0, curr, True)
            else:
                curr.children[name] = Node(name, int(info), curr, False)

curr = root

def getSums(node):
    total = 0
    # print(node.val, end=' ')
    for child in node.children.values():
        if child.isDir:
            total += getSums(child)
        else:
            total += child.size
    # print()
    if total > 0 and total <= 100000:
        print(total)
    return total

print(getSums(curr))
