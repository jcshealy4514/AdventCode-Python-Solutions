import os ##to pull windows environment variable - USERPROFILE
dict = {}
currentDirectory = ""
#Don't ask me how to format this script better, because I don't know.
#to be honest, I'm genuinely surprised this works
#this is one of them, idk how- but if you remove this scripts, it breaks everything in prod.

def updateOuterDict():
    global currentDirectory
    global dict

    returnDirectory = currentDirectory
    while not currentDirectory == '//':

        changeDirDown()
        currentSize = dict.get(currentDirectory)
        if not currentSize == None:
            dict[currentDirectory] = {int(currentSize.pop()) + int(fileData[0])}
        else:
            dict[currentDirectory] = {int(fileData[0])}
    currentDirectory = returnDirectory


def changeDirDown():
    global currentDirectory
    currentDirectory = currentDirectory.rsplit('/', 1)[0]


with open(os.environ['USERPROFILE'] + '/Downloads/Day7.txt') as file:
    for line in file.readlines():
        match line[0]:

            case '$':
                if line[2] + line[3] == 'cd':
                    if not line[5] + line[6] == '..':
                        currentDirectory = currentDirectory + "/" + line[4:].strip() #CD UP
                    else:
                        currentDirectory = currentDirectory.rsplit('/', 1)[0] #CD DOWN
                else:
                    None

            case 'd':
                None #dir command - do nothing

            case _: #This is what we run when we look at a file
                fileData = line.strip().split(" ")
                if currentDirectory in dict:
                    currentSize = dict.get(currentDirectory)
                    dict[currentDirectory] = {int(currentSize.pop()) + int(fileData[0])}
                    updateOuterDict()
                else:
                    dict[currentDirectory] = {fileData[0]} #do I really need any other keys?
                    updateOuterDict()

    #ONLY THING CHANGED FOR PT2
    dirSpaces = []
    print(int(dict['//'].pop()) - 40000000)
    for key in sorted(dict.keys(),reverse=True):
        if dict[key] and not dict[key] == None:
            dirSpaces.append(int(dict[key].pop()))
    print(sorted(dirSpaces, reverse=True))   

    #I'ma be honest, I just looked at the printed out list and found the first sorted number above 1072511 
    #1072511 was found on line 56