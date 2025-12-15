import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

input = aoc.getInput(os.getenv("HOME") + "/Desktop/input")
# input = aoc.getInput("test-input")
# input = aoc.getInput("part2-test-input")

"""
2,4 copies A%8 to B
1,5 XORs B with 5 (may or may not flip first and third bits)
7,5 Sets C to A//2^B
4,5 Sets B to B XOR C
0,3 Sets A to A//8
1,6 XORs B with 6 (may or may not flip second and third bits)
5,5 output B%8 (last 3 bits)
3,0 repeat
"""

def runProgram(i):
    A,B = i,0
    output = []
    while A > 0:
        B = A%8
        B ^= 5
        B ^= A>>B
        B ^= 6
        A >>= 3
        output.append(B%8)
    return output

origProgram = aoc.mapint(input[4].split(": ")[1].split(","))
print(runProgram(109019930331546)==origProgram)



"""
B = (((A & 111) ^ 101) ^ (A >> (A & 111) ^ 101)) ^ 110
A = A >> 3
output B & 111
repeat

for each octal in A:
(oct ^ (A >> (oct ^ 101))) ^ 110 # XORs octal with 3 digits in A, up to 7 shifts away, then XORs with 6

16 output numbers
at least 3*15+1=46 bits

only B is ever output
the jump is only ever back to the beginning
the only way it terminates is running off the end of the program after A becomes 0
"""

# Part 1
def getCombo(num):
    if num < 0 or num >= 7:
        print("Something went wrong")
        exit()
    if num <=3:
        return num
    return reg[num-4]
i = 2203
while True:
    reg[0] = i
    ip = 0
    output = []
    while True:
        spacing = " "*ip*2
        # for r in reg:
        #     print(format(r, 'b'), end=" ")
        # print()
        # print(' '.join(origProgram.split(",")))
        # print(f"{spacing}^")
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
            currOutput = getCombo(operand) % 8
            output.append(currOutput)
            # print("output:", format(currOutput, 'b'))
        elif op == 6:
            val = getCombo(operand)
            reg[1] = reg[0]//pow(2,val)
        elif op == 7:
            val = getCombo(operand)
            reg[2] = reg[0]//pow(2,val)

        if not jump:
            ip += 2

    currOutput = ','.join(aoc.mapstr(output))
    # print(f"input: {i}, output: {currOutput}")
    goal = "2,4,1,5,7"
    if currOutput[:len(goal)] == goal:
        print(i, oct(i), currOutput)
        break
    i += 1



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