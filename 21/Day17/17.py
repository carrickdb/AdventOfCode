# Part 2

# answer = set()
# with open("answer") as f:
#     for line in f:
#         coordinates = line.strip().split()
#         for coord in coordinates:
#             x, y = list(map(int, coord.split(",")))
#             answer.add((x, y))

with open("input17") as f:
    input = f.readline().strip().split(": x=")[1]
    x, y = input.split(", y=")
    minX, maxX = list(map(int, x.split("..")))
    minY, maxY = list(map(int, y.split("..")))

initialVelocities = 0
for x in range(maxX+1):
    for y in range(minY, abs(minY)+1):
        currY = 0
        currX = 0
        xVelocity = x
        yVelocity = y
        while currY >= minY and currX <= maxX:
            # if y == 6:
            #     print(currX, currY)
            if currY <= maxY and currX >= minX:
                # if (x, y) not in answer:
                #     print("We have a problem", x, y)
                #     assert False
                initialVelocities += 1
                # answer.remove((x, y))
                break
            currX += xVelocity
            if xVelocity > 0:
                xVelocity -= 1
            currY += yVelocity
            yVelocity -= 1
        # if y == 6:
        #     assert False

# print(answer)
print(initialVelocities)





# Part 1:
# target area: x=20..30, y=-10..-5
#
# with open("input17") as f:
#     input = f.readline().strip().split(": x=")[1]
#     x, y = input.split(", y=")
#     minX, maxX = list(map(int, x.split("..")))
#     minY, maxY = list(map(int, y.split("..")))
#
# initialY = abs(minY)-1
# print((initialY*(initialY+1))//2)
