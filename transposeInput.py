def transpose():
    #Get Input
    line = input()
    lineArray = []
    while line != "":
        lineArray.append(line)
        line = input()

    #Find the longest length
    maxLength = max(map(len, lineArray))

    #Print each column
    for i in range(maxLength):
        for line in lineArray:
            if i < len(line):
                print(line[i], end="")
        print("")

def transposeV2():
    #Get Input
    line = input()
    lineArray = []
    while line != "":
        lineArray.append(line)
        line = input()

    #Actual Logic
    print(*map(lambda x: "".join(x).rstrip(),zip(*map(lambda x: list(x.ljust(len(max(lineArray, key=len)), " ")),lineArray))),sep="\n")

def singleLine():
    print(*map(lambda x: "".join(x).rstrip(),[zip(*map(lambda x: list(x.ljust(len(max(lineArray,key=len))," ")),lineArray))for lineArray in [(lambda f: lambda read: [] if read == "" else [read]+f(f)(input()))(lambda f: lambda read: [] if read == "" else [read]+f(f)(input()))(input())]][0]) , sep="\n")
    
