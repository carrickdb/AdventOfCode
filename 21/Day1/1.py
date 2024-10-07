larger_measurement = 0

with open("input1", 'r') as f:
    window = []
    oldest = 0
    for line in f:
        if len(window) < 3:
            window.append(int(line))
        else:
            larger_measurement += window[oldest] < int(line)
            window[oldest] = int(line)
            oldest += 1
            oldest %= 3

print(larger_measurement)

"""
1 2 3 4 1 4 0
window = [4, 1, 4]
oldest = 0
line = 0

"""

larger_measurement = 0
with open("input1", 'r') as f:
    curr = None
    for line in f:
        if curr:
            larger_measurement += int(line) > curr
        curr = int(line)
print(larger_measurement)
