#E336

def run():
    nNums,nQueries = list(map(int, input(">").split()))
    nums = sorted(list(map(int, input().split())), reverse=True)
    queries = list(map(int, input().split()))

    counts = [0 for i in range(nQueries)]

    for i in range(nQueries):
        
        
    print(*counts)


if __name__=="__main__":
    run()
