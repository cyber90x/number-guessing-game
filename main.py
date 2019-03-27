import random

randomnumber = random.randint(1, 10)
running = True

while running:
  print("guess number")
  gamejam = int(input())

  if gamejam < randomnumber:
    print("your number is low")
  elif gamejam > randomnumber:
    print("your number is too high")
  else:
    print("you win")
    running = False