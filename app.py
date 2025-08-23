from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://43shrad:shrad2003@cluster0.oi9xlxj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["recipeDB"]
recipes_collection = db["recipes"]

# Route: Get all recipes
@app.route("/recipes", methods=["GET"])
def get_all_recipes():
    recipes = list(recipes_collection.find({}, {"_id": 0}))
    return jsonify(recipes)

# Route: Strict search by multiple ingredients
@app.route("/search", methods=["GET"])
def search_recipes():
    # Get ingredients from query string
    ingredients = request.args.getlist("ingredients")  # e.g. ?ingredients=egg&ingredients=milk

    if not ingredients:
        return jsonify({"error": "No ingredients provided"}), 400

    # Convert all ingredients to lowercase for strict case-insensitive match
    ingredients = [i.strip().lower() for i in ingredients]

    # Strict search: recipe must contain ALL ingredients
    query = {"ingredients": {"$all": ingredients}}

    results = list(recipes_collection.find(query, {"_id": 0}))

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
