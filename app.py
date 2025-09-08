from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

DB_NAME = "recipes.db"

# ------------------------------
# Helper: convert DB row to dict
# ------------------------------
def row_to_dict(row):
    return {
        "id": row[0],
        "name": row[1],
        "ingredients": row[2].split(","),
        "instructions": row[3],
        "prep_time": row[4],
        "cook_time": row[5],
        "servings": row[6]
    }

# ------------------------------
# Home page
# ------------------------------
@app.route("/")
def home():
    return render_template("index.html")

# ------------------------------
# Search endpoint
# ------------------------------
@app.route("/search")
def search():
    search_query = request.args.get("ingredients", "").lower().strip()
    if not search_query:
        return jsonify([])

    search_terms = [term.strip() for term in search_query.split(",")]

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM recipes")
    rows = cursor.fetchall()
    conn.close()

    results = []
    for row in rows:
        recipe = row_to_dict(row)
        recipe_ingredients = [i.strip().lower() for i in recipe["ingredients"]]

        # fuzzy match: "egg" should match "eggs"
        if all(any(term in ing for ing in recipe_ingredients) for term in search_terms):
            results.append(recipe)

    return jsonify(results)

# ------------------------------
# Run app
# ------------------------------
if __name__ == "__main__":
    app.run(debug=True)
