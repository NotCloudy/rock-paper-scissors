import random
from random import randint
board = []
board2 = []

for x in range(6):
    board.append(["[]"] * 6)
    board2.append(["[]"] * 6)
def print_board(board):
    for row in board:
        print((" ").join(row))
print("Let's play Battleship!")
print_board(board)

def random_row(board):
   return randint(0, len(board) - 1)
def random_col(board):
   return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print([ship_row] + [ship_col])
for turn in range(9):
   print ("Your Turn"), turn
   guess_row = int(input("Guess Row:"))
   guess_col = int(
        input("Guess Col:"))
   if guess_row == ship_row and guess_col == ship_col:
      print('Congratulations, you sunk my battle ship!')
      board2[ship_row][ship_col] = "X"
      print_board(board2)
      break
   else:
      if (guess_row < 0 or guess_row > 5) or (guess_col < 0 or guess_col > 5):
            print("Oops, that's not even in the ocean.")
            if turn == 8:
               print('\n Game Over!')
turn =+ 1




