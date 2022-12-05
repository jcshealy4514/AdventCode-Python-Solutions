import os ##to pull windows environment variable - USERPROFILE
overlaps = 0


def checkContains(range1, range2):

    firstRangeNums = range1.strip().split("-")
    secondRangeNums = range2.strip().split("-")

    #I check if the first range surrounds either endpoint of the second range separately
    if(
        int(firstRangeNums[0]) <= int(secondRangeNums[0]) and
        int(firstRangeNums[1]) >= int(secondRangeNums[0])
        or
        int(firstRangeNums[0]) <= int(secondRangeNums[1]) and
        int(firstRangeNums[1]) >= int(secondRangeNums[1])
        ):

        global overlaps
        overlaps += 1


with open(os.environ['USERPROFILE'] + '/Downloads/Day4.txt') as file:
    for line in file.readlines():

        currentOverlap = overlaps
        firstRange = line.split(",")[0]
        secondRange = line.split(",")[1]

        checkContains(firstRange,secondRange)
        if(currentOverlap == overlaps): #checking overlap count in case we have two ranges with exact same numbers (prevents incrementing overlaps variable twice)
            checkContains(secondRange,firstRange)

print(str(overlaps))