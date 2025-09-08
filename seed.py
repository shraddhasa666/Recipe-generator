import sqlite3
import json

conn = sqlite3.connect("recipes.db")
cursor = conn.cursor()

# Drop old table (optional, if you want to start fresh)
cursor.execute("DROP TABLE IF EXISTS recipes")

# Create table with new columns
cursor.execute("""
CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    ingredients TEXT NOT NULL,
    recipe TEXT NOT NULL,
    prep_time TEXT,
    cook_time TEXT,
    servings TEXT
)
""")

# Load data from recipes.json
with open("recipes.json", "r", encoding="utf-8") as f:
    recipes = json.load(f)

for recipe in recipes:
    name = recipe.get("name", "Unknown Recipe")
    ingredients = ", ".join(recipe.get("ingredients", []))
    instructions = recipe.get("recipe", "No instructions available.")
    prep_time = recipe.get("prep_time", "N/A")
    cook_time = recipe.get("cook_time", "N/A")
    servings = recipe.get("servings", "N/A")

    cursor.execute("""
    INSERT INTO recipes (name, ingredients, instructions, prep_time, cook_time, servings)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (name, ingredients, instructions, prep_time, cook_time, servings))

conn.commit()
conn.close()
print("✅ Database seeded successfully!")
