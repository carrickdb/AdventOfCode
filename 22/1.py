with open("input") as f:
    elf = 0
    maxElves = [float("-inf") for _ in range(3)]
    for line in f:
        if line == "\n":
            if maxElves[0] < elf:
                maxElves[2] = maxElves[1]
                maxElves[1] = maxElves[0]
                maxElves[0] = elf
            elif maxElves[1] < elf:
                maxElves[2] = maxElves[1]
                maxElves[1] = elf
            elif maxElves[2] < elf:
                maxElves[2] = elf
            elf = 0
        else:
            elf += int(line.strip())
    if maxElves[0] < elf:
        maxElves[2] = maxElves[1]
        maxElves[1] = maxElves[0]
        maxElves[0] = elf
    elif maxElves[1] < elf:
        maxElves[2] = maxElves[1]
        maxElves[1] = elf
    elif maxElves[2] < elf:
        maxElves[2] = elf

print(sum(maxElves))
