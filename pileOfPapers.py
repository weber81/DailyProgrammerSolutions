def placePaper():
    width, height = list(map(int, input().split()))
    grid = [[0 for x in range(width)] for y in range(height)]
    numbers =set()
    numbers.add(0)
    
    line = input()
    while line != "":
        number, startx, starty, width, height = list(map(int, line.split()))
        numbers.add(number)
        for x in range(startx, startx + width):
            for y in range(starty, starty+height):
                grid[y][x] = number
        line = input()
    for n in numbers:
        count = sum(map(lambda x: x.count(n), grid))
        print(n, count)
