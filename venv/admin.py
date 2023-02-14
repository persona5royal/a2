# Edward Lee
# edwarhl4@uci.edu
# 61666868

import pathlib
import shlex
import sys
import Profile
def inputSplitter(myInput):
    firstLetter = myInput[0]
    if firstLetter == "Q":
        sys.exit()
    elif firstLetter == "L":
        if myInput.find("-") == -1:
            # if the input has no dash, ergo, no commands after the path
            filePath = pathlib.Path(myInput[2:])
            remainingChars = ""
        else:
            filePath = pathlib.Path(myInput[2:myInput.find("-") - 1])
            remainingChars = myInput[myInput.find("-"):]
    elif firstLetter in "DRO":
        filePath = pathlib.Path(myInput[2:])
        remainingChars = ""
    elif firstLetter in "C":
        filePath = pathlib.Path(myInput[2:myInput.find("-")-1])
        remainingChars = myInput[myInput.find("-"):]
    elif firstLetter in "PE":
        filePath = ""
        remainingChars = myInput[2:]
    return [firstLetter, filePath, remainingChars]
def run(OFlag, OPath=pathlib.Path(".")):
    userInput = input()
    listOfInputs = inputSplitter(userInput)
    firstLetter = listOfInputs[0]
    filePath = listOfInputs[1]
    remainingChars = listOfInputs[2]
    remainingCharsSplit = remainingChars.split(" ")
    print(listOfInputs)
    # starting with the no remainingChars commands first
    if firstLetter in "DRO":
        if firstLetter == "D":
            # delete the file
            if filePath.is_file():
                if filePath.suffix == ".dsu":
                    filePath.unlink()
                    print(f'{filePath} DELETED')
                else:
                    print("ERROR, file extension not .dsu")
            else:
                print("ERROR, given path does not end in a file")
        elif firstLetter == "R":
            if filePath.is_file():
                if filePath.suffix == ".dsu":
                    if filePath.stat().st_size == 0:
                        print("EMPTY")
                    else:
                        with open(filePath) as tempPath:
                            print(tempPath.read())
                else:
                    print("ERROR, file does not end in .dsu")
            else:
                print("ERROR, selected path is not a file.")
        elif firstLetter == "O":
            OFlag = True
            OPath = filePath
            print("Your file is ready. Use a P or E command.")
    elif firstLetter in "LCEP":
        if firstLetter == "L":
            if not filePath.is_file():
                for element in filePath.iterdir():
                    print(element)
                print("L is not complete yet.")
            else:
                print("Error - you have given a file. This command reads folders")
        elif firstLetter == "C":
            if remainingCharsSplit[0] == "-n":
                fileName = remainingCharsSplit[1] + ".dsu"
                tempPath = filePath / fileName

                username = input("Please enter the username for this journal: ")
                password = input("Please enter the password for this journal: ")
                tempProfile = Profile.Profile(dsuserver=None, username=username, password=password)
                tempPath.touch()
                tempProfile.save_profile(tempPath)
                print(f'Your .dsu file exists here: {tempPath}')

                OFlag = True
                OPath = tempPath
        elif firstLetter == "E":
            if OFlag:
                print(remainingChars)
                EPSPLITCOMMANDS = remainingChars.split("-")
                del EPSPLITCOMMANDS[0]
                for iterator in range(len(EPSPLITCOMMANDS)):
                    EPSPLITCOMMANDS[iterator] = (EPSPLITCOMMANDS[iterator].split(maxsplit=1))
                print(EPSPLITCOMMANDS)
                ourProfile = Profile.Profile()
                ourProfile.load_profile(OPath)
                for miniList in EPSPLITCOMMANDS:
                    for accum in range(len(miniList)):
                        miniList[accum] = miniList[accum].replace('"','')
                for miniList in EPSPLITCOMMANDS:
                    if miniList[0] == "usr":
                        print(miniList[1])
                        ourProfile.username = miniList[1]
                    elif miniList[0] == "pwd":
                        print(miniList[1])
                        ourProfile.password = miniList[1]
                    elif miniList[0] == "bio":
                        print(miniList[1])
                        ourProfile.bio = miniList[1]
                    elif miniList[0] == "addpost":
                        print(miniList[1])
                        ourProfile.add_post(miniList[1])
                    elif miniList[0] == "delpost":
                        print(miniList[1])
                        ourProfile.del_post(miniList[1])
                ourProfile.save_profile(OPath)

            else:
                print("You have not prepared a file using either C or O commands. Try again.")
        elif firstLetter == "P":
            if OFlag:
                print(remainingChars)
            else:
                print("You have not prepared a file using either C or O commands. Try again.")

    else:
        print("ERROR, invalid command")
    if OFlag == True:
        run(True, OPath)
    else:
        run(False)