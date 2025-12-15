
from functools import cache


# input = "0 1 10 99 999"
# blinks = 25
# input = "125 17"

@cache
def rec(num, blinks):
    if blinks == 0:
        return 1
    b = blinks-1
    strs = str(num)
    if num==0:
        return rec(1,blinks-1)
    elif len(str(num))%2 == 0:
        return rec(int(strs[:len(strs)//2]), b) + rec(int(strs[len(strs)//2:]), b)
    else:
        return rec(2024*num, blinks-1)

stones = list(map(int, input.split()))
total = 0
for s in stones:
    total += rec(s,75)
print(total)

numStones = 0

for origStone in stones:
    currStones = [origStone]
    for b in range(75):
        print(b)
        lenCurrStones = len(currStones)
        for si in range(lenCurrStones):
            s = currStones[si]
            strs = str(s)
            if s==0:
                currStones[si] = 1
            elif len(strs)%2==0:
                currStones[si] = int(strs[:len(strs)//2])
                currStones.append(int(strs[len(strs)//2:]))
            else:
                currStones[si] *= 2024
    numStones += len(currStones)

print(numStones)




numStones = 0
stones = list(map(int, input.split()))
# print(stones)
for origStone in stones:
    currStones = [origStone]
    for b in range(75):
        print(b)
        lenCurrStones = len(currStones)
        for si in range(lenCurrStones):
            s = currStones[si]
            strs = str(s)
            if s==0:
                currStones[si] = 1
            elif len(strs)%2==0:
                currStones[si] = int(strs[:len(strs)//2])
                currStones.append(int(strs[len(strs)//2:]))
            else:
                currStones[si] *= 2024
        # print(currStones)
    numStones += len(currStones)

print(numStones)


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

input = list(map(int, input.split())) # TODO
head = Node(input[0])
print(input)
curr = head
for num in input[1:]:
    curr.next = Node(num)
    curr = curr.next

def printList(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()

for b in range(25):
    # printList(head)
    curr = head
    while curr:
        """
    If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
    If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
        """
        if curr.val == 0:
            curr.val = 1
        elif len(str(curr.val))%2==0:
            strcurr = str(curr.val)
            curr.val = int(strcurr[:len(strcurr)//2])
            next = curr.next
            curr.next = Node(int(strcurr[len(strcurr)//2:]))
            curr = curr.next
            curr.next = next
        else:
            curr.val *= 2024
        curr = curr.next

# printList(head)
numStones = 0
curr = head
while curr:
    numStones += 1
    curr = curr.next
print(numStones)