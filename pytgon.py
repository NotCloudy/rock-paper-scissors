import random
def game():
    rock = "r"
    paper = "p"
    scissors = "s"
    options = ["r","p","s"]
    humanCounter = 0
    aiCounter = 0
    aiTurn = random.choice(options)
    humanTurn = input("-rock papers scissors-")


    def winConditions(humanCounter, aiCounter):
        if humanTurn == "r" and aiTurn == "s":
            print(aiTurn)
            print("You win!")
            humanCounter = humanCounter + 1
        elif humanTurn == "s" and aiTurn == "p":
            print(aiTurn)
            print("You win!")
            humanCounter = humanCounter + 1
        elif humanTurn == "p" and aiTurn == "r":
            print(aiTurn)
            print("You win!")
            humanCounter = humanCounter + 1
        elif aiTurn == "r" and humanTurn == "s":
            print(aiTurn)
            print("You lose!")
            aiCounter = aiCounter + 1
        elif aiTurn == "s" and humanTurn == "p":
            print(aiTurn)
            print("You lose!")
            aiCounter = aiCounter + 1
        elif aiTurn == "p" and humanTurn == "r":
            print(aiTurn)
            print("You lose!")
            aiCounter = aiCounter + 1
    winConditions(humanCounter, aiCounter)
    def tieConditions():
        if humanTurn == "r" and aiTurn == "r":
            print(aiTurn)
            print("Tie!")
        elif humanTurn == "p" and aiTurn == "p":
            print(aiTurn)
            print("Tie!")
        elif humanTurn == "s" and aiTurn == "s":
            print(aiTurn)
            print("Tie!")
    tieConditions()

game()

print(' Next round! ')
game()
print(' Next round! ')
game()
print(' Next round! ')
game()

def win(humanCounter, aiCounter):
    if humanCounter > aiCounter:
        print("you win!!!!11!!!!!!!1")
    elif humanCounter < aiCounter:
        print("you lose !!!!!11!!!!!!1")
win()




