from app import app
from models import db, Recipe

with app.app_context():

    print("✅ Connected using Flask DB")

    # ✅ SHOW TABLE COUNT
    total = Recipe.query.count()
    print(f"📊 Total Recipes in DB: {total}")

    # ✅ UPDATE ALL NULL RATINGS
    updated = Recipe.query.filter(Recipe.rating == None).update(
        {Recipe.rating: 4.0},
        synchronize_session=False
    )

    db.session.commit()

    print(f"✅ Updated {updated} NULL ratings to 4.0")

    # ✅ VERIFY
    remaining = Recipe.query.filter(Recipe.rating == None).count()
    print(f"🔍 Remaining NULL ratings: {remaining}")

    print("✅ Bulk Rating Update Completed Successfully")
