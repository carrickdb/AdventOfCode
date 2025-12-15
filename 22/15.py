sensors = []
with open("input") as f:
    for line in f:
        line = line.strip().split(': ')
        sx, sy = line[0][len("Sensor at "):].split(', ')
        sx = int(sx[2:])
        sy = int(sy[2:])
        bx, by = line[1][len("closest beacon is at "):].split(', ')
        bx = int(bx[2:])
        by = int(by[2:])
        dy = abs(sy - by)
        dx = abs(sx - bx)
        distance = dy + dx
        sensors.append(((sx, sy), distance))

def checkSensors(x, y):
    for sensor, distance in sensors:
        ox, oy = sensor
        d = abs(ox-x) + abs(oy-y)
        if d <= distance:
            return False
    return True

def inBounds(x):
    return x >= 0 and x <= 4000000

for j in range(len(sensors)):
    sensor, distance = sensors[j]
    d = distance + 1
    x, y = sensor
    for i in range(d):
        for cx, cy in [(x-i, y-(d-i)), (x-i, y+(d-i)), (x+i, y+(d-i)), (x+i, y-(d-i))]:
            if inBounds(cx) and inBounds(cy) and checkSensors(cx, cy):
                print(cx, cy)
                # exit()







# # Sensor at x=101890, y=3940049: closest beacon is at x=955472, y=3457514
#
# target = 2000000
# # target = 10
# positions = set()
# with open("input") as f:
#     for line in f:
#         line = line.strip().split(': ')
#         sx, sy = line[0][len("Sensor at "):].split(', ')
#         sx = int(sx[2:])
#         sy = int(sy[2:])
#         bx, by = line[1][len("closest beacon is at "):].split(', ')
#         bx = int(bx[2:])
#         by = int(by[2:])
#         dy = abs(sy - by)
#         dx = abs(sx - bx)
#         distance = dy + dx
#         # print(distance)
#         leftOver = distance - abs(sy - target)
#         # print(leftOver)
#         for i in range(leftOver+1):
#             positions.add(sx + i)
#             positions.add(sx - i)
#
# # print(positions)
# print(len(positions)-1)
