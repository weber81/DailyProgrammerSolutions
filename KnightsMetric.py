moves = [(-1, -2), (1, -2), (-1, 2), (1, 2), (-2, -1), (2, -1), (-2, 1), (2, 1)]

def E316():
    xPos, yPos = map(int, input().split())
    hitList = set()
    poses = [(0, 0, 0)]
    #Brute force method. BFS of all moves
    while True:
        pos = poses.pop(0)
        for move in moves:
            newPos = (pos[0] + move[0], pos[1] + move[1])
            if newPos == (xPos, yPos):
                return pos[2] + 1
            if not newPos in hitList:
                hitList.add(newPos)
                poses.append((newPos[0], newPos[1], pos[2] + 1))
    return xPos, yPos
