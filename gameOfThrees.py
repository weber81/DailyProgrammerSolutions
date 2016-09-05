#E239
def gameOfThrees1(num):
    while num != 1:
        print(num, [0, -1, 1][num%3])
        num = (num + [0, -1, 1][num%3])//3
    print(1)

#I239
def gameOfThrees2(num):
    def gameOfThreesHelper(num, total):
        #End Case
        if num < 3:
            if total%3 == 0:
                return [(1, "")]
            else:
                return None
            
        for i in [(0,), (-1, 2), (-2, 1)][num%3]:
            result = gameOfThreesHelper((num+i)//3, total+i)
            if result != None:
                return result + [(num, i)]
            
    result = gameOfThreesHelper(num, 0)
    if result != None:
        for i in result[::-1]:
            print(*i)
    else:
        print("IMPOSSIBLE")
    return result
