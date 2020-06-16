from app.src.model.supermarket import Supermarket
from app.src.service import firebase
from app.src.model.model_constants import RECIPE_ALL_REF, RECIPE_REF
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
        return db.get(RECIPE_ALL_REF)

    @staticmethod
    def get_recipe(recipe_id: str):
        return db.get(RECIPE_REF.format(recipe_id))

    def add_recipe(self, recipe_dict: dict):
        # Add new units and supermarkets to the DB
        new_units = value_collector(dict_generator(recipe_dict), "unit")
        self.unit.add_unit(new_units)

        new_supermarkets = value_collector(dict_generator(recipe_dict), "supermarket")
        self.supermarket.add_supermarket(new_supermarkets)

        # Add new ingredients to the DB
        if recipe_dict.get("new_ingredients"):
            for new_ingredient in recipe_dict.get("new_ingredients"):
                quantity = new_ingredient.pop("quantity", None)
                unit = new_ingredient.get("unit")
                new_ingredient_ref = next(iter(self.ingredient.add_ingredient(new_ingredient)))
                new_ingredient_dict = {new_ingredient_ref: {"unit": unit, "quantity": quantity}}
                if recipe_dict.get("ingredients"):
                    recipe_dict["ingredients"].update(new_ingredient_dict)
                else:
                    recipe_dict["ingredients"] = new_ingredient_dict

        recipe_dict.pop("new_ingredients", None)

        # Append new units and supermarkets to <ingredients>.<id>.<unit> and <ingredients>.<id>.<supermarket>
        for ingredient_id, value in recipe_dict.get("ingredients").items():
            self.ingredient.update_ingredient_units(ingredient_id, value.get("unit"))

        recipe_child = db.child("", RECIPE_ALL_REF)

        if recipe_child.get():
            new_post_ref = db.add(RECIPE_ALL_REF, recipe_dict)
        else:
            new_post_ref = recipe_child.push(recipe_dict)
        return {new_post_ref.key: recipe_dict}

    @staticmethod
    def replace_recipe(recipe_dict: dict):
        db.set(RECIPE_ALL_REF, recipe_dict)
        return recipe_dict

    @staticmethod
    def update_recipe(recipe_dict: dict):
        db.update(RECIPE_ALL_REF, recipe_dict)
        return recipe_dict

    @staticmethod
    def delete_recipe(recipe_id: str):
        # TODO Verify this works
        db.delete(RECIPE_REF.format(recipe_id))
        return recipe_id
