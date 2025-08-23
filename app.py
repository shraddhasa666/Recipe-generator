from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb://localhost:27017/")
db = client["recipeDB"]
recipes_collection = db["recipes"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["GET"])
def search_recipes():
    ingredients = request.args.get("ingredients")
    if not ingredients:
        return jsonify({"error": "Provide ingredients"}), 400

    query_ingredients = [i.strip().lower() for i in ingredients.split(",")]

    # Build list of regex conditions
    regex_conditions = []
    for ingredient in query_ingredients:
        regex_conditions.append({"ingredients": {"$regex": f"{re.escape(ingredient)}", "$options": "i"}})

    # Use $and so that all ingredients must match partially
    recipes = list(recipes_collection.find({"$and": regex_conditions}, {"_id": 0}))

    return jsonify(recipes)

if __name__ == "__main__":
    app.run(debug=True)
