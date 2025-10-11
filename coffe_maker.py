import sqlite3

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


