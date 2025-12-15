
with open("input") as f:
    for l in f:
        steps = l.strip().split(",")

def HASH(s):
    total = 0
    for c in s:
        total += ord(c)
        total *= 17
        total %= 256
    return total

def printBoxes(b):
    for i, x in enumerate(b):
        if len(x) > 0:
            print(i, ":", end=' ')
            for l, f in x:
                print(f"[{l} {f}]", end="")
            print()

boxes = [[] for _ in range(256)]
for s in steps:
    if s[-1] == '-':
        label = s[:-1]
        box = HASH(label)
        todelete = -1
        for i, lens in enumerate(boxes[box]):
            if lens[0] == label:
                todelete = i
        if todelete > -1:
            del boxes[box][todelete]
    elif '=' in s:
        label, fl = s.split('=')
        focallength = int(fl)
        box = HASH(label)
        found = False
        for i, n in enumerate(boxes[box]):
            if n[0] == label:
                found = True
                boxes[box][i][1] = focallength
                break
        if not found:
            boxes[box].append([label, focallength])
    else:
        print("what is this: ", s)

total = 0
for i in range(len(boxes)):
    b = boxes[i]
    for j in range(len(b)):
        fl = (1+i)*(j+1)*b[j][1]
        total += fl

print(total)

with open("input") as f:
    for l in f:
        steps = l.strip().split(",")


sumtotal = 0
for s in steps:
    total = 0
    for c in s:
        total += ord(c)
        total *= 17
        total %= 256
    sumtotal += total

print(sumtotal)

