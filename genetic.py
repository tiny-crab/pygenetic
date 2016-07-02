#construct an array of random chromosomes
#construct an array for generations

#receive target number
#fill chromArray with random bitstrings
      #since mutations and recombination are necessary, we need to do this in binary bits

#translate function for bit strings -> arithmetic
#return a sequence, write another function to interpret sequence into a final number

'''
function RECEIVES string and RETURNS string
converts a 4 bit string into a decimal or operator string
'''
def bitsToArithmetic(bitString):
    switcher = {
        '1010': '+',
        '1011': '-',
        '1100': '*',
        '1101': '/',
        '1110': 'n/a',
        '1111': 'n/a',
    }
    #either transform a 4 bit string into a value listed in dictionary,
    #or default to convert it into an int!
    return switcher.get(bitString, str(int(bitString,2)))

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
