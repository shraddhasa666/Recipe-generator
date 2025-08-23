from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["recipeDB"]

recipes = list(db.recipes.find({}, {"_id": 0}))
for r in recipes:
    print(r)
