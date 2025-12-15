


cloth = []

for i in range(1000):
    row = [0 for i in range(1000)]
    cloth.append(row)


with open ("input.txt") as f:
    for line in f:
        ID, meas = line.strip().split("@")
        measurements = []
        delimiters = [",", ":", "x"]
        for delimiter in delimiters:
            curr, meas = meas.split(delimiter)
            measurements.append(int(curr))
        measurements.append(int(meas))
        left = measurements[0]
        top = measurements[1]
        for row in range(measurements[2]):
            for col in range(measurements[3]):
                cloth[left+row][top+col] += 1

with open("input.txt") as f:
    for line in f:
        ID, meas = line.strip().split("@")
        measurements = []
        delimiters = [",", ":", "x"]
        for delimiter in delimiters:
            curr, meas = meas.split(delimiter)
            measurements.append(int(curr))
        measurements.append(int(meas))
        left = measurements[0]
        top = measurements[1]
        overlap = False
        for row in range(measurements[2]):
            for col in range(measurements[3]):
                if cloth[left+row][top+col] > 1:
                    overlap = True
        if not overlap:
            print(ID)
            break




#
# class Interval:
#
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#         self.num_overlaps = 1
#         self.next = None
#
# class Row:
#
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#         self.intervals = None
#
#
#
#
#
# root = Row(-1)
#
# for claim in claims:
#     curr = root.next
#     while curr:
#         # find the row, if it's there
#         if curr.val == claim[0]:
#             break
#         elif curr.val < claim[0]:
#             curr = curr.next
#     if not curr:
#         # add a new row of intervals
#         # just create an interval
#
#         continue
#
#     # if there is no interval to revise, find the place to insert an interval
#
#     # revise the interval, creating any new nodes if necessary
#
#
#
#
#
#
# """
#
# intervals
# LL of LLs
# 66 -> 12-50 (1) -> 80-82 -> 83-93 (2) -> ...
# v
# 122 ->
# v
# 349 ->
#
#
#
# """