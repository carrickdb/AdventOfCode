import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import aoc

# input = aoc.getInput("input")
input = aoc.getInput("test-input")

# how often each number from the left list appears in the right list. Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.
from collections import Counter
list1=[]
list2=[]
for line in input:
    t1,t2 = line.split()
    list1.append(int(t1))
    list2.append(int(t2))

count = Counter(list2)
total = 0
for n in list1:
    total += n*count[n]
print(total)


# list1=[]
# list2=[]
# for line in input:
#     t1,t2 = line.split()
#     list1.append(int(t1))
#     list2.append(int(t2))

# list1.sort()
# list2.sort()
# total = 0
# for i in range(len(list1)):
#     total += abs(list1[i] - list2[i])

# print(total)