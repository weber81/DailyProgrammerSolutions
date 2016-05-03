import re

class Island():
    def __init__(self, location, value):
        self.location = location
        self.value = value
        self.west = self.east = self.south = self.north = None
        self.connections = [self.west, self.north, self.east, self.south]
        self.bridges = []
        self.eastB = []
        self.westB = []
        self.northB = []
        self.southB = []

    def addBridge(self, bridge):
        if self.checkAddBridge(bridge):
            self.bridges.append(bridge)
            if bridge.horizontal:
                if (bridge.end[0] < self.location[0] or bridge.start[0] < self.location[0]) and len(self.westB) != 2:
                    self.westB.append(bridge)
                if (bridge.end[0] > self.location[0] or bridge.start[0] > self.location[0]) and len(self.eastB) != 2:
                    self.eastB.append(bridge)
            else:
                if (bridge.end[1] < self.location[1] or bridge.start[1] < self.location[1]) and len(self.northB) != 2:
                    self.northB.append(bridge)
                if (bridge.end[1] > self.location[1] or bridge.start[1] > self.location[1]) and len(self.southB) != 2:
                    self.southB.append(bridge)
                    
    def checkAddBridge(self, bridge):
        if len(self.bridges) < self.value:
            if bridge.horizontal:
                if (bridge.end[0] < self.location[0] or bridge.start[0] < self.location[0]) and len(self.westB) != 2:
                    return True
                if (bridge.end[0] > self.location[0] or bridge.start[0] > self.location[0]) and len(self.eastB) != 2:
                    return True
            else:
                if (bridge.end[1] < self.location[1] or bridge.start[1] < self.location[1]) and len(self.northB) != 2:
                    return True
                if (bridge.end[1] > self.location[1] or bridge.start[1] > self.location[1]) and len(self.southB) != 2:
                    return True
        return False

    def findPossibleConnections(self, islands):
        for island in islands:
            if island == self:
                continue
            
            if island.location[1] == self.location[1]:
                if island.location[0] < self.location[0]:
                    if (not self.west) or (self.location[0] - self.west.location[0] > self.location[0] - island.location[0]):
                        self.west = island
                else:
                    if not self.east or self.east.location[0] - self.location[0] > island.location[0] - self.location[0]:
                        self.east = island
                        
            if island.location[0] == self.location[0]:
                if island.location[1] < self.location[1]:
                    if not self.north or self.location[1] - self.north.location[1] > self.location[1] - island.location[1]:
                        self.north = island
                else:
                    if not self.south or self.south.location[1] - self.location[1] > island.location[1] - self.location[1]:
                        self.south = island
                        
        self.connections = [self.west, self.north, self.east, self.south]

    @staticmethod         
    def parse(string):
        m = re.match("island\((?P<x>[0-9]*),(?P<y>[0-9]*),(?P<value>[1-8])\)\.", string)
        try:
            i = Island((int(m.groupdict()["x"]), int(m.groupdict()["y"])), int(m.groupdict()["value"]))
        except:
            return None
        return i

    def __str__(self):
        west = east = north = south = "None"
        
        if self.west != None:            
            west = str(self.west.location) + ", " + str(self.west.value) + ["", " -", " ="][len(self.westB)]
        if self.east != None:
            east = str(self.east.location) + ", " + str(self.east.value) + ["", " -", " ="][len(self.eastB)]
        if self.south != None:
            south = str(self.south.location) + ", " + str(self.south.value) + ["", " |", " ||"][len(self.southB)]
        if self.north != None:
            north = str(self.north.location) + ", " + str(self.north.value) + ["", " |", " ||"][len(self.northB)]
        returnString = "Island@(" + str(self.location) + ") Value:" + str(self.value) + "\n\t<: " + west + "\n\t^: " + north + "\n\t>: " + east + "\n\tv: " + south
        return returnString

    def __repr__(self):
        return self.__str__()

class Bridge():
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.horizontal= start[1] == end[1]

    def checkOverlap(self, bridges):
        for bridge in bridges:
            if self.horizontal ^ bridge.horizontal:
                if self.horizontal and ((bridge.start[0] > self.start[0] and bridge.start[0] < self.end[0]) or
                                        (bridge.start[0] < self.start[0] and bridge.start[0] > self.end[0])) and \
                                        ((bridge.start[1] > self.start[1] and bridge.end[1] < self.start[1]) or 
                                       (bridge.start[1] < self.start[1] and bridge.end[1] > self.start[1])):
                    return True
                if not self.horizontal and ((bridge.start[1] > self.start[1] and bridge.start[1] < self.end[1]) or
                                            (bridge.start[1] < self.start[1] and bridge.start[1] > self.end[1])) and \
                                            ((bridge.start[0] > self.start[0] and bridge.end[0] < self.start[0]) or \
                                           (bridge.start[0] < self.start[0] and bridge.end[0] > self.start[0])):
                    return True
        return False
                
def readInIslands():
    print("Enter Islands")
    line = input()
    islands = []
    while line != "":
        islands.append(Island.parse(line))
        line = input()
    return islands

def findAllAdjacents(islands):
    for island in islands:
        island.findPossibleConnections(islands)

def removeImpossibleAdjacents(islands, bridges):
    for island in islands:
        connectionsToRemove = []
        for connection in island.connections:

            if not connection in islands:
                connectionsToRemove.append(connection)
                
            if connection and Bridge(island.location, connection.location).checkOverlap(bridges):
                connectionsToRemove.append(connection)

            elif connection and connection.value == 1 and island.value == 1:
                connectionsToRemove.append(connection)

            
        for connection in connectionsToRemove:
            index = island.connections.index(connection)
            if index == 0:
                island.west = None
            if index == 1:
                island.north = None
            if index == 2:
                island.east = None
            if index == 3:
                island.south = None
            island.connections = [island.west, island.north, island.east, island.south]


def checkMusts(origIslands, bridges):
    islands = sorted(origIslands, key=lambda x: (x.value - (4-x.connections.count(None))*2), reverse=True)
    islandsToRemove = set()
    for island in islands:
        #If the number of connections is equal to half the value, each connection gets 2
        if (4-island.connections.count(None))*2 == island.value - len(island.bridges):
            for connection in island.connections:
                if connection != None:
                    b = Bridge(island.location, connection.location)
                    if island.checkAddBridge(b) and connection.checkAddBridge(b):
                        island.addBridge(b)
                        island.addBridge(b)
                        
                        connection.addBridge(b)
                        connection.addBridge(b)

                        bridges.append(b)
                        bridges.append(b)
                        
                        if len(connection.bridges) == connection.value:
                            islandsToRemove.add(connection)
            islandsToRemove.add(island)

        #If the number of 2* connections is one more than the value, each connection gets 1 bridge
        elif (4-island.connections.count(None))*2 == island.value+1:
            for connection in island.connections:
                if connection != None:
                    b = Bridge(island.location, connection.location)
                        
                    if island.checkAddBridge(b) and connection.checkAddBridge(b):
                        island.addBridge(b)
                        
                        connection.addBridge(b)

                        bridges.append(b)
                        
                        if len(connection.bridges) == connection.value:
                            islandsToRemove.add(connection)

                        if len(island.bridges) == island.value:
                            islandsToRemove.add(island)
            
        elif (4-island.connections.count(None)) == 1:
                for connection in island.connections:
                    if connection != None:
                        b = Bridge(island.location, connection.location)
                            
                        if island.checkAddBridge(b) and connection.checkAddBridge(b):
                            island.addBridge(b)
                            
                            connection.addBridge(b)

                            bridges.append(b)
                            
                            if len(connection.bridges) == connection.value:
                                islandsToRemove.add(connection)

                            if len(island.bridges) == island.value:
                                islandsToRemove.add(island)
                                
    for i in islandsToRemove:
        origIslands.remove(i)
    print("")


def solve(origIslands):

    #islands = sorted(origIslands, key=lambda x: (x.value, x.connections.count(None)), reverse=True)
    islands = origIslands.copy()
    bridges = []
    checkMusts(islands, bridges)
    draw(origIslands, bridges, islands)

    for _ in range(5):
        removeImpossibleAdjacents(islands, bridges)
        checkMusts(islands, bridges)
        draw(origIslands, bridges, islands)

    islands = sorted(islands, key=lambda x: x.value - len(x.bridges))
    return islands, bridges

def draw(islands, bridges, islands2):
    import pygame, random

    pygame.init()

    WINDOW = pygame.display.set_mode((400, 400))
    pygame.font.init()
    f = pygame.font.Font(pygame.font.get_default_font(), 16)


    for bridge in bridges:
        offset = random.randint(11, 29)
        pygame.draw.line(WINDOW, (0, 255, 0), tuple(map(lambda x: x*40 + offset, bridge.start)),
                         tuple(map(lambda x: x*40 + offset, bridge.end)))
        
    for island in islands:
        pygame.draw.rect(WINDOW, (255, 0, 0), (island.location[0] * 40 + 11, island.location[1] * 40 + 11, 18, 18))
        WINDOW.blit(f.render(str(island.value), True, (0, 0, 255)),
                    (island.location[0] * 40 + 11, island.location[1] * 40 + 11))
        

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    print(*islands2, sep="\n")
                    print("")
                if event.key == pygame.K_t:
                    print(*islands, sep="\n")
                    print("")
                if event.key == pygame.K_e:
                    for bridge in bridges:
                        print(bridge.start, bridge.end)
