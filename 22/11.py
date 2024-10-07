class Monkey:

    def __init__(self, id):
        self.id = id
        self.items = None
        self.operation = None
        self.test = None
        self.otherMonkey1 = None
        self.otherMonkey2 = None

lineNum = 0
monkeys = []
numMonkeys = 0
with open("input") as f:
    currMonkey = None
    for line in f:
        if line == "\n":
            lineNum = 0
            continue
        line = line.strip()
        if lineNum == 0:
            currMonkey = Monkey(numMonkeys)
            monkeys.append(currMonkey)
            numMonkeys += 1
        elif lineNum == 1:
            currMonkey.items = list(map(int, line.split(': ')[-1].split(", ")))
        elif lineNum == 2:
            # Operation: new = old * 13
            line = line.split()
            if line[-1] == "old":
                currMonkey.operation = lambda x: x * x
            else:
                num = int(line[-1])
                if line[-2] == "*":
                    currMonkey.operation = lambda x,num=num: x * num
                elif line[-2] == "+":
                    currMonkey.operation = lambda x, num=num: x + num
        elif lineNum == 3:
            # Test: divisible by 19
            currMonkey.test = int(line.split()[-1])
        elif lineNum == 4:
            # If true: throw to monkey 2
            currMonkey.otherMonkey1 = int(line.split()[-1])
        elif lineNum == 5:
            currMonkey.otherMonkey2 = int(line.split()[-1])
        lineNum += 1

inspections = [0 for _ in range(len(monkeys))]
mod = 1
for m in monkeys:
    mod *= m.test
for _ in range(10000):
    for i in range(len(monkeys)):
        currMonkey = monkeys[i]
        inspections[i] += len(monkeys[i].items)
        for item in currMonkey.items:
            """
            Monkey inspects an item with a worry level of 79.
            Worry level is multiplied by 19 to 1501.
            Current worry level is not divisible by 23.
            Item with worry level 500 is thrown to monkey 3.
            """
            newWorry = currMonkey.operation(item) % mod
            if newWorry % currMonkey.test == 0:
                monkeys[currMonkey.otherMonkey1].items.append(newWorry)
            else:
                monkeys[currMonkey.otherMonkey2].items.append(newWorry)
        currMonkey.items = []

inspections = sorted(inspections)
print(inspections[-1] * inspections[-2])






# """
# Monkey 0:
#   Starting items: 75, 75, 98, 97, 79, 97, 64
#   Operation: new = old * 13
#   Test: divisible by 19
#     If true: throw to monkey 2
#     If false: throw to monkey 7
# """
#
# class Monkey:
#
#     def __init__(self, id):
#         self.id = id
#         self.items = None
#         self.operation = None
#         self.test = None
#         self.otherMonkey1 = None
#         self.otherMonkey2 = None
#
# lineNum = 0
# monkeys = []
# numMonkeys = 0
# with open("input") as f:
#     currMonkey = None
#     for line in f:
#         if line == "\n":
#             lineNum = 0
#             continue
#         line = line.strip()
#         if lineNum == 0:
#             currMonkey = Monkey(numMonkeys)
#             monkeys.append(currMonkey)
#             numMonkeys += 1
#         elif lineNum == 1:
#             currMonkey.items = list(map(int, line.split(': ')[-1].split(", ")))
#         elif lineNum == 2:
#             # Operation: new = old * 13
#             line = line.split()
#             if line[-1] == "old":
#                 currMonkey.operation = lambda x: x * x
#             else:
#                 num = int(line[-1])
#                 if line[-2] == "*":
#                     currMonkey.operation = lambda x,num=num: x * num
#                 elif line[-2] == "+":
#                     currMonkey.operation = lambda x, num=num: x + num
#         elif lineNum == 3:
#             # Test: divisible by 19
#             currMonkey.test = int(line.split()[-1])
#         elif lineNum == 4:
#             # If true: throw to monkey 2
#             currMonkey.otherMonkey1 = int(line.split()[-1])
#         elif lineNum == 5:
#             currMonkey.otherMonkey2 = int(line.split()[-1])
#         lineNum += 1
#
# inspections = [0 for _ in range(len(monkeys))]
# for _ in range(20):
#     for i in range(len(monkeys)):
#         currMonkey = monkeys[i]
#         inspections[i] += len(currMonkey.items)
#         for item in currMonkey.items:
#             """
#             Monkey inspects an item with a worry level of 79.
#             Worry level is multiplied by 19 to 1501.
#             Monkey gets bored with item. Worry level is divided by 3 to 500.
#             Current worry level is not divisible by 23.
#             Item with worry level 500 is thrown to monkey 3.
#             """
#             newWorry = currMonkey.operation(item) // 3
#             if newWorry % currMonkey.test == 0:
#                 monkeys[currMonkey.otherMonkey1].items.append(newWorry)
#             else:
#                 monkeys[currMonkey.otherMonkey2].items.append(newWorry)
#         currMonkey.items = []
#
# inspections = sorted(inspections)
# print(inspections[-1] * inspections[-2])
