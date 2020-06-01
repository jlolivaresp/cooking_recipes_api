from flask import request, jsonify
from jsonschema import ValidationError

from app import app
from app.contants import INGREDIENTS_NAME_FORMAT, UNIT_DEFAULT_NAME, UNIT_DEFAULT_VALUE
from app.controller.schema_validations import Schema
from app.model.ingredients import Ingredient
from app.model.recipes import Recipe
from app.utils import _dict_counter, ods_parser

ingredient = Ingredient()
recipe = Recipe()
schema = Schema()


@app.route('/')
@app.route('/index')
def index():
    return jsonify("Groceries Project")


@app.route('/ingredients/get/all', methods=['GET'])
def get_all_ingredients():
    return jsonify(ingredient.get_all_ingredients())


@app.route('/ingredients/get/single', methods=['POST'])
def get_ingredient():
    if request.method == 'POST':
        try:
            schema.get_delete_node_request_schema(request.get_json())
            name = request.get_json().get("name")
            return ingredient.get_ingredient(name)
        except ValidationError as e:
            return jsonify(e.message)


@app.route('/ingredients/post/single', methods=['POST'])
def add_ingredient():
    try:
        if request.method == 'POST':
            schema.add_ingredient_request_schema(request.get_json())
            ingredient.add_ingredient(request.get_json())
            return request.get_json()
    except ValidationError as e:
        return jsonify(e.message)


@app.route('/ingredients/delete/single', methods=['POST'])
def delete_ingredient():
    if request.method == 'POST':
        try:
            schema.get_delete_node_request_schema(request.get_json())
            name = request.get_json().get("name")
            ingredient.delete_ingredient(name)
            return request.get_json()
        except ValidationError as e:
            return jsonify(e.message)


@app.route('/recipes/get/all', methods=['GET'])
def get_all_recipes():
    return jsonify(recipe.get_all_recipes())


@app.route('/recipes/get/single/', methods=['POST'])
def get_recipe():
    if request.method == 'POST':
        try:
            schema.get_delete_node_request_schema(request.get_json())
            name = request.get_json("name")
            return recipe.get_recipe(name)
        except ValidationError as e:
            return jsonify(e.message)


@app.route('/recipes/post/single', methods=['POST'])
def add_recipe():
    if request.method == 'POST':
        req_json = request.get_json()
        if len(req_json) == 1:
            try:
                schema.add_recipe_request_schema(req_json)
                recipe.add_recipe(req_json)
            except ValidationError as e:
                return jsonify(e)

            # Add the missing ingredients to the ingredients node
            for ing in req_json.get(*req_json).get(INGREDIENTS_NAME_FORMAT):
                try:
                    ing_dict = {
                        ing: {
                            UNIT_DEFAULT_NAME: UNIT_DEFAULT_VALUE
                        }
                    }
                    schema.add_ingredient_request_schema(ing_dict)
                    ingredient.add_ingredient(ing_dict)
                except NameError as e:
                    return e
                except ValidationError as e:
                    return e.message
            return jsonify(req_json)
        else:
            # TODO fix return | return valid view if method not POST
            return ""


@app.route('/recipes/delete/single', methods=['POST'])
def delete_recipe():
    if request.method == 'POST':
        try:
            schema.get_delete_node_request_schema(request.get_json())
            name = request.get_json().get("name")
            recipe.delete_recipe(name)
            return request.get_json()
        except ValidationError as e:
            return jsonify(e.message)


@app.route('/ingredients/summarize/recipes/', methods=['POST'])
def summarize_selected_recipes_ingredients():
    recipe_sub_dict = dict()

    if request.method == 'POST':
        for name in request.get_json().get("recipe_list"):
            selected_recipe = {name: recipe.get_recipe(name)}
            recipe_sub_dict = dict(**recipe_sub_dict, **selected_recipe)

        return jsonify(_dict_counter(recipe_sub_dict, "ingredients"))


@app.route('/recipes/add/from_local/ods', methods=['POST'])
def add_recipes_from_local_ods():
    if request.method == 'POST':
        req_json = request.get_json()

        path = req_json.get("path")
        sheet_name = req_json.get("sheet")
        recipes_dict = ods_parser(path, sheet_name)
        recipe.set_multiple_nodes(recipes_dict)

        # Add the missing ingredients to the ingredients node
        for rec in recipes_dict:
            # TODO this is gonna overwrite the unit value of every ingredient. Fix this
            for ing in recipes_dict.get(rec).get(INGREDIENTS_NAME_FORMAT):
                ing_dict = {
                    ing: {
                        UNIT_DEFAULT_NAME: UNIT_DEFAULT_VALUE
                    }
                }
                try:
                    schema.add_ingredient_request_schema(ing_dict)
                    ingredient.add_ingredient(ing_dict)
                except NameError as e:
                    return jsonify(e.__str__())
                except ValidationError as e:
                    return jsonify(e.message)
        return jsonify(recipes_dict)
