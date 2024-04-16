from board import create_new_board
from board import print_board

with open('README.md', 'r') as f:
  print(f.read())
board = create_new_board()
while True:
  command = input("Enter a command:")
  if command == "move":
      move()
  elif command == "quit":
      exit()
  elif command == "print board": 
     board= create_new_board ()
     print_board (board)
  else:
     print("I did not understand this command.")
      
