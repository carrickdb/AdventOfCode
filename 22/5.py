stacks = [['S', 'M', 'R', 'N', 'W', 'J', 'V', 'T'], ['B', 'W', 'D', 'J', 'Q', 'P', 'C', 'V'], ['B', 'J', 'F', 'H', 'D', 'R', 'P'], ['F', 'R', 'P', 'B', 'M', 'N', 'D'], ['H', 'V', 'R', 'P', 'T', 'B'], ['C', 'B', 'P', 'T'], ['B', 'J', 'R', 'P', 'L'], ['N', 'C', 'S', 'L', 'T', 'Z', 'B', 'W'], ['L', 'S', 'G']]


# stacks = [['Z', 'N'], ['M', 'C', 'D'], ['P']]
#     [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3

with open("input") as f:
    #  0   1 2    3  4 5
    # move 7 from 3 to 9
    for line in f:
        line = line.strip().split()
        source = int(line[3])-1
        destination = int(line[5])-1
        num = int(line[1])
        # print(line)
        for stack in stacks:
            print(stack)
        stacks[destination] += stacks[source][(-1*num):]
        stacks[source] = stacks[source][:-1*num]
        # print()


for stack in stacks:
    # print(stack)
    print(stack[-1], end='')
    # print()



"""
SMRNWJVT
BWDJQPCV
BJFHDRP
FRPBMND
HVRPTB
CBPT
BJRPL
NCSLTZBW
LSG


"""
