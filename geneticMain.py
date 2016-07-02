from genetic import *
from testGenetic import *

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
    mutationRate = 0.01
    targetNum = 1

    generation = []
    for x in range(0, chromosomesInGeneration):
        generation.append(Chromosome())

    #testUpdateFitness(generation, targetNum)


    #check fitness

    #roulette select for breeding
    #etc.

#run everything!
main()
