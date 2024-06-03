############DEBUGGING#####################

# # Describe Problem
def my_function():
  # for i in range(1, 20): This line has a bug, it will never print 20 because the range function will stop at 19.
  for i in range(1, 21):
    if i == 20:
      print("You got it")
my_function()

# # Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6) - This line has a bug, it will never print the 6th element of the list because the randint function will never generate 6.
dice_num = randint(0,5)
print(dice_imgs[dice_num])

# # Play Computer
year = int(input("What's your year of birth?\n"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
# elif year > 1994: This line has a bug, it will never print anything for 1994 because the condition will never be met.
elif year >= 1994:
  print("You are a Gen Z.")

# # Fix the Errors
age = int(input("How old are you?\n"))
if (age) > 18:
# print("You can drive at age {age}.") - This line has a bug, it will never print anything because the print function is not indented. Also we need to convert the input to an integer and use f string while using print.
 print(f"You can drive at age {age}.")

# #Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: ")) - This line has a bug, it will nvever take input from the user but check for the value because it has a double equal sign(comparison operator).
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

# #Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
 # b_list.append(new_item) - This line has a bug, it will only append the last item of the list. It is outside of for loop , so use indentation.
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])