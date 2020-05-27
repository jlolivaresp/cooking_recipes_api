from app.service import firebase
from app.model.model_constants import RECIPE_ALL_REF, RECIPE_REF


db = firebase.Firebase('firebase')


class Recipe:

    @staticmethod
    def get_all_recipes():
        return db.get_reference(RECIPE_ALL_REF).get()

    @staticmethod
    def get_recipe(name: str):
        return db.get_reference(RECIPE_REF + '/' + name).get()

    @staticmethod
    def add_recipe(recipe_dict: dict):
        db.get_reference(RECIPE_ALL_REF).update(recipe_dict)

    @staticmethod
    def delete_recipe(name: str):
        recipe_ref = db.get_reference(RECIPE_REF + '/' + name)
        recipe_ref.delete()
