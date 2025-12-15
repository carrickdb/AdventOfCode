import json, functools

def compare(l, r):
    # If both values are lists, compare the first value of each list, then the second value, and so on. If the left list runs out of items first, the inputs are in the right order. If the right list runs out of items first, the inputs are not in the right order. If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.
    for i in range(min(len(r), len(l))):
        currR = r[i]
        currL = l[i]
        if type(currL) == list and type(currR) == list:
            res = compare(currL, currR)
            if res != None:
                return res
        elif type(currR) == list:
            # If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then retry the comparison. For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2); the result is then found by instead comparing [0,0,0] and [2].
            res = compare([currL], currR)
            if res != None:
                return res
        elif type(currL) == list:
            res = compare(currL, [currR])
            if res != None:
                return res
        else:
            # If the left integer is lower than the right integer, the inputs are in the right order. If the left integer is higher than the right integer, the inputs are not in the right order. Otherwise, the inputs are the same integer; continue checking the next part of the input.
            if currL < currR:
                return -1
            if currR < currL:
                return 1
    if len(l) < len(r):
        return -1
    if len(r) < len(l):
        return 1

lines = []
with open("input") as f:
    for line in f:
        line = line.strip()
        if line != "\n" and line != '':
            lines.append(json.loads(line))

two = [[2]]
six = [[6]]
lines.append(two)
lines.append(six)

lines = sorted(lines, key=functools.cmp_to_key(compare))
i = lines.index(two) + 1
j = lines.index(six) + 1
print(i*j)



# import json
#
# def compare(l, r):
#     # If both values are lists, compare the first value of each list, then the second value, and so on. If the left list runs out of items first, the inputs are in the right order. If the right list runs out of items first, the inputs are not in the right order. If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.
#     for i in range(min(len(r), len(l))):
#         currR = r[i]
#         currL = l[i]
#         if type(currL) == list and type(currR) == list:
#             res = compare(currL, currR)
#             if res != None:
#                 return res
#         elif type(currR) == list:
#             # If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then retry the comparison. For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2); the result is then found by instead comparing [0,0,0] and [2].
#             res = compare([currL], currR)
#             if res != None:
#                 return res
#         elif type(currL) == list:
#             res = compare(currL, [currR])
#             if res != None:
#                 return res
#         else:
#             # If the left integer is lower than the right integer, the inputs are in the right order. If the left integer is higher than the right integer, the inputs are not in the right order. Otherwise, the inputs are the same integer; continue checking the next part of the input.
#             if currL < currR:
#                 return True
#             if currR < currL:
#                 return False
#     if len(l) < len(r):
#         return True
#     if len(r) < len(l):
#         return False
#
# def getLines():
#     with open("input") as f:
#         return f.read().split("\n\n")
#
# lines = getLines()
# i = 1
# total = 0
# for j in range(len(lines)):
#     curr = lines[j].strip().split('\n')
#     one, two = list(map(json.loads, curr))
#     res = compare(one, two)
#     if res == None:
#         print(i, "is None")
#     elif res == True:
#         total += i
#         print("right", i)
#     elif res == False:
#         print("wrong", i)
#     i += 1
#
# print(total)
