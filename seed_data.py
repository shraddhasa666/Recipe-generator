from pymongo import MongoClient

# Replace with your actual connection string
client = MongoClient("mongodb+srv://recipe_user:recipe123@cluster0.obfkhz2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["recipe_db"]

recipes = [
    # Italian
    {
        "name": "Margherita Pizza",
        "cuisine": "Italian",
        "ingredients": ["pizza dough", "tomato sauce", "mozzarella", "basil"]
    },
    {
        "name": "Pasta Carbonara",
        "cuisine": "Italian",
        "ingredients": ["pasta", "egg", "parmesan", "bacon"]
    },
    {
        "name": "Lasagna",
        "cuisine": "Italian",
        "ingredients": ["lasagna noodles", "tomato sauce", "ground beef", "ricotta", "mozzarella"]
    },

    # Indian
    {
        "name": "Chicken Curry",
        "cuisine": "Indian",
        "ingredients": ["chicken", "onion", "tomato", "garam masala", "ginger", "garlic"]
    },
    {
        "name": "Paneer Butter Masala",
        "cuisine": "Indian",
        "ingredients": ["paneer", "butter", "tomato", "cream", "garam masala"]
    },
    {
        "name": "Biryani",
        "cuisine": "Indian",
        "ingredients": ["rice", "chicken", "onion", "yogurt", "biryani masala"]
    },

    # Chinese
    {
        "name": "Fried Rice",
        "cuisine": "Chinese",
        "ingredients": ["rice", "egg", "carrot", "peas", "soy sauce"]
    },
    {
        "name": "Kung Pao Chicken",
        "cuisine": "Chinese",
        "ingredients": ["chicken", "peanuts", "chili peppers", "soy sauce", "garlic"]
    },
    {
        "name": "Spring Rolls",
        "cuisine": "Chinese",
        "ingredients": ["spring roll wrappers", "cabbage", "carrot", "soy sauce"]
    },

    # Mexican
    {
        "name": "Tacos",
        "cuisine": "Mexican",
        "ingredients": ["tortilla", "beef", "cheddar", "lettuce", "tomato"]
    },
    {
        "name": "Guacamole",
        "cuisine": "Mexican",
        "ingredients": ["avocado", "lime", "onion", "cilantro"]
    },
    {
        "name": "Quesadilla",
        "cuisine": "Mexican",
        "ingredients": ["tortilla", "cheddar", "chicken", "bell pepper"]
    },

    # American
    {
        "name": "Burger",
        "cuisine": "American",
        "ingredients": ["burger bun", "beef patty", "lettuce", "tomato", "cheddar"]
    },
    {
        "name": "Mac and Cheese",
        "cuisine": "American",
        "ingredients": ["macaroni", "cheddar", "milk", "butter"]
    },
    {
        "name": "Hot Dog",
        "cuisine": "American",
        "ingredients": ["hot dog bun", "sausage", "mustard", "ketchup"]
    }
]

# Insert recipes
db.recipes.insert_many(recipes)
print("Sample recipes inserted successfully!")
