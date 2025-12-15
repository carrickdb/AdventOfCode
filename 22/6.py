with open("input") as f:
    for line in f:
        line = line.strip()
        for i in range(13, len(line)):
            elements = set(line[i-13:i+1])
            if len(elements) == 14:
                print(i+1)
                break
