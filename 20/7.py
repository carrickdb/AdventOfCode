rules = {}
with open("input7") as f:
    for line in f:
        # light red bags contain 1 bright white bag, 2 muted yellow bags.
        start, ends = line.strip().split(" bags contain ")
        bags = []
        if ends != "no other bags.":
            ends = ends.split(", ")
            for bagRule in ends:
                ruleList = bagRule.split()
                bagName = ' '.join(ruleList[1:-1])
                bags.append([bagName, int(ruleList[0])])
        rules[start] = bags

# for bag, otherBags in rules.items():
#     print(bag, otherBags)

numBags = 0
stack = rules["shiny gold"][:]
while stack:
    # print(stack)
    currName, currNum = stack.pop()
    # print(currName, currNum)
    numBags += currNum
    for end, times in rules[currName]:
        for _ in range(currNum):
            stack.append([end, times])

print(numBags)


# # shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# rules = {}
# with open("input7") as f:
#     for line in f:
#         # print(line)
#         start, ends = line.strip().split(" bags contain ")
#         bags = []
#         if ends != "no other bags.":
#             ends = ends.split(", ")
#             for bagRule in ends:
#                 bagName = ' '.join(bagRule.split()[1:-1])
#                 bags.append(bagName)
#         rules[start] = bags
#         # print("'" + start + "'", bags)
#         # print()
#         # input()
#
# """
# dark blue
# bright teal
# striped lime
# drab blue
# dark purple
# pale blue
# """
#
# numBags = 0
# for bag, otherBags in rules.items():
#     stack = otherBags[:]
#     visited = set()
#     # print(rules['dark orange'])
#     while stack:
#         # if bag == "posh black":
#         #     print("stack:", stack)
#         curr = stack.pop()
#         visited.add(curr)
#         if "shiny gold" in curr:
#             numBags += 1
#             # print("bag", bag)
#             break
#         # if bag == "posh black":
#         #     print("curr:", curr)
#         #     print("rules[curr]:", rules[curr])
#         for end in rules[curr]:
#             if end not in visited:
#                 stack.append(end)
#         # input()
#
# print(numBags)
