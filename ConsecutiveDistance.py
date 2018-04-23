#E335

def run():
    trials, length = list(map(int, input(">").split()))
    for trial in range(trials):
        nums = list(map(int, input().split()))
        distanceSum = 0
        for i in range(len(nums)-1):
            num = nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == num + 1 or nums[j] == num - 1:
                   distanceSum += (j-i)
        print(distanceSum)


if __name__=="__main__":
    run()
