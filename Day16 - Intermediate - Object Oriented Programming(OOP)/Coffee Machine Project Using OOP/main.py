from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker

from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

machine_on = True

while machine_on:
    options = menu.get_items()
    print("Type 'off' to turn off the machine and 'report' to get the report below.")
    choice = input(f"What would you like? Options available: {options}: ")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
