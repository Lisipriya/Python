#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import art
import random

difficulty_level = { 
  "easy" : 10,
  "hard" : 5
}

def number_guess(user_guess, computer_guess):
  """Finding the Computer guessed number is equals or low or high 
  based on user's guess"""
  
  

  if computer_guess == user_guess:
    print(f"You got it! The answer was {computer_guess}.")
    return False

  elif user_guess > computer_guess:
    print("Too high.\nGuess again.")
    return True
  else:
    print("Too Low.\nGuess again.")
    return True

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
computer_guess = random.choice(range(1,101))
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
attempt = difficulty_level[level]
continue_guess = True
while continue_guess:

  print(f"You have {attempt} attempts remaining to guess the number.") 
  user_guess = int(input("Make a guess: "))
  continue_guess = number_guess(user_guess, computer_guess)
  attempt -= 1
  if attempt == 0:
    print(f"You lost it! The answer was {computer_guess}.")
    continue_guess = False