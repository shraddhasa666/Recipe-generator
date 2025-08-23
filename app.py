from flask import Flask, jsonify, request
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # enable CORS for frontend requests

# Connect to local MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["recipeDB"]
recipes_collection = db["recipes"]

# Route to get all recipes
@app.route("/recipes", methods=["GET"])
def get_recipes():
    recipes = list(recipes_collection.find({}, {"_id": 0}))
    return jsonify(recipes)

# Route to search recipes by strict ingredients
@app.route("/recipes/search", methods=["GET"])
def search_recipes():
    ingredients = request.args.get("ingredients")  # ?ingredients=egg,onion
    if not ingredients:
        return jsonify({"error": "Please provide ingredients"}), 400

    # convert to lowercase and split by comma
    ingredients_list = [i.strip().lower() for i in ingredients.split(",")]

    # strict match: recipe must contain all provided ingredients
    query = {"ingredients": {"$all": ingredients_list}}
    recipes = list(recipes_collection.find(query, {"_id": 0}))

    return jsonify(recipes)

if __name__ == "__main__":
    app.run(debug=True)
