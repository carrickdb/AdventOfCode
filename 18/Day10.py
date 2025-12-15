x = []
y = []
v = []

with open("input.txt") as f:
    for line in f:
        position, velocity = line.strip().split("> velocity=<")
        position = position.split("position=<")
        new_x, new_y = list(map(int, position[1].split(", ")))
        x_d, y_d = list(map(int, velocity[:-1].split(", ")))
        x.append(new_x)
        y.append(new_y)
        v.append((x_d, y_d))

t = 10656

for i in range(len(x)):
    x[i] += t*v[i][0]
    y[i] += t*v[i][1]


# print(max(x) - min(x))
# print(max(y) - min(y))

# coords = zip(x, y)
# coords = sorted(coords, key=lambda x: (x[1], x[0]))


sky = [['.' for i in range(max(x) - min(x) + 1)] for j in range(max(y) - min(y) + 1)]

for i in range(len(x)):
    curr_x = x[i] - min(x)
    curr_y = y[i] - min(y)
    try:
        sky[curr_y][curr_x] = "#"
    except:
        print(curr_x, curr_y)


for row in sky:
    line = ''.join(row)
    print(line)