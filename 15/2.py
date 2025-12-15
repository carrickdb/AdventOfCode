with open("input") as f:
    totalRibbon = 0
    for line in f:
        dimensions = list(map(int, line.strip().split('x')))
        minPerimeter = float("inf")
        for i in range(len(dimensions)):
            for j in range(i+1, len(dimensions)):
                minPerimeter = min(minPerimeter, 2 * (dimensions[i] + dimensions[j]))
        totalRibbon += minPerimeter + dimensions[0] * dimensions[1] * dimensions[2]
    print(totalRibbon)


# with open("input") as f:
#     totalArea = 0
#     for line in f:
#         dimensions = list(map(int, line.strip().split('x')))
#         # print(dimensions)
#         minArea = float("inf")
#         for i in range(len(dimensions)):
#             for j in range(i+1, len(dimensions)):
#                 currArea = dimensions[i] * dimensions[j]
#                 totalArea += currArea * 2
#                 minArea = min(currArea, minArea)
#         # print(totalArea, minArea)
#         totalArea += minArea
#     print(totalArea)
