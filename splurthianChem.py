"""Check if symbol is allowed.
Rules:
1) Must be two letters long
2) Letters must appear in order in the element"""
def SplurthianChem(element, symbol):
    try:
        #Check for the first letter in the symbol,
        #Then check for the second letter after the first letter
        element.lower().index(symbol.lower()[1],
                              element.lower().index(symbol.lower()[0])+1)
        return True
    except ValueError:
        return False

"""Check for the first letter alphabetically,
then check for the first letter alphabetically after that letter"""
def SplurthianChemBonus1v1(element):
    element = element.lower()
    startCharIndex = 0

    #Find the earliest letter in the string (Minus the last character)
    for char in range(ord("a"), ord("z")+1):
        if chr(char) in element[:len(element)-1]:
            startCharIndex = element.index(chr(char))
            break
        
    #Find the earliest letter alphabetically after the first letter
    for char in range(ord("a"), ord("z")+1):
        if chr(char) in element[startCharIndex+1:]:
            return element[startCharIndex].upper() + chr(char)

"""Make list of all letter pairs, then sort"""
def SplurthianChemBonus1v2(element):
    return sorted([element[j].upper() + element[i]
                       for j in range(len(element)) #Grab each letter
                       for i in range(j+1, len(element))])[0].capitalize() #Grab each letter after the first

"""Count number of valid letter pairs"""
def SplurtianChemBonus2(element):
    return len(set([element[j].upper() + element[i]
                       for j in range(len(element))
                       for i in range(j+1, len(element))]))

"""Blurthian Rules are the Same as Splurthian, except Rule 1 doesn't exist,
Symbols can be any length"""
def BlurthianChem(element, symbol):
    element = element.lower()
    index = -1
    #Check each letter in the symbol and make sure it exists
    #as you remove previous letters
    for char in symbol.lower():
        if char not in element[index+1:]:
            return False
        index = element[index+1:].index(char)
    return True

"""Get the longest, earliest alphabetically symbol:
e.g. Gozerium:
Gom > Zeri
Gori > Go
Eim >>> Everything Else
"""
def BlurthianChemBonus1(element):
    elementName = ""
    element = element.lower()
    try:
        #Keep going until you are our of characters
        while len(element) != 0:
            #Find the earliest letter alphabetically
            for char in range(ord("a"), ord("z")+1):
                if chr(char) in element:
                    elementName += chr(char)
                    element = element[element.index(chr(char))+1:]
                    break
    except ValueError:
        pass
    return elementName.capitalize()

def BlurthianChemBonus2(element):
    return len(set(x for x in BlurthianGenerator(element)))

"""Generate a Blurthian Symbol for the element"""
def BlurthianGenerator(element):
    size = len(element)
    #Go through each number between 1 and 1111... (2^len(element))
    #1 represents use the letter,
    #0 represents ignore the letter
    for i in range(1, 2**size):
        symbol = ""
        for j in range(size):
            if (i >> j) % 2:
                symbol = element[size-1-j] + symbol
        yield symbol.capitalize()
