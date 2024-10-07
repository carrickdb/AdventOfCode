mapping = {"A" : "rock", "B" : "paper", "C": "scissors"}
selection = {"rock" : 1, "paper":2, "scissors" : 3}

# them : me
lose = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
win = {"rock": "paper", "scissors": "rock", "paper": "scissors"}

with open("input") as f:
    score = 0
    for line in f:
        o, m = line.strip().split()
        other = mapping[o]

        if m == "X":
            score += selection[lose[other]]
        elif m == "Y":
            score += selection[other]
            score += 3
        elif m == "Z":
            score += selection[win[other]]
            score += 6

print(score)




# mapping = {"A" : "rock", "B" : "paper", "C": "scissors", "X" : "rock", "Y" : "paper", "Z": "scissors"}
#
# selection = {"rock" : 1, "paper":2, "scissors" : 3}
#
# # me: them
# win = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
#
# with open("input") as f:
#     score = 0
#     for line in f:
#         o, m = line.strip().split()
#         me = mapping[m]
#         other = mapping[o]
#         score += selection[me]
#         if me == other:
#             score += 3
#         elif win[me] == other:
#             score += 6
#
# print(score)
