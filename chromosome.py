from genetic import *
import random

class Chromosome:

    #constructor
    def __init__(self):
        self.chromosomeSize = 8
        self.geneSize = 4
        self.dnArray = []
        self.fitness = 0;
        #geneSize * chromosomeSize because there are geneSize # of bits
        #and chromosomeSize # of genes in a Chromosome
        for x in range(0, self.geneSize * self.chromosomeSize):
            self.dnArray.append(0)
        self.randomizeGenes()
        self.translate()

    #randomize all genes in the dnArray string
    def randomizeGenes(self):
        for x in range(0 , 4*self.chromosomeSize):
            gene = random.randrange(0, 1)
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
