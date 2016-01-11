def bruteForce():
    print("Input data")

    values = list(map(float, input().split(" ")))

    return max([item for l in \
                [list(zip(values[:i-1],(values[i],)*i)) \
                     for i in range(len(values)-1)] for item in l],
               key=lambda x: x[1]-x[0])
