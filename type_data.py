import sqlite3

# --- Database Initialization (Creating Tables) ---

# Connect (creates a file if it doesn’t exist)
conn = sqlite3.connect("coffee.db")
cursor = conn.cursor()

# Create a table for coffee types (if it doesn't exist)
cursor.execute("""
CREATE TABLE IF NOT EXISTS coffee_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    origin TEXT,
    roast_level TEXT,
    flavor_notes TEXT,
    price REAL
)
""")

# ---  Create the 'recipes' table here ---
cursor.execute("""
CREATE TABLE IF NOT EXISTS recipes (
    coffee_name TEXT PRIMARY KEY NOT NULL,
    water_ml INTEGER,
    coffee_g INTEGER,
    milk_ml INTEGER
)
""")

# --- Coffee Types Data Insertion (Only if empty) ---

# Check if coffee types already exist
cursor.execute("SELECT COUNT(*) FROM coffee_types")
if cursor.fetchone()[0] == 0:
    coffee_data = [
        ("Espresso", "Italy", "Dark", "Rich, strong, bold", 2.50),
        ("Americano", "USA", "Medium", "Smooth, slightly bitter", 3.00),
        ("Latte", "France", "Light", "Creamy, sweet, milky", 3.50),
        ("Cappuccino", "Italy", "Medium", "Frothy, balanced", 3.75),
        ("Mocha", "Yemen", "Medium-Dark", "Chocolate, nutty", 4.00),
        ("Macchiato", "Italy", "Dark", "Intense, slightly sweet", 3.25),
        ("Flat White", "Australia", "Medium", "Velvety, balanced", 3.80),
        ("Cortado", "Spain", "Medium", "Bold, smooth", 3.20),
        ("Cold Brew", "USA", "Medium", "Chilled, low acidity", 4.50),
        ("Turkish Coffee", "Turkey", "Dark", "Strong, aromatic, spiced", 4.00),
    ]

    cursor.executemany("""
    INSERT INTO coffee_types (name, origin, roast_level, flavor_notes, price)
    VALUES (?, ?, ?, ?, ?)
    """, coffee_data)
    print("✅ Added 10 coffee types to coffee.db!")

# --- Recipe Data Insertion (Only if empty) ---

# Check if recipes already exist
cursor.execute("SELECT COUNT(*) FROM recipes")
if cursor.fetchone()[0] == 0:
    # (Coffee Name, Water_ml, Coffee_g, Milk_ml)
    recipe_data = [
        ("Espresso", 50, 18, 0),
        ("Americano", 150, 18, 0),
        ("Latte", 50, 18, 200),
        ("Cappuccino", 75, 18, 150),
        ("Mocha", 75, 20, 150),
        ("Macchiato", 50, 18, 50),
        ("Flat White", 75, 18, 150),
        ("Cortado", 50, 18, 100),
        ("Cold Brew", 300, 30, 0), # Uses more water and coffee grounds
        ("Turkish Coffee", 100, 25, 0),
    ]

    cursor.executemany("""
    INSERT INTO recipes (coffee_name, water_ml, coffee_g, milk_ml)
    VALUES (?, ?, ?, ?)
    """, recipe_data)
    print("✅ Added 10 coffee recipes to coffee.db!")

# --- Final commit and close at the end ---
conn.commit()
conn.close()
