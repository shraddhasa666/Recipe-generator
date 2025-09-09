from flask import Flask, request, jsonify, render_template
import sqlite3
import json

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("recipes.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    query = request.args.get("ingredients", "").lower()
    search_ings = [ing.strip() for ing in query.split(",") if ing.strip()]

    if not search_ings:
        return jsonify([])  # Return empty list if no ingredients provided

    conn = get_db_connection()

    # Build placeholders for SQLite query
    placeholders = ",".join("?" for _ in search_ings)

    # SQLite query using json_each to check if any ingredient matches
    sql = f"""
    SELECT *
    FROM recipes
    WHERE EXISTS (
        SELECT 1
        FROM json_each(ingredients)
        WHERE LOWER(json_each.value) IN ({placeholders})
    )
    OR {" OR ".join(["LOWER(name) LIKE '%' || ? || '%'" for _ in search_ings])}
    """

    # Combine search_ings for ingredients and search_ings for name matching
    params = search_ings + search_ings

    recipes = conn.execute(sql, params).fetchall()
    conn.close()

    # Convert rows to dicts and parse ingredients JSON
    results = []
    for r in recipes:
        recipe = dict(r)
        recipe["ingredients"] = json.loads(recipe["ingredients"])
        results.append(recipe)

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
