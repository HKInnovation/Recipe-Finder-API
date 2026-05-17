# 🍽️ Recipe Finder API
A Flask-powered recipe search and management API backed by SQLite, with a built-in frontend. Browse paginated recipes, filter by cuisine, rating, and serving size — all through a clean REST interface.

---

## 🔍 What It Does
- Serves a paginated list of recipes sorted by rating
- Supports filtering by **title**, **cuisine**, **minimum rating**, and **exact serves**
- Imports recipes from a JSON dataset
- Auto-fills missing ratings via a bulk update utility
- Serves a built-in frontend from the same Flask app

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Flask | Web framework & API |
| Flask-SQLAlchemy | ORM & database management |
| SQLite | Lightweight local database |

---

## 📁 Project Structure

```
project/
├── app.py                  # Flask app & API routes
├── models.py               # SQLAlchemy database models
├── load_data.py            # Script to import recipes from JSON
├── bulk_update_rating.py   # Script to fill in missing ratings
├── recipes.json            # Your recipe dataset
└── frontend/
    └── index.html          # Frontend UI
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/recipe-finder.git
cd recipe-finder
```

### 2. Install dependencies
```bash
pip install flask flask-sqlalchemy
```

### 3. Add your recipe data

Place a `recipes.json` file in the project root:

```json
[
  {
    "title": "Spaghetti Carbonara",
    "cuisine": "Italian",
    "rating": 4.8,
    "prep_time": 10,
    "cook_time": 20,
    "total_time": 30,
    "description": "A classic Roman pasta dish.",
    "nutrients": { "calories": "450kcal", "protein": "20g" },
    "serves": 4
  }
]
```

### 4. Run the steps in order

**Start the server** (auto-creates the database):
```bash
python app.py
```

**Load recipe data** (in a new terminal):
```bash
python load_data.py
```

**Fix missing ratings** *(optional)*:
```bash
python bulk_update_rating.py
```

The app will be available at `http://localhost:5000`

---

## 📡 API Reference

### Get All Recipes (Paginated)

```
GET /api/recipes?page=1&limit=15
```

### Search & Filter Recipes

```
GET /api/recipes/search
```

| Query Param | Type | Description |
|---|---|---|
| `title` | string | Partial match on recipe title |
| `cuisine` | string | Partial match on cuisine type |
| `rating_min` | float | Minimum rating (e.g. `4.0`) |
| `serves` | int | Exact number of servings |

**Examples:**
```bash
GET /api/recipes/search?title=pasta
GET /api/recipes/search?cuisine=Indian
GET /api/recipes/search?rating_min=4.5
GET /api/recipes/search?cuisine=Italian&rating_min=4.0&serves=4
```

---

## 🗄️ Database Model

| Field | Type | Description |
|---|---|---|
| `id` | Integer | Primary key |
| `title` | String | Recipe name |
| `cuisine` | String | Cuisine type (e.g. Italian, Indian) |
| `rating` | Float | Rating out of 5 (nullable) |
| `prep_time` | Integer | Prep time in minutes |
| `cook_time` | Integer | Cook time in minutes |
| `total_time` | Integer | Total time in minutes |
| `description` | Text | Recipe description |
| `nutrients` | JSON | Nutritional info (flexible schema) |
| `serves` | String | Number of servings |

---

## 🛠️ Utility Scripts

**`load_data.py`** — Reads `recipes.json` and inserts records into the database. Skips duplicates by title.

**`bulk_update_rating.py`** — Sets all `NULL` ratings to `4.0`. Useful after initial data import.

---

## 📌 Requirements

- Python 3.8+
- `recipes.json` dataset in the project root
- `frontend/index.html` for the UI

---

## 🐛 Troubleshooting

| Problem | Fix |
|---|---|
| `ModuleNotFoundError` | Run `pip install flask flask-sqlalchemy` |
| `FileNotFoundError: recipes.json` | Make sure the JSON file is in the project root |
| Frontend shows 404 | Ensure `frontend/index.html` exists |
| Empty API results | Run `load_data.py` to populate the database |

---

## 📄 License

MIT License. Feel free to use and modify.