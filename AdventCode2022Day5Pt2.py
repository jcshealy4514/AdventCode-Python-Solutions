import os ##to pull windows environment variable - USERPROFILE
import time


#This entire definition will remain here as a tribute to the sheer magnitude of dumbassery one can achieve in the pursuit of.. anything really.
def initalizeTable(file):

    #Initalize Table & Variables
    rows, cols = (9, 8)
    crateArray = [[0 for i in range(cols)] for j in range(rows)]
    lineNum = int(0)
    charNum = int(1)
    colNum = int(0)

    #Open file, check every 4th character (actual letters)
    with open(os.environ['USERPROFILE'] + '/Downloads/Day5Table.txt') as tableFile:
        for line in tableFile.readlines():
            while charNum < len(line):
                if not (line[charNum].isspace()): #if not space then add the character to 2D array
                    crateArray[colNum][lineNum] = line[charNum]
                    charNum += 4
                else:
                    charNum += 4
                colNum += 1

            #Reset variables to stay inside array indexes and move to next line in 2D array
            colNum = int(0)
            lineNum += 1
            charNum = 1
        return crateArray

def smarterArray():
    #Initialize variables
    arr = [""   ] * 9
    charNum = int(1)
    colNum = int(0)

    with open(os.environ['USERPROFILE'] + '/Downloads/Day5Table.txt') as tableFile:
        for line in tableFile.readlines():

            while charNum < len(line):

                if not (line[charNum].isspace()):
                    arr[colNum] = arr[colNum] + (line[charNum])
                    charNum += 4
                else:
                    charNum += 4
                colNum += 1

            #Reset variables to stay inside array indexes and move to next line in array
            colNum = int(0)
            charNum = 1
        return arr



with open(os.environ['USERPROFILE'] + '/Downloads/Day5.txt') as file:
    crateArray = smarterArray()
    #print(crateArray)
    for line in file.readlines():

        #gather instructions
        moveAmount = int((line[5] + line[6]).strip())
        fromCol = int((line[12] + line[13]).strip()) - 1
        toCol = int((line[17] + line[18]).strip()) - 1 #whitespace added to end of file otherwise error on index 18

        #perform instructions one at a time(KEYWORD: one at a time)
        toMove = crateArray[fromCol][:moveAmount]
        crateArray[fromCol] = crateArray[fromCol][moveAmount:]
        crateArray[toCol] = toMove + crateArray[toCol]

    #When all is performed, report results
    print(crateArray)
    for col in crateArray:
        print(col[0])


