import json
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["recipeDB"]
recipes_collection = db["recipes"]

# Load recipes from JSON file
with open("recipes.json", "r") as f:
    recipes = json.load(f)

# Convert ingredients to lowercase
for recipe in recipes:
    recipe["ingredients"] = [i.lower() for i in recipe["ingredients"]]

# Clear collection first (so we don’t duplicate)
recipes_collection.delete_many({})

# Insert all recipes
recipes_collection.insert_many(recipes)
print("✅ Recipes inserted successfully!")
