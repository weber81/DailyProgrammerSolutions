import pygame, sys, math
from pygame.locals import *

def intToColor(color_int):
    b = color_int & 0xFF
    g = (color_int >> 8) & 0xFF
    r = (color_int >> 16) & 0xFF
    return (r, g, b)

def edge_detect(surface):
    width = surface.get_width()
    height = surface.get_height()

    #surface.fill((0, 0, 0))

    pixArray = pygame.PixelArray(surface)

    values = []
    
    for i in range(1, height-1):
        for j in range(1, width-1):            
            a = intToColor(pixArray[j-1][i-1])[0]
            b = intToColor(pixArray[j][i-1])[0]
            c = intToColor(pixArray[j+1][i-1])[0]
            d = intToColor(pixArray[j-1][i])[0]
            e = intToColor(pixArray[j][i+1])[0]
            f = intToColor(pixArray[j+1][i-1])[0]
            g = intToColor(pixArray[j+1][i])[0]
            h = intToColor(pixArray[j+1][i+1])[0]

            E_h = (c + 2*e + h) - (a + 2*d + f)
            E_v = (f + 2*g + h) - (a + 2*b + c)
            E = int(math.sqrt(E_h**2 + E_v**2))
            values.append(int(math.sqrt(E_h**2 + E_v**2)))
            
    m = max(values)
    for i in range(1, height-1):
        for j in range(1, width-1):
            color = (values[(i-1) * (width-2) + (j-1)]*255) // m
            pixArray[j][i] = (color, color, color)
    return values

image = open("edge_detect_test.ppm", "r")

text = [line.strip() for line in image][1:]

image.close()

text = list(filter(lambda x: not x.startswith("#"), text))
text = list(filter(lambda x: not x == "", text))

text = list(map(lambda x: min(int(x), 255), " ".join(text).split(" ")))

width = text[0]
height = text[1]
maxColor = text[2]

pixels = list(zip(text[3::3], text[4::3], text[5::3]))

pygame.init()
window = pygame.display.set_mode((width, height))

pixArray = pygame.PixelArray(window)

for i in range(height):
    for j in range(width):
        pixArray[j][i] = pixels[i * width + j]
    pygame.display.update()

del pixArray
values = []
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                values = edge_detect(window)
                pygame.display.update()
            if event.key == pygame.K_g:
                pixArray = pygame.PixelArray(window)

                for i in range(height):
                    for j in range(width):
                        color = pixels[i*width + j]
                        avgColor = color[0] + color[1] + color[2]
                        avgColor //= 3
                        pixArray[j][i] = (avgColor, avgColor, avgColor)
                    pygame.display.update()
            
                del pixArray
            if event.key == pygame.K_r:
                pixArray = pygame.PixelArray(window)

                for i in range(height):
                    for j in range(width):
                        pixArray[j][i] = pixels[i * width + j]
                    pygame.display.update()

                del pixArray
