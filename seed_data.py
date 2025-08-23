import json
from pymongo import MongoClient

# Connect to local MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["recipeDB"]
recipes_collection = db["recipes"]

# Load recipes from JSON file
with open("recipes.json", "r") as f:
    recipes = json.load(f)

# Convert all ingredients to lowercase
for recipe in recipes:
    recipe["ingredients"] = [i.lower() for i in recipe["ingredients"]]

# Insert only if collection is empty
if recipes_collection.count_documents({}) == 0:
    recipes_collection.insert_many(recipes)
    print("✅ Recipes inserted successfully!")
else:
    print("⚡ Recipes already exist in DB.")
