from pymongo import MongoClient

# Connect to local MongoDB
client = MongoClient("mongodb://localhost:27017/")  # use local MongoDB
db = client["recipeDB"]
recipes_collection = db["recipes"]

# List of recipes
recipes = [
    {"name": "Pasta", "ingredients": ["pasta", "tomato", "cheese", "olive oil"]},
    {"name": "Omelette", "ingredients": ["egg", "salt", "onion", "oil"]},
    {"name": "Salad", "ingredients": ["lettuce", "tomato", "cucumber", "lemon"]},
    {"name": "Fried Rice", "ingredients": ["rice", "carrot", "peas", "soy sauce", "egg"]},
    {"name": "Grilled Cheese", "ingredients": ["bread", "cheese", "butter"]},
]

# Convert all ingredients to lowercase
for recipe in recipes:
    recipe["ingredients"] = [i.lower() for i in recipe["ingredients"]]

# Insert only if collection is empty
if recipes_collection.count_documents({}) == 0:
    recipes_collection.insert_many(recipes)
    print("✅ Recipes inserted successfully!")
else:
    print("⚡ Recipes already exist in DB.")
