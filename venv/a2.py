# a2.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Edward Lee
# edwarhl4@uci.edu
# 61666868

import pathlib
import shlex

def inputSplitter(myInput):
    firstLetter = myInput[0]
    if firstLetter =


    return inputInList
def run():
    userInput = input()
    regexInput = shlex.split(userInput, posix=False)
    try:
        firstCommand = regexInput[0]
        print(regexInput[1])
        filePath = pathlib.Path(regexInput[1])
    except IndexError as error:
        print(f"error: {error}")

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
    elif firstCommand == "D":
        # delete the file
        if filePath.is_file():
            if filePath.suffix == ".dsu":
                filePath.unlink()
                print(f'{filePath} DELETED')
            else:
                print("ERROR")
        else:
            print("ERROR")
    elif firstCommand == "R":
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
    elif firstCommand == "Q":
        # quit
        return
    else:
        print("ERROR, invalid command")
        # NO QUOTES YOU HAVE NO QUOTES PLEASE PUT QUOTES INTO YOUR INPUT
    run()

if __name__ == "__main__":
    run()