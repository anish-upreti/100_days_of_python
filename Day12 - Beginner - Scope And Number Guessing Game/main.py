from art import logo
import random

print(logo)

print("Namaste and Welcome to the Number Guessing Game")
print("You have to guess a number starting from 1 to 100. Good luck!")

random_num = random.randint(1, 100)


def compare(guess_num, random_num):
    if guess_num > random_num:
        print("Guess is high.")
    elif guess_num < random_num:
        print("Guess is low.")
    else:
        print(f"You guessed it right 🎉. The answer is {random_num}.")
    if attempts == 0:
        print("You have run out of chances. You lose.")


difficulty = input(
    "Choose a difficulty level: Type 'easy' or 'hard': ").lower()

# Either use this block of code or the one below
#
# if difficulty == "easy":
#   attempts = 10
#   for i in range(0,10):
#     guess_num = int(input("Guess a number: "))
#     compare(guess_num, random_num)
#     attempts -= 1
#     if guess_num == random_num:
#       break
#     print(f"You have {attempts} attempts remaining.\n")
# elif difficulty == "hard":
#   attempts = 5
#   for i in range (0,5):
#     guess_num = int(input("Guess a number: "))
#     compare(guess_num, random_num)
#     attempts -= 1
#     if guess_num == random_num:
#       break
#     print(f"You have {attempts} attempts remaining.\n")
# else:
#   print("Invalid input.")
#

# Either use this block of code or one above
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
else:
    print("Invalid Input")

while attempts > 0:
    guess_num = int(input("Guess a number: "))
    compare(guess_num, random_num)
    attempts -= 1
    if guess_num == random_num:
        break
    print(f"You have {attempts} attempts remaining.\n")
