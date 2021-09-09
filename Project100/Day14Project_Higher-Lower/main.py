from replit import clear
from game_data import data
import random
import art

def pick_random_dict():
  """Get data from random account"""
  rand_dict = random.choice(data)
  return rand_dict

def personality_description(rand_dictionary):
  """Format account into printable format: name, followers_count, description and country"""
  list_of_personality = list(rand_dictionary.values())
  name = list_of_personality[0]
  followers_count = list_of_personality[1]
  description = list_of_personality[2]
  country = list_of_personality[-1]
  return f"{name}, {description}, from {country}.", followers_count

def compare(follower_A, follower_B):
  if follower_A > follower_B:
    return "A"
  else:
    return "B"

score = 0
value_A = pick_random_dict()
compare_A = (personality_description(value_A))[0]
follower_A = int((personality_description(value_A))[1])
print("Welcome to Higher-Lower game")
print(art.logo)
continue_game = True

while continue_game:
  value_B = pick_random_dict()
  if value_A == value_B:
    value_B == pick_random_dict()
  compare_B = (personality_description(value_B))[0]
  follower_B = int((personality_description(value_B))[1])
  print(f"Compare A : {compare_A}")
  print(art.vs)
  print(f"Against B: {compare_B}")
  find_followers = input("Who has more followers? Type 'A' or 'B': ") 
  answer = compare(follower_A, follower_B)
  clear()
  print(art.logo)
  if answer == find_followers:
    score +=1   
    print(f"You are right! Current score: {score}")
    value_A = value_B
    compare_A = compare_B
    follower_A = follower_B
  else:
    continue_game = False
    print(f"Sorry, that's wrong. Final score: {score}")
