import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# with open("test-input") as f:
with open("input") as f:
    input = f.read()

# Part 2
rules, updates = input.split("\n\n")

rules = set(rules.split("\n"))

g = {}
for rule in rules:
    u,v = rule.split("|")
    if v not in g:
        g[v] = []
    g[v].append(u)  # 21|37 -> 37->21

total = 0
for update in updates.split("\n"):
    update = update.split(",")  # 75,47,61,53,29
    ok = True
    for i in range(len(update)):
        pagei = update[i]
        for j in range(i+1, len(update)):
            pagej = update[j]
            if pagei in g and pagej in g[pagei]:
                ok = False
                break
        if not ok:
            break
    if not ok:
        updateset = set(update)
        incoming = {}
        forward = {}
        newupdate = []
        noIncoming = []
        for rule in rules:
            u,v = rule.split("|")
            if u not in updateset or v not in updateset:
                continue
            if u not in forward:
                forward[u] = []
            forward[u].append(v)
            if v not in incoming:
                incoming[v] = 0
            if u not in incoming:
                incoming[u] = 0
            incoming[v] += 1

        for v,c in incoming.items():
            if c == 0:
                noIncoming.append(v)
        while noIncoming:
            curr = noIncoming.pop()
            if curr in updateset:
                newupdate.append(curr)
            if curr not in forward:
                continue
            currChildren = forward[curr]
            del forward[curr]
            for child in currChildren:
                incoming[child] -= 1
                if incoming[child] == 0:
                    noIncoming.append(child)
                    del incoming[child]
        total += int(newupdate[len(newupdate)//2])
print(total)


# Part 1

rules, updates = input.split("\n\n")

rules = set(rules.split("\n"))

g = {}
for rule in rules:
    u,v = rule.split("|")
    if v not in g:
        g[v] = []
    g[v].append(u)  # 21|37 -> 37->21

# print(g)
# print("37" in g["21"])

total = 0
for update in updates.split("\n"):
    update = update.split(",")  # 75,47,61,53,29
    ok = True
    for i in range(len(update)):
        pagei = update[i]
        for j in range(i+1, len(update)):
            pagej = update[j]
            if pagei in g and pagej in g[pagei]:
                ok = False
                break
        if not ok:
            break
    if ok:
        total += int(update[len(update)//2])
print(total)
