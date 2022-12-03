import time #testing for loop

totalCalories = 0
highestCalories = 0

with open('C:/Users/jcshe/Downloads/AdventcodeDay1Input.txt') as file:
    for line in file.readlines():

        if(line.isspace()):
            #print('this line is whitespace')
            if(totalCalories > highestCalories):
                highestCalories = totalCalories
                #print('highest Calories is now' + str(highestCalories))
            totalCalories = 0
        else:
            #print(line)
            totalCalories += int(line)
            #print('totalCalories is now equal to ' + str(totalCalories))

        #time.sleep(.25)


print(highestCalories)
