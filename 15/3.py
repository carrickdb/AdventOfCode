with open("input") as f:
    dirs = f.readline().strip()
    visited = set()
    x, y = 0, 0
    rx, ry = 0, 0
    santa = True
    for dir in dirs:
        visited.add((x, y))
        visited.add((rx, ry))
        if dir == "^":
            if santa:
                y += 1
            else:
                ry += 1
        if dir == ">":
            if santa:
                x += 1
            else:
                rx += 1
        if dir == "<":
            if santa:
                x -= 1
            else:
                rx -= 1
        if dir == "v":
            if santa:
                y -= 1
            else:
                ry -= 1
        santa = not santa
    visited.add((x, y))
    visited.add((rx, ry))
    print(len(visited))
