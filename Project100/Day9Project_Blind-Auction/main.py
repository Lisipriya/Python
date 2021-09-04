from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
import products
import random
print(art.logo)
chosen_product= random.choice(products.product_list)
print("Welcome to the secret auction program for " + chosen_product)
auction = {}
continue_of_game = True

def find_highest_bidder(auction):
  max=0
  Max_bidder_name = ""
  for name in auction:
    bid_amount = int(auction[name])  
    if bid_amount > max:
      max = bid_amount
      Max_bidder_name = name
  print(f"The Secret bidding winner of {chosen_product} is {Max_bidder_name} with amount of ${max}")

while continue_of_game:
  name = input("What is your name?: ")
  bid = input("What's your bid? $")
  auction[name] = bid
  auction_continue = input("Are there any other bidders. Type yes or no\n")
  clear()
  if auction_continue == "no":
    continue_of_game = False
    find_highest_bidder(auction)   
  else:
    clear()
    