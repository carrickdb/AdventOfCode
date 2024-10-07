# Part 2

with open("input16") as f:
    message = f.readline().strip()

binList = []
for char in message:
    num = bin(int(char, 16))[2:]
    zeroes = ["0" for i in range(4-len(num))]
    binList.append(''.join(zeroes) + num)

binStr = ''.join(binList)

def getResult(type, vals):
    if type == 0:
        return sum(vals)
    if type == 1:
        product = 1
        for val in vals:
            product *= val
        return product
    if type == 2:
        return min(vals)
    if type == 3:
        return max(vals)
    if type == 5:
        return int(vals[0] > vals[1])
    if type == 6:
        return int(vals[0] < vals[1])
    if type == 7:
        return int(vals[0] == vals[1])

def getVersionFromPacket(packet):
    # print("packet:", packet)
    curr = 0
    version = int(packet[curr:curr+3], 2)
    # print("version:", version)
    curr += 3
    T = int(packet[curr:curr+3], 2)
    curr += 3
    if T != 4:
        if packet[curr] == "0":
            curr += 1
            lenSubpackets = int(packet[curr:curr+15], 2)
            # print("lenSubpackets", lenSubpackets)
            curr += 15
            vals = []
            initial = curr
            while curr < initial + lenSubpackets:
                """
                VVVTTTILLLLLLLLLLLLLLL
                0000010000000000010110
                len:22

                VVVTTTAAAAA
                10110000110011100010010000
                """
                retVersion, retCurr, val = getVersionFromPacket(packet[curr:])
                version += retVersion
                curr += retCurr
                # print("version, curr, val", version, curr, val)
                vals.append(val)
            res = getResult(T, vals)
            return version, curr, res
        elif packet[curr] == "1":
            curr += 1
            numSubpackets = int(packet[curr:curr+11], 2)
            # print("numSubpackets:", numSubpackets)
            curr += 11
            vals = []
            for _ in range(numSubpackets):
                retVersion, retCurr, val = getVersionFromPacket(packet[curr:])
                version += retVersion
                curr += retCurr
                vals.append(val)
            res = getResult(T, vals)
            return version, curr, res
    else:
        literal = ""
        while packet[curr] != "0":
            literal += packet[curr+1:curr+5]
            curr += 5
        literal += packet[curr+1:curr+5]
        curr += 5
        return version, curr, int(literal, 2)

versionNumbers = 0
print(getVersionFromPacket(binStr))




# Part 1
# with open("input16") as f:
#     message = f.readline().strip()
#
# binList = []
# for char in message:
#     num = bin(int(char, 16))[2:]
#     zeroes = ["0" for i in range(4-len(num))]
#     binList.append(''.join(zeroes) + num)
#
# binStr = ''.join(binList)
#
# """
# VVVTTTINNNNNNNNNNN
# 011000100000000010
#
# VVVTTTILLLLLLLLLLLLLLL
# 00000000000000000101100001000101010110001011001000100000000010000100011000111000110100
# len of subpackets: 22
# """
#
# def getVersionFromPacket(packet):
#     print("packet:", packet)
#     curr = 0
#     if not packet or int(packet, 2) == 0:
#         return 0, len(packet)
#     version = int(packet[curr:curr+3], 2)
#     print("version:", version)
#     curr += 3
#     T = int(packet[curr:curr+3], 2)
#     curr += 3
#     if T != 4:
#         if packet[curr] == "0":
#             curr += 1
#             lenSubpackets = int(packet[curr:curr+15], 2)
#             print("lenSubpackets", lenSubpackets)
#             curr += 15
#             while curr < len(packet):
#                 retVersion, retCurr = getVersionFromPacket(packet[curr:])
#                 version += retVersion
#                 curr += retCurr
#             return version, curr
#         elif packet[curr] == "1":
#             curr += 1
#             numSubpackets = int(packet[curr:curr+11], 2)
#             print("numSubpackets:", numSubpackets)
#             curr += 11
#             for _ in range(numSubpackets):
#                 retVersion, retCurr = getVersionFromPacket(packet[curr:])
#                 version += retVersion
#                 curr += retCurr
#             return version, curr
#     else:
#         while packet[curr] != "0":
#             curr += 5
#         curr += 5
#         return version, curr
#
# versionNumbers = 0
# print(getVersionFromPacket(binStr))
