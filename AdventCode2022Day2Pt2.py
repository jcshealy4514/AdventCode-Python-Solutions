totalScore = 0

with open('C:/Users/jcshe/Downloads/AdventcodeDay2Input.txt') as file:
    for line in file.readlines():

        match line.strip():
            #LOSE CASES
            case 'B X':
                PointsWon = 1    
            case 'C X':
                PointsWon = 2
            case 'A X':
                PointsWon = 3 

            #DRAW CASES
            case 'A Y':
                PointsWon = 4
            case 'B Y':
                PointsWon = 5
            case 'C Y':
                PointsWon = 6

            #WIN CASES
            case 'C Z':
                PointsWon = 7
            case 'A Z':
                PointsWon = 8
            case 'B Z':
                PointsWon = 9

            #DEFAULT CASE
            case _:
                None

        totalScore += PointsWon

print(totalScore)