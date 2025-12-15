def getSeat(partitions, ub):
    lb = 0
    for part in partitions:
        if part == "F" or part == "L":
            ub = lb + (ub-lb)//2
        if part == "B" or part == "R":
            lb += (ub-lb)//2
    return lb

def getSeatID(bp):
    # print(getSeat(bp[:7], 128))
    # print(getSeat(bp[7:], 8))
    return getSeat(bp[:7], 128)*8 + getSeat(bp[7:], 8)

seats = []
with open("input5") as f:
    for line in f:
        seats.append(getSeatID(line.strip()))

seats = sorted(seats)
curr = seats[0]
for next in seats[1:]:
    if next - curr == 2:
        print(curr + 1)
    curr = next

# def getSeat(partitions, ub):
#     lb = 0
#     for part in partitions:
#         if part == "F" or part == "L":
#             ub = lb + (ub-lb)//2
#         if part == "B" or part == "R":
#             lb += (ub-lb)//2
#     return lb
#
# def getSeatID(bp):
#     # print(getSeat(bp[:7], 128))
#     # print(getSeat(bp[7:], 8))
#     return getSeat(bp[:7], 128)*8 + getSeat(bp[7:], 8)
#
# maxID = float("-inf")
# with open("input5") as f:
#     for line in f:
#         maxID = max(maxID, getSeatID(line.strip()))
#
# print(maxID)
