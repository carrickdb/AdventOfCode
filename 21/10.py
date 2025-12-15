# Part 2

scores = {
    "(" : 1,
    "[" : 2,
    "{" : 3,
    "<" : 4,
}

matches = {
    ")" : "(",
    "]" : "[",
    "}" : "{",
    ">" : "<",
}

lineScores = []
with open("input10") as f:
    for line in f:
        stack = []
        next = False
        for char in line.strip():
            if char in matches:
                if stack[-1] == matches[char]:
                    stack.pop()
                else:
                    next = True
                    break
            else:
                stack.append(char)
        if next:
            continue
        score = 0
        while stack:
            char = stack.pop()
            if char not in matches:
                score *= 5
                score += scores[char]
        lineScores.append(score)

lineScores = sorted(lineScores)
print(lineScores[len(lineScores)//2])


# # Part 1
# scores = {
#     ")" : 3,
#     "]" : 57,
#     "}" : 1197,
#     ">" : 25137,
# }
#
# matches = {
#     ")" : "(",
#     "]" : "[",
#     "}" : "{",
#     ">" : "<",
# }
# score = 0
# with open("input10") as f:
#     for line in f:
#         stack = []
#         for char in line.strip():
#             if char in scores:
#                 if stack[-1] != matches[char]:
#                     score += scores[char]
#                     break
#                 else:
#                     stack.pop()
#             else:
#                 stack.append(char)
# print(score)
