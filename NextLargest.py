number = input()
while number.strip() != "":
    number = list(number[::-1])
    index = 0
    while index < len(number) and int(number[index]) <= int(number[index+1]):
        index+=1
    if index == len(number):
        print("Already biggest")
    else:
        startIndex = 0
        while number[startIndex] == "0":
            startIndex += 1
        temp = number[startIndex]
        number[startIndex] = number[index+1]
        number[index+1] = temp
        print("".join(sorted(number[index+1:])) + "".join((number[:index+1])))
    number = input()
