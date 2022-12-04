import string ##to initialize ascii lowercase and uppercase strings in one go
import os ##to pull windows environment variable - USERPROFILE
TotalRuckSackNumber = 0
RuckSacksChecked = 0
Alphabet = list(string.ascii_letters)

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

        removeMissingChar(line)
        RuckSacksChecked += 1

        #Using ord method to convert letter to number. Lowercase and uppercase numbers start at different numbers so I substract to get them to the numbers befitting the challenge.
        if(RuckSacksChecked == 3):
            letter = Alphabet[0]
            if(letter.isupper()):
                TotalRuckSackNumber += (ord(letter) - 38)
            else:
                TotalRuckSackNumber += (ord(letter) - 96)
            RuckSacksChecked = 0
            Alphabet = list(string.ascii_letters)
    
print(TotalRuckSackNumber)