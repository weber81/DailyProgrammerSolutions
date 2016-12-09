#277 Julia Sets!

class Julia():
    def __init__(self, c, threshold, resolution):
        self.f = lambda x: x*x + c
        self.threshold = threshold
        self.resolution = resolution
        self.values = [[0 for i in range(resolution[0])] for j in range(resolution[1])]

    """Generate the Julia Set in the given range

xyRange = (xStart, xEnd, yStart, yEnd)"""
    def create(self, xyRange):
        xStart, xEnd, yStart, yEnd = xyRange
        xSize, ySize = xEnd - xStart, yEnd - yStart
        for i in range(len(self.values)):
            for j in range(len(self.values[i])):
                x = xSize * j / self.resolution[0] + xStart
                y = ySize * i / self.resolution[1] + yStart
                z = complex(x, y)
                loops = 0
                while loops < 200 and abs(z) < self.threshold:
                    z = self.f(z)
                    loops += 1
                self.values[i][j] = loops
        
    def normalizeValues(self):
        maxValue = 0
        for row in self.values:
            if max(row) > maxValue:
                maxValue = max(row)
        if maxValue != 0:
            for i in range(len(self.values)):
                for j in range(len(self.values[i])):
                    self.values[i][j] /= maxValue

    def displaySet(self, channels=(1,1,1), wait=True):
        import pygame
        pygame.init()
        WINDOW = pygame.display.set_mode(self.resolution)
        pygame.display.update()
        pixArray = pygame.PixelArray(WINDOW)
        for i in range(len(self.values)):
            for j in range(len(self.values[i])):
                intensity = int(255 * self.values[i][j])
                pixArray[j][i] = (intensity, intensity, intensity)
            pygame.display.update()
        if wait:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        returnWindow = WINDOW.copy()
                        pygame.quit()
                        return returnWindow
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_s:
                            pygame.image.save(WINDOW, "juliaSet.png")
        else:
            returnWindow = WINDOW.copy()
            pygame.quit()
            return returnWindow

"drawThree(complex(-0.453, .581), complex(-0.446, .573), complex(-0.438, .567))"

def drawThree(res=(640, 480),
              redC=complex(-.221,-.713),
              greenC=complex(-.222, -.714),
              blueC=complex(-.220, -.712)):
    import pygame
    j = Julia(redC, 2, res)
    j.create((-1, 1, -1, 1))
    j.normalizeValues()
    window1 = j.displaySet((1, 0, 0), False)
    
    j = Julia(greenC, 2, res)
    j.create((-1, 1, -1, 1))
    j.normalizeValues()
    window2 = j.displaySet((0, 1, 0), False)
    
    j = Julia(blueC, 2, res)
    j.create((-1, 1, -1, 1))
    j.normalizeValues()
    window3 = j.displaySet((0, 0, 1), False)

    pygame.init()
    WINDOW = pygame.display.set_mode(res)
    pixArray = pygame.PixelArray(WINDOW)
    
    for i in range(window1.get_width()):
        for j in range(window1.get_height()):
            WINDOW.set_at((i,j), (window1.get_at((i,j))[0],window2.get_at((i,j))[1],window3.get_at((i,j))[2]))
        pygame.display.update()
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                returnWindow = WINDOW.copy()
                pygame.quit()
                return returnWindow
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    pygame.image.save(WINDOW, "juliaSet2.png")
