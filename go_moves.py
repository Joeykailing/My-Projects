


# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Robert Parker
#               Joey Lim
#               Eric Martinez
#               Ha Jeong
# Section:      102-535
# Assignment:   lab 7
# Date:         05/10/2022
#

# used to convert letters collumbs to number cordinates
BoardDictionary = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8}

# User instructions
print("Black's piece is ●")
print("White's piece is o")
print('"." represents an empty space on the board')
print('Moves are entered as a number followed by an uppercase letter.')
print('If both players enter stop the game ends.')
print('If board is filled, both players should enter stop')


# list of lists used as game board
board = [['.', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.', '.']]

# print game board
print('  A  B  C  D  E  F  G  H  I')
blackmove =''
whitemove =''
for i in range(9):
    print(f'{i + 1} ', end='')
    for j in range(9):
        print(board[i][j], end='  ')
    print()
blackstop = False
whitestop = False

# game runs in a infinite loop unless both players said stop
while True:

# Check if black said stopped
  if not blackstop:
    blackmove = input("Black's move: ")

# If black enters stop they will no longer play
    if blackmove == 'stop' or blackmove == 'Stop':
        blackstop = True
        print("Black is no longer playing.")
      
# if place on the board for black is already taken game will ask again
    elif (board[(int(blackmove[0]) - 1)][BoardDictionary[blackmove[1]]] != '.'):
      duplicate_move = True
      while duplicate_move:
        print("That place on the board has been taken. Please pick another place. Thank you.")
# if player tries to move  reasks 
        blackmove = input("Black's move: ")
        if blackmove == 'stop' or blackmove == 'Stop':
          duplicate_move = False
          blackstop = True
          print("Black is no longer playing.")
          
        elif (board[(int(blackmove[0]) - 1)][BoardDictionary[blackmove[1]]] == '.') :
          duplicate_move = False
          board[(int(blackmove[0]) - 1)][BoardDictionary[blackmove[1]]] = '●'
          print('  A  B  C  D  E  F  G  H  I')
          for i in range(9):
              print(f'{i + 1} ', end='')
              for j in range(9):
                  print(board[i][j], end='  ')
              print()
        
        
          
# print board with black's move
    else:
      board[(int(blackmove[0])-1)][BoardDictionary[blackmove[1]]] = '●'
      print('  A  B  C  D  E  F  G  H  I')
      for i in range(9):
          print(f'{i + 1} ', end='')
          for j in range(9):
               print(board[i][j], end='  ')
          print()


# Check if white said stopped
  # If white enters stop they will no longer play
  if not whitestop:
    whitemove = input("\nWhite's move: ")
    if whitemove == 'stop' or whitemove == 'Stop':
      whitestop = True
      print("White is no longer playing.")
       
# if place on the board for white is already taken game will ask again
    elif (board[(int(whitemove[0]) - 1)][BoardDictionary[whitemove[1]]] != '.'):
      duplicate_move = True
      while duplicate_move:
        
        print("That place on the board has been taken. Please pick another place. Thank you.")
        whitemove = input("White's move: ")
        if whitemove == 'stop' or whitemove == 'Stop':
          duplicate_move = False
          whitestop = True
          print("White is no longer playing.")
        elif (board[(int(whitemove[0]) - 1)][BoardDictionary[whitemove[1]]] == '.') :
          duplicate_move = False
          board[(int(whitemove[0]) - 1)][BoardDictionary[whitemove[1]]] = 'o'
          print('  A  B  C  D  E  F  G  H  I')
          for i in range(9):
              print(f'{i + 1} ', end='')
              for j in range(9):
                  print(board[i][j], end='  ')
              print()
              

# print board with white's move
    else:
        board[(int(whitemove[0]) - 1)][BoardDictionary[whitemove[1]]] = 'o'
        print('  A  B  C  D  E  F  G  H  I')
        for i in range(9):
            print(f'{i + 1} ', end='')
            for j in range(9):
                print(board[i][j], end='  ')
            print()
            


# condition for stopping the loop if both player said stop
  if whitestop and blackstop:
    print('The game has ended.')
    break



