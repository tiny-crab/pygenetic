from genetic import *
from chromosome import Chromosome

def instantiateGeneration(chromosomesInGeneration, targetNum):
    generation = []
    for x in range(0, chromosomesInGeneration):
        generation.append(Chromosome())

    for x in range(0, chromosomesInGeneration):
        generation[x].updateFitness(targetNum)

    return generation

def testNumbersToArithmetic():
    for x in range(-10,20):
        print(bitsToArithmetic("{0:b}".format(x)))

def testTranslate():
    first = Chromosome()
    print(first.dnArray)

def testArithmeticArray():
    first = Chromosome()
    print(first.dnArray)
    print(first.arithmeticArray)

def testToRealExpression():
    first = Chromosome()
    print(first.dnArray)
    print(first.arithmeticArray)
    print(toRealExpression(first.arithmeticArray))

def testComputeSum():
    first = Chromosome()
    print(toRealExpression(first.arithmeticArray))
    first.computeSum()

def testUpdateFitness(generation, targetNum):
    for x in range(0, len(generation)):
        print("Chromosome [" + str(x) + "]")
        print(toRealExpression(generation[x].arithmeticArray))
        print("Sum = " + str(generation[x].computeSum()))
        generation[x].updateFitness(targetNum)
        print("Fitness = " + str(generation[x].fitness) + "\n\n" )

def testRecombinate():
    first = Chromosome()
    second = Chromosome()
    print(first.dnArray)
    print(second.dnArray)
    print(first.arithmeticArray)
    print(second.arithmeticArray)
    first.recombinate(second)
    print(first.dnArray)
    print(second.dnArray)
    print(first.arithmeticArray)

def testRouletteSelection(chromosomesInGeneration, targetNum, crossoverRate):
    generation = instantiateGeneration(chromosomesInGeneration)
    for x in range(0, len(generation)):
        generation[x].updateFitness(targetNum)
    first = rouletteWheelSelection(generation,crossoverRate)
    print toRealExpression(first.arithmeticArray)

def printGeneration(generation):
    for x in range(0, len(generation)):
        print("Chromosome[" + str(x) + "]")
        print("Real Expression : ")
        print(toRealExpression(generation[x].arithmeticArray))
        print("Sum = " + str(generation[x].computeSum()))
        print("Fitness = " + str(generation[x].fitness))
        print('\n')
