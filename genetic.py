#8 byte chromosomes

class chromosome:

    private generate():
        
    
    
    
#construct an array of random chromosomes
#construct an array for generations

#receive target number
#fill chromArray with random bitstrings
      #since mutations and recombination are necessary, we need to do this in binary bits

#translate function for bit strings -> arithmetic
#return a sequence, write another function to interpret sequence into a final number

def translate(bitStringArray):
    for x in range(0, len(bitStringArray)):
        print(x)

    #return arithmeticArray

#number should be defined as a string
def numbersToArithmetic(number):
    switcher = {
        '1010': '+',
        '1011': '-',
        '1100': '*',
        '1101': '/',
        '1110': 'n/a',
        '1111': 'n/a',
    }
    #either transform a 4 bit string into a value listed in dictionary,
    #or default to reading it as binary!
    return switcher.get(number, int(number))


