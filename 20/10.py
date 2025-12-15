adapters = []

with open("input10") as f:
    adapters = list(map(int, f.readlines()))

deviceJolts = max(adapters) + 3
memos = [False for _ in range(deviceJolts)]
adapters = sorted(adapters)
# print(adapters)
for i in range(len(adapters)-1, -1, -1):
    curr = adapters[i]
    memos[curr] = curr+3==deviceJolts or any([(curr+j < deviceJolts and memos[curr+j] == True) for j in range(1, 4)])

print(memos)
i = 0
ways = [0 for i in range(deviceJolts-2)]
ways[-1] = 1
for i in range(len(ways)-2, -1, -1):
    if memos[i]:
        # print([ways[i+j] if i+j<deviceJolts-2 else 0 for j in range(1,4)])
        ways[i] = sum([ways[i+j]*memos[i] if i+j<deviceJolts-2 else 0 for j in range(1,4)])

print(adapters[:4])
print(ways[:4])
print(sum(ways[1:4]))


# adapters = []
#
# with open("input10") as f:
#     adapters = list(map(int, f.readlines()))
#
# deviceJolts = max(adapters) + 3
# memos = [False for _ in range(deviceJolts)]
# adapters = sorted(adapters)
# print(adapters)
# for i in range(len(adapters)-1, -1, -1):
#     curr = adapters[i]
#     memos[curr] = curr+3==deviceJolts or any([(curr+j < deviceJolts and memos[curr+j] == True) for j in range(1, 4)])
#
# i = 0
# ones = 0
# threes = 0
# while i < deviceJolts-2:
#     if i+3 == deviceJolts:
#         threes += 1
#         break
#     for j in range(1,4):
#         if memos[i+j]:
#             ones += j == 1
#             threes += j == 3
#             i += j
#             break
#
# print(ones, threes, ones*threes)
