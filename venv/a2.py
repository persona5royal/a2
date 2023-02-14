# a2.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python
# Edward Lee
# edwarhl4@uci.edu
# 61666868

import ui
import admin

def run():
    adminOrUI = input("Welcome to Pynote. To use the ui mode, type ui and press enter. To use "
                      "the admin mode, type admin and press enter. \n")
    if adminOrUI == "admin":
        admin.run(False)
    elif adminOrUI == "ui":
        ui.run(False)
    else:
        print("nice job. you either mispelled one of the words above or intentionally are not answering the question."
              " try again.")
        run()

if __name__ == "__main__":
    run()