rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")
import random

inp = int(input())
opt = ["rock","paper","scissors"]

if(opt[inp] == "rock"):
  print(rock)
elif(opt[inp] == "paper"):
  print(paper)
else:
  print(scissors)

rand = random.randint(0,2)

print("Computer chose :")


if(opt[rand] == "rock"):
  print(rock)
elif(opt[rand] == "paper"):
  print(paper)
else:
  print(scissors)


if inp == 0:
  if rand == 1:
    print("You lose.")
  elif rand == 2:
    print("You Win")
  else:
    print("It's a draw")
elif inp == 1:
  if rand == 2:
    print("You lose")
  elif rand == 0:
    print("You Win")
  else:
    print("It's a draw")
else:
  if rand == 0 :
    print("You lose")
  elif rand == 1:
    print("You Win")
  else:
    print("It's a draw")
