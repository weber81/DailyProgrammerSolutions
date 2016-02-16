def calc(numbers, goal, total=0):
    answer = ""
    #End cases:
    #1) Run out of Numbers
    #2) Get a fractional total
    if len(numbers) == 0 or total%1 != 0 or total < 0:
        return (len(numbers) == 0 or total < 0) and total == goal

    #Try + - * /
    for number in numbers:
        split = numbers.index(number)
        result = calc(numbers[:split]+numbers[split+1:], goal, total + number)
        if result:
            if type(result) == bool:
                return "+" + str(number)
            return "+" + str(number) + result
        
        result = calc(numbers[:split]+numbers[split+1:], goal, total - number)
        if result:
            if type(result) == bool:
                return "-" + str(number)
            return "-" + str(number) + result
        
        result = calc(numbers[:split]+numbers[split+1:], goal, total * number)
        if result:
            if type(result) == bool:
                return "*" + str(number)
            return "*" + str(number) + result
        
        result = calc(numbers[:split]+numbers[split+1:], goal, total / number)
        if result:
            if type(result) == bool:
                return "/" + str(number)
            return "/" + str(number) + result
    return False

def startCalc(numbers, goal):
    answer = ""
    for number in numbers:
        split = numbers.index(number)
        result = calc(numbers[:split]+numbers[split+1:], goal, number)
        if result:
            return str(number) + result
    return "NOT POSSIBLE"

def parseInput():
    inputLine = input("Type numbers and total in form # # #... makes #: ").split()
    numbers = []
    for i in range(len(inputLine)-2):
        numbers.append(int(inputLine[i]))
    return numbers, int(inputLine[len(inputLine)-1])

