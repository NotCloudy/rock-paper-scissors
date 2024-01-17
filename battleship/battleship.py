import random

def grid():
   row = [['|_|', '|_|', '|_|', '|_|', '|_|'],
           ['|_|', '|_|', '|_|', '|_|', '|_|'],
           ['|_|', '|_|', '|_|', '|_|', '|_|'],
           ['|_|', '|_|', '|_|', '|_|', '|_|'],
           ['|_|', '|_|', '|_|', '|_|', '|_|']]   
   
   print(row)
   for i in row:
      print(*i)

grid()
shipLocation1 = random.randrange(0,4)
shipLocation2 = random.randrange(0,4)
shipLocation3 = random.randrange(0,4)
shipLocation4 = random.randrange(0,4)
shipLocation5 = random.randrange(0,4)
def game():
   playerGuess = input(' \n Where would you like to shoot? (row,column)  ')
   def rows():
      def row1(): 
         if shipLocation1 == (0) and playerGuess == (0,0):
            print('|X| |_| |_| |_| |_|' + 'Congrats! you sunk one of their ships! ')
         if shipLocation1 == (1) and playerGuess == (0,1):
            print('|_| |X| |_| |_| |_|' + 'Congrats! you sunk one of their ships! ')
         if shipLocation1 == (2) and playerGuess == (0,2):
            print('|_| |_| |X| |_| |_|' + 'Congrats! you sunk one of their ships! ')
         if shipLocation1 == (3) and playerGuess == (0,3):
            print('|_| |_| |_| |X| |_|' + 'Congrats! you sunk one of their ships! ')
         if shipLocation1 == (4) and playerGuess == (0,4):
            print('|_| |_| |_| |_| |X|' + 'Congrats! you sunk one of their ships! ')
         row1()
      def row2():
         if shipLocation2 == (0) and playerGuess == (1,0):
            print('|X| |_| |_| |_| |_|' + 'Congrats! you sunk one of their ships! ')
         if shipLocation2 == (1) and playerGuess == (1,1):
            print('|_| |X| |_| |_| |_|' + 'Congrats! you sunk one of their ships! ')
         if shipLocation2 == (2) and playerGuess == (1,2):
            print('|_| |_| |X| |_| |_|' + 'Congrats! you sunk one of their ships! ')
         if shipLocation2 == (3) and playerGuess == (1,3):
            print('|_| |_| |_| |X| |_|' + 'Congrats! you sunk one of their ships! ')
         if shipLocation2 == (4) and playerGuess == (1,4):
            print('|_| |_| |_| |_| |X|' + 'Congrats! you sunk one of their ships! ')
         row2()
      def row3():
         if shipLocation3 == (0) and playerGuess == '2,0':
            print('|X| |_| |_| |_| |_|' + 'Congrats! you sunk one of their ships! ')
         if shipLocation3 == (1) and playerGuess == '2,1':
            print('|_| |X| |_| |_| |_|' + 'Congrats! you sunk one of their ships! ')
         if shipLocation3 == (2) and playerGuess == '2,2':
            print('|_| |_| |X| |_| |_|' + 'Congrats! you sunk one of their ships! ')
         if shipLocation3 == (3) and playerGuess == '2,3':
            print('|_| |_| |_| |X| |_|' + 'Congrats! you sunk one of their ships! ')
         if shipLocation3 == (4) and playerGuess == '2,4':
            print('|_| |_| |_| |_| |X|' + 'Congrats! you sunk one of their ships! ')
         row3()
      def row4():
         if shipLocation4 == (0) and playerGuess == '3,0':
            print('|X| |_| |_| |_| |_|' + 'Congrats! you sunk one of their ships! ')
         if shipLocation4 == (1) and playerGuess == '3,1':
            print('|_| |X| |_| |_| |_|' + 'Congrats! you sunk one of their ships! ')
         if shipLocation4 == (2) and playerGuess == '3,2':
            print('|_| |_| |X| |_| |_|' + 'Congrats! you sunk one of their ships! ')
         if shipLocation4 == (3) and playerGuess == '3,3':
            print('|_| |_| |_| |X| |_|' + 'Congrats! you sunk one of their ships! ')
         if shipLocation4 == (4) and playerGuess == '3,4':
            print('|_| |_| |_| |_| |X|' + 'Congrats! you sunk one of their ships! ')
         row4()
      def row5():
         if shipLocation5 == (0) and playerGuess == '4,0':
            print('|X| |_| |_| |_| |_|' + 'Congrats! you sunk one of their ships! ')
         if shipLocation5 == (1) and playerGuess == '4,1':
            print('|_| |X| |_| |_| |_|' + 'Congrats! you sunk one of their ships! ')
         if shipLocation5 == (2) and playerGuess == '4,2':
            print('|_| |_| |X| |_| |_|' + 'Congrats! you sunk one of their ships! ')
         if shipLocation5 == (3) and playerGuess == '4,3':
            print('|_| |_| |_| |X| |_|' + 'Congrats! you sunk one of their ships! ')
         if shipLocation5 == (4) and playerGuess == '4,4':
            print('|_| |_| |_| |_| |X|' + 'Congrats! you sunk one of their ships! ')
         row5()
      rows()
      def miss():
         def row1_miss():
            if shipLocation1 == (0) and playerGuess == (0,1):
               print('|_| |0| |_| |_| |_|' + 'You missed their battleship! ')
            if shipLocation1 == (0) and playerGuess == (0,2):
               print('|_| |_| |0| |_| |_|' + 'You missed their battleship! ')
            if shipLocation1 == (0) and playerGuess == (0,3):
               print('|_| |_| |_| |0| |_|' + 'You missed their battleship! ')
            if shipLocation1 == (0) and playerGuess == (0,4):
               print('|_| |_| |_| |_| |0|' + 'You missed their battleship! ')
            row1_miss()
         def row2_miss():
            if shipLocation2 == (0) and playerGuess == (1,1):
               print('|_| |0| |_| |_| |_|' + 'You missed their battleship! ')
            if shipLocation2 == (0) and playerGuess == (1,2):
               print('|_| |_| |0| |_| |_|' + 'You missed their battleship! ')
            if shipLocation2 == (0) and playerGuess == (1,3):
               print('|_| |_| |_| |0| |_|' + 'You missed their battleship! ')
            if shipLocation2 == (0) and playerGuess == (1,4):
               print('|_| |_| |_| |_| |0|' + 'You missed their battleship! ')
            row2_miss()
         miss()
game()
