def cout(box):
  print("●━━━●━━━●━━━●")
  for i in box[:3]:
    print("┃ " + i, end=" ")
  print("┃\n●━━━●━━━●━━━●")
  for i in box[3:6]:
    print("┃ " + i, end=" ")
  print("┃\n●━━━●━━━●━━━●")
  for i in box[6:]:
    print("┃ " + i, end=" ")
  print("┃\n●━━━●━━━●━━━●")

def reading(box, count):
  pos = int(input(("1st" if (count % 2) else "2nd") + 
  " player, enter the area number:")) - 1
  if (0 <= pos <= 8):
    if (box[pos] == " "): 
      box[pos] = "x" if (count % 2) else "o"
      return True
  return False

def check(box):
  for i in 0, 3, 6:
    if (box[i] == box[i+1] == box[i+2] != " "):
      return True
  for i in 0, 1, 2:
    if (box[i] == box[i+3] == box[i+6] != " "):
      return True
  if (box[0] == box[4] == box[8] != " "):
    return True
  if (box[2] == box[4] == box[6] != " "):
    return True
  return False

def answer(count):
  if (count > 0):
    print(("1st" if (count % 2) else "2nd") + 
    " player won")
  else:
    print("Friendship won")

def replay(func):
  def wrapper():
    func()
    if (input("Do you want to play again? (y/n)") == "y"):
      main()
  return wrapper

@replay
def main():
  print("\nThis is the game tic-tac-toe:")
  count, box = 9, [" "]*9
  cout(box)
  while(count):
    if (reading(box, count)):
      cout(box)
      if (check(box)):
        break
      count -= 1
  answer(count)

main()