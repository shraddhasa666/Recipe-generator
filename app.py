from flask import Flask, jsonify, request
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["recipeDB"]
recipes_collection = db["recipes"]

# Route to get all recipes
@app.route("/recipes", methods=["GET"])
def get_recipes():
    recipes = list(recipes_collection.find({}, {"_id": 0}))
    return jsonify(recipes)

# Route to search recipes by strict ingredients
@app.route("/search", methods=["GET"])
def search_recipes():
    ingredients = request.args.get("ingredients")
    if not ingredients:
        return jsonify({"error": "Provide ingredients"}), 400

    # Convert query ingredients to lowercase list
    query_ingredients = [i.strip().lower() for i in ingredients.split(",")]

    # Strict search: recipe must contain ALL ingredients
    recipes = list(recipes_collection.find(
        {"ingredients": {"$all": query_ingredients}},
        {"_id": 0}
    ))
    return jsonify(recipes)

if __name__ == "__main__":
    app.run(debug=True)
