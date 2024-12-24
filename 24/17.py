import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

# input = aoc.getInput(os.getenv("HOME") + "/Desktop/input")
input = aoc.getInput("test-input")
# input = aoc.getInput("second-example")

reg = [int(x.split(": ")[1]) for x in input[:3]]
print(reg)

program = aoc.mapint(input[4].split(": ")[1].split(","))
print(program)
lp = len(program)
ip = 0
output = []

def getCombo(num):
    if num < 0 or num >= 7:
        print("Something went wrong")
        exit()
    if num <=3:
        return num
    return reg[num-4]

while True:
    jump = False
    if ip >= lp:
        break
    op, operand = program[ip], program[ip+1]
    if op == 0:
        val = getCombo(operand)
        reg[0] = reg[0]//pow(2,val)
    elif op == 1:
        reg[1] ^= operand
    elif op == 2:
        reg[1] = getCombo(operand) % 8
    elif op == 3:
        if reg[0] != 0:
            ip = operand
            jump = True
    elif op == 4:
        reg[1] ^= reg[2]
    elif op == 5:
        output.append(getCombo(operand) % 8)
    elif op == 6:
        val = getCombo(operand)
        reg[1] = reg[0]//pow(2,val)
    elif op == 7:
        val = getCombo(operand)
        reg[2] = reg[0]//pow(2,val)

    if not jump:
        ip += 2

print(','.join(aoc.mapstr(output)))

# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# import aoc

# # input = aoc.getInput(os.getenv("HOME") + "/Desktop/input")
# input = aoc.getInput("test-input")
# # input = aoc.getInput("second-example")

# reg = [int(x.split(": ")[1]) for x in input[:3]]
# print(reg)

# program = aoc.mapint(input[4].split(": ")[1].split(","))
# print(program)
# lp = len(program)
# ip = 0
# output = []

# def getCombo(num):
#     if num < 0 or num >= 7:
#         print("Something went wrong")
#         exit()
#     if num <=3:
#         return num
#     return reg[num-4]

# while True:
#     jump = False
#     if ip >= lp:
#         break
#     op, operand = program[ip], program[ip+1]
#     if op == 0:
#         val = getCombo(operand)
#         reg[0] = reg[0]//pow(2,val)
#     elif op == 1:
#         reg[1] ^= operand
#     elif op == 2:
#         reg[1] = getCombo(operand) % 8
#     elif op == 3:
#         if reg[0] != 0:
#             ip = operand
#             jump = True
#     elif op == 4:
#         reg[1] ^= reg[2]
#     elif op == 5:
#         output.append(getCombo(operand) % 8)
#     elif op == 6:
#         val = getCombo(operand)
#         reg[1] = reg[0]//pow(2,val)
#     elif op == 7:
#         val = getCombo(operand)
#         reg[2] = reg[0]//pow(2,val)

#     if not jump:
#         ip += 2

# print(','.join(aoc.mapstr(output)))