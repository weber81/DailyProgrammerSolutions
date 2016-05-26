#amount = int(input())

#N|1|2 |3
#C|X|11|25
#

#2 sailors: 2, 5, 11
#3 sailors: 6, 10,16,25
#4 sailors: 36, 48, 
#5 sailors: 0, 5, 30, 155, 780

#start = N * (N-1)^(N-2)

#next = (N-1)/N*prev - 1
#prev = (next+1)*N/(N-1)

#end = amount * ((amount -1)**(amount-2))

"""for i in range(amount):
    end *= amount / (amount -1)
    end += 1

print(end)
"""
def withoutMonkey(number):
    end = number * (number-1)** number
    for i in range(number):
        end *= number / (number-1)
    print(end)
    #number^(number+1)

def withMonkeyBruteForce(number):
    for i in range(number, 100000000, number):
        start = i
        #start is N-1/N of the previous step,
        #So backwards is N/N-1
        #So at any point, the number of coconuts \ N-1
        try:
            for j in range(number):
                if start//(number-1) != start/(number-1):
                    raise ValueError
                start = start//(number-1)
                start *= number
                start += 1
            print(i, start)
            break
        except ValueError:
            pass
        
