class MirrorCipher():
    def __init__(self, grid):
        letterMap = {(i-ord('a'), -1):chr(i) for i in range(ord('a'), ord('m')+1)}
        letterMap.update({(13, i-ord('n')):chr(i) for i in range(ord('n'), ord('z')+1)})
        letterMap.update({(-1, i-ord('A')):chr(i) for i in range(ord('A'), ord('M')+1)})
        letterMap.update({(i-ord('N'), 13):chr(i) for i in range(ord('N'), ord('Z')+1)})

        keys = letterMap.keys()
        self.cipherMapping = {}

        for k in keys:
            if not letterMap[k] in self.cipherMapping:
                pos = k
                direction = (1, 0)
                if k[0] == -1:
                    direction = (1, 0)
                if k[1] == -1:
                    direction = (0, 1)
                if k[0] == 13:
                    direction = (-1, 0)
                if k[1] == 13:
                    direction = (0, -1)
                pos = (pos[0] + direction[0], pos[1] + direction[1])
                while pos[0] != -1 and pos[0] != 13 and pos[1] != -1 and pos[1] != 13:
                    if grid[pos[1]][pos[0]] == "\\":
                        direction = (direction[1], direction[0])
                    if grid[pos[1]][pos[0]] == "/":
                        direction = (-direction[1], -direction[0])
                    pos = (pos[0] + direction[0], pos[1] + direction[1])
                self.cipherMapping.update({letterMap[k]:letterMap[pos]})
                self.cipherMapping.update({letterMap[pos]:letterMap[k]})
        self.letterMap = letterMap

    def encrypt(self, text):
        return "".join(map(lambda x: self.cipherMapping[x], text))

def getGridFromString(gridString):
    if type(gridString) == str:
        grid = gridString.split("\n")
    else:
        grid = gridString
    grid = list(map(lambda x: x.ljust(13, " "), grid))
    return grid

def getGridFromInput():
    return getGridFromString([input() for i in range(13)])

def solveInput():
    grid = getGridFromInput()
    c = MirrorCipher(grid)
    print(c.encrypt(input()))
    return c
