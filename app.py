<<<<<<< HEAD
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
=======
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


recipes_database = [
    {
        'id': 1,
        'name': 'Carrot Ginger Soup',
        'vegetables': ['carrot', 'onion', 'garlic'],
        'description': 'A warm and comforting soup with a hint of ginger',
        'cook_time': '30 mins',
        'difficulty': 'Easy',
        'servings': 4,
        'ingredients': ['4 large carrots, peeled and chopped', '1 onion, diced', '2 cloves garlic, minced', '1 tbsp fresh ginger, grated', '4 cups vegetable broth', '1/2 cup coconut milk', 'Salt and pepper to taste', '2 tbsp olive oil'],
        'instructions': '1. Heat olive oil in a large pot over medium heat. 2. Add onion and garlic, sauté until softened. 3. Add carrots and ginger, cook for 5 minutes. 4. Pour in vegetable broth, bring to a boil. 5. Reduce heat and simmer for 20 minutes until carrots are tender. 6. Blend until smooth, stir in coconut milk. 7. Season with salt and pepper.'
    },
    {
        'id': 2,
        'name': 'Fresh Carrot Salad',
        'vegetables': ['carrot', 'lettuce'],
        'description': 'A crunchy and refreshing salad perfect for lunch',
        'cook_time': '10 mins',
        'difficulty': 'Easy',
        'servings': 2,
        'ingredients': ['3 carrots, grated', '2 cups lettuce, chopped', '1/4 cup raisins', '1/4 cup walnuts, chopped', '2 tbsp lemon juice', '3 tbsp olive oil', '1 tsp honey', 'Salt to taste'],
        'instructions': '1. Grate carrots into a large bowl. 2. Add chopped lettuce, raisins, and walnuts. 3. In a small bowl, whisk together lemon juice, olive oil, honey, and salt. 4. Pour dressing over salad and toss well. 5. Serve immediately.'
    },
    {
        'id': 3,
        'name': 'Broccoli Stir Fry',
        'vegetables': ['broccoli', 'bell pepper', 'garlic'],
        'description': 'Quick and healthy Asian-inspired stir fry',
        'cook_time': '15 mins',
        'difficulty': 'Easy',
        'servings': 3,
        'ingredients': ['2 cups broccoli florets', '1 red bell pepper, sliced', '3 cloves garlic, minced', '2 tbsp soy sauce', '1 tbsp sesame oil', '1 tsp cornstarch', '1/4 cup water', '1 tbsp vegetable oil', 'Sesame seeds for garnish'],
        'instructions': '1. Mix soy sauce, sesame oil, cornstarch, and water in a small bowl. 2. Heat vegetable oil in a wok or large pan over high heat. 3. Add garlic and stir fry for 30 seconds. 4. Add broccoli and bell pepper, stir fry for 5 minutes. 5. Pour in sauce mixture, cook for 2-3 minutes until thickened. 6. Garnish with sesame seeds.'
    },
    {
        'id': 4,
        'name': 'Creamy Broccoli Soup',
        'vegetables': ['broccoli', 'potato', 'onion'],
        'description': 'Rich and creamy soup that\'s also healthy',
        'cook_time': '35 mins',
        'difficulty': 'Medium',
        'servings': 4,
        'ingredients': ['3 cups broccoli florets', '2 potatoes, diced', '1 onion, chopped', '3 cups vegetable broth', '1 cup milk', '2 tbsp butter', '1/4 cup cheddar cheese, shredded', 'Salt and pepper to taste'],
        'instructions': '1. Melt butter in a pot, sauté onion until translucent. 2. Add potatoes and broth, simmer for 15 minutes. 3. Add broccoli, cook for 10 more minutes. 4. Blend until smooth, return to pot. 5. Stir in milk and cheese until melted. 6. Season with salt and pepper.'
    },
    {
        'id': 5,
        'name': 'Spinach and Feta Omelette',
        'vegetables': ['spinach', 'tomato'],
        'description': 'Protein-packed breakfast with Mediterranean flavors',
        'cook_time': '10 mins',
        'difficulty': 'Easy',
        'servings': 1,
        'ingredients': ['3 eggs', '1 cup fresh spinach', '1/4 cup feta cheese, crumbled', '1 small tomato, diced', '2 tbsp milk', '1 tbsp butter', 'Salt and pepper to taste'],
        'instructions': '1. Beat eggs with milk, salt, and pepper. 2. Melt butter in a non-stick pan over medium heat. 3. Pour in egg mixture. 4. When edges start to set, add spinach, tomato, and feta to one half. 5. Fold omelette in half and cook for 2 more minutes. 6. Slide onto plate and serve.'
    },
    {
        'id': 6,
        'name': 'Green Spinach Smoothie',
        'vegetables': ['spinach'],
        'description': 'Nutrient-dense smoothie that tastes amazing',
        'cook_time': '5 mins',
        'difficulty': 'Easy',
        'servings': 2,
        'ingredients': ['2 cups fresh spinach', '1 banana', '1 cup frozen mango', '1 cup almond milk', '1 tbsp chia seeds', '1 tsp honey (optional)'],
        'instructions': '1. Add all ingredients to a blender. 2. Blend on high speed until smooth and creamy. 3. Add more almond milk if too thick. 4. Pour into glasses and serve immediately.'
    },
    {
        'id': 7,
        'name': 'Roasted Vegetable Medley',
        'vegetables': ['bell pepper', 'zucchini', 'tomato', 'onion'],
        'description': 'Colorful oven-roasted vegetables with herbs',
        'cook_time': '40 mins',
        'difficulty': 'Easy',
        'servings': 4,
        'ingredients': ['2 bell peppers, chopped', '2 zucchini, sliced', '2 cups cherry tomatoes', '1 red onion, cut into wedges', '3 tbsp olive oil', '2 tsp dried herbs (thyme, rosemary)', '3 cloves garlic, minced', 'Salt and pepper to taste'],
        'instructions': '1. Preheat oven to 425°F (220°C). 2. Toss all vegetables with olive oil, garlic, herbs, salt, and pepper. 3. Spread on a baking sheet in a single layer. 4. Roast for 30-35 minutes, stirring halfway through. 5. Serve hot as a side dish or over rice.'
    },
    {
        'id': 8,
        'name': 'Tomato Basil Pasta',
        'vegetables': ['tomato', 'garlic'],
        'description': 'Classic Italian pasta with fresh ingredients',
        'cook_time': '25 mins',
        'difficulty': 'Easy',
        'servings': 4,
        'ingredients': ['1 lb pasta', '4 large tomatoes, diced', '4 cloves garlic, minced', '1/2 cup fresh basil, chopped', '1/4 cup olive oil', '1/4 cup parmesan cheese', 'Red pepper flakes', 'Salt to taste'],
        'instructions': '1. Cook pasta according to package directions. 2. While pasta cooks, heat olive oil in a large pan. 3. Add garlic and red pepper flakes, cook for 1 minute. 4. Add tomatoes and cook for 10 minutes until softened. 5. Toss drained pasta with sauce and fresh basil. 6. Top with parmesan cheese.'
    },
    {
        'id': 9,
        'name': 'Stuffed Bell Peppers',
        'vegetables': ['bell pepper', 'onion', 'tomato'],
        'description': 'Hearty stuffed peppers with rice and vegetables',
        'cook_time': '50 mins',
        'difficulty': 'Medium',
        'servings': 4,
        'ingredients': ['4 bell peppers, tops cut off and seeded', '1 cup cooked rice', '1 onion, diced', '2 tomatoes, diced', '1 cup black beans', '1 cup corn', '1 tsp cumin', '1/2 cup cheese', '2 tbsp olive oil'],
        'instructions': '1. Preheat oven to 375°F (190°C). 2. Sauté onion in olive oil until soft. 3. Mix onion, rice, tomatoes, beans, corn, and cumin. 4. Stuff mixture into bell peppers. 5. Place in baking dish, cover with foil. 6. Bake 35 minutes, top with cheese, bake 5 more minutes.'
    },
    {
        'id': 10,
        'name': 'Garlic Butter Mushrooms',
        'vegetables': ['mushroom', 'garlic'],
        'description': 'Savory mushrooms in rich garlic butter sauce',
        'cook_time': '15 mins',
        'difficulty': 'Easy',
        'servings': 3,
        'ingredients': ['1 lb mushrooms, cleaned and halved', '4 cloves garlic, minced', '3 tbsp butter', '1 tbsp olive oil', '2 tbsp fresh parsley, chopped', '1/4 cup white wine (optional)', 'Salt and pepper to taste'],
        'instructions': '1. Heat butter and olive oil in a large pan. 2. Add mushrooms and cook for 5 minutes until golden. 3. Add garlic and cook for 1 minute. 4. Add white wine if using, cook until evaporated. 5. Season with salt and pepper. 6. Garnish with fresh parsley.'
    },
    {
        'id': 11,
        'name': 'Potato and Leek Soup',
        'vegetables': ['potato', 'onion', 'garlic'],
        'description': 'Classic comfort soup with creamy texture',
        'cook_time': '40 mins',
        'difficulty': 'Easy',
        'servings': 6,
        'ingredients': ['4 large potatoes, diced', '2 leeks, sliced', '1 onion, chopped', '2 cloves garlic, minced', '6 cups vegetable broth', '1 cup cream', '2 tbsp butter', 'Fresh chives for garnish', 'Salt and pepper to taste'],
        'instructions': '1. Melt butter in a large pot, sauté leeks, onion, and garlic until soft. 2. Add potatoes and broth, bring to a boil. 3. Reduce heat and simmer for 25 minutes. 4. Partially blend for chunky texture or fully for smooth. 5. Stir in cream and season. 6. Garnish with chives.'
    },
    {
        'id': 12,
        'name': 'Zucchini Noodles with Pesto',
        'vegetables': ['zucchini', 'garlic'],
        'description': 'Low-carb alternative to pasta with fresh pesto',
        'cook_time': '15 mins',
        'difficulty': 'Easy',
        'servings': 2,
        'ingredients': ['3 medium zucchini, spiralized', '2 cups fresh basil', '1/3 cup pine nuts', '2 cloves garlic', '1/2 cup parmesan cheese', '1/2 cup olive oil', 'Cherry tomatoes for garnish', 'Salt to taste'],
        'instructions': '1. Make pesto: blend basil, pine nuts, garlic, parmesan, and olive oil until smooth. 2. Heat a pan over medium heat. 3. Add zucchini noodles and cook for 2-3 minutes. 4. Remove from heat, toss with pesto. 5. Garnish with cherry tomatoes and extra parmesan.'
    }
]


vegetables_to_recipes = {}
for recipe in recipes_database:
    for veg in recipe['vegetables']:
        if veg not in vegetables_to_recipes:
            vegetables_to_recipes[veg] = []
        vegetables_to_recipes[veg].append(recipe['id'])


all_vegetables = sorted(set(veg for recipe in recipes_database for veg in recipe['vegetables']))

@app.route('/')
def index():
    return render_template('index.html', vegetables=all_vegetables)

@app.route('/suggest', methods=['POST'])
def suggest():
    selected_vegetables = request.json.get('vegetables', [])

    if not selected_vegetables:
        return jsonify([])

    recipe_ids = set()
    for veg in selected_vegetables:
        if veg in vegetables_to_recipes:
            recipe_ids.update(vegetables_to_recipes[veg])

   
    suggestions = [recipe for recipe in recipes_database if recipe['id'] in recipe_ids]

    suggestions.sort(key=lambda r: len(set(r['vegetables']) & set(selected_vegetables)), reverse=True)

    return jsonify(suggestions)

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> 104c3911df3e4995e5b27ba53847c989fee2316d
