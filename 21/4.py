class Board:
    def __init__(self):
        self.numbers = set()
        self.rows = []
        self.cols = []

    def setCounters(self, numRows, numCols):
        self.rows = [0 for i in range(numRows)]
        self.cols = [0 for i in range(numCols)]


numberToBoards = {}  # number -> [(Board 1, number's row, number's col), (Board2, ...)]
boards = set()
with open("input4", 'r') as f:
    randomNumbers = list(map(int, f.readline().strip().split(',')))
    f.readline()
    rawBoards = f.read()
    rawBoards = rawBoards.split("\n\n")
    for rawBoard in rawBoards:
        numCols, numRows = 0, 0
        newBoard = Board()
        newRows = rawBoard.strip().split('\n')
        for newRow in newRows:
            numRows += 1
            currRow = newRow.split()
            if not numCols:
                numCols = len(currRow)
            currCol = 0
            for num in currRow:
                num = int(num)
                newBoard.numbers.add(num)
                if num in numberToBoards:
                    numberToBoards[num].append((newBoard, numRows-1, currCol))
                else:
                    numberToBoards[num] = [(newBoard, numRows-1, currCol)]
                currCol += 1
        newBoard.setCounters(numRows, numCols)
        boards.add(newBoard)

for number in randomNumbers:
    for board, row, col in numberToBoards[number]:
        if board not in boards:
            continue
        board.numbers.discard(number)
        board.rows[row] += 1
        board.cols[col] += 1
        if board.rows[row] >= 5 or board.cols[col] >= 5:
            if len(boards) == 1:
                print(number, sum(board.numbers) * number)
            boards.discard(board)


# class Board:
#     def __init__(self):
#         self.numbers = set()
#         self.rows = []
#         self.cols = []
#
#     def setCounters(self, numRows, numCols):
#         self.rows = [0 for i in range(numRows)]
#         self.cols = [0 for i in range(numCols)]


numberToBoards = {}  # number -> [(Board 1, number's row, number's col), Board2, ...]
with open("input4", 'r') as f:
    randomNumbers = list(map(int, f.readline().strip().split(',')))
    f.readline()
    rawBoards = f.read()
    rawBoards = rawBoards.split("\n\n")
    for rawBoard in rawBoards:
        numCols, numRows = 0, 0
        newBoard = Board()
        newRows = rawBoard.strip().split('\n')
        for newRow in newRows:
            numRows += 1
            currRow = newRow.split()
            if not numCols:
                numCols = len(currRow)
            currCol = 0
            for num in currRow:
                num = int(num)
                newBoard.numbers.add(num)
                if num in numberToBoards:
                    numberToBoards[num].append((newBoard, numRows-1, currCol))
                else:
                    numberToBoards[num] = [(newBoard, numRows-1, currCol)]
                currCol += 1
        newBoard.setCounters(numRows, numCols)

# 22,8
#
# 22 13
#  8  2
#
#  3 15
#  9 18

solutionFound = False
for number in randomNumbers:
    for board, row, col in numberToBoards[number]:
        board.numbers.discard(number)
        board.rows[row] += 1
        board.cols[col] += 1
        if board.rows[row] >= len(board.cols) or board.cols[col] >= len(board.rows):
            print(number, sum(board.numbers) * number)
            solutionFound = True
            break
    if solutionFound:
        break


"""
instantiate all the Boards:
    - set of numbers
    - arrays of counters for each row and col
hashmap of each number
    number -> [(Board 1, number's row, number's col), Board2, ...]
for each number, increment counter for row and col
if the counter reaches 5, multiply all the remaining elements in Board
"""
