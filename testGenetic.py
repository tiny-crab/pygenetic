from genetic import *
from chromosome import Chromosome

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
    first.randomizeGenes()
    print(first.dnArray)
    print(first.arithmeticArray)
    print(toRealExpression(first.arithmeticArray))
