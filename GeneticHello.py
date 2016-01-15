import random

def fitness(s, goal):
    """Hamming Distance Fitness"""
    return sum(list(map(lambda x: int(bool(abs(ord(x[0]) - ord(x[1])))), zip(s, goal))))

def reverseFitness(fitnesses):
    m = max(fitnesses)
    fitnesses = list(map(lambda x: (m+1)-x, fitnesses))
    return fitnesses

def generatePop(length, size):
    pop = []
    fitnesses = []
    for _ in range(size):
        testString = ""
        for i in range(length):
            testString += chr(random.randint(32, 126))
        pop.append(testString)
        fitnesses.append(fitness(testString, goal))
    return pop, fitnesses

def pickTwo(pop, fitness, total=-1):
    if total == -1:
        total = sum(fitness)
    i = -1
    
    number = random.randint(0, total-1)
    while number > 0:
        i += 1
        number -= fitness[i]
        i %= len(fitness)
    i1 = i
    i = 0
    pop1 = pop[i1]
    number = random.randint(0, total - 1 - fitness[i])
    while number > 0:
        i += 1
        if i == i1:
            i += 1
        i %= len(fitness)
        number -= fitness[i]
    i2 = i
    pop2 = pop[i2]
    return pop1, pop2

CROSSOVER_RATE = .2
MUTATE_RATE = .01
def breed(parent1, parent2):
    i = 0
    parents = (parent1, parent2)
    child = ""
    for j in range(len(parents[i])):
        if random.random() < MUTATE_RATE:
            child += chr(random.randint(32, 126));
        else:
            child += parents[i][j]
        if random.random() < CROSSOVER_RATE:
            i = -i + 1
    return child

goal = input("Enter goal string: ")
l = len(goal)

POP_SIZE = 300

pop, fitnesses = generatePop(l, POP_SIZE)
generation = 0

while min(fitnesses) != 0 and generation < 10000:
    newPop = []
    newFit = []
    rFitnesses = reverseFitness(fitnesses)
    total = sum(rFitnesses)
    for i in range(POP_SIZE):
        child = breed(*pickTwo(pop, rFitnesses, total))
        newPop.append(child)
        newFit.append(fitness(child, goal))
    pop = newPop
    fitnesses = newFit

    generation += 1

    bestChildi = fitnesses.index(min(fitnesses))
    print(generation, ",", pop[bestChildi], fitnesses[bestChildi])
    
