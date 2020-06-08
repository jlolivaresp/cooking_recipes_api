from app.service import firebase
from app.model.model_constants import RECIPE_ALL_REF, RECIPE_REF

db = firebase.Firebase('firebase')


class Recipe:
    def __init__(self, name: str = None, description: str = None, link: str = None):
        self.name = name
        self.description = description
        self.link = link

        self.attribute_dict = dict(name=self.name, description=self.description, link=self.link)

    @staticmethod
    def get_all_recipes():
        return db.get(RECIPE_ALL_REF)

    @staticmethod
    def get_recipe(recipe_id: str):
        return db.get(RECIPE_REF.format(recipe_id))

    @staticmethod
    def add_recipe(recipe_dict: dict):
        db.add(RECIPE_ALL_REF, recipe_dict)
        return recipe_dict

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
