import random

print("hello world")
rock = "r"
paper = "p"
scissors = "s"
options = ["r","p","s"]

aiTurn = random.choice(options)
humanTurn = input("-rock papers scissors-")


def winConditions():
    if humanTurn == "r" and aiTurn == "s":
        print("You win!")
    elif humanTurn == "s" and aiTurn == "p":
        print("You win!")
    elif humanTurn == "p" and aiTurn == "r":
        print("You win!")

    elif aiTurn == "r" and humanTurn == "s":
        print("You lose!")
    elif aiTurn == "s" and humanTurn == "p":
        print("You lose!")
    elif aiTurn == "p" and humanTurn == "r":
        print("You lose!")
