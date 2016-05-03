def permutationGenerator(l):
    if len(l) == 0:
        yield []
    else:
        for i in range(len(l)):
            newList = l[:i] + l[i+1:]
            for perm in permutationGenerator(newList):
                yield [l[i]] + perm

def permutation(nth, x):
    order = [i for i in range(x)]
    newArray = []
    g = permutationGenerator(order)
    for _ in range(nth):
        newArray = next(g)
    return newArray
    
def combinationGenerator(l, r):
    if r == 0:
        yield []
    else:
        for i in range(len(l)):
            newList = l[:i] + l[i+1:]
            for comb in combinationGenerator(newList, r-1):
                if sorted([l[i]] + comb) == [l[i]] + comb:
                    yield [l[i]] + comb
                
def combination(nth, n, r):
    order = [i for i in range(n)]
    newArray = []
    g = combinationGenerator(order, r)
    for _ in range(nth):
        newArray = next(g)
    return newArray

def getAllPermutations(x):
    return [_ for _ in permutationGenerator(list(range(x)))]

def getAllCombinations(n, r):
    return [_ for _ in combinationGenerator(list(range(n)), r)]
