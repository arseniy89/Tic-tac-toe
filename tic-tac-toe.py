def cout():
  print("+" +"---+"*2 + "---+")
  for i in range(0, 3):
    print("| "+box[i], end=" ")
  print("|")
  print("+" +"---+"*2 + "---+")
  for i in range(3, 6):
    print("| "+box[i], end=" ")
  print("|")
  print("+" +"---+"*2 + "---+")
  for i in range(6, 9):
    print("| "+box[i], end=" ")
  print("|")
  print("+" +"---+"*2 + "---+")

def check():
  for i in (0, 3, 6):
    if (box[i] == box[i+1] == box[i+2] != " "):
      return True
  for i in (0, 1, 2):
    if (box[i] == box[i+3] == box[i+6] != " "):
      return True
  if (box[0] == box[4] == box[8] != " "):
    return True
  if (box[2] == box[4] == box[6] != " "):
    return True
  return False

print("This is the game tic-tac-toe:")
count, box = 9, [" "]*9
cout()

while(count):
  pos = int(input(("First" if (count % 2 == 1) else "Second") + 
  " player, enter the area number:"))
  if (box[pos-1] == " "): 
    box[pos-1] = "x" if (count % 2 == 1) else "o"
    cout()
    if (check()): break
    count -= 1
    
if (count > 0):
  print(("First" if (count % 2 == 1) else "Second") + 
  " player won")
else:
  print("Friendship won")