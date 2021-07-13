from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
coffee_maker.report()
money_machine.report()
menu = Menu()

is_on = True
while is_on:
    # TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino/):”  
    choice = input("What would you like? (espresso/latte/cappuccino/):")

    # TODO 2:
    if choice == "off":
        is_on = False

    # TODO 3:
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
        
    # TODO 4:
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
            

    # TODO 5:
    # TODO 6:
    # TODO 7: