import random
class Markov():
    def __init__(self):
        self.bigramDict = {}

    def populate(self, text):
        prevStrings = (None, None)
        for t in text.replace(" ", ".").split(".") + [None]:
            if t == "":
                t = None
            if prevStrings == (None, None) and t == None:
                continue
            temp = self.bigramDict.get(prevStrings, [])
            temp.append(t)
            self.bigramDict.update({prevStrings: temp})
            prevStrings = (prevStrings[1], t)
            
    def generate(self, length=-1):
        string = ""
        prevStrings = (None, None)
        if length != -1:
            for i in range(length):
                temp = self.bigramDict[prevStrings]
                nextString = random.choice(temp)
                prevStrings = (prevStrings[1], nextString)
                if nextString == None:
                    prevStrings = (None, None)
                string += (nextString if nextString != None else ".") + " "
        else:
            temp = self.bigramDict[prevStrings]
            nextString = random.choice(temp)
            while nextString != None:
                string += nextString + " "
                prevStrings = (prevStrings[1], nextString)
                temp = self.bigramDict[prevStrings]
                nextString = random.choice(temp)
        return string
                
