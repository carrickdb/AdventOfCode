with open("input.txt") as f:
    polymer = f.readline()

class Node:

    def __init__(self, character):
        self.next = None
        self.character = character
        self.prev = None


# polymer = "hHUQeEpPiIq"
# polymer = ""
# polymer = "a"

"""
make a note about ascii difference between upper case and lower case
use a list of characters

create node class
turn the string into a linked list
do the thing
convert linked list back into a string

"""

min_len = float("inf")
diff = ord("a") - ord("A")

print(polymer[:10])
for k in range(26):
    first = None
    curr_char = chr(k + ord('a'))
    print(curr_char)
    for j in range(len(polymer)):
        if polymer[j].lower() != curr_char:
            first = j
            break
    head = Node(polymer[first])
    curr = head
    prev = None
    for i in range(first+1, len(polymer)):
        if polymer[i].lower() != chr(k + ord('a')):
            new_node = Node(polymer[i])
            curr.next = new_node
            new_node.prev = curr
            curr = new_node

    curr = head
    while curr and curr.next:
        if abs(ord(curr.character) - ord(curr.next.character)) == diff:
            if not curr.prev:
                # we're at the beginning of the list
                head = curr.next.next
                curr = head
                curr.prev = None
                continue
            elif not curr.next.next:
                # we're at the end of the list
                curr.prev.next = None
                break
            else:
                curr.prev.next = curr.next.next
                curr.next.next.prev = curr.prev
                curr = curr.prev
                continue
        curr = curr.next


    # turn LL back into regular list
    final = []
    curr = head
    while curr:
        final.append(curr.character)
        curr = curr.next

    new_length = len(final)
    print(new_length)
    if min_len > new_length:
        min_len = new_length

print(min_len)

"""
just go through the thing
cancel out all the things
make a new string each time
check new neighboring letters from the split

"""

