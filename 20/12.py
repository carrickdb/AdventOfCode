x, y = 0, 0
currDir = 0
wpx, wpy = 10,1

def rotate(x, y, rotationDirection, numRotations):
    d = [(x, y), (y, -x), (-x, -y), (-y, x)]
    if rotationDirection == "L":
        return d[-numRotations]
    if rotationDirection == "R":
        return d[numRotations]

with open("input12") as f:
    for line in f:
        instruction = line.strip()
        dir = instruction[0]
        val = int(instruction[1:])
        match dir:
            case "N":
                wpy += val
            case "S":
                wpy -= val
            case "E":
                wpx += val
            case "W":
                wpx -= val
            case "L":
                wpx, wpy = rotate(wpx, wpy, dir, (val//90)%4)
            case "R":
                wpx, wpy = rotate(wpx, wpy, dir, (val//90)%4)
            case "F":
                x += val*wpx
                y += val*wpy
        print("ship:", x, y)
        print("waypoint:", wpx, wpy)
        print()

print(abs(x)+abs(y))



# x, y = 0, 0
# currDir = 0
# # east: 0, south: 1, west: 2, north: 3
# with open("input12") as f:
#     for line in f:
#         instruction = line.strip()
#         dir = instruction[0]
#         val = int(instruction[1:])
#         match dir:
#             case "N":
#                 y += val
#             case "S":
#                 y -= val
#             case "E":
#                 x += val
#             case "W":
#                 x -= val
#             case "L":
#                 currDir = (currDir - val//90) % 4
#             case "R":
#                 currDir = (currDir + val//90) % 4
#             case "F":
#                 match currDir:
#                     case 0:
#                         x += val
#                     case 1:
#                         y -= val
#                     case 2:
#                         x -= val
#                     case 3:
#                         y += val
#
# print(abs(x)+abs(y))
