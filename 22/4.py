count = 0

with open("input") as f:
    for line in f:
        line = line.strip().split(',')
        intervals = []
        for interval in line:
            intervals.append(list(map(int, interval.split('-'))))
        int1 = intervals[0]
        int2 = intervals[1]
        if int1[0] <= int2[0] and int1[1] >= int2[1]:
            count += 1
        elif int1[0] >= int2[0] and int1[1] <= int2[1]:
            count += 1
        elif int1[1] >= int2[0] and int1[0] <= int2[1]:
            count += 1
        elif int1[0] <= int2[1] and int1[1] >= int2[0]:
            count += 1

print(count)



# count = 0
#
# with open("input") as f:
#     for line in f:
#         line = line.strip().split(',')
#         intervals = []
#         for interval in line:
#             intervals.append(list(map(int, interval.split('-'))))
#         int1 = intervals[0]
#         int2 = intervals[1]
#         if int1[0] <= int2[0] and int1[1] >= int2[1]:
#             count += 1
#         elif int1[0] >= int2[0] and int1[1] <= int2[1]:
#             count += 1
#
# print(count)
