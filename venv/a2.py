# a2.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

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
    elif firstLetter in "DRO":
        filePath = pathlib.Path(myInput[2:])
        remainingChars = ""
    elif firstLetter in "LCE":
        filePath = pathlib.Path(myInput[2:myInput.find("-")-1])
        remainingChars = myInput[myInput.find("-"):]
    return [firstLetter, filePath, remainingChars]

def run():
    userInput = input("enter le command rofl: ")
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
            print("O was selected. no code is available for O yet.")
    elif firstLetter in "LCE":
        if firstLetter == "L":
            for element in filePath.iterdir():
                print(element)
            print("L is not complete yet.")
        elif firstLetter == "C":
            if remainingCharsSplit[0] == "-n":
                fileName = remainingCharsSplit[1] + ".dsu"
                tempPath = filePath / fileName
                tempPath.touch()
                print(f'Your .dsu file exists here: {tempPath}')
                username = input("Please enter the username for this journal: ")
                password = input("Please enter the password for this journal: ")
                biography = input("Please enter the biography for this journal: ")
                tempProfile = Profile(username, password, biography)
                tempProfile.save_profile(tempPath)
        elif firstLetter == "E":
            print("E was selected. no code is available for E yet.")


    run()
"""
    if firstCommand == "L":
        for element in filePath.iterdir():
            print(element)
        print("L")
    elif firstCommand == "C":
        try:
            shouldBeN = regexInput[2]
            fileName = regexInput[3]
        except IndexError:
            print("Error")
        if shouldBeN == "-n":
            fileName = fileName + ".dsu"
            tempPath = filePath / fileName
            tempPath.touch()
            print(tempPath)
    elif firstCommand == "Q":
        # quit
        return
    else:
        print("ERROR, invalid command")
        # NO QUOTES YOU HAVE NO QUOTES PLEASE PUT QUOTES INTO YOUR INPUT
        """


if __name__ == "__main__":
    run()