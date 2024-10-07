with open("input13") as f:
    departure = int(f.readline().strip())
    allids = f.readline().strip().split(',')
    minutes = []
    ids = []
    product = 1
    for i in range(len(allids)):
        if allids[i] != 'x':
            ids.append(int(allids[i]))
            minutes.append(i)
            product *= int(allids[i])

# print(remainders)
# print(ids)
# print(product)

total = 0
for i in range(len(minutes)):
    b = product//ids[i]
    # print(b, pow(b, -1, ids[i]))
    total += ((ids[i]-minutes[i]) * b * pow(b, -1, ids[i]))

print(total % product)



"""
find x st
ai = x
bj = x+1
ck = x+2
dl = x+3
...

ai = bj-1
bj-1 = ck-2
ck-2 = dl-3

ai - bj = -1
bj - ck = -1
ck - dl = -1
"""






# with open("input13") as f:
#     departure = int(f.readline().strip())
#     allids = f.readline().strip().split(',')
#     ids = []
#     for id in allids:
#         if id != 'x':
#             ids.append(int(id))
#
# minwait = float("inf")
# minbus = None
# for curr in ids:
#     wait = ((departure//curr + 1) * curr)-departure
#     if wait < minwait:
#         minwait = wait
#         minbus = curr
#
# print(minbus * (((departure//minbus + 1) * minbus)-departure))
