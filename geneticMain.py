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
    generation = instantiateGeneration(chromosomesInGeneration)
    testRouletteSelection(5, 20, crossoverRate)

    #flag to see if algorithm has made any progress
    finished = False
    while(finished == False):
        finished = True

    #testUpdateFitness(generation, targetNum)




    #check fitness

    #roulette select for breeding
    #etc.

#run everything!
main()
