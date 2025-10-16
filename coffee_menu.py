import sqlite3
from unittest import expectedFailure


class CoffeeMenu:

    def __init__(self, db_name = "coffee.db"):
        self.db_name = db_name
        self.menu_items = self._load_menu_data()

    def _load_menu_data(self):

        conn = None

        try:
            conn= sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("SELECT name, price FROM coffee_types ORDER BY price ASC")
            items = []
            for name, price in cursor.fetchall():
                items.append({"name": name, "price": price})
            return items
        except sqlite3.Error as e:
            print(f"Database Error: {e}" )
            return []
        finally:
            if conn:
                conn.close()

    def display_menu(self):

        if not self.menu_items:
            print("Menu is currently unavailable. Please Check the Database")
            return
        print("Welcome to OOP Coffee Terminal")
        print("-" * 35)
        print(f"| {'Item':<20} | {'Price':>8} |")
        print("-" * 35)

        for item in self.menu_items:
            price_str = f"{item["price"]:.2f}:"
            print(f"{item["name"]:<20} | {price_str:>8} |" )
        print("-" * 35)

        choices = [item["name"].lower() for item in self.menu_items]
        return choices

    def find_item(self, order_name):

        order_name = order_name.lower()
        for item in self.menu_items:
            if item["name"].lower() == order_name:
                return item
        return None


