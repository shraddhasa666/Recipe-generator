from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# ---------- Database Setup ----------
def init_db():
    conn = sqlite3.connect("recipes.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            ingredients TEXT NOT NULL,
            image TEXT,
            recipe TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# ---------- Helper Functions ----------
def query_recipes(ingredients):
    conn = sqlite3.connect("recipes.db")
    cursor = conn.cursor()

    ingredients_list = [ing.strip().lower() for ing in ingredients.split(",")]

    query = "SELECT name, ingredients, image, recipe FROM recipes"
    cursor.execute(query)
    all_recipes = cursor.fetchall()
    conn.close()

    # Filter manually to allow partial matches (egg vs eggs)
    results = []
    for name, ing, image, recipe in all_recipes:
        ing_list = [i.strip().lower() for i in ing.split(",")]
        if all(any(q in i or i in q for i in ing_list) for q in ingredients_list):
            results.append({
                "name": name,
                "ingredients": ing_list,
                "image": image if image else "placeholder.jpg",
                "recipe": recipe
            })
    return results

# ---------- Routes ----------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search")
def search():
    ingredients = request.args.get("ingredients", "")
    if not ingredients:
        return jsonify([])
    return jsonify(query_recipes(ingredients))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
