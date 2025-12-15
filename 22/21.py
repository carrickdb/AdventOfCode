import sympy

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

rules = {}

with open("input") as f:
    for line in f:
        rulestr = line.strip().split(": ")[-1]
        try:
            curr = Node(int(rulestr))
        except:
            operation = rulestr.split()
            curr = Node(operation[1])
            curr.left = operation[0]
            curr.right = operation[2]
        rules[line[:4]] = curr

def printExpression(curr):
    if curr.right == None and curr.left == None:
        print(curr.val, end='')
    else:
        print('(', end='')
        printExpression(rules[curr.left])
        print(curr.val, end='')
        printExpression(rules[curr.right])
        print(')', end='')

rules["humn"].val = "x"
rules["root"].val = "="
printExpression(rules["root"])

# print()
# right = rules["root"].right
# print(traverse(rules[right]))

# # rtss: 5
# # snvq: thnm * bgfb
#
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.right = None
#         self.left = None
#
# rules = {}
#
# with open("input") as f:
#     for line in f:
#         rulestr = line.strip().split(": ")[-1]
#         try:
#             curr = Node(int(rulestr))
#         except:
#             operation = rulestr.split()
#             if operation[1] == "*":
#                 curr = Node(lambda x, y: x*y)
#             elif operation[1] == "+":
#                 curr = Node(lambda x, y: x+y)
#             elif operation[1] == "-":
#                 curr = Node(lambda x,y: x-y)
#             else:
#                 curr = Node(lambda x,y: x/y)
#             curr.left = operation[0]
#             curr.right = operation[2]
#         rules[line[:4]] = curr
#
# def traverse(curr):
#     if curr.right == None and curr.left == None:
#         return curr.val
#     else:
#         return curr.val(traverse(rules[curr.left]), traverse(rules[curr.right]))
#
# print(traverse(rules["root"]))
