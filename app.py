from flask import Flask, request, jsonify, send_from_directory
from models import db, Recipe
import os

app = Flask(__name__, static_folder="frontend")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///recipes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


# ✅ CREATE DATABASE AUTOMATICALLY
with app.app_context():
    db.create_all()


# ✅ Serve frontend
@app.route("/")
def frontend():
    return send_from_directory("frontend", "index.html")


# ✅ Serve static files
@app.route("/frontend/<path:filename>")
def serve_static(filename):
    return send_from_directory("frontend", filename)


# ✅ API: Get all recipes (with pagination)
@app.route("/api/recipes", methods=["GET"])
def get_recipes():
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 15))

    query = Recipe.query.order_by(Recipe.rating.desc().nullslast())
    total = query.count()

    recipes = query.offset((page - 1) * limit).limit(limit).all()

    return jsonify({
        "page": page,
        "limit": limit,
        "total": total,
        "data": [
            {
                "id": r.id,
                "title": r.title,
                "cuisine": r.cuisine,
                "rating": r.rating,
                "prep_time": r.prep_time,
                "cook_time": r.cook_time,
                "total_time": r.total_time,
                "description": r.description,
                "nutrients": r.nutrients,
                "serves": r.serves,
            }
            for r in recipes
        ]
    })


# ✅ API: Search Recipes (WITH EXACT SERVES FILTER)
@app.route("/api/recipes/search", methods=["GET"])
def search_recipes():
    query = Recipe.query

    title = request.args.get("title")
    cuisine = request.args.get("cuisine")
    rating_min = request.args.get("rating_min")
    serves_exact = request.args.get("serves")   # ✅ EXACT SERVES

    if title:
        query = query.filter(Recipe.title.ilike(f"%{title}%"))

    if cuisine:
        query = query.filter(Recipe.cuisine.ilike(f"%{cuisine}%"))

    if rating_min:
        query = query.filter(Recipe.rating >= float(rating_min))

    # ✅ EXACT SERVE MATCH (NOT MIN/MAX)
    if serves_exact:
        query = query.filter(Recipe.serves == int(serves_exact))

    results = query.all()

    return jsonify({
        "data": [
            {
                "id": r.id,
                "title": r.title,
                "cuisine": r.cuisine,
                "rating": r.rating,
                "prep_time": r.prep_time,
                "cook_time": r.cook_time,
                "total_time": r.total_time,
                "description": r.description,
                "nutrients": r.nutrients,
                "serves": r.serves
            }
            for r in results
        ]
    })


if __name__ == "__main__":
    app.run(debug=True)
