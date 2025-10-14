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

    def make_payment(self, cost):
        """Handles the payment process and checks if the transaction is successful."""

        # Get the money from the customer
        money_received = self._process_coins()

        # Check if payment is sufficient
        if money_received >= cost:
            change = money_received - cost
            # Round change to avoid floating point errors
            change = round(change, 2)

            # Update profit
            self.profit += cost

            print(f"✅ Success! Here is {self.currency}{change:.2f} in change.")
            return True
        else:
            # Refund the money inserted
            print(f"❌ Payment failed. Not enough money. {self.currency}{money_received:.2f} refunded.")
            return False