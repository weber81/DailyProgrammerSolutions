def findFarthestApartNoDouble(string):
    longest = -1
    start = -1
    end = -1
    for i in range(len(string)):
        currentSet = set()
        for j in range(i+1, len(string), 1):
            if string[j] in currentSet:
                break
            if string[j] == string[i]:
                if j-i > longest:
                    longest = j-i
                    start = i
                    end = j
                    break
            else:
                currentSet.add(string[j])
    return start, end;

                    
def fogcreek(string):
    currentIndex = 0
    fogcreekOut = open("fogcreekOut.txt", "w")
    currentChar = string[0]
    start, end = findFarthestApartNoDouble(string)
    while start != -1:
        insideString = string[start+1:end]
        string = string[:start] + insideString + string[end+1:] + string[end]
        fogcreekOut.write(str(end-start) + ":" + string[start] + ":")
        fogcreekOut.write(string + "\n")
        start, end = findFarthestApartNoDouble(string)
        
    if "_" in string:
        string = string[:string.index("_")]
        
    print(string)
    fogcreekOut.write(string + "\r\n")
