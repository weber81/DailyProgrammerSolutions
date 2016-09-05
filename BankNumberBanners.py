def to7Segment(numString):
    firstRow = []
    secondRow = []
    thirdRow = []
    for num in numString:
        firstRow += ([" _ ", "   ", " _ ", " _ ", "   "] + ([" _ "] * 5))[int(num)]
        secondRow +=(["| |", "  |", " _|", " _|", "|_|", "|_ ", "|_ ", "  |", "|_|", "|_|"])[int(num)]
        thirdRow += (["|_|", "  |", "|_ ", " _|", "  |", " _|", "|_|", "  |", "|_|", " _|"])[int(num)]
    print("".join(firstRow))
    print("".join(secondRow))
    print("".join(thirdRow))
    return [firstRow, secondRow, thirdRow]

def from7Segment(asciiString):
    splitRow = lambda n: ["".join(asciiString[n][i:i+3]) for i in range(0, len(asciiString[n]), 3)]
    firstRow = splitRow(0)
    secondRow = splitRow(1)
    thirdRow = splitRow(2)
    string = ""
    for i in range(len(firstRow)):
        if firstRow[i] == "   ": #First row is empty => 1, 4
            if secondRow[i] == "  |": 
                string += "1"
            else:
                string += "4"
                
        else:
            if secondRow[i] == "| |":
                string += "0"
                
            elif secondRow[i] == "  |":
                string += "7"
                
            elif secondRow[i] == " _|":
                if thirdRow[i] == "|_ ":
                    string += "2"
                else:
                    string += "3"
                    
            elif secondRow[i] == "|_ ":
                if thirdRow[i] == " _|":
                    string += "5"
                else:
                    string += "6"

            elif secondRow[i] == "|_|":
                if thirdRow[i] == "|_|":
                    string += "8"
                elif thirdRow[i] == " _|":
                    string += "9"
    print(string)
        

def mainPt1():
    row1 = to7Segment(input())
    row2 = to7Segment(input())
    row3 = to7Segment(input())
    return [row1, row2, row3]

def mainPt2(row1, row2, row3):
    from7Segment(row1)
    from7Segment(row2)
    from7Segment(row3)
