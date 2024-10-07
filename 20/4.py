import string

def validID(id):
    if len(id) != 9:
        return False
    for char in id:
        if not char.isdigit():
            return False
    return True

def validYear(year, minYear, maxYear):
    if len(year) != 4:
        return False
    try:
        yearNum = int(year)
        if yearNum < minYear or yearNum > maxYear:
            return False
    except:
        return False
    return True

def validHeight(height):
    if len(height) < 4:
        return False
    try:
        num = int(height[:-2])
        # If cm, the number must be at least 150 and at most 193.
        # If in, the number must be at least 59 and at most 76.
        if height[-2:] == "in":
            if num < 59 or num > 76:
                return False
        if height[-2:] == "cm":
            if num < 150 or num > 193:
                return False
    except:
        return False
    return True

def validHair(hair):
    # a # followed by exactly six characters 0-9 or a-f.
    if len(hair) != 7:
        return False
    if hair[0] != "#":
        return False
    for char in hair[1:]:
        if not (char.isdigit() or char in {'a', 'b','c','d','e','f'}):
            return False
    return True

bitarray = 0
numValid = 0
with open("input4") as f:
    for line in f:
        if line == "\n":
            if bitarray == (1 << 7) - 1:
                numValid += 1
            bitarray = 0
            continue
        fields = line.strip().split()
        for fieldVal in fields:
            field, val = fieldVal.split(':')
            match field:
                case "byr":
                    if validYear(val, 1920, 2002):
                        bitarray |= 1
                    # else:
                    #     print("invalid birth year")
                case "iyr":
                    if validYear(val, 2010, 2020):
                        bitarray |= 1 << 1
                    # else:
                    #     print("invalid issue year")
                case "eyr":
                    if validYear(val, 2020, 2030):
                        bitarray |= 1 << 2
                    # else:
                    #     print("invalid expiration year")
                case "hgt":
                    if validHeight(val):
                        bitarray |= 1 << 3
                    # else:
                    #     print("invalid height")
                case "hcl":
                    if validHair(val):
                        bitarray |= 1 << 4
                    # else:
                    #     print("invalid hair color")
                case "ecl":
                    if val in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
                        bitarray |= 1 << 5
                    # else:
                    #     print("invalid eye color")
                case "pid":
                    if validID(val):
                        bitarray |= 1 << 6
                    # else:
                    #     print("invalid ID")

if bitarray == (1 << 7) - 1:
    numValid += 1

print(numValid)






#
# bitarray = 0
# numValid = 0
# with open("input4") as f:
#     for line in f:
#         if line == "\n":
#             if bitarray == (1 << 7) - 1:
#                 numValid += 1
#             bitarray = 0
#             continue
#         fields = line.strip().split()
#         for fieldVal in fields:
#             field = fieldVal.split(':')[0]
#             match field:
#                 case "byr":
#                     bitarray |= 1
#                 case "iyr":
#                     bitarray |= 1 << 1
#                 case "eyr":
#                     bitarray |= 1 << 2
#                 case "hgt":
#                     bitarray |= 1 << 3
#                 case "hcl":
#                     bitarray |= 1 << 4
#                 case "ecl":
#                     bitarray |= 1 << 5
#                 case "pid":
#                     bitarray |= 1 << 6
#
# if bitarray == (1 << 7) - 1:
#     numValid += 1
#
# print(numValid)
