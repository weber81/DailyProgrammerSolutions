file = open("enable1.txt")
dictionary = file.read().splitlines()

def buildUp(dictionary, bases):
    n = 2
    if len(bases) != 0:
        n = len(bases[0]) + 1
    newDict = []
    for word in dictionary:
        if len(word) != n:
            continue
        buildable = any(map(lambda base: base in word, bases)) or bases == []
        if buildable:
            newDict.append(word)
    return newDict

def findLongestBuildUps(dictionary):
    bases = buildUp(dictionary, [])
    longest = []
    while bases != []:
        longest = bases
        bases = buildUp(dictionary, bases)
    return longest

def getWordsOfSizeN(dictionary, n):
    newDict = []
    for word in dictionary:
        if len(word) != n:
            continue
        newDict.append(word)
    return newDict
    

def tearDown(dictionary, longWord):
    n = len(longWord)-1
    possibles = []
    for word in dictionary:
        if len(word) != n:
            continue
        if word in longWord:
            possibles.append(word)
    return possibles

def findPath(longestWord, dictionary):
    if len(longestWord) == 2:
        return [longestWord]
    possibles = tearDown(dictionary, longestWord)
    for p in possibles:
        path = findPath(p, dictionary)
        if path != None:
            path.append(longestWord)
            return path
    return None

def fullBuildUp(dictionary):
    longests = findLongestBuildUps(dictionary)
    return list(map(lambda x: findPath(x, dictionary)[::-1], longests))
