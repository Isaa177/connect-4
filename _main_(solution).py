from hello import hello

with open('READ.md' 'r') as f:
  print(f.read())

while True:
  command = input("Enter a command:")
  if command == "hello":
      hello()
  elif command == "q":
      exit()
  else:
     print("I did not understand this command.")
  
