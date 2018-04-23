#329E

def findLuckyNumbers(findNextHighest=True):
    target = int(input(">"))
    sieve = [(2*i)+1 for i in range(target)]
    index = 1

    newSieve = []
    while sieve[index] < target:
        newSieve = sieve.copy()

        i = sieve[index]
        while i < len(newSieve):
            removed = newSieve.pop(i-1)
            i+= sieve[index] - 1 # the -1 treats it like you didn't remove the item
        
        index += 1
        if len(sieve) != len(newSieve):
            sieve = newSieve

    if(sieve[index] == target):
        print(target, "is a lucky number")
    else:
        print(sieve[index-1], "<", target, "<", sieve[index])
        
    return sieve
