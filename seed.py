import sqlite3
import json

conn = sqlite3.connect("recipes.db")
cursor = conn.cursor()

# Drop old table if exists
cursor.execute("DROP TABLE IF EXISTS recipes")

# Recreate table with correct schema
cursor.execute("""
CREATE TABLE recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    ingredients TEXT,
    recipe TEXT,
    prep_time TEXT,
    cook_time TEXT,
    servings TEXT,
    nutrition TEXT,
    image TEXT
)
""")

# Load JSON
with open("recipes.json", "r") as f:
    recipes = json.load(f)

# Insert recipes
for r in recipes:
    cursor.execute("""
    INSERT INTO recipes (name, ingredients, recipe, prep_time, cook_time, servings, nutrition, image)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        r.get("name", ""),
        json.dumps(r.get("ingredients", [])),
        r.get("recipe", ""),
        r.get("prep_time", ""),
        r.get("cook_time", ""),
        r.get("servings", ""),
        r.get("nutrition", ""),
        r.get("image", "")
    ))

conn.commit()
conn.close()
print("✅ Database seeded successfully!")
