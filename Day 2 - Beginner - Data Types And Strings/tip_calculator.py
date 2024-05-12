 
print("Namaste and Welcome to the tip calculator")

bill = float(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? "))

people = int(input("How many people to split the bill??"))

total_amount = bill + (bill *(tip/100))

amount_per_head = total_amount/people

print(f"Each person should pay: ${round(amount_per_head,2)}")
