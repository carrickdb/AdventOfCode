horizontal = 0
depth = 0
aim = 0

with open("input2", 'r') as f:
    for line in f:
        direction, units = line.strip().split()
        units = int(units)
        if direction == "forward":
            horizontal += units
            depth += aim * units
        elif direction == "down":
            aim += units
        else:
            aim -= units

print(horizontal * depth)



horizontal = 0
depth = 0

with open("input2", 'r') as f:
    for line in f:
        direction, units = line.strip().split()
        if direction == "forward":
            horizontal += int(units)
        elif direction == "down":
            depth += int(units)
        else:
            depth -= int(units)

print(horizontal * depth)
