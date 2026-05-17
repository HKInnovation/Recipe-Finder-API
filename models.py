from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(255))
    cuisine = db.Column(db.String(100))
    rating = db.Column(db.Float, nullable=True)

    prep_time = db.Column(db.Integer, nullable=True)
    cook_time = db.Column(db.Integer, nullable=True)
    total_time = db.Column(db.Integer, nullable=True)

    description = db.Column(db.Text)
    nutrients = db.Column(db.JSON)
    serves = db.Column(db.String(50))
