from chromosome import Chromosome
'''
function RECEIVES an array of Chromosomes
and RETURNS a recombinated Chromosome (for next generation)
'''
def rouletteWheelSelection(generation):
    #total up generation's fitness
    totalFitness = 0
    for x in range(0, len(generation)):
        totalFitness += generation[x].fitness
    #update probabilities for each Chromosome
    sum = 0
    for x in range(0, len(generation)):
        generation[x].updateProbability(totalFitness, sum)
        sum += generation[x].probability

    print totalFitness
    print sum
    #generate a random float between 0 and 1
    #iterate through generation and find a Chromosome with
    #generation[x].probability < rand and generation[x+1].probablity > rand
