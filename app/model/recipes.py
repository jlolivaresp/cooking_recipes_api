from app.service import firebase
from app.model.model_constants import RECIPE_ALL_REF, RECIPE_REF

db = firebase.Firebase('firebase')


class Recipe:

    @staticmethod
    def get_all_recipes():
        return db.get_reference(RECIPE_ALL_REF).get()

    @staticmethod
    def get_recipe(name: str):
        return db.get_reference(RECIPE_REF.format(name)).get()

    @staticmethod
    def add_recipe(recipe_dict: dict):
        # Check if the recipe already exists
        if not db.get_reference(RECIPE_ALL_REF).child(*recipe_dict).get():
            db.get_reference(RECIPE_ALL_REF).update(recipe_dict)
        else:
            raise NameError('The element already exists in the database')

    @staticmethod
    def delete_recipe(name: str):
        recipe_ref = db.get_reference(RECIPE_REF.format(name))
        recipe_ref.delete()
