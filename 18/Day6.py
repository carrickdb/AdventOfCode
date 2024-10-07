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

# print("min_x", min_x)
# print("max_x", max_x)
# print("min_y", min_y)
# print("max_y", max_y)

rows = max_y - min_y + 1
cols = max_x - min_x + 1
# print(rows)
# print(cols)

grid = [[None for i in range(cols)] for j in range(rows)]

# k = 1
# for i in range(len(x)):
#     grid[y[i] - min_y][x[i] - min_x] = k
#     k += 1

for i in range(rows):
    for j in range(cols):
        min_dist = float("inf")
        min_coord = None
        dupe = False
        for k in range(len(x)):
            curr_dist = abs(x[k] - min_x - j) + abs(y[k] - min_y - i)
            # if j == 9:
            #     print(curr_dist)
            #     print(x[k] - min_x - i)
            #     print(y[k])
            #     print(min_y)
            if curr_dist < min_dist:
                min_coord = str(k + 1)
                # print("curr_coord", i, j)
                # print("new min coord", min_coord)
                min_dist = curr_dist
                dupe = False
                if min_dist == 0:
                    # min_coord = "-" + str(k+1) + "-"
                    break
            elif curr_dist == min_dist:
                dupe = True
        if dupe:
            grid[i][j] = "."
        else:
            grid[i][j] = min_coord

for i in range(len(grid)):
    print(grid[i])

areas = {}

visited = [[False for i in range(cols)] for j in range(rows)]

for i in range(rows):
    for j in range(cols):
        curr_coord = grid[i][j]
        if curr_coord != "." and not visited[i][j] \
            and not (curr_coord in areas and areas[curr_coord] == float("inf")):
            if i == 0 or j == 0 or i == rows - 1 or j == cols - 1:
                areas[curr_coord] = float("inf")
            else:
                num_visited = 0
                stack = [(i, j)]
                print("___curr_coord___", curr_coord)
                while stack:
                    curr_i, curr_j = stack.pop()
                    print("DFS curr:", curr_i, curr_j)
                    if not visited[curr_i][curr_j]:
                        visited[curr_i][curr_j] = True
                        num_visited += 1
                        if curr_i == 0 or curr_j == 0 or curr_i == rows - 1 or curr_j == cols - 1:
                            areas[curr_coord] = float("inf")
                            break
                        if curr_i+1 < rows and grid[curr_i+1][curr_j] == curr_coord and not visited[curr_i+1][curr_j]:
                            stack.append((curr_i+1, curr_j))
                        if curr_i > 0 and grid[curr_i-1][curr_j] == curr_coord and not visited[curr_i-1][curr_j]:
                            stack.append((curr_i-1, curr_j))
                        if curr_j + 1 < cols and grid[curr_i][curr_j+1] == curr_coord and not visited[curr_i][curr_j+1]:
                            stack.append((curr_i, curr_j+1))
                        if curr_j > 0 and grid[curr_i][curr_j-1] == curr_coord and not visited[curr_i][curr_j-1]:
                            stack.append((curr_i, curr_j-1))
                if curr_coord in areas:
                    areas[curr_coord] += num_visited
                else:
                    areas[curr_coord] = num_visited
                print()


print(areas)
max_area = float("-inf")
for coord, area in areas.items():
    if area > max_area and area != float("inf"):
        max_area = area

print(max_area)

# to DFS/BFS on grid at the end
