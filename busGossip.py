def extend(routes, length):
    for i in range(len(routes)):
        route = routes[i]
        while len(route) < length:
            route.extend(route)
        routes[i] = route[:length]
    return routes

def runRoute(routes):
    knowledge = {i:{i} for i in range(len(routes))}
    for i in range(len(routes[0])):
        meets = []
        for j in range(len(routes)):
            try:
                meetIndex = meets.index(routes[j][i])
            except ValueError:
                meetIndex = -1
            if meetIndex != -1:
                knowledge[j] = knowledge[j].union(knowledge[meetIndex])
                knowledge[meetIndex] = knowledge[meetIndex].union(knowledge[j])
            meets.append(routes[j][i])
        match = list(knowledge.values())[0]
        finished = True
        for value in list(knowledge.values()):
            if value != match:
                finished = False
        if finished:
            return i
    return "NEVER"

def getRoutes():
    print("Enter Routes")
    row = input()
    routes = []
    while row != "":
        routes.append(list(map(int, row.split(" "))))
        row = input()
    return routes
