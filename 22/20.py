nums = []
with open("input") as f:
    for line in f:
        nums.append(int(line.strip())*811589153)

lennums = len(nums)

mixed = [(num, i) for i, num in enumerate(nums)]
# for num, _ in mixed:
#     print(num, end=' ')
# print()
# print()
for _ in range(10):
    for i in range(lennums):
        currVal = nums[i]
        currI = None
        for j in range(len(mixed)):
            if mixed[j][1] == i:
                currI = j
        del mixed[currI]
        # print("deleting", currVal, "at", currI)
        newI = (currI + currVal) % len(mixed)
        if newI == 0:
            mixed.append((currVal, i))
            # print("placed at", len(mixed)-1)
        else:
            mixed.insert(newI, (currVal, i))
            # print("placed at", newI)
        # for num, _ in mixed:
        #     print(num, end=' ')
        # print()
        # print()


# nums = []
# with open("input") as f:
#     for line in f:
#         nums.append(int(line.strip()))
#
# lennums = len(nums)
#
# mixed = [(num, i) for i, num in enumerate(nums)]
# # for num, _ in mixed:
# #     print(num, end=' ')
# # print()
# # print()
# for i in range(lennums):
#     currVal = nums[i]
#     currI = None
#     for j in range(len(mixed)):
#         if mixed[j][1] == i:
#             currI = j
#     del mixed[currI]
#     # print("deleting", currVal, "at", currI)
#     newI = (currI + currVal) % len(mixed)
#     if newI == 0:
#         mixed.append((currVal, i))
#         # print("placed at", len(mixed)-1)
#     else:
#         mixed.insert(newI, (currVal, i))
#         # print("placed at", newI)
#     # for num, _ in mixed:
#     #     print(num, end=' ')
#     # print()
#     # print()


zero = None
for i in range(len(mixed)):
    if mixed[i][0] == 0:
        zero = i
        break

first = (zero + 1000) % lennums
second = (zero + 2000) % lennums
third = (zero + 3000) % lennums
print(mixed[first][0] + mixed[second][0] + mixed[third][0])
# print(numsI[first], numsI[second], numsI[third])



# class Node:
#
#     def __init__(self, val, i):
#         self.val = val
#         self.i = i
#         self.next = None
#         self.prev = None
#
# head = Node(nums[0], 0)
# tail = head
# curr = head
# for i in range(lennums):
#     curr.next = Node(nums[i], i)
#     curr.next.prev = curr
#     curr = curr.next
#     tail = curr
#
# for i in range(lennums):
#     target = None
#     curr = head
#     while curr:
#         if curr.i == i:
#             break
#     newPos = curr
#     for _ in range(abs(curr.val)):
#         if curr.val < 0:
#             if newPos.prev == None:
#                 newPos = tail
#             else:
#                 newPos = newPos.prev
#         else:
#             if newPos.next == None:
#                 newPos = head
#             else:
#                 newPos = newPos.next
#     if newPos == head:
#
#         tail.next = curr
#     elif newPos == tail:
#
#     if curr == head:
#         head = curr.next
#         head.prev = None
#     elif curr == tail:
#         tail = tail.prev
#         tail.curr = None
#     else:
#         prev = curr.prev
#         next = curr.next
#         prev.next = next
#         next.prev = prev
