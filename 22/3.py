total = 0
with open("input") as f:
    i = 0
    seen = [None, None, None]
    for line in f:
        if i > 2:
            c = seen[0].intersection(seen[1])
            c = c.intersection(seen[2])
            c = list(c)[0]
            if ord(c) >= ord('a') and ord(c) <= ord('z'):
                total += ord(c) - ord('a') + 1
            else:
                total += ord(c) - ord('A') + 27
            i = 0
        line = line.strip()
        seen[i] = set(line)
        i += 1
c = seen[0].intersection(seen[1])
c = c.intersection(seen[2])
c = list(c)[0]
if ord(c) >= ord('a') and ord(c) <= ord('z'):
    total += ord(c) - ord('a') + 1
else:
    total += ord(c) - ord('A') + 27
print(total)


#
# total = 0
# with open("input") as f:
#     for line in f:
#         seen = set()
#         line = line.strip()
#         for c in line[:len(line)//2]:
#             seen.add(c)
#         for c in line[len(line)//2:]:
#             if c in seen:
#                 print(c)
#                 if ord(c) >= ord('a') and ord(c) <= ord('z'):
#                     total += ord(c) - ord('a') + 1
#                 else:
#                     total += ord(c) - ord('A') + 27
#                 break
#
# print(total)
