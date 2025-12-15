"""
0
(())
()()

3
(((
(()(()(
))(((((

-1
())
))(

-3
)))
)())())
"""

with open("input") as f:
    directions = f.readline().strip()
    # directions = "()())"
    curr = 0
    pos = 1
    for dir in directions:
        if dir == '(':
            curr += 1
        else:
            curr -= 1
        if curr == -1:
            print(pos)
            break
        pos += 1

# with open("input") as f:
#     directions = f.readline().strip()
#     directions = ")())())"
#     curr = 0
#     for dir in directions:
#         if dir == '(':
#             curr += 1
#         else:
#             curr -= 1
# print(curr)
