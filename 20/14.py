instructions = []
maxAddr = float("-inf")
maxX = -1
with open("input14") as f:
    for line in f:
        if line[:3] == 'mem':
            ins = line.strip().split("] = ")
            addr = int(ins[0][4:])
            instructions.append((addr, int(ins[1])))
            maxAddr = max(maxAddr, addr)
        else:
            bitmask = line.strip()[7:]
            instructions.append(bitmask)
            maxX = max(maxX, len(bitmask) - bitmask.index('X') - 1)

def makeBitmasks(bitmask):
    ones = 0 # or
    floats = []
    for i in range(len(bitmask)):
        if bitmask[i] == "1":
            # print(len(bitmask) - i - 1)
            ones |= 1 << (len(bitmask) - i - 1)
    numX = bitmask.count("X")
    print(2**numX)
    for i in range(2**numX):
        newFloat = ones
        zeroes = 0
        bitidx = 0
        for j in range(len(bitmask)):
            if bitmask[j] == "X":
                currBit = (i >> (numX-bitidx-1)) & 1
                if currBit == 0:
                    zeroes |= 1 << (len(bitmask) - j - 1)
                else:
                    newFloat |= 1 << (len(bitmask) - j - 1)
                bitidx += 1
        floats.append((newFloat, ~zeroes % 2**36))
    # print(bitmask)
    # print(bin(ones))
    return floats

maxAddr = max(maxAddr, 1 << maxX+1)
memory = {}
floats = []
for ins in instructions:
    if type(ins) == str:
        floats = makeBitmasks(ins)
    else:
        for ones, zeroes in floats:
            currAddr, val = ins
            currAddr |= ones
            currAddr &= zeroes
            memory[currAddr] = val

# print([bin(x) for x in memory])
print(sum([v for k,v in memory.items()]))




# instructions = []
# minAddr = float("inf")
# maxAddr = float("-inf")
# with open("input14") as f:
#     for line in f:
#         if line[:3] == 'mem':
#             ins = line.strip().split("] = ")
#             addr = int(ins[0][4:])
#             instructions.append((addr, int(ins[1])))
#             minAddr = min(minAddr, addr)
#             maxAddr = max(maxAddr, addr)
#         else:
#             instructions.append(line.strip()[7:])
#
# def makeBitmasks(bitmask):
#     ones = 0 # or
#     zeroes = 0 # and
#     for i in range(len(bitmask)):
#         if bitmask[i] == "0":
#             zeroes |= 1 << (len(bitmask) - i - 1)
#         elif bitmask[i] == "1":
#             # print(len(bitmask) - i - 1)
#             ones |= 1 << (len(bitmask) - i - 1)
#     # print(bitmask)
#     # print(bin(zeroes))
#     # print(bin(ones))
#     return (~zeroes) % 2**36, ones
#
# memory = [0 for i in range(maxAddr-minAddr+1)]
# zeroes = 0
# ones = 0
# for ins in instructions:
#     if type(ins) == str:
#         zeroes, ones = makeBitmasks(ins)
#     else:
#         addr, val = ins
#         val &= zeroes
#         val |= ones
#         memory[addr-minAddr] = val
#
# # print([bin(x) for x in memory])
# print(sum(memory))
