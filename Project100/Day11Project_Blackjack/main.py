# Blackjack Project 
# Our Blackjack House Rules
 #####################
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import art
from replit import clear
def deal_card():
  """Return the random choice from the deck of cards"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  random_card = random.choice(cards)
  return random_card 
    
def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  if sum(cards) == 21 and range(len(cards)) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    index = cards.index(11)
    cards[index] = 1
  return sum(cards)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Game draw 🙃"
  elif user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
  elif computer_score == 0 or user_score > 21:
    return "User loses the game😤"
  elif user_score == 0 or computer_score > 21:
    return "User wins the game 😎"
  elif user_score > computer_score:
    return "You Win 😎"
  else:
    return "You lose😤"

def blackjack():
  print(art.logo)
  
  user_cards = []
  computer_cards = []
  game_ends = False

  for user in range(0,2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not game_ends:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    if user_score == 0 or user_score > 21 or computer_score == 0:
      game_ends = True
    else:
      should_continue = input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ").lower()
      if should_continue == "yes":
        user_cards.append(deal_card())
      else:
        game_ends = True

  while computer_score < 17 and           computer_score != 0:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, Computer's final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ") == "yes":
  clear()
  blackjack()
