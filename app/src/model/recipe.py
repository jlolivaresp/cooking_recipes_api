from app.src.model.supermarket import Supermarket
from app.src.service import firebase
from app.src.model.model_constants import RECIPES_NODE_REF, RECIPES_SUB_NODE_REF_FORMAT, RECIPE_INGREDIENT_UNIT_REF, \
    RECIPE_INGREDIENT_SUPERMARKET_REF, RECIPE_NEW_INGREDIENTS_REF, RECIPE_SUB_NODE_INGREDIENTS_REF, \
    RECIPE_INGREDIENT_QUANTITY_REF
from app.src.model.ingredient import Ingredient
from app.src.model.unit import Unit
from app.src.utils import value_collector, dict_generator

db = firebase.Firebase("firebase")


class Recipe:
    def __init__(self, name: str = None, description: str = None, link: str = None):
        self.name = name
        self.description = description
        self.link = link
        self.ingredient = Ingredient()
        self.unit = Unit()
        self.supermarket = Supermarket()

        self.attribute_dict = dict(name=self.name, description=self.description, link=self.link)

    @staticmethod
    def get_all_recipes():
        return db.get(RECIPES_NODE_REF)

    @staticmethod
    def get_recipe(recipe_id: str):
        return db.get(RECIPES_SUB_NODE_REF_FORMAT.format(recipe_id))

    def add_recipe(self, recipe_dict: dict):
        # Add new units and supermarkets to the DB
        new_units = value_collector(dict_generator(recipe_dict), RECIPE_INGREDIENT_UNIT_REF)
        self.unit.add_unit(new_units)

        new_supermarkets = value_collector(dict_generator(recipe_dict), RECIPE_INGREDIENT_SUPERMARKET_REF)
        self.supermarket.add_supermarket(new_supermarkets)

        # Add new ingredients to the DB
        if recipe_dict.get(RECIPE_NEW_INGREDIENTS_REF):
            for new_ingredient in recipe_dict.get(RECIPE_NEW_INGREDIENTS_REF):
                quantity = new_ingredient.pop(RECIPE_INGREDIENT_QUANTITY_REF, None)
                unit = new_ingredient.get(RECIPE_INGREDIENT_UNIT_REF)
                new_ingredient_ref = next(iter(self.ingredient.add_ingredient(new_ingredient)))
                new_ingredient_dict = {new_ingredient_ref: {RECIPE_INGREDIENT_UNIT_REF: unit,
                                                            RECIPE_INGREDIENT_QUANTITY_REF: quantity}}
                if recipe_dict.get(RECIPE_SUB_NODE_INGREDIENTS_REF):
                    recipe_dict[RECIPE_SUB_NODE_INGREDIENTS_REF].update(new_ingredient_dict)
                else:
                    recipe_dict[RECIPE_SUB_NODE_INGREDIENTS_REF] = new_ingredient_dict

        recipe_dict.pop(RECIPE_NEW_INGREDIENTS_REF, None)

        # Append new units and supermarkets to <ingredients>.<id>.<unit> and <ingredients>.<id>.<supermarket>
        for ingredient_id, value in recipe_dict.get(RECIPE_SUB_NODE_INGREDIENTS_REF).items():
            self.ingredient.update_ingredient_units(ingredient_id, value.get(RECIPE_INGREDIENT_UNIT_REF))

        recipe_child = db.child("", RECIPES_NODE_REF)

        if recipe_child.get():
            new_post_ref = db.add(RECIPES_NODE_REF, recipe_dict)
        else:
            new_post_ref = recipe_child.push(recipe_dict)
        return {new_post_ref.key: recipe_dict}

    @staticmethod
    def replace_recipe(recipe_dict: dict):
        db.set(RECIPES_NODE_REF, recipe_dict)
        return recipe_dict

    @staticmethod
    def update_recipe(recipe_dict: dict):
        db.update(RECIPES_NODE_REF, recipe_dict)
        return recipe_dict

    @staticmethod
    def delete_recipe(recipe_id: str):
        # TODO Verify this works
        db.delete(RECIPES_SUB_NODE_REF_FORMAT.format(recipe_id))
        return recipe_id
