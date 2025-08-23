from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["recipeDB"]
recipes_collection = db["recipes"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recipes", methods=["GET"])
def get_recipes():
    recipes = list(recipes_collection.find({}, {"_id": 0}))
    return jsonify(recipes)

@app.route("/search", methods=["GET"])
def search_recipes():
    ingredients = request.args.get("ingredients")
    if not ingredients:
        return jsonify({"error": "Provide ingredients"}), 400

    query_ingredients = [i.strip().lower() for i in ingredients.split(",")]

    recipes = list(recipes_collection.find(
        {"ingredients": {"$all": query_ingredients}},
        {"_id": 0}
    ))
    return jsonify(recipes)

if __name__ == "__main__":
    app.run(debug=True)
