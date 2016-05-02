import re

class Island():
    def __init__(self, location, value):
        self.location = location
        self.value = value
        self.west = self.east = self.south = self.north = None
        self.connections = [self.west, self.north, self.east, self.south]

    def findPossibleConnections(self, islands):
        for island in islands:
            if island == self:
                continue
            if island.location[0] == self.location[0]:
                if island.location[1] < self.location[1]:
                    self.west = island
                else:
                    self.east = island
            if island.location[1] == self.location[1]:
                if island.location[0] < self.location[0]:
                    self.north = island
                else:
                    self.south = island
        self.connections = [self.west, self.north, self.east, self.south]

    @staticmethod         
    def parse(string):
        m = re.match("island\((?P<x>[0-9]*),(?P<y>[0-9]*),(?P<value>[1-8])\)\.", string)
        try:
            i = Island((m.groupdict()["x"], m.groupdict()["y"]), m.groupdict()["value"])
        except:
            return None
        return i

    def __str__(self):
        west = east = north = south = None
        
        if self.west != None:
            west = str(self.west.location) + ", " + self.west.value
        if self.east != None:
            east = str(self.east.location) + ", " + self.east.value
        if self.south != None:
            south = str(self.south.location) + ", " + self.south.value
        if self.north != None:
            north = str(self.north.location) + ", " + self.north.value
        returnString = "Island@(" + str(self.location) + ") Value:" + self.value + "\n\t<: " + str(west) + "\n\t^: " + str(north) + "\n\t>: " + str(east) + "\n\tv: " + str(south)
        return returnString

    
    
def readInIslands():
    print("Enter Islands")
    line = input()
    islands = []
    while line != "":
        islands.append(Island.parse(line))
        line = input()
    return islands
