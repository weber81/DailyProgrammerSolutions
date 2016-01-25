def readRow(row):
    description = map(len, filter(lambda x:x != "", row.split(" ")))
    description = list(description)
    if len(description) == 0:
        return (0,)
    return description


def generateDescription(picture):
    rowDescription = []
    columnDescription = []
    for i in range(len(picture)):
        rowDescription.append(readRow(picture[i]))
    transverse = ["".join([picture[i][j] for i in range(len(picture))]) for j in range(len(picture[0]))]
    for i in range(len(transverse)):
        columnDescription.append(readRow(transverse[i]))
    
    return rowDescription, columnDescription

print("Write each row of the image as a row of \"*\" and \" \"")

picture = []
row = input()
while row != "":
    picture.append(row)
    row = input()
rowSize = len(max(picture, key=len))
for i in range(len(row)):
    row[i] = row[i] + " "*(rowSize-len(row[i]))
rows, columns = generateDescription(picture)

maxSizeR = len(max(rows, key=len))
maxSizeC = len(max(columns, key=len))

digitsR = len(str(max(max(rows, key=lambda x: max(x)))))
digitsC = len(str(max(max(columns, key=lambda x: max(x)))))

for i in range(len(rows)):
    rows[i] = [" "]*(maxSizeR-len(rows[i])) + rows[i]
    
for i in range(len(columns)):
    columns[i] = [" "]*(maxSizeC-len(columns[i])) + columns[i]

headerSpaceR = digitsR*maxSizeR + maxSizeR - 1

header = []
for i in range(maxSizeC):
    headerString = " "*(headerSpaceR)
    for j in range(len(columns)):
        value = str(columns[j][i])
        headerString += " "*(digitsC - len(value)) + value +" "
    header.append(headerString)
for h in header:
    print(h)
    
for x in range(len(rows)):
    print((" "*digitsR)*(maxSizeR-len(rows[x])), end="")
    for r in rows[x]:
        print(" "*(digitsR-len(str(r)))+str(r) + " ", end="")
    print("")
