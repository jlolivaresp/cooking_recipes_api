from app.service import firebase
from app.model.model_constants import RECIPE_ALL_REF, RECIPE_REF

db = firebase.Firebase('firebase')


class Recipe:

    @staticmethod
    def get_all_recipes():
        return db.get(RECIPE_ALL_REF)

    @staticmethod
    def get_recipe(name: str):
        return db.get(RECIPE_REF.format(name))

    @staticmethod
    def add_recipe(recipe_dict: dict):
        db.add(RECIPE_ALL_REF, recipe_dict)
        return recipe_dict

    def add_multiple_recipes(self, recipes_dict: dict):
        for recipe, ingredients in recipes_dict.items():
            self.add_recipe({recipe: ingredients})
        return recipes_dict

    @staticmethod
    def replace_recipe(recipe_dict: dict):
        db.set(RECIPE_ALL_REF, recipe_dict)
        return recipe_dict

    @staticmethod
    def update_recipe(recipe_dict: dict):
        db.update(RECIPE_ALL_REF, recipe_dict)
        return recipe_dict

    @staticmethod
    def delete_recipe(name: str):
        # TODO Verify this works
        db.delete(RECIPE_REF.format(name))
        return name
