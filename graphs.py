#Format from Challenge 266E
def getEasyInput():
    print("Enter # nodes then each connection on a new line:")
    numNodes = int(input())
    connections = []
    line = input()
    while line != "":
        connections.append(list(map(int, line.split(" "))))
        line = input()
    return numNodes, connections

#Format from Challenge 266I
def getIntermediateInput():
    print("Enter # lines, then each connection on a new line:")
    numLines = int(input())
    connections = [list(map(int, input().split(" "))) for _ in range(numLines)]
    numNodes = max(max(connections, key=lambda x: max(x)))
    return numNodes, connections

#Format from Challenge 266H
def getHardInput():
    print("Enter # nodes then each connection on a new line:")
    numNodes = int(input())
    connections = []
    line = input()
    while line != "":
        connections.append(list(map(int, line.split(" "))))
        line = input()
    return numNodes, connections

def getDegrees(numNodes, connections):
    degrees = [0 for n in range(numNodes)]
    for c in connections:
        degrees[c[0]-1] += 1
        degrees[c[1]-1] += 1
    return degrees

def printDegrees(degrees):
    for i in range(len(degrees)):
        print("Node {} has a degree of {}".format(i+1, degrees[i]))

def getAdjacencyMatrix(numNodes, connections, directed=False):
    matrix = [[0 for i in range(numNodes)] for j in range(numNodes)]
    for c in connections:
        matrix[c[0]-1][c[1]-1] = 1
        if not directed:
            matrix[c[1]-1][c[0]-1] = 1
    return matrix

def printAdjacencyMatrix(matrix):
    for y in range(len(matrix)):
        print(" ".join(map(str, matrix[y])))

def getEccentricities(matrix):
    return [getEccentricity(matrix, i) for i in range(len(matrix))]

    
def getEccentricity(matrix, node):
    return len(max(getShortestPaths(matrix, node), key=len)) - 1

def getShortestPaths(matrix, node):
    path = [[] for i in range(len(matrix))]
    path[node] = [node]
    nodeStack = [node]
    while len(nodeStack) != 0:
        currentNode = nodeStack.pop()
        p = path[currentNode]
        for i in range(len(matrix[currentNode])):
            if matrix[currentNode][i] and (len(path[i]) == 0 or len(path[i]) > len(p)+1):
                nodeStack.append(i)
                path[i] = p.copy()
                path[i].append(i)
    return path

def getGraphRadiusAndDiameter(numNodes, connections):
    matrix = getAdjacencyMatrix(numNodes, connections, True)
    E = getEccentricities(matrix)
    return min(filter(lambda x: x > 0, E)), max(E)

def findGraphCenter(numNodes, connections):
    matrix = getAdjacencyMatrix(numNodes, connections, True)
    E = getEccentricities(matrix)
    radius = min(filter(lambda x: x > 0, E))
    index = E.index(radius)
    indeces = []
    while index != -1:
        indeces.append(index)
        index = E.index(radius, index+1)
    return indeces

def getAllIndeces(a, val):
    indeces = []
    for i in range(len(a)):
        if a[i] == val:
            indeces.append(i)
    return indeces

def powerset(iterable):
    from itertools import chain, combinations
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"

    s = sorted(list(iterable))
    return chain.from_iterable(list(combinations(s, r)) for r in range(len(s)+1))

def getCliques(numNodes, connections, findAll=False):
    matrix = getAdjacencyMatrix(numNodes, connections, False)
    maxSubSet = max(map(sum, matrix))
    possibleCliques = {}

    import itertools

    for row in matrix:
        powerSet = set(map(lambda x: tuple([matrix.index(row)]+x),
                       map(list, powerset(getAllIndeces(row, 1)))))
        for item in powerSet:
            item = tuple(sorted(item))
            possibleCliques.update({item: possibleCliques.get(item, 0)+1})

    keys = sorted(list(possibleCliques.keys()), reverse=True, key=len)
    for k in keys:
        if len(k) == possibleCliques[k]:
            print(" ".join(list(map(lambda x: str(x+1), k))))
            if not findAll:
                break
        
    return matrix, maxSubSet, possibleCliques
