from genetic import *
from testGenetic import *
from chromosome import Chromosome

def main():
    #-------------
    #testing block
    #-------------
    #testNumbersToArithmetic()
    #testTranslate()
    #testArithmeticArray()
    #testToRealExpression()
    #testComputeSum()
    #testRecombinate()

    #-------------
    #running block
    #-------------
    chromosomesInGeneration = 25
    crossoverRate = 0.7
    mutationRate = 0.001
    targetNum = 1

    #instantiate first generation
    generation = instantiateGeneration(chromosomesInGeneration,targetNum)
    printGeneration(generation)
    #flag to see if algorithm has made any progress
    finished = False
    while(finished == False):
        #nextGen will be filled with chromosomes selected from init generation
        nextGen = []
        for x in range (0, chromosomesInGeneration):
            someChromosome = rouletteWheelSelection(generation, crossoverRate)
            nextGen.append(someChromosome)
        mutateGeneration(nextGen, mutationRate)
        printGeneration(nextGen)
        break


    #testUpdateFitness(generation, targetNum)




    #check fitness

    #roulette select for breeding
    #etc.

#run everything!
main()
