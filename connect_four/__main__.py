from board import create_new_board
from board import print_board
from board import drop_piece
from board import get_next_open_row
from actions import check_win 
board_de_isabela = create_new_board()
with open('README.md', 'r') as f:
  print(f.read())
#PLAYER 1(O) AND PLAYER 2(X)

current_player = "X"
while True:
  command = input("Enter a command:")
  if command == "move":
      col_de_isabela = input("which column?")
      col_de_isabela = int(col_de_isabela)
      if col_de_isabela < 0:
         continue
      row_de_isabela = get_next_open_row(board_de_isabela,col_de_isabela)
      drop_piece(board_de_isabela,row_de_isabela,col_de_isabela,current_player)
      if current_player == "X":
        current_player = "O"
      elif current_player == "O":
        current_player = "X"
      who_has_won = check_win(board_de_isabela)
      if who_has_won == "X":
        print("X is the winner!")
      elif who_has_won == "O":
        print ("O is the winner!")
  elif command == "quit":
      exit()
  elif command == "print board": 
     print_board (board_de_isabela)
  else:
     print("I did not understand this command.")
      
