from flask import Flask, render_template, request, jsonify
import json
import difflib

app = Flask(__name__)

# Load recipes from JSON file
with open("recipes.json", "r", encoding="utf-8") as f:
    recipes = json.load(f)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search")
def search():
    ingredients_query = request.args.get("ingredients", "").lower().split(",")
    ingredients_query = [i.strip() for i in ingredients_query if i.strip()]

    results = []
    for recipe in recipes:
        # Match ingredients loosely (egg ≈ eggs)
        matched = False
        for query in ingredients_query:
            for ing in recipe["ingredients"]:
                if query in ing.lower() or difflib.get_close_matches(query, [ing.lower()]):
                    matched = True
        if matched:
            results.append(recipe)

    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)
