def secretSanta():
    #Step 1: Initialize Stuff
    import random
    familyMap = {} #Map Names to Families
    giftRing = [] #Ring of Names representing gifter and giftees
    familyIndex = 0 #Current Family

    #Step 2: Get Names and put them in both the family map and giftRing
    print("Enter giftRing with each family on a separate line")
    family = input()
    while family != "":
        giftRing += family.split(" ")
        familyMap.update({x:familyIndex for x in family.split(" ")})
        familyIndex += 1
        family = input()
        
    #Step 3: Enter Random!
    random.shuffle(giftRing)

    checks = 0
    #Step 4: Check the loop to make sure family doesn't gift to family
    checkAgain = True
    while checkAgain:
        checks += 1
        checkAgain = False

        #Step 4a (part 1 of 4): For each person in the ring...
        for index1 in range(len(giftRing)-1):
            person1 = giftRing[index1]
            
            index2 = (index1 + 1)%len(giftRing)
            person2 = giftRing[index2]

            #Step 4a (part 2 of 4): If they are gifting to their own family...
            if familyMap[person1] == familyMap[person2]:

                #Step 4a (part 3 of 4): Look for the next person who is not in their family...
                index3 = index2
                person3 = person2

                while familyMap[person1] == familyMap[person3]:
                    index3 += 1
                    index3 %= len(giftRing)
                    person3 = giftRing[index3]

                #Step 4a (part 4 of 4): And then swap the giftee with that new person
                giftRing[index2], giftRing[index3] = giftRing[index3], giftRing[index2]

                #Step 4b: Remember to check the list again to make sure you didn't create any problems
                checkAgain = True

    #Step 5: Print the Results
    print(checks)
    for i in range(len(giftRing)):
        print(giftRing[i] + "->" + giftRing[(i+1)%len(giftRing)])
    return giftRing
