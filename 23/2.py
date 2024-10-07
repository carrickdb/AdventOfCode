# Regex redux

import re

target = {"red":12, "green":13, "blue":14}
possible = 0
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
pattern = re.compile(r'Game (\d+): (?:\d+ (\b)(?:)(?:;|$))+')
with open("input") as f:
    for l in f:
        matches = pattern.findall(l.strip())

        ok = True
        for d in draws:
            cubes = d.split(", ")
            for c in cubes:
                num, color = c.split(" ")
                num = int(num)
                if num > target[color]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            possible += id

print(possible)



# ## Part 2
# total = 0
# with open("input2") as f:
#     for l in f:
#         data = l.strip().split(": ")
#         fewest = {"red":0, "green":0, "blue":0}
#         draws = data[1].split("; ")
#         for d in draws:
#             cubes = d.split(", ")
#             for c in cubes:
#                 num, color = c.split(" ")
#                 num = int(num)
#                 fewest[color] = max(fewest[color], num)
#         power = 1
#         for num in fewest.values():
#             power *= num
#         total += power

# print(total)


# ## Part 1
# # 12 red cubes, 13 green cubes, and 14 blue cubes
# target = {"red":12, "green":13, "blue":14}
# possible = 0
# # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# with open("input") as f:
#     for l in f:
#         data = l.strip().split(": ")
#         id = int(data[0].split(" ")[1])
#         draws = data[1].split("; ")
#         ok = True
#         for d in draws:
#             cubes = d.split(", ")
#             for c in cubes:
#                 num, color = c.split(" ")
#                 num = int(num)
#                 if num > target[color]:
#                     ok = False
#                     break
#             if not ok:
#                 break
#         if ok:
#             possible += id

# print(possible)