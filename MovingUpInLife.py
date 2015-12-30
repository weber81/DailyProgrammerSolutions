import sys, math

def countXs(board):
    count = 0
    for row in board:
        count += row.count("X")
    return count

def findX(board, rowSlice=None, columnSlice=None):
    if rowSlice == None:
        rowSlice = slice(0, len(board))
    if columnSlice == None:
        columnSlice = slice(0, len(board[0]))
    board = sliceArray(board, rowSlice, columnSlice)
    for row in board:
        if "X" in row:
            return board.index(row) + rowSlice.start, row.index("X") + columnSlice.start
    return -1, -1

"""Provide a slice object for rowSlice and columnSlice"""
def sliceArray(array, rowSlice=None, columnSlice=None):
    if rowSlice == None:
        rowSlice = slice(len(array))

    if type(array[0]) != list:
        return array[rowSlice]

    if columnSlice == None:
        columnSlice = slice(len(array[0]))
    return [row[columnSlice] for row in array[rowSlice]]

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def combinations(dx, dy):
    t = min(dx, dy)
    if dx == 0 or dy == 0:
        return 1
    
    return int(sum(list(map(lambda s: math.factorial(dx+dy - s)/(math.factorial(dx-s)*
                                       math.factorial(dy-s)*
                                       math.factorial(s)), range(0, t+1)))))
    
width, height = input().split(", ")
board = [list(input()) for i in range(int(height))]

board.reverse() #flip the board to work from the top down.

#find the first x from the top-left
nextX, nextY = findX(board)
Xs = [(nextX, nextY)]

nextX1, nextY1 = findX(board,
                     slice(nextX, len(board)),
                     slice(nextY+1, len(board[0]))
                     )
nextX2, nextY2 = findX(board,
                     slice(nextX+1, len(board)),
                     slice(nextY, len(board[0]))
                     )

nextX, nextY = min([(nextX1, nextY1), (nextX2, nextY2)], key=lambda x: x[0]+x[1]) 


while (nextX, nextY) != (-1, -1):
    Xs.append((nextX, nextY))
    nextX1, nextY1 = findX(board,
                         slice(nextX, len(board)),
                         slice(nextY+1, len(board[0]))
                         )
    nextX2, nextY2 = findX(board,
                         slice(nextX+1, len(board)),
                         slice(nextY, len(board[0]))
                         )
    nextX, nextY = min([(nextX1, nextY1), (nextX2, nextY2)], key=lambda x: x[0]+x[1]) 

if len(Xs) != countXs(board):
    print("IMPOSSIBLE")
    sys.exit()

pathsPerX = []
for i in range(len(Xs)-1):
    x1,y1 = Xs[i]
    x2,y2 = Xs[i+1]

    dx = x2-x1
    dy = y2-y1

    pathsPerX.append(combinations(dx, dy))

product = 1
for p in pathsPerX:
    product *= p

print(str(product) + " Paths")
