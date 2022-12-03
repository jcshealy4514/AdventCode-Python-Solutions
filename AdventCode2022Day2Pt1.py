totalScore = 0
handScore = 0

with open('C:/Users/jcshe/Downloads/AdventcodeDay2Input.txt') as file:
    for line in file.readlines():

        match line[2]:
            case 'X':
                handScore = 1
            case 'Y':
                handScore = 2
            case 'Z':
                handScore = 3
            case _:
                None

        match line.strip():
            case "A X" | "B Y" | "C Z":
                totalScore += 3
            case "A Y" | "B Z" | "C X":
                totalScore += 6
            case _:
                None

        totalScore += handScore

print(totalScore)