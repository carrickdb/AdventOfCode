# Part 2:

with open("input7") as f:
    crabPeople = sorted(map(int, (f.read().strip().split(","))))

lowest = crabPeople[0]
highest = crabPeople[-1]

minTotal = sum([((crab - lowest) * (crab-lowest)+1)//2 for crab in crabPeople])
# print(total)
for num in range(lowest+1, highest+1):
    minTotal = min(minTotal, sum([(abs(crab - num) * (abs(crab - num)+1))//2 for crab in crabPeople]))

print(minTotal)

# Part 1:
with open("input7") as f:
    crabPeople = sorted(map(int, (f.read().strip().split(","))))

lowest = crabPeople[0]
highest = crabPeople[-1]

minTotal = sum([crab - lowest for crab in crabPeople])
# print(total)
for num in range(lowest+1, highest+1):
    minTotal = min(minTotal, sum([abs(crab - num) for crab in crabPeople]))

print(minTotal)
