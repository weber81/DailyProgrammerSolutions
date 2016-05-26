def findSelfDescriptives(size):
    solutions = []
    for i in range(10**(size-1), 10**size -1, 10**(size//3)):
        iStr = str(i)
        selfDescript = True
        if sum(map(int, iStr)) != size:
            continue
        for j in range(len(iStr)):
            if iStr.count(str(j)) != int(iStr[j]):
                selfDescript = False
                break
        if selfDescript:
            solutions.append(i)

    if len(solutions) != 0:
        print(*solutions, sep="\n")
    else:
        print("No self-descriptive number found")
            
