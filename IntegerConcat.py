import itertools
def E314OneLine():
    print(*list(map(lambda x: (x[0], x[-1]), [sorted(list(map(lambda x: int("".join(x)), list(itertools.permutations(input().split())))))]))[0])

def E314Faster():
    values = input().split()
    maxLen = len(max(values, key=len))

    equaledValues = list(map(lambda x: (x[:-1] + (x[-1] * (maxLen - len(x) + 1)),
                                        x),
                             values))

    equaledToValues = dict(equaledValues)

    sortedValues = list(sorted(list(map(lambda x: x[0], equaledValues))))

    smallestValue = "".join(list(map(lambda x: equaledToValues[x], sortedValues)))
    largestValue = "".join(list(map(lambda x: equaledToValues[x], sortedValues[::-1])))

    #print("".join(list(map(lambda x: equaledToValues[x], sortedValues))))
    #print("".join(list(map(lambda x: equaledToValues[x], sortedValues[::-1]))))

    print(smallestValue, largestValue)
    return smallestValue, largestValue
