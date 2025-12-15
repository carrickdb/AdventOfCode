# total = 0
# with open("totals-take2") as f:
#     for line in f:
#         total += int(line.strip())
# print(total)
#

space_left = 30000000 - (70000000 - 40532950)
print(space_left)
closest = None
with open("totals-take2") as f:
    for line in f:
        curr = int(line.strip())
        if curr >= space_left and (closest == None or curr < closest):
            closest = curr

print(closest)
# totals = sorted(totals)
# for total in totals:
#     print(total)

# 5952839
# 10669187
# 1011938
