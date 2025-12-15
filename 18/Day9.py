NUM_PLAYERS = 458
LAST_MARBLE = 7130700


# NUM_PLAYERS = 9
# LAST_MARBLE = 25


class Marble:

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

scores = [0 for i in range(NUM_PLAYERS)]

root = Marble(0)
root.prev = root
root.next = root

curr = root

turn = 0
player = 0
for i in range(LAST_MARBLE+1):
    """
    if new marble % 23 != 0:
        insert as curr.next.next
        curr_marble becomes the marble that was placed

    else:
        remove 7th marble CCW of curr marble
        add its value plus value of marble to be played to curr player
        current marble becomes first marble CW of removed marble

    """
    if i % 23 != 0:
        new_marble = Marble(i)
        new_prev = curr.next
        new_next = curr.next.next
        new_marble.prev = new_prev
        new_prev.next = new_marble
        new_marble.next = new_next
        new_next.prev = new_marble
        curr = new_marble
    else:
        for j in range(6):
            curr = curr.prev
        removed = curr.prev
        # print(i)
        scores[player] += i + removed.val
        curr.prev = removed.prev
        removed.prev.next = curr

    turn += 1
    player = (player + 1) % NUM_PLAYERS



print(max(scores))