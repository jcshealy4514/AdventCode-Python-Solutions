import os ##to pull windows environment variable - USERPROFILE
import time

with open(os.environ['USERPROFILE'] + '/Downloads/Day6.txt') as file:
    for line in file.readlines():
        charStart = 0
        charEnd = 4

        while charEnd <= len(line):
            charString = line[charStart:charEnd]
            charArray = []

            for char in charString:
                if char not in charArray:
                    charArray.append(char)
            
            if len(charArray) == 4:
                print(charEnd)
                quit()
            
            charStart += 1
            charEnd += 1
            

