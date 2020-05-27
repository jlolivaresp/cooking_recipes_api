from collections import Counter
from flask import request, jsonify

from app import app
from app.model.ingredients import Ingredient
from app.model.recipes import Recipe


ingredient = Ingredient()
recipe = Recipe()


@app.route('/')
def index():
    return "Groceries Project"


@app.route('/ingredients/all', methods=['GET'])
def get_all_ingredients():
    return ingredient.get_all_ingredients()


@app.route('/ingredients/single', methods=['POST'])
def get_ingredient():
    if request.method == 'POST':
        name = request.get_json().get("name")
        return ingredient.get_ingredient(name)


@app.route('/ingredients/add', methods=['POST'])
def add_ingredient():
    if request.method == 'POST':
        ingredient.add_ingredient(request.get_json())
        return request.get_json()


@app.route('/ingredients/delete', methods=['POST'])
def delete_ingredient():
    if request.method == 'POST':
        name = request.get_json().get("name")
        ingredient.delete_ingredient(name)
        return request.get_json()


@app.route('/recipes/all', methods=['GET'])
def get_all_recipes():
    return recipe.get_all_recipes()


@app.route('/recipes/single', methods=['POST'])
def get_recipe():
    if request.method == 'POST':
        name = request.get_json("name")
        return recipe.get_recipe(name)


@app.route('/recipes/add', methods=['POST'])
def add_recipe():
    if request.method == 'POST':
        recipe.add_recipe(request.get_json())
        return request.get_json()


@app.route('/recipes/delete', methods=['POST'])
def delete_recipe():
    if request.method == 'POST':
        name = request.get_json().get("name")
        recipe.delete_recipe(name)
        return request.get_json()


@app.route('/ingredients/summarize', methods=['GET'])
def total_ingredients_list():
    all_recipes = get_all_recipes()
    print(all_recipes)
    r_dict = Counter(dict())
    for r in all_recipes:
        r_dict += Counter(all_recipes.get(r).get("ingredients"))
    return jsonify(r_dict)
