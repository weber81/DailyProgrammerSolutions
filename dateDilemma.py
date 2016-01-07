def part1():
    import re
    
    print("Enter Dates:")
    date = input()
    while date != "":
        date = date.split(re.findall("\D", date)[0])

        day = month = year = ""

        if len(date[0]) == 4:
            year = date[0]
            month = date[1]
            day = date[2]
        else:
            month = date[0]
            day = date[1]
            year = date[2]

        if len(day) == 1:
            day = "0" + day
        if len(month) == 1:
            month = "0" + month

        print(year + "-" + month + "-" + day)
        
        date = input()
