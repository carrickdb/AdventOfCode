
def print_seats(seats):
    for row in seats:
        print(row)
    print()

seats = []
with open("input11") as f:
    for line in f:
        seats.append(line.strip())

def inBounds(seats, i, j):
    return not (i < 0 or j < 0 or j >= len(seats[0]) or i >= len(seats))

def getAdjOccupied(seats, i, j):
    occupied = 0
    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    for dy, dx in deltas:
        newi = i
        newj = j
        while inBounds(seats, newi+dy, newj+dx) and seats[newi+dy][newj+dx] != 'L':
            newi += dy
            newj += dx
            if seats[newi][newj] == "#":
                occupied += 1
                break
    return occupied

changes = True
times = 0
while changes:
    changes = False
    newSeats = []
    for i in range(len(seats)):
        newRow = []
        for j in range(len(seats[i])):
            curr = seats[i][j]
            if curr == '.':
                newRow.append(curr)
                continue
            numOccupied = getAdjOccupied(seats, i, j)
            # print(numOccupied, end='')
            if curr == "L" and numOccupied == 0:
                newRow.append("#")
                changes = True
                continue
            if curr == "#" and numOccupied >= 5:
                newRow.append("L")
                changes = True
                continue
            newRow.append(curr)
        newSeats.append(''.join(newRow))
        # print()
    seats = newSeats

numOccupied = 0
for row in seats:
    numOccupied += row.count("#")

print(numOccupied)



# def print_seats(seats):
#     for row in seats:
#         print(row)
#     print()
#
# seats = []
# with open("input11") as f:
#     for line in f:
#         seats.append(line.strip())
#
# def inBounds(seats, i, j):
#     return not (i < 0 or j < 0 or j >= len(seats[0]) or i >= len(seats))
#
# def getAdjOccupied(seats, i, j):
#     deltas = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
#     return sum([seats[i+dy][j+dx] == "#" if inBounds(seats, i+dy, j+dx) else 0 for dy,dx in deltas])
#
# changes = True
# while changes:
#     changes = False
#     newSeats = []
#     for i in range(len(seats)):
#         newRow = []
#         for j in range(len(seats[i])):
#             curr = seats[i][j]
#             if curr == '.':
#                 newRow.append(curr)
#                 continue
#             numOccupied = getAdjOccupied(seats, i, j)
#             if curr == "L" and numOccupied == 0:
#                 newRow.append("#")
#                 changes = True
#                 continue
#             if curr == "#" and numOccupied >= 4:
#                 newRow.append("L")
#                 changes = True
#                 continue
#             newRow.append(curr)
#         newSeats.append(''.join(newRow))
#     seats = newSeats
#     # print_seats(seats)
#
# numOccupied = 0
# for row in seats:
#     numOccupied += row.count("#")
#
# print(numOccupied)
