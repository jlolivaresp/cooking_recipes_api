import os

from flask import request, jsonify, render_template, send_from_directory
from jsonschema import ValidationError

from app import app
from app.contants import INGREDIENTS_NAME_FORMAT, UNIT_DEFAULT_NAME, UNIT_DEFAULT_VALUE
from app.controller.schema_validations import ModelSchema
from app.model.ingredient import Ingredient
from app.model.recipe import Recipe
from app.service.firebase import ReferenceNotFoundException, ElementAlreadyExistsError, update_node_array_formatter
from app.utils import _dict_counter, ods_to_dict

ingredient = Ingredient()
recipe = Recipe()
model_schema = ModelSchema()


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
@app.route('/index')
def index():
    return render_template("API_documentation.html")


@app.route('/ingredients', methods=['GET'])
def get_all_ingredients():
    try:
        return jsonify(ingredient.get_all_ingredients())
    except ReferenceNotFoundException as e:
        return jsonify(e.error_dict)


@app.route('/ingredients/get', methods=['POST', 'GET'])
def get_ingredient(_ingredient_id: str = None):
    if _ingredient_id:
        ingredient_id = _ingredient_id
    elif request.method == 'POST':
        ingredient_id = request.get_json().get("id")
    elif request.method == 'GET':
        ingredient_id = request.args.get("id")
    else:
        ingredient_id = ""

    try:
        model_schema.get_delete_node_request_schema(request.get_json())
        return jsonify(ingredient.get_ingredient(ingredient_id))

    except ValidationError as e:
        return jsonify(e.message)

    except ReferenceNotFoundException as e:
        return jsonify(e.error_dict)


@app.route('/ingredients/add', methods=['POST'])
def add_ingredient(ingredients_dict: dict = None):
    try:
        if ingredients_dict:
            req_json = ingredients_dict
        else:
            req_json = request.get_json()

        if request.method == 'POST':
            model_schema.add_ingredient_request_schema(req_json)
            return ingredient.add_ingredient(req_json)

    except ValidationError as e:
        return jsonify(e.message)

    except ElementAlreadyExistsError as e:
        return jsonify(e.error_dict)


@app.route('/ingredients/update', methods=['PUT'])
def update_ingredient(ingredients_dict: dict = None):
    try:
        if ingredients_dict:
            req_json = ingredients_dict
        else:
            req_json = request.get_json()

        old = ingredient.get_ingredient(*req_json)
        update_dict = update_node_array_formatter(str(*req_json), old, req_json.get(*req_json))
        model_schema.update_node_field_request_schema(update_dict)
        return ingredient.update_ingredient(update_dict)

    except ValidationError as e:
        return jsonify(e.message)

    except ElementAlreadyExistsError as e:
        return jsonify(e.error_dict)


@app.route('/ingredients/delete', methods=['DELETE'])
def delete_ingredient():
    if request.method == 'DELETE':
        try:
            model_schema.get_delete_node_request_schema(request.get_json())
            ingredient_id = request.get_json().get("id")
            return jsonify(ingredient.delete_ingredient(ingredient_id))

        except ValidationError as e:
            return jsonify(e.message)

        except ElementAlreadyExistsError as e:
            return jsonify(e.error_dict)


@app.route('/recipes/get', methods=['GET'])
def get_all_recipes():
    try:
        return jsonify(recipe.get_all_recipes())
    except ReferenceNotFoundException as e:
        return jsonify(e.error_dict)


@app.route('/recipes/get', methods=['POST', 'GET'])
def get_recipe(_recipe_id: str = None):
    if _recipe_id:
        recipe_id = _recipe_id
    elif request.method == 'POST':
        recipe_id = request.get_json().get("id")
    elif request.method == 'GET':
        recipe_id = request.args.get("id")
    else:
        recipe_id = ""

    try:
        model_schema.get_delete_node_request_schema(request.get_json())
        return jsonify(recipe.get_recipe(recipe_id))

    except ValidationError as e:
        return jsonify(e.message)

    except ReferenceNotFoundException as e:
        return jsonify(e.error_dict)


@app.route('/recipes/add', methods=['POST'])
def add_recipe(recipes_dict: dict = None, add_ingredients: bool = True):
    if request.method == 'POST':
        if recipes_dict:
            req_json = recipes_dict
        else:
            req_json = request.get_json()

        try:
            model_schema.add_recipe_request_schema(req_json)

            # Add the missing ingredients to the ingredients node
            if add_ingredients:
                for ing in req_json.get(*req_json).get(INGREDIENTS_NAME_FORMAT):
                    ing_dict = {
                        ing: {
                            UNIT_DEFAULT_NAME: UNIT_DEFAULT_VALUE
                        }
                    }
                    model_schema.add_ingredient_request_schema(ing_dict)
                    try:
                        ingredient.add_ingredient(ing_dict)
                    except ElementAlreadyExistsError as e:
                        continue

            return jsonify(recipe.add_recipe(req_json))

        except ValidationError as e:
            return jsonify(e)

        except ElementAlreadyExistsError as e:
            return jsonify(e.error_dict)


@app.route('/recipes/delete', methods=['POST'])
def delete_recipe():
    if request.method == 'POST':
        try:
            model_schema.get_delete_node_request_schema(request.get_json())
            name = request.get_json().get("name")

            return jsonify(recipe.delete_recipe(name))

        except ValidationError as e:
            return jsonify(e.message)

        except ReferenceNotFoundException as e:
            return jsonify(e.error_dict)


@app.route('/recipe/update', methods=['POST'])
def update_recipe(recipe_dict: dict = None):
    try:
        if recipe_dict:
            req_json = recipe_dict
        else:
            req_json = request.get_json()

        old = recipe.get_recipe(*req_json)
        update_dict = update_node_array_formatter(str(*req_json), old, req_json.get(*req_json))
        model_schema.update_node_field_request_schema(update_dict)
        return recipe.update_recipe(update_dict)

    except ValidationError as e:
        return jsonify(e.message)

    except ElementAlreadyExistsError as e:
        return jsonify(e.error_dict)


@app.route('/recipes/get/ingredients/summary', methods=['POST'])
def summarize_selected_recipes_ingredients():
    recipe_sub_dict = dict()

    if request.method == 'POST':
        try:
            model_schema.summarize_selected_recipes_ingredients(request.get_json())
            for name in request.get_json().get("recipe_list"):
                selected_recipe = {name: recipe.get_recipe(name)}
                recipe_sub_dict = dict(**recipe_sub_dict, **selected_recipe)

            ingredients_summary_dict = _dict_counter(recipe_sub_dict, "ingredients")

            for ing in ingredients_summary_dict:
                # ing_json = {ing: get_ingredient(ing).get_json()}
                ingredients_summary_dict[ing] = str(ingredients_summary_dict.get(ing)) \
                                                + " {}".format(get_ingredient(ing).get_json().get("dimension"))

            return jsonify(ingredients_summary_dict)

        except ValidationError as e:
            return jsonify(e.message)


@app.route('/recipes/post/from_local/ods', methods=['POST'])
def add_recipes_from_local_ods():
    if request.method == 'POST':
        req_json = request.get_json()

        path = req_json.get("path")
        recipes_dict, ingredients_dict = ods_to_dict(path)

        for key, value in recipes_dict.items():
            add_recipe({key: value})

        for key, value in ingredients_dict.items():
            add_ingredient({key: value})

        return jsonify(recipes_dict, ingredients_dict)
