from time import sleep


x = []
y = []

with open("input.txt") as f:
    for line in f:
        x_curr, y_curr = line.strip().split(', ')
        x.append(int(x_curr))
        y.append(int(y_curr))

# x = [1, 1, 8, 3, 5, 8]
# y = [1, 6, 3, 4, 5, 9]

min_x = min(x)
max_x = max(x)
min_y = min(y)
max_y = max(y)

rows = max_y - min_y + 1
cols = max_x - min_x + 1
#
# grid = [[None for i in range(cols)] for j in range(rows)]

region_size = 0
# get all the distances
for i in range(rows):
    for j in range(cols):
        distance_sum = 0
        # print(i, j)
        for k in range(len(x)):
            curr_dist = abs(x[k] - min_x - j) + abs(y[k] - min_y - i)
            distance_sum += curr_dist
            # print(k, curr_dist)
            if distance_sum >= 10000:
                break
        if distance_sum < 10000:
            region_size += 1
        # print()

print(region_size)

# for i in range(len(grid)):
#     print(grid[i])
