from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

# Load recipes from JSON file
def load_recipes():
    with open("recipes.json", "r", encoding="utf-8") as f:
        return json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    query = request.args.get("ingredients", "").lower().split(",")
    query = [q.strip() for q in query if q.strip()]

    recipes = load_recipes()
    results = []

    for recipe in recipes:
        ingredients = [i.lower() for i in recipe["ingredients"]]
        if all(any(q in ing or ing in q for ing in ingredients) for q in query):
            results.append(recipe)

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
