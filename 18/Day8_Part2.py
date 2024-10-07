
with open("input.txt") as f:
    line = f.readline()

packet = list(map(int, line.strip().split()))

def fun(packet):

    num_children = packet[0]
    num_entries = packet[1]

    # first node has no children
    if num_children == 0:
        subtotal = 0
        for i in range(num_entries):
            subtotal += packet[2 + i]
        return subtotal, packet[num_entries + 2:]

    # the first node has children
    child_value, slice = fun(packet[2:])
    values = [child_value]
    for i in range(num_children - 1):
        child_value, slice = fun(slice)
        values.append(child_value)

    total = 0
    for i in range(num_entries):
        index = slice[i]
        if index > 0 and index <= num_children:
            total += values[index-1]

    return total, slice[num_entries:]

print(fun(packet))


"""

num_children
num_metadata

rest of string -> magical box -> index of where my children end, sum of my children's metadata

-> recurse on the string after the children

"""



