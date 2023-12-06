import random



# def reset():
#     global humanCounter
#     global aiCounter
#     if (humanCounter == 3):
#         game()

#     elif (aiCounter == 3):
#         game()
        
         
      

def winConditions(humanTurn, aiTurn):
        global humanCounter
        global aiCounter
        
        if humanTurn == "r" and aiTurn == "s":
            print(f"AI: {aiTurn}")
            print("You win!")
            print(humanCounter)
            humanCounter += 1
        elif humanTurn == "s" and aiTurn == "p":
            print(f"AI: {aiTurn}")
            print("You win!")
            humanCounter += 1
        elif humanTurn == "p" and aiTurn == "r":
            print(f"AI: {aiTurn}")
            print("You win!")
            humanCounter += 1
        elif aiTurn == "r" and humanTurn == "s":
            print(f"AI: {aiTurn}")
            print("You lose!")
            aiCounter += 1
        elif aiTurn == "s" and humanTurn == "p":
            print(f"AI: {aiTurn}")
            print("You lose!")
            aiCounter += 1
        elif aiTurn == "p" and humanTurn == "r":
            print(f"AI: {aiTurn}")
            print("You lose!")
            aiCounter += 1

def tieConditions(humanTurn, aiTurn):
        if humanTurn == "r" and aiTurn == "r":
            print(f"AI: {aiTurn}")
            print("Tie!")
        elif humanTurn == "p" and aiTurn == "p":
            print(f"AI: {aiTurn}")
            print("Tie!")
        elif humanTurn == "s" and aiTurn == "s":
            print(f"AI: {aiTurn}")
            print("Tie!")

def game():
    global humanCounter
    global aiCounter
    humanCounter = 0
    aiCounter = 0
    options = ["r","p","s"]
    aiTurn = random.choice(options)
    humanTurn = input("- rock papers scissors - ")
    
    print(f"Human: {humanTurn}")

    winConditions(humanTurn, aiTurn)
    tieConditions(humanTurn, aiTurn)
    


# def win(humanCounter, aiCounter):
#         if humanCounter > aiCounter:
#             print("you win!!!!11!!!!!!!1")
#         elif humanCounter < aiCounter:
#             print("you lose !!!!!11!!!!!!1")
#         win(humanCounter, aiCounter)
        
# game()
# game()
# print(f"\nNext round! H: {humanCounter} AI: {aiCounter}\n")
# game()
# print(f"\nNext round! H: {humanCounter} AI: {aiCounter}\n")
# game()

while(humanCounter <= 4 or aiCounter <= 4):
    if(humanCounter < 3 or aiCounter < 3):
        
        print(f"\nNext round! H: {humanCounter} AI: {aiCounter}\n")

    if(humanCounter == 3 or aiCounter == 4):
        if(humanCounter == 3):
            print(f"Human Wins | Human Score: {humanCounter} : AI Score: {aiCounter}")

        elif(aiCounter == 3):
            print(f"AI Wins | Human Score: {humanCounter} : AI Score: {aiCounter}")

    
 

    



