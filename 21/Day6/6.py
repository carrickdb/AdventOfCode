timers = [0 for i in range(9)]
with open("input6") as f:
    states = f.read().strip().split(',')
    for state in states:
        timers[int(state)] += 1

for i in range(256):
    prevSixes = timers[6]
    timers[6] = timers[0] + timers[7]
    timers[7] = timers[8]
    timers[8] = timers[0]
    for i in range(5):
        timers[i] = timers[i+1]
    timers[5] = prevSixes

print(sum(timers))
