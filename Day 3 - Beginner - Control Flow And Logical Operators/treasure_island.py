print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

op1 = input("You are on your way to find the treasure.Please choose where you want to go, left or right?\n")
op1.lower()
if op1 == "left":
          op2 = input("Congratulations! You have cleared the first step. Now you are at the lake. Choose whether you want to swim or wait for the boat?\n")
          op2.lower()
          if op2 == "wait":
                    op3 = input("Congratulations! You have done it again. Now you are in front of 3 doors. Choose which door you want to open. Red, Blue or Yellow?\n")
                    op3.lower()
                    if op3 == "yellow":
                              print("Congratulations! You are very lucky! You have found the treasure. You win!")
                    else:
                              print("You have opened the wrong door. Game over.")
          else:
                    print("There are dangers in the lake while swimming. Game over.")
else:
          print("You have chosen the wrong path. Game over.")

