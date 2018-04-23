#E328

def check():
    size = int(input(">"))
    data = list(map(int, input(">").split()))
    square = [data[i:i+size] for i in range(0, len(data), size)]
    if len(square) != len(square[0]):
        print("false")

    testCase = sorted(square[0])

    #Check each row
    for row in range(1, size):
        if sorted(square[row]) != testCase:
            print("false")
            return

    #Transpose so the columns are now rows
    for i in range(0, size):
        for j in range(i, size):
            square[i][j], square[j][i] = square[j][i], square[i][j]

    #Check each row (ex-columns)
    for row in range(1, size):
        if sorted(square[row]) != testCase:
            print("false")
            return

    print("true")
    return reduce(square)

def reduce(square):
    testCase = sorted(square[0])

    newSquare = []
    
    for i in range(len(testCase)):
        newSquare.append(testCase[i:] + testCase[:i])

    return newSquare
