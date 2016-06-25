from genetic import *

def testNumbersToArithmetic():
    for x in range(0,16):
        print(numbersToArithmetic("{0:b}".format(x)))

