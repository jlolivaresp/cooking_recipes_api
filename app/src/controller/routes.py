import os

from flask import request, jsonify, render_template, send_from_directory
from jsonschema import ValidationError

from app import app
from app.src.contants import INGREDIENTS_NAME_FORMAT, UNIT_DEFAULT_NAME, UNIT_DEFAULT_VALUE
from app.src.controller.schema_validations import ModelSchema
from app.src.errors import validation_error, reference_not_found_error, element_already_exists_error
from app.src.model.ingredient import Ingredient
from app.src.model.recipe import Recipe
from app.src.model.unit import Unit
from app.src.model.supermarket import Supermarket
from app.src.service.firebase import ReferenceNotFoundException, ElementAlreadyExistsError, update_node_array_formatter
from app.src.utils import _dict_counter, ods_to_dict

ingredient = Ingredient()
recipe = Recipe()
unit = Unit()
model_schema = ModelSchema()
supermarket = Supermarket()


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
@app.route('/index')
def index():
    return render_template("API_documentation.html")


@app.route('/units', methods=['GET', 'POST', 'DELETE'])
def units():
    try:
        if request.method == 'GET':
            return jsonify(unit.get_unit_list())

        elif request.method == 'POST':
            req_json = request.get_json().get('unit')

            return unit.add_unit(req_json), 201

        elif request.method == 'DELETE':
            req_json = request.get_json().get('unit')

            return jsonify(unit.delete_unit(req_json))

    except ValidationError as e:
        return validation_error(e)

    except ReferenceNotFoundException as e:
        return reference_not_found_error(e)


@app.route('/supermarkets', methods=['GET', 'POST', 'DELETE'])
def supermarkets():
    try:
        if request.method == 'GET':
            return jsonify(supermarket.get_supermarket_list())

        elif request.method == 'POST':
            req_json = request.get_json().get('unit')

            return supermarket.add_supermarket(req_json), 201

        elif request.method == 'DELETE':
            req_json = request.get_json().get('unit')

            return jsonify(supermarket.delete_supermarket(req_json))

    except ValidationError as e:
        return validation_error(e)

    except ReferenceNotFoundException as e:
        return reference_not_found_error(e)


@app.route('/ingredients/all', methods=['GET'])
def ingredients_all():
    try:
        return ingredient.get_all_ingredients()

    except ReferenceNotFoundException as e:
        return reference_not_found_error(e)


@app.route('/ingredients/single', methods=['POST', 'GET', 'PUT', 'DELETE'])
def ingredients_single(_ingredient_id: str = None):
    try:
        if _ingredient_id:
            ingredient_id = _ingredient_id

        elif request.method == 'POST':
            ingredient_id = request.get_json().get("id")

        elif request.method == 'GET':
            ingredient_id = request.args.get("id")

        elif request.method == 'PUT':
            req_json = request.get_json()

            old = ingredient.get_ingredient(*req_json)
            update_dict = update_node_array_formatter(str(*req_json), old, req_json.get(*req_json))
            model_schema.update_node_field_request_schema(update_dict)
            return ingredient.update_ingredient(update_dict)

        elif request.method == 'DELETE':
            model_schema.get_delete_node_request_schema(request.get_json())
            ingredient_id = request.get_json().get("id")
            return jsonify(ingredient.delete_ingredient(ingredient_id))

        else:
            ingredient_id = ""

        model_schema.get_delete_node_request_schema(request.get_json())
        return jsonify(ingredient.get_ingredient(ingredient_id))

    except ValidationError as e:
        return validation_error(e)

    except ReferenceNotFoundException as e:
        return reference_not_found_error(e)


@app.route('/ingredients/new', methods=['POST'])
def ingredients_new(ingredients_dict: dict = None):
    try:
        if ingredients_dict:
            req_json = ingredients_dict
        else:
            req_json = request.get_json()

        if request.method == 'POST':
            model_schema.add_ingredient_request_schema(req_json)
            return ingredient.add_ingredient(req_json), 201

    except ValidationError as e:
        return validation_error(e)

    except ElementAlreadyExistsError as e:
        return element_already_exists_error(e)


@app.route('/recipes/all', methods=['GET'])
def recipes_all():
    try:
        return jsonify(recipe.get_all_recipes())

    except ReferenceNotFoundException as e:
        return reference_not_found_error(e)


@app.route('/recipes/single', methods=['POST', 'GET', 'PUT', 'DELETE'])
def recipes_single(_recipe_id: str = None):
    try:
        if _recipe_id:
            recipe_id = _recipe_id

        elif request.method == 'POST':
            recipe_id = request.get_json().get("id")

        elif request.method == 'GET':
            recipe_id = request.args.get("id")

        elif request.method == 'PUT':
            req_json = request.get_json()

            old = recipe.get_recipe(*req_json)
            update_dict = update_node_array_formatter(str(*req_json), old, req_json.get(*req_json))
            model_schema.update_node_field_request_schema(update_dict)
            return recipe.update_recipe(update_dict)

        elif request.method == 'DELETE':
            # TODO validate request
            recipe_id = request.get_json().get("id")
            return jsonify(recipe.delete_recipe(recipe_id))

        else:
            recipe_id = ""

        model_schema.get_delete_node_request_schema(request.get_json())
        return jsonify(recipe.get_recipe(recipe_id))

    except ValidationError as e:
        return validation_error(e)

    except ReferenceNotFoundException as e:
        return reference_not_found_error(e)


@app.route('/recipes/new', methods=['POST'])
def recipes_new(recipes_dict: dict = None):
    if request.method == 'POST':
        if recipes_dict:
            req_json = recipes_dict
        else:
            req_json = request.get_json()

        try:
            model_schema.add_recipe_request_schema(req_json)

            return recipe.add_recipe(req_json), 201

        except ValidationError as e:
            return jsonify(e)

        except ElementAlreadyExistsError as e:
            return jsonify(e.error_dict)


# @app.route('/recipes/summary', methods=['POST'])
# def summarize_selected_recipes_ingredients():
#     recipe_sub_dict = dict()
#
#     if request.method == 'POST':
#         try:
#             model_schema.summarize_selected_recipes_ingredients(request.get_json())
#             for name in request.get_json().get("recipe_list"):
#                 selected_recipe = {name: recipe.get_recipe(name)}
#                 recipe_sub_dict = dict(**recipe_sub_dict, **selected_recipe)
#
#             ingredients_summary_dict = _dict_counter(recipe_sub_dict, "ingredients")
#
#             for ing in ingredients_summary_dict:
#                 # ing_json = {ing: get_ingredient(ing).get_json()}
#                 ingredients_summary_dict[ing] = str(ingredients_summary_dict.get(ing)) \
#                                                 + " {}".format(get_ingredient(ing).get_json().get("dimension"))
#
#             return jsonify(ingredients_summary_dict)
#
#         except ValidationError as e:
#             return jsonify(e.message)
#
#
# @app.route('/recipes/post/from_local/ods', methods=['POST'])
# def add_recipes_from_local_ods():
#     if request.method == 'POST':
#         req_json = request.get_json()
#
#         path = req_json.get("path")
#         recipes_dict, ingredients_dict = ods_to_dict(path)
#
#         for key, value in recipes_dict.items():
#             add_recipe({key: value})
#
#         for key, value in ingredients_dict.items():
#             add_ingredient({key: value})
#
#         return jsonify(recipes_dict, ingredients_dict)
