from board import create_new_board

with open('README.md', 'r') as f:
  print(f.read())

board = create_new_board()
while True:
  command = input("Enter a command:")
  if command == "move":
      move()
  elif command == "quit":
      exit()
  else:
     print("I did not understand this command.")
  
  board = create_new_board()
  while True: 
     command = input ("Enter a command")
     if command == "print_board"
        print_board ()
  elif command == "quit": 
       exit ()
  else: 
    print ("I did not understand this command")
