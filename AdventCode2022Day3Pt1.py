import string ##to initialize ascii lowercase and uppercase strings in one go
import os ##to pull windows environment variable - USERPROFILE
TotalRuckSackNumber = 0

#Calling same script to remove missing characters from both compartments
def removeMissingChar(compartment):
    charNum = 0
    while charNum < len(Alphabet):
        if(Alphabet[charNum] not in compartment):
            Alphabet.remove(Alphabet[charNum])
            charNum -= 1
        charNum += 1

with open(os.environ['USERPROFILE'] + '/Downloads/AdventcodeDay3Input.txt') as file:
    for line in file.readlines():
            
        #Initilize Alphabet
        Alphabet = list(string.ascii_letters)

        #To select first and second half of string (len is weird? Both compartments are not same length, this seems like a broken challenge)
        firstCompartment = (len(line) // 2)
        secondCompartment = len(line)

        removeMissingChar(line[0:firstCompartment])
        removeMissingChar(line[firstCompartment:secondCompartment])

        #Using ord method to convert letter to number. Lowercase and uppercase numbers start at different numbers so I substract to get them to the numbers befitting the challenge.
        letter = Alphabet[0]
        if(letter.isupper()):
            TotalRuckSackNumber += (ord(letter) - 38)
        else:
            TotalRuckSackNumber += (ord(letter) - 96)

    
print(TotalRuckSackNumber)
