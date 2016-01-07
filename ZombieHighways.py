
#Get all of the input tuples
data = input()
data = data.replace("(", "")
data = data.replace(")", "")
data = list(map(int, data.split(", ")))

highways = list(zip(data[0::3], data[1::3], data[2::3]))

numberOfCities = max(data[0::3] + data[1::3]) + 1

#Initialize arrays for use with Dijkstra's algorithm
weights = [[-1 for i in range(numberOfCities)] for j in range(numberOfCities)]

weightsToCities = [0 for i in range(numberOfCities)]
pathToCity = [[] for i in range(numberOfCities)]
isShortest = [False for i in range(numberOfCities)]

#Record when you use the Bfzg to go to each city
BfzgUse = [0 for i in range(numberOfCities)]

for highway in highways:
    c1 = highway[0]
    c2 = highway[1]
    z = highway[2]

    weights[c1][c2] = z
    weights[c2][c1] = z


start = 0
isShortest[0] = True
pathToCity[0] = [0]
for i in range(numberOfCities):
    if weights[0][i] != -1:
        weightsToCities[i] = weights[0][i] + weightsToCities[0]
        pathToCity[i] = pathToCity[0].copy()

print(weightsToCities)
print("")

currIndex = start
while currIndex != numberOfCities -1:
    minDist = -1;
    minIndex = 0;
    for i in range(numberOfCities):
        if not isShortest[i] and (minDist == -1 or
                                    (weightsToCities[i] != 0 and
                                     weightsToCities[i] < minDist)):
            minDist = weightsToCities[i]
            minIndex = i
    isShortest[minIndex] = True
    pathToCity[minIndex].append(minIndex)
    for i in range(numberOfCities):
        if not isShortest[i] and weights[minIndex][i] != -1:
            weightsToCities[i] = weights[minIndex][i] + weightsToCities[minIndex]
            pathToCity[i] = pathToCity[minIndex].copy()
    currIndex = minIndex
    print(weightsToCities)
    print("")
    
    
