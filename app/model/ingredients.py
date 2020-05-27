from app.service import firebase
from app.model.model_constants import INGREDIENT_ALL_REF, INGREDIENT_REF


db = firebase.Firebase('firebase')


class Ingredient:

    @staticmethod
    def get_all_ingredients():
        return db.get_reference(INGREDIENT_ALL_REF).get()

    @staticmethod
    def get_ingredient(name: str):
        return db.get_reference(INGREDIENT_REF.format(name)).get()

    @staticmethod
    def add_ingredient(ingredient_dict: dict):
        db.get_reference(INGREDIENT_ALL_REF).update(ingredient_dict)

    @staticmethod
    def delete_ingredient(name: str):
        ingredient_ref = db.get_reference(INGREDIENT_ALL_REF + '/' + name)
        ingredient_ref.delete()


