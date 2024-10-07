
with open("input") as f:
    for line in f:
        program = line.strip().split(',')
        program = list(map(int, program))

initial_program = program.copy()

for i in range(99):
    for j in range(99):
        program = initial_program.copy()
        program[1] = i
        program[2] = j

        PC = 0
        while PC < len(program):
            if program[PC] == 1:
                ptr1 = program[PC+1]
                ptr2 = program[PC+2]
                result_ptr = program[PC+3]
                program[result_ptr] = program[ptr1] + program[ptr2]
                PC += 4
            elif program[PC] == 2:
                ptr1 = program[PC+1]
                ptr2 = program[PC+2]
                result_ptr = program[PC+3]
                program[result_ptr] = program[ptr1] * program[ptr2]
                PC += 4
            elif program[PC] == 99:
                if program[0] == 19690720:
                    print(i, j)
                    exit()
                PC = float("inf")
                break
            else:
                print("ERROR: Invalid opcode")
                exit()
