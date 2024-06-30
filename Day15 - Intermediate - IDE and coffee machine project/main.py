MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def compare_resource(order_ingredients):
    """returns true if resources are sufficient otherwise false"""
    for items in order_ingredients:
        if order_ingredients[items] > resources[items]:
            print(f"Sorry there is not enough {items}")
            return False
    return True


def calculate_coin():
    """returns the total calculated value of inserted coins"""
    print("Please insert coins.")
    total = int(input("Number of quarters: ")) * 0.25
    total += int(input("Number of dimes: ")) * 0.10
    total += int(input("Number of nickels: ")) * 0.05
    total += int(input("Number of pennies: ")) * 0.01
    return total


def check_transaction(money_received, cost):
    """returns true if money is sufficient, else returns false"""
    if money_received >= cost:
        global earning
        earning += cost
        change = round((money_received - cost), 2)
        print(f"Transaction successful. Here is your ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(coffee_name, order_ingredients):
    for items in order_ingredients:
        resources[items] -= order_ingredients[items]
    print(f"Here is your {coffee_name} ☕. Enjoy")


earning = 0
machine_on = True

while machine_on:
    option = input(
        "What would you like? Options available : Cappuccino, Latte, Espresso, 'off' and 'report' : ").lower()
    if option == "off":
        machine_on = False
    elif option == "report":
        print(f"Remaining water: {resources['water']}ml")
        print(f"Remaining milk: {resources['milk']}ml")
        print(f"Remaining coffee: {resources['coffee']}g")
        print(f"Money from sales: ${earning}")
    elif option == "cappuccino" or option == "latte" or option == "espresso":
        coffee = MENU[option]
        if compare_resource(coffee["ingredients"]):
            payment = calculate_coin()
            if check_transaction(payment, coffee["cost"]):
                make_coffee(option, coffee["ingredients"])
    else:
        print("Please enter a valid input.")
