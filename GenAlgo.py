import numpy as np
from random import randrange


class Unit:
    def __init__(self, accuracy, gen):
        self.accuracy = accuracy
        self.gen = gen

    fitness = 0
    accuracy = 0.0
    gen = []


def firstGeneration():
    fitnessSum = 0.0
    for i in range(0, generationSize):
        prelist = []
        for j in range(0, len(parameters)):
            prelist.append(randrange(sum))
        currentGeneration.append(Unit(0.0, prelist))
    for i in range(0, generationSize):
        value = 0
        for j in range(0, len(parameters)):
            value += currentGeneration[i].gen[j] * parameters[j]
        if abs(value - sum == 0):
            print("решение найдено: " + currentGeneration[i].gen)
        currentGeneration[i].fitness = abs(value - sum)
        fitnessSum += 1.0 / abs(value - sum)
    for i in range(0, generationSize):
        currentGeneration[i].accuracy = 1.0 / currentGeneration[i].fitness / fitnessSum


def getNewUnit():
    probs = []
    for i in range(0, len(currentGeneration)):
        probs.append(currentGeneration[i].accuracy)
    firstParent = np.random.choice(currentGeneration, 1, p=probs)[0]
    secondParent = np.random.choice(currentGeneration, 1, p=probs)[0]
    rand = randrange(0, len(parameters))
    dominantParent = randrange(0, 2)
    if dominantParent == 0:
        gens = firstParent.gen
        gens[rand] = secondParent.gen[rand]
        mutationProb = randrange(0, 101)
        if mutationProb < mutationChance:
            rand2 = randrange(0, len(parameters))
            gens[rand2] = randrange(0, 31)
        return Unit(0.0, gens)
    else:
        gens = secondParent.gen
        gens[rand] = firstParent.gen[rand]
        mutationProb = randrange(0, 101)
        if mutationProb < mutationChance:
            rand2 = randrange(0, len(parameters))
            gens[rand2] = randrange(0, 31)
        return Unit(0.0, gens)


def anotherGeneration():
    fitnessSum = 0.0
    newGeneration = []
    for i in range(0, generationSize):
        newGeneration.append(getNewUnit())
    currentGeneration = newGeneration  # отладить
    for i in range(0, generationSize):
        value = 0
        for j in range(0, len(parameters)):
            value += currentGeneration[i].gen[j] * parameters[j]
        if abs(value - sum == 0):
            print("решение найдено: ")
            print(*currentGeneration[i].gen)
            exit(0)
        currentGeneration[i].fitness = abs(value - sum)
        fitnessSum += 1.0 / abs(value - sum)
    for i in range(0, generationSize):
        currentGeneration[i].accuracy = 1.0 / currentGeneration[i].fitness / fitnessSum


# параметры конфигурации
sum = 30
generationSize = 5  # кол-во порождаемых элементов
mutationChance = 10  # в процентах
parameters = [1, 2, 3, 4]
# parameters задает кол-во и числа у аргументов

currentGeneration = []
firstGeneration()
while 1:
    anotherGeneration()
