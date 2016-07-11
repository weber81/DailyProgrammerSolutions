import functools

#All the places your dog didn't win
def E267():
    print(", ".join(filter(None, [[((str(i) + (["th", "st", "nd"] + ["th"]*8)[i%10 if i//10%10 != 1 else 0]) if i != int(j) else "") for i in range(1,200)] for j in range(int(input())+1)][-1])))

#Atbash Cipher
def E254():
    print(*[{chr(i):chr(ord('z')-i + ord('a')) for i in range(ord('a'), ord('z')+1)}.get(j, j) for j in input().lower()], sep="")

#Atbash Cipher Bonus
def E254B():
    print(*[{**{chr(i):chr(ord('z')-i + ord('a')) for i in range(ord('a'), ord('z')+1)},**{chr(i):chr(ord('Z')-i + ord('A'))for i in range(ord('A'), ord('Z')+1)}}.get(j, j) for j in input()], sep="")

#Abundand And Deficient Numbers
def E243():
    return list(map(lambda x: "{} abundant by {}".format(x[0], x[1]-x[0]) if x[0]-x[1] < 0 else ("{} deficient".format(x[0]) if x[0] != x[1] else "{} ~~neither~~".format(x[0])), [(j,sum(list([((i if j%i == 0 else 0) for i in range(1, j))][0])))for j in [int(input(">>"))]]))[0]

#Funny Plant
def E242():
    #return functools.reduce(lambda x, y:(([x[0][i]+1 for i in range(len(x[0]))]+[0]*(sum(x[0])+len(x[0]))), x[1], x[2]+1)if sum(x[0]) < x[1]else x,*[[([0]*j, i, 1) for k in range(i)] for i, j in [list(map(int, input().split()))]])
    print(functools.reduce(lambda x, y:(([x[0][i]+1 for i in range(len(x[0]))]+[0]*(sum(x[0])+len(x[0]))), x[1], x[2]+1)if sum(x[0]) < x[1]else x,*[[([0]*j, i, 1) for k in range(i)] for i, j in [list(map(int, input().split()))]][2]))
    
#Alphabetical words
def E228():
    [print(i+" IN ORDER")if list(i)==sorted(i)else(print(i+" REVERSED")if sorted(i)==list(i)[::-1]else print(i+" NOT IN ORDER"))for i in[input(">").lower()]]

#Stock Trading
def E249():
    print(max(list(map(lambda x: max(x, key=lambda y: y[1]-y[0]), [[list(zip(i, i[j:])) for j in range(2, len(i))] for i in [list(map(float, input(">").split()))]][0])), key=lambda x: x[1]-x[0]))

#Splurtian Chemistry
def E275(element, symbol):
    try:
        element.lower().index(symbol.lower()[1], element.lower().index(symbol.lower()[0])+1)
        return True
    except ValueError:
        return False

