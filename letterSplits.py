def runProgram(readFile=True):

    wordList = []
    if readFile:
        f = open("enable1.txt", "r")
        wordList = f.read().splitlines()
        f.close()
        
    numbers = input()

    i = 0

    numLetDict = dict(list(map(lambda x: (str(x+1), chr(x+ord('A'))),
                               range(0, ord('z')-ord('a')+1))))

    words = []

    word = [1, numLetDict[numbers[0]]]
    words.append(word)

    if numbers[0:2] in numLetDict:
        words.append([2, numLetDict[numbers[0:2]]])

    while len(words) > 0:
        newWords = []
        for index, word in words:
            if index >= len(numbers):
                if readFile:
                    if isSentenceInWordList(word.lower(), wordList):
                        print(word)
                else:
                    print(word)
                continue
            if numbers[index] == '0':
                continue
            newWords.append([index+1, word + numLetDict[numbers[index]]])
            if index +2 <= len(numbers) and numbers[index:index+2] in numLetDict:
                newWords.append([index+2, word + numLetDict[numbers[index:index+2]]])
        words = newWords

digraphs = None
def isSentenceInWordList(sentence, wordList):
    
    for word in wordList:
        for i in range(len(word)-1):
            digraphs.add(word[i:i+2])
    possibleWordBreaks = set()
    for i in range(len(sentence)+1):
        if not sentence[i:i+2] in digraphs and len(possibleWordBreaks) == 0:
            return False
        if sentence[0:i] in wordList:
            possibleWordBreaks.add(sentence[0:i] + "/")
        for breaks in possibleWordBreaks.copy():
            if not sentence[len(breaks)-1+i:len(breaks)+i+1] in digraphs \
                and len(possibleWordBreaks) == 0:
                return False
            if sentence[len(breaks)-1:i] in wordList:
                possibleWordBreaks.add(breaks + sentence[len(breaks)-1:i] + "/")
    if any(map(lambda x: len(x.replace("/","")) == len(sentence), possibleWordBreaks)):
        for b in possibleWordBreaks:
            if len(b.replace("/", "")) == len(sentence):
                print(b)
    return any(map(lambda x: len(x.replace("/","")) == len(sentence), possibleWordBreaks))
        


#if __name__ == "__main__":
#    runProgram()
