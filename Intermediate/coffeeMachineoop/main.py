from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

on = True
while on:
    choice = menu.get_items()
    choices = input(f"What would you like? ({choice}): ")
    if choices == "off":
        on = False
    elif choices == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drinks = menu.drinks(choices)

    if coffee_maker.resource_sufficient(drinks) and money_machine.payment(drinks.cost):
        coffee_maker.coffee(drinks)
