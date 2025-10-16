from coffee_menu import CoffeeMenu
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker

def main():

    menu = CoffeeMenu()
    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker()

    if not menu.display_menu():
        print("Exiting program due to missing menu item")
        return

    is_on = True
    print("\n---- Welcome to the Fatih's Coffee Co. ----")

    while is_on :

        menu_choices = menu.display_menu()

        prompt_choices = ", ".join(menu_choices)

        choices = input(f"\nWhat would you like? ({prompt_choices}/ report / refill / off): ").lower()



