class MoneyMachine:
    CURRENCY = "$"

    VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.m_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def coins(self):
        """Returns the total calculated from coins inserted."""
        print(" Insert coins.")
        for coin in self.VALUES:
            self.m_received += int(input(f"How many {coin}?: ")) * self.VALUES[coin]
        return self.m_received

    def payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.coins()
        if self.m_received >= cost:
            change = round(self.m_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.m_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.m_received = 0
            return False
