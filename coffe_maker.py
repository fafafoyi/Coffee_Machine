import sqlite3
from operator import countOf


class CoffeeMaker:
     """Manages machine's resources and makes the coffee"""

     def __init__(self, db_name="coffee.db"):

             self.db_name = db_name
             self.resources = {
                 "water_ml": 1000,
                 "milk_ml": 800,
                 "coffe_g": 300

             }

    def _get_recipe(self, coffee_name):

            conn= None
            recipe = None
            try:
                conn = sqlite3.connect(self.db_name)
                cursor= conn.cursor()
                cursor.execute(
                    "SELECT water_ml, coffee_g, milk_ml FROM recipes WHERE coffee_name = ?",
                    (coffee_name,)
                )
                data = cursor.fetchone()
                if data:
                    recipe = {
                        "water_ml": data[0],
                        "milk_ml": data[2],
                        "coffee_g": data[1]

                    }
                return recipe
            except sqlite3.Error as e:
                print(f"Database error while fetching recipe: {e}")
                return None
            finally:
                if conn:
                    conn.close()

    def report(self):
        """printing current resource levels"""
        print("\n--- Coffe Machine Inventory")
        print(f"Water: {self.resource ['water_ml']}ml")
        print(f"Milk: {self.resource ['milk_ml']}ml")
        print(f"Coffe: {self.resource ['coffee_g']}g")
        print("-------------------------------------")

    def is_resource_sufficient(self, coffee_name):

        recipe = self._get_recipe(coffee_name)
        if not recipe:
            print(f"Error: Could not find recipe for {coffee_name}.")
            return False

        can_make = True
        for ingredient, required_amount in recipe.items():
            current_amount = self.resources[ingredient]
            if required_amount > current_amount:

                display_name = ingredient.split("-")[0].capitalize()
                print(f"Sorry, there is not enough {display_name} for a {coffee_name}. ")
                can_make = False

        return can_make, recipe

    def make_coffe(self, coffee_name, recipe):

        self.resources["water_ml"] -= recipe["water_ml"]
        self.resources["milk_ml"] -= recipe["milk_ml"]
        self.resources["coffee_g"] -= recipe["coffee_ml"]

        print(f"Dispensing your {coffee_name}...")
        print(f"Enjoy your {coffee_name}")

    def refill(self):

        self.resources = {

            "water_ml" : 1000,
            "milk_ml": 800,
            "coffee_g": 300

        }

        print("Inventory successfully refilled")








