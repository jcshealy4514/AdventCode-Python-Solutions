totalCaloriesForAllElfs = []
totalCalories = 0
finalCount = 0

with open('C:/Users/jcshe/Downloads/AdventcodeDay1Input.txt') as file:
    for line in file.readlines():

        if(line.isspace()):
            totalCaloriesForAllElfs.append(int(totalCalories))
            totalCalories = 0
        else:
            totalCalories += int(line)


totalCaloriesForAllElfs.sort(reverse=True)

for calorieCount in totalCaloriesForAllElfs[0:3]:
    finalCount += calorieCount

print(finalCount)
