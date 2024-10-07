numValid = 0
with open("input2") as f:
    for line in f:
        # 2-9 c: ccccccccc
        policy, password = line.strip().split(": ")
        positions, letter = policy.split()
        p1, p2 = list(map(int, positions.split("-")))
        p1 -= 1
        p2 -= 1
        # print(((password[p1] == letter) ^ (password[p2] == letter)))
        if len(password) > p2 and ((password[p1] == letter) ^ (password[p2] == letter)):
            numValid += 1

print(numValid)




# # Part 1
#
# numValid = 0
# with open("input2") as f:
#     for line in f:
#         # 2-9 c: ccccccccc
#         policy, password = line.strip().split(": ")
#         limits, letter = policy.split()
#         lower, upper = list(map(int, limits.split("-")))
#         if password.count(letter) <= upper and password.count(letter) >= lower:
#             numValid += 1
#
# print(numValid)
