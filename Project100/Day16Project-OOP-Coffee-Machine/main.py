from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
machine_on = True

while machine_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ").lower()
    if choice == "report":
        coffee_maker.report()
        money_machine.report()

    elif choice == "off":
        machine_on = False

    else:
        drink = menu.find_drink(choice)
        resources_sufficient = coffee_maker.is_resource_sufficient(drink)
        transaction_sufficient = money_machine.make_payment(drink.cost)
        if resources_sufficient and transaction_sufficient:
            coffee_maker.make_coffee(drink)
