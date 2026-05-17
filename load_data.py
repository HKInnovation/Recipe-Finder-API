import json
from app import app
from models import db, Recipe

FILE_PATH = "recipes.json"

with app.app_context():

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    # If JSON is a dict, convert to list
    if isinstance(data, dict):
        data = list(data.values())

    inserted = 0
    skipped = 0

    for item in data:
        if not isinstance(item, dict):
            skipped += 1
            continue

        title = item.get("title")
        cuisine = item.get("cuisine")

        # ✅ FIX RATING
        raw_rating = item.get("rating")
        try:
            rating = float(raw_rating) if raw_rating not in [None, "", "null"] else None
        except:
            rating = None

        prep_time = item.get("prep_time")
        cook_time = item.get("cook_time")
        total_time = item.get("total_time")
        description = item.get("description")
        nutrients = item.get("nutrients")

        # ✅ FIX SERVES
        raw_serves = item.get("serves")
        try:
            # If serves is invalid or missing, store 0
            serves = int(raw_serves)
        except (TypeError, ValueError):
            try:
                serves = int(raw_serves)
            except (TypeError, ValueError):
                serves = None
 # or None if you prefer

        # Skip duplicates by title
        if Recipe.query.filter_by(title=title).first():
            skipped += 1
            continue

        # Create recipe object
        recipe = Recipe(
            title=title,
            cuisine=cuisine,
            rating=rating,
            prep_time=prep_time,
            cook_time=cook_time,
            total_time=total_time,
            description=description,
            nutrients=nutrients,
            serves=serves
        )

        db.session.add(recipe)
        inserted += 1

    db.session.commit()

    print("✅ Import Complete")
    print(f"Inserted: {inserted}")
    print(f"Skipped: {skipped}")
