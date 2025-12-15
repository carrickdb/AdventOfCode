"""
total = 0

push first pointers on the stack:

    pop pointers from stack

    get number of children of current thing being pointed to
    get number of metadata entries
    get metadata entries

    total += metadata entries

    push the children's pointers onto the stack

return metadata sums from the children

"""


with open("input.txt") as f:
    line = f.readline()

packet = list(map(int, line.strip().split()))

def fun(packet):

    num_curr_children = packet[0]
    num_entries = packet[1]

    """
    2 3 1 3 0 1 5 10 11 12 1 1 0 1 99 2 1 1 2
    """
    # first node has no children
    if num_curr_children == 0:
        subtotal = 0
        for i in range(num_entries):
            subtotal += packet[2 + i]
        return subtotal, packet[num_entries + 2:]

    # the first node has children
    subtotal, slice = fun(packet[2:])
    total = subtotal
    for i in range(num_curr_children - 1):
        subtotal, slice = fun(slice)
        total += subtotal

    for i in range(num_entries):
        total += slice[i]

    return total, slice[num_entries:]

print(fun(packet))


"""

num_children
num_metadata

rest of string -> magical box -> index of where my children end, sum of my children's metadata

-> recurse on the string after the children



"""



