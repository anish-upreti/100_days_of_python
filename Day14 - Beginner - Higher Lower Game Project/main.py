#import logo ,random module and game_data
import random
from game_data import data
import art
import os

# print logo
print(art.logo)
score = 0
continue_game = True
random_B = random.choice(data)


# function that takes the account data and return into printable format
def account_data(account):
  """return the account data into printable format"""
  acc_name = account["name"]
  acc_desc = account["description"]
  acc_country = account["country"]
  return f"{acc_name}, a {acc_desc}, from {acc_country}"


# function that checks the answer
def check_answer(guess, a_followers, b_followers):
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


while continue_game:
  # Choose a random account from list of accounts

  # Switching the account of option B to option A
  random_A = random_B
  random_B = random.choice(data)
  while random_A == random_B:
    random_B = random.choice(data)

  print(f"Option A: {account_data(random_A)}")
  print(art.vs)
  print(f"Option B: {account_data(random_B)}")

  guess = input("Guess who has more followers: 'A' or 'B': ").lower()

  # Get follower count of each account
  followers_of_A = random_A["follower_count"]
  followers_of_B = random_B["follower_count"]

  is_correct = check_answer(guess, followers_of_A, followers_of_B)

  # Clear the screen between rounds
  os.system("clear")  # for linux and mac
  # os.system("cls")   # for windows

  if is_correct:
    score += 1
    print(f"You got it right. Your score is {score}\n")
  else:
    continue_game = False
    print(f"Sorry, you are wrong. Your final score is {score}")
