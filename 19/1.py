
total = 0
with open("input") as f:
    for line in f:
        num = int(line.strip())
        while num > 0:
            num = max(0, num//3 - 2)
            total += num

print(total)

# total = 0
# with open("input") as f:
#     for line in f:
#         total += int(line.strip())//3 - 2
#
# print(total)
