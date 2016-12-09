"""RULES:
White -> -White & -Black
Red -> Green
Black -> -White & -Green & -Orange
orange -> Red | Black
green -> Orange | White
purple -> -Purple & -Green & -Orange & -White"""


def ruleBased():
    colorRules = {"white":["purple", "red", "green", "orange"],
                  "red":["green"],
                  "black":["black", "purple", "red"],
                  "orange":["black", "red"],
                  "green":["orange", "white"],
                  "purple":["black", "red"]}

    colorList = []
    line = input()

    while line != "":
        colorList.append(line)
        line = input()

    for i in range(len(colorList)-1):
        if colorList[i+1] not in colorRules[colorList[i]]:
            print('"Boom"')
            return

    print('"Bomb Defused"') 

def stateMachine():
    states = ["white", "red", "black", "orange", "green", "purple", "boom"]
    transitionDict = {"start":
                          {"white":"white",
                           "red":"red",
                           "black":"black",
                           "purple":"purple",
                           "green":"green",
                           "orange":"orange",
                           "boom": "boom",
                           "":"defused"},
                      "white":
                          {"white":"boom",
                           "red":"red",
                           "black":"boom",
                           "purple":"purple",
                           "green":"green",
                           "orange":"orange",
                           "boom": "boom",
                           "":"defused"},
                      "red":
                          {"white":"boom",
                           "red":"boom",
                           "black":"boom",
                           "purple":"boom",
                           "green":"green",
                           "orange":"boom",
                           "boom": "boom",
                           "":"defused"},
                      "black":
                          {"white":"boom",
                           "red":"red",
                           "black":"black",
                           "purple":"purple",
                           "green":"boom",
                           "orange":"boom",
                           "boom": "boom",
                           "":"defused"},
                      "orange":
                          {"white":"boom",
                           "red":"red",
                           "black":"black",
                           "purple":"boom",
                           "green":"boom",
                           "orange":"boom",
                           "boom": "boom",
                           "":"defused"},
                      "green":
                          {"white":"white",
                           "red":"boom",
                           "black":"boom",
                           "purple":"boom",
                           "green":"boom",
                           "orange":"orange",
                           "boom": "boom",
                           "":"defused"},
                      "purple":
                          {"white":"boom",
                           "red":"red",
                           "black":"black",
                           "purple":"boom",
                           "green":"boom",
                           "orange":"boom",
                           "boom": "boom",
                           "":"defused"},
                      "boom":
                          {"white":"boom",
                           "red":"boom",
                           "black":"boom",
                           "purple":"boom",
                           "green":"boom",
                           "orange":"boom",
                           "boom": "boom",
                           "":"failed"}
                      }
    state = "start"
    while state != "defused" and state != "failed":
        try:
            state = transitionDict[state][input()]
        except KeyError:
            print("You must give a correct color")
    if state == "defused":
        print('"Bomb defused"')
    else:
        print('"Boom"')
