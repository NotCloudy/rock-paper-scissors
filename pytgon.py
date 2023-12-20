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
                print(f'>>> You Scored: {humanCounter} point(s) <<<')
                print(f'>>> AI Scored: {aiCounter} point(s) <<<')
        elif humanTurn == "s" and aiTurn == "p":
                print(f"AI: {aiTurn}")
                print("You win!")
                humanCounter += 1
                print(f'>>> You Scored: {humanCounter} point(s) <<<')
                print(f'>>> AI Scored: {aiCounter} point(s) <<<')
        elif humanTurn == "p" and aiTurn == "r":
                print(f"AI: {aiTurn}")
                print("You win!")
                humanCounter += 1
                print(f'>>> You Scored: {humanCounter} point(s) <<<')
                print(f'>>> AI Scored: {aiCounter} point(s) <<<')
        elif aiTurn == "r" and humanTurn == "s":
                print(f"AI: {aiTurn}")
                print("You lose!")
                aiCounter += 1
                print(f'>>> You Scored: {humanCounter} point(s) <<<')
                print(f'>>> AI Scored: {aiCounter} point(s) <<<')
        elif aiTurn == "s" and humanTurn == "p":
                print(f"AI: {aiTurn}")
                print("You lose!")
                aiCounter += 1
                print(f'>>> You Scored: {humanCounter} point(s) <<<')
                print(f'>>> AI Scored: {aiCounter} point(s) <<<')
        elif aiTurn == "p" and humanTurn == "r":
                print(f"AI: {aiTurn}")
                print("You lose!")
                aiCounter += 1
                print(f'>>> You Scored: {humanCounter} point(s) <<<')
                print(f'>>> AI Scored: {aiCounter} point(s) <<<')

        if humanCounter == necessary_wins or aiCounter == necessary_wins:
            break
    if humanCounter > aiCounter:  
        print(f'>>> You Win! <<<')
    elif aiCounter > humanCounter: 
        print(f'>>> AI Wins! <<<')
      
    play_again = input('>>> Would You Like To Play Again? y/n ')
    if play_again == ('y'):
        game()
    elif play_again == ('n'):
        print('>>> Thanks For Playing! <<<')
    elif play_again != ('y') or ('n'):
        e = input (' please respond with either y or n ')
    
        if e == ('y'):
            game()
        else:
            print('\n |>>>Thank you for playing!<<<|')
         
    

    
    
    

game()



