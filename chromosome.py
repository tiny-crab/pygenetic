import random

class Chromosome:

    #constructor
    def __init__(self):
        self.chromosomeSize = 8
        self.geneSize = 4
        self.dnArray = []
        self.fitness = 0
        self.probability = 0
        #geneSize * chromosomeSize because there are geneSize # of bits
        #and chromosomeSize # of genes in a Chromosome
        for x in range(0, self.geneSize * self.chromosomeSize):
            self.dnArray.append(0)
        self.randomizeGenes()
        self.translate()

    #randomize all genes in the dnArray string
    def randomizeGenes(self):
        for x in range(0 , self.geneSize * self.chromosomeSize):
            gene = random.randrange(0, 2)
            self.dnArray[x] = gene

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
    function RECEIVES a chromosome
    and RETURNS a chromosome with updated arithmeticArray
    '''
    def translate(self):
        self.arithmeticArray = []
        bitString = ""
        for x in range(0, self.chromosomeSize):
            #x counts genes
            for y in range(0, self.geneSize):
                #y counts bits in a gene
                bitString += str(self.dnArray[x+y])

            #after finished with a single gene, translate with bitsToArithmetic
            #and transfer to the arithmeticArray
            self.arithmeticArray.append(bitsToArithmetic(bitString))
            #reset bitString so we don't get huge strings of bits :)
            bitString = ""

    def computeSum(self):
        realExpressionArray = toRealExpression(self.arithmeticArray)
        if(realExpressionArray[0] == 'n/a'):
            return -1
        sum = float(realExpressionArray[0])
        counter = 1
        while(counter < len(realExpressionArray)):
            if(realExpressionArray[counter] == '+'):
                sum += float(realExpressionArray[counter+1])
            if(realExpressionArray[counter] == '-'):
                sum -= float(realExpressionArray[counter+1])
            if(realExpressionArray[counter] == '*'):
                sum *= float(realExpressionArray[counter+1])
            if(realExpressionArray[counter] == '/'):
                sum /= float(realExpressionArray[counter+1])
            counter += 2

        return sum

    def updateFitness(self, targetNum):
        #if the denominator isn't 0...
        if( abs(targetNum - self.computeSum()) != 0 ):
            self.fitness = 1 / abs(targetNum - self.computeSum())
        else:
            self.fitness = 0

    def recombinate(self, otherChromosome):
        bitPick = random.randrange(0, self.geneSize*self.chromosomeSize)
        print(bitPick)
        for x in range(bitPick, self.geneSize*self.chromosomeSize):
            #swap everything past the bitPick point
            temp = self.dnArray[x]
            self.dnArray[x] = otherChromosome.dnArray[x]
            otherChromosome.dnArray[x] = temp

    def mutate(self, mutationRate):
        for x in range(0, self.geneSize * self.chromosomeSize):
            gamble = random.randrange(0, 1/mutationRate)
            if(gamble == 1):
                self.dnArray[x] = not self.dnArray[x]

    #this probability ONLY is calculated in the context of a generation
    #the sumSoFar provides boundaries for the pick (essentially defining pie chart)
    #This will probably cause issues with [n/a] strings... how to fix?
    def updateProbability(self, totalFitness, sumSoFar):
        self.probability = fitness/totalFitness + sumSoFar

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
