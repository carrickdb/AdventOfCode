import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

input = aoc.getInput("input")
# input = aoc.getInput("test-input")

t = 0
for line in input:
    l = line.split(" ")
    goalCounters = [int(i) for i in l[-1][1:-1].split(',')]
    maxCounter = max(goalCounters)
    numCounters = len(goalCounters)
    buttons = l[1:-1]
    numButtons = len(buttons)
    mdbp = [0 for _ in range(numButtons+1)]
    print(numButtons, maxCounter, numCounters)
    for i in range(numCounters):
        print(i)
        mdbp = [mdbp for _ in range(maxCounter+1)]
        print(mdbp)
        break
    break





# t = 0
# for line in input:
#     l = line.split(" ")
#     specifiedJoltage = [int(i) for i in l[-1][1:-1].split(',')]
#     # print(diagram)
#     numCounters = len(specifiedJoltage)
#     counters = {tuple([False for _ in range(numCounters)]): 0}
#     minPresses = float("inf")
#     for button in l[1:-1]:
#         print(button, len(counters))
#         indices = list(map(int, button[1:-1].split(',')))
#         prevStates = [(k,v) for k,v in counters.items()]
#         for state, presses in prevStates:
#             newState = list(state)
#             while True:
#                 presses += 1
#                 for index in indices:
#                     newState[index] += 1
#                 if newState == specifiedJoltage:
#                     minPresses = min(minPresses, presses)
#                 if not all(newState[i] <= specifiedJoltage[i] for i in range(numCounters)):
#                     break
#                 # print(newState, presses+1)
#                 newStateTup = tuple(newState)
#                 if newStateTup in counters:
#                     counters[newStateTup] = min(counters[newStateTup], presses)
#                 else:
#                     counters[newStateTup] = presses
#         # print()
#     # print(minPresses)
#     t += minPresses

# print(t)

# t = 0
# for line in input:
#     l = line.split(" ")
#     diagram = [False if x=="." else True for x in l[0][1:-1]]
#     # print(diagram)
#     numLights = len(diagram)
#     lights = {tuple([False for _ in range(numLights)]): 0}
#     minPresses = float("inf")
#     for button in l[1:-1]:
#         # print(button)
#         toggles = list(map(int, button[1:-1].split(',')))
#         prevStates = [(k,v) for k,v in lights.items()]
#         for state, presses in prevStates:
#             newState = list(state)
#             for toggle in toggles:
#                 newState[toggle] = not newState[toggle]
#             if newState == diagram:
#                 minPresses = min(minPresses, presses+1)
#             # print(newState, presses+1)
#             newStateTup = tuple(newState)
#             if newStateTup in lights:
#                 lights[newStateTup] = min(lights[newStateTup], presses+1)
#             else:
#                 lights[newStateTup] = presses+1
#         # print()
#     # print(minPresses)
#     t += minPresses

# print(t)




