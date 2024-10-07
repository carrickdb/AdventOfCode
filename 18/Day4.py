from datetime import datetime

log = []
with open("input.txt") as f:
    for line in f:
        timestamp, description = line.strip().split(']')
        timestamp = datetime.strptime(timestamp[1:], '%Y-%m-%d %H:%M')
        log.append((timestamp, description))

log = sorted(log)

# for time, entry in log:
#     print(time.minute, entry)

guards = {}
guard_mins_asleep = {}
curr_guard = None
falls = None
for time, entry in log:
    entry = entry.split()
    if entry[0] == "Guard":
        curr_guard = entry[1][1:]
    elif entry[0] == "falls":
        falls = time.minute
    elif entry[0] == "wakes":
        if curr_guard not in guards:
            guards[curr_guard] = []
            guard_mins_asleep[curr_guard] = 0
        guards[curr_guard].append((falls, time.minute))
        guard_mins_asleep[curr_guard] += time.minute - falls
        falls = None

# for guard, mins in guard_mins_asleep.items():
#     print(guard, mins)


mins = [{} for i in range(60)]

for guard, intervals in guards.items():
    for interval in intervals:
        start, stop = interval
        for i in range(start, stop):
            if guard not in mins[i]:
                mins[i][guard] = 1
            else:
                mins[i][guard] += 1

max_count = float("-inf")
sleepiest_guard = None
sleepiest_min = None
for i in range(len(mins)):
    guard_counts = mins[i]
    for guard, count in guard_counts.items():
        if count > max_count:
            max_count = count
            sleepiest_guard = guard
            sleepiest_min = i


print(sleepiest_min*int(sleepiest_guard))






# # go through each night, get the guard ID with the max # of minutes asleep
# sleepiest_guard = None
# max_mins = float("-inf")
# for guard, mins_asleep in guard_mins_asleep.items():
#     if mins_asleep > max_mins:
#         max_mins = mins_asleep
#         sleepiest_guard = guard
#
# mins = [0 for i in range(60)]
# for asleep, awake in guards[sleepiest_guard]:
#     for i in range(asleep, awake):
#         mins[i] += 1
#
# max_min = 0
# for i in range(1, len(mins)):
#     if not max_min or mins[i] > mins[max_min]:
#         max_min = i
#
# print(max_min * int(sleepiest_guard))




# make an array and just tally all the minutes he spends asleep