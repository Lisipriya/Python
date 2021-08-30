import random
rock = ''' Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = ''' Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = ''' Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.
print("Welcome to the Rock Paper Scissors Game")
choice_int = int(input("What do you choose Type 0 for Rock, Type 1 for Paper and Type 2 for Scissors\nUser turn:\n"))
if choice_int>2:
  print("Enter number between 0 and 2")
choice = [rock, paper, scissors]
print(f"{choice[choice_int]}")
rand_int = random.randint(0, 2)
if choice_int == rand_int:
  print(f"Computer turn:\n{choice[rand_int]} \n Game Draw")
elif (choice_int == 0 and rand_int == 2) or (choice_int == 1 and rand_int == 0) or (choice_int == 2 and rand_int == 1):
  print(f"Computer turn:\n{choice[rand_int]} \n You won the Game")
else:
  print(f"Computer turn:\n{choice[rand_int]} \n You lose the Game")
