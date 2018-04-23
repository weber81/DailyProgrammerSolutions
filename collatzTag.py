#E317
def collatzTag(row):
    rules = {"a":"bc", "b":"a", "c":"aaa"}
    row = list(row)
    while len(row) != 1:
        print("".join(row))
        condition = row.pop(0)
        row.pop(0)
        row += list(rules[condition])
    print("".join(row))
    
def collatzTag2(number):
    row = ["a" for i in range(number)]
    rules = {"a":"bc", "b":"a", "c":"aaa"}
    while len(row) != 1:
        if all(map(lambda x: x=="a", row)):
            print(len(row))
        condition = row.pop(0)
        row.pop(0)
        row += list(rules[condition])
        
    print(1)    

def collatz(number):
    numSteps = 0
    while number != 1:
        print(number)
        if number % 2 == 0:
            number //= 2
        else:
            number = number * 3 + 1
        numSteps += 1
    print(1)
    return numSteps
