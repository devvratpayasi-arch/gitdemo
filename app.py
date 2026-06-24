from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("recipes.db")

@app.route("/", methods=["GET", "POST"])
def index():
    recipes = []
    if request.method == "POST":
        ingredient = request.form["ingredient"].lower()
        con = get_db()
        cur = con.cursor()
        cur.execute("SELECT name, ingredients, steps FROM recipes WHERE ingredients LIKE ?", ('%' + ingredient + '%',))
        recipes = cur.fetchall()
        con.close()
    return render_template("index.html", recipes=recipes)

if __name__ == "__main__":
    app.run(debug=True)
