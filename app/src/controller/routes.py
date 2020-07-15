import os
from collections import Counter

from flask import request, jsonify, render_template, send_from_directory
from jsonschema import ValidationError

from app import app
from app.src.controller.schema_validations import ModelSchema, ApiSchema
from app.src.errors import validation_error, reference_not_found_error, element_already_exists_error
from app.src.model.ingredient import Ingredient
from app.src.model.model_constants import NEW_UNIT_REF, NEW_SUPERMARKET_REF, GENERAL_ID_REF, RECIPE_SUB_NODE_INGREDIENTS_REF, \
    INGREDIENTS_SUB_NODE_NAME_REF, RECIPE_INGREDIENT_UNIT_REF, RECIPE_INGREDIENT_QUANTITY_REF, RECIPE_IDS_REF
from app.src.model.recipe import Recipe
from app.src.model.unit import Unit
from app.src.model.supermarket import Supermarket
from app.src.service.firebase import ReferenceNotFoundException, ElementAlreadyExistsError, update_node_array_formatter
from app.src.utils import ods_to_dict

ingredient = Ingredient()
recipe = Recipe()
unit = Unit()
model_schema = ModelSchema()
api_schema = ApiSchema()
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
            api_schema.add_or_delete_new_unit_request_schema(request.get_json())
            req_json = request.get_json().get(NEW_UNIT_REF)

            return unit.add_unit(req_json), 201

        elif request.method == 'DELETE':
            api_schema.add_or_delete_new_unit_request_schema(request.get_json())
            req_json = request.get_json().get(NEW_UNIT_REF)

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
            api_schema.add_or_delete_new_supermarket_request_schema(request.get_json())
            req_json = request.get_json().get(NEW_SUPERMARKET_REF)

            return supermarket.add_supermarket(req_json), 201

        elif request.method == 'DELETE':
            api_schema.add_or_delete_new_supermarket_request_schema(request.get_json())
            req_json = request.get_json().get(NEW_SUPERMARKET_REF)

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
def ingredients_single():
    try:
        if request.method == 'POST':
            ingredient_dict = request.get_json()
            model_schema.add_ingredient_request_schema(ingredient_dict)
            return jsonify(ingredient.add_ingredient(ingredient_dict)), 201

        elif request.method == 'GET':
            model_schema.get_delete_node_request_schema(request.args)
            ingredient_id = request.args.get(GENERAL_ID_REF)
            return jsonify(ingredient.get_ingredient(ingredient_id))

        elif request.method == 'PUT':
            req_json = request.get_json()

            old = ingredient.get_ingredient(*req_json)
            update_dict = update_node_array_formatter(str(*req_json), old, req_json.get(*req_json))
            model_schema.update_node_field_request_schema(update_dict)
            return ingredient.update_ingredient(update_dict)

        elif request.method == 'DELETE':
            model_schema.get_delete_node_request_schema(request.get_json())
            ingredient_id = request.get_json().get(GENERAL_ID_REF)
            return jsonify(ingredient.delete_ingredient(ingredient_id))

    except ValidationError as e:
        return validation_error(e)

    except ReferenceNotFoundException as e:
        return reference_not_found_error(e)

    except ElementAlreadyExistsError as e:
        return element_already_exists_error(e)


@app.route('/recipes/all', methods=['GET'])
def recipes_all():
    try:
        return jsonify(recipe.get_all_recipes())

    except ReferenceNotFoundException as e:
        return reference_not_found_error(e)


@app.route('/recipes/single', methods=['POST', 'GET', 'PUT', 'DELETE'])
def recipes_single():
    try:
        if request.method == 'POST':
            recipe_dict = request.get_json()
            model_schema.add_recipe_request_schema(recipe_dict)
            return jsonify(recipe.add_recipe(recipe_dict)), 201

        elif request.method == 'GET':
            model_schema.get_delete_node_request_schema(request.args)
            recipe_id = request.args.get(GENERAL_ID_REF)
            return jsonify(recipe.get_recipe(recipe_id))

        elif request.method == 'PUT':
            req_json = request.get_json()
            # TODO validate
            # model_schema.update_node_field_request_schema(req_json)
            return recipe.update_recipe(req_json)

        elif request.method == 'DELETE':
            model_schema.get_delete_node_request_schema(request.get_json())
            recipe_id = request.get_json().get(GENERAL_ID_REF)
            return jsonify(recipe.delete_recipe(recipe_id))

        else:
            recipe_id = ""

        model_schema.get_delete_node_request_schema(request.get_json())
        return jsonify(recipe.get_recipe(recipe_id))

    except ValidationError as e:
        return validation_error(e)

    except ReferenceNotFoundException as e:
        return reference_not_found_error(e)

    except ElementAlreadyExistsError as e:
        return jsonify(e.error_dict)


@app.route('/recipes/summary', methods=['POST'])
def recipes_summary():
    try:
        if request.method == 'POST':
            # Validate request schema
            model_schema.summarize_selected_recipes_ingredients(request.get_json())

            # Extract the list of recipe id's from the request
            recipes_id_list = request.get_json().get(RECIPE_IDS_REF)

            # Define a Counter object to add recipe's ingredients in common
            counter = Counter()

            # For every selected recipe in the request
            for recipe_id in recipes_id_list:

                # Get that recipe's ingredients
                recipe_ingredients = recipe.get_recipe(recipe_id).get(RECIPE_SUB_NODE_INGREDIENTS_REF)

                # And convert that dictionary of dictionaries into a list of dictionaries
                # It's easier to add the common ingredients' quantities this way
                recipe_ingredients_list = [
                    {
                        # Since every ingredient in a recipe has an unit
                        # Make a concatenated key from <<ingredient_id> <unit>>
                        "{} {}".format(ingredient_id,
                                       value.get(RECIPE_INGREDIENT_UNIT_REF)): value.get(RECIPE_INGREDIENT_QUANTITY_REF)
                    }
                    for ingredient_id, value in recipe_ingredients.items()
                ]

                # Add quantities for every <<ingredient_id> <unit>> pair
                for ingredient_id_quantity_pair in recipe_ingredients_list:
                    counter.update(ingredient_id_quantity_pair)

            # Make a copy of the Counter dict to avoid iterative modification over the same object
            counter_copy = counter.copy()

            # Pull all the ingredients from the DB to get their names later on
            all_ingredients = ingredient.get_all_ingredients()

            # For every <<ingredient_id> <unit>> pair, replace <ingredient_id> for <ingredient_name>
            for key, value in counter.items():
                # Get the <ingredient_id> and its unit
                ingredient_id_from_recipe, unit = key.split(" ")

                # Get the reference for that id in the ingredients node from the DB
                ingredients_recipe_id_ref = all_ingredients.get(ingredient_id_from_recipe)

                # If the <ingredient_id> is in the node reference
                if ingredients_recipe_id_ref:
                    # Get its name
                    ingredient_name = ingredients_recipe_id_ref.get(INGREDIENTS_SUB_NODE_NAME_REF)

                    # Replace <ingredient_id> for <ingredient_name>
                    counter_copy["{} {}".format(ingredient_name, unit)] = counter_copy.pop(key)

            return jsonify(counter_copy)

    except ValidationError as e:
        return jsonify(e)
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
