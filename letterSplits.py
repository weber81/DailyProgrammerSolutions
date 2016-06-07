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
    if sentence == "":
        return True
    for i in range(len(sentence)+1):
        if sentence[:i] in wordList:
            if isSentenceInWordList(sentence[i:], wordList):
                return True
    return False
        


if __name__ == "__main__":
    runProgram()
