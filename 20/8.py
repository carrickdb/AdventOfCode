instructions = []
with open("input8") as f:
    for line in f:
        operation, argument = line.strip().split()
        if argument[0] == '-':
            argument = -1*int(argument[1:])
        else:
            argument = int(argument[1:])
        instructions.append([operation, argument])

for i in range(len(instructions)):
    PC = 0
    acc = 0
    visited = [0 for i in range(len(instructions))]
    old = instructions[i][0]
    if old == "jmp":
        instructions[i][0] = "nop"
    elif old == "nop":
        instructions[i][0] = "jmp"
    while PC < len(instructions) and visited[PC] == 0:
        visited[PC] = 1
        match instructions[PC][0]:
            case "jmp":
                PC += instructions[PC][1]
                continue
            case "acc":
                acc += instructions[PC][1]
        PC += 1
    if PC == len(instructions):
        break
    instructions[i][0] = old

print(acc)


# instructions = []
# with open("input8") as f:
#     for line in f:
#         operation, argument = line.strip().split()
#         if argument[0] == '-':
#             argument = -1*int(argument[1:])
#         else:
#             argument = int(argument[1:])
#         instructions.append([operation, argument])
#
# print(instructions)
# PC = 0
# acc = 0
# visited = [0 for i in range(len(instructions))]
#
# while visited[PC] == 0:
#     visited[PC] = 1
#     match instructions[PC][0]:
#         case "jmp":
#             PC += instructions[PC][1]
#             continue
#         case "acc":
#             acc += instructions[PC][1]
#     PC += 1
#
# print(acc)
