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
    elif firstLetter in "CE":
        filePath = pathlib.Path(myInput[2:myInput.find("-")-1])
        remainingChars = myInput[myInput.find("-"):]
    return [firstLetter, filePath, remainingChars]
def run():
    userInput = input()
    listOfInputs = inputSplitter(userInput)
    firstLetter = listOfInputs[0]
    filePath = listOfInputs[1]
    remainingChars = listOfInputs[2]
    remainingCharsSplit = remainingChars.split(" ")
    print(listOfInputs)
    OFlag = False
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
    elif firstLetter in "LCE":
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
                tempPath.touch()
                print(f'Your .dsu file exists here: {tempPath}')
                username = input("Please enter the username for this journal: ")
                password = input("Please enter the password for this journal: ")
                biography = input("Please enter the biography for this journal: ")
                tempProfile = Profile.Profile(username, password, biography)
                tempProfile.save_profile(tempPath)
                OFlag = True
        elif firstLetter == "E":
            if OFlag:
                pass
            else:
                print("You have not prepared a file using either C or O commands. Try again.")

    else:
        print("ERROR, invalid command")
    run()