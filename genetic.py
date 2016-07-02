import random

'''
function RECEIVES string and RETURNS string
converts a 4 bit string into a decimal or operator string
'''
def bitsToArithmetic(bitString):
    switcher = {
        '0000': '0',
        '0001': '1',
        '0010': '2',
        '0011': '3',
        '0100': '4',
        '0101': '5',
        '0110': '6',
        '0111': '7',
        '1000': '8',
        '1001': '9',
        '1010': '+',
        '1011': '-',
        '1100': '*',
        '1101': '/',
        '1110': 'n/a',
        '1111': 'n/a',
    }
    #either transform a 4 bit string into a value listed in dictionary,
    #or default to convert it into an int!
    return switcher.get(bitString, 'n/a')

'''
function RECEIVES a length 8 array of numeric and operator strings
and RETURNS an array of "real" expression
'''
def toRealExpression(arithmeticArray):
    #if 0, it's looking for a number next
    #if 1, it's looking for an operator next
    found = 0;
    realExpressionArray = []
    #check through arithmeticArray to pick out alternating numbers and operators
    for x in range(0, len(arithmeticArray)):
        if(found == 0 and arithmeticArray[x] >= '0' and arithmeticArray[x] <= '9'):
            found = 1
            realExpressionArray.append(arithmeticArray[x])
        if(found == 1 and
           (arithmeticArray[x] == '+' or
            arithmeticArray[x] == '-' or
            arithmeticArray[x] == '*' or
            arithmeticArray[x] == '/')
          ):
            found = 0
            realExpressionArray.append(arithmeticArray[x])

    #if the last symbol is an operator
    if(found == 0):
        realExpressionArray = ['n/a']

    return realExpressionArray


'''
function RECEIVES an array of Chromosomes
and RETURNS a recombinated Chromosome (for next generation)
'''
def rouletteWheelSelection(generation, crossoverRate):
    #total up generation's fitness
    totalFitness = 0
    for x in range(0, len(generation)):
        totalFitness += generation[x].fitness
    #update probabilities for each Chromosome
    #this sum of probabilities should equal 1
    sum = 0
    probabilitiesArray = []
    for x in range(0, len(generation)):
        generation[x].updateProbability(totalFitness, sum)

        #print("Chromosome["+str(x)+"].probability = " + str(generation[x].probability))
        
        sum += generation[x].probability
        probabilitiesArray.append(sum)

    first = rouletteDartPick(generation, probabilitiesArray)
    second = rouletteDartPick(generation, probabilitiesArray)
    if(random.random() < crossoverRate):
        if(toRealExpression(second.arithmeticArray) == 'n/a'):
            return first
        elif(toRealExpression(second.arithmeticArray) == 'n/a'):
            return second
        else:
            return first.recombinate(second)

'''
function RECEIVES the generation and its respective "pie chart" of probabilities
and RETURNS a single picked Chromosome
'''
def rouletteDartPick(generation, probabilitiesArray):
    #generate a random float between 0 and 1
    #this is like throwing a dart at a pie chart
    rouletteDart = random.random()

    #print rouletteDart
    #print probabilitiesArray

    #iterate through generation and find a Chromosome with
    #generation[x].probability < rand and generation[x+1].probablity > rand
    for x in range(0, len(generation)):
        if(probabilitiesArray[x] < rouletteDart and probabilitiesArray[x+1] > rouletteDart):
            return generation[x]

    return generation[0]
