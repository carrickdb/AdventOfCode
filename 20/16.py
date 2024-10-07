with open("input16") as f:
    input = f.read().split("your ticket:")

# ['class: 1-3 or 5-7\nrow: 6-11 or 33-44\nseat: 13-40 or 45-50\n\n', '\n7,1,14\n\nnearby tickets:\n7,3,47\n40,4,50\n55,2,20\n38,6,12\n']

rules = input[0].split('\n')
# ['class: 1-3 or 5-7', 'row: 6-11 or 33-44', 'seat: 13-40 or 45-50', '', '']
ranges = []
mapping = []
for i in range(len(rules)):
    if rules[i] == '':
        continue
    name = rules[i].split(": ")[0]
    mapping.append([name, set()])
    newRule = rules[i].split(": ")[1].split(" or ")
    for j in range(len(newRule)):
        newRule[j] = list(map(int, newRule[j].split('-')))
    ranges.append(newRule)

yourTicket = list(map(int, input[1].split('\n')[1].split(',')))
nearbyTickets = input[1].split('nearby tickets:')[1].split('\n')
tickets = []
for tick in nearbyTickets:
    if tick != '':
        tickets.append(list(map(int, tick.split(','))))

valid = []
for tick in tickets:
    for val in tick:
        invalid = True
        for rule in ranges:
            for lb, ub in rule:
                if lb <= val <= ub:
                    invalid = False  # valid for some rule
                    break
            if not invalid:
                break
        if invalid:
            break
    if not invalid:
        valid.append(tick)

for k in range(len(ranges)):
    for j in range(len(valid[0])):
        rightRule = True
        for i in range(len(valid)):
            curr = valid[i][j]
            validVal = False
            for lb, ub in ranges[k]:
                if lb <= curr <= ub:
                    validVal = True
                    break
            if not validVal:
                rightRule = False
                break
        if rightRule:
            mapping[k][1].add(j)

def getMapping(mapping, doneSet):
    # print(mapping, doneSet)
    if len(doneSet) == len(mapping):
        return mapping, doneSet
    fewestPossNum = float("inf")
    fewestPoss = None
    fewestName = None
    for name, possibilities in mapping:
        if len(possibilities) < fewestPossNum and name not in doneSet:
            fewestPossNum = len(possibilities)
            fewestPoss = list(possibilities)[0]
            fewestName = name
    # print("fewestPoss", fewestPoss)
    doneSet.add(fewestName)
    # print("doneSet", doneSet)
    for name, possibilities in mapping:
        if fewestPoss in possibilities and name not in doneSet:
            possibilities.remove(fewestPoss)
    # print()
    return getMapping(mapping, doneSet)

mapping, doneSet = getMapping(mapping, set())
print(mapping)
total = 1
for name, assignment in mapping:
    if name.startswith("departure"):
        print(yourTicket[list(assignment)[0]])
        total *= yourTicket[list(assignment)[0]]
print(total)


# with open("input16") as f:
#     input = f.read().split("your ticket:")
#
# # ['class: 1-3 or 5-7\nrow: 6-11 or 33-44\nseat: 13-40 or 45-50\n\n', '\n7,1,14\n\nnearby tickets:\n7,3,47\n40,4,50\n55,2,20\n38,6,12\n']
#
# rules = input[0].split('\n')
# # ['class: 1-3 or 5-7', 'row: 6-11 or 33-44', 'seat: 13-40 or 45-50', '', '']
# ranges = []
# for i in range(len(rules)):
#     if rules[i] == '':
#         continue
#     newRule = rules[i].split(": ")[1].split(" or ")
#     for j in range(len(newRule)):
#         newRule[j] = list(map(int, newRule[j].split('-')))
#     ranges.append(newRule)
#
# nearbyTickets = input[1].split('nearby tickets:')[1].split('\n')
# tickets = []
# for tick in nearbyTickets:
#     if tick != '':
#         tickets.append(list(map(int, tick.split(','))))
#
# total = 0
# for tick in tickets:
#     for val in tick:
#         invalid = True
#         for rule in ranges:
#             for lb, ub in rule:
#                 if lb <= val <= ub:
#                     invalid = False
#                     break
#             if not invalid:
#                 break
#         if invalid:
#             total += val
#
# print(total)
