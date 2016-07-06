import random
from genetic import *

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
        if( abs(targetNum - self.computeSum()) == 0 ):
            #throw a flag here! Found a solution
            self.fitness = 0
        else:
            self.fitness = 1 / abs(targetNum - self.computeSum())

    def recombinate(self, otherChromosome):
        bitPick = random.randrange(0, self.geneSize*self.chromosomeSize)
        for x in range(bitPick, self.geneSize*self.chromosomeSize):
            #swap everything past the bitPick point
            temp = self.dnArray[x]
            self.dnArray[x] = otherChromosome.dnArray[x]
            otherChromosome.dnArray[x] = temp
        self.translate()
        otherChromosome.translate()

    def mutate(self, mutationRate):
        for x in range(0, self.geneSize * self.chromosomeSize):
            gamble = random.random()
            if(gamble < mutationRate):
                self.dnArray[x] = not self.dnArray[x]

    #this probability ONLY is calculated in the context of a generation
    #the sumSoFar provides boundaries for the pick (essentially defining pie chart)
    #This will probably cause issues with [n/a] strings... how to fix?
    def updateProbability(self, totalFitness, sumSoFar):
        if(toRealExpression(self.arithmeticArray) == 'n/a'):
            self.probability = 0
            return
        self.probability = self.fitness/totalFitness
