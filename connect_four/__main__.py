from board import create_new_board
from board import print_board
from board import drop_piece
from board import get_next_open_row
board_de_isabela = create_new_board()
with open('README.md', 'r') as f:
  print(f.read())

while True:
  command = input("Enter a command:")
  if command == "move":
      col_de_isabela = input("which column?")
      row_de_isabela = get_next_open_row(board_de_isabela,col_de_isabela)
      drop_piece(board_de_isabela,row_de_isabela,col_de_isabela,"X")
  elif command == "quit":
      exit()
  elif command == "print board": 
     print_board (board_de_isabela)
  else:
     print("I did not understand this command.")
      
