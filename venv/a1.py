import pathlib
import shlex

def run():
    userInput = input()
    regexInput = shlex.split(userInput)
    try:
        firstCommand = regexInput[0]
        filePath = pathlib.Path(regexInput[1])
    except IndexError:
        print("Error")

    if firstCommand =="L":
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
                print("ERROR")
        else:
            print("ERROR")
    elif firstCommand == "Q":
        # quit
        return
    else:
        print("ERROR")
        # NO QUOTES YOU HAVE NO QUOTES PLEASE PUT QUOTES INTO YOUR INPUT
    run()

if __name__ == "__main__":
    run()