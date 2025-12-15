import aoc, functools

## Part 2

mapping = {
    "J":1,
    "T": 10,
    "Q":11,
    "K":12,
    "A":13,
}

def getHand(hand):
    count = {}
    js = 0
    for c in hand:
        if c == "J":
            js += 1
            continue
        if c not in count:
            count[c] = 0
        count[c] += 1
    if js:
        biggestCount = float("-inf")
        bname = None
        for k, v in count.items():
            if v > biggestCount:
                biggestCount = v
                bname = k
        count[bname] = biggestCount+js
    return count

def sortCards(a, b):
    x = a[0]
    y = b[0]
    c1 = getHand(x)
    c2 = getHand(y)
    if len(c1) < len(c2):
        return 1
    elif len(c1) > len(c2):
        return -1
    else:
        n1 = sorted(c1.values(), reverse=True)
        n2 = sorted(c2.values(), reverse=True)
        for i in range(min(len(n1), len(n2))):
            first = n1[i]
            second = n2[i]
            if first == second:
                continue
            if first < second:
                return -1
            return 1
    for i in range(len(x)):
        curr1 = x[i]
        if curr1.isdigit():
            curr1 = int(curr1)
        else:
            curr1 = mapping[curr1]
        curr2 = y[i]
        if curr2.isdigit():
            curr2 = int(curr2)
        else:
            curr2 = mapping[curr2]
        if curr1 == curr2:
            continue
        elif curr1 < curr2:
            return -1
        else:
            return 1


hands = []
with open("input") as f:
    for l in f:
        line = l.strip().split()
        hands.append((line[0], int(line[1])))
    hands = sorted(hands, key=functools.cmp_to_key(sortCards))
    print(hands)
    place = 1
    total = 0
    for _, b in hands:
        total += place*b
        place += 1

print(total)


## Part 1

mapping = {
    "T": 10,
    "J":11,
    "Q":12,
    "K":13,
    "A":14,
}

def sortCards(a, b):
    x = a[0]
    y = b[0]
    c1 = {}
    for c in x:
        if c not in c1:
            c1[c] = 0
        c1[c] += 1
    c2 = {}
    for c in y:
        if c not in c2:
            c2[c] = 0
        c2[c] += 1
    if len(c1) < len(c2):
        return 1
    elif len(c1) > len(c2):
        return -1
    else:
        n1 = sorted(c1.values(), reverse=True)
        n2 = sorted(c2.values(), reverse=True)
        for i in range(min(len(n1), len(n2))):
            first = n1[i]
            second = n2[i]
            if first == second:
                continue
            if first < second:
                return -1
            return 1
    for i in range(len(x)):
        curr1 = x[i]
        if curr1.isdigit():
            curr1 = int(curr1)
        else:
            curr1 = mapping[curr1]
        curr2 = y[i]
        if curr2.isdigit():
            curr2 = int(curr2)
        else:
            curr2 = mapping[curr2]
        if curr1 == curr2:
            continue
        elif curr1 < curr2:
            return -1
        else:
            return 1


hands = []
with open("input") as f:
    for l in f:
        line = l.strip().split()
        hands.append((line[0], int(line[1])))
    hands = sorted(hands, key=functools.cmp_to_key(sortCards))
    place = 1
    total = 0
    for _, b in hands:
        total += place*b
        place += 1

print(total)

