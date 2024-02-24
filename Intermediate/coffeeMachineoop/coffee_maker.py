class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 400,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def resource_sufficient(self, drink):
        make = True
        for things in drink.ingredients:
            if drink.ingredients[things] > self.resources[things]:
             #   print(f"Sorry there is not enough {things}.")
                make = False
        return make

    def coffee(self, order):
        for things in order.ingredients:
            self.resources[things] -= order.ingredients[things]
        print(f"Here is your {order.drinki} ☕️. Enjoy!")


