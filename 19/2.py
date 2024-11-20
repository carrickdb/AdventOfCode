

with open("input") as f:
    for line in f:
        program = line.strip().split(',')
        program = list(map(int, program))

