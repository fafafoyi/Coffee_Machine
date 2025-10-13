class MoneyMachine:

    currency = "$"

    coin_values = {

        "dollar" : 1,
        "cent" : 0.50,
        "quarters" : 0.25,
        "dimes" : 0.10,
        "nickels": 0.05

    }

    def __init__(self):

        self.profit = 0.0

    def report(self):

        print(f"Machine Profit: {self.currency}{self.profit:.2f}")

    def _process_coins(self):

        print("Please insert coins.")
        total = 0.0
        for coin_name, coin_value in self.coin_values.items():
            while True:
                try:
                    amount = int(input(f"How many {coin_name}s?: "))
                    total += amount * coin_value
                    break
                except ValueError:
                    print("Invalid input. Please enter a whole number")

        return total