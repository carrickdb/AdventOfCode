buffer = []

invalid = None

allNums = []

with open("input9") as f:
    oldest = 0
    for line in f:
        curr = int(line.strip())
        allNums.append(curr)
        if len(buffer) < 25:
            buffer.append(curr)
            continue
        sumFound = False
        for i in range(len(buffer)):
            for j in range(i+1, len(buffer)):
                if buffer[i] + buffer[j] == curr:
                    sumFound = True
                    buffer[oldest] = curr
                    oldest = (oldest+1) % len(buffer)
                    break
            if sumFound:
                break
        if not sumFound:
            invalid = curr
            break

print(invalid)

for windowSize in range(2, len(allNums)):
    for i in range(len(allNums)-windowSize):
        slice = allNums[i:i+windowSize]
        if sum(slice) == invalid:
            print(min(slice) + max(slice))
            assert False



# buffer = []
#
# with open("input9") as f:
#     oldest = 0
#     for line in f:
#         curr = int(line.strip())
#         if len(buffer) < 25:
#             buffer.append(curr)
#             continue
#         print(buffer)
#         sumFound = False
#         for i in range(len(buffer)):
#             for j in range(i+1, len(buffer)):
#                 if buffer[i] + buffer[j] == curr:
#                     sumFound = True
#                     buffer[oldest] = curr
#                     oldest = (oldest+1) % len(buffer)
#                     break
#             if sumFound:
#                 break
#         if not sumFound:
#             print(curr)
#             break
