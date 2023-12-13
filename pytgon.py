# import random



# def reset():
    
    
#     global humanCounter
#     global aiCounter
#     humanCounter = 0

#     aiCounter = 0
#     if (humanCounter == 3):
#         game()

#     elif (aiCounter == 3):
#         game()
        
         
      

# def winConditions(humanTurn, aiTurn):
#         global humanCounter
#         global aiCounter
#         humanCounter = 0

#         aiCounter = 0
        
#         if humanTurn == "r" and aiTurn == "s":
#             print(f"AI: {aiTurn}")
#             print("You win!")
#             print(humanCounter)
#             humanCounter += 1
#         elif humanTurn == "s" and aiTurn == "p":
#             print(f"AI: {aiTurn}")
#             print("You win!")
#             humanCounter += 1
#         elif humanTurn == "p" and aiTurn == "r":
#             print(f"AI: {aiTurn}")
#             print("You win!")
#             humanCounter += 1
#         elif aiTurn == "r" and humanTurn == "s":
#             print(f"AI: {aiTurn}")
#             print("You lose!")
#             aiCounter += 1
#         elif aiTurn == "s" and humanTurn == "p":
#             print(f"AI: {aiTurn}")
#             print("You lose!")
#             aiCounter += 1
#         elif aiTurn == "p" and humanTurn == "r":
#             print(f"AI: {aiTurn}")
#             print("You lose!")
#             aiCounter += 1

# def tieConditions(humanTurn, aiTurn):
#         if humanTurn == "r" and aiTurn == "r":
#             print(f"AI: {aiTurn}")
#             print("Tie!")
#         elif humanTurn == "p" and aiTurn == "p":
#             print(f"AI: {aiTurn}")
#             print("Tie!")
#         elif humanTurn == "s" and aiTurn == "s":
#             print(f"AI: {aiTurn}")
#             print("Tie!")

# def game():
#     global humanCounter
#     global aiCounter
#     humanCounter = 0

#     aiCounter = 0
    
#     options = ["r","p","s"]
#     aiTurn = random.choice(options)
#     humanTurn = input("- rock papers scissors - ")
    
#     print(f"Human: {humanTurn}")

#     winConditions(humanTurn, aiTurn)
#     tieConditions(humanTurn, aiTurn)




    
# import random
# def game():
#     rock = "r"
#     paper = "p"
#     scissors = "s"
#     options = ["r","p","s"]
#     global humanCounter
#     global aiCounter
#     humanCounter = 0
#     aiCounter = 0
#     aiTurn = random.choice(options)
#     humanTurn = input("-rock papers scissors-")
#     def winConditions(humanCounter, aiCounter):
#         if humanTurn == "r" and aiTurn == "s":
#             print(aiTurn)
#             print("You win!")
#             humanCounter = humanCounter + 1
#         elif humanTurn == "s" and aiTurn == "p":
#             print(aiTurn)
#             print("You win!")
#             humanCounter = humanCounter + 1
#         elif humanTurn == "p" and aiTurn == "r":
#             print(aiTurn)
#             print("You win!")
#             humanCounter = humanCounter + 1
#         elif aiTurn == "r" and humanTurn == "s":
#             print(aiTurn)
#             print("You lose!")
#             aiCounter = aiCounter + 1
#         elif aiTurn == "s" and humanTurn == "p":
#             print(aiTurn)
#             print("You lose!")
#             aiCounter = aiCounter + 1
#         elif aiTurn == "p" and humanTurn == "r":
#             print(aiTurn)
#             print("You lose!")
#             aiCounter = aiCounter + 1
#     winConditions(humanCounter, aiCounter)
#     def tieConditions():
#         if humanTurn == "r" and aiTurn == "r":
#             print(aiTurn)
#             print("Tie!")
#         elif humanTurn == "p" and aiTurn == "p":
#             print(aiTurn)
#             print("Tie!")
#         elif humanTurn == "s" and aiTurn == "s":
#             print(aiTurn)
#             print("Tie!")
#     tieConditions()
  

# humanCounter = 0
# aiCounter = 0


# while True:
#     if humanCounter <= 4:
#         game() 
        
#     elif aiCounter <= 4:
#         game()
import random 
def game():
    options = ['r','p','s']
    while True:
        try:

            turns = int(input("best out of (3 or 5):"))
            if turns == 3 or turns == 5:
                break
            continue
        except ValueError:
            print("Invalid Choice.")
    necessary_wins = int(turns/2) + 1

    humanCounter = 0
    aiCounter = 0
    while True:
        while True:
            humanTurn = input(">>> rock, paper, scissors:")
            if humanTurn in options:
                break
        aiTurn = random.choice(options)
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

        if humanCounter == necessary_wins or aiCounter == necessary_wins:
            break
    if humanCounter > aiCounter:  
        print(f'>>> You Win! <<<')
    elif aiCounter > humanCounter: 
        print(f'>>> AI Wins! <<<')


    print(f'>>> You Scored: {humanCounter} point(s) <<<')
    print(f'>>> AI Scored: {aiCounter} point(s) <<<')

play_again = input('>>> Would You Like To Play Again? y/n ')
if play_again == ('y'):
    game()
elif play_again == ('n'):
    print('>>> Thanks For Playing! <<<')



