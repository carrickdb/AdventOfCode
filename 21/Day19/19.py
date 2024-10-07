# Part 1

def rotateRight(points):
    matrix = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
    newPoints = []
    for i in range(len(points)):
        newPoint = []
        for j in range(len(matrix)):
            newCoord = 0
            for k in range(len(matrix[j])):
                newCoord += points[i][k] * matrix[j][k]
            newPoint.append(newCoord)
        newPoints.append(newPoint)
    return newPoints

scanners = []
with open("input") as f:
    scanner = []
    for line in f:
        if len(line) < 2:
            scanners.append(scanner)
            continue
        if line[1] == "-":
            scanner = []
            continue
        scanner.append(list(map(int, line.strip().split(","))))

if scanner:
    scanners.append(scanner)

beacons = [x for x in scanners[0]]
def match(points):
    global beacons
    numIntersections = 0
    translations = []
    for point in points:
        currTranslation = set()
        for beacon in beacons:
            currTranslation.add(tuple([point[i]-beacon[i] for i in range(3)]))
        translations.append(currTranslation)
    intersection = translations[0]
    for translation in translations:
        intersection &= translation
    if len(intersection) != 0:
        print(len(intersection))
        print(intersection)
        assert False


scanners = scanners[1:]
while scanners:
    todoScanners = []
    for scanner in scanners:
        done = False
        if not match(scanner):
            for i in range(3):
                points = rotateRight(scanner)
                if match(points):
                    done = True
                    break
                
        if done:
            continue
        todoScanners.append(scanner)
    scanners = todoScanners


# # Attempt 1
# def getVectors(i, coords):
#     vectors = set()
#     # vectors = []
#     for j in range(len(coords)):
#         if i != j:
#             inRange = True
#             for k in range(3):
#                 if abs(coords[j][k] - coords[i][k]) > 2000:
#                     inRange = False
#                     break
#             if inRange:
#                 vectors.add(tuple([coords[j][k] - coords[i][k] for k in range(3)]))
#             # vectors.append(tuple([coords[j][k] - coords[i][k] for k in range(3)]))
#     return vectors
#
# beacons = set(scanners[0])
# vectorSets = []
# for i in range(len(beacons)):
#     vectorSets.append([beacons[i], getVectors(i, beacons)])
# # print(vectorSets)
# # print()
#
# def checkBeacons(currVectors):
#     global vectorSets
#     newBeacons = None
#     for _, vectors in vectorSets:
#         if len(vectors.intersection(currVectors)) > 10:
#             newBeacons = vectors - currVectors
#             # print("size of intersection:", len(vectors.intersection(currVectors)))
#             for newBeacon in newBeacons:
#                 beacons.append(list(newBeacon))
#             for i in range(len(beacons)):
#                 vectorSets.append([beacons[i], getVectors(i, beacons)])
#             return True
#     return False
#
# # 38 beacons in 0 and 1
# scanners = scanners[1:]
# while scanners:
#     todoScanners = []
#     for scanner in scanners:
#         intersectionFound = False
#         for direction in range(6):
#             newPoints = translatePoints(scanner, direction)
#             for i in range(len(scanner)):
#                 currVectors = getVectors(i, newPoints)
#                 intersectionFound |= checkBeacons(currVectors)
#                 currVectors = getVectors(i, [[-x, -y, -z] for x,y,z in newPoints])
#                 intersectionFound |= checkBeacons(currVectors)
#                 # print(currVectors)
#         if not intersectionFound:
#             todoScanners.append(scanner)
#     scanners = todoScanners
#
# print(len(beacons))
