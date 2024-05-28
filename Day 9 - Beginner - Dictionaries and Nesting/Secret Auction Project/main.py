import os

import art

print(art.logo)

bidder_data = {}
def compare_bid(bidder_record):
  greatest_bid = 0
  highest_bidder = ""
  for bidder in bidder_record:
    bid_amount = bidder_record[bidder]
    if bid_amount > greatest_bid: 
      greatest_bid = bid_amount
      highest_bidder = bidder

  print(f"\nThe winner is {highest_bidder} with a bid of {greatest_bid}!")

bidding_finished = False
while not bidding_finished:
  name = input("What is your name?\n")
  bid = int(input("What is your bid?\n"))
  bidder_data[name] = bid
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
  if should_continue == "no":
    bidding_finished = True
    compare_bid(bidder_data)
  elif should_continue == "yes":
    os.system("clear")
  else:
    print("Invalid input. Please try again.")
