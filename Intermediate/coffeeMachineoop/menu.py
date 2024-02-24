class MenuItem:
    def __init__(self, drinki, water, milk, coffee, cost):
        self.drinki = drinki
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(drinki="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(drinki="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(drinki="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        choice = ""
        for things in self.menu:
            choice += f"{things.drinki}/"
        return choice

    def drinks(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.drinki == order_name:
                return item
        print("Sorry that item is not available.")
