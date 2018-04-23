#330E

def solveOriginal():
    row = input(">")
    floats = list(map(float, row.split(",")))
    left = floats[0] - floats[2]
    right = floats[0] + floats[2]
    top = floats[1] + floats[2]
    bottom = floats[1] - floats[2]
    
    row = input("")
    while row != "":
        floats = list(map(float, row.split(",")))
        left = min(left, floats[0] - floats[2])
        right = max(right, floats[0] + floats[2])
        top = max(top, floats[1] + floats[2])
        bottom = min(bottom, floats[1] - floats[2])
        row = input("")

    print("(%.3f, %.3f), (%.3f, %.3f), (%.3f, %.3f), (%.3f, %.3f)" % (left, top, right, top, right, bottom, left, bottom))
