import sqlite3

class coffee_menu:

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
                items.append({})