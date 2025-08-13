from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

# Replace <username> and <password> with your MongoDB Atlas credentials
client = MongoClient("mongodb+srv://recipe_user:recipe123@cluster0.obfkhz2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Choose a database name (it will be created automatically if it doesn't exist)
db = client["recipe_db"]

@app.route("/")
def home():
    return "MongoDB connection successful!"
@app.route("/add_test_recipe")
def add_test_recipe():
    sample_recipe = {
        "name": "Test Pasta",
        "ingredients": ["pasta", "tomato sauce", "cheese"],
        "cuisine": "Italian"
    }
    db.recipes.insert_one(sample_recipe)
    return "Test recipe added!"

from flask import request, jsonify

@app.route("/search")
def search_recipes():
    ingredients = request.args.get("ingredients")
    cuisine = request.args.get("cuisine")

    ingredient_list = []
    if ingredients:
        ingredient_list = [ing.strip().lower() for ing in ingredients.split(",")]

    results = list(db.recipes.find({}, {"_id": 0}))
    exact_matches = []
    partial_matches = []

    for recipe in results:
        recipe_ingredients = [i.lower() for i in recipe["ingredients"]]
        recipe_cuisine = recipe["cuisine"].lower()

        # Cuisine filter (if specified)
        if cuisine and recipe_cuisine != cuisine.strip().lower():
            continue

        if ingredient_list:
            if all(ing in recipe_ingredients for ing in ingredient_list):
                exact_matches.append(recipe)
            elif any(ing in recipe_ingredients for ing in ingredient_list):
                partial_matches.append(recipe)
        else:
            exact_matches.append(recipe)  # No ingredients specified = include all

    if exact_matches:
        return jsonify(exact_matches)
    elif partial_matches:
        return jsonify(partial_matches)
    else:
        return jsonify({"message": "No matching recipes found"}), 404



if __name__ == "__main__":
    app.run(debug=True)
