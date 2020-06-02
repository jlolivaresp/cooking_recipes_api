from flask import request, jsonify
from jsonschema import ValidationError

from app import app
from app.contants import INGREDIENTS_NAME_FORMAT, UNIT_DEFAULT_NAME, UNIT_DEFAULT_VALUE
from app.controller.schema_validations import Schema
from app.model.ingredient import Ingredient
from app.model.recipe import Recipe
from app.service.firebase import ReferenceNotFoundException, ElementAlreadyExistsError
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
            return jsonify(ingredient.get_ingredient(name))

        except ValidationError as e:
            return jsonify(e.message)

        except ReferenceNotFoundException as e:
            return jsonify(e.error_dict)


@app.route('/ingredients/post/single', methods=['POST'])
def add_ingredient():
    try:
        if request.method == 'POST':
            schema.add_ingredient_request_schema(request.get_json())
            return ingredient.add_ingredient(request.get_json())

    except ValidationError as e:
        return jsonify(e.message)

    except ElementAlreadyExistsError as e:
        return jsonify(e.error_dict)


@app.route('/ingredients/delete/single', methods=['POST'])
def delete_ingredient():
    if request.method == 'POST':
        try:
            schema.get_delete_node_request_schema(request.get_json())
            name = request.get_json().get("name")
            return jsonify(ingredient.delete_ingredient(name))

        except ValidationError as e:
            return jsonify(e.message)

        except ElementAlreadyExistsError as e:
            return jsonify(e.error_dict)


@app.route('/recipes/get/all', methods=['GET'])
def get_all_recipes():
    return jsonify(recipe.get_all_recipes())


@app.route('/recipes/get/single/', methods=['POST'])
def get_recipe():
    if request.method == 'POST':
        try:
            schema.get_delete_node_request_schema(request.get_json())
            name = request.get_json().get("name")
            return jsonify(recipe.get_recipe(name))

        except ValidationError as e:
            return jsonify(e.message)

        except ReferenceNotFoundException as e:
            return jsonify(e.error_dict)


@app.route('/recipes/post/single', methods=['POST'])
def add_recipe(recipes_dict: dict = None):
    if request.method == 'POST':
        if recipes_dict:
            req_json = recipes_dict
        else:
            req_json = request.get_json()

        if len(req_json) == 1:
            try:
                schema.add_recipe_request_schema(req_json)

                # Add the missing ingredients to the ingredients node
                for ing in req_json.get(*req_json).get(INGREDIENTS_NAME_FORMAT):
                    ing_dict = {
                        ing: {
                            UNIT_DEFAULT_NAME: UNIT_DEFAULT_VALUE
                        }
                    }
                    schema.add_ingredient_request_schema(ing_dict)
                    try:
                        ingredient.add_ingredient(ing_dict)
                    except ElementAlreadyExistsError as e:
                        continue

                return jsonify(recipe.add_recipe(req_json))

            except ValidationError as e:
                return jsonify(e)

            except ElementAlreadyExistsError as e:
                return jsonify(e.error_dict)

        else:
            # TODO fix return | return valid view if method not POST
            return ""


@app.route('/recipes/delete/single', methods=['POST'])
def delete_recipe():
    if request.method == 'POST':
        try:
            schema.get_delete_node_request_schema(request.get_json())
            name = request.get_json().get("name")

            return jsonify(recipe.delete_recipe(name))

        except ValidationError as e:
            return jsonify(e.message)

        except ReferenceNotFoundException as e:
            return jsonify(e.error_dict)


@app.route('/recipes/get/ingredients/summary', methods=['POST'])
def summarize_selected_recipes_ingredients():
    recipe_sub_dict = dict()

    if request.method == 'POST':
        try:
            schema.summarize_selected_recipes_ingredients(request.get_json())
            for name in request.get_json().get("recipe_list"):
                selected_recipe = dict(name=recipe.get_recipe(name))
                recipe_sub_dict = dict(**recipe_sub_dict, **selected_recipe)

            return jsonify(_dict_counter(recipe_sub_dict, "ingredients"))

        except ValidationError as e:
            return jsonify(e.message)


@app.route('/recipes/post/from_local/ods', methods=['POST'])
def add_recipes_from_local_ods():
    if request.method == 'POST':
        req_json = request.get_json()

        path = req_json.get("path")
        sheet_name = req_json.get("sheet")
        recipes_dict = ods_parser(path, sheet_name)

        for key, value in recipes_dict.items():
            add_recipe({key: value})

        return jsonify(recipes_dict)
